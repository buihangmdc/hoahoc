# Phiếu prompt video Vật lý

> Ba đơn vị theo `rules/CONG-THUC-SCENE-WORD.md`: `SCENE` (SC01, SC02…) là mắt xích sư phạm; `CLIP` (SC0X-A, SC0X-B…) là tệp video kỹ thuật khi một scene phải chia nhỏ; `SHOT` là góc máy bên trong một clip — mặc định 1 clip = 1 shot. Không dùng "Shot" để đặt tên hàng Narrative Spine hay scene.

## 1. Hồ sơ

- Môn/lớp/chủ đề:
- Mục tiêu học tập:
- Nền tảng video:
- Tổng thời lượng:
- Tỉ lệ/độ phân giải/fps:
- Phong cách hình ảnh:
- Đối tượng người xem:
- Danh sách FORMULA-ID / CONCEPT-ID:
- Mặt phẳng quan sát, chiều dương và quy tắc trục 180°:

## 2. Concept thống nhất

Mô tả nhân vật, bối cảnh, bảng màu, dụng cụ, quy ước màu của vectơ/đại lượng và điều phải giữ nhất quán trong toàn video.

## 3. Narrative Spine (điền TRƯỚC khi chia clip)

> Mỗi hàng = một SCENE (mắt xích sư phạm). Cột "Câu hỏi mở ra" của SCENE n = câu trả lời của SCENE n+1.

| SCENE | Học sinh vào đây đã biết gì? | Cảnh dạy/cho thấy gì? | Câu hỏi/tension mở ra cho cảnh sau |
|------|--------------------------|------------------|--------------------------------------|
| SC01 | *(chưa biết gì)* | Hook, hiện tượng gây tò mò | *"Tại sao?"* |
| SC02 | Thấy hiện tượng, tò mò | Khái niệm/nguyên lý giải thích | *"Nhưng cụ thể thế nào?"* |
| SC03 | Hiểu nguyên lý | Ví dụ / thí nghiệm cụ thể | *"Thực tế ra sao?"* |
| SC04 | Thấy ví dụ | Vận dụng / chốt ghi nhớ | — |

> **Kiểm tra:** Cột "Cảnh dạy/cho thấy gì?" của SCENE n phải là câu trả lời của cột "Câu hỏi mở ra" của SCENE n−1.

## 4. Chia clip và shot list

Áp dụng công thức chia clip ở `rules/CONG-THUC-SCENE-WORD.md` mục 2 (`clip_cap = max_clip_seconds`, mặc định 9s nếu chưa chọn công cụ). Mỗi CLIP mặc định là 1 SHOT (1 góc máy liên tục).

| CLIP (SC0X-A) | Scene gốc | Thời lượng | Cầu nối | ID/beat công thức | Hình ảnh/hành động | Camera geometry (shot) | Science freeze-frame | Lời dẫn/chữ | Âm thanh |
|---|---|---:|---|---|---|---|---|---|---|
| SC01-A | SC01 | 5–8s | *(clip đầu)* | PHENOMENON |  |  |  |  |  |
| SC02-A | SC02 | 5–8s | Trả lời SC01-A | SYSTEM/DIRECTION |  |  |  |  |  |
| SC03-A | SC03 | 5–8s | Tiếp nối SC02-A | RELATION/FORMULA |  |  |  |  |  |
| SC04-A | SC04 | 5–8s | Áp dụng SC03-A | SUBSTITUTION/CHECK |  |  |  |  |  |

## 5. Prompt từng clip

`CLIP [SC0X-A] — [thời lượng]. [Bối cảnh và vật thể giữ nguyên từ concept]. [Hành động theo trình tự thời gian], thể hiện chính xác [quan hệ theo FORMULA-ID/CONCEPT-ID]. VIEW PLANE/REFERENCE AXIS [mô tả]. SCIENCE FREEZE-FRAME [timecode và trạng thái]. Camera [cỡ cảnh, tiêu cự quy ước, độ cao, góc, chuyển động; không vượt trục]. Ánh sáng [mô tả], phong cách [mô tả]. Giữ nguyên [continuity]. Không sinh chữ, công thức, mũi tên khoa học trong khung hình; chừa vùng [vị trí] để thêm lớp hậu kỳ.`

