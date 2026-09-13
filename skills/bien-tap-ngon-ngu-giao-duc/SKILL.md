---
name: bien-tap-ngon-ngu-giao-duc
description: Biên tập tiếng Việt cho giáo án, phiếu học tập, câu hỏi, lời giảng, kịch bản và phụ đề; bảo toàn nội dung khoa học, chuẩn hóa thuật ngữ, điều chỉnh độ khó theo lớp, tối ưu câu đọc thành tiếng và phát hiện diễn đạt mơ hồ hoặc dẫn dắt sai. Dùng trước khi bàn giao nội dung cho giáo viên/học sinh hoặc trước GATE 2 của video giáo dục.
---

# Biên tập ngôn ngữ giáo dục

## Quy trình

1. Xác định người đọc/nghe, lớp, mục đích, kênh và thời lượng.
2. Khóa danh sách thuật ngữ, ký hiệu, FORMULA-ID và câu không được đổi nghĩa.
3. Biên tập theo ba lượt: đúng nghĩa → dễ hiểu → đọc thành tiếng.
4. Đọc [chuẩn biên tập](references/chuan-bien-tap.md) và áp dụng checklist phù hợp đầu ra.
5. So lại mọi con số, dấu, đơn vị, phủ định và quan hệ nguyên nhân–kết quả với bản nguồn.
6. Xuất bản sạch và bảng thay đổi đối với chỗ sửa có thể ảnh hưởng chuyên môn.

## Khóa bắt buộc

- Không “làm hay” bằng cách thêm fact, ví dụ, trích dẫn hoặc kết quả không có nguồn.
- Không thay thuật ngữ chính xác bằng từ đời thường nếu làm sai nghĩa; giải thích sau thuật ngữ ở lần xuất hiện đầu.
- Mỗi câu hỏi chỉ kiểm tra điều đã dạy hoặc nguồn cho phép; tránh mẹo ngôn ngữ ngoài mục tiêu.
- Công thức có bản viết, cách đọc và quy ước dấu nhất quán.
- Lời đọc dành khoảng nghỉ cho công thức, hình và câu hỏi; không ép tốc độ bằng cách bỏ điều kiện khoa học.
- Phụ đề bám lời thực tế, chia dòng theo cụm nghĩa, không tách số khỏi đơn vị.

## Đầu ra

Ghi `EDIT-PASS` gồm đối tượng, mức lớp, thuật ngữ khóa, lỗi đã sửa, câu cần chuyên gia xác nhận và trạng thái `PASS/FAIL`. Nếu còn câu mơ hồ có thể đổi kết luận khoa học, trả `FAIL` cho lượt biên tập và chuyển lại GATE 1.
