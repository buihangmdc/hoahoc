---
name: kiem-dinh-su-pham-giao-duc
description: Kiểm định độc lập giáo án, phiếu học tập, câu hỏi, kịch bản và video giáo dục về liên kết mục tiêu–hoạt động–đánh giá, hiểu lầm, tải nhận thức, phân hóa, UDL/khả năng tiếp cận, an toàn, công bằng và tính khả thi lớp học. Dùng trước khi bàn giao cho giáo viên hoặc làm GATE 2 trong pipeline sản xuất học liệu.
---

# Kiểm định sư phạm giáo dục

## Quy trình

1. Khóa hồ sơ: môn, lớp, chủ đề, đối tượng, thời lượng, điều kiện, yêu cầu cần đạt và đầu ra.
2. Không tự kiểm sản phẩm do chính agent này vừa thiết kế. Nhận bản nguồn, source map và báo cáo GATE 1.
3. Lập ma trận `mục tiêu → bằng chứng → hoạt động → phản hồi → đánh giá` theo [rubric sư phạm](references/rubric-su-pham.md).
4. Lập bản đồ hiểu lầm và câu hỏi chẩn đoán theo [khung đánh giá](references/khung-danh-gia-va-hieu-lam.md).
5. Kiểm phân hóa, khả năng tiếp cận, công bằng, an toàn và phương án ít thiết bị theo [khung triển khai](references/kha-nang-tiep-can-va-trien-khai.md).
6. Đọc sản phẩm từ góc nhìn học sinh: kiến thức đầu vào, tải mới mỗi bước, hướng dẫn, thời gian thao tác và cơ hội nhận phản hồi.
7. Gắn BLOCKER/MAJOR/MINOR; nêu vị trí, bằng chứng, ảnh hưởng và bản sửa có thể kiểm chứng.

## Cổng dừng

- Chuyển về GATE 1 nếu phát hiện claim/công thức mơ hồ hoặc sai.
- BLOCKER nếu không có mục tiêu đo được, không có bằng chứng đánh giá, hoạt động nguy hiểm, đánh giá nội dung chưa dạy, hoặc thiết kế loại trừ một nhóm học sinh mà không có phương án tương đương.
- MAJOR nếu thiếu chẩn đoán, phản hồi sửa sai, phân hóa, thời gian thực hiện hoặc phương án ít thiết bị.
- Chỉ PASS khi mỗi mục tiêu có ít nhất một bằng chứng phù hợp và sản phẩm có thể triển khai trong điều kiện đã khai báo.

## Đầu ra

Tạo `REPORT-GATE2.md` và dữ liệu `pedagogy` trong `validation-report.json`. Không cộng điểm trung bình để che BLOCKER; báo cáo từng chiều và quyết định cổng riêng.
