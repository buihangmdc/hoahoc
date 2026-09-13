# KHUNG KIỂM ĐỊNH 3 CỔNG

**Phiên bản:** 2.0  
**Cập nhật:** 2026-07-14  
**Phạm vi:** Mọi giáo án, học liệu, kịch bản, prompt và gói sản xuất trước khi bàn giao.

## 1. Nguyên tắc không thương lượng

1. Kiểm định độc lập với agent tạo sản phẩm.
2. Mỗi nhận định quan trọng phải truy được tới nguồn hoặc phép suy luận đã ghi.
3. Không dùng một Knowledge Base nội bộ làm nguồn duy nhất.
4. Không hạ cấp hoặc miễn trừ BLOCKER khoa học, an toàn, quyền riêng tư hay bản quyền.
5. Bản nháp được phép thiếu hạng mục chưa đến giai đoạn, nhưng phải mang trạng thái `DRAFT/INCOMPLETE`; không được ghi `PASS` hoặc “có thể bàn giao”.

## 2. Thứ tự nguồn cho GATE 1

Khi nguồn mâu thuẫn, dừng và ghi rõ mâu thuẫn; không tự hòa giải bằng phỏng đoán.

1. Yêu cầu chương trình hoặc văn bản chính thức đã xác minh.
2. Tài liệu giáo viên cung cấp, kèm `source-map` và vị trí trang/đoạn.
3. Kiến thức khoa học ổn định từ nguồn chính thống hoặc tài liệu chuyên môn đáng tin cậy.
4. Knowledge Base nội bộ đã ghi phiên bản và nguồn gốc.
5. Đề xuất sáng tạo của AI, phải gắn nhãn “đề xuất”, không dùng làm căn cứ khoa học.

## 3. GATE 1 — Khoa học và nguồn

**Agent:** `kiem-dinh-hoa-hoc-chuan` đối với Hóa học; agent bộ môn tương ứng đối với môn khác.

### 3.1 Phương trình hóa học, công thức và mô hình
- Lập `FORMULA-ID` cho từng phương trình/công thức hóa học; ghi tên chất theo danh pháp IUPAC chuẩn CTGDPT 2018, trạng thái chất `(s), (l), (g), (aq)`, điều kiện phản ứng (nhiệt độ, áp suất, xúc tác) và biến thiên enthalpy $\Delta_r H^\circ_{298}$.
- Tính lại kết quả bằng đường độc lập: kiểm tra bảo toàn nguyên tố, bảo toàn điện tích, bảo toàn electron, bảo toàn khối lượng và số có nghĩa.
- Không áp dụng sai điều kiện cân bằng hóa học: chất rắn nguyên chất không đưa vào biểu thức hằng số cân bằng $K_C, K_p$.
- Phân biệt rõ chiều phản ứng và dấu biến thiên enthalpy: $\Delta_r H^\circ_{298} < 0$ là phản ứng tỏa nhiệt, $\Delta_r H^\circ_{298} > 0$ là phản ứng thu nhiệt.

### 3.2 Đơn vị và số liệu Hóa học
- Sử dụng thể tích mol chất khí ở điều kiện chuẩn ($25^\circ\text{C}, 1\text{ bar}$) là $24.79\text{ L/mol}$ (theo CTGDPT 2018).
- Đơn vị nồng độ: $\text{mol/L (M)}$, $\text{g/L}$, nồng độ phần trăm $(\%)$, $pH = -\log[H^+]$.
- Số liệu đo thực nghiệm, hằng số phân li $K_a, K_b$, thế điện cực chuẩn $E^\circ$ phải có nguồn đối chiếu tin cậy.

### 3.3 Điều kiện phản ứng và an toàn
- Ghi rõ điều kiện phản ứng: nhiệt độ, áp suất, chất xúc tác, dung môi.
- Cảnh báo an toàn hóa chất bắt buộc (MSDS): quy tắc pha loãng acid sunfuric đặc (rót acid vào nước), độc tính, nguy cơ cháy nổ, xử lý rác thải hóa chất.

### 3.4 Cấu trúc phân tử và trực quan hóa
- Khóa mô hình phân tử 3D theo chuẩn màu CPK quốc tế (Carbon: xám/đen, Hydrogen: trắng, Oxygen: đỏ, Nitrogen: xanh lam, Chlorine: xanh lá, Sulfur: vàng).
- Khóa góc liên kết không gian và hình học phân tử; sơ đồ dụng cụ thí nghiệm thủy tinh chuẩn xác.

