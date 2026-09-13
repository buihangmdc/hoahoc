---
name: thiet-ke-bai-day-hoa-hoc
description: Thiết kế trọn gói Kế hoạch bài dạy (Giáo án) môn Hóa học cấp THPT chuẩn Công văn 5512/BGDĐT-GDTrH, tuân thủ nghiêm ngặt kế hoạch dạy học người dùng, SGK, A4, căn lề và xuất dữ liệu tương thích chuyển đổi Word (.docx).
---

# Thiết kế bài dạy Hóa học

## 1. Lập hồ sơ yêu cầu bài dạy & Định tuyến tri thức

Xác định thông tin đầu vào:
- **Thông tin bài học:** Môn Hóa học, Khối lớp (10, 11, 12), Tên bài học / Chủ đề, Thời lượng (số tiết), Bộ sách giáo khoa.
- **Quy tắc bất biến về Mục tiêu, NLS và AI:**
  - Tiết, Yêu cầu cần đạt (YCCĐ), Năng lực số (NLS), Năng lực AI, Thiết bị dạy học: **PHẢI bám sát Kế hoạch dạy học trong tài liệu người dùng** (`kho-tai-lieu/hoa-hoc/lop-<n>/tai-lieu-nguoi-dung/Ke_hoach_day_hoc...pdf`).
  - **TUYỆT ĐỐI KHÔNG ĐƯỢC sáng tạo thêm bất cứ năng lực số hay AI nào so với kế hoạch người dùng đã cung cấp.**
  - Nội dung bài dạy: Bám sát sách giáo khoa (SGK).
  - Có hoạt động trò chơi khởi động phù hợp với từng bài học.
  - Tính toán thời gian dạy học hợp lý trên lớp. Nếu không đủ thời gian thì giao nhiệm vụ về nhà cho học sinh thực hiện.
  - Các hoạt động giáo viên có thể thực hiện được trong điều kiện thực tế lớp học. Ngôn ngữ phù hợp với học sinh THPT từng khối lớp.

## 2. Form mẫu & Quy cách trình bày

- **Mẫu form chuẩn:** Giống mẫu `tài liệu người dùng > hóa học 10 > bài 1 thành phần nguyên tử` (`kho-tai-lieu/hoa-hoc/lop-10/tai-lieu-nguoi-dung/2. Bài 1. thành phần nguyên tử.pdf`).
- **Quy cách trang in & Font chữ:**
  - Khổ giấy: **A4** (không dùng Letter).
  - Có **đánh số trang** ở giữa chân trang (Footer).
  - Căn lề chuẩn: **Trên 2.0 cm, Dưới 2.0 cm, Trái 2.0 cm, Phải 1.5 cm**.
  - Căn lề đoạn văn: **Căn lề hai bên (Justified)**.
  - Phân cấp ý: Dùng **gạch đầu dòng (-)** ở các ý, **KHÔNG dùng chấm tròn (•)**.
  - Các đề mục: **KHÔNG để gạch đầu dòng**.
  - Ký tự toán học và công thức hóa học: Chuẩn xác, không bị lỗi font hay cú pháp.

## 3. Quy chuẩn tiến trình sư phạm (Công văn 5512)

Mỗi hoạt động dạy học bắt buộc tổ chức đầy đủ theo quy trình 4 bước:
1. **Bước 1: Giao nhiệm vụ học tập** (Rõ mục tiêu, câu hỏi, phiếu học tập hoặc lệnh thao tác).
2. **Bước 2: Thực hiện nhiệm vụ** (Học sinh làm việc độc lập hoặc hợp tác nhóm; giáo viên quan sát, định hướng).
3. **Bước 3: Báo cáo, thảo luận** (Đại diện trình bày kết quả, đối chiếu chéo giữa các nhóm).
4. **Bước 4: Kết luận, nhận định** (Giáo viên chuẩn hóa kiến thức khoa học, nhận xét quá trình).

## 4. Gói bàn giao mặc định

Toàn bộ gói sản phẩm xuất vào thư mục `dau-ra/lop-<n>/giao-an/`:
1. `ke-hoach-bai-day-5512.md`: Giáo án chi tiết chuẩn cấu trúc 5512.
2. Chạy `py scripts/export_to_docx.py <input.md> <output.docx>` để xuất file Word `.docx` hoàn chỉnh đúng quy chuẩn khổ A4, căn lề và đánh số trang.