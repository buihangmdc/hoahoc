# PRESET 07 — 📐 Công Thức Động
> **Tên dễ nhớ:** `Công Thức Động`
> **Tên kỹ thuật:** `MOTION-TYPE`
> **ID sản xuất:** `MATH-MOTION`
> **Trigger:** "công thức động", "kinetic typography", "motion type", "chữ động", "tóm tắt công thức", "ôn tập công thức", "formula animation"

---

## 1. Định nghĩa phong cách

**MOTION-TYPE** là phong cách **kinetic typography + formula animation** — công thức, ký hiệu, từ khóa xuất hiện và chuyển động theo nhịp giải thích, trên nền tối. Không có illustration. Sức mạnh: truyền đạt cấu trúc toán học và logic vật lý cực kỳ rõ ràng, nhanh và đẹp. Thích hợp nhất cho video ôn tập, tóm tắt chương, định nghĩa.

Chính sách nguyên bản: dùng nguyên lí đồ họa toán học và chuyển động biến đổi; không sao chép palette, bố cục, giọng kể hoặc nhận diện của tác giả/kênh cụ thể.

---

## 2. Hệ màu (Color System)

### Palette chính — Dark Science
| Token | Hex | Dùng cho |
|-------|-----|----------|
| `bg-dark` | `#0F0F1A` | Nền chính — đen xanh rất đậm |
| `text-main` | `#E8E8F0` | Công thức chính, text thường |
| `text-dim` | `#8888AA` | Text phụ, đã giải thích xong |
| `color-result` | `#FFD700` | Kết quả cuối, đáp số — vàng gold |
| `color-variable` | `#64B5F6` | Biến số (x, v, a, t...) — xanh nhạt |
| `color-constant` | `#81C784` | Hằng số (g, G, c, k...) — xanh lá |
| `color-force` | `#EF5350` | Lực, năng lượng, nhiệt — đỏ |
| `color-vector` | `#29B6F6` | Vector, hướng — xanh dương |
| `color-highlight` | `#FFB74D` | Highlight box, underline — cam |
| `color-new` | `#CE93D8` | Khái niệm/đại lượng mới — tím nhạt |
| `color-unit` | `#80CBC4` | Đơn vị đo [m], [s], [N]... — xanh ngọc |

---

## 3. Visual Anchor chuẩn

```
[MOTION-TYPE VISUAL ANCHOR: Kinetic typography animation on deep dark #0F0F1A background. 
Clean mathematical typography, LaTeX-style rendering. 
Color system: main text #E8E8F0, variables #64B5F6, constants #81C784, 
forces/energy #EF5350, vectors #29B6F6, results #FFD700, units #80CBC4.
No illustrations. No characters. No background texture.
All content: text, symbols, formulas, simple geometric indicators (arrows, boxes, lines).
Negative space is intentional — maximum 40% of screen filled at any time.]
```

---

## 4. Typography System

### Font hierarchy
```
CÔNG THỨC CHÍNH: LaTeX-style math font hoặc Fira Math — size 64px ở 720p
TỪ KHÓA: Poppins Bold hoặc Montserrat ExtraBold — size 48px
GIẢI THÍCH PHỤ: Poppins Regular — size 32px
ĐƠN VỊ: Fira Code hoặc monospace — size 28px, trong ngoặc vuông
GHI CHÚ NHỎ: Poppins Light — size 24px, dim color
```

### Layout zones
```
ZONE 1 — Tiêu đề (trên cùng): Tên đại lượng/định luật đang trình bày
ZONE 2 — Main formula (trung tâm 60%): Công thức lớn, animation chính
ZONE 3 — Breakdown (dưới): Giải thích từng ký hiệu, list
ZONE 4 — Context (trái/phải): Điều kiện, giới hạn áp dụng
```

---

## 5. Formula Animation Patterns