### 3.1 Công thức và mô hình

- Lập `FORMULA-ID` cho từng công thức; ghi tên đại lượng, đơn vị SI, dạng vô hướng/vectơ, điều kiện áp dụng và quy ước dấu.
- Tính lại kết quả bằng đường độc lập; kiểm tra thứ nguyên, giới hạn, bậc độ lớn và số có nghĩa.
- Không áp dụng công thức riêng cho mô hình hẹp sang trường hợp tổng quát. Ví dụ `U = 3/2 nRT` chỉ dùng cho khí lí tưởng đơn nguyên tử.
- Với nguyên lí I nhiệt động lực học, chọn đúng một quy ước và giữ xuyên suốt:
  - `ΔU = Q - A_hệ`, trong đó `A_hệ > 0` khi hệ thực hiện công; hoặc
  - `ΔU = Q + A_ngoài`, trong đó `A_ngoài > 0` khi ngoại lực thực hiện công lên hệ.
  Không dùng cùng một ký hiệu `A` cho hai đại lượng trên.

### 3.2 Đơn vị và số liệu

- Phân biệt nhiệt độ tuyệt đối `K` với nhiệt độ Celsius `°C`; chuyển đổi `T(K) = t(°C) + 273,15` khi cần.
- Không kết luận một nhiệt độ thấp là sai chỉ vì “không quen thuộc”. `25 K` có ý nghĩa vật lý; chỉ đánh lỗi nếu ngữ cảnh, phép đổi đơn vị hoặc điều kiện thực nghiệm không phù hợp.
- Số liệu đo phải có nguồn, độ phân giải và sai số phù hợp. Dữ liệu mô phỏng phải ghi rõ là dữ liệu mô phỏng.

### 3.3 Điều kiện áp dụng

- `pV = nRT` là mô hình khí lí tưởng. Mức gần đúng phụ thuộc chất khí, nhiệt độ, mật độ và khoảng cách tới vùng chuyển pha; không dùng một ngưỡng áp suất/nhiệt độ phổ quát.
- Nếu dùng gần đúng, ghi rõ đại lượng bỏ qua và phạm vi bài toán.

### 3.4 Vectơ, chiều và hình biểu diễn

- Khóa hệ quy chiếu, chiều dương, mặt phẳng quan sát và trạng thái đầu–cuối.
- Dùng tích có hướng làm chuẩn khi xác định chiều; quy tắc bàn tay chỉ là cách ghi nhớ theo đúng quy ước đang dùng.
- Với điện tích âm, chiều lực Lorentz ngược với `v × B`.
- “Dòng điện quy ước từ cực dương sang cực âm” chỉ đúng khi mô tả mạch ngoài của nguồn; phải nêu ngữ cảnh.
- Đường sức từ đi ra cực Bắc và đi vào cực Nam ở bên ngoài nam châm; không suy rộng câu này cho mọi miền không gian.

### 3.5 Truy xuất nguồn

Mỗi claim quan trọng ghi `CLAIM-ID`, `SOURCE-ID`, vị trí nguồn và một trong ba nhãn:

- `SOURCE`: có trong nguồn.
- `INFERENCE`: suy ra hợp lệ từ nguồn, kèm bước suy luận.
- `AI-PROPOSAL`: đề xuất sáng tạo, không phải nội dung nguồn.

## 4. GATE 2 — Sư phạm, ngôn ngữ và an toàn

**Agent:** `kiem-dinh-su-pham`, độc lập với agent thiết kế.

- Mục tiêu quan sát và đánh giá được; phù hợp lớp, thời lượng và yêu cầu cần đạt.
- Mỗi hoạt động tạo bằng chứng học tập; vai trò giáo viên, học sinh, sản phẩm và tiêu chí đánh giá rõ.
- Có chẩn đoán kiến thức đầu vào, dự báo hiểu lầm điển hình, phản hồi sửa sai và đánh giá cuối.
- Có phân hóa hỗ trợ–chuẩn–mở rộng và phương án ít thiết bị.
- Ngôn ngữ đúng thuật ngữ, phù hợp độ tuổi, câu đủ ngắn để đọc một lần hiểu; công thức có hướng dẫn đọc.
- Hình, màu, phụ đề và âm thanh bảo đảm khả năng tiếp cận cơ bản; không dùng màu là tín hiệu duy nhất.
- Thí nghiệm có nhận diện nguy cơ, biện pháp phòng ngừa và phương án thay thế an toàn.
- Không bịa trích dẫn, trang sách, kết quả thí nghiệm hoặc phản ứng của học sinh.

