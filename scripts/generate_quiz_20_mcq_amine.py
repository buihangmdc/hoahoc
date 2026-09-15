"""
Script: generate_quiz_20_mcq_amine.py
Purpose: Generate 20 Multiple Choice Questions (A, B, C, D) covering all aspects of Amine (Chemistry Grade 12 - Ket noi tri thuc)
- NO COMBUSTION QUESTIONS (replaced with statement-counting questions as requested)
- Difficulty levels: Recognition -> Comprehension -> Application -> High Application
Outputs:
1. dau-ra/lop-12/bai-tap/20-cau-trac-nghiem-nhieu-lua-chon-amine-hoa-hoc-12.md
2. dau-ra/lop-12/bai-tap/20-cau-trac-nghiem-nhieu-lua-chon-amine-hoa-hoc-12.docx
3. dau-ra/lop-12/bai-tap/20-cau-trac-nghiem-nhieu-lua-chon-amine-hoa-hoc-12.html (vatli102.com style + Google Sheet sync)
"""

import os
import sys
import json
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.abspath("."))
from scripts.export_to_docx import create_styled_document

GOOGLE_SHEET_URL = "https://script.google.com/macros/s/AKfycbwRRiM81mghvA7cInvJgb4rPLzWOAE3s44wer0BJcURQ4hWwoykS19pkNQ9LyzH6Q8lTQ/exec"

