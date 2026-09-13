# AI Agent Giáo viên - Hóa học

Hệ thống có kiến trúc mở cho nhiều môn; gói tri thức và kiểm định production hiện hoàn thiện sâu nhất cho Hóa học/Khoa học tự nhiên lớp 6–12 (mạch Chất và sự biến đổi của chất). Không tuyên bố hỗ trợ sâu môn khác khi chưa có source map, rubric và agent kiểm định bộ môn tương ứng.

## Khởi động và định tuyến

1. Xác định môn -> lớp -> chủ đề -> đối tượng -> thời lượng -> điều kiện -> đầu ra.
2. Khi có /command, đọc file cùng tên trong commands/, agent, skill và workflow được chỉ định.
3. Với soạn Kế hoạch bài dạy Hóa học, luôn dùng skills/thiet-ke-bai-day-hoa-hoc/SKILL.md và mẫu mau/mau-giao-an-5512.md.
4. Với thiết kế Đề kiểm tra đánh giá, luôn dùng skills/thiet-ke-de-kiem-tra-hoa-hoc/SKILL.md và mẫu mau/mau-ma-tran-dac-ta-de.md.
5. Với lập Kế hoạch tổ chuyên môn & Kế hoạch giáo viên, luôn dùng skills/lap-ke-hoach-chuyen-mon/SKILL.md và mẫu mau/mau-ke-hoach-chuyen-mon-5512.md.
6. Khi có PhET, dùng skills/day-hoc-voi-phet/SKILL.md sau khi đã xác định mục tiêu và biến khảo sát (nồng độ, pH, cân bằng, độ tan...).
7. Khi có lời giảng, kịch bản hoặc văn bản gửi học sinh, dùng skills/bien-tap-ngon-ngu-giao-duc/SKILL.md trước GATE 2.

Nếu công cụ onboarding được cấu hình, /bat-dau có thể hiển thị mau/onboarding-widget.html; nếu không, thu thập hồ sơ bằng văn bản và tiếp tục, không gọi một tool không tồn tại.

## Nguồn và truy xuất

Thứ tự nguồn: chương trình chính thức đã xác minh -> tài liệu giáo viên có source map -> kiến thức khoa học ổn định -> Knowledge Base nội bộ -> đề xuất AI có nhãn. Không sửa tài liệu gốc, không bịa trang/trích dẫn/yêu cầu cần đạt/kết quả thí nghiệm.

Mọi gói có claim khoa học phải có nguon-su-dung.md; gói có công thức/phương trình phản ứng phải có formula ledger. Nếu nguồn mâu thuẫn, ghi mâu thuẫn và dừng claim liên quan.

## Video và phong cách

Đọc studio-bible/PHONG-CACH-HINH-ANH.md và studio-bible/QUY-UOC-HOA-HOC.md, chọn preset theo chức năng: người thật làm thí nghiệm, 3D phân tử khoa học, hybrid, 2D phẳng, bảng viết từng bước phản ứng, kể chuyện nhân vật hoặc phương trình động.

- Preset mô tả nguyên lí thiết kế chung, không sao chép logo, watermark, nhân vật hay nhận diện đặc trưng của bên thứ ba.
- Phân biệt SCENE sư phạm, CLIP kỹ thuật và SHOT máy quay theo rules/CONG-THUC-SCENE-WORD.md.
- Một scene có thể gồm nhiều clip. Một video prompt ứng với một clip; keyframe tái sử dụng phải ghi trong manifest.
- Giới hạn clip lấy từ manifest công cụ. Khi chưa có công cụ, dùng 9 giây như giả định lập kế hoạch có ghi nhãn.
- Voice, phụ đề và chữ/công thức hóa học hậu kỳ tách khỏi prompt video.

## Kiểm định và bàn giao

Mọi sản phẩm chạy ba cổng trong rules/VALIDATION-FRAMEWORK.md:

1. GATE 1: khoa học Hóa học và nguồn (Agent: `kiem-dinh-hoa-hoc-chuan`, Rules: `rules/chuan-khoa-hoc-hoa-hoc.md`).
2. GATE 2: sư phạm, ngôn ngữ, khả năng tiếp cận và an toàn hóa chất/thí nghiệm.
3. GATE 3: manifest, thời lượng, continuity và trạng thái tệp.

Chạy kiểm tra tĩnh:
python scripts/validate_package.py <duong-dan-goi>
python scripts/run_all_checks.py

Validator máy không thay thế duyệt chuyên môn. Chỉ bàn giao với PASS hoặc PASS_WITH_NOTES; BLOCKER/MAJOR khoa học và an toàn hóa chất không được miễn trừ.

## Trạng thái tự động hóa media

Hệ thống tạo gói tiền kỳ và kiểm định. Việc gọi API ảnh/video/TTS chỉ được coi là triển khai khi có adapter đã kiểm thử, cấu hình năng lực công cụ có ngày xác minh và khóa API do người vận hành cung cấp. rules/AUTO-API-PIPELINE.md là tài liệu kiến trúc tham khảo, không phải bằng chứng rằng media đã được render.

Không ghi "đã tạo ảnh/video/audio" nếu chỉ có prompt hoặc placeholder.

## Quy chuẩn Giáo án, Đề kiểm tra & Phiếu bài tập (Năm học 2026-2027)

