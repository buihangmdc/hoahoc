# Video Prompts — Video Nhiệt học 60 giây
## Preset: MOTION-TYPE (Công Thức Động)
**Phiên bản:** 2.0 (Đã sửa khoa học, timing, bỏ tên công cụ)
**Tổng số clip:** 5 clip animation
**Thời lượng:** clip tối đa 9s, hold cuối 9s
**Tổng:** 51s animation + 9s hold = 60s với voice-over

> **SCIENCE LOCK (toàn file):**
> Công thức chuẩn: **ΔU = Q − A** (SGK KNTT 2018, KB mục 1.2)
> A = công hệ thực hiện | A > 0: hệ làm công | A < 0: nhận công từ ngoài

> **CONTINUITY RULE:**
> END STATE của Clip N = START STATE của Clip N+1
> Không re-animate phần tử đã xuất hiện — chỉ dim hoặc giữ nguyên

---

## VIDEO PROMPT 1 — CLIP 1 (Hook & Title)
**Thời lượng:** 9 giây (0:00–0:09)
**Reference image:** IMG-1-HOOK.png
**Mục đích:** Bắt chú ý, tiêu đề xuất hiện

```
[MOTION-TYPE CONTINUITY ANCHOR: Kinetic typography on deep dark #0F0F1A background.
Color system: main #E8E8F0, results #FFD700, highlight #FFB74D, dim #8888AA.
No illustrations. No characters. Static frame — no camera movement whatsoever.]

ANIMATE FROM REFERENCE IMAGE. 9 seconds. CLIP 1.

START STATE (frame 0:00):
  Screen empty. Pure dark #0F0F1A. Nothing visible.

ANIMATION SEQUENCE:
  0:00–0:02: "THERMODYNAMICS" appears character by character from horizontal center,
             color #E8E8F0, size 56px. Each character writes in place (no flying),
             left to right, 0.07s per character. Total: ~1.4s for 14 chars.
  
  0:02–0:03: "THERMODYNAMICS" scales down (0.7x) and translates up to y=8%.
             Color simultaneously dims: #E8E8F0 → #8888AA.
             Easing: ease-in-out, 0.8s.
  
  0:03–0:06: "FIRST LAW" appears character by character from center,
             color #FFD700, size 72px. Write-in-place, 0.1s per char.
             Total: ~0.9s for 9 chars.
  
  0:06–0:07: Highlight box (#FFB74D, 2px border, radius 6px, no fill)
             scales in around "FIRST LAW": scale 0→1, ease-out, 0.4s.
  
  0:07–0:09: Subtitle "Năng lượng không sinh ra, không mất đi" fades in,
             size 28px, color #E8E8F0, centered, y=65%.
             Fade: opacity 0→1, 0.5s ease-in.
  
  0:09: All elements hold. No further animation.

END STATE (frame 9s):
  y=8%: "THERMODYNAMICS" dim #8888AA, size 40px
  y=38%: "FIRST LAW" bright #FFD700, size 72px, inside highlight box
  y=65%: "Năng lượng không sinh ra, không mất đi" #E8E8F0, size 28px
  Background: pure #0F0F1A

MOTION RULES:
  - All text appears IN PLACE — no flying, no slide-in
  - Scale and translate only for "THERMODYNAMICS" (step 0:02–0:03)
  - Camera: absolutely static, no zoom, no pan
  
SCIENCE ACCURACY LOCK:
  - "THERMODYNAMICS": correct spelling ✓
  - "FIRST LAW": First Law of Thermodynamics (Định luật I) ✓
  - "Năng lượng không sinh ra, không mất đi": phát biểu chính xác Luật I ✓

SOUND: Ambient sci-tech hum, soft rise at 0:04 when "FIRST LAW" appears.
       Subtle chime at 0:06 when highlight box appears. No voice. No subtitles.
```

---

## VIDEO PROMPT 2 — CLIP 2 (Công thức chính)
**Thời lượng:** 9 giây (0:09–0:18)
**Reference image:** IMG-2-FORMULA.png
**Mục đích:** ΔU = Q − A reveal với color mapping

