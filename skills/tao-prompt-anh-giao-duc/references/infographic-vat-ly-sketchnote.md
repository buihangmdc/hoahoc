# Infographic Hóa học dạng sketchnote

## Mục tiêu

Tạo một trang cô đọng cho học sinh nhưng đủ điều kiện khoa học để giáo viên dùng. Phong cách tham khảo: nền giấy sáng, nét bút xanh–đen, khung bo góc, minh họa sketch đơn giản, màu nhấn tiết chế. Không mô phỏng chữ viết tay bằng model ảnh; dàn chữ/công thức bằng hậu kỳ.

## Kiến trúc trang

1. `TITLE`: tên phản ứng/định luật/nguyên tố/hợp chất, tối đa hai dòng.
2. `DEFINITION`: phát biểu chuẩn, danh pháp IUPAC CT 2018, có điều kiện phản ứng.
3. `KEY IDEAS`: 3–5 ý, mỗi ý một mệnh đề (tính chất vật lí, tính chất hóa học, ứng dụng).
4. `FORMULA/REACTION CARD`: phương trình từ `FORMULA-ID`, trạng thái chất, điều kiện, biến thiên enthalpy Δr H°₂₉₈.
5. `VISUAL PROOF`: sơ đồ cấu tạo phân tử (màu CPK) hoặc hình ảnh thí nghiệm thực tế.
6. `SPECIAL CASE / MISCONCEPTION`: trường hợp ngoại lệ hoặc lỗi học sinh thường mắc (ví dụ sai cân bằng, nhầm môi trường acid/base).
7. `TAKEAWAY`: một câu chốt cốt lõi.

## Chọn hình chiếu

| Nội dung | Góc nhìn ưu tiên | Khóa bắt buộc |
|---|---|---|
| Cấu tạo phân tử 3D | Góc nhìn 3/4 phối cảnh | Mã màu CPK chuẩn, góc liên kết, liên kết đơn/đôi/ba |
| Thí nghiệm ống nghiệm | Nhìn ngang chính diện | Dụng cụ thủy tinh, ngấn chất lỏng, màu kết tủa/bọt khí |
| Đồ thị năng lượng phản ứng | Nhìn chính diện vuông góc | Trục năng lượng, Ea (năng lượng hoạt hóa), Δr H |
| Pin điện hóa / Điện phân | Chính diện sơ đồ hai bình/màng ngăn | Cực Anode (-/+), Cathode (+/-), chiều dòng electron |
| Cấu hình electron / Nguyên tử | Lát cắt phẳng hoặc obitan 3D | Gắn nhãn "mô hình obitan", hạt nhân ở tâm |

## Pipeline hai lớp

### Lớp A — nền minh họa sinh bằng AI
- Chỉ sinh giấy/nền, khung, dụng cụ thí nghiệm, mô hình phân tử và khoảng trống.
- Không sinh chữ, công thức, số liệu, watermark.
- Chừa vùng đúng tỉ lệ cho title, reaction card và chú thích.

### Lớp B — hậu kỳ chính xác
- Chèn chữ tiếng Việt, công thức hóa học, phương trình phản ứng chuẩn IUPAC, nhãn mũi tên và thông số.