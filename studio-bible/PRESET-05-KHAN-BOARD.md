# PRESET 05 — ✏️ Viết Tay
> **Tên dễ nhớ:** `Viết Tay`
> **ID sản xuất:** `STEP-WHITEBOARD`
> **Trigger:** "viết tay", "whiteboard", "bảng trắng", "vẽ tay từng bước", "giải bài step by step", "chứng minh công thức"

---

## 1. Định nghĩa phong cách

**STEP-WHITEBOARD** là phong cách **whiteboard/blackboard animation nguyên bản** — bàn tay cầm bút vẽ sơ đồ và viết công thức trực tiếp theo nhịp giải thích. Sức mạnh nằm ở sự tiệm tiến: người xem thấy tư duy hình thành từng bước.

Chính sách nguyên bản: không sao chép nét chữ, bố cục, giọng kể hoặc nhận diện của giáo viên/kênh cụ thể.

---

## 2. Hệ màu (Color System)

### Phiên bản A — Bảng trắng (White Board)
| Token | Hex | Dùng cho |
|-------|-----|----------|
| `bg-white` | `#F5F5F0` | Nền bảng trắng (off-white nhẹ, không chói) |
| `ink-main` | `#1A1A1A` | Chữ viết tay, sơ đồ chính |
| `highlight-yellow` | `#FFD600` | Highlight marker vàng — nhấn khái niệm chính |
| `highlight-blue` | `#2979FF` | Màu viết vector, vận tốc |
| `highlight-red` | `#E53935` | Màu viết lực, năng lượng, chú ý |
| `highlight-green` | `#2E7D32` | Kết quả, đáp số, điều kiện |
| `hand-skin` | `#F4A464` | Bàn tay người viết |

### Phiên bản B — Bảng đen (Black Board)
| Token | Hex | Dùng cho |
|-------|-----|----------|
| `bg-blackboard` | `#1C2833` | Nền bảng đen (không đen tuyền, hơi xanh navy) |
| `chalk-white` | `#F0EDE0` | Phấn trắng chính |
| `chalk-yellow` | `#F9E04B` | Phấn vàng — highlight |
| `chalk-blue` | `#5DADE2` | Phấn xanh — vector, vận tốc |
| `chalk-red` | `#EC7063` | Phấn đỏ — lực, năng lượng |
| `chalk-green` | `#58D68D` | Phấn xanh lá — kết quả |

> Mặc định dùng **Phiên bản A (trắng)** cho Vật lý THPT. Dùng phiên bản B khi muốn cảm giác "lớp học truyền thống".

---

## 3. Visual Anchor chuẩn

```
[STEP-WHITEBOARD VISUAL ANCHOR: Original whiteboard animation on clean off-white #F5F5F0 background. 
A human hand holding a black marker appears from the right edge. Handwriting style: 
clean printed text, not cursive. Diagrams drawn with straight lines and smooth curves. 
Color coding: black for main content, red #E53935 for forces/energy, blue #2979FF for 
velocity/vectors, green #2E7D32 for results. Yellow highlighter #FFD600 for key terms. 
No decorative elements. No background patterns. Minimal and focused.]
```

---

## 4. Illustration Elements

### Sơ đồ vật lý (Physics Diagrams)
```
Vẽ tay, nét đơn giản, không cần hoàn hảo — nét không đều là intentional
- Vật thể: hình chữ nhật hoặc hình vuông, label chữ viết tay bên cạnh
- Vector: mũi tên thẳng, đầu tam giác rõ, label tên + độ lớn
- Đường dốc, mặt phẳng: đường thẳng có góc, label góc α
- Lò xo: hình zigzag đơn giản
- Đồng hồ/đồng hồ: vẽ đơn giản không chi tiết
- Trục tọa độ: 2 mũi tên vuông góc, label x và y
- Đồ thị: vẽ trực tiếp trên lưới hoặc trên 2 trục
```

### Công thức (Formulas)
```
- Viết từng ký tự, từng cụm theo nhịp giải thích
- Đánh số từng bước: (1), (2), (3)...
- Dùng → để chỉ suy ra
- Box quanh kết quả cuối
- Gạch chân hoặc box vàng cho công thức quan trọng
- Đơn vị trong ngoặc vuông: [m/s], [N], [J]
```

---

## 5. Quy tắc Animation

### Timing
| Loại | Duration | Ghi chú |
|---|---|---|
| Tay vào frame | 0.3s | Slide từ phải |
| Vẽ đường thẳng | 0.3–0.5s/cm | Tốc độ bút đều |
| Viết chữ | 0.08s/ký tự | Không quá nhanh |
| Highlight marker | 0.4s | Sweep ngang |
| Box quanh kết quả | 0.5s | Vẽ vòng ngoài |
| Xóa (erase) | 0.3s | Sweep ngang |
| Tay rút khỏi frame | 0.2s | Slide ra phải |

