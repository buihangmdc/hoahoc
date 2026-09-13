# Tạo Kế hoạch Chuyên môn & Kế hoạch Giáo viên Hóa học (Chuẩn 5512)

Nhận `$ARGUMENTS` (bao gồm: Tên trường, Tổ chuyên môn [Tổ Hóa học / Khoa học tự nhiên], Tên giáo viên, Khối lớp giảng dạy, Bộ sách), gọi skill `lap-ke-hoach-chuyen-mon` để tự động lập bảng phân phối chương trình, kế hoạch tổ chuyên môn và kế hoạch giáo dục cá nhân môn Hóa học.

## Quy tắc xử lý mặc định:
- Đọc file mẫu chuẩn tại `mau/mau-ke-hoach-chuyen-mon-5512.md`.
- Phân bổ đủ 35 tuần thực học (Học kỳ I: 18 tuần; Học kỳ II: 17 tuần) theo khung PPCT môn Hóa học CTGDPT 2018 (70 tiết/năm lớp 10, 11, 12; cộng 35 tiết chuyên đề học tập nếu có).
- Cố định lịch Kiểm tra định kỳ: Giữa kỳ I (Tuần 9), Cuối kỳ I (Tuần 18), Giữa kỳ II (Tuần 27), Cuối kỳ II (Tuần 35).
- Tự động lồng ghép mã Năng lực số (NLS) và Trí tuệ nhân tạo (AI - `AI-H10`, `AI-H11`, `AI-H12`) vào cột "Thiết bị dạy học / Tích hợp" đối với các bài có thí nghiệm ảo (PhET), phần mềm vẽ công thức phân tử (MolView, ChemSketch) hoặc mô phỏng.
- Xuất file kết quả vào thư mục `dau-ra/ke-hoach-chuyen-mon/`.