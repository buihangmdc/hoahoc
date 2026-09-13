# VIDEO PROMPT [CLIP-ID: SC0X-A] ← phải khớp với IMAGE PROMPT cùng CLIP-ID

> CLIP-ID theo định dạng `SC0X-A/B/C` (xem `rules/CONG-THUC-SCENE-WORD.md`). Không dùng "SHOT-ID" hay "SCENE-ID" cho tên file/tiêu đề prompt video — SHOT là góc máy bên trong một clip, không phải ID của clip.

## ⚠ Thiết lập bắt buộc (điền TRƯỚC khi viết prompt)

- **Reference image:** [CLIP-ID: SC0X-A] — tên/đường dẫn image prompt đã tạo  
- **Mode:** image-to-video  
- **Duration:** [x] giây  
- **Aspect ratio:** [16:9 / 9:16 / 1:1]  
- **Tool ID:** [ID `enabled=true` từ `config/tool-capabilities.json`]
- **FORMULA-ID / CONCEPT-ID:** [ID đã kiểm định]
- **View plane / positive axis:** [mặt phẳng và chiều dương]
- **Axis-crossing rule:** [cấm vượt trục / shot chuyển tiếp được duyệt]

---

## ① PROMPT GỬI CHO AI VIDEO TOOL — English standalone
> Chỉ copy phần này gửi vào Kling / Runway / Veo / Sora. Không có voice, không có chữ.

`[CONTINUITY ANCHOR — sao chép NGUYÊN VĂN VISUAL ANCHOR từ image prompt tương ứng, không tóm tắt]. STORY BRIDGE: [vật thể/trạng thái mang qua từ clip trước — ví dụ: "piston already compressed from SC01-A, begin from that compressed state"]. One continuous shot, duration [x] seconds. ANIMATE FROM REFERENCE IMAGE: describe only motion and changes, not static elements already in the image. OPENING 0:00–0:02: [trạng thái ban đầu — khớp với ảnh, kế thừa trạng thái cuối clip trước]. CORE 0:02–0:05: [chuyển động / hiện tượng vật lý chính]. SCIENCE FREEZE-FRAME 0:05–0:07: [frame phải nhìn rõ quan hệ theo FORMULA-ID/CONCEPT-ID để giáo viên duyệt]. CLOSING 0:07–0:08: [hold cuối — để lại visual hook cho clip tiếp]. CAMERA GEOMETRY: [shot, lens, view plane, height, angle, movement, no axis crossing]. REFERENCE AXIS: [chiều dương, hướng vào/ra mặt phẳng]. MOTION: [hướng, tốc độ định tính/định lượng, số lượng vật thể khóa cứng]. SCIENCE ACCURACY LOCK [ID]: [điều kiện và quan hệ không được vi phạm]. SOUND: [ambient / SFX / music — không có giọng người]. No speech, no voice, no text, no formulas, no arrows, no subtitles, no logo, no watermark.`

---

## Negative prompt
`scientifically impossible motion, wrong force direction, changing object count, apparatus morphing, character inconsistency, costume change, location change, lighting change, flicker, jump cut, camera shake, speech, voice, narration, text, subtitles, logo, watermark`

---

## ② VOICE-OVER SCRIPT — Gửi riêng cho TTS / thu âm
> **KHÔNG đưa phần này vào AI video tool.** Dùng để: gửi FPT.AI / ElevenLabs / Zalo TTS sinh file .mp3, hoặc đọc thật khi thu âm.

### Câu mở đầu (NARRATIVE BRIDGE — bắt buộc)
> Câu đầu tiên PHẢI nối từ cảnh trước. Chọn một trong ba kiểu:
> - **Kiểu trả lời:** *"Vừa rồi chúng ta thấy [X từ cảnh trước] — lý do là..."*
> - **Kiểu tiếp nối:** *"Tiếp theo, hãy xem điều đó có nghĩa gì khi..."*
> - **Kiểu so sánh:** *"Tương tự như [X cảnh trước], ở đây..."*

**Câu bridge:** [Viết câu nối — IN HOA phần nhấn mạnh, dấu / là chỗ nghỉ lấy hơi]

### Nội dung chính
[Tiếp sau câu bridge — nội dung đọc cho clip này, vừa thời lượng [x] giây]

### Câu kết / hook sang cảnh sau (nếu không phải cảnh cuối)
> Câu cuối nên đặt câu hỏi hoặc gợi sự tò mò cho cảnh tiếp.
> Ví dụ: *"Vậy khi nhiệt độ tăng, áp suất sẽ thay đổi như thế nào?"*

**Câu hook:** [Viết câu kết/câu hỏi mở]

**Giọng đọc:** [Nữ miền Nam phổ thông / Nam miền Bắc / trung tính]  
**Tốc độ:** [0.9× bình thường / 1.0× / 1.1×]

---

## ③ HẬU KỲ — Ghép trong CapCut / Premiere / DaVinci
> Thực hiện SAU KHI có file .mp4 từ AI tool và file .mp3 từ TTS.

- Ghép audio: căn [x] giây voice với timeline video
- Label tiếng Việt thêm sau (hậu kỳ, không trong AI prompt):
- Công thức / ký hiệu thêm sau:
- Vectơ / trục / đồ thị thêm sau:
- Timecode science freeze-frame:
- Kiểm tra công thức, đơn vị, hướng và làm tròn:
- Subtitle (nếu cần):
- Đồ họa overlay / chú thích thêm:
- **Transition sang clip tiếp:** [cross-dissolve Xs / cut / fade]
