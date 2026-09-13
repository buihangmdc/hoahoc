---
name: dong-goi-video-bai-giang
description: Điều phối tự động toàn bộ dây chuyền từ tài liệu giáo viên đến gói sản xuất video bài giảng gồm source map, knowledge brief, kịch bản, storyboard, prompt ảnh, prompt video, voice-over, thumbnail, phụ đề và báo cáo kiểm định. Dùng khi người dùng yêu cầu “làm full”, “tài liệu thành video”, “auto”, hoặc gói production giáo dục hoàn chỉnh.
---

# Đóng gói video bài giảng

## Pipeline bắt buộc

1. Gọi `doc-tai-lieu-giao-duc` để tạo manifest, source map và knowledge brief.
2. Gọi skill bộ môn, với Hóa học là `thiet-ke-bai-day-hoa-hoc`, để kiểm định nội dung và mục tiêu.
3. Gọi `viet-kich-ban-video-giao-duc` để tạo script và storyboard.
4. Gọi `bien-tap-ngon-ngu-giao-duc` để khóa thuật ngữ, lời đọc và phụ đề; khóa continuity bible của dự án.
5. Gọi `tao-prompt-anh-giao-duc` cho thumbnail, keyframe và từng cảnh.
6. Gọi `tao-prompt-video-giao-duc` cho từng shot.
7. Chạy kiểm định 3-gate theo `rules/VALIDATION-FRAMEWORK.md`:
   - GATE 1 (khoa học): agent `kiem-dinh-hoa-hoc-chuan` → đối chiếu thứ tự nguồn trong framework, không dùng một Knowledge Base duy nhất
   - GATE 2 (sư phạm): agent `kiem-dinh-su-pham` + skill `kiem-dinh-su-pham-giao-duc` → rubric, hiểu lầm, đánh giá, ngôn ngữ, khả năng tiếp cận và an toàn
   - GATE 3 (quy trình): agent `quan-ly-san-xuat` → kiểm continuity, thời lượng, prompt độc lập
   - BLOCKER bất kỳ → dừng, phải sửa trước khi xuất.
8. Xuất theo [production package](references/production-package.md).
9. Chạy `python scripts/validate_package.py <thu-muc-goi> --mode strict`; validator máy bổ sung, không thay thế duyệt chuyên môn.

Không dừng ở outline nếu người dùng yêu cầu full production. Mọi prompt phải độc lập; không dùng “như trên”.
