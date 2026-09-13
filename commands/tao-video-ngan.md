# Command: /tao-video-ngan

Tạo gói tiền kỳ video giáo dục ngắn theo `workflows/07-video-ngan-fast.md`.

## Cách dùng

```text
/tao-video-ngan <môn> <lớp> <chủ đề> [thời lượng] [phong cách] [công cụ đích]
```

Nếu thiếu dữ liệu, xác định bằng giả định có ghi nhãn; chỉ hỏi khi lựa chọn làm thay đổi đáng kể nội dung hoặc chi phí.

## Bắt buộc

1. Với Vật lý, dùng `thiet-ke-bai-day-vat-ly` và nguồn đúng lớp/chủ đề.
2. Dựng Narrative Spine trước storyboard.
3. Phân biệt scene sư phạm với clip kỹ thuật; một scene có thể gồm nhiều clip.
4. Lấy `max_clip_seconds` từ công cụ đích. Nếu chưa có, dùng 9 giây như giả định, không gọi là giới hạn phổ quát.
5. Một video prompt cho mỗi clip; keyframe tái sử dụng phải được ghi trong manifest.
6. Tách voice, phụ đề và chữ hậu kỳ khỏi prompt video.
7. Chạy 3 gate và validator máy trước bàn giao.

Không tuyên bố đã có ảnh, audio hoặc video khi mới chỉ tạo prompt/script.
