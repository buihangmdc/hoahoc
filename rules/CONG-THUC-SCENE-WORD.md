# CHUẨN SCENE – CLIP – SHOT – VOICE

**Phiên bản:** 2.0  
**Cập nhật:** 2026-07-14

## 1. Ba đơn vị không được trộn

- `SCENE`: một mắt xích sư phạm trong Narrative Spine, có mục tiêu và câu hỏi chuyển tiếp.
- `CLIP`: một tệp đầu ra của công cụ video, có thời lượng tối đa theo `tool-capabilities` hoặc manifest dự án.
- `SHOT`: một bố cục/góc máy liên tục. Mặc định một clip–một shot; chỉ dùng multi-shot khi công cụ và continuity cho phép.

Một scene dài có thể tách thành nhiều clip: `SC03-A`, `SC03-B`. Quan hệ kỹ thuật là một video prompt cho mỗi clip. Keyframe được tái sử dụng khi manifest ghi rõ và trạng thái khung hình phù hợp.

## 2. Công thức lập kế hoạch

```text
clip_cap = max_clip_seconds của công cụ
nếu chưa chọn công cụ: clip_cap = 9 giây, gắn ASSUMPTION

số_clip_của_scene = ceil(thời_lượng_scene / clip_cap)
tổng_clip = tổng số_clip_của_từng_scene
tổng_thời_lượng = tổng duration của clip
```

Không chia tổng thời lượng rồi gọi kết quả là “số scene”. Số scene do logic sư phạm quyết định; số clip do giới hạn kỹ thuật quyết định.

## 3. Tốc độ lời đọc

Chọn tốc độ theo mật độ nhận thức, sau đó đọc thử hoặc đo bằng TTS thực tế:

| Loại lời | Khoảng tham chiếu |
|---|---:|
| Công thức, định nghĩa mới, hướng dẫn thao tác | 90–120 từ/phút |
| Giải thích thông thường | 120–145 từ/phút |
| Chuyển ý hoặc tóm tắt quen thuộc | 140–160 từ/phút |

```text
ngân_sách_từ = (thời_lượng_scene - khoảng_nghỉ) × tốc_độ_từ_phút / 60
```

Chừa khoảng nghỉ cho quan sát hình, đọc công thức và trả lời câu hỏi. Không ép 150 từ/phút cho mọi lớp và mọi nội dung.

## 4. Ví dụ đúng cho video 60 giây

Năm scene sư phạm, bảy clip kỹ thuật với giả định `clip_cap = 9s`:

| Scene | Thời lượng | Chức năng | Clip |
|---|---:|---|---|
| SC01 | 8s | Hiện tượng và câu hỏi | SC01-A 8s |
| SC02 | 14s | Giải thích khái niệm | SC02-A 7s, SC02-B 7s |
| SC03 | 16s | Biểu diễn/công thức | SC03-A 8s, SC03-B 8s |
| SC04 | 9s | Ví dụ kiểm tra | SC04-A 9s |
| SC05 | 13s | Chốt và câu hỏi chuyển giao | SC05-A 6s, SC05-B 7s |

Tổng scene = 5; tổng clip = 7; tổng thời lượng = 60 giây.

## 5. Video dài

Không mặc định biến toàn bộ tiết học thành hàng trăm clip AI. Lập kế hoạch theo segment 3–10 phút và phối hợp:

- giáo viên/người dẫn;
- slide hoặc bảng viết;
- quay màn hình mô phỏng;
- sơ đồ tĩnh có chuyển động nhẹ;
- clip AI chọn lọc cho hiện tượng khó quay hoặc không thể quan sát trực tiếp.

Manifest phải ghi loại media, thời lượng, nguồn, chi phí dự kiến và phương án thay thế cho từng segment.

## 6. Kiểm tra bắt buộc

- Tổng duration clip khớp timeline trong dung sai đã cấu hình.
- Không clip nào vượt `max_clip_seconds` của manifest.
- Mỗi clip có `START_STATE`, `ACTION`, `END_STATE` và camera plane.
- Clip kế tiếp liên kết bằng ID trạng thái, không viết “như cảnh trước”.
- Voice không vượt ngân sách; công thức có khoảng dừng; phụ đề khớp lời thực tế.
- Giá và phiên bản công cụ chỉ được ghi trong cấu hình có ngày xác minh, không ghi thành chuẩn sư phạm.
