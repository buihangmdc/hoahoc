"""
Script: generate_quiz_amino_acid_12.py
Purpose: Generate Lesson: Amino acid - Chemistry Grade 12 (Ket noi tri thuc) Worksheet / Exam:
- Part 1: 18 Multiple Choice Questions (A, B, C, D)
  + Questions 14 & 15: Removed given ion formulas, requiring students to deduce the ionic form and migration direction in electric field.
- Part 2: 4 True/False Questions (Contextual Real-world & Experimental)
  + Replaced pH_IE with standard pI notation.
  + Each True/False question includes 1 applied quantitative calculation statement related to context.
- Part 3: 6 Short Answer Questions (Calculations & Counting)
- Output to Markdown, Word (.docx), and interactive HTML (vatli102.com format) with Google Sheet sync
"""

import os
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath("."))
import json
from scripts.export_to_html_quiz import generate_quiz_html
from scripts.export_to_docx import create_styled_document

quiz_data = {
    "title": "ĐỀ ÔN TẬP BÀI: AMINO ACID",
    "badge": "HÓA HỌC 12 - KẾT NỐI TRI THỨC VỚI CUỘC SỐNG",
    "duration": 50,
    "grade": 12,
    "google_sheet_url": "https://script.google.com/macros/s/AKfycbwRRiM81mghvA7cInvJgb4rPLzWOAE3s44wer0BJcURQ4hWwoykS19pkNQ9LyzH6Q8lTQ/exec",
    "part1": [
        {
            "id": 1,
            "question": "Amino acid là loại hợp chất hữu cơ tạp chức mà trong phân tử chứa đồng thời các nhóm chức nào sau đây?",
            "options": {
                "A": "Nhóm hydroxy (-OH) và nhóm carboxyl (-COOH).",
                "B": "Nhóm amino (-NH₂) và nhóm carboxyl (-COOH).",
                "C": "Nhóm amino (-NH₂) và nhóm carbonyl (>C=O).",
                "D": "Nhóm carboxyl (-COOH) và nhóm nitro (-NO₂)."
            },
            "answer": "B",
            "explanation": "Amino acid là hợp chất hữu cơ tạp chức, trong phân tử chứa đồng thời nhóm chức amino (-NH₂) mang tính base và nhóm chức carboxyl (-COOH) mang tính acid."
        },
        {
            "id": 2,
            "question": "Hầu hết các amino acid tạo nên protein của cơ thể sinh vật và cơ thể người thuộc loại nào sau đây?",
            "options": {
                "A": "α-amino acid.",
                "B": "β-amino acid.",
                "C": "γ-amino acid.",
                "D": "ε-amino acid."
            },
            "answer": "A",
            "explanation": "Các amino acid thiên nhiên cấu thành nên chuỗi polypeptide trong phân tử protein của cơ thể sinh vật hầu hết là các α-amino acid (nhóm -NH₂ liên kết trực tiếp với nguyên tử carbon số 2, ngay cạnh nhóm -COOH)."
        },
        {
            "id": 3,
            "question": "Amino acid nào sau đây có phân tử khối nhỏ nhất (M = 75 amu)?",
            "options": {
                "A": "Alanine.",
                "B": "Glycine.",
                "C": "Valine.",
                "D": "Lysine."
            },
            "answer": "B",
            "explanation": "Glycine có công thức cấu tạo thu gọn là H₂N-CH₂-COOH, phân tử khối M = 75 amu, là amino acid đơn giản và có phân tử khối nhỏ nhất."
        },
        {
            "id": 4,
            "question": "Tên gọi thay thế (theo danh pháp IUPAC) của alanine (CH₃-CH(NH₂)-COOH) là",
            "options": {
                "A": "2-aminopropanoic acid.",
                "B": "3-aminopropanoic acid.",
                "C": "aminoethanoic acid.",
                "D": "2-amino-3-methylbutanoic acid."
            },
            "answer": "A",
            "explanation": "Mạch chính của alanine gồm 3 nguyên tử carbon (propanoic acid), đánh số từ carbon của nhóm -COOH là số 1. Nhóm amino (-NH₂) đính ở carbon số 2. Tên thay thế chuẩn là 2-aminopropanoic acid."
        },
        {
            "id": 5,
            "question": "Hợp chất có công thức cấu tạo (CH₃)₂CH-CH(NH₂)-COOH có tên thông thường là",
            "options": {
                "A": "glycine.",
                "B": "alanine.",
                "C": "valine.",
                "D": "glutamic acid."
            },
            "answer": "C",
            "explanation": "Valine là một α-amino acid có mạch nhánh, công thức cấu tạo là (CH₃)₂CH-CH(NH₂)-COOH, có tên thay thế là 2-amino-3-methylbutanoic acid."
        },
        {
            "id": 6,
            "question": "Trong tinh thể và trong dung dịch nước ở điều kiện thường, amino acid tồn tại chủ yếu ở dạng nào sau đây?",
            "options": {
                "A": "Phân tử trung hòa không mang điện H₂N-CH(R)-COOH.",
                "B": "Cation H₃N⁺-CH(R)-COOH.",
                "C": "Anion H₂N-CH(R)-COO⁻.",
                "D": "Ion lưỡng cực H₃N⁺-CH(R)-COO⁻."
            },
            "answer": "D",
            "explanation": "Do trong phân tử có nhóm -COOH có tính acid và nhóm -NH₂ có tính base, proton H⁺ chuyển dịch nội phân tử từ nhóm -COOH sang nhóm -NH₂, tạo thành cấu trúc ion lưỡng cực (zwitterion) H₃N⁺-CH(R)-COO⁻."
        },
        {
            "id": 7,
            "question": "Nhận định nào sau đây về tính chất vật lí của amino acid là ĐÚNG?",
            "options": {
                "A": "Ở điều kiện thường, amino acid là chất lỏng dễ bay hơi, có mùi khai khó chịu.",
                "B": "Amino acid là chất rắn kết tinh, không màu, có nhiệt độ nóng chảy cao và dễ tan trong nước.",
                "C": "Amino acid rất khó tan trong nước nhưng tan vô hạn trong các dung môi hữu cơ không phân cực như benzene.",
                "D": "Tất cả các amino acid đều có nhiệt độ nóng chảy thấp và dễ thăng hoa khi đun nhẹ."
            },
            "answer": "B",
            "explanation": "Vì tồn tại ở dạng ion lưỡng cực với lực hút tĩnh điện liên phân tử mạnh (tương tự như hợp chất ion), amino acid ở thể rắn kết tinh, không màu, vị hơi ngọt, có nhiệt độ nóng chảy cao (bị phân hủy khi nóng chảy) và dễ tan trong nước."
        },
        {
            "id": 8,
            "question": "Amino acid nào sau đây trong phân tử có 2 nhóm amino (-NH₂) và 1 nhóm carboxyl (-COOH)?",
            "options": {
                "A": "Glycine.",
                "B": "Alanine.",
                "C": "Glutamic acid.",
                "D": "Lysine."
            },
            "answer": "D",
            "explanation": "Lysine có công thức phân tử C₆H₁₄N₂O₂ và công thức cấu tạo H₂N-(CH₂)₄-CH(NH₂)-COOH (2,6-diaminohexanoic acid), gồm 2 nhóm amino (-NH₂) và 1 nhóm carboxyl (-COOH)."
        },
        {
            "id": 9,
            "question": "Dung dịch chất nào sau đây làm giấy quỳ tím ẩm chuyển sang màu xanh?",
            "options": {
                "A": "Glycine.",
                "B": "Alanine.",
                "C": "Lysine.",
                "D": "Glutamic acid."
            },
            "answer": "C",
            "explanation": "Lysine có 2 nhóm -NH₂ (tính base) và chỉ có 1 nhóm -COOH (tính acid), nên dung dịch lysine có môi trường kiềm (pH > 7), làm quỳ tím hóa xanh."
        },
        {
            "id": 10,
            "question": "Dung dịch chất nào sau đây làm giấy quỳ tím ẩm chuyển sang màu hồng / đỏ?",
            "options": {
                "A": "Valine.",
                "B": "Glutamic acid.",
                "C": "Glycine.",
                "D": "Lysine."
            },
            "answer": "B",
            "explanation": "Glutamic acid (HOOC-CH₂-CH₂-CH(NH₂)-COOH) có 2 nhóm -COOH và chỉ có 1 nhóm -NH₂, nên dung dịch có môi trường acid yếu (pH < 7), làm quỳ tím chuyển sang màu hồng/đỏ."
        },
        {
            "id": 11,
            "question": "Glycine phản ứng được với cả dung dịch hydrochloric acid (HCl) và dung dịch sodium hydroxide (NaOH). Hiện tượng này chứng minh glycine có",
            "options": {
                "A": "tính acid mạnh.",
                "B": "tính base mạnh.",
                "C": "tính chất lưỡng tính.",
                "D": "tính oxi hóa - khử."
            },
            "answer": "C",
            "explanation": "Hợp chất vừa có khả năng tác dụng với acid mạnh (nhờ nhóm -NH₂), vừa có khả năng tác dụng với base mạnh (nhờ nhóm -COOH) là hợp chất có tính chất lưỡng tính (amphoteric)."
        },
        {
            "id": 12,
            "question": "Khi cho alanine (CH₃-CH(NH₂)-COOH) phản ứng hoàn toàn với dung dịch HCl, muối thu được có công thức cấu tạo là",
            "options": {
                "A": "CH₃-CH(NH₃Cl)-COOH.",
                "B": "CH₃-CH(NH₂)-COONa.",
                "C": "Cl-CH₂-CH(NH₂)-COOH.",
                "D": "CH₃-CH(NHCl)-COOH."
            },
            "answer": "A",
            "explanation": "Nhóm -NH₂ nhận proton H⁺ từ acid HCl tạo thành cation ammonium: CH₃-CH(NH₂)-COOH + HCl → CH₃-CH(NH₃Cl)-COOH (alanine hydrochloride)."
        },
        {
            "id": 13,
            "question": "Cho glycine tác dụng với dung dịch sodium hydroxide (NaOH) vừa đủ, sản phẩm hữu cơ thu được là",
            "options": {
                "A": "H₂N-CH₂-COONa.",
                "B": "NaHN-CH₂-COOH.",
                "C": "H₂N-CH₂-CH₂-OH.",
                "D": "H₃N⁺-CH₂-COO⁻."
            },
            "answer": "A",
            "explanation": "Nhóm -COOH tham gia phản ứng trung hòa với base mạnh NaOH sinh ra muối sodium glycinate và nước: H₂N-CH₂-COOH + NaOH → H₂N-CH₂-COONa + H₂O."
        },
        {
            "id": 14,
            "question": "Trong dung dịch ở pH = 1,0 (môi trường acid mạnh), khi đặt trong một điện trường đồng nhất, phân tử glycine sẽ di chuyển về phía",
            "options": {
                "A": "cực âm (cathode).",
                "B": "cực dương (anode).",
                "C": "không di chuyển về cực nào.",
                "D": "dao động liên tục giữa hai điện cực."
            },
            "answer": "A",
            "explanation": "Ở môi trường acid mạnh (pH = 1,0 < pI = 5,97), nhóm carboxyl dạng -COO⁻ nhận proton H⁺ chuyển thành -COOH không tích điện, trong khi nhóm amino nhận proton tồn tại ở dạng cation -NH₃⁺ tích điện dương (H₃N⁺-CH₂-COOH). Do đó phân tử glycine tích điện dương tổng cộng và bị hút di chuyển về phía cực âm (cathode) trong điện trường."
        },
        {
            "id": 15,
            "question": "Trong dung dịch ở pH = 11,0 (môi trường base mạnh), khi tiến hành điện di, phân tử glycine sẽ di chuyển về phía",
            "options": {
                "A": "cực âm (cathode).",
                "B": "cực dương (anode).",
                "C": "không dịch chuyển trong điện trường.",
                "D": "kết tinh ngay tại vị trí ban đầu."
            },
            "answer": "B",
            "explanation": "Ở môi trường base mạnh (pH = 11,0 > pI = 5,97), nhóm -NH₃⁺ nhường proton H⁺ chuyển thành nhóm -NH₂ không tích điện, trong khi nhóm carboxyl ở dạng anion -COO⁻ tích điện âm (H₂N-CH₂-COO⁻). Do đó phân tử glycine tích điện âm tổng cộng và bị hút di chuyển về phía cực dương (anode) trong điện trường."
        },
        {
            "id": 16,
            "question": "Khi đun nóng hỗn hợp gồm glycine và ethanol có sục khí HCl bão hòa làm xúc tác, sản phẩm ester thu được (ở dạng muối) có công thức cấu tạo là",
            "options": {
                "A": "H₂N-CH₂-COOC₂H₅.",
                "B": "ClH₃N-CH₂-COOC₂H₅.",
                "C": "H₂N-CH₂-CH₂-Cl.",
                "D": "CH₃-COOC₂H₅."
            },
            "answer": "B",
            "explanation": "Trong môi trường acid HCl bão hòa, nhóm -COOH bị ester hóa tạo ester, đồng thời nhóm -NH₂ tác dụng với acid HCl tạo muối ammonium: H₂N-CH₂-COOH + C₂H₅OH + HCl → ClH₃N-CH₂-COOC₂H₅ + H₂O."
        },
        {
            "id": 17,
            "question": "Khi đun nóng 6-aminohexanoic acid (ε-aminocaproic acid) có mặt chất xúc tác thích hợp, xảy ra phản ứng trùng ngưng tạo thành polymer nào sau đây?",
            "options": {
                "A": "Poly(vinyl chloride).",
                "B": "Tơ capron (nylon-6).",
                "C": "Tơ nylon-6,6.",
                "D": "Polyethylene."
            },
            "answer": "B",
            "explanation": "Khi đun nóng, nhóm -NH₂ của phân tử này phản ứng với nhóm -COOH của phân tử kia tách nước tạo liên kết amide, hình thành polycaproamide (tơ capron hay nylon-6): n H₂N-(CH₂)₅-COOH → -(-NH-(CH₂)₅-CO-)-_n + n H₂O."
        },
        {
            "id": 18,
            "question": "Hợp chất nào sau đây được sử dụng phổ biến trong công nghiệp thực phẩm với vai trò là chất điều vị mì chính (bột ngọt)?",
            "options": {
                "A": "Sodium chloride.",
                "B": "Monosodium glutamate (MSG).",
                "C": "Sodium benzoate.",
                "D": "Sodium acetate."
            },
            "answer": "B",
            "explanation": "Monosodium glutamate (MSG) là muối mononatri của glutamic acid, có khả năng kích thích vị giác tạo vị ngọt thịt (umami), được sử dụng rộng rãi làm mì chính (bột ngọt)."
        }
    ],
    "part2": [
        {
            "id": 1,
            "title": "Bột ngọt (Mì chính), An toàn thực phẩm và Hội chứng nhà hàng Trung Hoa",
            "context": "Bột ngọt (Monosodium glutamate - MSG) là phụ gia thực phẩm phổ biến (mã số quốc tế E621) mang vị umami (vị ngọt thịt đặc trưng) được Giáo sư Ikeda Kikunae (Đại học Tokyo) phát hiện lần đầu tiên từ tảo bẹ Kombu vào năm 1908. Bột ngọt là muối mononatri của glutamic acid, có công thức cấu tạo HOOC-[CH₂]₂-CH(NH₂)-COONa. Trong công nghiệp hiện đại, MSG được sản xuất chủ yếu bằng phương pháp lên men vi sinh vật hiếu khí từ nguồn nguyên liệu giàu tinh bột hoặc rỉ đường mía. Một số người nhạy cảm với bột ngọt có thể gặp các triệu chứng tạm thời như hồi hộp, đau đầu, tê mỏi vùng gáy (thường gọi là 'hội chứng quán ăn Trung Hoa'). Ngoài ra, nếu đun nấu ở nhiệt độ quá cao (> 270°C) kéo dài, MSG có thể bị mất nước nội phân tử tạo thành pyroglutamate làm mất vị umami. Dựa vào kiến thức về amino acid, xét tính đúng/sai của các phát biểu sau:",
            "statements": {
                "a": "MSG là muối mononatri của glutamic acid, có công thức phân tử là C₅H₈NO₄Na.",
                "b": "Glutamic acid là một amino acid thiết yếu mà cơ thể con người hoàn toàn không thể tự tổng hợp được, bắt buộc phải lấy từ thức ăn.",
                "c": "Khi hòa tan vào nước, dung dịch MSG có môi trường kiềm mạnh làm quỳ tím chuyển sang màu xanh đậm tương tự như dung dịch lysine.",
                "d": "Để sản xuất được 16,9 kg bột ngọt (monosodium glutamate, M = 169 g/mol) với hiệu suất của toàn bộ quá trình đạt 90%, khối lượng glutamic acid (M = 147 g/mol) tối thiểu cần dùng là 16,33 kg."
            },
            "answers": {
                "a": "Đ",
                "b": "S",
                "c": "S",
                "d": "Đ"
            },
            "explanations": {
                "a": "ĐÚNG: Công thức cấu tạo của MSG là HOOC-CH₂-CH₂-CH(NH₂)-COONa, gom lại ta có công thức phân tử là C₅H₈NO₄Na (M = 169 amu).",
                "b": "SAI: Glutamic acid là amino acid không thiết yếu (non-essential amino acid) vì cơ thể sinh vật có thể tự tổng hợp được từ các chất chuyển hóa trung gian (như α-ketoglutarate).",
                "c": "SAI: Dung dịch MSG trong nước có pH gần như trung tính hoặc kiềm rất yếu (pH khoảng 6,8 - 7,2) do gốc glutamate là anion của acid yếu và vẫn còn một nhóm -COOH liên kết nội phân tử, không làm đổi màu quỳ tím sang xanh đậm như lysine.",
                "d": "ĐÚNG: Số mol MSG lý thuyết cần tạo ra: n(MSG) = 16,9 / 169 = 0,10 kmol = 100 mol. Phản ứng theo tỉ lệ mol 1 : 1 giữa glutamic acid và NaOH. Vì hiệu suất đạt 90%, số mol glutamic acid thực tế cần dùng là: n(Glu) = 0,10 / 0,90 = 1/9 kmol ≈ 0,1111 kmol. Khối lượng glutamic acid cần dùng: m = (1/9) × 147 = 16,33 kg."
            }
        },
        {
            "id": 2,
            "title": "Thí nghiệm khảo sát tính chất acid - base và tính lưỡng tính của amino acid",
            "context": "Tiến hành hai thí nghiệm khảo sát tính chất của amino acid trong phòng thí nghiệm trường THPT:\n- Thí nghiệm 1: Chuẩn bị ba ống nghiệm (1), (2), (3) lần lượt chứa 2 mL dung dịch glycine 0,1 M; lysine 0,1 M; glutamic acid 0,1 M. Dùng đũa thủy tinh nhúng vào từng ống nghiệm rồi chấm lên các mẩu giấy quỳ tím riêng biệt đặt trên mặt kính đồng hồ.\n- Thí nghiệm 2: Cho 2 mL dung dịch glycine vào ống nghiệm (4), nhỏ tiếp từ từ từng giọt dung dịch HCl 1 M vào ống nghiệm, vừa nhỏ vừa lắc đều; sau đó chia dung dịch làm hai phần: Phần một cho tác dụng với vài giọt dung dịch AgNO₃; Phần hai nhỏ từ từ dung dịch NaOH 1 M cho đến dư.\nXét tính đúng/sai của các phát biểu sau:",
            "statements": {
                "a": "Ở Thí nghiệm 1, giấy quỳ tím của ống (1) không đổi màu, ống (2) hóa xanh, ống (3) hóa đỏ/hồng.",
                "b": "Trong dung dịch nước, phân tử glycine tồn tại chủ yếu ở dạng phân tử trung hòa H₂N-CH₂-COOH không mang điện tích.",
                "c": "Ở Thí nghiệm 2, glycine phản ứng với hydrochloric acid nhờ nguyên tử nitrogen của nhóm -NH₂ nhận proton H⁺.",
                "d": "Cho 7,50 gam glycine phản ứng vừa đủ với 100 mL dung dịch HCl 1,0 M thu được dung dịch X; để phản ứng hoàn toàn với các chất tan trong X cần dùng đúng 200 mL dung dịch NaOH 1,0 M."
            },
            "answers": {
                "a": "Đ",
                "b": "S",
                "c": "Đ",
                "d": "Đ"
            },
            "explanations": {
                "a": "ĐÚNG: Glycine có 1 nhóm -NH₂ và 1 nhóm -COOH nên dung dịch trung tính (quỳ tím không đổi màu); Lysine có 2 nhóm -NH₂ và 1 nhóm -COOH nên môi trường base (quỳ hóa xanh); Glutamic acid có 1 nhóm -NH₂ và 2 nhóm -COOH nên môi trường acid (quỳ hóa đỏ/hồng).",
                "b": "SAI: Trong dung dịch nước, amino acid tồn tại chủ yếu ở dạng ion lưỡng cực (zwitterion) H₃N⁺-CH₂-COO⁻ do quá trình chuyển dịch proton nội phân tử.",
                "c": "ĐÚNG: Nhóm amino (-NH₂) có đôi electron tự do trên nguyên tử N đóng vai trò là base theo thuyết Brønsted - Lowry, nhận proton H⁺ từ acid HCl: H₂N-CH₂-COOH + HCl → ClH₃N-CH₂-COOH.",
                "d": "ĐÚNG: Số mol glycine: n(Gly) = 7,50 / 75 = 0,10 mol; số mol HCl = 0,100 × 1,0 = 0,10 mol. Dung dịch X chứa 0,10 mol muối ClH₃N-CH₂-COOH. Muối này phản ứng với NaOH theo tỉ lệ 1 : 2 (gồm nhóm carboxyl -COOH và nhóm ammonium -NH₃⁺): ClH₃N-CH₂-COOH + 2NaOH → H₂N-CH₂-COONa + NaCl + 2H₂O. Do đó n(NaOH) = 2 × 0,10 = 0,20 mol. Thể tích NaOH 1,0 M cần dùng: V = 0,20 / 1,0 = 0,20 lít = 200 mL."
            }
        },
        {
            "id": 3,
            "title": "Kỹ thuật Điện di (Electrophoresis) phân tách amino acid và điểm đẳng điện pI",
            "context": "Điện di là kĩ thuật sinh hóa hiện đại dùng để tách, tinh chế và nhận diện các amino acid dựa vào sự dịch chuyển của các hạt tích điện trong điện trường. Mỗi amino acid có một điểm đẳng điện đặc trưng (kí hiệu là pI). Khi giá trị pH của dung dịch đệm bằng pI, amino acid tồn tại ở dạng ion lưỡng cực có tổng điện tích bằng 0 (không dịch chuyển trong điện trường). Cho biết giá trị pI của ba amino acid:\n- Glycine: pI = 5,97\n- Glutamic acid: pI = 3,22\n- Lysine: pI = 9,74\nNgười ta chấm một giọt dung dịch hỗn hợp gồm 3 amino acid trên lên tâm bản đệm điện di được duy trì ổn định ở pH = 6,00, sau đó áp một hiệu điện thế một chiều xác định. Xét tính đúng/sai của các phát biểu sau:",
            "statements": {
                "a": "Ở pH = 6,00, glycine có pH đệm xấp xỉ pI nên phân tử tồn tại chủ yếu ở dạng ion lưỡng cực có tổng điện tích bằng 0 và hầu như không di chuyển trong điện trường.",
                "b": "Ở pH = 6,00 (pH > pI của glutamic acid), phân tử glutamic acid tích điện âm (dạng anion) nên sẽ di chuyển về phía cực dương (anode).",
                "c": "Ở pH = 6,00 (pH < pI của lysine), phân tử lysine tích điện dương (dạng cation) nên sẽ di chuyển về phía cực âm (cathode).",
                "d": "Cho biết glycine có giá trị hằng số phân li acid của nhóm -COOH là pKa₁ = 2,34 và của nhóm -NH₃⁺ là pKa₂ = 9,60; điểm đẳng điện pI của glycine tính theo công thức bán tổng pI = (pKa₁ + pKa₂) / 2 có giá trị bằng 5,97."
            },
            "answers": {
                "a": "Đ",
                "b": "Đ",
                "c": "Đ",
                "d": "Đ"
            },
            "explanations": {
                "a": "ĐÚNG: Vì pH dung dịch (6,00) gần bằng pI của glycine (5,97), glycine tồn tại chủ yếu dưới dạng ion lưỡng cực H₃N⁺-CH₂-COO⁻, tổng đại số điện tích bằng 0 nên hầu như không di chuyển khỏi vị trí ban đầu.",
                "b": "ĐÚNG: Với glutamic acid, pH = 6,00 > pI (3,22), môi trường kiềm hơn điểm đẳng điện nên glutamic acid nhường proton trở thành anion tích điện âm, bị bản cực dương (anode) hút về.",
                "c": "ĐÚNG: Với lysine, pH = 6,00 < pI (9,74), môi trường acid hơn điểm đẳng điện nên lysine nhận proton trở thành cation tích điện dương, bị bản cực âm (cathode) hút về.",
                "d": "ĐÚNG: Đối với amino acid trung hòa (có 1 nhóm amino và 1 nhóm carboxyl), điểm đẳng điện pI được tính bằng trung bình cộng của 2 giá trị pKa: pI = (pKa₁ + pKa₂) / 2 = (2,34 + 9,60) / 2 = 11,94 / 2 = 5,97."
            }
        },
        {
            "id": 4,
            "title": "Phản ứng trùng ngưng amino acid và ứng dụng sản xuất tơ tổng hợp Polyamide",
            "context": "Trong ngành công nghiệp sợi dệt tổng hợp, sợi polyamide (tơ nylon) chiếm vị trí vô cùng quan trọng nhờ các đặc tính cơ lý ưu việt: độ bền kéo lớn, độ đàn hồi cao, sợi bóng mượt và mau khô. Bên cạnh tơ nylon-6,6 (tổng hợp từ hexamethylenediamine và adipic acid), hai loại tơ nylon rất phổ biến được sản xuất trực tiếp từ phản ứng trùng ngưng của các amino acid mạch dài:\n- Quá trình (1): Đun nóng 6-aminohexanoic acid (ε-aminocaproic acid: H₂N-(CH₂)₅-COOH, M = 131 g/mol) ở nhiệt độ cao có mặt xúc tác, thu được tơ capron (nylon-6).\n- Quá trình (2): Đun nóng 7-aminoheptanoic acid (ω-aminoenanthic acid: H₂N-(CH₂)₆-COOH, M = 145 g/mol) thu được tơ enang (nylon-7).\nXét tính đúng/sai của các phát biểu sau:",
            "statements": {
                "a": "6-aminohexanoic acid và 7-aminoheptanoic acid đều thuộc loại α-amino acid thiên nhiên có mặt trong thành phần protein của cơ thể người.",
                "b": "Phản ứng tổng hợp nylon-6 từ 6-aminohexanoic acid là phản ứng trùng hợp mở vòng vì mạch phân tử polymer không giải phóng phân tử nhỏ nào.",
                "c": "Liên kết -CO-NH- được tạo thành giữa các mắt xích trong phân tử nylon-6 và nylon-7 được gọi là liên kết amide.",
                "d": "Tiến hành trùng ngưng hoàn toàn 26,2 kg 6-aminohexanoic acid (M = 131 g/mol) với hiệu suất phản ứng đạt 90%, khối lượng polymer tơ capron thu được là 20,34 kg."
            },
            "answers": {
                "a": "S",
                "b": "S",
                "c": "Đ",
                "d": "Đ"
            },
            "explanations": {
                "a": "SAI: Trong 6-aminohexanoic acid và 7-aminoheptanoic acid, nhóm -NH₂ gắn ở vị trí carbon số 6 (ε) và số 7 (ω), không phải gắn ở carbon số 2 (α); đây là các amino acid tổng hợp công nghiệp, không phải amino acid cấu tạo protein.",
                "b": "SAI: Phản ứng tổng hợp nylon-6 từ 6-aminohexanoic acid là phản ứng TRÙNG NGƯNG vì ngoài polymer còn giải phóng các phân tử nhỏ là nước (H₂O): n H₂N-(CH₂)₅-COOH → -(-NH-(CH₂)₅-CO-)-_n + n H₂O.",
                "c": "ĐÚNG: Nhóm chức -CO-NH- liên kết giữa gốc acyl và nguyên tử nitrogen được gọi là liên kết amide (đặc trưng của họ polymer polyamide).",
                "d": "ĐÚNG: Số mol 6-aminohexanoic acid phản ứng: n = 26,2 / 131 = 0,20 kmol. Phân tử khối của mỗi mắt xích polycaproamide (-NH-(CH₂)₅-CO-) là: M = 131 - 18 = 113 g/mol. Khối lượng polymer thu được theo lý thuyết: m(LT) = 0,20 × 113 = 22,60 kg. Với hiệu suất phản ứng đạt 90%, khối lượng polymer thực tế thu được là: m = 22,60 × 90% = 20,34 kg."
            }
        }
    ],
    "part3": [
        {
            "id": 1,
            "question": "Cho 7,50 gam một α-amino acid no, mạch hở X (trong phân tử chỉ chứa một nhóm -NH₂ và một nhóm -COOH) tác dụng vừa đủ với 100 mL dung dịch NaOH 1,0 M. Phân tử khối của amino acid X bằng bao nhiêu amu?",
            "answer": "75",
            "explanation": "Số mol NaOH phản ứng: n(NaOH) = 0,100 × 1,0 = 0,10 mol.\nVì phân tử amino acid X chỉ chứa một nhóm -COOH nên tỉ lệ phản ứng với NaOH là 1 : 1:\nX + NaOH → Muối + H₂O\nSuy ra: n(X) = n(NaOH) = 0,10 mol.\nPhân tử khối của amino acid X:\nM(X) = 7,50 / 0,10 = 75 (amu).\n(X chính là Glycine: H₂N-CH₂-COOH, M = 75 amu)."
        },
        {
            "id": 2,
            "question": "Có bao nhiêu đồng phân cấu tạo amino acid (trong phân tử chứa đồng thời nhóm -NH₂ và nhóm -COOH) có cùng công thức phân tử C₃H₇NO₂?",
            "answer": "2",
            "explanation": "Với công thức phân tử C₃H₇NO₂, các đồng phân amino acid có mạch chính 3 carbon C-C-COOH:\n1. CH₃-CH(NH₂)-COOH: 2-aminopropanoic acid (alanine, α-amino acid).\n2. H₂N-CH₂-CH₂-COOH: 3-aminopropanoic acid (β-alanine).\nVậy có tất cả 2 đồng phân cấu tạo amino acid."
        },
        {
            "id": 3,
            "question": "Cho 8,90 gam alanine (CH₃-CH(NH₂)-COOH) phản ứng hoàn toàn với 150 mL dung dịch HCl 1,0 M. Cô cạn cẩn thận toàn bộ dung dịch sau phản ứng thu được m gam chất rắn khan. Giá trị của m bằng bao nhiêu gam? (Làm tròn kết quả đến hai chữ số thập phân).",
            "answer": "12.55",
            "explanation": "Số mol alanine: n(Ala) = 8,90 / 89 = 0,10 mol.\nSố mol HCl ban đầu: n(HCl) = 0,150 × 1,0 = 0,15 mol.\nPhương trình hóa học:\nCH₃-CH(NH₂)-COOH + HCl → CH₃-CH(NH₃Cl)-COOH\nSo sánh tỉ lệ mol: n(HCl) > n(Ala) → HCl dư (0,15 - 0,10 = 0,05 mol), alanine phản ứng hết.\nKhi cô cạn cẩn thận dung dịch, khí HCl dư và nước đều bay hơi hết, chất rắn khan thu được chỉ là muối alanine hydrochloride (CH₃-CH(NH₃Cl)-COOH).\nKhối lượng mol của muối: M = 89 + 36,5 = 125,5 g/mol.\nKhối lượng chất rắn khan:\nm = 0,10 × 125,5 = 12,55 gam."
        },
        {
            "id": 4,
            "question": "Cho dãy gồm 5 amino acid sau: glycine, alanine, valine, glutamic acid, lysine. Có bao nhiêu amino acid trong dãy trên làm đổi màu giấy quỳ tím ẩm?",
            "answer": "2",
            "explanation": "Khảo sát tính acid - base theo số nhóm chức trong phân tử:\n- Glycine, alanine, valine: có 1 nhóm -NH₂ và 1 nhóm -COOH → dung dịch gần như trung tính (pH ≈ 6), không làm đổi màu quỳ tím.\n- Glutamic acid: có 1 nhóm -NH₂ và 2 nhóm -COOH → dung dịch có tính acid (pH < 7), làm quỳ tím hóa đỏ/hồng (1 chất).\n- Lysine: có 2 nhóm -NH₂ và 1 nhóm -COOH → dung dịch có tính base (pH > 7), làm quỳ tím hóa xanh (1 chất).\nVậy có 2 amino acid làm đổi màu giấy quỳ tím ẩm."
        },
        {
            "id": 5,
            "question": "Cho các phát biểu sau về hợp chất amino acid:\n(1) Ở điều kiện thường, các amino acid là những chất rắn kết tinh, có nhiệt độ nóng chảy cao và tương đối dễ tan trong nước.\n(2) Trong dung dịch nước, amino acid tồn tại chủ yếu ở dạng phân tử trung hòa H₂N-CH(R)-COOH.\n(3) Amino acid là hợp chất hữu cơ lưỡng tính, phản ứng được với cả dung dịch acid mạnh và dung dịch base mạnh.\n(4) Muối monosodium glutamate (MSG) được sử dụng phổ biến làm mì chính trong công nghệ thực phẩm.\n(5) Tất cả các amino acid đều làm đổi màu giấy quỳ tím ẩm.\n(6) Dung dịch lysine có môi trường base (pH > 7) do số nhóm amino (-NH₂) nhiều hơn số nhóm carboxyl (-COOH).\nTrong 6 phát biểu trên, có bao nhiêu phát biểu ĐÚNG?",
            "answer": "4",
            "explanation": "Các phát biểu ĐÚNG gồm: (1), (3), (4), (6).\n- Phát biểu (2) SAI: Trong dung dịch nước, amino acid tồn tại chủ yếu ở dạng ion lưỡng cực (zwitterion) H₃N⁺-CH(R)-COO⁻.\n- Phát biểu (5) SAI: Các amino acid có số nhóm -NH₂ bằng số nhóm -COOH như glycine, alanine, valine không làm đổi màu quỳ tím ẩm.\nTổng số phát biểu đúng là 4."
        },
        {
            "id": 6,
            "question": "Cho 15,0 gam glycine (H₂N-CH₂-COOH) tác dụng với lượng dư ethanol có sục khí HCl bão hòa làm xúc tác đun nóng. Sau phản ứng, thu được 16,74 gam muối ethyl glycinate hydrochloride (ClH₃N-CH₂-COOC₂H₅, M = 139,5 g/mol). Hiệu suất của phản ứng ester hóa trên bằng bao nhiêu phần trăm?",
            "answer": "60",
            "explanation": "Số mol glycine ban đầu: n(Gly) = 15,0 / 75 = 0,20 mol.\nPhương trình hóa học phản ứng ester hóa:\nH₂N-CH₂-COOH + C₂H₅OH + HCl → ClH₃N-CH₂-COOC₂H₅ + H₂O\nTheo phương trình, số mol muối ester thu được theo lý thuyết là: n(LT) = 0,20 mol.\nKhối lượng muối ester theo lý thuyết: m(LT) = 0,20 × 139,5 = 27,90 gam.\nHiệu suất của phản ứng ester hóa:\nH = (16,74 / 27,90) × 100% = 60%."
        }
    ]
}

