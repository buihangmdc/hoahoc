# Image Prompts — Video Nhiệt học 60 giây
## Preset: MOTION-TYPE (Công Thức Động)
**Phiên bản:** 2.0 (Đã sửa khoa học + tăng chiều sâu)
**Tổng số ảnh:** 5 ảnh reference
**Độ phân giải:** 1280×720 (16:9), PNG

> **SCIENCE LOCK (toàn bộ file):**
> Công thức chuẩn: **ΔU = Q − A** (SGK KNTT 2018)
> A = công hệ thực hiện | A > 0 hệ làm công | A < 0 nhận công từ ngoài
> KHÔNG dùng ΔU = Q + A_outside (tránh nhầm lẫn quy ước dấu)

---

## IMAGE PROMPT 1 — CLIP 1 (Hook & Title)
**Thời lượng tương ứng:** 0:00–0:09
**Mục đích:** Bắt chú ý, đặt vấn đề

```
[MOTION-TYPE VISUAL ANCHOR: Kinetic typography animation on deep dark #0F0F1A background.
Clean mathematical typography, LaTeX-style rendering.
Color system: main text #E8E8F0, results #FFD700, highlight box #FFB74D, dim #8888AA.
No illustrations. No characters. No background texture.
Maximum 40% screen filled. Negative space intentional.]

[CLIP: 1 — HOOK: Tiêu đề FIRST LAW xuất hiện]

[CONTENT AT FRAME END — exact pixel positions:
  ZONE 1 (top 15%):
    "THERMODYNAMICS" — size 40px, color #8888AA (đã giải thích, mờ)
    position: horizontally centered, y = 8% from top
  
  ZONE 2 (center 60%):
    "FIRST LAW" — size 72px, color #FFD700, bold
    position: horizontally centered, y = 38% from top
    Highlight box: border #FFB74D, 2px solid, border-radius 6px, no fill
    padding: 8px horizontal, 6px vertical
  
  ZONE 3 (lower center, 65%):
    "Năng lượng không sinh ra, không mất đi"
    size 28px, color #E8E8F0, Poppins Regular
    position: horizontally centered, y = 65% from top

  BACKGROUND: pure #0F0F1A — no gradients, no texture]

[STAGE: title — tiêu đề xuất hiện, chưa có công thức]

[PATTERN: Sequential Reveal — "THERMODYNAMICS" xuất hiện trước, thu nhỏ, sau đó "FIRST LAW" xuất hiện]

SCIENCE ACCURACY LOCK:
  - "FIRST LAW" = Định luật I Nhiệt động lực học ✓
  - "THERMODYNAMICS" = Nhiệt động lực học ✓
  - Không có công thức hay ký hiệu vật lý sai ở frame này ✓

COMPOSITION:
  - Chỉ 3 text elements. Không illustration, không icon.
  - Khoảng trắng dưới cùng 25% màn hình — trống hoàn toàn
  - Watermark area: góc trên phải 80×80px — để trống

STYLE: 3Blue1Brown kinetic typography aesthetic. Dark science visualization.
1280×720. PNG.
```

---

## IMAGE PROMPT 2 — CLIP 2 (Công thức chính)
**Thời lượng tương ứng:** 0:09–0:18
**Mục đích:** Reveal công thức ΔU = Q − A với color mapping từng ký hiệu

