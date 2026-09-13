---
name: tao-prompt-anh-giao-duc
description: Tạo prompt ảnh giáo dục độc lập, copy-paste được cho từng cảnh, thumbnail, sơ đồ, infographic, reference sheet hoặc hình minh họa; khóa tính đúng khoa học, phong cách, nhân vật, thiết bị và bố cục. Dùng sau khi có storyboard hoặc khi người dùng yêu cầu prompt ảnh cho bài dạy/video.
---

# Tạo prompt ảnh giáo dục

> **Bước 0 — Xác định preset:** Đọc `studio-bible/PHONG-CACH-HINH-ANH.md` để biết preset đang dùng. Nếu preset là `MANABIE-2D`, đọc `studio-bible/PRESET-04-MANABIE-2D.md` và dùng template Section 9 của file đó — không dùng template mặc định bên dưới.

1. Đọc storyboard (bao gồm **Narrative Spine** và cột “Cầu nối từ cảnh trước”), preset file và quy tắc môn học. Với Hóa học, chỉ dùng công thức đã có `FORMULA-ID` và khóa biểu diễn đã duyệt.
2. Tạo một VISUAL ANCHOR dùng chung cho toàn bộ video; lặp nguyên văn anchor trong từng prompt, không viết “same as above”.
3. **Mỗi CLIP video cần 1 ảnh riêng (quan hệ 1:1 tuyệt đối):**  
   - 1 scene sư phạm dài → nhiều clip → mỗi clip cần 1 ảnh tương ứng.  
   - Ảnh mô tả **trạng thái frame CUỐI của clip đó** — đây là reference image AI tool dùng để animate.  
   - Đặt tên ảnh theo CLIP-ID chuẩn `rules/CONG-THUC-SCENE-WORD.md`: `SC0X-A`, `SC0X-B`, `SC0X-C`...  
   - Ảnh clip A là điểm bắt đầu của clip B (continuity).
4. **STORY BRIDGE — bắt buộc từ cảnh 2 trở đi:**  
   - Mỗi image prompt phải có trường `STORY BRIDGE` trong phần prompt English.  
   - STORY BRIDGE = vật thể/trạng thái visual mang từ cảnh trước sang cảnh này (ví dụ: “piston already compressed from SC01-A”).  
   - Không được để ảnh cảnh 2 trông như cảnh hoàn toàn mới không liên quan cảnh 1.
4. Với từng cảnh/clip, ghi: VISUAL ANCHOR, CLIP-ID, CONTENT (frame cuối), STAGE, PATTERN, FORMULA-ID, science lock, composition, mặt phẳng quan sát, cỡ cảnh/góc nhìn và style.
5. Tách chữ/công thức sang lớp hậu kỳ — không nhúng text vào illustration (trừ MOTION-TYPE là ngoại lệ).
6. Với `MANABIE-2D`: không có camera/lighting — thay bằng Zone (A/B), background decoration, label positions.
7. Với `HYBRID-NGUOI-THAT-3D`: xuất hai prompt/keyframe: `clean live-action plate` và `composite reference`.
8. Xuất prompt tiếng Anh; chú thích và chữ hậu kỳ bằng tiếng Việt.
9. Dùng [mẫu prompt độc lập](assets/mau-prompt-anh-standalone.md) và kiểm tra [visual lock](references/visual-lock.md).
10. Khi tạo infographic/sketchnote Hóa học, đọc [quy chuẩn infographic Hóa học](references/infographic-vat-ly-sketchnote.md); không sao chép bố cục hay chữ nguyên xi từ ảnh tham khảo.
