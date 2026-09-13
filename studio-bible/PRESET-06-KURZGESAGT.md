# PRESET 06 — 🦆 Kể Chuyện
> **Tên dễ nhớ:** `Kể Chuyện`
> **ID sản xuất:** `COSMIC-STORY-2D`
> **Trigger chức năng:** "kể chuyện", "nhân vật kể chuyện", "storytelling", "Shorts", "kể chuyện khoa học", "nhân hóa", "flat character"

---

## 1. Định nghĩa phong cách

**COSMIC-STORY-2D** là phong cách kể chuyện bằng nhân vật phẳng nguyên bản — nhân vật 2D có biểu cảm, hiện tượng được nhân hóa có kiểm soát, chuyển thang từ vật thể đến vi mô hoặc vũ trụ. Màu nền đậm, tương phản cao; phù hợp hook và câu hỏi “tại sao”.

Chính sách nguyên bản: không sao chép mascot, hình dáng nhân vật, tổ hợp màu hay bố cục nhận diện của kênh cụ thể.

---

## 2. Hệ màu (Color System)

### Palette chính — Dark Gradient
| Token | Hex | Dùng cho |
|-------|-----|----------|
| `bg-deep-navy` | `#0D1B2A` | Nền cảnh vũ trụ, vi mô |
| `bg-gradient-start` | `#1B2A4A` | Nền gradient trên |
| `bg-gradient-end` | `#0A1628` | Nền gradient dưới |
| `accent-amber` | `#FFB300` | Highlight, ánh sáng, năng lượng |
| `accent-teal` | `#00BCD4` | Nước, sóng, điện từ |
| `accent-coral` | `#FF5252` | Nhiệt, nguy hiểm, lực mạnh |
| `accent-lime` | `#AEEA00` | Hóa học, phản ứng, sinh học |
| `accent-purple` | `#7C4DFF` | Từ trường, trường lực, lượng tử |

### Palette phụ — Light Story
| Token | Hex | Dùng cho |
|-------|-----|----------|
| `bg-sky` | `#87CEEB` | Cảnh ban ngày, trái đất, lớp học |
| `bg-warm-cream` | `#FFF3E0` | Cảnh trong nhà, ấm áp |
| `character-skin-1` | `#FFCC80` | Da nhân vật sáng |
| `character-skin-2` | `#A1887F` | Da nhân vật tối hơn |
| `character-outline` | `#2C1810` | Viền nhân vật |

---

## 3. Visual Anchor chuẩn

```
[COSMIC-STORY-2D VISUAL ANCHOR: Original flat 2D character animation for science storytelling. 
Deep navy-to-dark-blue gradient background #0D1B2A to #1B2A4A. 
Characters: rounded flat 2D figures with simple faces (dot eyes, arc smile), 
outline color #2C1810, smooth fill colors. 
Color accents: amber #FFB300, teal #00BCD4, coral #FF5252. 
All objects: flat vector, clean edges, consistent drop shadow 3px offset. 
Scale transitions allowed: macro to micro to cosmic. 
Storytelling composition: characters interact with physics phenomena as tangible objects.]
```

---

## 4. Character Design

### Nhân vật nguyên bản
```
Đầu: hình tròn hoặc oval, mắt tròn 2 chấm, miệng cung đơn giản
Thân: hình chữ nhật bo góc, tay ngắn có 3 ngón
Màu: solid fill, không gradient trên người
Biểu cảm: thay đổi qua mắt (to = ngạc nhiên, nhíu = suy nghĩ, nhắm = vui)
Chiều cao: ~30% frame height khi đứng một mình
```

### Nhân vật hóa vật lý (Physics Personification)
```
Electron: hình cầu xanh nhỏ có mặt, mang dấu (-)
Proton: hình cầu đỏ có mặt, mang dấu (+)
Photon: hình sóng vàng có mắt, di chuyển theo sóng
Nguyên tử: nhân ở giữa + quỹ đạo electron quay quanh, có biểu cảm
Lực: mũi tên lớn có cơ bắp (nhân hóa lực mạnh)
Năng lượng: tia sét/lửa màu vàng có mắt
```

---

## 5. Transition & Scale System

```
MACRO (vật thể quan sát được):
  Kích thước bình thường, màu sắc đời thực, nhân vật tương tác

ZOOM IN → MICRO (phân tử, nguyên tử):
  Nền chuyển sang deep navy
  Các hạt xuất hiện với màu accent rực rỡ
  Animation: circular zoom in, nền fade dark

ZOOM OUT → COSMIC (hệ mặt trời, thiên hà):
  Nền đen tuyền với star field
  Đối tượng nhỏ dần, label scale xuống

TRANSITION CUẨ: scale zoom 0.8s ease-in-out, nền cross-dissolve 0.4s
```

---

## 6. Quy tắc Animation

### Timing
| Loại | Duration | Easing |
|---|---|---|
| Character walk-in | 0.5s | ease-out |
| Character expression change | 0.2s | instant + squash |
| Object appear | 0.4s | scale 0→1 + bounce |
| Scale transition (zoom) | 0.8s | ease-in-out |
| Text caption appear | 0.3s | fade + slide up |
| Particle burst | 0.6s | radial explode |
| Scene cut | 0.2s | hard cut |

