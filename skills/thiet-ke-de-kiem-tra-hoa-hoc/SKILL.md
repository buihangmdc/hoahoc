---
name: thiet-ke-de-kiem-tra-hoa-hoc
description: Thiết kế trọn gói Phiếu bài tập và Đề kiểm tra đánh giá môn Hóa học (Lớp 10, 11, 12) chuẩn CTGDPT 2018. Xuất đồng thời 01 file Word (.docx) và 01 file HTML trắc nghiệm tương tác chuẩn vatli102.com.
---

# Thiết kế Phiếu bài tập & Đề kiểm tra Hóa học

## 1. Cấu trúc chuẩn Phiếu bài tập & Đề kiểm tra cuối chương

### A. Đối với Khối 10 và Khối 11
- **Phần I: 16 câu trắc nghiệm nhiều lựa chọn** (A, B, C, D) - Suy luận lí thuyết từ cơ bản đến nâng cao.
- **Phần II: 02 câu trắc nghiệm Đúng / Sai** (mỗi câu gồm ngữ cảnh thực tế đời sống/sản xuất/thí nghiệm và 4 lệnh hỏi độc lập a, b, c, d) - Suy luận lí thuyết từ cơ bản đến nâng cao.
- **Phần III: 04 câu trắc nghiệm Trả lời ngắn** tính toán (hoặc đếm số phát biểu đúng, hoặc câu hỏi có đáp số là dạng số).
- **Phần IV: 02 câu tự luận tính toán** từ cơ bản đến nâng cao.

### B. Đối với Khối 12 (Chuẩn kỳ thi Tốt nghiệp THPT)
- **Phần I: 18 câu trắc nghiệm nhiều lựa chọn** (A, B, C, D) - Suy luận lí thuyết từ cơ bản đến nâng cao.
- **Phần II: 04 câu trắc nghiệm Đúng / Sai** (có bối cảnh thực tế) - Suy luận lí thuyết từ cơ bản đến nâng cao.
- **Phần III: 06 câu trắc nghiệm Trả lời ngắn** tính toán (hoặc đếm số phát biểu đúng, hoặc câu hỏi có đáp số là dạng số).
- **Phần IV: TUYỆT ĐỐI KHÔNG CÓ TỰ LUẬN**.

## 2. Quy cách đóng gói & Xuất bản song song (.docx & .html)

Mỗi phiếu bài tập hoặc đề kiểm tra đều bắt buộc xuất song song hai định dạng:
1. **File Word (.docx):**
   - Chứa đầy đủ tất cả các phần (kèm tự luận đối với lớp 10, 11).
   - Khổ A4, lề trên 2cm, dưới 2cm, trái 2cm, phải 1.5cm, có đánh số trang, căn lề hai bên (justified).
   - Chạy `py scripts/export_to_docx.py <input.md> <output.docx>`.
2. **File Web HTML (.html):**
   - **CHỈ CÓ TRẮC NGHIỆM (Phần I, II, III), KHÔNG CÓ TỰ LUẬN**, thiết kế để đẩy lên blog/web cho học sinh làm online trực tiếp.
   - Giao diện chuẩn theo mẫu `https://vatli102.com/Lop12/de10/index.html` (Form thông tin thí sinh, đếm thời gian, thanh tiến độ, chọn đáp án tương tác, tự động chấm điểm thang 10, barem lũy tiến Phần II, hiệu ứng pháo hoa confetti, hiển thị lời giải chi tiết, MathJax công thức hóa học chuẩn).
   - Chạy `py scripts/export_to_html_quiz.py <quiz_data.json> <output.html>`.
3. **Quy tắc tuyệt đối về định dạng đáp án:**
   - Các phương án trắc nghiệm **A, B, C, D**, các ý **a), b), c), d)** và **Đáp số:** **TUYỆT ĐỐI KHÔNG ĐƯỢC để dấu gạch đầu dòng (-)**.
   - Dấu gạch đầu dòng (-) chỉ dùng cho các ý phân cấp trong Kế hoạch bài dạy (giáo án CV 5512).

## 3. Quản lý thư mục đầu ra

- Khối 10: `dau-ra/lop-10/bai-tap/` và `dau-ra/lop-10/de-kiem-tra/`
- Khối 11: `dau-ra/lop-11/bai-tap/` và `dau-ra/lop-11/de-kiem-tra/`
- Khối 12: `dau-ra/lop-12/bai-tap/` và `dau-ra/lop-12/de-kiem-tra/`
- **MẶC ĐỊNH TỰ ĐỘNG PUSH LÊN WEB VATLI102.COM:** Mỗi khi hoàn thành tạo đề hoặc cập nhật đề, tự động thực thi script đẩy lên `vatli102.com` (repo `Vatli102/Vatli`) trong phạm vi `hoa/**`, cập nhật trang môn Hóa (`hoa/index.html`) và trang khối lớp tương ứng (`hoa/lop-<n>/index.html`), đồng thời tích hợp sẵn Google Apps Script endpoint mà không cần đợi người dùng nhắc lại.