# PRESET 04 — 🎨 Hoạt Hình 2D
> **Tên dễ nhớ:** `Hoạt Hình 2D`
> **ID sản xuất:** `EDU-FLAT-2D`
> Tên file cũ chỉ để tương thích. Dùng khi cần hoạt hình giáo dục 2D phẳng, sơ đồ nguyên lí và khung máy tĩnh.

---

## 1. Định nghĩa phong cách

**EDU-FLAT-2D** là hệ **2D flat animation nguyên bản** — không có người thật, không render 3D photorealistic. Toàn bộ nội dung là illustration vector 2D, animation mượt, label text layer riêng. Phù hợp giải thích hiện tượng có thể biểu diễn bằng sơ đồ nguyên lí.

Chính sách nguyên bản: không sao chép logo, watermark, mascot, bố cục nhận diện hoặc nhân vật của bất kỳ kênh nào.

---

## 2. Hệ màu (Color System)

### Zone A — Nền kem (dùng cho phần lý thuyết, Định luật Lenz)
| Token | Hex | Dùng cho |
|-------|-----|----------|
| `bg-cream` | `#FFF8D0` | Nền chính toàn frame |
| `accent-orange-dark` | `#FF9500` | Bán tròn trang trí góc |
| `accent-orange-medium` | `#FFAB40` | Chi tiết phụ |

### Zone B — Nền xanh (dùng cho phần ứng dụng, Dòng Fu-cô)
| Token | Hex | Dùng cho |
|-------|-----|----------|
| `bg-blue` | `#1BB0EA` | Nền chính toàn frame |
| `accent-blue-dark` | `#0D8BC0` | Bán tròn trang trí góc |

### Màu UI / Label
| Token | Hex | Dùng cho |
|-------|-----|----------|
| `label-red` | `#E53232` | Label concept chính, cực N nam châm |
| `label-navy` | `#1A3C8C` | Tooltip term, accent square trước label |
| `label-blue` | `#1E88E5` | Galvanometer, cực S nam châm |
| `text-white` | `#FFFFFF` | Chữ trên mọi label |

### Màu illustration vật lý
| Token | Hex | Dùng cho |
|-------|-----|----------|
| `coil-outer` | `#FF8C00` | Cuộn dây solenoid — lớp ngoài |
| `coil-inner` | `#CC3300` | Cuộn dây solenoid — lớp trong |
| `field-line` | `#BBBBBB` | Đường sức từ, mũi tên trường |
| `wire-pos` | `#E53232` | Dây điện cực dương |
| `wire-neg` | `#1E88E5` | Dây điện cực âm |
| `hand-skin` | `#F4A464` | Tay người flat illustration |
| `vector-b` | `#4CAF50` | Vector B (mũi tên từ trường) |
| `foucault-current` | `#FF5252` | Vòng dòng Fu-cô trên đĩa |
| `disc-surface` | `#E8E8E8` | Mặt đĩa dẫn điện |
| `disc-pillar` | `#FFC107` | Trụ đỡ đĩa |

---

## 3. Trang trí nền (Background Decoration)

### Zone A (kem):
- **Góc trái dưới:** 1/4 hình tròn to `accent-orange-dark`, radius ~180px, cut vào từ góc
- **Góc phải trên:** góc tròn nhỏ `accent-orange-dark`, radius ~120px, cut vào từ góc
- **Góc phải dưới:** 1/4 hình tròn to `accent-orange-dark`, radius ~200px, cut vào từ góc
- Góc phải trên để trống cho metadata dự án nếu được yêu cầu.

### Zone B (xanh):
- **Góc trái trên:** bán tròn `accent-blue-dark`, radius ~150px
- **Góc phải dưới:** bán tròn `accent-blue-dark`, radius ~180px

---

## 4. Vùng an toàn thương hiệu dự án

Chỉ chèn logo khi người dùng cung cấp tài sản và xác nhận quyền sử dụng. Mặc định không có logo/watermark. Có thể giữ vùng an toàn 80×80 px cho metadata hậu kỳ của chính dự án.

