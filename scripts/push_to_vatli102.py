import os
import sys
import json
import base64
import datetime
import urllib.request
import urllib.error

sys.stdout.reconfigure(encoding='utf-8')

def get_github_token():
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        return token
    if os.path.exists(".git/config"):
        with open(".git/config", "r", encoding="utf-8") as f:
            m = re.search(r':(ghp_[A-Za-z0-9]+)@', f.read())
            if m:
                return m.group(1)
    if os.path.exists(".token"):
        with open(".token", "r", encoding="utf-8") as f:
            return f.read().strip()
    return ""

REPO = "Vatli102/Vatli"
BRANCH = "main"
TOKEN = get_github_token()
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def api_request(endpoint, method="GET", data=None):
    url = f"https://api.github.com/repos/{REPO}/{endpoint}"
    req = urllib.request.Request(url, headers=HEADERS, method=method)
    if data is not None:
        json_bytes = json.dumps(data).encode('utf-8')
        req.add_header("Content-Type", "application/json; charset=utf-8")
        req.data = json_bytes
    try:
        with urllib.request.urlopen(req) as resp:
            resp_body = resp.read().decode('utf-8')
            return json.loads(resp_body) if resp_body else {}
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode('utf-8')
        print(f"❌ API Error [{e.code}] on {method} {url}: {err_msg}")
        raise

def main():
    print(f"=== BẮT ĐẦU PUSH HỌC LIỆU MÔN HÓA LÊN {REPO} ({BRANCH}) ===")
    
    # 1. Get current commit on main
    ref_info = api_request(f"git/refs/heads/{BRANCH}")
    latest_commit_sha = ref_info["object"]["sha"]
    print(f"1. Commit hiện tại trên main: {latest_commit_sha}")
    
    commit_info = api_request(f"git/commits/{latest_commit_sha}")
    base_tree_sha = commit_info["tree"]["sha"]
    print(f"   Base Tree SHA: {base_tree_sha}")

    # 2. Collect files from vatli102_export
    tree_items = []
    export_root = "vatli102_export"
    
    print("\n2. Đang tạo Git Blobs cho các tệp tin...")
    for root, dirs, files in os.walk(export_root):
        for f in sorted(files):
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, export_root).replace("\\", "/")
            
            # CRITICAL CHECK: Must strictly start with hoa/
            if not rel_path.startswith("hoa/"):
                raise ValueError(f"Vi phạm phạm vi bộ môn: {rel_path} không thuộc hoa/!")
            
            with open(full_path, "rb") as fp:
                file_bytes = fp.read()
            
            b64_content = base64.b64encode(file_bytes).decode('ascii')
            blob_resp = api_request("git/blobs", method="POST", data={
                "content": b64_content,
                "encoding": "base64"
            })
            blob_sha = blob_resp["sha"]
            print(f"   ✓ {rel_path:35} -> Blob SHA: {blob_sha[:10]} ({len(file_bytes):,} bytes)")
            
            tree_items.append({
                "path": rel_path,
                "mode": "100644",
                "type": "blob",
                "sha": blob_sha
            })

    # 3. Create new tree
    print(f"\n3. Đang tạo Git Tree mới với {len(tree_items)} tệp tin...")
    new_tree_resp = api_request("git/trees", method="POST", data={
        "base_tree": base_tree_sha,
        "tree": tree_items
    })
    new_tree_sha = new_tree_resp["sha"]
    print(f"   ✓ New Tree SHA: {new_tree_sha}")

    # 4. Create new commit
    print("\n4. Đang tạo Commit...")
    now_iso = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=7))).isoformat()
    author_info = {
        "name": "Bùi Thị Hằng",
        "email": "buihangmdc@users.noreply.github.com",
        "date": now_iso
    }
    commit_msg = (
        "Cập nhật Môn Hóa Học: Xuất bản Đề số 1, 2, 3 và Chuyên trang Hóa học 12 trực tuyến\n\n"
        "- Bổ sung Đề số 1: Ôn tập Chương 1, 2 và Chương 3 (đến Amine)\n"
        "- Bổ sung Đề số 2: Ôn tập tới hết Chương 3 (Mã 01)\n"
        "- Bổ sung Đề số 3: Ôn tập tới hết Chương 3 (Chuẩn cấu trúc 2026)\n"
        "- Thiết kế chuyên trang Hóa Học 12 (hoa/lop-12/) và cập nhật cổng Môn Hóa (hoa/)\n"
        "- Tích hợp đồng bộ kết quả thi vào Google Sheets giáo viên"
    )
    new_commit_resp = api_request("git/commits", method="POST", data={
        "message": commit_msg,
        "tree": new_tree_sha,
        "parents": [latest_commit_sha],
        "author": author_info,
        "committer": author_info
    })
    new_commit_sha = new_commit_resp["sha"]
    print(f"   ✓ New Commit SHA: {new_commit_sha}")

    # 5. Update branch ref
    print(f"\n5. Đang cập nhật ref refs/heads/{BRANCH}...")
    update_ref_resp = api_request(f"git/refs/heads/{BRANCH}", method="PATCH", data={
        "sha": new_commit_sha,
        "force": False
    })
    print(f"   ✓ ĐÃ PUSH THÀNH CÔNG LÊN {BRANCH}!")
    print(f"   SHA: {update_ref_resp['object']['sha']}")

if __name__ == "__main__":
    main()