### Pattern A — Sequential Reveal (Từng bước)
```
Ứng dụng: chứng minh, suy ra công thức
- Viết vế trái → pause 0.5s → viết dấu = → pause → viết vế phải
- Mỗi bước có số thứ tự (1), (2)... xuất hiện trước
- Dùng mũi tên → để chỉ "suy ra"
- Highlight ký hiệu đang giải thích bằng box màu cam
```

### Pattern B — Color Mapping (Tô màu vai trò)
```
Ứng dụng: giới thiệu công thức mới
- Công thức xuất hiện toàn bộ (trắng)
- Từng nhóm ký hiệu đổi màu theo vai trò
- Text giải thích xuất hiện bên cạnh kết nối bằng đường kẻ
- Ví dụ: F = ma → F đỏ, m xanh lá, a xanh dương
```

### Pattern C — Transform (Biến đổi)
```
Ứng dụng: thể hiện phép biến đổi toán học
- Công thức ban đầu → animate biến đổi → công thức mới
- Phần giữ nguyên: không di chuyển
- Phần thay đổi: fade out cũ, fade in mới tại chỗ
- Dùng underbrace/overbrace highlight
```

### Pattern D — Graph Build (Xây đồ thị)
```
Ứng dụng: minh họa quan hệ hàm số
- Trục tọa độ vẽ trước (stroke animation)
- Đường đồ thị vẽ từ trái → phải (stroke dashoffset)
- Label điểm đặc biệt (gốc, cực trị, nghiệm) hiện sau
- Màu đường = màu đại lượng (xanh dương cho v-t, đỏ cho a-t)
```

---

## 6. Indicator Elements (Không phải illustration)

```
MŨI TÊN: → (suy ra), ↑↓ (tăng/giảm), ↔ (tỉ lệ), ∝ (tỉ lệ thuận)
BOX HIGHLIGHT: border-radius 4px, màu accent, stroke 2px — không fill
UNDERLINE: 2px, màu accent, animate sweep
BRACKET: underbrace/overbrace với label
EQUALS CHAIN: =, ≈, ≠, ∝, → align thẳng đứng
CIRCLED NUMBER: ① ② ③ màu accent — đánh dấu bước
CHECKMARK: ✓ xanh lá khi kết quả đúng
CROSS: ✗ đỏ khi điều kiện sai
```

---

## 7. Quy tắc Animation

### Timing
| Loại | Duration | Easing |
|---|---|---|
| Ký tự/ký hiệu appear | 0.05s/ký tự | linear |
| Toàn công thức scale in | 0.4s | ease-out |
| Color highlight sweep | 0.3s | linear |
| Box appear | 0.3s | scale 0→1 |
| Arrow draw | 0.4s | ease-out |
| Text dim (đã qua) | 0.5s | fade to dim |
| Transform formula | 0.6s | ease-in-out |
| Graph line draw | 1.0–2.0s | ease-out |
| Underbrace expand | 0.4s | ease-out |

### Timing chuẩn mỗi ký hiệu
- Công thức ngắn (≤8 ký tự): xuất hiện cùng lúc
- Công thức dài: write character by character, 0.05s/ký tự
- Sau mỗi cụm: pause 0.3s trước khi xuất hiện cụm tiếp

### Camera: **STATIC FRAME TUYỆT ĐỐI** — không bao giờ zoom/pan

---

## 8. Giới hạn kỹ thuật AI video tool (BẮT BUỘC ĐỌC TRƯỚC KHI VIẾT PROMPT)

