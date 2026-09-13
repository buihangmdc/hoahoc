# WF-07 — VIDEO NGẮN NHANH, ĐÚNG VÀ KIỂM ĐƯỢC

**Kích hoạt:** `/tao-video-ngan`  
**Đầu ra:** gói tiền kỳ; không tuyên bố đã tạo media nếu chưa có tệp thực.

## 1. Hồ sơ đầu vào

Xác định môn, lớp, chủ đề, đối tượng, mục tiêu, thời lượng, tỉ lệ khung hình, phong cách và công cụ đích. Nếu chưa chọn công cụ, ghi `max_clip_seconds = 9` là giả định lập kế hoạch.

Với Vật lý, bắt buộc nạp `thiet-ke-bai-day-vat-ly`, nguồn đúng lớp/chủ đề và formula ledger.

## 2. Khóa nội dung

1. Tạo source map và knowledge brief.
2. Lập Narrative Spine theo chuỗi `hiện tượng → câu hỏi → mô hình/nguyên lí → kiểm tra bằng ví dụ → chốt`.
3. Mỗi scene có mục tiêu, kiến thức đầu vào, nội dung mới và câu hỏi mở ra scene kế tiếp.
4. Chạy GATE 1 trước khi tạo prompt hình/video.

## 3. Tách scene và clip

- Scene do logic sư phạm quyết định, thường 4–6 scene cho 60 giây.
- Mỗi scene tách thành một hoặc nhiều clip theo `rules/CONG-THUC-SCENE-WORD.md`.
- Một video prompt ứng với một clip. Keyframe có thể dùng riêng hoặc tái sử dụng nếu manifest ghi rõ.
- Mỗi clip có ID, duration, camera plane, start state, action, end state và liên kết trạng thái.

Ví dụ 60 giây với `max_clip_seconds = 9`: 5 scene sư phạm có thể tách thành 7 clip kỹ thuật; không ép 5 scene thành 5 clip.

## 4. Viết lời và hình

1. Viết voice theo ngân sách tốc độ phù hợp mật độ kiến thức; dành khoảng nghỉ cho công thức và quan sát.
2. Câu đầu scene 2+ phải nối logic với scene trước; câu cuối mở câu hỏi cho scene sau nếu phù hợp.
3. Tạo storyboard theo clip manifest.
4. Tạo prompt ảnh/keyframe độc lập; không viết “như trên”.
5. Tạo prompt video theo từng clip, tách voice và chữ hậu kỳ khỏi prompt chuyển động.
6. Tạo phụ đề từ voice đã khóa, không từ bản nháp.

## 5. Gói đầu ra

```text
01-HO-SO.md
02-NGUON-SU-DUNG.md
03-KNOWLEDGE-BRIEF.md
04-FORMULA-LEDGER.md        # khi có công thức/đại lượng
05-NARRATIVE-SPINE.md
06-SCRIPT-VOICE.md
07-STORYBOARD.md
08-CLIP-MANIFEST.json
09-IMAGE-PROMPTS.md
10-VIDEO-PROMPTS.md
11-SUBTITLES.srt
12-VALIDATION-REPORT.md
validation-report.json
```

Chỉ tạo những tệp thuộc phạm vi yêu cầu, nhưng manifest và báo cáo phải phản ánh trung thực tệp nào `READY`, `INCOMPLETE` hoặc `NOT_REQUESTED`.

## 6. Cổng bàn giao

- GATE 1: khoa học và nguồn.
- GATE 2: sư phạm, ngôn ngữ, khả năng tiếp cận và an toàn.
- GATE 3: thời lượng, manifest, continuity, prompt độc lập và trạng thái tệp.
- Chạy `python scripts/validate_package.py <thu-muc> --mode strict`.
- Chỉ bàn giao với `PASS` hoặc `PASS_WITH_NOTES`; không đổi tên `INCOMPLETE` thành `PASS`.