questions = [
    {
        "id": 1,
        "level": "Nhận biết",
        "question": "Hợp chất nào sau đây thuộc loại amine bậc III?",
        "options": {
            "A": "CH₃-NH-CH₂-CH₃.",
            "B": "(CH₃)₃N.",
            "C": "CH₃-CH₂-CH₂-NH₂.",
            "D": "C₆H₅-NH-CH₃."
        },
        "answer": "B",
        "explanation": "Bậc của amine được tính bằng số nguyên tử hydrogen trong phân tử ammonia (NH₃) bị thay thế bởi các gốc hydrocarbon. Hợp chất (CH₃)₃N (trimethylamine) có cả 3 nguyên tử H bị thay thế bởi 3 nhóm methyl nên thuộc loại amine bậc III. CH₃-NH-CH₂-CH₃ và C₆H₅-NH-CH₃ là amine bậc II; CH₃-CH₂-CH₂-NH₂ là amine bậc I."
    },
    {
        "id": 2,
        "level": "Nhận biết",
        "question": "Aniline (phenylamine) là amine thơm đơn giản và quan trọng nhất. Công thức phân tử của aniline là",
        "options": {
            "A": "C₇H₉N.",
            "B": "C₆H₇N.",
            "C": "C₆H₅N.",
            "D": "C₆H₁₃N."
        },
        "answer": "B",
        "explanation": "Aniline có công thức cấu tạo thu gọn là C₆H₅NH₂, gồm một nhóm amino (-NH₂) liên kết trực tiếp với vòng benzene. Gom các nguyên tử lại ta được công thức phân tử là C₆H₇N (phân tử khối M = 93 amu)."
    },
    {
        "id": 3,
        "level": "Nhận biết",
        "question": "Hợp chất CH₃-NH-C₂H₅ có tên gốc - chức là",
        "options": {
            "A": "ethylmethylamine.",
            "B": "methylethylamine.",
            "C": "N-methylethanamine.",
            "D": "propan-2-amine."
        },
        "answer": "A",
        "explanation": "Theo danh pháp gốc - chức, tên các gốc alkyl liên kết với nguyên tử N được đọc theo thứ tự bảng chữ cái tiếng Anh (ethyl đứng trước methyl), sau đó thêm từ 'amine'. Do đó hợp chất có tên gốc - chức là ethylmethylamine. (N-methylethanamine là tên thay thế)."
    },
    {
        "id": 4,
        "level": "Nhận biết",
        "question": "Tên gọi thay thế (theo danh pháp IUPAC) của amine có công thức cấu tạo CH₃-CH(NH₂)-CH₃ là",
        "options": {
            "A": "isopropylamine.",
            "B": "propan-1-amine.",
            "C": "propan-2-amine.",
            "D": "1-methylethanamine."
        },
        "answer": "C",
        "explanation": "Theo danh pháp thay thế, chọn mạch chính dài nhất chứa nhóm amine và đánh số sao cho vị trí nhóm amine là nhỏ nhất. Mạch chính có 3 nguyên tử C (propane), nhóm -NH₂ liên kết ở carbon số 2. Tên thay thế là propan-2-amine. (Isopropylamine là tên gốc - chức)."
    },
    {
        "id": 5,
        "level": "Nhận biết",
        "question": "Ở điều kiện thường, dãy gồm các amine đều là chất khí, có mùi khai khó chịu, độc và tan nhiều trong nước là",
        "options": {
            "A": "methylamine, ethylamine, dimethylamine, trimethylamine.",
            "B": "aniline, methylamine, ethylamine, dimethylamine.",
            "C": "propylamine, dimethylamine, trimethylamine, aniline.",
            "D": "methylamine, benzylamine, ethylamine, diethylamine."
        },
        "answer": "A",
        "explanation": "Bốn amine đầu dãy đồng đẳng gồm methylamine (CH₃NH₂), ethylamine (C₂H₅NH₂), dimethylamine ((CH₃)₂NH) và trimethylamine ((CH₃)₃N) là những chất khí ở điều kiện thường, có mùi khai nồng tương tự ammonia, độc và tan rất nhiều trong nước nhờ khả năng tạo liên kết hydrogen với nước."
    },
    {
        "id": 6,
        "level": "Nhận biết",
        "question": "Trong phân tử methylamine (CH₃NH₂), nguyên tử nitrogen ở trạng thái lai hóa sp³ và dạng hình học xung quanh nguyên tử N là",
        "options": {
            "A": "đường thẳng.",
            "B": "tam giác phẳng.",
            "C": "hình chóp tam giác (tháp tam giác).",
            "D": "hình tứ diện đều."
        },
        "answer": "C",
        "explanation": "Tương tự phân tử ammonia (NH₃), nguyên tử N trong amine tạo 3 liên kết σ (1 liên kết C-N và 2 liên kết N-H) và còn 1 cặp electron tự do chưa tham gia liên kết. Do lực đẩy của cặp electron tự do này, hình học phân tử xung quanh nguyên tử N có cấu trúc hình chóp tam giác (tháp tam giác)."
    },
    {
        "id": 7,
        "level": "Thông hiểu",
        "question": "Cho các chất sau: C₂H₆ (ethane), CH₃-O-CH₃ (dimethyl ether), C₂H₅NH₂ (ethylamine), C₂H₅OH (ethanol). Chất có nhiệt độ sôi cao nhất là",
        "options": {
            "A": "C₂H₆.",
            "B": "CH₃-O-CH₃.",
            "C": "C₂H₅NH₂.",
            "D": "C₂H₅OH."
        },
        "answer": "D",
        "explanation": "Ethanol tạo được liên kết hydrogen liên phân tử O-H···O rất bền do nguyên tử O có độ âm điện lớn hơn nguyên tử N. Ethylamine cũng tạo liên kết hydrogen N-H···N nhưng yếu hơn alcohol tương ứng. Hydrocarbon và ether không tạo được liên kết hydrogen liên phân tử. Thứ tự nhiệt độ sôi giảm dần: C₂H₅OH (78,3°C) > C₂H₅NH₂ (16,6°C) > CH₃-O-CH₃ (-24°C) > C₂H₆ (-88,6°C)."
    },
    {
        "id": 8,
        "level": "Thông hiểu",
        "question": "Dãy sắp xếp các chất theo thứ tự lực base tăng dần từ trái sang phải là",
        "options": {
            "A": "C₆H₅NH₂ < NH₃ < CH₃NH₂ < (CH₃)₂NH.",
            "B": "NH₃ < C₆H₅NH₂ < CH₃NH₂ < (CH₃)₂NH.",
            "C": "(CH₃)₂NH < CH₃NH₂ < NH₃ < C₆H₅NH₂.",
            "D": "C₆H₅NH₂ < (CH₃)₂NH < CH₃NH₂ < NH₃."
        },
        "answer": "A",
        "explanation": "Gốc alkyl (-CH₃) đẩy electron làm tăng mật độ điện tích âm trên nguyên tử N, làm tăng khả năng nhận proton H⁺ => tăng lực base. Gốc phenyl (-C₆H₅) hút electron do hiệu ứng liên hợp p-π với vòng benzene, làm giảm mật độ electron trên N => giảm mạnh lực base. Thứ tự lực base: C₆H₅NH₂ (aniline) < NH₃ < CH₃NH₂ < (CH₃)₂NH."
    },
    {
        "id": 9,
        "level": "Thông hiểu",
        "question": "Dung dịch chất nào sau đây KHÔNG làm đổi màu giấy quỳ tím ẩm?",
        "options": {
            "A": "Methylamine (CH₃NH₂).",
            "B": "Dimethylamine ((CH₃)₂NH).",
            "C": "Ammonia (NH₃).",
            "D": "Aniline (C₆H₅NH₂)."
        },
        "answer": "D",
        "explanation": "Aniline có tính base rất yếu (hằng số Kb ≈ 3,8.10⁻¹⁰) do hiệu ứng hút electron của gốc phenyl làm giảm khả năng nhận proton H⁺. Vì vậy dung dịch aniline không đủ mạnh để làm đổi màu giấy quỳ tím và không làm đổi màu dung dịch phenolphthalein. Các amine no (methylamine, dimethylamine) và NH₃ đều làm quỳ tím hóa xanh."
    },
    {
        "id": 10,
        "level": "Thông hiểu",
        "question": "Cho từ từ dung dịch methylamine đến dư vào ống nghiệm chứa dung dịch FeCl₃, hiện tượng quan sát được là",
        "options": {
            "A": "xuất hiện kết tủa màu nâu đỏ, sau đó kết tủa tan dần tạo dung dịch trong suốt.",
            "B": "xuất hiện kết tủa màu trắng xanh, sau đó hóa nâu đỏ ngoài không khí.",
            "C": "xuất hiện kết tủa màu nâu đỏ và kết tủa không tan khi cho methylamine dư.",
            "D": "không có hiện tượng gì xuất hiện."
        },
        "answer": "C",
        "explanation": "Trong nước, methylamine nhận proton tạo môi trường kiềm yếu: CH₃NH₂ + H₂O ⇌ CH₃NH₃⁺ + OH⁻. Ion OH⁻ kết hợp với Fe³⁺ tạo kết tủa hydroxide: 3CH₃NH₂ + 3H₂O + FeCl₃ -> Fe(OH)₃↓ (nâu đỏ) + 3CH₃NH₃Cl. Khác với Cu(OH)₂, Fe(OH)₃ không có khả năng tạo phức tan với amine nên kết tủa không tan trong amine dư."
    },
    {
        "id": 11,
        "level": "Thông hiểu",
        "question": "Nhỏ vài giọt nước bromine vào ống nghiệm đựng dung dịch aniline, hiện tượng quan sát được là",
        "options": {
            "A": "xuất hiện kết tủa màu vàng nhạt và có khí bay ra.",
            "B": "xuất hiện kết tủa màu trắng.",
            "C": "dung dịch chuyển sang màu xanh lam đậm.",
            "D": "dung dịch bị mất màu hoàn toàn và không có kết tủa."
        },
        "answer": "B",
        "explanation": "Do ảnh hưởng định hướng và hoạt hóa mạnh của nhóm amino (-NH₂), aniline tham gia phản ứng thế electrophile vào nhân thơm rất dễ dàng ở nhiệt độ thường, đồng thời thế 3 nguyên tử H ở các vị trí ortho và para: C₆H₅NH₂ + 3Br₂ -> C₆H₂Br₃NH₂↓ (2,4,6-tribromoaniline, kết tủa trắng) + 3HBr. Phản ứng này dùng để nhận biết aniline."
    },
    {
        "id": 12,
        "level": "Thông hiểu",
        "question": "Ở nhiệt độ thường, khi cho ethylamine tác dụng với dung dịch chứa hỗn hợp NaNO₂ và HCl (sinh ra nitrous acid, HNO₂), hiện tượng quan sát được là",
        "options": {
            "A": "sủi bọt khí không màu (N₂) và tạo thành alcohol.",
            "B": "xuất hiện kết tủa màu vàng cam.",
            "C": "dung dịch chuyển sang màu hồng cánh sen.",
            "D": "xuất hiện kết tủa màu trắng đục."
        },
        "answer": "A",
        "explanation": "Amine no bậc I phản ứng với nitrous acid (HNO₂) ở nhiệt độ thường tạo thành alcohol và giải phóng khí nitrogen không màu: C₂H₅NH₂ + HNO₂ -> C₂H₅OH + N₂↑ + H₂O. Ngược lại, amine thơm bậc I (như aniline) khi phản ứng với HNO₂ ở 0 - 5°C tạo muối diazonium tan trong nước (không sủi bọt khí)."
    },
    {
        "id": 13,
        "level": "Vận dụng",
        "question": "Số lượng đồng phân cấu tạo amine bậc I có cùng công thức phân tử C₄H₁₁N là",
        "options": {
            "A": "2.",
            "B": "3.",
            "C": "4.",
            "D": "8."
        },
        "answer": "C",
        "explanation": "Ứng với công thức phân tử C₄H₁₁N có tổng cộng 8 đồng phân amine. Trong đó có đúng 4 đồng phân amine bậc I (chứa nhóm -NH₂ liên kết với gốc alkyl C₄H₉-):\n1) CH₃-CH₂-CH₂-CH₂-NH₂ (butan-1-amine)\n2) CH₃-CH₂-CH(NH₂)-CH₃ (butan-2-amine)\n3) (CH₃)₂CH-CH₂-NH₂ (2-methylpropan-1-amine)\n4) (CH₃)₃C-NH₂ (2-methylpropan-2-amine)."
    },
    {
        "id": 14,
        "level": "Vận dụng",
        "question": "Cho 4,5 gam một alkylamine no, đơn chức, mạch hở X tác dụng vừa đủ với 100 mL dung dịch HCl 1M. Công thức phân tử của X là",
        "options": {
            "A": "CH₅N.",
            "B": "C₂H₇N.",
            "C": "C₃H₉N.",
            "D": "C₄H₁₁N."
        },
        "answer": "B",
        "explanation": "n(HCl) = 0,1.1 = 0,1 mol. Vì X là amine đơn chức: n(X) = n(HCl) = 0,1 mol. Phân tử khối của X: M(X) = 4,5 / 0,1 = 45 g/mol. Công thức phân tử của alkylamine no đơn chức là CnH₂n₊₃N => 14n + 17 = 45 => 14n = 28 => n = 2. Vậy CTPT của X là C₂H₇N (ethylamine hoặc dimethylamine)."
    },
    {
        "id": 15,
        "level": "Vận dụng",
        "question": "Cho các phát biểu sau về cấu tạo và tính chất của amine:\n(a) Ở điều kiện thường, methylamine và ethylamine là những chất khí tan nhiều trong nước.\n(b) Nhỏ dung dịch methylamine lên mẩu giấy quỳ tím, quỳ tím chuyển sang màu xanh.\n(c) Aniline có lực base mạnh hơn ammonia do có vòng benzene giàu electron.\n(d) Liên kết hydrogen giữa các phân tử amine bền hơn liên kết hydrogen giữa các phân tử alcohol tương ứng.\n(e) Cho dung dịch dimethylamine vào dung dịch FeCl₃ xuất hiện kết tủa màu nâu đỏ.\nSố phát biểu đúng là",
        "options": {
            "A": "2.",
            "B": "3.",
            "C": "4.",
            "D": "5."
        },
        "answer": "B",
        "explanation": "Gồm 3 phát biểu đúng: (a), (b), (e).\n- (a) ĐÚNG: Methylamine và ethylamine là chất khí ở điều kiện thường, có mùi khai và tan nhiều trong nước.\n- (b) ĐÚNG: Methylamine là base yếu, dung dịch trong nước làm quỳ tím hóa xanh.\n- (c) SAI: Vòng benzene hút electron do hiệu ứng liên hợp p-π làm giảm mật độ electron trên N => lực base của aniline yếu hơn ammonia rất nhiều.\n- (d) SAI: Độ âm điện của N (3,04) nhỏ hơn O (3,44) nên liên kết hydrogen N-H···N kém bền hơn liên kết O-H···O của alcohol tương ứng.\n- (e) ĐÚNG: 3(CH₃)₂NH + 3H₂O + FeCl₃ -> Fe(OH)₃↓ (nâu đỏ) + 3(CH₃)₂NH₂Cl."
    },
    {
        "id": 16,
        "level": "Vận dụng",
        "question": "Cho 9,3 gam aniline tác dụng hoàn toàn với lượng dư nước bromine. Khối lượng kết tủa trắng 2,4,6-tribromoaniline thu được là",
        "options": {
            "A": "16,5 gam.",
            "B": "33,0 gam.",
            "C": "24,75 gam.",
            "D": "49,5 gam."
        },
        "answer": "B",
        "explanation": "n(aniline) = 9,3 / 93 = 0,1 mol. Phương trình phản ứng: C₆H₅NH₂ + 3Br₂ -> C₆H₂Br₃NH₂↓ + 3HBr. Theo phương trình: n(kết tủa) = n(aniline) = 0,1 mol. Phân tử khối của 2,4,6-tribromoaniline là M = 93 + 3.79 = 330 g/mol. Khối lượng kết tủa: m = 0,1.330 = 33,0 gam."
    },
    {
        "id": 17,
        "level": "Vận dụng",
        "question": "Mùi tanh của cá (đặc biệt là cá biển, cá mè) chủ yếu do các amine gây ra, trong đó nhiều nhất là trimethylamine (CH₃)₃N. Để khử mùi tanh của cá trước khi nấu, biện pháp nào sau đây là phù hợp nhất dựa trên cơ sở hóa học?",
        "options": {
            "A": "Ngâm cá trong dung dịch nước vôi trong (Ca(OH)₂).",
            "B": "Rửa cá bằng dung dịch xà phòng hoặc nước tro bếp có tính kiềm.",
            "C": "Rửa cá với nước pha giấm ăn hoặc nước cốt chanh có tính acid nhẹ.",
            "D": "Ngâm cá trong dung dịch đường saccharose bão hòa."
        },
        "answer": "C",
        "explanation": "Trimethylamine là một chất có tính base. Khi dùng giấm ăn (chứa acetic acid CH₃COOH) hoặc nước cốt chanh (chứa citric acid), acid sẽ tác dụng với amine tạo thành muối ammonium: (CH₃)₃N + CH₃COOH -> (CH₃)₃NH⁺CH₃COO⁻. Muối này không bay hơi và dễ dàng bị rửa trôi bởi nước, nhờ đó mùi tanh của cá được khử triệt để."
    },
    {
        "id": 18,
        "level": "Vận dụng cao",
        "question": "Cho m gam hỗn hợp X gồm ba amine no, đơn chức, mạch hở (methylamine, dimethylamine và ethylamine) tác dụng vừa đủ với 150 mL dung dịch HCl 1M. Sau phản ứng, cô cạn cẩn thận dung dịch thu được 11,475 gam muối khan. Giá trị của m là",
        "options": {
            "A": "6,00.",
            "B": "5,475.",
            "C": "4,50.",
            "D": "7,825."
        },
        "answer": "A",
        "explanation": "Số mol HCl đã phản ứng: n(HCl) = 0,15.1 = 0,15 mol. Khối lượng HCl: m(HCl) = 0,15.36,5 = 5,475 gam. Các amine đều là đơn chức nên phản ứng theo tỉ lệ 1 : 1 với HCl: R-NH₂ + HCl -> R-NH₃Cl. Áp dụng định luật bảo toàn khối lượng: m(X) + m(HCl) = m(muối) => m(X) = 11,475 - 5,475 = 6,00 gam."
    },
    {
        "id": 19,
        "level": "Vận dụng cao",
        "question": "Cho các phát biểu sau về tính chất, điều chế và ứng dụng của các hợp chất amine:\n(a) Aniline không làm đổi màu giấy quỳ tím ẩm do có tính base rất yếu.\n(b) Phản ứng giữa amine thơm bậc I với nitrous acid ở 0 – 5 °C sinh ra khí nitrogen và alcohol tương ứng.\n(c) Khi cho từ từ dung dịch HCl vào ống nghiệm đựng aniline vẩn đục, chất lỏng trong ống nghiệm chuyển dần thành trong suốt đồng nhất.\n(d) Dẫn xuất halogen R-X tác dụng với ammonia có thể tạo ra hỗn hợp gồm các amine bậc I, bậc II, bậc III và muối ammonium bậc IV.\n(e) Cho mẩu giấy quỳ tím ẩm vào bình chứa khí trimethylamine, mẩu giấy quỳ tím chuyển sang màu đỏ.\n(g) Trong công nghiệp, hexamethylenediamine phản ứng trùng ngưng với adipic acid để sản xuất tơ nilon-6,6.\nSố phát biểu đúng là",
        "options": {
            "A": "3.",
            "B": "4.",
            "C": "5.",
            "D": "2."
        },
        "answer": "B",
        "explanation": "Gồm 4 phát biểu đúng: (a), (c), (d), (g).\n- (a) ĐÚNG: Do gốc phenyl hút electron mạnh, tính base của aniline rất yếu nên không làm đổi màu quỳ tím ẩm.\n- (b) SAI: Amine NO bậc I mới tạo alcohol và sủi bọt khí N₂; còn amine THƠM bậc I (như aniline) ở 0 – 5 °C tạo muối diazonium tan [C₆H₅N₂]⁺Cl⁻, không giải phóng khí N₂.\n- (c) ĐÚNG: Aniline rất ít tan trong nước nên tạo vẩn đục; khi thêm HCl xảy ra phản ứng C₆H₅NH₂ + HCl -> C₆H₅NH₃Cl (muối tan tốt) tạo dung dịch trong suốt đồng nhất.\n- (d) ĐÚNG: Đây là phản ứng alkyl hóa ammonia từng nấc, sản phẩm thu được thường là hỗn hợp các bậc amine khác nhau.\n- (e) SAI: Trimethylamine có tính base nên làm quỳ tím ẩm hóa XANH, không phải màu đỏ.\n- (g) ĐÚNG: n H₂N-(CH₂)₆-NH₂ + n HOOC-(CH₂)₄-COOH -> -(HN-(CH₂)₆-NH-CO-(CH₂)₄-CO)-n + 2n H₂O (tơ nilon-6,6)."
    },
    {
        "id": 20,
        "level": "Vận dụng cao",
        "question": "Cho các phát biểu sau về amine:\n(1) Nhỏ vài giọt dung dịch aniline vào ống nghiệm chứa nước cất, thấy aniline tan hoàn toàn tạo dung dịch đồng nhất.\n(2) Nhỏ vài giọt nước bromine vào dung dịch aniline thấy xuất hiện kết tủa trắng.\n(3) Để rửa sạch ống nghiệm có dính cặn aniline, người ta có thể tráng bằng dung dịch HCl rồi rửa lại bằng nước sạch.\n(4) Trimethylamine có công thức phân tử C₃H₉N và thuộc loại amine bậc III.\n(5) Lực base của methylamine mạnh hơn ammonia, nhưng yếu hơn aniline.\n(6) Trong công nghiệp, aniline được sản xuất chủ yếu bằng cách khử nitrobenzene bằng kim loại Fe trong dung dịch HCl.\nSố phát biểu đúng là",
        "options": {
            "A": "2.",
            "B": "3.",
            "C": "4.",
            "D": "5."
        },
        "answer": "C",
        "explanation": "Gồm 4 phát biểu đúng: (2), (3), (4), (6).\n- Phát biểu (1) SAI: Aniline rất ít tan trong nước lạnh (ở 20°C độ tan chỉ 3,6 g/100 g nước), aniline tạo vẩn đục rồi lắng xuống đáy ống nghiệm do khối lượng riêng lớn hơn nước (D ≈ 1,02 g/mL).\n- Phát biểu (5) SAI: Lực base của methylamine mạnh hơn ammonia, và mạnh hơn aniline rất nhiều (thứ tự: methylamine > ammonia > aniline). Aniline có tính base rất yếu do hiệu ứng hút electron của gốc phenyl."
    }
]

