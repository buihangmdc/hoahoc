# FORMULA-LEDGER — [Môn/lớp/chủ đề]

> Tổng hợp mọi mục FORMULA-LOCK dùng trong gói này. Xem quy trình đầy đủ ở [khóa công thức và biểu diễn](../references/khoa-cong-thuc-va-bieu-dien.md). Không đưa công thức/phương trình vào giáo án, đề, đáp án, prompt ảnh hoặc prompt video nếu dòng tương ứng còn thiếu `Công thức chuẩn`, `Kí hiệu`, `Điều kiện` hoặc `Kiểm tra`.

| FORMULA-ID | Phát biểu | Công thức/PTHH chuẩn | Kí hiệu (danh pháp, đơn vị SI) | Điều kiện | Quy ước | Kiểm tra | Biểu diễn | Lỗi cấm | Nguồn |
|---|---|---|---|---|---|---|---|---|---|
| [VD: CHEM-ENTHALPY-01] | Biến thiên enthalpy chuẩn phản ứng | Δr H°₂₉₈ = Σ Δf H°₂₉₈(sp) - Σ Δf H°₂₉₈(cđ) | kJ/mol, trạng thái chuẩn | 298 K, 1 bar | Tỏa nhiệt < 0, Thu nhiệt > 0 | Bảo toàn năng lượng | Sơ đồ enthalpy | Nhầm thứ tự trừ | SGK Hóa 10 tr. 82 |

## Ghi chú bắt buộc

- Mỗi `FORMULA-ID` chỉ xuất hiện một lần trong ledger của gói; nếu dùng lại từ gói khác, ghi chú "kế thừa từ [đường dẫn gói nguồn]".
- Cột `Nguồn` trỏ về `nguon-su-dung.md` hoặc source map tương ứng, không để trống.
- File này bắt buộc trong gói bàn giao khi có ít nhất một `FORMULA-ID` (xem `SKILL.md` mục 5); GATE 3 của `rules/VALIDATION-FRAMEWORK.md` từ chối bàn giao nếu thiếu.