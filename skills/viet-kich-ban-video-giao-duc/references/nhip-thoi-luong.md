# Nhịp thời lượng

> **Nguồn tính toán:** Xem `rules/CONG-THUC-SCENE-WORD.md` để tra bảng đầy đủ và công thức gốc.

## Bảng nhịp cảnh và số scene

| Dạng | Scene (8s/scene) | Scene (9s trung bình) | Scene (10s/scene) | Cấu trúc gợi ý |
|---|---:|---:|---:|---|
| 30 giây | 4 | 3 | 3 | 1 ý chính, hook ngay đầu |
| 60 giây | 8 | 7 | 6 | Hook → Giải thích → Chốt |
| 3 phút | 23 | 20 | 18 | Chia 3 nhịp, có ví dụ |
| 5 phút | 38 | 33 | 30 | Chia chương, có câu hỏi xen |
| 10 phút | **75** | **67** | **60** | Segment + checkpoint |
| 20 phút | 150 | 133 | 120 | Chia 2 segment; bài tập xen |
| 30 phút | 225 | 200 | 180 | 3 segment; checkpoint mỗi 10 phút |
| 45 phút (giáo án) | ~338* | ~300* | ~270* | *Xem chú thích bên dưới |
| 60 phút | 450 | 400 | 360 | 4 segment; bài tập + kết |

> **(*) Giáo án 45 phút thực tế:** Không phải toàn bộ là video liên tục.  
> Phần cần sản xuất video: ~30 phút (bỏ ~15 phút HS làm bài).  
> 30 phút video = **200–225 scene**, không phải 338.

## Tốc độ lời dẫn tiếng Việt (chuẩn duy nhất)

| Tình huống | Tốc độ giây | Tốc độ phút |
|---|---|---|
| **Chuẩn lip-sync** (giải thích bình thường) | **2.5 từ/giây** | **150 từ/phút** |
| Nói chậm (khái niệm khó, công thức) | 2.0 từ/giây | 120 từ/phút |
| Nói nhanh (tóm tắt, chuyển cảnh) | 3.0 từ/giây | 180 từ/phút |
| TTS (FPT.AI / ElevenLabs) | Đặt **speed = 0.95×** | ~142 từ/phút |
| Người thật đọc trong studio | Review bằng tai; mục tiêu 2.5 từ/giây | — |

> **GATE 3 kiểm định:** Script vượt số từ cho phép → 🟠 MAJOR.

## Tính số từ và số scene nhanh

```
CÔNG THỨC GỐC (không được thay đổi):
  1 scene = 8–10 giây
  1 giây  = 2.5 từ  ← chuẩn lip-sync

Số scene = Tổng giây ÷ Giây/scene
Số từ    = Tổng giây × 2.5

Từ/scene theo thời lượng:
  Scene 8s  = 20 từ
  Scene 9s  = 22 từ   ← trung bình dùng
  Scene 10s = 25 từ

Ví dụ kiểm nhanh:
  60 giây  → 6–8 scene; 150 từ
  10 phút  → 60–75 scene; 1.500 từ
  30 phút* → 200–225 scene; 4.500 từ  (* phần video của giáo án 45 phút)
```