```
⚠️ CLIP LIMIT: Các AI video tool hiện tại (Kling, MiniMax, Runway...) 
chỉ render tối đa 8–10 giây / clip.

QUY TẮC CỨNG:
- Mỗi VIDEO PROMPT không được vượt quá 9 giây.
- Mỗi VIDEO PROMPT phải có một PROMPT ẢNH riêng làm reference image.
- 1 scene dài → chia thành nhiều clip 8–9s, mỗi clip = 1 ảnh + 1 video prompt.
- Số ảnh = số video prompt = số clip (quan hệ 1:1 tuyệt đối).
- Clip kế tiếp bắt đầu bằng trạng thái kết thúc của clip trước (continuity).
- Trong mỗi clip: chỉ animate 1–2 sự kiện chính, không nhồi nhiều bước.

CÁCH ĐẶT TÊN CLIP (theo `rules/CONG-THUC-SCENE-WORD.md`):
  SC0X-A, SC0X-B, SC0X-C...
  Ví dụ: SC02-A (0:05–0:13), SC02-B (0:13–0:22)

CONTINUITY ANCHOR giữa các clip:
  - Clip B bắt đầu bằng: "START FROM END STATE OF [SC0X-A]."
  - Mô tả ngắn trạng thái màn hình đầu clip (những gì đã có sẵn).
  - Không animate lại những gì đã xuất hiện ở clip trước.
```

---

## 9. Cấu trúc Scene chuẩn (sau khi áp dụng clip-limit)

```
BEAT 1 — Tiêu đề (1 clip, ≤8s):
  Tên đại lượng/định luật hiện to ở trung tâm, fade nhỏ xuống zone trên.

BEAT 2 — Công thức chính (1 clip, ≤9s):
  Công thức xuất hiện theo pattern A hoặc B. Mỗi ký hiệu đổi màu.
  Highlight box xuất hiện quanh ký hiệu trọng tâm. Dừng ở đây.

BEAT 3 — Breakdown (1–2 clip, mỗi clip ≤9s):
  Clip 3A: 1–2 breakdown line đầu slide in.
  Clip 3B (nếu cần): breakdown line còn lại + điều kiện áp dụng.

BEAT 4 — Application (1 clip, ≤9s):
  Ví dụ số: thay giá trị, kết quả gold highlight.

BEAT 5 — Summary hold (1 clip, ≤8s):
  Tất cả công thức thu nhỏ, dim breakdown, gold box quanh kết quả.
```

---

## 10. Image Prompt Template — MOTION-TYPE

> Mỗi clip cần 1 ảnh riêng mô tả **trạng thái màn hình cuối clip** (frame cuối).  
> Ảnh này vừa là reference image, vừa là điểm bắt đầu của clip kế tiếp.

```
[MOTION-TYPE VISUAL ANCHOR: Kinetic typography animation on deep dark #0F0F1A background. 
Clean mathematical typography, LaTeX-style rendering. 
Color coding: variables #64B5F6, constants #81C784, forces #EF5350, vectors #29B6F6, 
results #FFD700, units #80CBC4. No illustrations. No characters. 
Maximum 40% of screen filled. Clean negative space intentional.]

[CLIP: SC0X-[A/B/C] — mô tả đây là clip thứ mấy của scene nào]
[CONTENT — mô tả chính xác những gì có trên màn hình ở frame CUỐI clip:
  - Công thức / ký hiệu nào, màu gì, kích thước, vị trí
  - Breakdown line nào đã xuất hiện (nếu có)
  - Highlight box nào đang active
  - Text nào đã dim (#8888AA) vì đã qua]
[STAGE — title / formula-reveal / breakdown-partial / breakdown-complete / result / summary]
[PATTERN — Sequential / Color-mapping / Transform / Graph]
SCIENCE ACCURACY LOCK: [ký hiệu, chiều, đơn vị phải đúng — liệt kê cụ thể]
COMPOSITION: formula centered 60%, breakdown below 30%, title top 10%.
STYLE: original kinetic typography and mathematical visualization; no imitation of a named creator or channel.
Leave upper-right 80×80px clear for watermark. No embedded decorative text. 16:9, 1280×720.
```

---

## 11. Video Prompt Template — MOTION-TYPE

> ⚠️ Mỗi prompt tối đa 9 giây. Chỉ mô tả animation xảy ra trong clip này.

