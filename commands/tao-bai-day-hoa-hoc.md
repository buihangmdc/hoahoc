# Tạo Kế hoạch bài dạy Hóa học chuẩn 5512

Nhận `$ARGUMENTS`, gọi skill `thiet-ke-bai-day-hoa-hoc`, đọc khung mẫu tại `mau/mau-giao-an-5512.md` và tạo trọn gói Kế hoạch bài dạy (Giáo án) theo chuẩn Công văn 5512/BGDĐT-GDTrH.

## Quy tắc xử lý và mặc định:
- **Thông tin đầu vào:** Lớp, Tên bài dạy / Chủ đề, Thời lượng (số tiết), Bộ sách (mặc định Kết nối tri thức nếu không nêu).
- **Tích hợp bắt buộc:**
  - Tự động lồng ghép chỉ báo **Năng lực số (NLS)** theo Thông tư 02/2025/TT-BGDĐT.
  - Tự động tích hợp chuyên đề **Giáo dục Trí tuệ nhân tạo (AI)** cốt lõi theo Công văn 5588/BGDĐT-GDPT môn Hóa học (`AI-H10`, `AI-H11`, `AI-H12`).
- **Tiến trình dạy học:** Đầy đủ 4 hoạt động (Mở đầu, Hình thành kiến thức, Luyện tập, Vận dụng), mỗi hoạt động đủ 4 bước (Giao nhiệm vụ -> Thực hiện -> Báo cáo, thảo luận -> Kết luận, nhận định).
- **Định dạng đầu ra:** Xuất file Markdown chuẩn cấu trúc tại `dau-ra/giao-an/02-ke-hoach-bai-day-5512.md` với bảng biểu sạch và công thức/phương trình phản ứng rõ ràng để chuyển đổi trực tiếp sang file Word (.docx).