---

## 5. Hệ thống Typography (Label System)

### Label Concept Chính (Red Label)
```
Dùng cho: tên hiện tượng, trạng thái, định luật đang minh họa
Ví dụ: "Φ tăng", "chống lại sự tăng từ thông", "Định luật Lenz"

Cấu trúc: [■ navy accent square 8×32px] + [red background] + [white bold text]
Background: #E53232, border-radius 4px
Padding: 10px top/bottom, 16px left/right
Font: Nunito ExtraBold hoặc Poppins Bold, size ~28px ở 720p
Text: WHITE ALL CAPS hoặc Title Case
Vị trí: trên cùng trái frame, cách mép 32px
```

### Tooltip Term (Navy Tooltip)
```
Dùng cho: tên thuật ngữ chú thích trên illustration
Ví dụ: "Dòng điện cảm ứng", "Dòng Fu-cô"

Background: #1A3C8C, border-radius 8px
Có mũi tên tooltip (triangle) pointing xuống-trái
Padding: 8px top/bottom, 14px left/right  
Font: Poppins SemiBold, size ~22px ở 720p
Text: WHITE
Vị trí: floating gần đối tượng được chú thích, không đè lên
```

> **QUY TẮC TUYỆT ĐỐI:** Không embed chữ trực tiếp vào illustration. Tất cả label là layer riêng thêm hậu kỳ. Trong image/video prompt luôn viết: `No embedded text in illustration. All labels and formulas added in post-production.`

---

## 6. Illustration Elements (Mô tả kỹ từng đối tượng)

### Solenoid (Cuộn dây)
```
Mô tả: solenoid coil, 5–7 vòng, nhìn góc 3/4 frontal-slightly-right
Màu: cam-đỏ gradient, outer #FF8C00, inner #CC3300, stroke #8B2000
Đầu dây: 2 terminal màu vàng/đồng nhỏ (top và bottom)
Style: 2D flat, drop shadow nhẹ phía dưới
Tỉ lệ: chiều cao ~ 60% frame height khi là element chính
```

### Nam châm Bar (Bar Magnet)
```
Mô tả: rectangular block magnet, 2 nửa rõ ràng
Nửa N: màu đỏ #E53232, label "N" trắng bold center
Nửa S: màu xanh #1E88E5, label "S" trắng bold center
Viền: bo góc 6px, stroke tối nhẹ
Khi đang tiến vào cuộn dây: có bracket đỏ nhấp nháy ở góc phải
Style: 2D flat, drop shadow nhỏ
```

### Galvanometer (Điện kế)
```
Mô tả: square analog meter, nhìn thẳng frontal
Vỏ ngoài: hình vuông bo góc, màu xanh dương #1E88E5
Mặt đồng hồ: hình tròn trắng, có vạch -10, 0, +10
Kim: pointer đen mỏng, xoay từ tâm
Terminal: 2 nút tròn dưới đáy (label A và B hoặc + và -)
Animation: kim swing có overshoot nhẹ khi có dòng
```

### Đường sức từ (Field Lines)
```
Mô tả: đường cong ellipse đối xứng quanh nam châm
Màu: xám nhạt #BBBBBB, opacity 70%
Mũi tên: nhỏ, chỉ hướng ra từ N vào S bên ngoài
Độ dày stroke: 1.5px
Animation: vẽ từng đường từ nam châm ra ngoài
```

### Tay người (Hand)
```
Mô tả: bàn tay phải flat 2D, cầm hoặc di chuyển đối tượng
Màu da: #F4A464, outline #C47A3C
Style: cartoon flat, ngón tay rõ ràng, không quá chi tiết
Khi dùng quy tắc bàn tay phải: ngón cái chỉ hướng dòng điện, ngón khác cuộn
```

