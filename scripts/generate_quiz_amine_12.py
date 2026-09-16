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
            "title": "Mùi tanh của cá và ứng dụng trung hòa amine trong đời sống thực tế",
            "context": "Trong quá trình đánh bắt và bảo quản thủy hải sản, các vi sinh vật và enzyme phân giải protein cùng hợp chất chứa nitrogen sinh ra hỗn hợp các amine bay hơi (chủ yếu là trimethylamine (CH₃)₃N, dimethylamine (CH₃)₂NH và methylamine), tạo nên mùi tanh nồng khó chịu đặc trưng. Để loại bỏ mùi tanh khi chế biến món ăn, kinh nghiệm dân gian thường rửa cá với giấm ăn (chứa acetic acid), nước cốt chanh (chứa citric acid) hoặc nấu canh chua với me, khế, cà chua. Dựa vào kiến thức về hợp chất amine, xét tính đúng/sai của các phát biểu sau:",
            "statements": {
                "a": "Mùi tanh đặc trưng của cá ươn sinh ra chủ yếu do các amine bay hơi, trong đó có trimethylamine.",
                "b": "Giấm ăn và nước cốt chanh giúp khử mùi tanh vì các acid này tác dụng với amine tạo thành muối ammonium ion dễ tan trong nước và không còn khả năng bay hơi.",
                "c": "Để khử mùi tanh của cá nhanh và sạch hơn, ta có thể ngâm rửa cá bằng dung dịch xà phòng hoặc nước vôi trong có tính kiềm.",
                "d": "Để trung hòa hoàn toàn 0,018 mol trimethylamine trong một mẻ cá, người ta dùng vừa đủ 20 mL dung dịch giấm ăn. Biết acetic acid trong giấm phản ứng với trimethylamine theo tỉ lệ mol 1 : 1. Nồng độ mol của acetic acid trong dung dịch giấm ăn trên là 0,9 M."
            },
            "answers": {
                "a": "Đ",
                "b": "Đ",
                "c": "S",
                "d": "Đ"
            },
            "explanations": {
                "a": "ĐÚNG: Trimethylamine ((CH₃)₃N) và các alkylamine phân tử nhỏ là thủ phạm chính gây ra mùi tanh khó chịu của cá và hải sản.",
                "b": "ĐÚNG: Amine có tính base tác dụng với acid hữu cơ (acetic acid, citric acid) tạo thành muối ammonium: (CH₃)₃N + CH₃COOH → CH₃COO⁻NH⁺(CH₃)₃. Muối này tan tốt trong nước và không bay hơi nên triệt tiêu mùi tanh.",
                "c": "SAI: Môi trường kiềm (xà phòng, nước vôi) làm chuyển dịch cân bằng giữ amine ở dạng phân tử tự do, càng khiến amine dễ bay hơi gây mùi tanh nồng hơn; đồng thời xà phòng gây độc hại cho thực phẩm.",
                "d": "ĐÚNG: Phương trình phản ứng: (CH₃)₃N + CH₃COOH → CH₃COONH(CH₃)₃. Số mol CH₃COOH = số mol trimethylamine = 0,018 mol. Đổi thể tích: V = 20 mL = 0,02 L. Nồng độ mol của acetic acid: C_M = 0,018 / 0,02 = 0,9 M."
            }
        },
        {
            "id": 2,
            "title": "Kiểm soát và định lượng Aniline trong nước thải dệt nhuộm",
            "context": "Aniline (C₆H₅NH₂) là tiền chất quan trọng để tổng hợp phẩm nhuộm azo, tuy nhiên aniline là chất độc hại cao đối với con người và sinh vật thủy sinh. Nước thải sau công đoạn tổng hợp phẩm nhuộm của một nhà máy thường chứa một lượng nhỏ aniline hòa tan. Để kiểm tra và định lượng nồng độ aniline trong nguồn nước thải, phòng kiểm nghiệm môi trường đã tiến hành các thí nghiệm hóa học sau:\n- Thí nghiệm 1: Lấy mẫu nước thải cho phản ứng với dung dịch hydrochloric acid loãng.\n- Thí nghiệm 2: Lấy một phần mẫu nước thải khác cho tác dụng hoàn toàn với lượng dư nước bromine để làm kết tủa hoàn toàn aniline dưới dạng 2,4,6-tribromoaniline.\nXét tính đúng/sai của các phát biểu sau:",
            "statements": {
                "a": "Ở điều kiện thường, aniline nguyên chất rất ít tan trong nước lạnh và có khối lượng riêng lớn hơn nước nên lắng xuống đáy ống nghiệm.",
                "b": "Trong Thí nghiệm 1, aniline tác dụng với dung dịch HCl tạo thành muối phenylammonium chloride (C₆H₅NH₃Cl) tan tốt trong nước.",
                "c": "Nếu cho tiếp dung dịch NaOH dư vào sản phẩm của Thí nghiệm 1 thì chất lỏng vẫn giữ nguyên trạng thái trong suốt, đồng nhất.",
                "d": "Trong Thí nghiệm 2, lấy 200 mL mẫu nước thải cho tác dụng hoàn toàn với lượng dư nước bromine thu được 0,99 gam kết tủa trắng 2,4,6-tribromoaniline (M = 330 g/mol). Nồng độ của aniline trong mẫu nước thải trên là 1,395 g/L."
            },
            "answers": {
                "a": "Đ",
                "b": "Đ",
                "c": "S",
                "d": "Đ"
            },
            "explanations": {
                "a": "ĐÚNG: Aniline rất ít tan trong nước lạnh và có khối lượng riêng D ≈ 1,02 g/mL > 1 g/mL nên bị tách lớp và chìm xuống đáy.",
                "b": "ĐÚNG: Aniline tác dụng với acid mạnh tạo muối ion tan: C₆H₅NH₂ + HCl → C₆H₅NH₃Cl.",
                "c": "SAI: Khi cho NaOH dư vào, base mạnh NaOH đẩy aniline ra khỏi muối: C₆H₅NH₃Cl + NaOH → C₆H₅NH₂ + NaCl + H₂O. Aniline sinh ra không tan trong nước làm dung dịch vẩn đục và phân lớp trở lại.",
                "d": "ĐÚNG: Phương trình: C₆H₅NH₂ + 3Br₂ → C₆H₂Br₃NH₂↓ + 3HBr. Số mol kết tủa n = 0,99 / 330 = 0,003 mol. Do đó số mol aniline có trong 200 mL nước thải là 0,003 mol. Khối lượng aniline trong 200 mL: m = 0,003 × 93 = 0,279 gam. Nồng độ aniline trong nước thải: C = 0,279 g / 0,2 L = 1,395 g/L."
            }
        },
        {
            "id": 3,
            "title": "Phản ứng của amine với Nitrous acid (HNO₂) và ứng dụng tổng hợp phẩm màu Azo",
            "context": "Nitrous acid (HNO₂) là một acid kém bền, thường được tạo ra trực tiếp trong hỗn hợp phản ứng bằng cách phối trộn sodium nitrite (NaNO₂) với hydrochloric acid (HCl). Phản ứng của amine với nitrous acid phụ thuộc chặt chẽ vào cấu trúc amine và nhiệt độ:\n- Thí nghiệm 1: Cho ethylamine tác dụng với hỗn hợp NaNO₂ và HCl ở nhiệt độ phòng (25°C).\n- Thí nghiệm 2: Cho aniline tác dụng với hỗn hợp NaNO₂ và HCl ở nhiệt độ thấp (0 - 5°C, ngâm trong chậu nước đá) thu được dung dịch chất X. Tiếp tục cho dung dịch X tác dụng với dung dịch phenol trong môi trường kiềm thấy xuất hiện hợp chất màu đỏ cam rực rỡ (chất Y).\nXét tính đúng/sai của các phát biểu sau:",
            "statements": {
                "a": "Ở Thí nghiệm 1, hiện tượng quan sát được là có bọt khí không màu thoát ra liên tục, đó là khí nitrogen (N₂).",
                "b": "Ở Thí nghiệm 2, chất X tạo thành trong dung dịch là muối phenyldiazonium chloride ([C₆H₅N₂⁺]Cl⁻), muối này rất bền vững kể cả khi đun sôi ở 100°C.",
                "c": "Chất màu đỏ cam Y thuộc loại phẩm màu azo (chứa liên kết đôi mang màu -N=N-), được ứng dụng rộng rãi trong công nghiệp nhuộm sợi và in ấn.",
                "d": "Ở Thí nghiệm 1, khi cho 3,6 gam ethylamine (M = 45 g/mol) phản ứng hoàn toàn với lượng dư nitrous acid, thể tích khí N₂ thu được ở điều kiện chuẩn (25°C, 1 bar) là 1,9832 lít."
            },
            "answers": {
                "a": "Đ",
                "b": "S",
                "c": "Đ",
                "d": "Đ"
            },
            "explanations": {
                "a": "ĐÚNG: Alkylamine bậc I phản ứng giải phóng khí nitrogen: C₂H₅NH₂ + HNO₂ → C₂H₅OH + N₂↑ + H₂O.",
                "b": "SAI: Muối phenyldiazonium chloride rất kém bền nhiệt; khi đun nóng nó bị thủy phân nhanh chóng giải phóng khí N₂ và phenol: [C₆H₅N₂⁺]Cl⁻ + H₂O → C₆H₅OH + N₂↑ + HCl, không bền ở 100°C.",
                "c": "ĐÚNG: Phản ứng ghép đôi diazo giữa phenyldiazonium với phenolate tạo thành phẩm màu azo có hệ liên hợp dài, tạo màu đỏ cam đặc trưng.",
                "d": "ĐÚNG: Số mol ethylamine: n = 3,6 / 45 = 0,08 mol. Theo phương trình: n(N₂) = n(ethylamine) = 0,08 mol. Ở điều kiện chuẩn (25°C, 1 bar, 1 mol = 24,79 L): V(N₂) = 0,08 × 24,79 = 1,9832 lít."
            }
        },
        {
            "id": 4,
            "title": "Sản xuất vật liệu Polymer - Tơ Nylon-6,6 từ Hexamethylenediamine",
            "context": "Hexamethylenediamine (hexane-1,6-diamine, công thức H₂N-(CH₂)₆-NH₂) là một diamine công nghiệp quan trọng. Khi cho hexamethylenediamine đồng trùng ngưng với adipic acid (HOOC-(CH₂)₄-COOH) ở điều kiện nhiệt độ và áp suất thích hợp, thu được poly(hexamethylene adipamide) - tức tơ nylon-6,6. Tơ nylon-6,6 có tính dai bền, mềm mại, óng mượt và ít thấm nước, được ứng dụng rộng rãi để dệt vải may mặc cao cấp, bện dây dù, đan lưới đánh cá và sản xuất chỉ khâu phẫu thuật. Xét tính đúng/sai của các phát biểu sau:",
            "statements": {
                "a": "Hexamethylenediamine là amine hai chức bậc I, phân tử chứa hai nhóm amino (-NH₂).",
                "b": "Phản ứng tổng hợp nylon-6,6 thuộc loại phản ứng trùng hợp mở vòng của các monomer mạch vòng.",
                "c": "Vải may mặc dệt từ sợi nylon-6,6 rất bền khi ngâm giặt trong môi trường xà phòng có tính kiềm mạnh hoặc chất tẩy có tính acid mạnh.",
                "d": "Để sản xuất 2,26 tấn polymer nylon-6,6 với hiệu suất của toàn bộ quá trình đạt 80%, khối lượng hexamethylenediamine (M = 116 g/mol) tối thiểu cần dùng trong nhà máy là 1,45 tấn."
            },
            "answers": {
                "a": "Đ",
                "b": "S",
                "c": "S",
                "d": "Đ"
            },
            "explanations": {
                "a": "ĐÚNG: Hexamethylenediamine có công thức cấu tạo H₂N-(CH₂)₆-NH₂, phân tử chứa 2 nhóm -NH₂ liên kết với gốc hydrocarbon no nên là diamine bậc I.",
                "b": "SAI: Phản ứng giữa diamine và dicarboxylic acid tạo polymer đồng thời giải phóng các phân tử H₂O thuộc loại phản ứng đồng trùng ngưng, không phải trùng hợp mở vòng.",
                "c": "SAI: Tơ nylon-6,6 chứa các liên kết amide -CO-NH-, các liên kết này rất dễ bị thủy phân trong môi trường acid hoặc môi trường kiềm, làm mục hỏng sợi vải.",
                "d": "ĐÚNG: Mắt xích của nylon-6,6 là [-NH-(CH₂)₆-NH-CO-(CH₂)₄-CO-] có phân tử khối M = 226 g/mol. Số mol mắt xích nylon-6,6: n = 2,26 × 10⁶ / 226 = 10 000 mol. Theo tỉ lệ phản ứng, số mol hexamethylenediamine lý thuyết cần dùng: n = 10 000 mol → Khối lượng lý thuyết: m_LT = 10 000 × 116 = 1 160 000 gam = 1,16 tấn. Do hiệu suất quá trình đạt 80%, khối lượng thực tế cần dùng là: m_TT = 1,16 / 0,80 = 1,45 tấn."
            }
        }
    ],
    "part3": [
        {
            "id": 1,
            "question": "Cho 5,9 gam một alkylamine đơn chức, no, mạch hở X tác dụng vừa đủ với 100 mL dung dịch HCl 1,0 M. Phân tử khối của amine X bằng bao nhiêu amu?",
            "answer": "59",
            "explanation": "Số mol HCl đã dùng: n(HCl) = 0,100 × 1,0 = 0,1 mol.\nVì amine X đơn chức nên phản ứng với HCl theo tỉ lệ mol 1 : 1:\nX + HCl → X·HCl\nDo đó: n(X) = n(HCl) = 0,1 mol.\nPhân tử khối của amine X:\nM(X) = 5,9 / 0,1 = 59 amu.\n(Amine X có công thức phân tử C₃H₉N)."
        },
        {
            "id": 2,
            "question": "Có bao nhiêu amine đồng phân cấu tạo bậc I có cùng công thức phân tử C₄H₁₁N?",
            "answer": "4",
            "explanation": "Các đồng phân cấu tạo amine bậc I (chứa nhóm -NH₂) có công thức C₄H₁₁N gồm:\n(1) CH₃-CH₂-CH₂-CH₂-NH₂ (butan-1-amine)\n(2) CH₃-CH₂-CH(NH₂)-CH₃ (butan-2-amine)\n(3) (CH₃)₂CH-CH₂-NH₂ (2-methylpropan-1-amine)\n(4) (CH₃)₃C-NH₂ (2-methylpropan-2-amine)\nTổng số đồng phân cấu tạo amine bậc I là 4."
        },
        {
            "id": 3,
            "question": "Cho 9,0 gam ethylamine (C₂H₅NH₂) phản ứng hoàn toàn với lượng dư dung dịch hydrochloric acid (HCl). Sau khi phản ứng kết thúc, cô cạn cẩn thận dung dịch thu được m gam muối khan ethylammonium chloride. Giá trị của m bằng bao nhiêu gam? (Kết quả làm tròn đến một chữ số thập phân).",
            "answer": "16.3",
            "explanation": "Khối lượng mol của ethylamine C₂H₅NH₂: M = 45 g/mol.\nSố mol ethylamine: n = 9,0 / 45 = 0,2 mol.\nPhương trình hóa học:\nC₂H₅NH₂ + HCl → C₂H₅NH₃Cl\nKhối lượng mol của muối C₂H₅NH₃Cl: M = 45 + 36,5 = 81,5 g/mol.\nKhối lượng muối khan thu được:\nm = 0,2 × 81,5 = 16,3 gam."
        },
        {
            "id": 4,
            "question": "Cho 18,6 gam aniline tác dụng hoàn toàn với lượng dư nước bromine trong bình phản ứng, thu được m gam kết tủa trắng 2,4,6-tribromoaniline. Biết hiệu suất của phản ứng đạt 90%. Giá trị của m bằng bao nhiêu gam? (Kết quả làm tròn đến một chữ số thập phân).",
            "answer": "59.4",
            "explanation": "Khối lượng mol của aniline C₆H₅NH₂: M = 93 g/mol.\nSố mol aniline: n(aniline) = 18,6 / 93 = 0,2 mol.\nPhương trình hóa học:\nC₆H₅NH₂ + 3Br₂ → C₆H₂Br₃NH₂↓ + 3HBr\nKhối lượng mol của kết tủa 2,4,6-tribromoaniline: M = 330 g/mol.\nVì hiệu suất đạt 90%, số mol kết tủa thực tế thu được là:\nn(kết tủa) = 0,2 × 90% = 0,18 mol.\nKhối lượng kết tủa thu được:\nm = 0,18 × 330 = 59,4 gam."
        },
        {
            "id": 5,
            "question": "Cho các phát biểu sau về hợp chất amine:\n(1) Methylamine, dimethylamine, trimethylamine và ethylamine là những chất khí ở điều kiện thường, có mùi khai khó chịu.\n(2) Nhiệt độ sôi của ethylamine cao hơn so với ethanol vì amine có phân tử khối gần tương đương.\n(3) Dung dịch methylamine phản ứng với dung dịch FeCl₃ tạo kết tủa màu nâu đỏ của Fe(OH)₃.\n(4) Nhỏ nước bromine vào ống nghiệm chứa dung dịch aniline thấy xuất hiện kết tủa màu trắng.\n(5) Aniline làm dung dịch phenolphthalein chuyển sang màu hồng do trong phân tử có nhóm amino mang tính base.\n(6) Hexamethylenediamine (hexane-1,6-diamine) là nguyên liệu chính để sản xuất tơ nylon-6,6.\nTrong 6 phát biểu trên, có bao nhiêu phát biểu ĐÚNG?",
            "answer": "4",
            "explanation": "Các phát biểu ĐÚNG gồm: (1), (3), (4), (6).\n- Phát biểu (2) SAI vì liên kết hydrogen N-H···N yếu hơn liên kết O-H···O nên ethylamine (sôi ở 16,6°C) có nhiệt độ sôi thấp hơn ethanol (sôi ở 78,3°C).\n- Phát biểu (5) SAI vì aniline có tính base rất yếu do hiệu ứng hút electron của vòng benzene nên không làm đổi màu phenolphthalein.\nTổng số phát biểu đúng là 4."
        },
        {
            "id": 6,
            "question": "Tiến hành khử 24,6 gam nitrobenzene (C₆H₅NO₂, M = 123 g/mol) bằng bột sắt trong dung dịch hydrochloric acid đặc đun nóng, sau đó kiềm hóa hỗn hợp bằng dung dịch NaOH dư và chưng cất lôi cuốn hơi nước thu được 14,88 gam aniline (C₆H₅NH₂, M = 93 g/mol). Hiệu suất của quá trình điều chế trên bằng bao nhiêu phần trăm?",
            "answer": "80",
            "explanation": "Số mol nitrobenzene ban đầu:\nn(C₆H₅NO₂) = 24,6 / 123 = 0,2 mol.\nPhương trình hóa học tổng quát:\nC₆H₅NO₂ + 6[H] (Fe + HCl, t°) → C₆H₅NH₂ + 2H₂O\nTheo lý thuyết (hiệu suất 100%):\nn(aniline LT) = 0,2 mol → m(aniline LT) = 0,2 × 93 = 18,6 gam.\nHiệu suất của quá trình điều chế:\nH = (14,88 / 18,6) × 100% = 80%."
        }
    ]
}

