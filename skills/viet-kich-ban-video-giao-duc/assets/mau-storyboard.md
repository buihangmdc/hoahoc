# Storyboard video giáo dục

> **Quy tắc:** Mỗi hàng = 1 cảnh (scene). ID cảnh dùng `SC01`, `SC02`... — phải khớp với image prompt và video prompt cùng ID.  
> Không để cột "Kiểm định" trống — điền ✓ (pass) hoặc lỗi cụ thể sau khi review.

---

## BƯỚC 0 — NARRATIVE SPINE (bắt buộc viết TRƯỚC khi điền storyboard)

> Narrative spine là sợi chỉ logic xuyên suốt video. Mỗi mũi tên = một cảnh.  
> Dạng: **[Điều học sinh đã biết / câu hỏi được nêu]** → **[Điều cảnh này giải đáp/bổ sung]** → **[Câu hỏi/vấn đề mở ra cho cảnh tiếp]**

| # | Học sinh vào cảnh biết gì? | Cảnh này dạy/cho thấy điều gì? | Câu hỏi/tension mở ra cho cảnh sau |
|---|--------------------------|-------------------------------|-------------------------------------|
| SC01 | *(học sinh chưa biết gì về chủ đề)* | Hook: hiện tượng kỳ lạ/câu hỏi gây tò mò | *"Tại sao lại xảy ra điều đó?"* |
| SC02 | Đã thấy hiện tượng, tò mò nguyên nhân | Khái niệm/công thức giải thích | *"Nhưng công thức áp dụng thế nào?"* |
| SC03 | Hiểu khái niệm trừu tượng | Ví dụ cụ thể / thí nghiệm minh họa | *"Còn trong thực tế thì sao?"* |
| SC04 | Thấy ví dụ | Vận dụng / bài tập / so sánh | *"Học sinh đã nắm chưa?"* |
| SC05 | Đã luyện tập | Chốt, tổng kết, ghi nhớ | — |

> **Quy tắc spine:** Cột 2 của SC(n) phải là câu trả lời cho cột 4 của SC(n−1).  
> Nếu không trả lời được → đảo thứ tự cảnh hoặc thêm cảnh chuyển tiếp.

---

## Bảng khóa công thức/góc máy

Điền bảng này trước storyboard nếu video có công thức, vectơ, đồ thị hoặc hướng chuyển động.

| ID | Phát biểu/công thức chuẩn | Điều kiện và quy ước dấu | Mặt phẳng/chiều dương | Góc máy và trục cấm vượt | Science freeze-frame |
|---|---|---|---|---|---|
| [FORMULA-ID] | | | | | [SCxx, timecode] |

## Bảng storyboard

| Cảnh | Timecode | Mục đích sư phạm | Cầu nối | ID/beat công thức | Visual | Camera geometry | Graphics / Overlay | Freeze-frame | Lời dẫn / Thoại | Câu mở đầu transition | Chữ hậu kỳ | Âm thanh | Nguồn | Kiểm định |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SC01 | 0:00–0:08 | Gợi tò mò | *(cảnh đầu)* | THERM-1ST-01 / PHENOMENON | Mặt cắt piston, khí bị nén | Trung cảnh chính diện; camera khóa; không vượt trục piston | Biên hệ và mũi tên chuyển động, thêm hậu kỳ | 0:06 | “Tại sao khi nén nhanh, khí có thể nóng lên?” | — | Không hiện công thức | SFX nén | [ID nguồn thật] | ✓/lỗi |
| SC02 | 0:08–0:16 | Khóa hệ và quy ước công | Trả lời câu hỏi SC01 | THERM-1ST-01 / SYSTEM+DIRECTION | Giữ nguyên piston | Cùng góc SC01 | `A>0` khi khí nhận công; lớp vector | 0:14 | “Vì môi trường thực hiện công lên khí, năng lượng của hệ thay đổi…” | “Quan hệ đó viết thế nào?” | `ΔU=Q+A`, kèm định nghĩa dấu | SFX pop-in | [ID nguồn thật] | ✓/lỗi |
| SC03 | | | | | | | | | | | | | | |
| SC04 | | | | | | | | | | | | | | |
| SC05 | | | | | | | | | | | | | | |

---

## Continuity bible của video

- **Nhân vật / người dẫn:** [Tên, giới tính, giọng nói]
- **Trang phục:** [Mô tả — không thay đổi giữa các cảnh]
- **Bối cảnh:** [Lớp học / studio / 2D animation]
- **Dụng cụ:** [Danh sách, số lượng cố định]
- **Quy ước màu đại lượng:** [Lực → đỏ, vận tốc → xanh lá, từ trường → tím...]
- **Hướng chuyển động / hệ quy chiếu:** [Chiều dương → phải, up → trên...]
- **Mặt phẳng quan sát / trục 180°:** [camera ở phía nào; trục nào cấm vượt]
- **FORMULA-ID / quy ước dấu:** [danh sách ID và quy ước]
- **Phong cách ánh sáng:** [Chỉ áp dụng nếu không phải MANABIE-2D]
- **Preset đang dùng:** [MANABIE-2D / KHAN-BOARD / KURZGESAGT / MOTION-TYPE / NGUOI-THAT / 3D / HYBRID]
- **Zone màu (MANABIE-2D):** [Zone A (kem) = lý thuyết; Zone B (xanh) = ứng dụng]

---

## Quy tắc chuyển cảnh

- Câu mở đầu của SC(n) **phải** dùng từ nối hoặc nhắc lại kết quả/câu hỏi từ SC(n−1):
  - Kiểu "trả lời": *"Vừa rồi chúng ta thấy X — lý do là…"*
  - Kiểu "đặt câu hỏi tiếp": *"Vậy điều đó có nghĩa là gì trong thực tế?"*
  - Kiểu "so sánh mở rộng": *"Tương tự, nếu ta thay X bằng Y…"*
- Mỗi cảnh kết thúc bằng: hold 1–2 giây → cross-dissolve 0.2s sang cảnh tiếp.
- Checkpoint (câu hỏi check) đặt sau mỗi 5–10 phút (video dài) hoặc trước cảnh chốt (video ngắn).
- Thứ tự cảnh = thứ tự logical theo narrative spine — không được xáo trộn.