### Đĩa dẫn điện — Dòng Fu-cô (Foucault Disc)
```
Mô tả: đĩa tròn isometric view (nhìn từ trên xuống góc 45°)
Mặt đĩa: màu trắng/xám nhạt #E8E8E8
Viền đĩa: có các chấm tròn nhỏ chạy đều quanh mép (symbolize conductor)
Trụ đỡ: 2 trụ vàng #FFC107 trên và dưới đĩa
Nam châm trên đĩa: N đỏ + S xanh isometric block nhỏ, đứng giữa đĩa
Dòng Fu-cô: vòng xoắn ellipse đỏ hồng #FF5252, animate xoáy theo chiều kim đồng hồ hoặc ngược lại
Vector B: mũi tên xanh lá #4CAF50 nhỏ, label "B" — chỉ hướng từ trường
```

---

## 7. Quy tắc Animation

### Timing cơ bản
| Loại chuyển động | Duration | Easing |
|---|---|---|
| Object enter (slide) | 0.4s | ease-out |
| Label pop-in | 0.3s | ease-out + slight bounce (overshoot 1.05) |
| Arrow draw | 0.5s | linear |
| Needle swing | 0.6s | ease-in-out + overshoot |
| Magnet translate | 0.8s | ease-in-out |
| Background zone change | 0.3s | hard cut hoặc cross-fade |
| Scene transition | 0.2s | cross-dissolve |

### Entry patterns
- Đối tượng từ trái: slide in từ x=-200
- Đối tượng từ phải: slide in từ x=+200
- Label: scale từ 0.8 + fade in
- Mũi tên: stroke-dashoffset animate từ 100% → 0%
- Tooltip: fade in tại chỗ

### Camera
- **STATIC FRAME** — tuyệt đối không pan, không zoom, không camera movement
- Mọi "chuyển động" đều là object animation trên canvas cố định
- Aspect ratio: 16:9, 1280×720px

### Số elements per frame
- Tối đa 4–5 objects đồng thời
- Luồng đọc: trái → phải, trên → dưới
- Quan hệ nhân quả: nguyên nhân trái, kết quả phải

---

## 8. Cấu trúc Scene chuẩn (Scene Blueprint)

Mỗi scene EDU-FLAT-2D gồm các beat:

```
BEAT 1 — Setup (0:00–0:03):
  Illustration xuất hiện trên background, không có label.
  Magnet/object ở trạng thái ban đầu.

BEAT 2 — Action (0:03–0:06):
  Object chuyển động (magnet tiến vào/ra).
  Red label xuất hiện góc trên trái: trạng thái đang xảy ra.

BEAT 3 — Response (0:06–0:09):
  Galvanometer needle swing.
  Dây điện có mũi tên dòng chạy.
  Tooltip navy xuất hiện chú thích kết quả.

BEAT 4 — Hold (0:09–0:10):
  Giữ nguyên trạng thái 1 giây.
  Chuẩn bị cut sang scene tiếp.
```

---

## 9. Image Prompt Template — EDU-FLAT-2D

```
[EDU-FLAT-2D VISUAL ANCHOR: original 2D flat vector animation, clean educational illustration, 
no photorealism, no 3D render. Background: [ZONE-A: solid cream #FFF8D0 with three orange 
#FF9500 quarter-circle decorations at bottom-left, top-right, and bottom-right corners | 
ZONE-B: solid sky-blue #1BB0EA with dark-blue #0D8BC0 half-circle at top-left and bottom-right]. 
Drop shadow: subtle only on main objects. All objects: 2D flat vector, consistent stroke weight 2px.]

[SUBJECT — mô tả đối tượng chính].
[ACTION — trạng thái/vị trí].
SCIENCE ACCURACY LOCK: [quan hệ vật lý bắt buộc].
COMPOSITION: [bố cục trái-phải].
STYLE: original 2D flat educational animation, vector art, clean lines, 
vibrant colors on cream/blue background.
Leave upper-right corner 80×80px clear for optional project metadata. Do not generate any logo or watermark.
Leave [vị trí] clear for Vietnamese text label added in post-production.
No embedded text, no formulas, no subtitles in illustration. 16:9, 1280×720.
```

