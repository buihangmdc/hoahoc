---
name: viet-kich-ban-video-giao-duc
description: Chuyển knowledge brief, giáo án hoặc tài liệu môn học thành kịch bản video giáo dục, storyboard, lời dẫn, lời thoại và nhịp cảnh theo thời lượng. Dùng khi cần video bài giảng, video giải thích khái niệm, thí nghiệm mô phỏng, Shorts/Reels/TikTok giáo dục hoặc chuỗi video theo bài học.
---

# Viết kịch bản video giáo dục

## Đầu vào bắt buộc

Đọc `knowledge-brief.md`, `source-map.md`, hồ sơ lớp và `studio-bible/`. Nếu thiếu knowledge brief, gọi skill `doc-tai-lieu-giao-duc` trước.

---

## BƯỚC 1 — Dựng NARRATIVE SPINE (BẮT BUỘC trước khi viết storyboard)

> **Đây là bước quan trọng nhất để tránh video rời rạc, vô logic.**  
> Narrative spine = sợi chỉ logic xuyên suốt — mỗi cảnh là câu trả lời cho câu hỏi cảnh trước.

### Cách dựng spine:

1. **Xác định mục tiêu học tập duy nhất** của video: học sinh sẽ hiểu được/làm được gì?
2. **Xác định điểm xuất phát** của học sinh: họ đã biết gì, còn thắc mắc gì?
3. **Vẽ chuỗi concept** từ điểm xuất phát đến mục tiêu — mỗi bước chỉ tiến một khái niệm:
   ```
   [Hiện tượng lạ] → [Câu hỏi tại sao] → [Khái niệm giải thích] → [Công thức/mô hình] → [Ví dụ cụ thể] → [Vận dụng]
   ```
4. **Mỗi node trong chuỗi = một cảnh (SC)**. Node phải trả lời câu hỏi từ node trước.
5. **Viết bảng spine** (xem mẫu trong `assets/mau-storyboard.md`) trước khi viết storyboard chi tiết.

### Kiểm tra spine trước khi tiếp tục:
- [ ] Mỗi cảnh có "câu hỏi mở ra" → cảnh tiếp có "câu trả lời"
- [ ] Xóa bất kỳ cảnh nào → video bị đứt logic → cảnh đó là "load-bearing" ✓
- [ ] Không có hai cảnh liên tiếp cùng dạy một khái niệm (tránh lặp)
- [ ] Cảnh đầu có hook tạo tò mò; cảnh cuối có chốt/vận dụng

---

## BƯỚC 2 — Thiết kế kịch bản

1. Chốt một mục tiêu học tập chính cho mỗi video ngắn.
2. Chọn cấu trúc dựa trên spine: Hook → Vấn đề → Quan sát → Giải thích → Kiểm tra hiểu → Chốt/vận dụng.
3. Chọn người thật, 3D hoặc hybrid theo [hướng dẫn phong cách](references/chon-phong-cach-hinh-anh.md) và preset trong `studio-bible/`.
4. Tính số cảnh theo [nhịp thời lượng](references/nhip-thoi-luong.md).
5. Điền storyboard theo mẫu — **bắt buộc điền cột "Cầu nối từ cảnh trước"** và **"Câu mở đầu transition"** cho mỗi cảnh từ SC02 trở đi.
6. Với hybrid, tách hai cột `LIVE-ACTION PLATE` và `GRAPHICS/3D OVERLAY`.
7. Với cảnh Vật lí, gắn `FORMULA-ID/CONCEPT-ID`, mặt phẳng quan sát, chiều dương, lí do chọn góc máy và timecode science freeze-frame.
8. Nếu có công thức, tách nhịp: hiện tượng → hệ/đại lượng → hướng/dấu → quan hệ → công thức/điều kiện → thế số/đơn vị → kiểm tra. Không bắt buộc mỗi nhịp là một cảnh, nhưng mỗi cảnh chỉ có một thay đổi nhận thức chính.
9. Dùng [mẫu storyboard](assets/mau-storyboard.md).
10. Chạy kiểm định khoa học trên freeze-frame trước khi chuyển sang prompt.

---

## BƯỚC 3 — Viết lời dẫn từng cảnh

Với mỗi cảnh từ SC02 trở đi:

**Câu đầu tiên PHẢI là câu bridge — nối từ cảnh trước.** Chọn một kiểu:

| Kiểu bridge | Khi nào dùng | Ví dụ |
|-------------|-------------|-------|
| **Trả lời** | Cảnh này giải đáp câu hỏi cảnh trước | "Vừa rồi ta thấy bóng đèn sáng — lý do là dòng điện chạy qua..." |
| **Tiếp nối** | Cảnh này mở rộng cùng khái niệm | "Tiếp theo, hãy xem điều đó thay đổi như thế nào khi nhiệt độ tăng..." |
| **So sánh** | Cảnh này dùng tương tự/phản ví dụ | "Tương tự như nén khí vừa rồi, ở đây ta nén lò xo và..." |
| **Hệ quả** | Cảnh trước là nguyên nhân, cảnh này là kết quả | "Vì áp suất tăng, nên theo định luật I, nội năng phải..." |

**Câu cuối cùng (nếu không phải cảnh kết):** Đặt câu hỏi mở hoặc gợi sự tò mò cho cảnh tiếp.

---

## Quy tắc bất biến

- Mỗi cảnh chỉ truyền **một ý chính** — nhiều hơn → tách cảnh.
- Lời dẫn phải vừa thời lượng và **không đọc lại toàn bộ chữ** trên màn hình.
- Không dùng kịch tính làm sai bản chất khoa học.
- Tách rõ hiện tượng thật, mô phỏng và ẩn dụ.
- Không đổi góc máy làm đảo chiều biểu kiến của lực, vận tốc, dòng điện hoặc tia sáng nếu chưa có shot chuyển hệ nhìn và gắn lại trục.
- Không để model hình/video tự sinh công thức; storyboard chỉ định lớp hậu kỳ đã khóa.
- **Không viết cảnh nào mà xóa đi video vẫn hiểu được bình thường** — mỗi cảnh phải là mắt xích không thể thiếu.