```
[MOTION-TYPE CONTINUITY ANCHOR: Kinetic typography on deep dark #0F0F1A.
Color system: ΔU #FFD700, Q #64B5F6, minus sign #EF5350, A #81C784, main #E8E8F0.
Static frame.]

ANIMATE FROM REFERENCE IMAGE. 9 seconds. CLIP 2.

START STATE (frame 0:00 of this clip = 0:09 of video):
  [CARRY-OVER from CLIP 1 — do NOT re-animate these:]
  y=8%: "THERMODYNAMICS" dim #8888AA, size 40px
  y=38%: "FIRST LAW" #FFD700 with highlight box
  y=65%: subtitle #E8E8F0
  [All three elements remain visible but static]

ANIMATION SEQUENCE:
  0:00–0:01 of clip (=0:09–0:10 video):
    "FIRST LAW" and subtitle simultaneously fade to dim: opacity 100%→40%.
    Subtitle translates up slightly (+5% y). Duration 0.6s ease-in-out.
    [Making space for main formula]
  
  0:01–0:03: "ΔU" appears at horizontal center, y=42%.
             Color #FFD700, size 72px. Write-in-place, 0.15s per char (2 chars → 0.3s).
             Highlight box (#FFB74D, 2px, radius 4px) scales in: 0.4s ease-out.
  
  0:03–0:04: "=" appears immediately right of ΔU.
             Color #E8E8F0, size 72px. Fade-in 0.3s.
  
  0:04–0:05: "Q" appears right of "=".
             Color #64B5F6 (variable blue), size 72px. Write-in-place, 0.15s.
  
  0:05–0:06: "−" appears right of Q.
             Color #EF5350 (red — emphasize the MINUS sign!), size 72px.
             IMPORTANT: This MUST be a minus "−" NOT a plus "+". Fade-in 0.4s.
  
  0:06–0:07: "A" appears right of "−".
             Color #81C784 (constant green), size 72px. Write-in-place, 0.15s.
  
  0:07–0:08: Labels appear below each symbol, fading in simultaneously:
             "nội năng" below ΔU | "nhiệt nhận" below Q | "công thực hiện" below A
             Size 24px, color #8888AA. Fade-in 0.5s.
  
  0:08–0:09: All elements hold. Highlight box steady on ΔU.

END STATE (frame 9s of clip):
  [CARRY-OVER headers still visible dim at top]
  Center (y=42%): Full formula "ΔU = Q − A" with color coding:
    ΔU=#FFD700 with box, =#E8E8F0, Q=#64B5F6, −=#EF5350, A=#81C784
  Below formula (y=60%): labels "nội năng" | "nhiệt nhận" | "công thực hiện"
  Background: #0F0F1A

MOTION RULES:
  - All text writes in place. Box scales in place.
  - No flying elements. Static frame, no camera movement.
  
SCIENCE ACCURACY LOCK:
  - Formula: ΔU = Q − A (MINUS sign, NOT plus) ✓
  - Color #EF5350 on "−" draws attention to the crucial minus sign ✓
  - A = "công thực hiện" (NOT "công từ ngoài" / "công ngoại lực") ✓
  - Formula matches SGK KNTT 2018, KB mục 1.2 ✓

SOUND: Soft chime at 0:06 when "−" appears (red = important).
       Chord resolution at 0:08 when labels fade in. Ambient continues.
       No voice, no subtitles.
```

---

## VIDEO PROMPT 3 — CLIP 3 (Quy ước dấu)
**Thời lượng:** 9 giây (0:18–0:27)
**Reference image:** IMG-3-BREAKDOWN.png
**Mục đích:** Giải thích Q và A với quy ước dấu