# 1. Xuất HTML Interactive Test
html_local1 = "dau-ra/lop-12/bai-tap/de-on-tap-bai-amine-hoa-hoc-12.html"
html_local2 = "dau-ra/lop-12/bai-tap/de-on-tap-amine-hoa-hoc-12.html"
html_web = "lop-12/de-on-tap-amine.html"
os.makedirs(os.path.dirname(html_local1), exist_ok=True)
os.makedirs(os.path.dirname(html_web), exist_ok=True)

generate_quiz_html(quiz_data, html_local1)
generate_quiz_html(quiz_data, html_local2)
generate_quiz_html(quiz_data, html_web)
print(f"Đã tạo file HTML local: {html_local1} và {html_local2}")
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
    "| 4 | C | 10 | D | 16 | B |",
    "| 5 | A | 11 | B | 17 | A |",
    "| 6 | B | 12 | A | 18 | A |",
    "",
    "### BẢNG ĐÁP ÁN PHẦN II",
    "| Câu | Lệnh hỏi | Đáp án (Đ/S) | Câu | Lệnh hỏi | Đáp án (Đ/S) |",
    "| :---: | :---: | :---: | :---: | :---: | :---: |",
    "| 1 | a | Đ | 3 | a | Đ |",
    "| 1 | b | Đ | 3 | b | S |",
    "| 1 | c | S | 3 | c | Đ |",
    "| 1 | d | Đ | 3 | d | Đ |",
    "| 2 | a | Đ | 4 | a | Đ |",
    "| 2 | b | Đ | 4 | b | S |",
    "| 2 | c | S | 4 | c | S |",
    "| 2 | d | Đ | 4 | d | Đ |",
    "",
    "### BẢNG ĐÁP ÁN PHẦN III",
    "| Câu | Lời giải tóm tắt | Đáp số |",
    "| :---: | :--- | :---: |",
    "| 1 | n_HCl = 0,1 mol -> M_X = 5,9 / 0,1 = 59 amu (C₃H₉N) | 59 |",
    "| 2 | 4 đồng phân amine bậc I: butan-1-amine, butan-2-amine, 2-methylpropan-1-amine, 2-methylpropan-2-amine | 4 |",
    "| 3 | n_amine = 0,2 mol -> m_muối = 0,2 * 81,5 = 16,3 gam | 16.3 |",
    "| 4 | n_aniline = 0,2 mol; H = 90% -> m_kết tủa = 0,18 * 330 = 59,4 gam | 59.4 |",
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

md_path1 = "dau-ra/lop-12/bai-tap/de-on-tap-bai-amine-hoa-hoc-12.md"
md_path2 = "dau-ra/lop-12/bai-tap/de-on-tap-amine-hoa-hoc-12.md"
os.makedirs(os.path.dirname(md_path1), exist_ok=True)
with open(md_path1, 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))
with open(md_path2, 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))
print(f"Đã tạo file Markdown: {md_path1} và {md_path2}")

# 3. Xuất Word DOCX
docx_path1 = "dau-ra/lop-12/bai-tap/de-on-tap-bai-amine-hoa-hoc-12.docx"
docx_path2 = "dau-ra/lop-12/bai-tap/de-on-tap-amine-hoa-hoc-12.docx"
create_styled_document(md_path1, docx_path1)
create_styled_document(md_path2, docx_path2)
print(f"Đã tạo file Word DOCX: {docx_path1} và {docx_path2}")
