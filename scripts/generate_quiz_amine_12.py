"""
Script: generate_quiz_amine_12.py
Purpose: Generate Lesson 8: Amine - Chemistry Grade 12 (Ket noi tri thuc) Worksheet / Exam:
- Part 1: 18 Multiple Choice Questions (A, B, C, D)
- Part 2: 4 True/False Questions (Contextual Real-world & Experimental)
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
    "title": "ĐỀ ÔN TẬP BÀI 8: AMINE",
    "badge": "HÓA HỌC 12 - KẾT NỐI TRI THỨC VỚI CUỘC SỐNG",
    "duration": 50,
    "grade": 12,
    "google_sheet_url": "https://script.google.com/macros/s/AKfycbwRRiM81mghvA7cInvJgb4rPLzWOAE3s44wer0BJcURQ4hWwoykS19pkNQ9LyzH6Q8lTQ/exec",
    "part1": [
        {
            "id": 1,
            "question": "Hợp chất nào sau đây thuộc loại amine bậc III?",
            "options": {
                "A": "CH₃-NH-CH₂-CH₃",
                "B": "(CH₃)₃N",
                "C": "CH₃-CH₂-CH₂-NH₂",
                "D": "C₆H₅-NH-CH₃"
            },
            "answer": "B",
            "explanation": "Bậc của amine được xác định bằng số nguyên tử hydrogen trong phân tử ammonia (NH₃) bị thay thế bởi các gốc hydrocarbon. Hợp chất (CH₃)₃N (trimethylamine) có cả 3 nguyên tử H bị thay thế bởi 3 nhóm methyl nên là amine bậc III. CH₃-NH-CH₂-CH₃ và C₆H₅-NH-CH₃ là amine bậc II; CH₃-CH₂-CH₂-NH₂ là amine bậc I."
        },
        {
            "id": 2,
            "question": "Tên gọi thay thế (theo danh pháp IUPAC) của amine có công thức cấu tạo CH₃-CH(NH₂)-CH₃ là",
            "options": {
                "A": "isopropylamine.",
                "B": "propan-1-amine.",
                "C": "propan-2-amine.",
                "D": "1-methylethanamine."
            },
            "answer": "C",
            "explanation": "Theo danh pháp thay thế IUPAC, chọn mạch chính dài nhất chứa nhóm amine và đánh số sao cho vị trí nhóm amine là nhỏ nhất. Mạch chính có 3 nguyên tử C (propane), nhóm -NH₂ liên kết ở nguyên tử carbon số 2. Tên thay thế là propan-2-amine (isopropylamine là tên gốc - chức)."
        },
        {
            "id": 3,
            "question": "Hợp chất CH₃-NH-C₂H₅ có tên gốc - chức là",
            "options": {
                "A": "ethylmethylamine.",
                "B": "methylethylamine.",
                "C": "N-methylethanamine.",
                "D": "propan-2-amine."
            },
            "answer": "A",
            "explanation": "Theo danh pháp gốc - chức, tên các gốc alkyl được gọi theo thứ tự bảng chữ cái alphabet (ethyl đứng trước methyl), sau đó thêm từ 'amine'. Do đó hợp chất có tên gốc - chức là ethylmethylamine. (N-methylethanamine là tên thay thế)."
        },
        {
            "id": 4,
            "question": "Aniline (phenylamine) là amine thơm đơn giản và quan trọng nhất. Công thức phân tử của aniline là",
            "options": {
                "A": "C₇H₉N.",
                "B": "C₆H₇N.",
                "C": "C₆H₅N.",
                "D": "C₆H₁₃N."
            },
            "answer": "B",
            "explanation": "Aniline có công thức cấu tạo là C₆H₅NH₂, gồm một nhóm amino (-NH₂) liên kết trực tiếp với vòng benzene. Gom các nguyên tử lại ta được công thức phân tử là C₆H₇N (phân tử khối M = 93 amu)."
        },
        {
            "id": 5,
            "question": "Ở điều kiện thường, dãy gồm các amine đều tồn tại ở thể khí, có mùi khai khó chịu và độc là",
            "options": {
                "A": "methylamine, ethylamine, dimethylamine, trimethylamine.",
                "B": "aniline, methylamine, ethylamine, dimethylamine.",
                "C": "propylamine, dimethylamine, trimethylamine, aniline.",
                "D": "methylamine, benzylamine, ethylamine, diethylamine."
            },
            "answer": "A",
            "explanation": "Bốn amine đầu dãy đồng đẳng gồm methylamine (CH₃NH₂), ethylamine (C₂H₅NH₂), dimethylamine ((CH₃)₂NH) và trimethylamine ((CH₃)₃N) là những chất khí ở điều kiện thường, có mùi khai nồng khó chịu, độc và tan rất nhiều trong nước."
        },
        {
            "id": 6,
            "question": "Nhận định nào sau đây về tính chất vật lí của aniline là KHÔNG đúng?",
            "options": {
                "A": "Aniline là chất lỏng không màu, mùi hắc và rất độc.",
                "B": "Khi để lâu trong không khí, aniline dễ bị oxy hóa và dần chuyển sang màu nâu đen.",
                "C": "Aniline tan vô hạn trong nước lạnh ở nhiệt độ phòng.",
                "D": "Aniline nặng hơn nước và có xu hướng chìm xuống đáy ống nghiệm khi trộn với nước cất."
            },
            "answer": "C",
            "explanation": "Aniline rất ít tan trong nước lạnh (ở 20°C độ tan chỉ khoảng 3,6 g/100 g nước). Do khối lượng riêng lớn hơn nước (D ≈ 1,02 g/mL), khi cho vào nước lạnh aniline tạo thể vẩn đục rồi tách lớp lắng xuống đáy ống nghiệm. Nhận định C sai."
        },
        {
            "id": 7,
            "question": "Chất nào sau đây có nhiệt độ sôi cao nhất?",
            "options": {
                "A": "C₂H₆ (ethane, M = 30 amu).",
                "B": "CH₃-O-CH₃ (dimethyl ether, M = 46 amu).",
                "C": "CH₃-CH₂-NH₂ (ethylamine, M = 45 amu).",
                "D": "CH₃-CH₂-OH (ethanol, M = 46 amu)."
            },
            "answer": "D",
            "explanation": "Ethanol có liên kết hydrogen liên phân tử dạng O-H···O rất bền (do oxygen có độ âm điện lớn hơn nitrogen). Ethylamine cũng tạo được liên kết hydrogen N-H···N nhưng yếu hơn alcohol tương ứng. Hydrocarbon và ether không tạo được liên kết hydrogen liên phân tử. Do đó nhiệt độ sôi: ethanol (78,3°C) > ethylamine (16,6°C) > dimethyl ether (-24°C) > ethane (-88,6°C)."
        },
        {
            "id": 8,
            "question": "Trong phân tử methylamine (CH₃NH₂), nguyên tử nitrogen ở trạng thái lai hóa sp³ và hình học phân tử xung quanh nguyên tử N có dạng",
            "options": {
                "A": "đường thẳng.",
                "B": "tam giác phẳng.",
                "C": "hình chóp tam giác (tháp tam giác).",
                "D": "hình tứ diện đều."
            },
            "answer": "C",
            "explanation": "Tương tự phân tử ammonia (NH₃), nguyên tử N trong methylamine có 3 liên kết σ (1 liên kết C-N và 2 liên kết N-H) và 1 cặp electron tự do chưa liên kết. Do lực đẩy của cặp electron tự do, hình dạng hình học xung quanh nguyên tử N có cấu trúc hình chóp tam giác (tháp tam giác)."
        },
        {
            "id": 9,
            "question": "Dãy các chất được sắp xếp theo thứ tự tính base tăng dần từ trái sang phải là",
            "options": {
                "A": "C₆H₅NH₂ < NH₃ < CH₃NH₂ < (CH₃)₂NH",
                "B": "NH₃ < C₆H₅NH₂ < CH₃NH₂ < (CH₃)₂NH",
                "C": "(CH₃)₂NH < CH₃NH₂ < NH₃ < C₆H₅NH₂",
                "D": "C₆H₅NH₂ < CH₃NH₂ < NH₃ < (CH₃)₂NH"
            },
            "answer": "A",
            "explanation": "Gốc phenyl (-C₆H₅) hút electron liên hợp làm giảm mật độ điện tích trên nguyên tử N nên aniline có tính base yếu hơn ammonia (NH₃). Nhóm methyl (-CH₃) đẩy electron làm tăng mật độ electron trên N, làm tăng lực base. Amine bậc II có 2 nhóm đẩy electron nên tính base mạnh hơn amine bậc I. Thứ tự tăng dần chuẩn: C₆H₅NH₂ < NH₃ < CH₃NH₂ < (CH₃)₂NH."
        },
        {
            "id": 10,
            "question": "Dung dịch chất nào sau đây KHÔNG làm đổi màu giấy quỳ tím ẩm?",
            "options": {
                "A": "Methylamine.",
                "B": "Dimethylamine.",
                "C": "Ethylamine.",
                "D": "Aniline."
            },
            "answer": "D",
            "explanation": "Alkylamine (methylamine, dimethylamine, ethylamine) có tính base mạnh hơn NH₃, làm quỳ tím ẩm hóa xanh. Aniline có tính base rất yếu do hiệu ứng hút e của gốc phenyl, dung dịch aniline không làm đổi màu quỳ tím và cũng không làm đổi màu phenolphthalein."
        },
        {
            "id": 11,
            "question": "Cho mẩu giấy quỳ tím ẩm vào bình chứa khí methylamine, sau đó đưa đũa thủy tinh nhúng dung dịch HCl đặc vào gần miệng bình. Hiện tượng quan sát được là",
            "options": {
                "A": "quỳ tím chuyển đỏ, xuất hiện khói trắng dày đặc.",
                "B": "quỳ tím chuyển xanh, xuất hiện khói trắng dày đặc.",
                "C": "quỳ tím chuyển xanh, xuất hiện khí màu vàng lục.",
                "D": "quỳ tím mất màu, không có hiện tượng gì thêm."
            },
            "answer": "B",
            "explanation": "Khí methylamine có tính base nên làm quỳ tím ẩm hóa xanh. Hơi methylamine bay lên gặp hơi HCl bay ra từ dung dịch đặc phản ứng tạo thành tinh thể muối methylammonium chloride lơ lửng trong không khí như khói trắng: CH₃NH₂(g) + HCl(g) → CH₃NH₃Cl(s)."
        },
        {
            "id": 12,
            "question": "Nhỏ từ từ từng giọt dung dịch ethylamine vào ống nghiệm chứa dung dịch FeCl₃, hiện tượng quan sát được là",
            "options": {
                "A": "có kết tủa màu nâu đỏ xuất hiện, không tan khi amine dư.",
                "B": "có kết tủa màu trắng xanh xuất hiện, sau đó hóa nâu đỏ trong không khí.",
                "C": "xuất hiện kết tủa trắng, sau đó kết tủa tan dần tạo dung dịch trong suốt.",
                "D": "có bọt khí không màu thoát ra và xuất hiện kết tủa màu nâu đỏ."
            },
            "answer": "A",
            "explanation": "Dung dịch ethylamine có tính base yếu, cung cấp ion OH⁻: C₂H₅NH₂ + H₂O ⇌ C₂H₅NH₃⁺ + OH⁻. Ion OH⁻ kết hợp với Fe³⁺ tạo kết tủa iron(III) hydroxide màu nâu đỏ: FeCl₃ + 3C₂H₅NH₂ + 3H₂O → Fe(OH)₃↓ (nâu đỏ) + 3C₂H₅NH₃Cl. Kết tủa Fe(OH)₃ không có khả năng tạo phức tan với amine nên không tan khi amine dư."
        },
        {
            "id": 13,
            "question": "Khi nhỏ dung dịch methylamine dư vào ống nghiệm chứa kết tủa copper(II) hydroxide (Cu(OH)₂), hiện tượng quan sát được là",
            "options": {
                "A": "kết tủa không tan, giữ nguyên màu xanh lam.",
                "B": "kết tủa tan dần tạo thành dung dịch phức chất màu xanh lam thẫm.",
                "C": "kết tủa chuyển dần sang màu đen do bị khử.",
                "D": "có khí không màu thoát ra và xuất hiện kết tủa đỏ gạch."
            },
            "answer": "B",
            "explanation": "Tương tự như ammonia, các alkylamine đơn chức phân tử nhỏ như methylamine, ethylamine có khả năng tạo phức chất tan với Cu(OH)₂ nhờ cặp electron tự do trên nguyên tử N: Cu(OH)₂ + 4CH₃NH₂ → [Cu(CH₃NH₂)₄](OH)₂ (dung dịch phức chất màu xanh lam thẫm)."
        },
        {
            "id": 14,
            "question": "Cho ethylamine (C₂H₅NH₂) tác dụng với dung dịch hỗn hợp NaNO₂ và HCl ở nhiệt độ phòng, sản phẩm thu được gồm",
            "options": {
                "A": "C₂H₅OH, N₂ và H₂O.",
                "B": "[C₂H₅N₂⁺]Cl⁻ và H₂O.",
                "C": "CH₃CHO, NH₃ và HCl.",
                "D": "C₂H₅NO₂ và NaCl."
            },
            "answer": "A",
            "explanation": "Alkylamine bậc I phản ứng với nitrous acid (HNO₂ tạo ra từ NaNO₂ + HCl) ở nhiệt độ phòng sinh ra alcohol tương ứng, giải phóng bọt khí nitrogen và nước: C₂H₅NH₂ + HNO₂ → C₂H₅OH + N₂↑ + H₂O. Phản ứng này dùng để định lượng hoặc nhận biết amine bậc I mạch hở."
        },
        {
            "id": 15,
            "question": "Cho aniline tác dụng với dung dịch nitrous acid (HNO₂) có mặt acid HCl ở nhiệt độ 0 - 5°C (ngâm trong nước đá) thu được chất X. Chất X là",
            "options": {
                "A": "phenol (C₆H₅OH).",
                "B": "phenyldiazonium chloride ([C₆H₅N₂⁺]Cl⁻).",
                "C": "nitrobenzene (C₆H₅NO₂).",
                "D": "phenylammonium chloride (C₆H₅NH₃Cl)."
            },
            "answer": "B",
            "explanation": "Aniline (arylamine bậc I) tác dụng với HNO₂ có mặt HCl ở nhiệt độ thấp (0 - 5°C) tạo ra muối phenyldiazonium chloride tương đối bền ở nhiệt độ lạnh: C₆H₅NH₂ + HNO₂ + HCl (0 - 5°C) → [C₆H₅N₂⁺]Cl⁻ + 2H₂O. Muối diazonium là chất trung gian quan trọng để tổng hợp phẩm nhuộm azo."
        },
        {
            "id": 16,
            "question": "Để nhận biết aniline và ethylamine bằng phương pháp hóa học đơn giản, người ta có thể sử dụng thuốc thử nào sau đây?",
            "options": {
                "A": "Dung dịch acid HCl.",
                "B": "Nước bromine (Br₂/H₂O).",
                "C": "Dung dịch NaOH.",
                "D": "Khí oxygen ở điều kiện thường."
            },
            "answer": "B",
            "explanation": "Nhóm -NH₂ hoạt hóa vòng benzene rất mạnh ở các vị trí ortho và para, aniline phản ứng dễ dàng với nước bromine ngay ở nhiệt độ phòng tạo kết tủa trắng 2,4,6-tribromoaniline. Ethylamine không phản ứng tạo kết tủa với nước bromine."
        },
        {
            "id": 17,
            "question": "Trong công nghiệp, aniline thường được sản xuất bằng cách khử hợp chất nào sau đây?",
            "options": {
                "A": "Benzene (C₆H₆).",
                "B": "Phenol (C₆H₅OH).",
                "C": "Nitrobenzene (C₆H₅NO₂).",
                "D": "Benzoic acid (C₆H₅COOH)."
            },
            "answer": "C",
            "explanation": "Aniline được sản xuất chủ yếu bằng phương pháp khử nitrobenzene (C₆H₅NO₂) bằng hydrogen mới sinh (thường dùng kim loại Fe hoặc Zn tác dụng với dung dịch HCl đun nóng): C₆H₅NO₂ + 6[H] (Fe + HCl, t°) → C₆H₅NH₂ + 2H₂O."
        },
        {
            "id": 18,
            "question": "Hợp chất diamine nào sau đây là nguyên liệu quan trọng được dùng để trùng ngưng với adipic acid sản xuất tơ nylon-6,6?",
            "options": {
                "A": "Hexamethylenediamine (hexane-1,6-diamine).",
                "B": "Ethylenediamine (ethane-1,2-diamine).",
                "C": "Tetramethylenediamine (butane-1,4-diamine).",
                "D": "Phenylenediamine (benzene-1,4-diamine)."
            },
            "answer": "A",
            "explanation": "Tơ nylon-6,6 là một loại polyamide tổng hợp từ phản ứng đồng trùng ngưng giữa hexamethylenediamine (H₂N-(CH₂)₆-NH₂) và adipic acid (HOOC-(CH₂)₄-COOH)."
        }
    ],
    "part2": [
        {
            "id": 1,
            "title": "Mùi tanh của cá và ứng dụng trung hòa amine trong đời sống",
            "context": "Trong quá trình đánh bắt và bảo quản thủy hải sản, các vi sinh vật và enzyme phân giải protein và hợp chất chứa nitrogen sinh ra hỗn hợp các amine bay hơi (chủ yếu là trimethylamine, dimethylamine và methylamine), tạo nên mùi tanh nồng khó chịu đặc trưng. Để loại bỏ mùi tanh khi chế biến món ăn, kinh nghiệm dân gian thường rửa cá với nước vo gạo, giấm ăn hoặc nước cốt chanh; khi nấu canh cá thường nấu với các quả có vị chua (me, sấu, khế, cà chua) hoặc ướp cá với rượu trắng. Dựa vào kiến thức về hợp chất amine, xét tính đúng/sai của các phát biểu sau:",
            "statements": {
                "a": "Mùi tanh đặc trưng của cá ươn sinh ra chủ yếu do các amine bậc thấp bay hơi, trong đó có trimethylamine (CH₃)₃N.",
                "b": "Giấm ăn (chứa acetic acid) và nước cốt chanh (chứa citric acid) giúp khử mùi tanh vì các acid này tác dụng với amine tạo thành muối ammonium ion dễ tan trong nước và không còn khả năng bay hơi.",
                "c": "Để khử mùi tanh của cá nhanh hơn, ta có thể ngâm rửa cá bằng dung dịch xà phòng hoặc dung dịch nước vôi trong có tính kiềm.",
                "d": "Khi hòa tan vào nước ở cùng nồng độ, dung dịch trimethylamine làm quỳ tím hóa xanh, còn dung dịch aniline không làm đổi màu quỳ tím."
            },
            "answers": {
                "a": "Đ",
                "b": "Đ",
                "c": "S",
                "d": "Đ"
            },
            "explanations": {
                "a": "ĐÚNG: Trimethylamine ((CH₃)₃N) và các amine bay hơi là nguyên nhân cốt lõi gây ra mùi tanh khó chịu của cá và hải sản.",
                "b": "ĐÚNG: Amine có tính base tác dụng với acid hữu cơ tạo thành muối ammonium ion tan tốt trong nước, không bay hơi nên triệt tiêu hoàn toàn mùi tanh.",
                "c": "SAI: Môi trường kiềm giữ amine ở dạng phân tử tự do, càng kích thích amine bay hơi gây mùi nồng hơn; mặt khác xà phòng và nước vôi gây độc hại cho thực phẩm.",
                "d": "ĐÚNG: Trimethylamine là alkylamine có tính base mạnh hơn ammonia nên làm quỳ tím hóa xanh; aniline có tính base rất yếu do hiệu ứng hút e của vòng benzene nên không đổi màu quỳ tím."
            }
        },
        {
            "id": 2,
            "title": "Khảo sát tính tan, tính base và phản ứng đặc trưng của aniline",
            "context": "Tiến hành khảo sát tính chất của aniline theo các bước thí nghiệm sau:\n- Bước 1: Cho khoảng 2 mL nước cất vào ống nghiệm (1), sau đó nhỏ tiếp khoảng 5 giọt aniline vào, lắc mạnh rồi để yên trong 3 phút.\n- Bước 2: Nhỏ từ từ từng giọt dung dịch HCl loãng vào ống nghiệm (1), vừa nhỏ vừa lắc đều.\n- Bước 3: Cho tiếp lượng dư dung dịch NaOH vào ống nghiệm (1), lắc đều rồi để yên vài phút.\n- Bước 4: Lấy một ống nghiệm (2) chứa 1 mL dung dịch aniline, nhỏ tiếp từng giọt nước bromine vào và lắc nhẹ.\nXét tính đúng/sai của các phát biểu sau:",
            "statements": {
                "a": "Ở Bước 1, aniline tan hoàn toàn trong nước cất tạo thành một dung dịch đồng nhất, trong suốt.",
                "b": "Ở Bước 2, chất lỏng trong ống nghiệm (1) trở nên đồng nhất, trong suốt do aniline tác dụng với HCl tạo muối phenylammonium chloride (C₆H₅NH₃Cl) là hợp chất ion tan tốt trong nước.",
                "c": "Ở Bước 3, khi thêm NaOH dư vào, chất lỏng trong ống nghiệm (1) lại bị vẩn đục và phân lớp trở lại do phản ứng tái tạo ra aniline không tan trong nước.",
                "d": "Ở Bước 4, trong ống nghiệm (2) xuất hiện kết tủa màu vàng nhạt của hợp chất monobromoaniline."
            },
            "answers": {
                "a": "S",
                "b": "Đ",
                "c": "Đ",
                "d": "S"
            },
            "explanations": {
                "a": "SAI: Aniline rất ít tan trong nước lạnh. Khi lắc với nước cất, aniline tạo thành hỗn dịch vẩn đục, để yên sẽ phân lớp và aniline nặng hơn chìm xuống đáy.",
                "b": "ĐÚNG: Phản ứng tạo muối ion tan: C₆H₅NH₂ + HCl → C₆H₅NH₃Cl. Muối phenylammonium chloride tan hoàn toàn trong nước làm dung dịch trong suốt.",
                "c": "ĐÚNG: Base mạnh NaOH đẩy aniline ra khỏi muối: C₆H₅NH₃Cl + NaOH → C₆H₅NH₂ + NaCl + H₂O. Aniline sinh ra ít tan trong nước làm dung dịch vẩn đục và phân lớp trở lại.",
                "d": "SAI: Nhóm -NH₂ định hướng thế đồng thời vào các vị trí 2, 4, 6 tạo kết tủa màu TRẮNG của 2,4,6-tribromoaniline, không phải kết tủa màu vàng."
            }
        },
        {
            "id": 3,
            "title": "Phản ứng với nitrous acid (HNO₂) & Công nghiệp phẩm màu Azo",
            "context": "Nitrous acid (HNO₂) là một acid kém bền, thường được tạo ra trực tiếp trong dung dịch phản ứng bằng cách phối trộn sodium nitrite (NaNO₂) với hydrochloric acid (HCl). Hóa học của amine với nitrous acid phụ thuộc chặt chẽ vào cấu trúc amine và nhiệt độ phản ứng:\n- Thí nghiệm 1: Cho ethylamine tác dụng với hỗn hợp NaNO₂ và HCl ở nhiệt độ phòng.\n- Thí nghiệm 2: Cho aniline tác dụng với hỗn hợp NaNO₂ và HCl ở 0 - 5°C (ngâm trong chậu nước đá) thu được dung dịch chất X. Tiếp tục cho chất X tác dụng với dung dịch sodium phenolate trong môi trường kiềm thấy xuất hiện hợp chất màu đỏ cam rực rỡ (chất Y).\nXét tính đúng/sai của các phát biểu sau:",
            "statements": {
                "a": "Ở Thí nghiệm 1, hiện tượng quan sát được là có bọt khí không màu thoát ra liên tục từ dung dịch, đó là khí nitrogen (N₂).",
                "b": "Ở Thí nghiệm 2, chất X được tạo thành trong dung dịch là muối phenyldiazonium chloride [C₆H₅N₂⁺]Cl⁻.",
                "c": "Nếu tiến hành Thí nghiệm 2 ở nhiệt độ cao (80 - 100°C) ngay từ đầu thì muối phenyldiazonium sinh ra càng bền vững và phản ứng tạo phẩm màu Y càng thuận lợi hơn.",
                "d": "Hợp chất Y có màu đỏ cam thu được thuộc loại phẩm màu azo (chứa nhóm mang màu -N=N-), được ứng dụng rộng rãi trong công nghiệp nhuộm sợi dệt và in ấn."
            },
            "answers": {
                "a": "Đ",
                "b": "Đ",
                "c": "S",
                "d": "Đ"
            },
            "explanations": {
                "a": "ĐÚNG: Phản ứng của alkylamine bậc I: C₂H₅NH₂ + HNO₂ → C₂H₅OH + N₂↑ + H₂O. Khí nitrogen thoát ra dưới dạng bọt khí không màu.",
                "b": "ĐÚNG: Aniline phản ứng với HNO₂ ở nhiệt độ 0 - 5°C tạo muối phenyldiazonium chloride: C₆H₅NH₂ + HNO₂ + HCl → [C₆H₅N₂⁺]Cl⁻ + 2H₂O.",
                "c": "SAI: Muối diazonium rất kém bền nhiệt; ở nhiệt độ phòng hoặc đun nóng, muối bị thủy phân nhanh chóng giải phóng phenol và khí nitrogen: [C₆H₅N₂⁺]Cl⁻ + H₂O → C₆H₅OH + N₂↑ + HCl, không tạo được phẩm màu Y.",
                "d": "ĐÚNG: Phản ứng ghép đôi diazo giữa cation phenyldiazonium với phenol/phenolate tạo hợp chất azo có hệ liên kết đôi liên hợp dài, tạo màu đỏ cam đặc trưng dùng làm phẩm nhuộm azo."
            }
        },
        {
            "id": 4,
            "title": "Tác dụng của alkylamine với dung dịch muối ion kim loại",
            "context": "Chuẩn bị hai ống nghiệm (A) và (B):\n- Ống nghiệm (A): Chứa 2 mL dung dịch copper(II) sulfate (CuSO₄) 0,1 M.\n- Ống nghiệm (B): Chứa 2 mL dung dịch iron(III) chloride (FeCl₃) 0,1 M.\nTiến hành nhỏ từ từ từng giọt dung dịch methylamine (CH₃NH₂) 1 M vào cả hai ống nghiệm cho đến dư. Xét tính đúng/sai của các phát biểu sau:",
            "statements": {
                "a": "Ở ống nghiệm (B), xuất hiện kết tủa màu nâu đỏ của iron(III) hydroxide do dung dịch methylamine có môi trường kiềm.",
                "b": "Nếu tiếp tục nhỏ dư dung dịch methylamine vào ống nghiệm (B), kết tủa nâu đỏ sẽ tan dần tạo thành dung dịch phức chất màu nâu trong suốt.",
                "c": "Ở ống nghiệm (A), ban đầu xuất hiện kết tủa màu xanh lam của Cu(OH)₂, sau đó khi nhỏ dư methylamine thì kết tủa tan dần tạo dung dịch phức chất có màu xanh lam thẫm.",
                "d": "Nếu thay methylamine bằng aniline và lặp lại thí nghiệm với ống (A), kết tủa Cu(OH)₂ cũng sẽ tan hoàn toàn tạo dung dịch phức chất màu xanh lam thẫm tương tự."
            },
            "answers": {
                "a": "Đ",
                "b": "S",
                "c": "Đ",
                "d": "S"
            },
            "explanations": {
                "a": "ĐÚNG: Methylamine thủy phân tạo môi trường base: 3CH₃NH₂ + 3H₂O + FeCl₃ → Fe(OH)₃↓ (nâu đỏ) + 3CH₃NH₃Cl.",
                "b": "SAI: Fe(OH)₃ không có khả năng tạo phức tan với methylamine, do đó kết tủa màu nâu đỏ không tan khi amine dư.",
                "c": "ĐÚNG: Ban đầu tạo kết tủa Cu(OH)₂ màu xanh lam: 2CH₃NH₂ + 2H₂O + CuSO₄ → Cu(OH)₂↓ + (CH₃NH₃)₂SO₄. Khi methylamine dư, kết tủa tan tạo phức [Cu(CH₃NH₂)₄](OH)₂ màu xanh lam thẫm.",
                "d": "SAI: Aniline có tính base rất yếu và đôi electron tự do trên nguyên tử N bị giải tỏa vào vòng thơm nên không có khả năng tạo phức hòa tan Cu(OH)₂."
            }
        }
    ],
    "part3": [
        {
            "id": 1,
            "question": "Cho 5,9 gam một alkylamine đơn chức, no, mạch hở X tác dụng vừa đủ với 100 mL dung dịch HCl 1,0 M. Phân tử khối của amine X bằng bao nhiêu amu?",
            "answer": "59",
            "explanation": "Số mol HCl đã dùng: n(HCl) = 0,100 × 1,0 = 0,1 mol.\nVì amine X đơn chức nên phản ứng theo tỉ lệ 1 : 1:\nX + HCl → X·HCl\nDo đó: n(X) = n(HCl) = 0,1 mol.\nPhân tử khối của amine X:\nM(X) = 5,9 / 0,1 = 59 (amu).\n(Amine X là C₃H₉N, gồm các đồng phân propan-1-amine, propan-2-amine, N-methylethanamine, trimethylamine)."
        },
        {
            "id": 2,
            "question": "Có bao nhiêu amine đồng phân cấu tạo có cùng công thức phân tử C₄H₁₁N?",
            "answer": "8",
            "explanation": "Các đồng phân cấu tạo của amine C₄H₁₁N gồm:\n- Amine bậc I (4 đồng phân): CH₃CH₂CH₂CH₂NH₂ (butan-1-amine), CH₃CH₂CH(NH₂)CH₃ (butan-2-amine), (CH₃)₂CHCH₂NH₂ (2-methylpropan-1-amine), (CH₃)₃CNH₂ (2-methylpropan-2-amine).\n- Amine bậc II (3 đồng phân): CH₃CH₂CH₂NHCH₃ (N-methylpropan-1-amine), (CH₃)₂CHNHCH₃ (N-methylpropan-2-amine), CH₃CH₂NHCH₂CH₃ (N-ethylethanamine).\n- Amine bậc III (1 đồng phân): (CH₃)₂NCH₂CH₃ (N,N-dimethylethanamine).\nTổng số đồng phân cấu tạo là 4 + 3 + 1 = 8."
        },
        {
            "id": 3,
            "question": "Cho 18,6 gam aniline phản ứng hoàn toàn với lượng dư nước bromine thu được m gam kết tủa trắng 2,4,6-tribromoaniline. Biết hiệu suất của phản ứng đạt 90%. Giá trị của m bằng bao nhiêu gam? (Kết quả làm tròn đến một chữ số thập phân).",
            "answer": "59.4",
            "explanation": "Khối lượng mol của aniline C₆H₅NH₂: M = 93 g/mol.\nSố mol aniline: n(aniline) = 18,6 / 93 = 0,2 mol.\nPhương trình hóa học:\nC₆H₅NH₂ + 3Br₂ → C₆H₂Br₃NH₂↓ + 3HBr\nKhối lượng mol của 2,4,6-tribromoaniline (C₆H₄NBr₃): M = 330 g/mol.\nDo hiệu suất đạt 90%, số mol kết tủa thực tế thu được là:\nn(kết tủa) = 0,2 × 90% = 0,18 mol.\nKhối lượng kết tủa thu được:\nm = 0,18 × 330 = 59,4 gam."
        },
        {
            "id": 4,
            "question": "Cho 9,0 gam ethylamine (C₂H₅NH₂) tác dụng hết với lượng dư dung dịch nitrous acid (HNO₂) ở nhiệt độ phòng. Thể tích khí N₂ thu được ở điều kiện chuẩn (25°C, 1 bar) bằng bao nhiêu lít? (Làm tròn kết quả đến hai chữ số thập phân, biết 1 mol khí ở điều kiện chuẩn chiếm thể tích 24,79 L).",
            "answer": "4.96",
            "explanation": "Khối lượng mol của ethylamine C₂H₅NH₂: M = 45 g/mol.\nSố mol ethylamine: n = 9,0 / 45 = 0,2 mol.\nPhương trình hóa học:\nC₂H₅NH₂ + HNO₂ → C₂H₅OH + N₂↑ + H₂O\nTheo phương trình: n(N₂) = n(ethylamine) = 0,2 mol.\nThể tích khí N₂ ở điều kiện chuẩn (25°C, 1 bar):\nV(N₂) = 0,2 × 24,79 = 4,958 ≈ 4,96 lít."
        },
        {
            "id": 5,
            "question": "Cho các phát biểu sau về hợp chất amine:\n(1) Methylamine, dimethylamine, trimethylamine và ethylamine là những chất khí ở điều kiện thường, có mùi khai khó chịu.\n(2) Nhiệt độ sôi của ethylamine cao hơn ethanol do amine có khả năng tạo liên kết hydrogen mạnh hơn.\n(3) Dung dịch methylamine phản ứng với dung dịch FeCl₃ tạo kết tủa màu nâu đỏ của Fe(OH)₃.\n(4) Nhỏ nước bromine vào ống nghiệm chứa dung dịch aniline thấy xuất hiện kết tủa màu trắng.\n(5) Aniline làm dung dịch phenolphthalein chuyển sang màu hồng do trong phân tử có nhóm amino mang tính base.\n(6) Hexamethylenediamine (hexane-1,6-diamine) là nguyên liệu chính để sản xuất tơ nylon-6,6.\nTrong 6 phát biểu trên, có bao nhiêu phát biểu ĐÚNG?",
            "answer": "4",
            "explanation": "Các phát biểu ĐÚNG gồm: (1), (3), (4), (6).\n- Phát biểu (2) SAI: Liên kết hydrogen N-H···N yếu hơn O-H···O do độ âm điện N < O, nên nhiệt độ sôi của ethylamine (16,6°C) thấp hơn ethanol (78,3°C).\n- Phát biểu (5) SAI: Aniline có tính base rất yếu nên không làm đổi màu phenolphthalein.\nTổng số phát biểu đúng là 4."
        },
        {
            "id": 6,
            "question": "Tiến hành khử 24,6 gam nitrobenzene (C₆H₅NO₂) bằng bột sắt trong dung dịch hydrochloric acid đặc đun nóng, sau đó kiềm hóa hỗn hợp bằng dung dịch NaOH dư và chưng cất lôi cuốn hơi nước thu được 14,88 gam aniline (C₆H₅NH₂). Hiệu suất của quá trình điều chế trên bằng bao nhiêu phần trăm?",
            "answer": "80",
            "explanation": "Số mol nitrobenzene ban đầu:\nn(C₆H₅NO₂) = 24,6 / 123 = 0,2 mol.\nPhương trình hóa học tổng quát:\nC₆H₅NO₂ + 6[H] (Fe + HCl, t°) → C₆H₅NH₂ + 2H₂O\nTheo lý thuyết (hiệu suất 100%):\nn(aniline lý thuyết) = 0,2 mol → m(aniline lý thuyết) = 0,2 × 93 = 18,6 gam.\nHiệu suất của quá trình điều chế:\nH = (14,88 / 18,6) × 100% = 80%."
        }
    ]
}

# 1. Xuất HTML Interactive Test
html_local = "dau-ra/lop-12/bai-tap/de-on-tap-bai-amine-hoa-hoc-12.html"
html_web = "lop-12/de-on-tap-amine.html"
os.makedirs(os.path.dirname(html_local), exist_ok=True)
os.makedirs(os.path.dirname(html_web), exist_ok=True)

generate_quiz_html(quiz_data, html_local)
generate_quiz_html(quiz_data, html_web)
print(f"Đã tạo file HTML local: {html_local}")
print(f"Đã tạo file HTML web: {html_web}")

# 2. Tạo Markdown
md_lines = [
    "# ĐỀ ÔN TẬP BÀI 8: AMINE",
    "## MÔN HÓA HỌC 12 - BỘ SÁCH KẾT NỐI TRI THỨC VỚI CUỘC SỐNG",
    "### Thời gian làm bài: 50 phút (Không kể thời gian phát đề)",
    "",
    "---",
    "",
    "## PHẦN I. CÂU TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN (4,5 ĐIỂM)",
    "Thí sinh trả lời từ Câu 1 đến Câu 18. Mỗi câu hỏi thí sinh chỉ chọn một phương án. Mỗi câu trả lời đúng thí sinh được 0,25 điểm.",
    ""
]

for q in quiz_data["part1"]:
    md_lines.append(f"Câu {q['id']}: {q['question']}")
    for k, v in q["options"].items():
        md_lines.append(f"{k}. {v}")
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
    md_lines.append(q['context'])
    for k, v in q['statements'].items():
        md_lines.append(f"{k}) {v}")
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
    "| 1 | B | 7 | D | 13 | B |",
    "| 2 | C | 8 | C | 14 | A |",
    "| 3 | A | 9 | A | 15 | B |",
    "| 4 | B | 10 | D | 16 | B |",
    "| 5 | A | 11 | B | 17 | C |",
    "| 6 | C | 12 | A | 18 | A |",
    "",
    "### BẢNG ĐÁP ÁN PHẦN II",
    "| Câu | Lệnh hỏi | Đáp án (Đ/S) | Câu | Lệnh hỏi | Đáp án (Đ/S) |",
    "| :---: | :---: | :---: | :---: | :---: | :---: |",
    "| 1 | a | Đ | 3 | a | Đ |",
    "| 1 | b | Đ | 3 | b | Đ |",
    "| 1 | c | S | 3 | c | S |",
    "| 1 | d | Đ | 3 | d | Đ |",
    "| 2 | a | S | 4 | a | Đ |",
    "| 2 | b | Đ | 4 | b | S |",
    "| 2 | c | Đ | 4 | c | Đ |",
    "| 2 | d | S | 4 | d | S |",
    "",
    "### BẢNG ĐÁP ÁN PHẦN III",
    "| Câu | Lời giải tóm tắt | Đáp số |",
    "| :---: | :--- | :---: |",
    "| 1 | n_HCl = 0,1 mol -> M_X = 5,9 / 0,1 = 59 amu (C₃H₉N) | 59 |",
    "| 2 | 4 bậc I + 3 bậc II + 1 bậc III = 8 đồng phân cấu tạo | 8 |",
    "| 3 | n_aniline = 0,2 mol; H = 90% -> m_kết tủa = 0,18 * 330 = 59,4 gam | 59,4 |",
    "| 4 | n_ethylamine = 0,2 mol -> V_N2 (đkc) = 0,2 * 24,79 = 4,958 ≈ 4,96 lít | 4,96 |",
    "| 5 | Các phát biểu đúng gồm: (1), (3), (4), (6) | 4 |",
    "| 6 | n_nitrobenzene = 0,2 mol -> m_LT = 18,6 g -> H = (14,88 / 18,6) * 100% = 80% | 80 |",
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

md_path = "dau-ra/lop-12/bai-tap/de-on-tap-bai-amine-hoa-hoc-12.md"
os.makedirs(os.path.dirname(md_path), exist_ok=True)
with open(md_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))
print(f"Đã tạo file Markdown: {md_path}")

# 3. Xuất Word DOCX
docx_path = "dau-ra/lop-12/bai-tap/de-on-tap-bai-amine-hoa-hoc-12.docx"
create_styled_document(md_path, docx_path)
print(f"Đã tạo file Word DOCX: {docx_path}")