```
[MOTION-TYPE CONTINUITY ANCHOR: Kinetic typography on deep dark #0F0F1A.
Color system: variables #64B5F6, constants #81C784, energy #EF5350,
main #E8E8F0, dim #8888AA, units #80CBC4.
Static frame.]

ANIMATE FROM REFERENCE IMAGE. 9 seconds. CLIP 3.

START STATE (frame 0:00 of clip = 0:18 video):
  [CARRY-OVER from CLIP 2:]
  Top headers: "THERMODYNAMICS" + "FIRST LAW" dim
  Center (y=42%): formula "ΔU = Q − A" fully visible with color coding and labels
  [DO NOT re-animate these — they are static carry-over]

ANIMATION SEQUENCE:
  0:00–0:01: Formula "ΔU = Q − A" dims further → all symbols → #8888AA.
             Labels below also dim. Highlight box moves to surround "Q − A" (not just ΔU).
             Duration 0.5s ease-in-out.
  
  0:01–0:02: Section header "NHIỆT LƯỢNG Q" appears at y=28%, left-aligned.
             Color #64B5F6, size 28px, bold. Fade-in 0.3s.
  
  0:02–0:04: Breakdown line Q1 slides in from left margin:
             "Q > 0 : hệ nhận nhiệt   ↑ nội năng tăng"
             Slide-in: x from -100% → 0, ease-out, 0.5s.
             Colors: "Q" #64B5F6, "> 0" #E8E8F0, "hệ nhận nhiệt" #80CBC4,
                     "↑" #81C784, "nội năng tăng" #81C784.
             Position: y=35%, left-aligned from 8%.
  
  0:04–0:05: Breakdown line Q2 slides in from left:
             "Q < 0 : hệ tỏa nhiệt    ↓ nội năng giảm"
             Same style. Colors: "↓" #EF5350, "nội năng giảm" #EF5350.
             Position: y=42%.
  
  0:05–0:05.5: Thin horizontal divider line appears at y=52%, color #333344, 0.3s.
  
  0:05.5–0:06: Section header "CÔNG HỆ THỰC HIỆN A" at y=56%.
               Color #81C784, size 28px. Fade-in 0.3s.
  
  0:06–0:07.5: Breakdown line A1 slides in from left:
               "A > 0 : hệ làm công ra    ΔU < Q"
               Slide-in, 0.5s.
               Colors: "A" #81C784, "> 0" #E8E8F0, "hệ làm công ra" #80CBC4,
                       "ΔU < Q" #EF5350 (mất năng lượng qua công).
               Position: y=63%.
  
  0:07.5–0:09: Breakdown line A2 slides in from left:
               "A < 0 : nhận công từ ngoài   ΔU > Q"
               Same style. "ΔU > Q" color #81C784 (tăng vì được thêm công).
               Position: y=70%.

END STATE (frame 9s of clip):
  [Top: headers dim, formula dim, highlight box on "Q − A"]
  y=28%: "NHIỆT LƯỢNG Q" header #64B5F6
  y=35%: Q1 line fully visible
  y=42%: Q2 line fully visible
  y=52%: divider
  y=56%: "CÔNG HỆ THỰC HIỆN A" header #81C784
  y=63%: A1 line fully visible
  y=70%: A2 line fully visible
  Background: #0F0F1A

MOTION RULES:
  - Lines slide in from left. Headers fade in. Divider grows.
  - No camera movement. Static frame.
  
SCIENCE ACCURACY LOCK:
  - Q > 0: hệ nhận nhiệt ✓ (NOT "Q > 0: hệ tỏa nhiệt")
  - A > 0: hệ làm công RA NGOÀI ✓ (NOT "A > 0: ngoại lực làm công")
  - A < 0: NHẬN công từ ngoài ✓
  - "ΔU < Q" khi A > 0: đúng vì ΔU = Q − A, A > 0 → ΔU < Q ✓
  - "ΔU > Q" khi A < 0: đúng vì ΔU = Q − (−|A|) = Q + |A| > Q ✓

SOUND: Soft whoosh at 0:02 and 0:05.5 when sections appear. Ambient continues.
```

---

## VIDEO PROMPT 4 — CLIP 4 (Ví dụ số)
**Thời lượng:** 9 giây (0:27–0:36)
**Reference image:** IMG-4-EXAMPLE.png
**Mục đích:** Q=800J, A=200J → ΔU=600J, step-by-step