### Squash & Stretch
- Nhân vật cúi xuống: squash 10%
- Nhân vật nhảy: stretch 15% khi lên, squash 20% khi chạm đất
- Object bị đập: squash rõ, recover 0.3s
- Áp dụng cho tất cả nhân vật, không áp dụng cho sơ đồ kỹ thuật

### Camera
- **Zoom cho phép** — đây là điểm khác với EDU-FLAT-2D
- Zoom in để focus chi tiết (push in 20–30%)
- Zoom out để reveal context (pull out 30–50%)
- **Không pan ngang** trừ khi follow nhân vật
- Transition giữa scale: circular mask expand/contract

---

## 7. Cấu trúc Scene chuẩn

```
BEAT 1 — Hook (0:00–0:05):
  Câu hỏi gây tò mò. Nhân vật phản ứng ngạc nhiên.
  Ví dụ: nhân vật bị sét đánh → mắt to → câu hỏi pop lên

BEAT 2 — Scale in (0:05–0:12):
  Zoom vào hiện tượng. Transition từ macro → micro.
  Nhân vật hóa các hạt/lực xuất hiện.

BEAT 3 — Story action (0:12–0:22):
  Nhân vật/hạt tương tác minh họa nguyên lý.
  Caption text xuất hiện từng cụm từ.

BEAT 4 — Punchline (0:22–0:28):
  Zoom out về macro. Kết nối với đời thực.
  Nhân vật phản ứng thích thú/ngạc nhiên.

BEAT 5 — Hold (0:28–0:30):
  Caption tóm tắt 1 dòng. Nhân vật nháy mắt.
```

---

## 8. Image Prompt Template — COSMIC-STORY-2D

```
[COSMIC-STORY-2D VISUAL ANCHOR: Original flat 2D character animation for science storytelling. 
Deep navy-to-dark-blue gradient background #0D1B2A to #1B2A4A. 
Characters: rounded flat 2D figures, dot eyes, arc smile, outline #2C1810. 
Color accents: amber #FFB300, teal #00BCD4, coral #FF5252. 
Flat vector style, consistent 3px drop shadow on objects.]

[SUBJECT — nhân vật và đối tượng vật lý đang tương tác].
[SCALE — macro / micro / cosmic].
[ACTION — hành động storytelling].
SCIENCE ACCURACY LOCK: [hiện tượng vật lý phải đúng dù được nhân hóa].
COMPOSITION: [nhân vật trái/phải, đối tượng trung tâm].
STYLE: original flat character animation, educational storytelling, vibrant colors on dark background; no imitation of a named studio or channel.
Leave upper-right 80×80px clear for watermark. No embedded text. 16:9, 1280×720.
```

---

## 9. Video Prompt Template — COSMIC-STORY-2D

### Phần A — Gửi AI video tool
```
[COSMIC-STORY-2D CONTINUITY ANCHOR — sao chép nguyên văn Visual Anchor từ image prompt].
ANIMATE FROM REFERENCE IMAGE. Original flat 2D character animation for science storytelling.
One continuous shot, [x] seconds.

OPENING 0:00–0:02: characters hold positions from reference image.
CORE 0:02–[n]s: [nhân vật chuyển động / tương tác / zoom transition].
Character animation: squash and stretch on impacts, expression changes via eyes.
[Nếu có zoom]: circular zoom [in/out] over [duration]s transitioning from [macro/micro] to [micro/macro].
TEACHING PEAK [n]s: [hành động minh họa đỉnh điểm của nguyên lý vật lý].
CLOSING [n+2]s: characters hold, expression [happy/surprised/thoughtful].

MOTION: smooth ease-in-out, squash 10% on landing, stretch 15% on jump.
SCIENCE ACCURACY LOCK: [ràng buộc — dù nhân hóa, hướng lực/chuyển động phải đúng].
SOUND: upbeat orchestral/electronic, whoosh on zoom, pop on character appear.
No speech, no embedded text, no subtitles, no watermark.
```

### Phần B — Voice Script (gửi TTS riêng)
```
[Kịch bản giọng kể chuyện tiếng Việt — tone tò mò, hào hứng]
```

### Phần C — Hậu kỳ
```
- Caption text thêm sau (font Nunito Bold, màu trắng/vàng)
- Ghép audio TTS
- Subtitle
```

---

## 10. Negative Prompt

### Image:
```
photorealistic, 3D render, realistic faces, anime style, manga, 
light background (unless story scene), scientifically impossible personification 
that violates physics direction, text embedded in illustration, complex background details
```

### Video:
```
realistic movement, motion capture, 3D, camera shake, 
scientifically wrong force direction on personified characters,
too many simultaneous characters (max 4), 
characters speaking (mouth opening and closing with speech), 
text appearing without caption layer
```

---

## 11. Khi nào dùng

| Tình huống | Dùng COSMIC-STORY-2D? |
|---|---|
| Video mở đầu chương "Điện từ trường là gì?" | ✅ Ưu tiên |
| Giải thích ứng dụng đời sống (MRI, GPS, đèn LED) | ✅ Ưu tiên |
| Lịch sử phát hiện (Newton, Faraday, Einstein) | ✅ Ưu tiên |
| Video ngắn TikTok/Shorts gây tò mò | ✅ Ưu tiên |
| Giải bài tập có số liệu cụ thể | ❌ Dùng STEP-WHITEBOARD |
| Sơ đồ mạch điện, vector lực chi tiết | ❌ Dùng EDU-FLAT-2D |