def generate_markdown(out_path):
    lines = []
    lines.append("# BỘ CÂU HỎI TRẮC NGHIỆM CHUYÊN ĐỀ: AMINE")
    lines.append("")
    lines.append("Trường THPT Mạc Đĩnh Chi – Nam Sách")
    lines.append("Tổ: Hóa – Sinh")
    lines.append("Họ và tên GV: Bùi Thị Hằng")
    lines.append("")
    lines.append("Môn: Hóa học — Khối lớp: 12 (Bộ sách: Kết nối tri thức với cuộc sống)")
    lines.append("Chủ đề: Amine — Số lượng câu hỏi: 20 câu trắc nghiệm nhiều phương án lựa chọn")
    lines.append("Mức độ đánh giá: Từ Nhận biết đến Vận dụng cao (Bao hàm toàn bộ nội dung amine, chú trọng các câu mệnh đề đếm)")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## NỘI DUNG ĐỀ BÀI")
    lines.append("")
    for q in questions:
        lines.append(f"Câu {q['id']} ({q['level']}): {q['question']}")
        for opt_key, opt_val in q['options'].items():
            lines.append(f"{opt_key}. {opt_val}")
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## ĐÁP ÁN VÀ HƯỚNG DẪN GIẢI CHI TIẾT")
    lines.append("")
    for q in questions:
        lines.append(f"Câu {q['id']}: Đáp án {q['answer']}.")
        lines.append(f"Hướng dẫn giải: {q['explanation']}")
        lines.append("")
    
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))
    print(f"Đã tạo file Markdown: {out_path}")