```
[MOTION-TYPE CONTINUITY ANCHOR: Kinetic typography on deep dark #0F0F1A.
Color system: result #FFD700, highlight #FFB74D, variables #64B5F6,
constants #81C784, main #E8E8F0, dim #8888AA, units #80CBC4.
Static frame.]

ANIMATE FROM REFERENCE IMAGE. 9 seconds. CLIP 4.

START STATE (frame 0:00 of clip = 0:27 video):
  [CARRY-OVER from CLIP 3:]
  All breakdown lines from CLIP 3 still visible but dim slightly.
  Formula at top dim.
  [DO NOT re-animate these]

ANIMATION SEQUENCE:
  0:00–0:01: All CLIP 3 content fades to dim: opacity → 30%, scale → 90%.
             Duration 0.6s ease-in. Space cleared for new content.
  
  0:01–0:02: Title "Ví dụ: Khí đẳng áp (p = const)" appears top-left, y=8%.
             Color #FFB74D, size 28px. Fade-in 0.4s.
  
  0:02–0:03: "Cho:" label appears at y=22%, left-aligned.
             Color #E8E8F0, size 26px. Fade-in 0.3s.
  
  0:03–0:04: First given: "Q = +800 J  (nhận nhiệt)" writes in.
             "Q" #64B5F6, "= +800" #E8E8F0, "J" #80CBC4, "(nhận nhiệt)" #8888AA.
             Size 34px. Write-in-place, 0.05s/char.
             Position: y=30%.
  
  0:04–0:05: Second given: "A = +200 J  (hệ làm công)" writes in.
             "A" #81C784, "= +200" #E8E8F0, "J" #80CBC4, "(hệ làm công)" #8888AA.
             Size 34px. Position: y=40%.
  
  0:05–0:06: Implication arrow "⟹" appears at y=52%, centered.
             Color #E8E8F0, size 40px. Fade-in 0.4s.
             Formula "ΔU = Q − A" appears after arrow, colored, size 40px.
  
  0:06–0:07: Substitution line writes in at y=60%:
             "ΔU = 800 − 200"
             Color #E8E8F0, size 40px. Write-in-place character by character.
  
  0:07–0:09: Result box appears at y=73%:
             Box: #FFB74D border, 2px, radius 6px.
             Inside: "ΔU = 600 J" — size 56px, color #FFD700, bold.
             Caption below: "(Nội năng tăng 600 Jun)" — 24px, #80CBC4.
             Box scales: 0→1 ease-out 0.4s, then holds.

END STATE (frame 9s of clip):
  y=8%: Title "Ví dụ: Khí đẳng áp" #FFB74D
  y=30%: Q=+800J data line
  y=40%: A=+200J data line
  y=52%: Arrow + formula
  y=60%: Substitution line
  y=73%: Result box "ΔU = 600 J" #FFD700
  Background: #0F0F1A

MOTION RULES:
  - Data lines write in place. Box scales in place.
  - All transitions sequential — no simultaneous reveals.
  - Static frame, no camera movement.
  
SCIENCE ACCURACY LOCK:
  - Khí đẳng áp (p = const): setup chính xác ✓
  - Q = +800 J > 0: nhận nhiệt ✓
  - A = +200 J > 0: hệ làm công (khí đẩy piston) ✓
  - ΔU = Q − A = 800 − 200 = 600 J ✓ (phép tính chính xác)
  - ΔU = 600 < Q = 800: hợp lý — một phần nhiệt thành công ✓
  - TUYỆT ĐỐI KHÔNG viết "ΔU = Q + A = 800 + 200 = 1000" ✓

SOUND: Soft chimes at each major step (0:03, 0:05, 0:07). 
       Result box: subtle success chord at 0:07. Ambient continues.
```

---

## VIDEO PROMPT 5 — CLIP 5 (Tóm tắt & Kết luận)
**Thời lượng:** 9 giây (0:36–0:45)
**Reference image:** IMG-5-SUMMARY.png
**Mục đích:** 3 điểm mnemonic — giữ frame đến 1:00

