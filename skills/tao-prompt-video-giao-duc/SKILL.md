---
name: tao-prompt-video-giao-duc
description: Tạo prompt video giáo dục độc lập theo từng clip cho Kling, Runway, Veo, Sora hoặc công cụ tương đương; gồm timeline, camera, blocking, chuyển động, performance, continuity, voice-over, âm thanh, chữ hậu kỳ và negative prompt. Dùng sau storyboard hoặc khi cần biến ảnh tham chiếu thành video bài giảng.
---

# Tạo prompt video giáo dục

> **GIỚI HẠN KỸ THUẬT:** Lấy `max_clip_seconds` từ manifest năng lực công cụ. Nếu chưa chọn công cụ, dùng 9 giây như giả định lập kế hoạch có ghi nhãn. Scene dài hơn giới hạn phải chia thành nhiều CLIP theo `rules/CONG-THUC-SCENE-WORD.md`, đặt ID dạng `SC0X-A/B/C` (không dùng chữ đầy đủ "SCENE" trong ID clip).

> **QUY TẮC BẮT BUỘC:** `1 clip = 1 clip manifest = 1 VIDEO PROMPT`. Với image-to-video, clip phải có keyframe tham chiếu; keyframe có thể tái sử dụng khi trạng thái phù hợp và manifest ghi rõ, không ép số ảnh bằng số clip.

> **QUY TẮC CONTINUITY KHI CHIA CLIP:**  
> Clip B phải bắt đầu bằng: `START FROM END STATE OF [SC0X-A].`  
> Mô tả ngắn trạng thái màn hình đầu clip (những gì đã có sẵn).  
> Không animate lại những gì đã xuất hiện ở clip trước.

> **QUY TẮC NARRATIVE BRIDGE — VOICE-OVER:**  
> Câu đầu tiên của Voice-over script mỗi cảnh (từ SC02 trở đi) PHẢI là câu bridge — nhắc lại hoặc trả lời cảnh trước.  
> Dùng một trong 4 kiểu: Trả lời / Tiếp nối / So sánh / Hệ quả (xem SKILL.md kịch bản).  
> Câu cuối (trừ cảnh kết) PHẢI đặt câu hỏi/hook cho cảnh tiếp.  
> Không được bắt đầu câu đầu bằng tên khái niệm lạnh ngắt như "Phản ứng este hóa là…" mà không có cầu nối từ cảnh trước.

> **Khi dùng preset 2D phẳng:** Đọc `studio-bible/PRESET-04-MANABIE-2D.md` như tệp tương thích cũ, nhưng dùng định danh `EDU-FLAT-2D`; không sao chép logo, watermark hay nhận diện thương hiệu. CONTINUITY ANCHOR khai báo “original flat 2D educational animation, static frame, no camera movement”.

1. Đọc storyboard, continuity bible và image prompt đã duyệt để lấy VISUAL ANCHOR. Với Hóa học, đọc [ma trận góc máy và khóa công thức](references/goc-may-va-khoa-cong-thuc-vat-ly.md).
2. **Sao chép nguyên văn VISUAL ANCHOR từ image prompt vào đầu CONTINUITY ANCHOR của video prompt** — không viết lại, không tóm tắt.
3. Khai báo `Reference image: [SC0X-A/B/C]` (CLIP-ID theo `rules/CONG-THUC-SCENE-WORD.md`) ở dòng đầu tiên — bắt buộc, không để trống.
4. Khai báo `START STATE` (frame 0): mô tả những gì đã có sẵn trên màn hình từ ảnh tham chiếu — những phần này không animate lại.
5. Chỉ mô tả **chuyển động và thay đổi** xảy ra trong clip này; không mô tả lại những gì đã có trong ảnh.
6. Mỗi prompt là một clip liên tục không vượt `max_clip_seconds` của manifest; không nhét nhiều sự kiện vào một prompt.
7. Mô tả theo timeline: opening state → animation sequence → science freeze-frame → end state.
8. Khai báo `END STATE` (frame cuối): trạng thái màn hình khi clip kết thúc — phải khớp với CONTENT trong ảnh reference.
9. Khóa FORMULA-ID/CONCEPT-ID, hệ quy chiếu, mặt phẳng quan sát, hướng chuyển động, số lượng vật thể, trạng thái dụng cụ và biến thiên hóa học. Cấm vượt trục hành động khi việc đó đảo chiều biểu kiến.
10. Chỉ một người nói tại một thời điểm; người còn lại giữ miệng đóng và phản ứng không lời.
11. Với hybrid, tạo prompt chuyển động cho live-action plate và đặc tả overlay 3D/AR riêng; không giao model tự sinh chữ khoa học.
12. Dùng [mẫu prompt video](assets/mau-video-standalone.md) và [quy tắc công cụ](references/tool-routing.md).
13. Công thức, đơn vị, đồ thị, vectơ và nhãn khoa học chỉ xuất hiện ở lớp hậu kỳ đã kiểm định; không giao model video tự viết.
