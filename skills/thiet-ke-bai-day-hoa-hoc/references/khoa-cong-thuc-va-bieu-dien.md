# Khóa công thức và biểu diễn Hóa học

## Quy trình FORMULA-LOCK trong Hóa học

FORMULA-LOCK là quy trình khóa từng công thức tính toán và phương trình phản ứng riêng lẻ. Tổng hợp toàn bộ mục FORMULA-LOCK dùng trong một gói bàn giao vào file `FORMULA-LEDGER.md` (tên bắt buộc, xem `SKILL.md` mục 5 và `rules/VALIDATION-FRAMEWORK.md` GATE 3) — đây là hai tên cho cùng một sổ công thức: FORMULA-LOCK mô tả quy trình/cấu trúc từng mục, FORMULA-LEDGER là tên file chứa tập hợp các mục đó.

Với mỗi công thức hoặc phương trình hóa học, tạo một mục duy nhất:

| Trường | Nội dung bắt buộc |
|---|---|
| `FORMULA-ID` | ID ổn định, ví dụ `CHEM-ENTHALPY-01` |
| Phát biểu | Quan hệ bằng lời, bản chất hóa học của hiện tượng |
| Công thức/PTHH chuẩn | LaTeX/Unicode với trạng thái `(s), (l), (g), (aq)`, điều kiện phản ứng |
| Kí hiệu / Danh pháp | Tên chất theo danh pháp IUPAC CT 2018, tên đại lượng, đơn vị SI |
| Điều kiện | Nhiệt độ, áp suất, chất xúc tác, nồng độ, dung môi |
| Quy ước | Dấu enthalpy (tỏa nhiệt âm, thu nhiệt dương), số oxi hóa, chiều cân bằng |
| Biến đổi | Từng bước đại số/bảo toàn, không nhảy bước gây sai số mol/nồng độ |
| Kiểm tra | Bảo toàn nguyên tố, bảo toàn điện tích, bảo toàn electron, thứ nguyên |
| Biểu diễn | Mô hình phân tử (màu CPK), đồ thị năng lượng, sơ đồ dụng cụ thí nghiệm |
| Lỗi cấm | Sai cân bằng, quên trạng thái chất, sai danh pháp IUPAC, sai dấu nhiệt |

Không đưa công thức/phản ứng vào đề, đáp án, infographic hoặc video nếu thiếu một trong các trường `Công thức chuẩn`, `Kí hiệu / Danh pháp`, `Điều kiện`, `Kiểm tra`.

## Các khóa thường dùng trong Hóa học chuẩn CTGDPT 2018

### `CHEM-MOLE-01` — Tính số mol và nồng độ dung dịch

- Thể tích khí ở điều kiện chuẩn ($25^\circ\text{C}, 1\text{ bar}$): $V = n \times 24.79 \text{ L} \Rightarrow n = \frac{V}{24.79}$.
- Số mol theo khối lượng: $n = \frac{m}{M}$.
- Nồng độ mol: $C_M = \frac{n}{V_{dd}} \text{ (mol/L)}$.
- Nồng độ phần trăm: $C\% = \frac{m_{ct}}{m_{dd}} \times 100\%$.
- Lỗi cấm: Dùng hệ số $22.4$ của điều kiện tiêu chuẩn cũ $0^\circ\text{C}, 1\text{ atm}$ thay vì $24.79$ theo CT 2018.

### `CHEM-ENTHALPY-01` — Biến thiên Enthalpy phản ứng ($\Delta_r H^\circ_{298}$)

- Theo enthalpy tạo thành chuẩn: $\Delta_r H^\circ_{298} = \sum \Delta_f H^\circ_{298}(\text{sản phẩm}) - \sum \Delta_f H^\circ_{298}(\text{chất đầu})$.
- Theo năng lượng liên kết (cho phản ứng khí): $\Delta_r H^\circ_{298} = \sum E_b(\text{chất đầu}) - \sum E_b(\text{sản phẩm})$.
- Quy ước dấu:
  - $\Delta_r H^\circ_{298} < 0$: Phản ứng tỏa nhiệt (Exothermic).
  - $\Delta_r H^\circ_{298} > 0$: Phản ứng thu nhiệt (Endothermic).
- Lỗi cấm: Nhầm lẫn giữa (chất đầu - sản phẩm) với (sản phẩm - chất đầu) khi tính theo năng lượng liên kết $E_b$.

### `CHEM-EQUIL-01` — Cân bằng hóa học và hằng số cân bằng $K_C$

- Xét phản ứng thuận nghịch: $aA + bB \rightleftharpoons cC + dD$.
- Biểu thức: $K_C = \frac{[C]^c [D]^d}{[A]^a [B]^b}$ tại trạng thái cân bằng.
- Quy ước: Nồng độ của chất rắn nguyên chất không xuất hiện trong biểu thức $K_C$.
- Nguyên lí Le Chatelier: Khi thay đổi yếu tố ngoài (nhiệt độ, áp suất, nồng độ), cân bằng chuyển dịch theo chiều làm giảm tác động đó.
- Lỗi cấm: Đưa nồng độ chất rắn vào biểu thức $K_C$; kết luận chất xúc tác làm thay đổi hằng số $K_C$ (chất xúc tác chỉ làm tăng tốc độ đạt cân bằng).

### `CHEM-REDOX-01` — Phản ứng oxi hóa - khử và bảo toàn electron

- Xác định số oxi hóa theo quy tắc IUPAC.
- Quá trình oxi hóa (nhường electron): Chất khử $\rightarrow$ dạng oxi hóa $+ ne$.
- Quá trình khử (nhận electron): Chất oxi hóa $+ ne \rightarrow$ dạng khử.
- Định luật bảo toàn: $\sum n_e \text{ nhường} = \sum n_e \text{ nhận}$.
- Lỗi cấm: Đảo ngược giữa chất khử và chất oxi hóa ("Khử cho - O nhận"); không bảo toàn điện tích ở hai vế phương trình ion.

### `CHEM-PH-01` — pH và cân bằng acid - base

- Dung dịch nước ở $25^\circ\text{C}$: $[H^+][OH^-] = 1.0 \times 10^{-14}$.
- Định nghĩa: $pH = -\log[H^+] \Rightarrow [H^+] = 10^{-pH}$.
- Môi trường acid: $pH < 7$, trung tính: $pH = 7$, base: $pH > 7$.
- Lỗi cấm: Cho rằng $pH$ luôn nằm trong khoảng $0 - 14$ (với dung dịch nồng độ rất đặc, $pH$ có thể $< 0$ hoặc $> 14$).

### `CHEM-ELECTRO-01` — Pin điện hóa và thế điện cực chuẩn

- Sức điện động chuẩn: $E^\circ_{pin} = E^\circ_{cathode} - E^\circ_{anode} = E^\circ_{(+)} - E^\circ_{(-)} > 0$.
- Cực Anode: Cực âm, nơi xảy ra quá trình oxi hóa.
- Cực Cathode: Cực dương, nơi xảy ra quá trình khử.
- Lỗi cấm: Nhầm lẫn vai trò cực anode/cathode giữa pin điện hóa (Galvanic cell) và bình điện phân (Electrolytic cell).