```
[MOTION-TYPE VISUAL ANCHOR: Kinetic typography on deep dark #0F0F1A.
Color system: ΔU result #FFD700, Q variable #64B5F6, minus sign #EF5350,
A constant #81C784, main text #E8E8F0, dim #8888AA.
Static frame. No camera movement.]

[CLIP: 2 — CÔNG THỨC: ΔU = Q − A với color mapping]

[CONTENT AT FRAME END — exact specifications:
  ZONE 1 (top 12%):
    "FIRST LAW" — size 32px, color #8888AA (dim, carry-over từ CLIP 1)
    "THERMODYNAMICS" — size 24px, color #8888AA
    Both horizontally centered, y = 8%

  ZONE 2 (center formula — y = 42%):
    CÔNG THỨC CHÍNH: "ΔU = Q − A"
    Kích thước tổng thể: chiều rộng ~60% màn hình, centered
    
    Từng ký hiệu:
    • "ΔU" — size 72px, color #FFD700 (result/gold), bold
      Highlight box #FFB74D, 2px solid, border-radius 4px
    • "=" — size 72px, color #E8E8F0 (trắng)
    • "Q" — size 72px, color #64B5F6 (xanh nhạt — biến số)
    • "−" — size 72px, color #EF5350 (đỏ — CHÚ Ý dấu trừ!)
    • "A" — size 72px, color #81C784 (xanh lá — đại lượng công)
    
    Spacing: đều nhau, không chèn quá gần

  ZONE 3 (below formula — y = 65%):
    Label gắn dưới mỗi ký hiệu (aligned với ký hiệu tương ứng):
    • Dưới ΔU: "nội năng" — 24px, #8888AA
    • Dưới Q: "nhiệt nhận" — 24px, #8888AA
    • Dưới A: "công thực hiện" — 24px, #8888AA

  BACKGROUND: pure #0F0F1A]

[STAGE: formula-complete — công thức đầy đủ với color coding và labels]

[PATTERN: Color-mapping — mỗi ký hiệu có màu thể hiện vai trò vật lý]

SCIENCE ACCURACY LOCK:
  - Công thức: ΔU = Q − A ✓ (theo SGK KNTT 2018, KB mục 1.2)
  - Dấu: PHẢI LÀ DẤU TRỪ "−" không phải dấu cộng "+" ✓
  - ΔU (gold): kết quả, đại lượng cần tính ✓
  - Q (blue): nhiệt lượng nhận được ✓
  - A (green): công hệ thực hiện lên ngoài ✓
  - Label: "công thực hiện" — không viết "công từ ngoài" hoặc "công ngoại lực" ✓

COMPOSITION:
  - Công thức centered, vertically at 42%
  - Labels nhỏ dưới formula — không che khuất
  - Khoảng trắng hai bên >= 20% mỗi bên
  - Watermark area: upper-right 80×80px clear

STYLE: 3Blue1Brown kinetic typography. Clean, minimal, dark.
1280×720. PNG.
```

---

## IMAGE PROMPT 3 — CLIP 3 (Quy ước dấu)
**Thời lượng tương ứng:** 0:18–0:30
**Mục đích:** Giải thích ý nghĩa dấu Q và A — hai breakdown lines

```
[MOTION-TYPE VISUAL ANCHOR: Kinetic typography on deep dark #0F0F1A.
Color system: variables #64B5F6, constants #81C784, energy #EF5350,
main #E8E8F0, dim #8888AA, units #80CBC4.
Static frame.]

[CLIP: 3 — QUY ƯỚC DẤU: Breakdown Q và A]

[CONTENT AT FRAME END — exact positions:
  ZONE 1 (top 15%):
    "ΔU = Q − A" — dim version: ΔU=#8888AA, Q=#8888AA, −=#8888AA, A=#8888AA
    size 40px, centered, y = 8%
    Highlight box focus đặt xung quanh cả "Q − A" (không phải ΔU)

  ZONE 2 (Breakdown Q — y = 32%):
    Tiêu đề: "NHIỆT LƯỢNG Q" — 28px, color #64B5F6, bold, left-aligned từ 8%
    
    Line 1a: "Q > 0 : hệ nhận nhiệt   ↑ nội năng tăng"
      • "Q" — #64B5F6 | "> 0" — #E8E8F0 | ":" — #E8E8F0
      • "hệ nhận nhiệt" — #80CBC4 (context)
      • "↑ nội năng tăng" — #81C784 (positive outcome)
      size 30px
    
    Line 1b: "Q < 0 : hệ tỏa nhiệt    ↓ nội năng giảm"
      • "Q" — #64B5F6 | "< 0" — #E8E8F0
      • "hệ tỏa nhiệt" — #80CBC4
      • "↓ nội năng giảm" — #EF5350 (negative outcome)
      size 30px

  DIVIDER: thin horizontal line #333344 at y = 54%

  ZONE 3 (Breakdown A — y = 62%):
    Tiêu đề: "CÔNG HỆ THỰC HIỆN A" — 28px, color #81C784, bold, left-aligned từ 8%
    
    Line 2a: "A > 0 : hệ làm công ra    ΔU = Q − A < Q"
      • "A" — #81C784 | "> 0" — #E8E8F0
      • "hệ làm công ra" — #80CBC4
      • "ΔU = Q − A < Q" — #EF5350 (giảm so với Q)
      size 30px
    
    Line 2b: "A < 0 : nhận công từ ngoài  ΔU = Q − A > Q"
      • "A" — #81C784 | "< 0" — #E8E8F0
      • "nhận công từ ngoài" — #80CBC4
      • "ΔU = Q − A > Q" — #81C784 (tăng so với Q)
      size 30px

  BACKGROUND: pure #0F0F1A]

[STAGE: breakdown-complete — cả hai breakdown lines Q và A đã xuất hiện đầy đủ]

[PATTERN: Sequential Reveal — line Q xuất hiện trước, sau đó line A]

SCIENCE ACCURACY LOCK:
  - Q > 0: hệ nhận nhiệt ← đúng SGK KNTT ✓
  - Q < 0: hệ tỏa nhiệt ← đúng SGK KNTT ✓
  - A > 0: hệ làm công LÊN NGOÀI ← đúng (work BY system) ✓
  - A < 0: nhận công TỪ NGOÀI ← đúng (external does work on system) ✓
  - "ΔU = Q − A < Q" khi A > 0 ← đúng (làm công → mất năng lượng) ✓
  - KHÔNG viết "A > 0: ngoại lực làm công" ← SAI, đó là A < 0 mới đúng ✓

COMPOSITION:
  - 2 zones rõ ràng, divider ở giữa
  - Left-aligned text cho dễ đọc theo hàng
  - Labels khoảng cách đủ rộng

STYLE: kinetic typography, clean breakdown layout.
1280×720. PNG.
```

