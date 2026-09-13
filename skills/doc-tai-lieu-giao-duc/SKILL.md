---
name: doc-tai-lieu-giao-duc
description: Tiếp nhận, kiểm kê, đọc, trích xuất và chuẩn hóa tài liệu giáo dục từ PDF, DOCX, PPTX, TXT, Markdown hoặc hình ảnh; tạo bản đồ nguồn, đơn vị kiến thức, yêu cầu cần đạt và cảnh báo mâu thuẫn. Dùng khi giáo viên đưa tài liệu vào để làm giáo án, kịch bản, video, prompt ảnh, prompt video hoặc ngân hàng câu hỏi.
---

# Đọc tài liệu giáo dục

## Quy trình

1. Chốt đúng thư mục đầu vào; chỉ quét thư mục đó bằng `scripts/scan_materials.py <nguồn> --output <nguồn>/van-ban-chuan-hoa/manifest.json`.
2. Xác định môn, lớp, chủ đề, đối tượng, loại tài liệu, phạm vi trang và quyền sử dụng. Tách tài liệu nhiều lớp/chủ đề thành các nhánh độc lập.
3. Gắn vai trò nguồn: `CHƯƠNG-TRÌNH`, `NGƯỜI-DÙNG`, `KHOA-HỌC-ỔN-ĐỊNH`, `BÊN-THỨ-BA` hoặc `AI-BỔ-SUNG`; không nâng tài liệu luyện thi thành nguồn chính thức.
4. Đọc theo lô; giữ số trang/slide/tiêu đề mục, phương thức trích xuất và mức tin cậy để truy vết.
5. Tạo `source-map.md` theo [mẫu truy vết](references/mau-truy-vet.md). Gộp tệp trùng SHA-256; bản sao không được tăng trọng số bằng chứng.
6. Tách thành đơn vị kiến thức: khái niệm, định luật, công thức, thí nghiệm, ví dụ, lỗi sai, câu hỏi và yêu cầu sản xuất.
7. Lập `FORMULA-LEDGER.md` cho mọi công thức (tên file thống nhất với `skills/thiet-ke-bai-day-hoa-hoc/references/khoa-cong-thuc-va-bieu-dien.md`): ảnh cắt/trang nguồn, bản chép chuẩn, kí hiệu, đơn vị, điều kiện áp dụng, dạng vectơ/vô hướng, biến đổi và mức tin cậy.
8. Đối chiếu kho lớp trong `kho-tai-lieu/`; đánh dấu `KHỚP`, `BỔ-SUNG`, `MÂU-THUẪN`, `CHƯA-XÁC-MINH`.
9. Xuất `knowledge-brief.md` và nhật ký lỗi; không viết kịch bản, đề hoặc đáp án trước khi kiểm định xong.
10. **Lưu đúng chỗ — BẮT BUỘC, không phải bước tuỳ chọn:** `scan_materials.py` chỉ suy luận lớp bằng cách tìm chuỗi `lop-N`/`lớp N` trong tên/đường dẫn tệp; nếu `grade_inferred` là `null` hoặc không khớp với lớp môn/lớp đã xác định ở bước 2, KHÔNG được coi là đã suy luận đúng. Sau khi chuẩn hoá xong, phải di chuyển/copy toàn bộ `source-map.md`, `formula-ledger.md`, `knowledge-brief.md` và tài liệu gốc vào đúng `kho-tai-lieu/hoa-hoc/lop-<n>/tai-lieu-nguoi-dung/` (hoặc nhánh tương ứng ở `kho-tai-lieu/hoa-hoc/lop-<n>/`) rồi cập nhật `index.md` của lớp đó để trỏ tới. Không được để tài liệu đã xử lý nằm ngoài cấu trúc `lop-<n>/` — thư mục ngoài cấu trúc này sẽ vô hình với `thiet-ke-bai-day-hoa-hoc/SKILL.md` khi định tuyến tri thức theo lớp.

## Cổng OCR và công thức

- PDF có text layer vẫn phải render trang chứa công thức, bảng, hình, chỉ số hoặc kí hiệu hạt nhân; text layer chỉ dùng để tìm kiếm.
- Với PDF scan/ảnh, OCR từng vùng theo thứ tự: tiêu đề → thân bài → công thức → nhãn hình. Lưu bản chép và ảnh gốc cạnh nhau trong bản đồ nguồn.
- Không tự sửa kí hiệu mơ hồ. Gắn `[KHÔNG-RÕ]`, ghi hai khả năng nếu cần và chuyển giáo viên xác nhận.
- Xác minh độc lập phép tính, đơn vị, dấu, hướng vectơ, số có nghĩa và làm tròn; đáp án tô màu không phải bằng chứng khoa học.
- Với DOCX/PPTX, trích xuất cấu trúc và đồng thời render để phát hiện công thức, hình hoặc bố cục bị mất. Nếu không có bộ render, ghi rõ cổng hình thức chưa thực hiện.

## Quy tắc

- Không suy ra nội dung không có trong nguồn mà không gắn nhãn “bổ sung của AI”.
- Không bịa số trang, trích dẫn hoặc yêu cầu cần đạt.
- Không sửa tài liệu gốc.
- Không đưa nguyên văn dài từ tài liệu có bản quyền vào đầu ra.
- Không coi số lần lặp, watermark, tên tệp hay đáp án được tô sáng là chỉ báo độ đúng.
