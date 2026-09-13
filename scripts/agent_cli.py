import os
import sys
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

from pathlib import Path
from google import genai

KEY_FILE = Path("api_key.txt")

# Đọc hoặc lưu API Key để không phải nhập lại
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key and KEY_FILE.exists():
    api_key = KEY_FILE.read_text(encoding="utf-8").strip()

if not api_key:
    print("=" * 60)
    print("CHƯA CÓ API KEY!")
    api_key = input("Vui lòng dán Gemini API Key của bạn vào đây: ").strip()
    if api_key:
        KEY_FILE.write_text(api_key, encoding="utf-8")
        print("Đã lưu API Key thành công cho các lần sau!\n")

client = genai.Client(api_key=api_key)

# Đọc cấu hình hệ thống từ CLAUDE.md nếu có
system_prompt = ""
claude_md = Path("CLAUDE.md")
if claude_md.exists():
    system_prompt = claude_md.read_text(encoding="utf-8")

print("=" * 60)
print("  HỆ THỐNG AI AGENT HỖ TRỢ GIẢNG DẠY HÓA HỌC (CLI)")
print("=" * 60)
print("Nhập yêu cầu bài giảng / đề thi của bạn (hoặc gõ 'exit' để thoát).\n")

try:
    chat = client.chats.create(
        model="gemini-2.5-flash",
        config={"system_instruction": system_prompt} if system_prompt else None
    )
except Exception:
    # Dự phòng nếu model 2.5 chưa khả dụng thì chuyển sang 1.5-flash
    chat = client.chats.create(
        model="gemini-1.5-flash",
        config={"system_instruction": system_prompt} if system_prompt else None
    )

while True:
    try:
        user_input = input("\n[Bạn] > ").strip()
        if not user_input:
            continue
        if user_input.lower() in ["exit", "quit"]:
            print("Đã thoát chương trình.")
            break
        
        print("\n[AI Agent đang xử lý...]\n")
        response = chat.send_message(user_input)
        print(response.text)
        
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"Lỗi: {e}")