# 1. Xuất file HTML tương tác
html_path = "dau-ra/lop-12/bai-tap/de-on-tap-bai-amino-acid-hoa-hoc-12.html"
generate_quiz_html(quiz_data, html_path)
print(f"Đã tạo file HTML: {html_path}")

# 2. Tạo nội dung Markdown
md_lines = [
    f"# {quiz_data['title']}",
    f"## MÔN HÓA HỌC 12 - BỘ SÁCH KẾT NỐI TRI THỨC VỚI CUỘC SỐNG",
    f"### Thời gian làm bài: {quiz_data['duration']} phút (Không kể thời gian phát đề)",
    "",
    "---",
    "",
    "## PHẦN I. CÂU TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN (4,5 ĐIỂM)",
    "Thí sinh trả lời từ Câu 1 đến Câu 18. Mỗi câu hỏi thí sinh chỉ chọn một phương án. Mỗi câu trả lời đúng thí sinh được 0,25 điểm.",
    ""
]

for q in quiz_data["part1"]:
    md_lines.append(f"Câu {q['id']}: {q['question']}")
    for k in ["A", "B", "C", "D"]:
        md_lines.append(f"{k}. {q['options'][k]}")
    md_lines.append("")

md_lines.extend([
    "---",
    "",
    "## PHẦN II. CÂU TRẮC NGHIỆM ĐÚNG / SAI (4,0 ĐIỂM)",
    "Thí sinh trả lời từ Câu 1 đến Câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.",
    "Thí sinh chỉ lựa chọn chính xác 01 ý trong 01 câu được 0,1 điểm; lựa chọn chính xác 02 ý được 0,25 điểm; lựa chọn chính xác 03 ý được 0,5 điểm; lựa chọn chính xác cả 04 ý được 1,0 điểm.",
    ""
])

