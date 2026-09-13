"""
Script: generate_exam_ch3_12.py
Purpose: Generate Chapter 3 Chemistry Grade 12 Exam:
- Part 1: 18 Multiple Choice Questions
- Part 2: 4 True/False Questions (Contextual)
- Part 3: 6 Short Answer Questions (Calculations/Counts)
- NO Part 4 (Essay)
- Output to DOCX and interactive HTML (vatli102.com format)
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
    "title": "ĐỀ ÔN TẬP CHƯƠNG 3: HỢP CHẤT CHỨA NITROGEN",
    "badge": "HÓA HỌC 12 - KẾT NỐI TRI THỨC",
    "duration": 50,
    "grade": 12,
    "part1": [
        {
            "id": 1,
            "question": "Hợp chất nào sau đây thuộc loại amine bậc II?",
            "options": {
                "A": "CH₃-CH₂-NH₂",
                "B": "CH₃-NH-CH₃",
                "C": "(CH₃)₃N",
                "D": "C₆H₅-NH₂"
            },
            "answer": "B",
            "explanation": "Amine bậc II là amine có 2 nguyên tử hydrogen trong phân tử ammonia (NH₃) bị thay thế bởi 2 gốc hydrocarbon. Công thức cấu tạo tổng quát dạng R-NH-R'. Hợp chất CH₃-NH-CH₃ (dimethylamine) là amine bậc II."
        },
        {
            "id": 2,
            "question": "Tên gọi thay thế (theo danh pháp IUPAC) của hợp chất CH₃-CH₂-NH₂ là",
            "options": {
                "A": "ethylamine.",
                "B": "ethanamine.",
                "C": "methylamine.",
                "D": "aminoethane."
            },
            "answer": "B",
            "explanation": "Theo danh pháp thay thế IUPAC, tên của amine mạch hở no đơn chức = tên hydrocarbon no tương ứng (bỏ 'e') + vị trí nhóm amine (nếu có) + 'amine'. Do đó CH₃-CH₂-NH₂ có tên thay thế là ethanamine (ethylamine là tên gốc - chức)."
        },
        {
            "id": 3,
            "question": "Ở điều kiện thường, chất nào sau đây là chất khí, có mùi khai khó chịu và độc?",
            "options": {
                "A": "Aniline.",
                "B": "Methylamine.",
                "C": "Glycine.",
                "D": "Alanine."
            },
            "answer": "B",
            "explanation": "Ở điều kiện thường, methylamine, dimethylamine, trimethylamine và ethylamine là những chất khí, có mùi khai khó chịu, độc và tan nhiều trong nước. Các amine đồng đẳng cao hơn là chất lỏng hoặc rắn."
        },
        {
            "id": 4,
            "question": "Dãy các chất nào sau đây được sắp xếp theo thứ tự tính base tăng dần từ trái sang phải?",
            "options": {
                "A": "C₆H₅NH₂ < NH₃ < CH₃NH₂ < (CH₃)₂NH",
                "B": "NH₃ < C₆H₅NH₂ < CH₃NH₂ < (CH₃)₂NH",
                "C": "C₆H₅NH₂ < CH₃NH₂ < NH₃ < (CH₃)₂NH",
                "D": "(CH₃)₂NH < CH₃NH₂ < NH₃ < C₆H₅NH₂"
            },
            "answer": "A",
            "explanation": "Gốc phenyl (-C₆H₅) hút electron làm giảm mật độ điện tích trên nguyên tử nitrogen, do đó tính base của aniline yếu hơn ammonia. Nhóm alkyl (-CH₃) đẩy electron làm tăng mật độ điện tích trên nguyên tử N, làm tăng tính base. Do đó thứ tự tăng dần là: C₆H₅NH₂ < NH₃ < CH₃NH₂ < (CH₃)₂NH."
        },
        {
            "id": 5,
            "question": "Hiện tượng quan sát được khi nhỏ vài giọt nước bromine vào ống nghiệm chứa dung dịch aniline là",
            "options": {
                "A": "xuất hiện kết tủa màu vàng.",
                "B": "xuất hiện kết tủa màu trắng.",
                "C": "dung dịch chuyển sang màu tím hoa cà.",
                "D": "có bọt khí không màu thoát ra."
            },
            "answer": "B",
            "explanation": "Nhóm -NH₂ hoạt hóa vòng thơm mạnh ở các vị trí ortho và para, aniline phản ứng thế nhanh với nước bromine tạo kết tủa trắng 2,4,6-tribromoaniline."
        },
        {
            "id": 6,
            "question": "Để phân biệt dung dịch ethylamine và aniline ở nhiệt độ phòng, thuốc thử đơn giản nhất có thể dùng là",
            "options": {
                "A": "dung dịch HCl.",
                "B": "giấy quỳ tím.",
                "C": "dung dịch NaOH.",
                "D": "nước cất."
            },
            "answer": "B",
            "explanation": "Dung dịch ethylamine có tính base mạnh hơn ammonia nên làm quỳ tím chuyển sang màu xanh. Aniline có tính base rất yếu nên không làm đổi màu quỳ tím."
        },
        {
            "id": 7,
            "question": "Amino acid là hợp chất hữu cơ tạp chức, trong phân tử chứa đồng thời các nhóm chức nào sau đây?",
            "options": {
                "A": "Nhóm amino (-NH₂) và nhóm hydroxy (-OH).",
                "B": "Nhóm amino (-NH₂) và nhóm carboxyl (-COOH).",
                "C": "Nhóm carbonyl (-CO-) và nhóm carboxyl (-COOH).",
                "D": "Nhóm amino (-NH₂) và nhóm ester (-COO-)."
            },
            "answer": "B",
            "explanation": "Amino acid là loại hợp chất hữu cơ tạp chức mà phân tử chứa đồng thời nhóm amino (-NH₂) có tính base và nhóm carboxyl (-COOH) có tính acid."
        },
        {
            "id": 8,
            "question": "Hợp chất nào sau đây có tên gọi là glycine?",
            "options": {
                "A": "H₂N-CH₂-COOH",
                "B": "CH₃-CH(NH₂)-COOH",
                "C": "H₂N-(CH₂)₄-CH(NH₂)-COOH",
                "D": "HOOC-(CH₂)₂-CH(NH₂)-COOH"
            },
            "answer": "A",
            "explanation": "Glycine là amino acid đơn giản nhất với công thức H₂N-CH₂-COOH (M = 75 amu)."
        },
        {
            "id": 9,
            "question": "Dung dịch chất nào sau đây làm quỳ tím chuyển sang màu hồng đỏ?",
            "options": {
                "A": "Glycine.",
                "B": "Alanine.",
                "C": "Lysine.",
                "D": "Glutamic acid."
            },
            "answer": "D",
            "explanation": "Glutamic acid có 2 nhóm -COOH và 1 nhóm -NH₂, môi trường dung dịch có tính acid (pH < 7) nên làm quỳ tím chuyển sang màu đỏ (hồng). Lysine có 2 nhóm -NH₂ và 1 nhóm -COOH làm quỳ chuyển xanh; Glycine và Alanine có 1 nhóm -NH₂ và 1 nhóm -COOH không làm đổi màu quỳ."
        },
        {
            "id": 10,
            "question": "Chất nào sau đây thể hiện tính chất lưỡng tính?",
            "options": {
                "A": "CH₃NH₂",
                "B": "H₂N-CH₂-COOH",
                "C": "CH₃COOH",
                "D": "C₆H₅OH"
            },
            "answer": "B",
            "explanation": "Glycine (H₂N-CH₂-COOH) chứa cả nhóm base (-NH₂) và nhóm acid (-COOH) nên có tính chất lưỡng tính, tác dụng được với cả acid mạnh và base mạnh."
        },
        {
            "id": 11,
            "question": "Liên kết peptide là liên kết amide được hình thành giữa",
            "options": {
                "A": "nhóm -COOH của một đơn vị α-amino acid với nhóm -NH₂ của một đơn vị α-amino acid khác.",
                "B": "nhóm -NH₂ và nhóm -OH của hai phân tử bất kì.",
                "C": "nhóm -COOH và nhóm -COOH của hai phân tử acid.",
                "D": "nhóm -NH₂ và nhóm -NH₂ của hai phân tử amine."
            },
            "answer": "A",
            "explanation": "Liên kết peptide là liên kết amide (-CO-NH-) giữa nhóm carboxyl (-COOH) của một đơn vị α-amino acid với nhóm amino (-NH₂) của một đơn vị α-amino acid khác."
        },
        {
            "id": 12,
            "question": "Số liên kết peptide có trong một phân tử tripeptide mạch hở là",
            "options": {
                "A": "1.",
                "B": "2.",
                "C": "3.",
                "D": "4."
            },
            "answer": "B",
            "explanation": "Tripeptide được cấu tạo từ 3 gốc α-amino acid liên kết với nhau bằng 2 liên kết peptide."
        },
        {
            "id": 13,
            "question": "Chất nào sau đây KHÔNG cho phản ứng màu biuret với Cu(OH)₂ trong môi trường kiềm?",
            "options": {
                "A": "Lòng trắng trứng (albumin).",
                "B": "Tripeptide Gly-Ala-Val.",
                "C": "Dipeptide Gly-Ala.",
                "D": "Tetrapeptide Ala-Gly-Ala-Val."
            },
            "answer": "C",
            "explanation": "Phản ứng màu biuret chỉ xảy ra với protein hoặc các peptide có từ 2 liên kết peptide trở lên (tripeptide trở lên). Dipeptide chỉ có 1 liên kết peptide nên không cho phản ứng này."
        },
        {
            "id": 14,
            "question": "Hiện tượng lòng trắng trứng bị đông cứng lại khi luộc trong nước sôi được gọi là",
            "options": {
                "A": "sự thủy phân protein.",
                "B": "sự đông tụ protein bởi nhiệt độ.",
                "C": "sự lên men protein.",
                "D": "sự trùng ngưng protein."
            },
            "answer": "B",
            "explanation": "Dưới tác dụng của nhiệt độ, cấu trúc bậc cao của protein bị phá vỡ, các phân tử protein duỗi mạch và kết tụ lại với nhau tạo thành thể rắn đông tụ."
        },
        {
            "id": 15,
            "question": "Khi nhỏ vài giọt dung dịch HNO₃ đặc vào dung dịch lòng trắng trứng rồi đun nóng nhẹ, hiện tượng quan sát được là",
            "options": {
                "A": "xuất hiện kết tủa màu vàng.",
                "B": "dung dịch chuyển sang màu xanh lam.",
                "C": "xuất hiện kết tủa màu tím.",
                "D": "có khí mùi khai thoát ra."
            },
            "answer": "A",
            "explanation": "Đây là phản ứng xanthoproteic đặc trưng: các gốc amino acid chứa vòng thơm trong chuỗi polypeptide của protein bị nitro hóa tạo sản phẩm màu vàng."
        },
        {
            "id": 16,
            "question": "Đặc điểm nào sau đây KHÔNG đúng khi nói về enzyme?",
            "options": {
                "A": "Hầu hết enzyme có bản chất là protein.",
                "B": "Enzyme có tính xúc tác chọn lọc và đặc hiệu rất cao.",
                "C": "Enzyme làm tăng tốc độ phản ứng trong điều kiện êm dịu của cơ thể sống.",
                "D": "Enzyme vẫn duy trì hoạt tính xúc tác tối ưu ở nhiệt độ rất cao trên 150°C."
            },
            "answer": "D",
            "explanation": "Do có bản chất là protein, ở nhiệt độ cao (thường trên 60°C), enzyme bị biến tính và mất hoàn toàn hoạt tính xúc tác sinh học."
        },
        {
            "id": 17,
            "question": "Thủy phân hoàn toàn 1 mol tripeptide Gly-Ala-Val trong dung dịch NaOH dư, đun nóng. Số mol NaOH đã tham gia phản ứng là",
            "options": {
                "A": "1 mol.",
                "B": "2 mol.",
                "C": "3 mol.",
                "D": "4 mol."
            },
            "answer": "C",
            "explanation": "Tripeptide tạo bởi các α-amino acid có 1 nhóm -COOH và 1 nhóm -NH₂: Tripeptide + 3 NaOH → 3 muối + 1 H₂O. Do đó 1 mol tripeptide phản ứng vừa đủ với 3 mol NaOH."
        },
        {
            "id": 18,
            "question": "Chất điều vị được dùng phổ biến trong nấu ăn gia đình và công nghiệp thực phẩm (thường gọi là bột ngọt hoặc mì chính) là muối nào sau đây?",
            "options": {
                "A": "Sodium chloride.",
                "B": "Monosodium glutamate.",
                "C": "Disodium succinate.",
                "D": "Sodium acetate."
            },
            "answer": "B",
            "explanation": "Mì chính (bột ngọt) là muối mononatri của glutamic acid, có tên quốc tế là monosodium glutamate (MSG)."
        }
    ],
    "part2": [
        {
            "id": 1,
            "title": "Mùi tanh của cá và ứng dụng tính chất của amine trong đời sống",
            "context": "Trong đời sống hàng ngày, khi chế biến các món ăn từ cá, người nội trợ thường ngửi thấy mùi tanh khó chịu. Mùi tanh này sinh ra chủ yếu do các amine bay hơi (đặc biệt là trimethylamine và dimethylamine) được tạo thành trong quá trình chuyển hóa chất của cá sau khi đánh bắt. Để loại bỏ mùi tanh, kinh nghiệm dân gian thường rửa cá với nước vo gạo, giấm ăn hoặc nước cốt chanh, hoặc nấu canh chua với quả me, cà chua. Dựa vào kiến thức về hợp chất amine, xét tính đúng/sai của các phát biểu sau:",
            "statements": {
                "a": "Mùi tanh của cá chủ yếu do các hợp chất amine bay hơi gây ra, tiêu biểu là trimethylamine (CH₃)₃N.",
                "b": "Giấm ăn (chứa acetic acid) và nước cốt chanh (chứa citric acid) giúp khử mùi tanh vì các acid này trung hòa amine tạo muối ion không bay hơi, dễ tan trong nước.",
                "c": "Nếu rửa cá bằng dung dịch xà phòng hoặc dung dịch có tính kiềm nhẹ sẽ loại bỏ mùi tanh hiệu quả hơn giấm ăn.",
                "d": "Dung dịch methylamine và dung dịch aniline đều làm quỳ tím ẩm chuyển sang màu xanh rõ rệt ở nhiệt độ phòng."
            },
            "answers": {
                "a": "Đ",
                "b": "Đ",
                "c": "S",
                "d": "S"
            },
            "explanations": {
                "a": "ĐÚNG: Trimethylamine và các amine bậc thấp bay hơi là tác nhân chính gây ra mùi tanh của thủy hải sản.",
                "b": "ĐÚNG: Phản ứng trung hòa tạo muối ammonium tan trong nước và không còn khả năng bay hơi, triệt tiêu mùi tanh.",
                "c": "SAI: Môi trường kiềm chuyển amine về dạng phân tử tự do làm tăng lượng bay hơi, gây mùi nồng hơn và xà phòng gây độc thực phẩm.",
                "d": "SAI: Methylamine làm quỳ tím chuyển xanh, còn aniline có tính base rất yếu do hiệu ứng hút e của vòng benzene nên không đổi màu quỳ tím."
            }
        },
        {
            "id": 2,
            "title": "Khảo sát tính chất hóa học đặc trưng của aniline",
            "context": "Tiến hành thí nghiệm khảo sát tính chất của aniline theo các bước sau:\n- Bước 1: Cho khoảng 2 mL nước cất vào ống nghiệm, sau đó nhỏ tiếp vài giọt aniline vào, lắc nhẹ rồi để yên.\n- Bước 2: Chia hỗn hợp ở Bước 1 vào hai ống nghiệm (1) và (2).\n  + Ở ống nghiệm (1): Nhỏ từ từ từng giọt dung dịch HCl loãng vào, lắc đều.\n  + Ở ống nghiệm (2): Nhỏ từ từ từng giọt nước bromine vào, lắc nhẹ.\n- Bước 3: Cho tiếp dung dịch NaOH dư vào ống nghiệm (1), lắc đều.\nXét tính đúng/sai của các phát biểu sau:",
            "statements": {
                "a": "Ở Bước 1, aniline tan hoàn toàn trong nước cất tạo thành dung dịch trong suốt, đồng nhất.",
                "b": "Ở Bước 2, chất lỏng trong ống nghiệm (1) trở nên đồng nhất, trong suốt do aniline đã phản ứng với HCl tạo muối phenylammonium chloride tan tốt trong nước.",
                "c": "Ở Bước 2, trong ống nghiệm (2) xuất hiện kết tủa màu trắng của hợp chất 2,4,6-tribromoaniline.",
                "d": "Ở Bước 3, khi thêm dung dịch NaOH dư vào ống nghiệm (1), chất lỏng trong ống nghiệm vẫn giữ nguyên trạng thái trong suốt."
            },
            "answers": {
                "a": "S",
                "b": "Đ",
                "c": "Đ",
                "d": "S"
            },
            "explanations": {
                "a": "SAI: Aniline rất ít tan trong nước lạnh, chìm xuống đáy tạo lớp chất lỏng phân lớp vẩn đục.",
                "b": "ĐÚNG: Phản ứng tạo muối C₆H₅NH₃Cl là hợp chất ion tan tốt trong nước nên chất lỏng chuyển sang trong suốt.",
                "c": "ĐÚNG: Aniline phản ứng thế dễ dàng với nước bromine tạo kết tủa trắng 2,4,6-tribromoaniline.",
                "d": "SAI: NaOH trung hòa muối giải phóng lại aniline: C₆H₅NH₃Cl + NaOH → C₆H₅NH₂ + NaCl + H₂O. Aniline ít tan làm dung dịch vẩn đục trở lại."
            }
        },
        {
            "id": 3,
            "title": "Hiện tượng điện di phân tách amino acid và ứng dụng của monosodium glutamate",
            "context": "Amino acid là các chất có tính lưỡng tính. Trong dung dịch nước, tùy thuộc vào pH của môi trường mà amino acid có thể tồn tại ở dạng cation (mang điện tích dương), anion (mang điện tích âm) hoặc ion lưỡng cực (trung hòa về điện). Phương pháp điện di được dùng để tách các amino acid dựa trên sự di chuyển của chúng trong điện trường ở một giá trị pH xác định.\nCho hỗn hợp gồm ba amino acid: Glutamic acid (Glu, pI ≈ 3,2), Alanine (Ala, pI ≈ 6,0) và Lysine (Lys, pI ≈ 9,7). Tiến hành điện di hỗn hợp này trong dung dịch đệm có pH = 6,0. Xét tính đúng/sai của các nhận định sau:",
            "statements": {
                "a": "Monosodium glutamate (mì chính/bột ngọt) là muối mononatri của glutamic acid, kích thích vị giác tạo vị umami (ngọt thịt).",
                "b": "Ở pH = 6,0, Alanine hầu như không di chuyển về cực nào của điện trường vì phân tử tồn tại chủ yếu ở dạng ion lưỡng cực trung hòa điện tích (pH = pI).",
                "c": "Ở pH = 6,0, Glutamic acid tích điện dương tổng cộng nên sẽ di chuyển về phía cực âm (cathode).",
                "d": "Ở pH = 6,0, phân tử Lysine tích điện dương tổng cộng (do chứa hai nhóm amino) nên sẽ di chuyển về phía cực âm (cathode)."
            },
            "answers": {
                "a": "Đ",
                "b": "Đ",
                "c": "S",
                "d": "Đ"
            },
            "explanations": {
                "a": "ĐÚNG: MSG kích hoạt thụ thể umami ở gai lưỡi tạo cảm giác ngon miệng.",
                "b": "ĐÚNG: Tại pH = pI = 6,0, phân tử Alanine trung hòa về điện nên đứng yên trong điện trường.",
                "c": "SAI: Tại pH = 6,0 > pI = 3,2, các nhóm carboxyl phân li tạo ion âm, Glu tích điện âm nên phải di chuyển về cực DƯƠNG (anode).",
                "d": "ĐÚNG: Tại pH = 6,0 < pI = 9,7, các nhóm amino nhận proton tạo ion dương, Lys tích điện dương nên di chuyển về cực ÂM (cathode)."
            }
        },
        {
            "id": 4,
            "title": "Hiện tượng đông tụ protein và ứng dụng trong công nghệ chế biến thực phẩm",
            "context": "Protein là thành phần thiết yếu cấu tạo nên tế bào sinh vật. Trong công nghệ chế biến thực phẩm và đời sống, hiện tượng biến tính và đông tụ protein được ứng dụng rộng rãi: nấu canh riêu cua, làm đậu phụ từ sữa đậu nành, sản xuất phô mai, sữa chua. Ngoài ra, các phản ứng màu đặc trưng cũng được dùng để kiểm nghiệm chất lượng protein trong mẫu thử thực phẩm. Xét tính đúng/sai của các nhận định sau:",
            "statements": {
                "a": "Khi nấu canh cua, các mảng gạch cua nổi lên bề mặt nước dùng là do protein trong thịt cua bị đông tụ dưới tác dụng của nhiệt độ.",
                "b": "Trong quy trình làm đậu phụ, người ta thêm nước chua (acid hữu cơ) hoặc thạch cao (CaSO₄) vào sữa đậu nành nóng nhằm làm đông tụ khối protein đậu nành.",
                "c": "Có thể sử dụng phản ứng màu biuret để phân biệt dung dịch lòng trắng trứng (albumin) với dung dịch dipeptide Gly-Ala.",
                "d": "Khi nhỏ vài giọt dung dịch nitric acid đặc vào dung dịch lòng trắng trứng rồi đun nóng nhẹ, xuất hiện kết tủa màu tím hoa cà đặc trưng."
            },
            "answers": {
                "a": "Đ",
                "b": "Đ",
                "c": "Đ",
                "d": "S"
            },
            "explanations": {
                "a": "ĐÚNG: Protein thịt cua tan trong nước lạnh nhưng khi đun sôi thì bị đông tụ và nổi lên thành mảng riêu cua.",
                "b": "ĐÚNG: Acid và ion Ca²⁺ làm trung hòa điện tích bề mặt phân tử protein, làm giảm độ hòa tan và kết tụ thành óc đậu (đậu phụ).",
                "c": "ĐÚNG: Albumin là protein cho màu tím biuret với Cu(OH)₂ trong kiềm, còn dipeptide Gly-Ala không cho phản ứng này.",
                "d": "SAI: Phản ứng với HNO₃ đặc tạo kết tủa màu VÀNG (phản ứng xanthoproteic), không phải màu tím."
            }
        }
    ],
    "part3": [
        {
            "id": 1,
            "question": "Cho 4,5 gam một amine đơn chức, no, mạch hở X tác dụng vừa đủ với 100 mL dung dịch HCl 1,0 M. Phân tử khối của amine X bằng bao nhiêu amu?",
            "answer": "45",
            "explanation": "Số mol HCl: n(HCl) = 0,1 × 1,0 = 0,1 mol.\nVì X là amine đơn chức nên n(X) = n(HCl) = 0,1 mol.\nPhân tử khối của amine X: M(X) = 4,5 / 0,1 = 45 (amu).\nCông thức phân tử của X là C₂H₇N (ethylamin hoặc dimethylamin)."
        },
        {
            "id": 2,
            "question": "Có bao nhiêu amine đồng phân cấu tạo có cùng công thức phân tử C₃H₉N?",
            "answer": "4",
            "explanation": "Các đồng phân cấu tạo của C₃H₉N gồm:\n- Amine bậc I (2 chất): CH₃-CH₂-CH₂-NH₂ và CH₃-CH(NH₂)-CH₃.\n- Amine bậc II (1 chất): CH₃-CH₂-NH-CH₃.\n- Amine bậc III (1 chất): (CH₃)₃N.\nTổng số đồng phân cấu tạo là 4."
        },
        {
            "id": 3,
            "question": "Cho 7,5 gam glycine (H₂N-CH₂-COOH) phản ứng hoàn toàn với lượng dư dung dịch NaOH. Cô cạn cẩn thận dung dịch sau phản ứng thu được m gam muối khan. Giá trị của m bằng bao nhiêu gam?",
            "answer": "9.7",
            "explanation": "Số mol glycine: n(Gly) = 7,5 / 75 = 0,1 mol.\nPhương trình hóa học: H₂N-CH₂-COOH + NaOH → H₂N-CH₂-COONa + H₂O.\nMuối khan thu được là H₂N-CH₂-COONa (M = 97 g/mol).\nKhối lượng muối khan: m = 0,1 × 97 = 9,7 gam."
        },
        {
            "id": 4,
            "question": "Thủy phân hoàn toàn 1 mol hexapeptide mạch hở X tạo nên từ các α-amino acid. Phân tử hexapeptide X có chứa bao nhiêu liên kết peptide?",
            "answer": "5",
            "explanation": "Hexapeptide mạch hở được cấu tạo từ 6 gốc α-amino acid.\nSố liên kết peptide trong chuỗi peptide mạch hở gồm n gốc là (n - 1).\nDo đó số liên kết peptide = 6 - 1 = 5."
        },
        {
            "id": 5,
            "question": "Cho các phát biểu sau đây về hợp chất chứa nitrogen:\n(1) Ở điều kiện thường, methylamine và ethylamine là các chất khí có mùi khai, tan nhiều trong nước.\n(2) Aniline tác dụng với dung dịch nitrous acid (HNO₂) ở nhiệt độ phòng giải phóng khí nitrogen (N₂).\n(3) Amino acid là chất rắn kết tinh, dễ tan trong nước và có nhiệt độ nóng chảy cao do tồn tại ở dạng ion lưỡng cực.\n(4) Tất cả các peptide khi cho tác dụng với Cu(OH)₂ trong môi trường kiềm đều xuất hiện màu tím đặc trưng.\n(5) Hiện tượng nấu riêu cua bị đông tụ thành mảng là do sự đông tụ của protein dưới tác dụng của nhiệt độ.\nTrong 5 phát biểu trên, có bao nhiêu phát biểu ĐÚNG?",
            "answer": "3",
            "explanation": "Các phát biểu ĐÚNG là: (1), (3), (5).\n- Phát biểu (2) SAI: Aniline phản ứng với HNO₂ ở nhiệt độ thấp (0 - 5°C) tạo muối diazonium, không giải phóng N₂.\n- Phát biểu (4) SAI: Dipeptide chỉ có 1 liên kết peptide nên không cho phản ứng màu biuret.\nVậy có 3 phát biểu đúng."
        },
        {
            "id": 6,
            "question": "Cho 9,3 gam aniline phản ứng hoàn toàn với lượng dư nước bromine thu được m gam kết tủa trắng 2,4,6-tribromoaniline. Biết hiệu suất phản ứng đạt 100%. Giá trị của m bằng bao nhiêu gam?",
            "answer": "33",
            "explanation": "Số mol aniline: n(aniline) = 9,3 / 93 = 0,1 mol.\nPhương trình hóa học: C₆H₅NH₂ + 3Br₂ → C₆H₂Br₃NH₂↓ + 3HBr.\nKhối lượng mol của 2,4,6-tribromoaniline: M = 330 g/mol.\nKhối lượng kết tủa: m = 0,1 × 330 = 33 gam."
        }
    ]
}

# 1. Xuất file HTML (cả thư mục máy tính dau-ra và thư mục web rút gọn lop-12)
html_local = "dau-ra/lop-12/de-kiem-tra/de-on-tap-chuong-3-hoa-hoc-12.html"
html_web = "lop-12/de-on-tap-chuong-3-so-1.html"
generate_quiz_html(quiz_data, html_local)
generate_quiz_html(quiz_data, html_web)

# 2. Tạo Markdown
md_lines = [
    "# ĐỀ ÔN TẬP CHƯƠNG 3: HỢP CHẤT CHỨA NITROGEN",
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
    "| 1 | B | 7 | B | 13 | C |",
    "| 2 | B | 8 | A | 14 | B |",
    "| 3 | B | 9 | D | 15 | A |",
    "| 4 | A | 10 | B | 16 | D |",
    "| 5 | B | 11 | A | 17 | C |",
    "| 6 | B | 12 | B | 18 | B |",
    "",
    "### BẢNG ĐÁP ÁN PHẦN II",
    "| Câu | Lệnh hỏi | Đáp án (Đ/S) | Câu | Lệnh hỏi | Đáp án (Đ/S) |",
    "| :---: | :---: | :---: | :---: | :---: | :---: |",
    "| 1 | a | Đ | 3 | a | Đ |",
    "| 1 | b | Đ | 3 | b | Đ |",
    "| 1 | c | S | 3 | c | S |",
    "| 1 | d | S | 3 | d | Đ |",
    "| 2 | a | S | 4 | a | Đ |",
    "| 2 | b | Đ | 4 | b | Đ |",
    "| 2 | c | Đ | 4 | c | Đ |",
    "| 2 | d | S | 4 | d | S |",
    "",
    "### BẢNG ĐÁP ÁN PHẦN III",
    "| Câu | Lời giải tóm tắt | Đáp số |",
    "| :---: | :--- | :---: |",
    "| 1 | n_HCl = 0,1 mol -> M_X = 4,5 / 0,1 = 45 amu | 45 |",
    "| 2 | 2 bậc I + 1 bậc II + 1 bậc III = 4 đồng phân | 4 |",
    "| 3 | n_Gly = 0,1 mol -> m_muối = 0,1 * 97 = 9,7 gam | 9,7 |",
    "| 4 | Hexapeptide có 6 gốc -> số liên kết peptide = 6 - 1 = 5 | 5 |",
    "| 5 | Các phát biểu đúng gồm: (1), (3), (5) | 3 |",
    "| 6 | n_aniline = 0,1 mol -> m_kết tủa = 0,1 * 330 = 33 gam | 33 |",
    ""
])

md_path = "dau-ra/lop-12/de-kiem-tra/de-on-tap-chuong-3-hoa-hoc-12.md"
os.makedirs(os.path.dirname(md_path), exist_ok=True)
with open(md_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))
print(f"Đã tạo file Markdown: {md_path}")

# 3. Xuất Word DOCX
docx_path = "dau-ra/lop-12/de-kiem-tra/de-on-tap-chuong-3-hoa-hoc-12.docx"
create_styled_document(md_path, docx_path)
print(f"Đã tạo file Word DOCX: {docx_path}")
