# Visual lock

Khóa nhất quán: nhân vật, trang phục, màu nhận diện, đạo cụ, bố cục lớp học/phòng thí nghiệm, quy ước màu vectơ, loại ống kính, bảng màu và phong cách render. Từng prompt phải chứa đủ khóa cần thiết để chạy độc lập.

## Khóa riêng theo preset

### MANABIE-2D
- Background Zone (A=kem/B=xanh) phải nhất quán trong cùng một segment; đổi zone = đổi segment.
- Logo watermark góc phải trên: **luôn để trống 80×80px** — ghi rõ trong mọi prompt.
- Màu cuộn dây, nam châm, galvanometer, tay người phải khớp hệ màu trong `PRESET-04-MANABIE-2D.md`.
- Không có lighting/shadow phức tạp — chỉ drop shadow nhẹ trên object chính.
- Không có camera movement trong video prompt.

## Quy tắc ghép cặp ảnh–video

- Mỗi IMAGE PROMPT là **keyframe tĩnh** cho một cảnh.
- VIDEO PROMPT tương ứng **bắt đầu từ đúng keyframe đó** (image-to-video).
- VISUAL ANCHOR trong image prompt = CONTINUITY ANCHOR trong video prompt — **sao chép nguyên văn**, không paraphrase.
- Số lượng cặp ảnh–video phải bằng nhau; không tạo video prompt cho cảnh chưa có ảnh.

