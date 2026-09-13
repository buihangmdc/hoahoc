# WF-04 — Kiểm định và bàn giao

> **Cập nhật 2026-06-23:** WF-04 hiện ủy quyền toàn bộ cho framework kiểm định chuẩn 3-gate.  
> Dùng lệnh `/kiem-dinh-chuan` thay vì chạy thủ công 7 bước cũ.  
> Tài liệu tham chiếu: `rules/VALIDATION-FRAMEWORK.md`

## Quy trình chuẩn

```
Đầu vào (bài dạy / script / storyboard / prompt / video)
 ↓
GATE 1 — Nội dung khoa học   ← agent: kiem-dinh-vat-ly-chuan
  • So claim với KNOWLEDGE-BASE-CHUAN.md
  • Kiểm: công thức, đơn vị SI, quy ước dấu, chiều vectơ, điều kiện áp dụng
  • Gắn BLOCKER/MAJOR/MINOR → REPORT-GATE1.md
  • BLOCKER → DỪNG, phải sửa trước khi qua GATE 2
 ↓ (pass)
GATE 2 — Sư phạm             ← agent: kiem-dinh-su-pham
  • Kiểm: mục tiêu Bloom, hoạt động có sản phẩm, đánh giá, phân hóa, an toàn, khả thi, nguồn
  • Dùng rubric 7 tiêu chí trong skill/rubric-kiem-dinh.md
  • Gắn BLOCKER/MAJOR/MINOR → REPORT-GATE2.md
  • BLOCKER → DỪNG, phải sửa trước khi qua GATE 3
 ↓ (pass)
GATE 3 — Quy trình sản xuất  ← agent: quan-ly-san-xuat
  • Kiểm video ngắn: thời lượng ±5%, prompt độc lập, voice sync
  • Kiểm video dài: story arc, continuity bible, checkpoint, file structure
  • Xem CHECKLIST-VIDEO-DAI.md nếu thời lượng > 2 phút
  • Gắn BLOCKER/MAJOR/MINOR → REPORT-GATE3.md
 ↓ (pass)
Tạo SUMMARY-VALIDATION.md → Bàn giao
```

## Cổng dừng cứng

- **Bất kỳ BLOCKER nào** → cấm bàn giao.
- Không được skip GATE 1 để chạy GATE 2.
- Không được skip GATE 2 để chạy GATE 3.

## Khi nào dùng lệnh trực tiếp

```
/kiem-dinh-chuan [thư mục hoặc file]
```

Agent `quan-ly-san-xuat` khi tích hợp vào pipeline tự động sẽ gọi nội bộ theo thứ tự trên.  
Giáo viên gọi thủ công dùng lệnh `/kiem-dinh-chuan`.

## Ghi chú (so với WF-04 cũ)

| Bước cũ | Tương đương mới |
|---------|----------------|
| So claim với source map | GATE 1 — kiem-dinh-vat-ly-chuan |
| So storyboard với script | GATE 3 — quan-ly-san-xuat |
| So prompt với continuity bible | GATE 3 — quan-ly-san-xuat |
| Kiểm science lock, đơn vị, hướng | GATE 1 — kiem-dinh-vat-ly-chuan |
| Kiểm prompt độc lập | GATE 3 — quan-ly-san-xuat |
| Kiểm voice-over thời lượng | GATE 3 — quan-ly-san-xuat |
| Gắn BLOCKER/MAJOR/MINOR | Cả 3 GATE |
