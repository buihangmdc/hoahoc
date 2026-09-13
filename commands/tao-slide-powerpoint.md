# Tạo Slide PowerPoint bài giảng (Chuẩn 5512)

Nhận `$ARGUMENTS` (Tên bài học, Khối lớp, Số tiết), AI sẽ:
1. Đọc kế hoạch bài dạy tương ứng tại `dau-ra/giao-an/` hoặc tạo mới kịch bản slide theo `mau/mau-slide-powerpoint.md`.
2. Xuất file kịch bản slide vào `dau-ra/giao-an/04-kich-ban-slide.md`.
3. Chạy lệnh xuất bản `.pptx`:
   `py scripts/export_to_pptx.py dau-ra/giao-an/04-kich-ban-slide.md dau-ra/giao-an/04-bai-giang-dien-tu.pptx`