# Sổ công thức từ bộ tài liệu người dùng

> Mục đích: truy vết và khóa điều kiện trước khi tái sử dụng. `ĐẠT-CÓ-ĐIỀU-KIỆN` nghĩa là công thức đúng khi dùng đúng mô hình/quy ước nêu trong bảng.

| FORMULA-ID | Nguồn | Công thức chuẩn | Kí hiệu/SI và điều kiện | Kiểm tra biểu diễn | Trạng thái |
|---|---|---|---|---|---|
| VEC-PARA-01 | I01 | `\vec R=\vec A+\vec B`; `R=√(A²+B²+2ABcosθ)` | `θ` là góc giữa hai vectơ cùng gốc | Cạnh tịnh tiến giữ hướng/độ dài; đường chéo từ gốc chung | ĐẠT |
| VEC-DIR-01 | I01 | `α=atan2(Bsinθ, A+Bcosθ)` | `α` đo từ `\vec A`; dùng `atan2` để đúng góc phần tư | Không chỉ dùng `tanα` khi mẫu bằng 0/âm | ĐẠT-CÓ-ĐIỀU-KIỆN |
| MECH-N1-01 | I05, I06 | `Σ\vec F=\vec0 ⇒ \vec a=\vec0 ⇒ \vec v` không đổi | Hệ quy chiếu quán tính | Sửa “no force” thành “net force is zero” | ĐẠT-SAU-SỬA |
| MECH-N2-01 | I04/I07 | `Σ\vec F=m\vec a` | `F` N, `m` kg, `a` m/s²; khối lượng không đổi; hệ quán tính | `\vec a` cùng hướng hợp lực, không nhất thiết cùng hướng `\vec v` | ĐẠT-CÓ-ĐIỀU-KIỆN |
| MECH-N3-01 | I02 | `\vec F_{A→B}=-\vec F_{B→A}` | Hai lực trên hai vật khác nhau, xuất hiện đồng thời | Không dùng mô hình “action trước, reaction sau” | ĐẠT-SAU-SỬA-DIỄN-ĐẠT |
| MAG-FORCE-01 | U03 tr.3; U04 tr.6 | `F=BIl sinα` | Đoạn dây thẳng dài `l` trong từ trường đều; `α` giữa dòng điện và `\vec B` | Hướng vuông góc mặt phẳng `I–B` | ĐẠT-CÓ-ĐIỀU-KIỆN |
| IND-FLUX-01 | U03 tr.1 | `Φ=BS cosα` | `α` giữa `\vec B` và pháp tuyến có hướng; Wb | Khóa pháp tuyến và dấu từ thông | ĐẠT |
| IND-EMF-01 | U03 tr.4; U04 tr.9–10 | `e=-N dΦ/dt`; độ lớn đều: `|e|=N|ΔΦ|/Δt` | V, Wb, s; dấu trừ theo Lenz | Bài thanh trượt: `|e|=Blv` khi hình học vuông góc phù hợp | ĐẠT-CÓ-ĐIỀU-KIỆN |
| THERM-Q-01 | U04 tr.1, 6–7 | `Q=mcΔT`; `c=Q/(mΔT)` | J, kg, J/(kg·K), K; không chuyển thể; `c` coi không đổi | Phải tính/ước lượng thất thoát nhiệt trong thí nghiệm thật | ĐẠT-CÓ-ĐIỀU-KIỆN |
| THERM-1ST-01 | U03 tr.2; U04 tr.5, 7 | `ΔU=Q+A_ngoài` hoặc `ΔU=Q-A_hệ` | Ghi rõ quy ước dấu ngay cạnh công thức; không trộn hai `A` | Với cách nhiệt `Q=0`; nén làm khí nhận công | ĐẠT-CÓ-QUY-ƯỚC |
| GAS-IDEAL-01 | U04 tr.3–4, 8–9 | `pV=nRT`; lượng khí không đổi: `pV/T=const` | `T` kelvin; chọn đẳng nhiệt/đẳng tích/đẳng áp đúng điều kiện | Đề U04 cho `T=t+273`; ngoài ngữ cảnh dùng `273,15` | ĐẠT-CÓ-ĐIỀU-KIỆN |
| NUC-BIND-01 | U04 tr.1 | `E_lk=Δmc²`; `E_lk,riêng=E_lk/A` | Độ bền so theo năng lượng liên kết riêng, không chỉ tổng liên kết | Không suy ra độ hụt khối lớn hơn nếu tổng `E_lk` bằng nhau | ĐẠT |
| NUC-DECAY-01 | U03 tr.4; U04 tr.8 | `N=N₀e^{-λt}`; `A=λN`; `T₁/₂=ln2/λ` | Đồng nhất đơn vị của `λ` và `t` | Tính lại lũy thừa và bậc độ lớn | ĐẠT |
| ELEC-JOULE-01 | U03 tr.4; U04 tr.5, 10 | `P=I²R=U²/R`; `Q=PΔt` | Thuần trở, dùng đúng hiệu dụng trong AC | U04 tr.10: kết quả xấp xỉ `0,13 mW` | ĐẠT-CÓ-ĐIỀU-KIỆN |

## Kiểm tra số học nguồn U04 trang 8

Với các số đã in: `λ=2,50×10^-10 s^-1`, `N₀=8,60×10^24`, `E₀=8,97×10^-13 J`, `η=0,062`:

- `ΔN≈λN₀Δt=2,15×10^15` hạt trong `1 s`.
- `E_nhiệt=ΔN·E₀=1928,55 J`.
- `E_điện=ηE_nhiệt=119,5701 J=0,1195701 kJ≈0,12 kJ`.

Nguồn ghi `1929,55 J` ở bước trung gian; đây là sai lệch cộng `1 J`, không đổi đáp án làm tròn cuối.