## 5. GATE 3 — Sản xuất và khả năng triển khai

### 5.1 Đơn vị video

- `SCENE`: đơn vị ý nghĩa sư phạm.
- `CLIP`: tệp video kỹ thuật, bị giới hạn bởi công cụ.
- `SHOT`: một bố cục/góc máy liên tục; một clip có thể có một hoặc nhiều shot nếu công cụ cho phép, nhưng mặc định một clip–một shot để ổn định.
- Một scene có thể gồm nhiều clip. Quan hệ bắt buộc là `1 clip = 1 clip manifest + 1 video prompt`; keyframe có thể dùng riêng hoặc tái sử dụng nếu trạng thái hình phù hợp và được ghi trong manifest.
- `max_clip_seconds` lấy từ manifest năng lực công cụ. Nếu chưa chọn công cụ, dùng giả định lập kế hoạch 9 giây và gắn nhãn `ASSUMPTION`, không gọi đó là giới hạn phổ quát.

### 5.2 Kiểm thời lượng

- Tổng thời lượng clip phải khớp timeline mục tiêu trong dung sai cấu hình, mặc định ±5%.
- Số từ voice tính theo độ tuổi, mật độ công thức và khoảng nghỉ; không áp một tốc độ duy nhất cho mọi cảnh.
- Mỗi clip có `START_STATE`, `ACTION`, `END_STATE`; clip kế tiếp tham chiếu `END_STATE` bằng ID, không dùng câu mơ hồ “như trước”.
- Video dài ưu tiên mixed-media: người dạy/slides/screen capture/đồ họa tĩnh có chuyển động, chỉ dùng clip sinh AI ở điểm cần trực quan hóa.

### 5.3 Gói bàn giao

- Có hồ sơ yêu cầu, nguồn sử dụng, `FORMULA-LEDGER.md` nếu có công thức (tên file bắt buộc, xem `skills/thiet-ke-bai-day-vat-ly/references/khoa-cong-thuc-va-bieu-dien.md`), script/storyboard, manifest clip, prompt, voice/subtitle và báo cáo kiểm định tương ứng với phạm vi yêu cầu.
- Không còn `TODO`, `TBD`, `PLACEHOLDER`, đường dẫn giả hoặc tuyên bố đã render khi chưa có tệp media.
- Không dùng logo, watermark, nhân vật hay phong cách nhận diện của bên thứ ba nếu chưa có quyền; preset chỉ mô tả nguyên lí thiết kế chung.

## 6. Mức độ lỗi và cổng dừng

- `BLOCKER`: sai khoa học; sai an toàn; giả nguồn; vi phạm quyền; thiếu thành phần khiến sản phẩm không dùng được. Phải sửa trước khi bàn giao.
- `MAJOR`: đúng lõi nhưng thiếu điều kiện, thiếu phân hóa, lệch thời lượng hoặc continuity yếu. Phải sửa trước bản phát hành.
- `MINOR`: lỗi diễn đạt, metadata hoặc cơ hội cải thiện không làm sai mục tiêu. Có thể ghi nợ kỹ thuật.

`PASS` chỉ khi không còn BLOCKER và MAJOR. `PASS_WITH_NOTES` chỉ có MINOR. Mọi trạng thái khác là `FAIL` hoặc `INCOMPLETE`.

## 7. Báo cáo tối thiểu

Báo cáo Markdown và JSON phải thống nhất, gồm:

```json
{
  "status": "PASS|PASS_WITH_NOTES|FAIL|INCOMPLETE",
  "target": "duong-dan",
  "assumptions": [],
  "gates": {
    "science": {"status": "PASS", "issues": []},
    "pedagogy": {"status": "PASS", "issues": []},
    "production": {"status": "PASS", "issues": []}
  },
  "counts": {"blocker": 0, "major": 0, "minor": 0}
}
```

Mỗi issue có `id`, `severity`, `file`, `line`, `claim`, `evidence`, `fix` và `validator`. Chạy kiểm tra máy trước, sau đó agent chuyên môn duyệt các nội dung không thể xác minh bằng luật tĩnh.