for q in quiz_data["part2"]:
    md_lines.append(f"Câu {q['id']}: {q['title']}")
    if q.get("context"):
        md_lines.append(q["context"])
    for k in ["a", "b", "c", "d"]:
        md_lines.append(f"{k}) {q['statements'][k]}")
    md_lines.append("")

md_lines.extend([
    "---",
    "",
    "## PHẦN III. CÂU TRẮC NGHIỆM TRẢ LỜI NGẮN (1,5 ĐIỂM)",
    "Thí sinh trả lời từ Câu 1 đến Câu 6. Mỗi câu trả lời đúng thí sinh được 0,25 điểm.",
    ""
])

for q in quiz_data["part3"]:
    md_lines.append(f"Câu {q['id']}: {q['question']}")
    md_lines.append(f"Đáp số: {q['answer']}")
    md_lines.append("")

md_lines.extend([
    "---",
    "",
    "## HƯỚNG DẪN CHẤM VÀ ĐÁP ÁN CHI TIẾT",
    "",
    "### BẢNG ĐÁP ÁN PHẦN I",
    "| Câu | Đáp án | Câu | Đáp án | Câu | Đáp án |",
    "| :---: | :---: | :---: | :---: | :---: | :---: |",
    "| 1 | B | 7 | B | 13 | A |",
    "| 2 | A | 8 | D | 14 | A |",
    "| 3 | B | 9 | C | 15 | B |",
    "| 4 | A | 10 | B | 16 | B |",
    "| 5 | C | 11 | C | 17 | B |",
    "| 6 | D | 12 | A | 18 | B |",
    "",
    "### BẢNG ĐÁP ÁN PHẦN II",
    "| Câu | Lệnh hỏi | Đáp án (Đ/S) | Câu | Lệnh hỏi | Đáp án (Đ/S) |",
    "| :---: | :---: | :---: | :---: | :---: | :---: |",
    "| 1 | a | Đ | 3 | a | Đ |",
    "| 1 | b | S | 3 | b | Đ |",
    "| 1 | c | S | 3 | c | Đ |",
    "| 1 | d | Đ | 3 | d | Đ |",
    "| 2 | a | Đ | 4 | a | S |",
    "| 2 | b | S | 4 | b | S |",
    "| 2 | c | Đ | 4 | c | Đ |",
    "| 2 | d | Đ | 4 | d | Đ |",
    "",
    "### BẢNG ĐÁP ÁN PHẦN III",
    "| Câu | Lời giải tóm tắt | Đáp số |",
    "| :---: | :--- | :---: |",
    "| 1 | n_NaOH = 0,10 mol -> M_X = 7,50 / 0,10 = 75 amu (Glycine) | 75 |",
    "| 2 | C₃H₇NO₂: alanine (α) và β-alanine -> 2 đồng phân amino acid | 2 |",
    "| 3 | n_Ala = 0,10 mol; HCl dư; m_rắn = 0,10 × 125,5 = 12,55 gam | 12.55 |",
    "| 4 | Glu (hóa đỏ/hồng) và Lys (hóa xanh) -> 2 amino acid | 2 |",
    "| 5 | Các phát biểu đúng gồm: (1), (3), (4), (6) -> 4 phát biểu | 4 |",
    "| 6 | n_Gly = 0,20 mol -> m_LT = 27,90 g -> H = (16,74 / 27,90) × 100% = 60% | 60 |",
    "",
    "---",
    "",
    "### LỜI GIẢI CHI TIẾT TỪNG PHẦN",
    "",
    "#### PHẦN I: TRẮC NGHIỆM NHIỀU LỰA CHỌN"
])