### Nguyên tắc motion
- **Tay luôn hiện khi đang viết/vẽ** — rút tay ra khi dừng lại giải thích
- Vẽ từ **trái sang phải**, từ **trên xuống dưới**
- Không teleport — mọi thứ phải được vẽ, không pop-in
- Khi highlight: tay cầm marker vàng, sweep 1 lần qua chữ
- Khi xóa sai: tay cầm khăn/eraser, sweep rõ ràng rồi viết lại

### Camera
- **STATIC FRAME** — không pan, không zoom
- Bố cục chia 2/3 bảng cho bước hiện tại, 1/3 cho tóm tắt đã qua
- Nếu cần thêm chỗ: wipe sang frame mới (không zoom out)

---

## 6. Cấu trúc Scene chuẩn

```
BEAT 1 — Đặt vấn đề (0:00–0:05):
  Tay viết tiêu đề bước / câu hỏi cần giải.
  Ví dụ: "Tính gia tốc của vật?"

BEAT 2 — Vẽ sơ đồ (0:05–0:15):
  Tay vẽ hình minh họa (vật, lực, trục).
  Label từng phần ngay khi vẽ xong.

BEAT 3 — Viết công thức (0:15–0:25):
  Viết từng bước, có đánh số.
  Highlight kết quả từng bước.

BEAT 4 — Kết quả (0:25–0:30):
  Box quanh đáp số.
  Tay rút ra, giữ nguyên frame.
```

---

## 7. Image Prompt Template — STEP-WHITEBOARD

```
[STEP-WHITEBOARD VISUAL ANCHOR: Original whiteboard animation on clean off-white #F5F5F0 background. 
A human hand holding a black marker appears from the right edge. Handwriting style: 
clean printed text, not cursive. Color coding: black for main content, red #E53935 for 
forces/energy, blue #2979FF for velocity/vectors, green #2E7D32 for results, 
yellow highlighter #FFD600 for key terms. No decorative elements.]

[SUBJECT — nội dung đang được vẽ/viết].
[STAGE — giai đoạn: diagram drawn / formula writing / result boxed].
SCIENCE ACCURACY LOCK: [quan hệ vật lý, chiều vector, ký hiệu đúng].
COMPOSITION: content fills 70% of frame, clean margins 15% each side.
STYLE: whiteboard animation, hand-drawn educational diagram, clean marker strokes.
Leave top-right 80×80px clear for watermark. No embedded printed text — only hand-drawn content. 16:9, 1280×720.
```

---

## 8. Video Prompt Template — STEP-WHITEBOARD

### Phần A — Gửi AI video tool
```
[STEP-WHITEBOARD CONTINUITY ANCHOR — sao chép nguyên văn Visual Anchor từ image prompt].
ANIMATE FROM REFERENCE IMAGE. Whiteboard animation, static frame, no camera movement.
One continuous shot, [x] seconds.

OPENING 0:00–0:02: hand enters from right holding black marker, positions at start point.
CORE 0:02–[n]s: hand draws [diagram/formula] stroke by stroke, left-to-right, 
top-to-bottom. Each element appears as hand passes over it.
TEACHING PEAK [n]s: hand switches to yellow highlighter, sweeps over key result once.
Hand draws rectangle box around final answer using red marker.
CLOSING [n+2]s: hand retracts from frame. All content holds visible.

MOTION: hand moves at natural writing speed (~0.4s per stroke). 
Strokes appear exactly where hand touches surface.
SCIENCE ACCURACY LOCK: [vector directions, formula correctness].
SOUND: soft marker-on-whiteboard SFX, light background music.
No speech, no voice, no embedded printed text, no subtitles, no watermark.
```

### Phần B — Voice Script (gửi TTS riêng)
```
[Lời giải thích tiếng Việt theo từng bước — sync với animation]
```

### Phần C — Hậu kỳ
```
- Ghép audio TTS theo timeline
- Không thêm label — tất cả đã trong animation
- Subtitle nếu cần
```

---

## 9. Negative Prompt

### Image:
```
photorealistic, 3D render, printed text, typed formula, PowerPoint style, 
digital clean vector, no hand visible, floating text, dark background (unless blackboard version),
busy illustration, colored background, decorative elements
```

### Video:
```
camera zoom, camera pan, text appearing without hand drawing it, 
printed/typed text popping in, no hand visible, teleporting elements,
content appearing instantly without drawing motion, speech in video
```

---

## 10. Khi nào dùng

| Tình huống | Dùng STEP-WHITEBOARD? |
|---|---|
| Chứng minh định luật bảo toàn năng lượng từng bước | ✅ Ưu tiên |
| Giải bài tập động học, lực, điện | ✅ Ưu tiên |
| Vẽ đồ thị v-t, x-t và phân tích | ✅ Ưu tiên |
| Phân tích lực trên mặt phẳng nghiêng | ✅ Ưu tiên |
| Giới thiệu khái niệm mới cần hình ảnh đẹp | ❌ Dùng EDU-FLAT-2D |
| Cần engagement cao, nhân vật | ❌ Dùng COSMIC-STORY-2D |