## 6. Continuity lock

- Nhân vật/trang phục:
- Dụng cụ/số lượng/màu:
- Vị trí và hướng chuyển động:
- Mặt phẳng quan sát / chiều dương / trục cấm vượt:
- Quy ước màu vectơ:
- Ánh sáng/thời gian/bối cảnh:

## 7. Voice-over

> **Quy tắc bridge — bắt buộc từ CLIP thứ hai trở đi (tương ứng SC02 trở đi):**
> - Câu ĐẦU của mỗi clip phải nối từ clip trước (không được bắt đầu lạnh ngắt bằng tên khái niệm mới).
> - Câu CUỐI của mỗi clip (trừ clip cuối) phải đặt câu hỏi hoặc gợi tò mò cho clip tiếp.
>
> **4 kiểu câu mở đầu hợp lệ:**
> 1. Trả lời: *"Vừa rồi ta thấy X — lý do chính là…"*
> 2. Tiếp nối: *"Tiếp theo, hãy xem điều đó thay đổi thế nào khi…"*
> 3. So sánh: *"Tương tự như X ở clip trước, ở đây…"*
> 4. Hệ quả: *"Vì X, nên theo Y…"*

Ghi lời dẫn theo từng clip, câu ngắn, đúng thuật ngữ và vừa thời lượng. Đánh dấu chỗ nghỉ (/), từ cần nhấn (IN HOA) và câu hỏi tương tác.

| CLIP | Câu mở đầu (bridge) | Nội dung chính | Câu kết / hook |
|------|---------------------|---------------|----------------|
| SC01-A | — | | Câu hỏi gây tò mò |
| SC02-A | Trả lời câu hỏi SC01-A | | |
| SC03-A | | | |
| SC04-A | | | — (cảnh kết) |

## 8. Negative prompt

`sai định luật vật lý, chuyển động phi vật lý, sai hướng lực, sai mạch điện, vật thể tự xuất hiện hoặc biến mất, thay đổi số lượng dụng cụ, đổi màu/đổi trang phục, flicker, morphing, jump cut, camera rung, chữ rác, watermark, thao tác nguy hiểm`

## 9. Ghi chú hậu kỳ

- Chữ/công thức chèn thêm:
- Đồ họa vectơ/đường sức/tia sáng:
- Nhạc và hiệu ứng âm thanh:
- Phụ đề và khả năng tiếp cận:
- Khung hình cần giáo viên duyệt trước khi xuất:

## 10. Checklist

- [ ] Narrative Spine đã điền và logic (cột "Cảnh dạy" của SCENE n = câu trả lời cột "Câu hỏi mở ra" của SCENE n−1)
- [ ] Clip list có cột "Cầu nối" đã điền cho clip thứ hai trở đi
- [ ] Voice-over: câu đầu clip thứ hai trở đi là câu bridge hợp lệ
- [ ] Voice-over: câu cuối mỗi clip (trừ cuối) là câu hook
- [ ] Từng clip đúng khoa học
- [ ] FORMULA-ID/CONCEPT-ID và science freeze-frame đã được kiểm tra; đã lập `FORMULA-LEDGER.md` nếu có công thức
- [ ] Camera không đảo chiều biểu kiến hoặc đã có shot chuyển hệ nhìn
- [ ] Chuyển động liên tục, không thay đổi nhân vật/dụng cụ
- [ ] Lời dẫn vừa thời lượng
- [ ] Có negative prompt và continuity lock
- [ ] Có phụ đề/ghi chú hậu kỳ
- [ ] Không có hành vi thí nghiệm nguy hiểm