```
[MOTION-TYPE CONTINUITY ANCHOR: Kinetic typography on deep dark #0F0F1A.
Color system: result #FFD700, text #E8E8F0, check #81C784, dim #8888AA.
Static frame.]

ANIMATE FROM REFERENCE IMAGE. 9 seconds. CLIP 5.
NOTE: After clip ends, hold final frame until 1:00 (video editor adds 15s hold).

START STATE (frame 0:00 of clip = 0:36 video):
  [CARRY-OVER from CLIP 4: Example content still visible, dim]
  [DO NOT re-animate]

ANIMATION SEQUENCE:
  0:00–0:01.5: All CLIP 4 content fades and scales down: opacity → 15%, scale → 75%.
               This creates the "receding into background" effect. Duration 0.8s.
  
  0:01.5–0:02: Header "LUẬT I NHIỆT ĐỘNG LỰC HỌC" fades in at y=10%.
               Size 32px, color #8888AA (dim — supporting, not main). Fade 0.4s.
  
  0:02–0:04: Point 1 writes in at y=30%:
             "①  ΔU = Q − A"
             "①" color #FFB74D, size 36px.
             "ΔU" #FFD700, "= Q − A" colored (Q #64B5F6, − #EF5350, A #81C784).
             Size 44px. Write-in-place.
             Checkmark ✓ (#81C784, 30px) appears at end of line, fade-in.
  
  0:04–0:06: Point 2 writes in at y=50%:
             "②  Dấu xác định chiều năng lượng"
             "②" #FFB74D, text #E8E8F0. Size 36px.
             Sub-text at y=57%: "Q+ nhận | Q− tỏa  ·  A+ làm công | A− nhận công"
             Sub-text: 22px, #8888AA.
             Checkmark ✓ appears at end of main line.
  
  0:06–0:08: Point 3 writes in at y=72%:
             "③  Không có động cơ vĩnh cửu"
             "③" #FFB74D, text #E8E8F0. Size 36px.
             Sub-text at y=79%: "→ Năng lượng luôn bảo toàn"
             Sub-text: 22px, #8888AA.
             Checkmark ✓ appears at end.
  
  0:08–0:09: All 3 points fully visible. All 3 checkmarks visible. HOLD.

END STATE (frame 9s — HOLD FRAME until 1:00):
  y=10%: Header dim
  y=30%: Point 1: ΔU = Q − A ✓
  y=50%: Point 2: Dấu xác định chiều ✓
  y=72%: Point 3: Không có động cơ vĩnh cửu ✓
  Background: #0F0F1A
  [Background has faint receding content from previous clips for visual depth]

MOTION RULES:
  - Points write in sequence. Checkmarks fade in per point.
  - Background content just fades/scales (no translation).
  - Static frame, no camera movement.
  
SCIENCE ACCURACY LOCK:
  - "ΔU = Q − A" — công thức chuẩn ✓
  - "Dấu xác định chiều" — đúng ý nghĩa vật lý ✓
  - "Không có động cơ vĩnh cửu" — hệ quả chính xác của Luật I ✓
  - Checkmark ✓ chỉ trên khẳng định đúng ✓

SOUND: Subtle crescendo builds across 0:02–0:08.
       Small chime per checkmark. Final sustained chord at 0:08.
       Fade to silence at 0:09. No voice, no subtitles.

VIDEO EDITOR NOTE: Export clip 5 + hold last frame (freeze frame) for 15s.
Total CLIP 5 contribution to timeline: 9s animation + 15s hold = 24s (0:36–1:00).
Voice-over continues over hold frame per VOICE-SCRIPT-TTS.md.
```

---

## Continuity Chain — Kiểm tra liền mạch

| Clip | Thời lượng | START State | END State | Clip tiếp theo nhận |
|------|-----------|------------|----------|---------------------|
| CLIP 1 | 9s | Empty | Title + subtitle | Headers dim ✓ |
| CLIP 2 | 9s | Headers carry | Formula + labels | Formula dim, carry ✓ |
| CLIP 3 | 9s | Formula dim | Breakdown Q, A | Breakdown carry ✓ |
| CLIP 4 | 9s | Breakdown dim | Example + result | Example carry ✓ |
| CLIP 5 | 9s → hold | Example dim | 3 points + checks | Final hold ✓ |

**Tổng timeline video:**
```
0:00──────0:09──────0:18──────0:27──────0:36──────0:45──1:00
  CLIP 1    CLIP 2    CLIP 3    CLIP 4    CLIP 5   HOLD FRAME
  [Hook]   [Formula] [Breakdwn][Example]  [Summary][Voice only]
```

---

## Lưu ý kỹ thuật

**Nếu video tool giới hạn clip < 9s:**
- Chia CLIP 3 → 3A (Q) + 3B (A), mỗi 4.5s
- Chia CLIP 4 → 4A (setup) + 4B (result), mỗi 4.5s
- Tổng: 7 clips × ~4-5s = ~35s + 25s hold

**Post-production ghép clip:**
```bash
# Ghép 5 clip thành video không tiếng
ffmpeg -i clip1.mp4 -i clip2.mp4 -i clip3.mp4 -i clip4.mp4 -i clip5_with_hold.mp4 \
  -filter_complex "[0:v][1:v][2:v][3:v][4:v]concat=n=5:v=1:a=0[v]" \
  -map "[v]" video-no-audio.mp4

# Add voice-over
ffmpeg -i video-no-audio.mp4 -i voice-60s.wav \
  -c:v copy -c:a aac -shortest video-final.mp4
```

**Kiểm định trước bàn giao:**
- ✓ 5 clip, mỗi clip ≤ 9s
- ✓ Clip 5 có hold frame đến 1:00
- ✓ Continuity: END Clip N = START Clip N+1
- ✓ Công thức: luôn là "ΔU = Q − A" (dấu trừ)
- ✓ A > 0: hệ làm công (KHÔNG phải "ngoại lực làm công")
- ✓ Ví dụ số: 800 − 200 = 600 (KHÔNG phải 800 + 200 = 1000)
- ✓ Màu sắc theo PRESET-07 color system
- ✓ Không có illustration, nhân vật, background động
- ✓ Static frame, không camera movement