---

## IMAGE PROMPT 4 — CLIP 4 (Ví dụ số)
**Thời lượng tương ứng:** 0:30–0:42
**Mục đích:** Ví dụ cụ thể với số: Q=800J, A=200J → ΔU=600J

```
[MOTION-TYPE VISUAL ANCHOR: Kinetic typography on deep dark #0F0F1A.
Color system: result #FFD700, highlight #FFB74D, variables #64B5F6,
constants #81C784, main #E8E8F0, dim #8888AA, units #80CBC4.
Static frame.]

[CLIP: 4 — VÍ DỤ SỐ: Khí đẳng áp nhận nhiệt và làm công]

[CONTENT AT FRAME END — exact positions:
  ZONE 1 (top label — y = 6%):
    "Ví dụ: Khí đẳng áp (p = const)"
    size 28px, color #FFB74D (highlight cam), left-aligned từ 5%

  ZONE 2 (given data — y = 20%):
    "Cho:" — 26px, #E8E8F0
    Line: "Q  =  +800  J   (nhận nhiệt)"
      • "Q" #64B5F6 | "= +800" #E8E8F0 | "J" #80CBC4 | "(nhận nhiệt)" #8888AA
      size 34px
    Line: "A  =  +200  J   (hệ làm công)"
      • "A" #81C784 | "= +200" #E8E8F0 | "J" #80CBC4 | "(hệ làm công)" #8888AA
      size 34px

  ZONE 3 (calculation — y = 50%):
    Mũi tên "⟹" — size 40px, color #E8E8F0, centered
    
    "ΔU  =  Q  −  A"
    size 44px, colored as per CLIP 2: ΔU=#FFD700, Q=#64B5F6, −=#EF5350, A=#81C784
    
    Next line (y=58%):
    "ΔU  =  800  −  200"
    size 44px, color #E8E8F0, number substituted

  ZONE 4 (result — y = 72%):
    Large box (#FFB74D border, 2px, radius 6px, no fill):
    "ΔU  =  600  J" — size 56px, color #FFD700, bold, centered
    Caption below: "(Nội năng tăng 600 Jun)" — size 24px, #80CBC4

  BACKGROUND: pure #0F0F1A]

[STAGE: result — phép tính hoàn chỉnh, kết quả highlighted]

[PATTERN: Transform — dữ kiện → công thức → thay số → kết quả]

SCIENCE ACCURACY LOCK:
  - Đẳng áp (p = const): khí nhận nhiệt và giãn nở ✓
  - Q = +800 J: hệ nhận nhiệt (Q > 0) ✓
  - A = +200 J: hệ thực hiện công (A > 0, khí đẩy piston) ✓
  - ΔU = Q − A = 800 − 200 = 600 J ✓ (tính toán chính xác)
  - ΔU < Q (600 < 800): đúng — một phần nhiệt thành công ✓
  - Không suy ra ΔU = Q + A (TUYỆT ĐỐI KHÔNG) ✓

COMPOSITION:
  - Flow từ trên xuống: Dữ kiện → Công thức → Thay số → Kết quả
  - Result box ở dưới cùng, lớn, nổi bật
  - Spacing đủ rộng giữa các zone

STYLE: kinetic typography, step-by-step calculation reveal.
1280×720. PNG.
```

