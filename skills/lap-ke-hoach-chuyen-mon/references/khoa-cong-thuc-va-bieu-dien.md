# Khóa công thức và biểu diễn Vật lí

## Quy trình FORMULA-LOCK

FORMULA-LOCK là quy trình khóa từng công thức riêng lẻ. Tổng hợp toàn bộ mục FORMULA-LOCK dùng trong một gói bàn giao vào file `FORMULA-LEDGER.md` (tên bắt buộc, xem `SKILL.md` mục 5 và `rules/VALIDATION-FRAMEWORK.md` GATE 3) — đây là hai tên cho cùng một sổ công thức: FORMULA-LOCK mô tả quy trình/cấu trúc từng mục, FORMULA-LEDGER là tên file chứa tập hợp các mục đó.

Với mỗi công thức, tạo một mục duy nhất:

| Trường | Nội dung bắt buộc |
|---|---|
| `FORMULA-ID` | ID ổn định, ví dụ `MECH-N2-01` |
| Phát biểu | Quan hệ bằng lời, không chỉ chép kí hiệu |
| Công thức chuẩn | LaTeX/Unicode đã đối chiếu hình nguồn |
| Kí hiệu | Tên đại lượng, vectơ hay độ lớn, đơn vị SI |
| Điều kiện | Hệ quy chiếu, mô hình, đại lượng giữ không đổi, miền giá trị |
| Quy ước | Chiều dương, dấu công/nhiệt, góc, hướng vào–ra mặt phẳng |
| Biến đổi | Từng bước đại số, không nhảy bước gây đổi dấu/đơn vị |
| Kiểm tra | Thứ nguyên, giới hạn, bậc độ lớn, phép tính độc lập |
| Biểu diễn | Hệ trục, điểm đặt, mũi tên, đồ thị/hình cần có |
| Lỗi cấm | Ngộ nhận hoặc hình sai phải loại |

Không đưa công thức vào đề, đáp án, infographic hoặc video nếu thiếu một trong các trường `Công thức chuẩn`, `Kí hiệu`, `Điều kiện`, `Kiểm tra`.

## Các khóa thường dùng trong bộ nguồn hiện tại

### `VEC-PARA-01` — tổng hai vectơ

- `\vec R=\vec A+\vec B`.
- `R=\sqrt{A^2+B^2+2AB\cos\theta}`, với `θ` là góc giữa hai vectơ cùng gốc.
- Hướng so với `\vec A`: `α=atan2(B\sinθ, A+B\cosθ)`; không dùng riêng `tanα` nếu chưa xét góc phần tư.
- Hình: hai cạnh kề cùng gốc; cạnh tịnh tiến giữ nguyên hướng/độ dài; đường chéo đi từ gốc chung.

### `MECH-N1-01` — định luật I Newton

- `\sum\vec F=\vec0 ⇒ \vec a=\vec0 ⇒ \vec v` không đổi.
- Điều kiện: hệ quy chiếu quán tính.
- Lỗi cấm: “đứng yên thì không có lực”; đúng là các lực có thể cân bằng.

### `MECH-N2-01` — định luật II Newton

- `\sum\vec F=m\vec a` cho vật có khối lượng không đổi trong hệ quy chiếu quán tính.
- SI: `F` (N), `m` (kg), `a` (m/s²).
- Hình: gia tốc cùng hướng hợp lực, không nhất thiết cùng hướng vận tốc.
- Lỗi cấm: thay hợp lực bằng một lực thành phần; bỏ mũi tên vectơ khi đang xét hướng.

### `MECH-N3-01` — định luật III Newton

- `\vec F_{A→B}=-\vec F_{B→A}`.
- Hai lực cùng loại tương tác, đồng thời, đặt lên hai vật khác nhau nên không triệt tiêu nhau trên một vật.
- Lỗi cấm: gọi trọng lực và phản lực sàn trên cùng một vật là cặp lực III Newton.

### `MAG-FORCE-01` — lực từ lên dây dẫn

- `F=BIl\sinα`, với `α` là góc giữa chiều dòng điện và `\vec B`; đoạn dây thẳng dài `l` nằm trong từ trường đều.
- Hướng lực vuông góc mặt phẳng chứa `\vec l` và `\vec B`, xác định nhất quán bằng quy tắc bàn tay trái/tích có hướng.
- Kí hiệu hình: `⊙` ra khỏi mặt phẳng, `⊗` vào mặt phẳng.

### `IND-FLUX-01` — từ thông

- `Φ=BS\cosα`, `α` là góc giữa `\vec B` và pháp tuyến có hướng của mặt.
- SI: weber (Wb). Dấu phụ thuộc quy ước pháp tuyến; độ lớn không được tự thay bằng `BS sinα` nếu chưa đổi định nghĩa góc.

### `IND-EMF-01` — suất điện động cảm ứng

- `e=-N\,dΦ/dt`; bài độ lớn biến thiên đều dùng `|e|=N|ΔΦ|/Δt`.
- Dấu trừ thể hiện Lenz; khi chỉ hỏi độ lớn phải nói rõ đã lấy trị tuyệt đối.

### `THERM-Q-01` — nhiệt lượng làm đổi nhiệt độ

- `Q=mcΔT`, khi không có chuyển thể và `c` có thể coi không đổi trên khoảng nhiệt độ.
- SI: `Q` (J), `m` (kg), `c` (J/(kg·K)), `ΔT` (K hoặc độ chênh °C).

### `THERM-1ST-01` — định luật I nhiệt động lực học

- Chọn một quy ước dấu và ghi ngay cạnh công thức. Theo quy ước phổ biến trong tài liệu THPT Việt Nam: `ΔU=Q+A`, `A>0` khi hệ nhận công.
- Không trộn với quy ước `ΔU=Q-W` mà không định nghĩa `W` là công do hệ thực hiện.

### `GAS-IDEAL-01` — khí lí tưởng

- `pV=nRT`; nhiệt độ phải ở kelvin.
- Các hệ quả đẳng nhiệt/đẳng tích/đẳng áp chỉ dùng khi lượng khí không đổi và đại lượng được nêu là không đổi.
- Đổi nhiệt độ: `T=t+273,15 K`; nếu đề cho quy ước `+273`, làm theo đề và ghi rõ.

### `NUC-DECAY-01` — phóng xạ

- `N=N_0e^{-λt}`, `A=λN`, `T_{1/2}=\ln2/λ`.
- Khóa đơn vị thời gian giữa `λ` và `t`; kiểm tra bậc lũy thừa bằng tính độc lập.

### `ELEC-JOULE-01` — công suất tỏa nhiệt

- `P=I^2R=U^2/R=UI` cho phần tử thuần trở ở điều kiện phù hợp.
- Không dùng lẫn giá trị cực đại và hiệu dụng trong mạch xoay chiều.

## Cổng biểu diễn hình và video

1. Chốt mặt phẳng vật lí và góc nhìn trước khi vẽ mũi tên.
2. Dùng một quy ước màu nhất quán, nhưng không dùng màu thay cho nhãn/kí hiệu.
3. Công thức và nhãn khoa học là lớp vector/text hậu kỳ; ảnh sinh chỉ cung cấp minh họa nền.
4. Tạo một freeze-frame kiểm định ở thời điểm quan hệ vật lí rõ nhất; giáo viên duyệt frame này trước khi render dài.
5. Nếu góc máy đổi qua phía đối diện trục hành động, phải có shot chuyển tiếp và cập nhật nhãn chiều; nếu không, cấm vượt trục.
