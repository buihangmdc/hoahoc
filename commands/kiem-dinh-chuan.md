# Command: /kiem-dinh-chuan

## Cách dùng

```
/kiem-dinh-chuan [đường dẫn file hoặc tên bài]
```

**Ví dụ:**
```
/kiem-dinh-chuan dau-ra/bai-day/hoa-hoc/lop-10/nguyen-tu/2026-06-23/script.md
/kiem-dinh-chuan "Năng lượng hóa học và Biến thiên enthalpy"
```

---

## Chức năng

Chạy **3-gate validation framework** (GATE 1–3 tuần tự):

1. **GATE 1** — Kiểm định nội dung khoa học Hóa học (Agent: `kiem-dinh-hoa-hoc-chuan`)
   - Đối chiếu theo thứ tự nguồn trong `rules/VALIDATION-FRAMEWORK.md` và `rules/chuan-khoa-hoc-hoa-hoc.md`
   - Gán BLOCKER/MAJOR/MINOR
   - Output: `REPORT-GATE1.md`

2. **GATE 2** — Kiểm định sư phạm (Agent: `kiem-dinh-su-pham`)
   - Kiểm tra mục tiêu, hoạt động, đánh giá, an toàn hóa chất
   - Output: `REPORT-GATE2.md`

3. **GATE 3** — Kiểm định quy trình (Agent: `quan-ly-san-xuat`)
   - Kiểm tra thời lượng, file, continuity
   - Output: `REPORT-GATE3.md`

---

## Output

Tạo 3 file report:
```
dau-ra/bai-day/hoa-hoc/lop-10/<chu-de>/<ngay>/
├── REPORT-GATE1.md (nội dung khoa học)
├── REPORT-GATE2.md (sư phạm & an toàn)
├── REPORT-GATE3.md (quy trình)
└── SUMMARY-VALIDATION.md (tóm tắt chung, PASS/FAIL)
```

---

## Cổng dừng (Stop Gates)

| Cổng | BLOCKER → | Hành động |
|------|-----------|----------|
| GATE 1 | 🔴 Phương trình hóa học sai, sai cân bằng, sai bảo toàn điện tích/e, sai danh pháp IUPAC | **DỪNG** — Phải sửa |
| GATE 2 | 🔴 Mục tiêu không rõ, không có đánh giá, vi phạm an toàn hóa chất | **DỪNG** — Phải sửa |
| GATE 3 | 🔴 Tệp thiếu, không tổ chức | **DỪNG** — Phải sửa |

Nếu tất cả PASS (không BLOCKER):
```
✓ PASS — Có thể bàn giao
```

---

## Ghi chú

- Chỉ dùng `/kiem-dinh-chuan` **sau khi** tạo xong sản phẩm (bài dạy, script, prompt, video)
- Quy trình mặc định: GATE 1 → (nếu pass) → GATE 2 → (nếu pass) → GATE 3
- Chạy kiểm tra tĩnh cho gói video bằng `py scripts/validate_package.py <thu-muc> --mode strict`
- Không skip GATE để phát hành. Có thể chạy riêng một GATE để chẩn đoán, nhưng trạng thái toàn gói vẫn là `INCOMPLETE` cho tới khi đủ ba GATE.