---

## IMAGE PROMPT 5 — CLIP 5 (Tóm tắt)
**Thời lượng tương ứng:** 0:42–0:51
**Mục đích:** 3 điểm mnemonic — học sinh nhớ lâu

```
[MOTION-TYPE VISUAL ANCHOR: Kinetic typography on deep dark #0F0F1A.
Color system: result #FFD700, text #E8E8F0, check #81C784, dim #8888AA.
Static frame.]

[CLIP: 5 — TÓM TẮT: 3 điểm cần nhớ]

[CONTENT AT FRAME END — exact positions:
  ZONE 1 (tiêu đề — y = 8%):
    "LUẬT I NHIỆT ĐỘNG LỰC HỌC" — 32px, #8888AA, centered
    Dimmed so main content stands out

  ZONE 2 (3 điểm — y starting 28%):
    Spacing: mỗi điểm cách nhau 20% chiều cao
    
    ĐIỂM 1 (y = 28%):
    "① ΔU = Q − A"
    • "①" — 36px, #FFB74D | "ΔU" — 44px, #FFD700 | "= Q − A" — 44px, #E8E8F0
    Checkmark ✓ (#81C784, 30px) ở cuối dòng
    
    ĐIỂM 2 (y = 48%):
    "② Dấu xác định chiều năng lượng"
    • "②" — 36px, #FFB74D | text — 36px, #E8E8F0
    Sub-label (y=54%): "Q(+) nhận | Q(−) tỏa | A(+) làm công | A(−) nhận công"
    Sub-label: 22px, #8888AA
    Checkmark ✓ (#81C784, 30px) ở cuối dòng 2
    
    ĐIỂM 3 (y = 70%):
    "③ Năng lượng bảo toàn — không có động cơ vĩnh cửu"
    • "③" — 36px, #FFB74D | text — 32px, #E8E8F0
    Checkmark ✓ (#81C784, 30px) ở cuối dòng 3

  BACKGROUND: pure #0F0F1A]

[STAGE: summary — 3 điểm đầy đủ, static hold frame]

[PATTERN: Numbered list reveal — xuất hiện theo thứ tự 1→2→3]

SCIENCE ACCURACY LOCK:
  - "ΔU = Q − A" ← đúng công thức chuẩn ✓
  - "Dấu xác định chiều năng lượng" ← đúng ý nghĩa vật lý ✓
  - "Không có động cơ vĩnh cửu" ← hệ quả trực tiếp Luật I ✓
  - Checkmark ✓ chỉ gắn với khẳng định đúng ✓

COMPOSITION:
  - 3 điểm cách đều nhau
  - Số ① ② ③ màu cam để dễ nhìn
  - Phần dưới cùng 10% trống (breathing room)
  - Watermark area upper-right 80×80px clear

STYLE: kinetic typography, conclusion/summary frame. Clean.
1280×720. PNG. This frame will HOLD for 0:51–1:00 in final video.
```

---

## Bảng kiểm định toàn bộ 5 ảnh

| # | Clip | Công thức hiển thị | Dấu | Science ✓ |
|---|------|-------------------|-----|-----------|
| 1 | Hook | Không (chỉ title) | N/A | ✓ |
| 2 | Formula | **ΔU = Q − A** | Dấu **−** màu đỏ | ✓ |
| 3 | Breakdown | **A > 0: hệ làm công** | Đúng quy ước | ✓ |
| 4 | Example | **ΔU = 800 − 200 = 600 J** | Tính đúng | ✓ |
| 5 | Summary | **ΔU = Q − A** | Nhất quán | ✓ |

**Quy tắc màu nhất quán:**
- ΔU = `#FFD700` (vàng gold — kết quả)
- Q = `#64B5F6` (xanh nhạt — biến số nhiệt)
- Dấu "−" = `#EF5350` (đỏ — nhấn mạnh)
- A = `#81C784` (xanh lá — công)
- Dim/giải thích xong = `#8888AA`
- Highlight box = `#FFB74D`
- Nền = `#0F0F1A`

**Bàn giao:**
- 5 PNG files (1 cho mỗi clip)
- Tên file: `IMG-1-HOOK.png` → `IMG-5-SUMMARY.png`
- Format: PNG, 1280×720, sRGB, không nền trắng