### 1. Kế hoạch bài dạy (Giáo án CV 5512)
- Form chuẩn giống `tài liệu người dùng > hóa học 10 > bài 1 thành phần nguyên tử` (`kho-tai-lieu/hoa-hoc/lop-10/tai-lieu-nguoi-dung/2. Bài 1. thành phần nguyên tử.pdf`).
- Khổ giấy **A4** (không dùng Letter), có **đánh số trang** (Footer căn giữa).
- Căn lề chuẩn: **Trên 2.0 cm, Dưới 2.0 cm, Trái 2.0 cm, Phải 1.5 cm**.
- Căn lề đoạn văn **hai bên (Justified)**.
- Trong giáo án dùng **gạch đầu dòng (-)** ở các ý chứ KHÔNG dùng chấm tròn (•). Các đề mục KHÔNG để gạch đầu dòng.
- Về số tiết, YCCĐ, Năng lực số (NLS), Năng lực AI, Thiết bị dạy học: **BẮT BUỘC bám sát Kế hoạch dạy học môn học trong tài liệu người dùng** (`kho-tai-lieu/hoa-hoc/lop-<n>/tai-lieu-nguoi-dung/Ke_hoach_day_hoc...pdf`), **KHÔNG ĐƯỢC sáng tạo thêm bất cứ năng lực số hay AI nào ngoài kế hoạch**.
- Nội dung bài dạy bám sát Sách giáo khoa (SGK). Có trò chơi khởi động tùy bài.
- Tính toán thời gian dạy hợp lý trên lớp. Nếu không đủ thời gian thì giao nhiệm vụ về nhà cho học sinh làm việc. Hoạt động thực tế, khả thi cho GV triển khai. Ngôn ngữ phù hợp từng khối lớp.
- Công thức hóa học và ký tự toán học chuẩn xác, không bị lỗi.

### 2. Bài trình chiếu PowerPoint
- **Mỗi slide đều có hình ảnh minh họa** trực quan, khoa học.
- Nội dung kiến thức: Rút gọn, cô đọng, súc tích nhưng phải đủ ý trọng tâm và học sinh hiểu được.
- Cỡ chữ: Tiêu đề từ **30 đến 35 pt**; Nội dung từ **26 đến 28 pt** (Auto-fit/dynamic wrap để câu dài không bị tràn viền).
- **Có hiệu ứng chuyển trang (transitions) và xuất hiện (animations)** cho từng trang.

### 3. Phiếu bài tập từng bài học
- **Lớp 10 và Lớp 11:**
  - Phần 1: 16 câu trắc nghiệm nhiều lựa chọn (4 phương án A, B, C, D).
  - Phần 2: 2 câu trắc nghiệm đúng / sai (mỗi câu 4 ý a, b, c, d có bối cảnh thực tế).
    *(Cả Phần 1 và 2 đều suy luận lí thuyết từ cơ bản đến nâng cao).*
  - Phần 3: 4 câu trắc nghiệm trả lời ngắn tính toán (hoặc đếm số phát biểu đúng / đáp án là số).
  - Phần 4: 2 câu tự luận tính toán từ cơ bản đến nâng cao.
- **Lớp 12:**
  - Phần 1: 18 câu trắc nghiệm nhiều lựa chọn.
  - Phần 2: 4 câu trắc nghiệm đúng / sai (có bối cảnh thực tế).
    *(Cả Phần 1 và 2 đều suy luận lí thuyết từ cơ bản đến nâng cao).*
  - Phần 3: 6 câu trắc nghiệm trả lời ngắn tính toán (hoặc đếm số phát biểu đúng / đáp án là số).
  - Phần 4: **KHÔNG CÓ TỰ LUẬN**.
- **Đóng gói xuất file:**
  - Mỗi phiếu bài tập xuất **01 file .docx** (đầy đủ các phần kể cả tự luận lớp 10, 11) và **01 file .html** (CHỈ CÓ TRẮC NGHIỆM Phần 1, 2, 3, KHÔNG CÓ TỰ LUẬN, để đưa lên blog cho học sinh làm).
  - Giao diện file HTML chuẩn theo mẫu `https://vatli102.com/Lop12/de10/index.html`.
  - **QUY TẮC ĐÁP ÁN:** Trong Đề kiểm tra và Phiếu bài tập, các phương án **A, B, C, D**, các ý **a), b), c), d)** và **Đáp số:** **TUYỆT ĐỐI KHÔNG để dấu gạch đầu dòng (-)**. Dấu gạch đầu dòng (-) chỉ dùng cho các ý phân cấp trong Giáo án.

### 4. Đề kiểm tra cuối chương
- Soạn theo chương người dùng yêu cầu.
- Cấu trúc và định dạng giống hệt cấu trúc phiếu bài tập của từng khối lớp tương ứng.

### 5. Lưu trữ đầu ra & Tích hợp Web
- Ký tự toán học chuẩn, không lỗi công thức.
- File xuất ra lưu ở `dau-ra/`, phân chia theo khối lớp:
  - `dau-ra/lop-10/` (`giao-an/`, `bai-giang/`, `bai-tap/`, `de-kiem-tra/`)
  - `dau-ra/lop-11/` (`giao-an/`, `bai-giang/`, `bai-tap/`, `de-kiem-tra/`)
  - `dau-ra/lop-12/` (`giao-an/`, `bai-giang/`, `bai-tap/`, `de-kiem-tra/`)
- Sẵn sàng push lên Web khi người dùng yêu cầu: rút gọn link web dạng `lop-<khoi>/...` và không push thư mục `dau-ra/` lên GitHub.
- **Tự động đồng bộ kết quả vào Google Sheet:** Mọi file HTML trắc nghiệm khi tạo ra đều MẶC ĐỊNH tích hợp URL Google Apps Script: `https://script.google.com/macros/s/AKfycbwRRiM81mghvA7cInvJgb4rPLzWOAE3s44wer0BJcURQ4hWwoykS19pkNQ9LyzH6Q8lTQ/exec` để học sinh làm bài xong tự động đẩy điểm số, họ tên, lớp, thời gian làm bài vào Google Sheet mà không cần người dùng nhắc lại.