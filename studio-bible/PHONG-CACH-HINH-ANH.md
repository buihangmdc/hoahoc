# Phong cách hình ảnh — nguồn định tuyến

## Nguyên tắc

- Tạo thiết kế nguyên bản theo chức năng sư phạm; không sao chép logo, watermark, mascot, nhân vật hoặc tổ hợp nhận diện đặc trưng của bên thứ ba.
- Tên thương hiệu người dùng nêu chỉ được dùng để hiểu thuộc tính cấp cao như “2D phẳng”, “bảng viết từng bước”, “kể chuyện nhân vật” hoặc “đồ họa toán học”; prompt cuối phải dùng mô tả trung tính.
- Công thức, chữ tiếng Việt và nhãn khoa học thêm ở lớp hậu kỳ đã kiểm định.
- Màu không được là tín hiệu duy nhất; mọi vectơ/hướng phải có nhãn hoặc kiểu nét bổ sung.
- `continuity-bible.md` được phép ghi đè palette nhưng không được phá quy ước khoa học.

## Bảy preset chức năng

| ID sản xuất | Tên gọi | File tương thích | Dùng khi |
|---|---|---|---|
| `LIVE-TEACHER` | Người thật | `PRESET-01-NGUOI-THAT.md` | Lớp học, thí nghiệm và kết nối giáo viên |
| `SCIENCE-3D` | 3D khoa học | `PRESET-02-3D.md` | Vi mô, cấu trúc bên trong, thiên văn |
| `LIVE-3D-HYBRID` | Người thật + 3D | `PRESET-03-HYBRID-NGUOI-THAT-3D.md` | Người thật kết hợp overlay giải thích phần vô hình |
| `EDU-FLAT-2D` | Hoạt hình 2D | `PRESET-04-MANABIE-2D.md` | Sơ đồ nguyên lí, mạch và hiện tượng dạng phẳng |
| `STEP-WHITEBOARD` | Bảng viết từng bước | `PRESET-05-KHAN-BOARD.md` | Giải bài, chứng minh, hình thành công thức |
| `COSMIC-STORY-2D` | Kể chuyện nhân vật | `PRESET-06-KURZGESAGT.md` | Hook, câu chuyện khoa học, chuyển thang vi mô–vĩ mô |
| `MATH-MOTION` | Công thức động | `PRESET-07-MOTION-TYPE.md` | Quan hệ đại lượng, biến đổi và tóm tắt công thức |

Tên file cũ chỉ để không làm gãy liên kết. Trong manifest và prompt mới, dùng ID sản xuất trung tính ở cột đầu.