---

## 10. Video Prompt Template — EDU-FLAT-2D

> Output của bước này gồm **3 phần tách biệt**. Chỉ Phần A gửi vào AI video tool.

### Phần A — Gửi AI video tool (Kling / Runway / Veo)
```
[EDU-FLAT-2D CONTINUITY ANCHOR — sao chép NGUYÊN VĂN VISUAL ANCHOR từ image prompt tương ứng].
ANIMATE FROM REFERENCE IMAGE. 2D flat animation style, no camera movement, static frame.
One continuous shot, [x] seconds.

OPENING 0:00–0:02: [trạng thái ban đầu khớp ảnh, objects hold].
BEAT-ACTION 0:02–0:05: [object translate/animate — mô tả hướng chính xác].
BEAT-RESPONSE 0:05–0:08: [reaction elements animate — needle swing / current arrow draw].
CLOSING 0:08–0:10: [all elements hold, no movement].

ANIMATION RULES: ease-out entries 0.4s, label pop-in scale 0.3s, arrow stroke-draw 0.5s,
needle overshoot then settle. Static background — no parallax, no zoom, no pan.
SCIENCE ACCURACY LOCK: [ràng buộc vật lý].
SOUND: light upbeat electronic music background, soft pop SFX on object entry — no speech, no voice.
No embedded text, no subtitles, no watermark.
```

### Phần B — Gửi TTS riêng (FPT.AI / ElevenLabs / thu âm)
```
[Câu tiếng Việt vừa [x] giây — đánh dấu nhấn IN HOA, nghỉ dấu /]
Giọng đọc: [nữ miền Nam phổ thông / nam miền Bắc]
Tốc độ: [0.9× / 1.0×]
```

### Phần C — Hậu kỳ (CapCut / Premiere)
```
- Ghép Phần A (.mp4) + Phần B (.mp3), căn theo timeline
- Red label: [nội dung] tại góc trên trái
- Navy tooltip: [nội dung] gần [đối tượng]
- Subtitle phụ đề (nếu cần)
```

---

## 11. Negative Prompt chuẩn cho EDU-FLAT-2D

### Image:
```
photorealistic, 3D render, CGI, live action, real person, photograph, 
camera lens flare, depth of field blur, shadow realism, 
embedded text, formula in illustration, subtitle, watermark, third-party logo,
wrong force direction, scientifically incorrect diagram,
busy background, gradient sky, dark theme, monochrome
```

### Video:
```
camera pan, camera zoom, camera shake, camera movement of any kind,
character morphing, style inconsistency between frames,
photorealistic transition, 3D render, live action,
embedded text, subtitle, formula in animation,
scientifically impossible motion, wrong current direction, wrong needle direction,
more than 5 simultaneous moving objects
```

---

## 12. Khi nào dùng preset này

| Tình huống | Dùng EDU-FLAT-2D? |
|---|---|
| Giải thích nguyên lý bằng sơ đồ (cảm ứng, mạch điện, quang học) | ✅ Ưu tiên |
| Minh họa định luật, quy tắc (Lenz, Fleming, Ohm) | ✅ Ưu tiên |
| Video dài >5 phút cần nhiều segment | ✅ Phù hợp |
| Cần người thật giảng bài | ❌ Dùng PRESET-01 |
| Cần render 3D photorealistic (phân tử, thiên văn) | ❌ Dùng PRESET-02 |
| Cần người thật + 3D overlay | ❌ Dùng PRESET-03 |

---

## 13. Ghi chú sản xuất

- Âm nhạc: nhạc nền điện tử nhẹ nhàng, upbeat, không lời — style tương tự Lo-fi edu
- Không voice-over trong frame — animation tự kể câu chuyện qua labels
- Voice-over (nếu có) record riêng, sync theo beat
- Xuất file: MP4 H.264, 1280×720, 30fps
- Font khuyến nghị: **Nunito ExtraBold** (labels), **Nunito Regular** (body text)
