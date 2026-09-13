# Định tuyến công cụ media

Không chọn tool theo trí nhớ, quảng cáo hoặc bảng giá đóng cứng. Đọc `config/tool-capabilities.json`, chỉ dùng mục `enabled=true`, còn hạn xác minh và có URL tài liệu chính thức.

## Tiêu chí chọn

### Ảnh/keyframe

Kiểm aspect ratio, reference image, seed/consistency, quyền dữ liệu, khả năng giữ bố cục và chính sách nội dung. Công thức/chữ khoa học thêm hậu kỳ.

### Video

Kiểm `max_clip_seconds`, image-to-video/text-to-video, camera control, first/last frame, resolution, audio, hàng đợi và cơ chế retry. Ghi tool/model thực tế vào clip manifest; không dùng một giới hạn clip phổ quát.

### TTS

Kiểm tiếng Việt, quyền giọng, SSML/nhịp nghỉ, đơn vị tính, sample rate và khả năng tái tạo. Không clone giọng nếu chưa có đồng ý rõ ràng.

### Hậu kỳ

Ưu tiên công cụ có thể kiểm soát deterministically cho ghép, phụ đề, loudness và checksum. Lưu command/config đã dùng để tái lập.

## Quyết định mode

- Cần continuity nhân vật/dụng cụ: ưu tiên image-to-video với keyframe đã duyệt.
- Cảnh môi trường không cần identity: có thể text-to-video nếu capability cho phép.
- Cần chữ/công thức: tạo lớp hậu kỳ, không giao model video tự viết.
- Tool chưa xác minh hoặc capability hết hạn: `PLAN_ONLY`, không render.

Chạy `python scripts/validate_tool_capabilities.py config/tool-capabilities.json` trước khi đưa ID tool vào production manifest.