def generate_html(out_path):
    html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>📝 20 CÂU TRẮC NGHIỆM AMINE - HÓA HỌC 12 KNTT</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <script>
        window.MathJax = {{
            tex: {{
                inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
                displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
                processEscapes: true
            }},
            options: {{
                skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
            }}
        }};
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        :root {{
            --primary: #0284c7;
            --primary-hover: #0369a1;
            --secondary: #0d9488;
            --bg-body: #f8fafc;
            --card-bg: #ffffff;
            --text-dark: #0f172a;
            --text-muted: #64748b;
            --border: #e2e8f0;
        }}

        body {{
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-body);
            color: var(--text-dark);
            line-height: 1.65;
            padding-bottom: 40px;
        }}

        p, .question-title, .explanation-box, .score-desc, .form-group label {{
            text-align: justify;
        }}

        .sticky-header {{
            position: sticky; top: 0; z-index: 1000;
            background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px);
            border-bottom: 1px solid var(--border); box-shadow: 0 4px 15px rgba(0, 0, 0, 0.04);
        }}
        .header-container {{
            max-width: 920px; margin: 0 auto; padding: 10px 15px;
            display: flex; justify-content: space-between; align-items: center;
        }}
        .site-logo {{ display: flex; align-items: center; gap: 8px; text-decoration: none; }}
        .logo-text {{
            font-size: 1.25rem; font-weight: 800;
            background: linear-gradient(135deg, #0284c7, #0d9488);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }}
        .nav-links {{ display: flex; gap: 18px; align-items: center; }}
        .timer-badge {{
            background: #fee2e2; color: #ef4444; padding: 4px 10px; border-radius: 8px;
            font-weight: 800; font-size: 0.9rem; display: flex; align-items: center; gap: 5px;
        }}

        .quiz-container {{ max-width: 920px; margin: 20px auto; padding: 0 15px; min-height: 80vh; }}

        .exam-banner {{
            background: linear-gradient(135deg, #0f172a, #0369a1, #0f766e); color: white;
            padding: 2.2rem 1.5rem; border-radius: 20px; text-align: center; margin-bottom: 20px;
            box-shadow: 0 10px 25px rgba(15,23,42,0.25);
        }}
        .exam-banner h1 {{ font-size: 1.7rem; font-weight: 800; margin-bottom: 8px; }}
        .exam-banner p {{ font-size: 0.95rem; color: #e0f2fe; text-align: center; }}
        .badge-exam {{ display: inline-block; background: rgba(255,255,255,0.2); padding: 4px 14px; border-radius: 20px; font-size: 0.82rem; font-weight: 700; margin-top: 10px; }}

        .login-card {{
            background: white; border-radius: 16px; padding: 30px 20px; text-align: center;
            border: 1px solid var(--border); box-shadow: 0 10px 25px rgba(0,0,0,0.05); margin-bottom: 30px;
        }}
        .login-title {{ font-size: 1.25rem; font-weight: 700; margin-bottom: 8px; }}
        .login-subtitle {{ color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px; }}
        .form-group {{ max-width: 360px; margin: 0 auto 15px auto; text-align: left; }}
        .form-group label {{ display: block; margin-bottom: 5px; font-weight: 600; font-size: 0.88rem; }}
        .form-control {{
            width: 100%; padding: 10px 14px; border: 1.5px solid var(--border);
            border-radius: 8px; font-size: 0.95rem; outline: none; transition: border-color 0.2s;
        }}
        .form-control:focus {{ border-color: var(--primary); }}
        .btn-start {{
            background: var(--primary); color: white; border: none; padding: 12px 30px;
            font-size: 1rem; font-weight: 700; border-radius: 30px; cursor: pointer;
            box-shadow: 0 4px 15px rgba(2, 132, 199, 0.3); transition: all 0.2s;
        }}
        .btn-start:hover {{ background: var(--primary-hover); transform: translateY(-2px); }}

        .student-info-bar {{
            background: white; padding: 12px 18px; border-radius: 10px; margin-bottom: 18px;
            display: flex; justify-content: space-between; font-size: 0.95rem; font-weight: 600;
            border: 1px solid var(--border);
        }}

        .progress-container {{ margin-bottom: 20px; }}
        .progress-bar-bg {{ background: #e2e8f0; border-radius: 10px; height: 10px; overflow: hidden; }}
        .progress-bar-fill {{ background: linear-gradient(90deg, #0284c7, #0d9488); height: 100%; width: 0%; transition: width 0.3s; }}
        .progress-text {{ display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--text-muted); margin-top: 5px; }}

        .section-header {{
            background: linear-gradient(135deg, #0284c7, #0369a1); color: white;
            padding: 10px 16px; border-radius: 8px; font-size: 1.05rem; font-weight: 700;
            margin: 25px 0 15px 0; display: flex; align-items: center; gap: 8px;
        }}

        .question-card {{
            background: var(--card-bg); border-radius: 12px; padding: 18px 20px;
            margin-bottom: 18px; border: 1px solid var(--border); box-shadow: 0 2px 8px rgba(0,0,0,0.03);
        }}
        .question-title {{ font-size: 1rem; font-weight: 600; margin-bottom: 14px; line-height: 1.6; }}
        .question-num {{ color: var(--primary); font-weight: 700; margin-right: 4px; }}
        .level-badge {{ display: inline-block; padding: 2px 8px; border-radius: 6px; font-size: 0.75rem; font-weight: 700; margin-left: 6px; }}
        .level-nhan-biet {{ background: #e0f2fe; color: #0284c7; }}
        .level-thong-hieu {{ background: #dcfce7; color: #15803d; }}
        .level-van-dung {{ background: #fef3c7; color: #b45309; }}
        .level-van-dung-cao {{ background: #fee2e2; color: #b91c1c; }}

        .options-grid {{ display: grid; grid-template-columns: 1fr; gap: 10px; }}
        @media (min-width: 640px) {{
            .options-grid {{ grid-template-columns: 1fr 1fr; }}
        }}

        .option-item {{
            background: #f8fafc; border: 1.5px solid var(--border); border-radius: 8px;
            padding: 10px 14px; display: flex; align-items: center; gap: 10px; cursor: pointer;
            transition: all 0.2s; font-size: 0.95rem;
        }}
        .option-item:hover {{ background: #f1f5f9; border-color: #cbd5e1; }}
        .option-item.selected {{
            background: #e0f2fe; border-color: var(--primary); color: #0369a1; font-weight: 600;
        }}
        .option-item.correct {{
            background: #dcfce7 !important; border-color: #22c55e !important; color: #15803d !important; font-weight: 700;
        }}
        .option-item.incorrect {{
            background: #fee2e2 !important; border-color: #ef4444 !important; color: #b91c1c !important;
        }}
        .option-label {{
            display: inline-flex; justify-content: center; align-items: center;
            width: 26px; height: 26px; border-radius: 50%; background: white;
            border: 1.5px solid #cbd5e1; font-weight: 700; font-size: 0.85rem; flex-shrink: 0;
        }}
        .option-item.selected .option-label {{
            background: var(--primary); color: white; border-color: var(--primary);
        }}

        .explanation-box {{
            display: none; background: #f0fdf4; border-left: 4px solid #22c55e;
            padding: 12px 16px; margin-top: 14px; border-radius: 0 8px 8px 0;
            font-size: 0.92rem; color: #166534; line-height: 1.6;
        }}
        .explanation-box.show {{ display: block; animation: fadeIn 0.4s; }}

        .btn-submit {{
            background: linear-gradient(135deg, #0284c7, #0d9488); color: white;
            border: none; padding: 14px 40px; font-size: 1.1rem; font-weight: 700;
            border-radius: 30px; cursor: pointer; box-shadow: 0 6px 20px rgba(2, 132, 199, 0.35);
            transition: all 0.25s;
        }}
        .btn-submit:hover {{ transform: translateY(-2px); box-shadow: 0 8px 25px rgba(2, 132, 199, 0.45); }}

        .results-panel {{
            display: none; background: white; border-radius: 20px; padding: 30px 20px;
            text-align: center; border: 1px solid var(--border); box-shadow: 0 10px 30px rgba(0,0,0,0.06);
            margin-top: 25px;
        }}
        .score-circle {{
            width: 120px; height: 120px; border-radius: 50%;
            background: linear-gradient(135deg, #0284c7, #0d9488);
            color: white; display: flex; flex-direction: column; justify-content: center;
            align-items: center; margin: 0 auto 15px auto; box-shadow: 0 8px 20px rgba(2, 132, 199, 0.35);
        }}
        .score-val {{ font-size: 2.2rem; font-weight: 800; line-height: 1; }}
        .score-max {{ font-size: 0.8rem; font-weight: 600; opacity: 0.9; }}
        .score-title {{ font-size: 1.4rem; font-weight: 700; margin-bottom: 6px; }}
        .score-desc {{ color: var(--text-muted); font-size: 0.95rem; margin-bottom: 20px; text-align: center; }}

        .details-summary {{
            display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
            gap: 12px; margin-top: 20px;
        }}
        .summary-card {{ background: #f8fafc; border: 1px solid var(--border); border-radius: 10px; padding: 12px; }}
        .summary-num {{ font-size: 1.4rem; font-weight: 800; }}
        .summary-label {{ font-size: 0.82rem; color: var(--text-muted); }}

        @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(8px); }} to {{ opacity: 1; transform: translateY(0); }} }}

        footer {{
            text-align: center; margin-top: 40px; font-size: 0.85rem; color: var(--text-muted);
        }}
    </style>
</head>
<body>
    <header class="sticky-header">
        <div class="header-container">
            <a href="#" class="site-logo">
                <i class="fa-solid fa-flask-vial" style="font-size: 1.4rem; color: var(--primary);"></i>
                <span class="logo-text">HÓA HỌC 12 ONLINE</span>
            </a>
            <div class="nav-links">
                <div id="timerBadge" class="timer-badge" style="display: none;">
                    <i class="fa-regular fa-clock"></i>
                    <span id="timerText">30:00</span>
                </div>
            </div>
        </div>
    </header>

    <div class="quiz-container">
        <div class="exam-banner">
            <h1>📝 20 CÂU TRẮC NGHIỆM AMINE</h1>
            <p>HÓA HỌC 12 - BỘ SÁCH KẾT NỐI TRI THỨC VỚI CUỘC SỐNG</p>
            <span class="badge-exam">HỆ THỐNG KIỂM TRA ĐÁNH GIÁ CHUẨN GDPT 2018</span>
        </div>

        <div id="loginCard" class="login-card">
            <div class="login-title">Thông Tin Học Sinh Làm Bài</div>
            <div class="login-subtitle">Vui lòng điền họ tên và lớp để hệ thống tự động ghi nhận kết quả và đồng bộ về Google Sheet</div>
            <div class="form-group">
                <label for="studentName"><i class="fa-solid fa-user"></i> Họ và tên học sinh:</label>
                <input type="text" id="studentName" class="form-control" placeholder="Ví dụ: Nguyễn Văn An" required>
            </div>
            <div class="form-group">
                <label for="studentClass"><i class="fa-solid fa-graduation-cap"></i> Lớp:</label>
                <input type="text" id="studentClass" class="form-control" placeholder="Ví dụ: 12A1" required>
            </div>
            <button id="btnStart" class="btn-start" onclick="startExam()"><i class="fa-solid fa-play"></i> BẮT ĐẦU LÀM BÀI</button>
        </div>

        <div id="examWorkspace" style="display: none;">
            <div class="student-info-bar">
                <span><i class="fa-solid fa-user-graduate"></i> Học sinh: <strong id="displayName"></strong></span>
                <span><i class="fa-solid fa-school"></i> Lớp: <strong id="displayClass"></strong></span>
            </div>

            <div class="progress-container">
                <div class="progress-bar-bg">
                    <div id="progressFill" class="progress-bar-fill"></div>
                </div>
                <div class="progress-text">
                    <span>Tiến độ hoàn thành</span>
                    <span id="progressCount">0 / 20 câu</span>
                </div>
            </div>

            <div class="section-header">
                📌 PHẦN I. Câu hỏi trắc nghiệm nhiều phương án lựa chọn (20 câu - Mức độ từ Nhận biết đến Vận dụng cao)
            </div>
            <p style="font-size: 0.88rem; color: #64748b; margin-bottom: 15px;">Thí sinh chọn 1 phương án đúng (A, B, C hoặc D) cho mỗi câu hỏi. Mỗi câu đúng đạt 0,5 điểm (Tổng điểm: 10,0 điểm).</p>
            
            <div id="questionsContainer"></div>

            <div style="text-align: center; margin: 35px 0 20px 0;">
                <button id="btnSubmit" class="btn-submit" onclick="confirmSubmitExam()">
                    <i class="fa-solid fa-cloud-arrow-up"></i> NỘP BÀI THI & CHẤM ĐIỂM
                </button>
            </div>

            <div id="resultsPanel" class="results-panel">
                <div class="score-circle">
                    <span id="scoreCircle" class="score-val">0.0</span>
                    <small class="score-max">/ 10 ĐIỂM</small>
                </div>
                <div class="score-title" id="scoreTitle">Hoàn Thành Bài Thi!</div>
                <div class="score-desc" id="scoreDesc">Xem hướng dẫn giải chi tiết cho từng câu hỏi bên dưới.</div>

                <div class="details-summary">
                    <div class="summary-card">
                        <div class="summary-num" style="color: #22c55e;" id="correctCountText">0</div>
                        <div class="summary-label">Số câu đúng</div>
                    </div>
                    <div class="summary-card">
                        <div class="summary-num" style="color: #ef4444;" id="incorrectCountText">0</div>
                        <div class="summary-label">Số câu sai</div>
                    </div>
                    <div class="summary-card">
                        <div class="summary-num" style="color: #0284c7;" id="gradeText">0.0/10</div>
                        <div class="summary-label">Điểm số đạt được</div>
                    </div>
                    <div class="summary-card">
                        <div class="summary-num" style="color: #0d9488;" id="timeSpentText">--:--</div>
                        <div class="summary-label">Thời gian làm bài</div>
                    </div>
                </div>
                <div id="sheetSyncStatus" style="display: none; margin: 15px auto; padding: 12px 18px; border-radius: 10px; font-size: 0.92rem; font-weight: 600; background: #f0fdf4; border: 1.5px solid #86efac; color: #166534; max-width: 550px; text-align: center;"></div>
            </div>
        </div>
    </div>

    <footer>
        <p>Hệ thống Học tập & Kiểm tra Trắc nghiệm Hóa học 12 — Chuẩn GDPT 2018</p>
    </footer>

    <script>
        const questionsData = {json.dumps(questions, ensure_ascii=False)};
        const GOOGLE_SHEET_URL = "{GOOGLE_SHEET_URL}";

        let userAnswers = {{}};
        let examSubmitted = false;
        let timerInterval = null;
        let totalTimeSeconds = 30 * 60;
        let timeRemaining = totalTimeSeconds;

        function sendResultsToGoogleSheet(data) {{
            if (!GOOGLE_SHEET_URL || GOOGLE_SHEET_URL.trim() === "" || GOOGLE_SHEET_URL.includes("DAN_LINK")) {{
                return;
            }}
            const statusEl = document.getElementById("sheetSyncStatus");
            if (statusEl) {{
                statusEl.style.display = "block";
                statusEl.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Đang đồng bộ kết quả vào Google Sheet của giáo viên...';
            }}
            fetch(GOOGLE_SHEET_URL, {{
                method: "POST",
                mode: "no-cors",
                headers: {{ "Content-Type": "application/json" }},
                body: JSON.stringify(data)
            }}).then(() => {{
                if (statusEl) {{
                    statusEl.innerHTML = '<i class="fa-solid fa-circle-check"></i> Đã tự động đồng bộ kết quả thành công về Google Sheet!';
                }}
            }}).catch(err => {{
                console.error("Lỗi đồng bộ Google Sheet:", err);
                if (statusEl) {{
                    statusEl.innerHTML = '<i class="fa-solid fa-triangle-exclamation" style="color:#dc2626;"></i> Không thể kết nối Google Sheet. Vui lòng kiểm tra mạng.';
                }}
            }});
        }}

        function startExam() {{
            const name = document.getElementById('studentName').value.trim();
            const sClass = document.getElementById('studentClass').value.trim();
            if (!name || !sClass) {{
                alert('Vui lòng điền đầy đủ Họ và tên và Lớp trước khi bắt đầu!');
                return;
            }}
            document.getElementById('displayName').innerText = name;
            document.getElementById('displayClass').innerText = sClass;
            document.getElementById('loginCard').style.display = 'none';
            document.getElementById('examWorkspace').style.display = 'block';
            document.getElementById('timerBadge').style.display = 'flex';

            renderQuestions();
            startTimer();
            if (window.MathJax) {{ MathJax.typesetPromise(); }}
        }}

        function startTimer() {{
            timerInterval = setInterval(() => {{
                if (timeRemaining <= 0) {{
                    clearInterval(timerInterval);
                    alert('Hết giờ làm bài! Hệ thống tự động nộp bài.');
                    submitExam();
                    return;
                }}
                timeRemaining--;
                const mins = Math.floor(timeRemaining / 60);
                const secs = timeRemaining % 60;
                document.getElementById('timerText').innerText = 
                    `${{mins < 10 ? '0' : ''}}${{mins}}:${{secs < 10 ? '0' : ''}}${{secs}}`;
            }}, 1000);
        }}

        function formatContent(str) {{
            if (str === null || str === undefined) return '';
            return String(str).replace(/\\n/g, '<br>');
        }}

        function getLevelClass(level) {{
            if (level === 'Nhận biết') return 'level-nhan-biet';
            if (level === 'Thông hiểu') return 'level-thong-hieu';
            if (level === 'Vận dụng') return 'level-van-dung';
            return 'level-van-dung-cao';
        }}

        function renderQuestions() {{
            const container = document.getElementById('questionsContainer');
            let html = '';
            questionsData.forEach((q, idx) => {{
                html += `
                <div class="question-card" id="card-${{q.id}}">
                    <div class="question-title">
                        <span class="question-num">Câu ${{idx + 1}}:</span>
                        ${{formatContent(q.question)}}
                        <span class="level-badge ${{getLevelClass(q.level)}}">${{q.level}}</span>
                    </div>
                    <div class="options-grid">
                        ${{Object.entries(q.options).map(([k, v]) => `
                            <div class="option-item" id="opt-${{q.id}}-${{k}}" onclick="selectOption(${{q.id}}, '${{k}}')">
                                <span class="option-label">${{k}}</span>
                                <span>${{formatContent(v)}}</span>
                            </div>
                        `).join('')}}
                    </div>
                    <div class="explanation-box" id="exp-${{q.id}}">
                        <strong>💡 Hướng dẫn giải chi tiết (Đáp án ${{q.answer}}):</strong><br>${{formatContent(q.explanation)}}
                    </div>
                </div>`;
            }});
            container.innerHTML = html;
        }}

        function selectOption(qId, option) {{
            if (examSubmitted) return;
            userAnswers[qId] = option;
            const q = questionsData.find(item => item.id === qId);
            Object.keys(q.options).forEach(k => {{
                const el = document.getElementById(`opt-${{qId}}-${{k}}`);
                if (el) el.classList.remove('selected');
            }});
            const selectedEl = document.getElementById(`opt-${{qId}}-${{option}}`);
            if (selectedEl) selectedEl.classList.add('selected');
            updateProgress();
        }}

        function updateProgress() {{
            const count = Object.keys(userAnswers).length;
            const total = questionsData.length;
            const pct = Math.round((count / total) * 100);
            document.getElementById('progressFill').style.width = pct + '%';
            document.getElementById('progressCount').innerText = `${{count}} / ${{total}} câu (${{pct}}%)`;
        }}

        function confirmSubmitExam() {{
            if (examSubmitted) return;
            const answered = Object.keys(userAnswers).length;
            const total = questionsData.length;
            if (answered < total) {{
                if (!confirm(`Bạn mới trả lời ${{answered}}/${{total}} câu hỏi. Bạn có chắc chắn muốn nộp bài sớm không?`)) {{
                    return;
                }}
            }} else {{
                if (!confirm('Bạn có chắc chắn muốn nộp bài thi để chấm điểm không?')) {{
                    return;
                }}
            }}
            submitExam();
        }}

        function submitExam() {{
            if (examSubmitted) return;
            examSubmitted = true;
            clearInterval(timerInterval);

            document.getElementById('btnSubmit').style.display = 'none';

            let totalCorrect = 0;
            let totalIncorrect = 0;

            questionsData.forEach(q => {{
                const userChoice = userAnswers[q.id];
                const isCorrect = (userChoice === q.answer);
                if (isCorrect) {{
                    totalCorrect++;
                }} else {{
                    totalIncorrect++;
                }}

                Object.keys(q.options).forEach(k => {{
                    const el = document.getElementById(`opt-${{q.id}}-${{k}}`);
                    if (el) {{
                        if (k === q.answer) {{
                            el.classList.add('correct');
                        }} else if (k === userChoice) {{
                            el.classList.add('incorrect');
                        }}
                    }}
                }});

                const expEl = document.getElementById(`exp-${{q.id}}`);
                if (expEl) expEl.classList.add('show');
            }});

            const score = (totalCorrect * 0.5).toFixed(2);
            document.getElementById('scoreCircle').innerText = score;
            document.getElementById('gradeText').innerText = `${{score}}/10`;
            document.getElementById('correctCountText').innerText = totalCorrect;
            document.getElementById('incorrectCountText').innerText = totalIncorrect;

            const spentSeconds = totalTimeSeconds - timeRemaining;
            const sMins = Math.floor(spentSeconds / 60);
            const sSecs = spentSeconds % 60;
            document.getElementById('timeSpentText').innerText = 
                `${{sMins < 10 ? '0' : ''}}${{sMins}}:${{sSecs < 10 ? '0' : ''}}${{sSecs}}`;

            document.getElementById('resultsPanel').style.display = 'block';
            document.getElementById('resultsPanel').scrollIntoView({{ behavior: 'smooth' }});

            sendResultsToGoogleSheet({{
                timestamp: new Date().toLocaleString("vi-VN", {{ timeZone: "Asia/Ho_Chi_Minh" }}),
                studentName: document.getElementById('displayName').innerText,
                studentClass: document.getElementById('displayClass').innerText,
                score: score,
                correctCount: totalCorrect,
                incorrectCount: totalIncorrect,
                timeSpent: document.getElementById('timeSpentText').innerText,
                examTitle: "20 Câu Trắc Nghiệm Amine - Hóa Học 12"
            }});

            if (window.MathJax && window.MathJax.typesetPromise) {{
                MathJax.typesetPromise();
            }}

            if (parseFloat(score) >= 7.0 && typeof confetti === 'function') {{
                confetti({{ particleCount: 100, spread: 70, origin: {{ y: 0.6 }} }});
            }}
        }}
    </script>
</body>
</html>
"""
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Đã tạo file HTML trắc nghiệm online: {out_path}")

if __name__ == "__main__":
    md_file = "dau-ra/lop-12/bai-tap/20-cau-trac-nghiem-nhieu-lua-chon-amine-hoa-hoc-12.md"
    docx_file = "dau-ra/lop-12/bai-tap/20-cau-trac-nghiem-nhieu-lua-chon-amine-hoa-hoc-12.docx"
    html_file = "dau-ra/lop-12/bai-tap/20-cau-trac-nghiem-nhieu-lua-chon-amine-hoa-hoc-12.html"

    generate_markdown(md_file)
    try:
        create_styled_document(md_file, docx_file)
        print(f"Đã tạo file Word DOCX: {docx_file}")
    except PermissionError:
        docx_file_cap_nhat = "dau-ra/lop-12/bai-tap/20-cau-trac-nghiem-nhieu-lua-chon-amine-hoa-hoc-12-cap-nhat.docx"
        create_styled_document(md_file, docx_file_cap_nhat)
        print(f"File gốc đang mở trong Word. Đã tạo file Word DOCX mới: {docx_file_cap_nhat}")
    
    generate_html(html_file)
    print("Tất cả file đã được cập nhật thành công!")

