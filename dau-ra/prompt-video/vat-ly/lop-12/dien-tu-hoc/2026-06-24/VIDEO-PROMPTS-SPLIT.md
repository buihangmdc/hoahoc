# Video prompts đã tách clip - Điện từ học 60 giây

Mỗi clip dùng thiết kế `MATH-MOTION` nguyên bản, khung 16:9, không logo/watermark. Chữ và công thức thêm hậu kỳ từ `FORMULA-LEDGER.md`; tool lấy từ capability manifest, hiện ở trạng thái `PLAN_ONLY`.

## SC01-A - 5s
START STATE: nền tối sạch. ACTION: hiện tiêu đề “Điện từ học” và phụ đề “Ba công thức cốt lõi”. END STATE: tiêu đề ổn định, vùng công thức trống. Camera tĩnh.

## SC02-A - 9s
START FROM END STATE OF SC01-A. ACTION: hiện `Φ = BS cos α`, lần lượt nhấn B và S. END STATE: công thức đầy đủ, vùng giải thích góc còn trống. SCIENCE LOCK: EM-FLUX-1.

## SC02-B - 8s
START FROM END STATE OF SC02-A. ACTION: thêm pháp tuyến và chú thích α là góc giữa B với pháp tuyến; thêm đơn vị Wb. END STATE: sơ đồ góc và đơn vị rõ. SCIENCE LOCK: EM-FLUX-1; không vẽ α với mặt phẳng.

## SC03-A - 7s
START FROM END STATE OF SC02-B; transition reset to force formula panel. ACTION: hiện `F = BIl sin α` và đơn vị. END STATE: công thức lực từ ổn định. SCIENCE LOCK: EM-FORCE-1.

## SC03-B - 7s
START FROM END STATE OF SC03-A. ACTION: hiện B, chiều dòng điện và góc α trên camera plane đã khóa. END STATE: hai hướng và góc rõ, chưa hiện chiều lực. SCIENCE LOCK: EM-FORCE-1.

## SC03-C - 6s
START FROM END STATE OF SC03-B. ACTION: thêm vectơ lực theo tích có hướng/quy ước; giữ freeze-frame cuối 2s. END STATE: B, I, F và α đủ nhãn. Không đổi góc nhìn.

## SC04-A - 7s
START FROM END STATE OF SC03-C; transition reset to induction panel. ACTION: hiện `e_tb = -ΔΦ/Δt`, nhấn dấu âm. END STATE: công thức đầy đủ. SCIENCE LOCK: EM-FARADAY-1.

## SC04-B - 6s
START FROM END STATE OF SC04-A. ACTION: giải thích dấu âm theo Lenz và thêm đơn vị V, Wb, s. END STATE: điều kiện “giá trị trung bình” và quy ước chiều được ghi rõ.

## SC05-A - 5s
START FROM END STATE OF SC04-B. ACTION: xếp ba công thức đã khóa và câu hỏi tự kiểm tra góc/điều kiện. END STATE: bảng tổng kết sạch, không tuyên bố “chỉ cần thuộc lòng”.