for q in quiz_data["part1"]:
    md_lines.append(f"Câu {q['id']}: Chọn {q['answer']}.")
    md_lines.append(f"Lời giải: {q['explanation']}")
    md_lines.append("")

md_lines.append("#### PHẦN II: TRẮC NGHIỆM ĐÚNG / SAI")
for q in quiz_data["part2"]:
    md_lines.append(f"Câu {q['id']}: {q['title']}")
    for k, exp in q["explanations"].items():
        ans_text = "Đúng" if q["answers"][k] == "Đ" else "Sai"
        md_lines.append(f"{k}) {ans_text}. {exp}")
    md_lines.append("")

md_lines.append("#### PHẦN III: TRẮC NGHIỆM TRẢ LỜI NGẮN")
for q in quiz_data["part3"]:
    md_lines.append(f"Câu {q['id']}: Đáp số {q['answer']}.")
    md_lines.append(f"Lời giải: {q['explanation']}")
    md_lines.append("")

md_path = "dau-ra/lop-12/bai-tap/de-on-tap-bai-amino-acid-hoa-hoc-12.md"
os.makedirs(os.path.dirname(md_path), exist_ok=True)
with open(md_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))
print(f"Đã tạo file Markdown: {md_path}")

# 3. Xuất Word DOCX
docx_path = "dau-ra/lop-12/bai-tap/de-on-tap-bai-amino-acid-hoa-hoc-12.docx"
create_styled_document(md_path, docx_path)
print(f"Đã tạo file Word DOCX: {docx_path}")

# 4. Xuất HTML trắc nghiệm online
html_path = "dau-ra/lop-12/bai-tap/de-on-tap-bai-amino-acid-hoa-hoc-12.html"
generate_quiz_html(quiz_data, html_path)
print(f"Đã tạo file HTML trắc nghiệm: {html_path}")

# 5. Lưu bản web vào lop-12/
web_path = "lop-12/de-on-tap-amino-acid.html"
import shutil
shutil.copy(html_path, web_path)
print(f"Đã cập nhật file HTML tại: {web_path}")
