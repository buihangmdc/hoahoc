# Lệnh /bat-dau

## Mục đích
Hiển thị form nhập liệu tương tác để giáo viên nhập thông tin bài dạy. Đây là điểm khởi đầu mặc định của hệ thống.

## Kích hoạt
Khi người dùng gõ: `bắt đầu`, `bat dau`, `/bat-dau`, `hello`, `xin chào`, `bắt đầu thôi`, hoặc không có yêu cầu cụ thể nào khác trong tin nhắn đầu tiên của phiên làm việc.

## Quy trình

1. Render widget onboarding từ `mau/onboarding-widget.html` bằng tool `mcp__visualize__show_widget`.
2. Không hỏi thêm gì — widget đã có đủ trường thông tin.
3. Khi nhận dữ liệu từ form (qua sendPrompt), phân tích và bắt đầu tạo học liệu ngay.

## Nội dung widget
Xem file `mau/onboarding-widget.html` để lấy mã HTML đầy đủ.

## Sau khi nhận dữ liệu từ form

Dữ liệu đến dưới dạng:
```
Bài dạy — Môn: [môn] [lớp] · Chủ đề: [chủ đề] · Đầu ra: [loại] · Thời lượng: [x phút] · Hình thức: [hình thức] · Tài liệu: [tên file nếu có]
```

Xử lý:
- Xác định hồ sơ bài học từ dữ liệu trên
- Truy xuất kho tài liệu đúng lớp trong `kho-tai-lieu/`
- Nếu có tài liệu đính kèm → đọc và dùng làm nguồn chính
- Chạy đúng workflow tương ứng với loại đầu ra được chọn
- Kiểm định 3-gate trước khi bàn giao nếu đầu ra là giáo án/script