### Phần A — Gửi AI video tool
```
[MOTION-TYPE CONTINUITY ANCHOR: Kinetic typography on deep dark #0F0F1A background.
Color system: variables #64B5F6, constants #81C784, forces #EF5350, vectors #29B6F6,
results #FFD700, units #80CBC4. No illustrations. Static frame, no camera movement.]

ANIMATE FROM REFERENCE IMAGE. [X] seconds. CLIP: SC0X-[A/B/C].

START STATE (frame 0): [mô tả những gì đã có sẵn trên màn hình — 
  những phần tử này KHÔNG animate lại, chỉ giữ nguyên]
  Ví dụ: "Formula 'Φ = B·S·cosα' already visible with color coding. 
  Orange box around cosα already present."

ANIMATION SEQUENCE:
  0:00–0:[n]: [sự kiện 1 — cụ thể, ngắn gọn]
  0:[n]–0:[m]: [sự kiện 2 — nếu có]
  0:[m]–0:[end]: [hold / fade / transition sang trạng thái kết thúc]

END STATE (frame cuối): [mô tả màn hình trông như thế nào — 
  khớp với CONTENT trong ảnh reference của clip này]

MOTION: all text appears in place. Static frame. No camera movement whatsoever.
SCIENCE ACCURACY LOCK: [ký hiệu, đơn vị, chiều đúng — liệt kê cụ thể]
SOUND: [mô tả âm thanh — ambient / chime / tone — hoặc "continue ambient from previous clip"]
No speech, no voice, no subtitles, no watermark.
```

### Phần B — Voice Script (gửi TTS riêng, sync với toàn scene)
```
[Lời giải thích — viết theo đơn vị scene, không chia theo clip]
[Tone học thuật nhưng thân thiện, tốc độ vừa, tiếng Việt chuẩn]
```

### Phần C — Hậu kỳ
```
- Ghép clip theo thứ tự A → B → C... (hard cut hoặc 2-frame cross dissolve)
- Subtitle sync theo TTS — không để subtitle chạy quá frame
- Kiểm tra màu sắc ký hiệu khớp color system qua toàn scene
- Không thêm illustration — text only
- Kiểm tra continuity: clip B phải bắt đầu đúng từ end state của clip A
```

---

## 11. Negative Prompt

### Image:
```
illustrations, characters, decorative elements, colorful background, 
light background, gradient sky, cluttered layout, more than 40% screen filled,
handwritten text, chalk style, whiteboard, colored ink,
random text colors not following the color system
```

### Video:
```
text flying in from offscreen, camera zoom, camera pan, 
characters, illustrations, background texture animation,
more than one formula animating simultaneously,
overlapping text, unreadable font size
```

---

## 12. Use Cases nhanh (với clip-limit 9s)

| Loại nội dung | Pattern | Tổng thời lượng | Số clip | Số ảnh |
|---|---|---|---|---|
| Giới thiệu công thức F = ma | B (Color-map) | 20s | 3 clip ×7s | 3 |
| Chứng minh v² = v₀² + 2aΔx | A (Sequential) | 45s | 5 clip ×9s | 5 |
| So sánh Wd và Wt (năng lượng) | C (Transform) | 30s | 4 clip ×8s | 4 |
| Vẽ đồ thị v-t chuyển động đều | D (Graph Build) | 25s | 3 clip ×8s | 3 |
| Tóm tắt 5 công thức động học | B × 5 lặp | 60s | 7–8 clip | 7–8 |

---

## 13. Khi nào dùng

| Tình huống | Dùng MOTION-TYPE? |
|---|---|
| Video tóm tắt công thức cuối chương | ✅ Ưu tiên |
| Giới thiệu định nghĩa đại lượng mới | ✅ Ưu tiên |
| Chứng minh toán học từng bước | ✅ Ưu tiên |
| Video ôn tập trước kỳ thi (60–90s) | ✅ Ưu tiên |
| Cần minh họa trực quan hiện tượng | ❌ Dùng EDU-FLAT-2D |
| Cần nhân vật kể chuyện | ❌ Dùng COSMIC-STORY-2D |
| Cần vẽ sơ đồ bằng tay | ❌ Dùng STEP-WHITEBOARD |
