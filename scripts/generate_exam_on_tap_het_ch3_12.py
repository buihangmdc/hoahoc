"""
Script: generate_exam_on_tap_het_ch3_12.py
Purpose: Chuyển đổi và tạo bộ Đề ôn tập tới hết Chương 3 - Hóa học 12 chuẩn quy cách:
- Phần 1: 18 câu trắc nghiệm nhiều lựa chọn
- Phần 2: 4 câu trắc nghiệm Đúng / Sai (bối cảnh thực tế & thí nghiệm)
- Phần 3: 6 câu trắc nghiệm trả lời ngắn (tính toán / đếm số phát biểu)
- Không có phần tự luận (chuẩn Lớp 12 Bộ GD&ĐT)
- Xuất 01 file Markdown (.md)
- Xuất 01 file Word (.docx) chuẩn A4, lề chuẩn, không gạch đầu dòng đáp án, có ảnh minh họa
- Xuất 01 file Web (.html) chuẩn vatli102, MathJax, đếm ngược 50p, chấm điểm tự động, lời giải chi tiết, đồng bộ Google Sheet
"""

import os
import sys
import base64
import json
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath("."))

from scripts.export_to_docx import create_styled_document
from scripts.export_to_html_quiz import generate_quiz_html

# Đọc và mã hóa Base64 các hình ảnh
IMAGE_DIR = os.path.join("dau-ra", "lop-12", "de-kiem-tra", "images")

def get_base64_img(filename):
    path = os.path.join(IMAGE_DIR, filename)
    if not os.path.exists(path):
        return ""
    mime = "image/jpeg" if filename.endswith(('.jpg', '.jpeg')) else "image/png"
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode('utf-8')
    return f"data:{mime};base64,{data}"

b64_ethyl = get_base64_img("ethyl_acetate_experiment.jpg")
b64_lactose = get_base64_img("lactose_structure.png")
b64_lys_glu = get_base64_img("lys_glu_structure.jpg")
b64_linoleic = get_base64_img("linoleic_acid_structure.png")

quiz_data = {
    "title": "ĐỀ ÔN TẬP TỚI HẾT CHƯƠNG 3 - MÔN HÓA HỌC 12",
    "badge": "HÓA HỌC 12 - CHUẨN THI TỐT NGHIỆP THPT",
    "duration": 50,
    "grade": 12,
    "google_sheet_url": "https://script.google.com/macros/s/AKfycbwRRiM81mghvA7cInvJgb4rPLzWOAE3s44wer0BJcURQ4hWwoykS19pkNQ9LyzH6Q8lTQ/exec",
    "part1": [
        {
            "id": 1,
            "question": "Carbohydrate nào sau đây là polysaccharide?",
            "options": {
                "A": "Fructose.",
                "B": "Cellulose.",
                "C": "Saccharose.",
                "D": "Glucose."
            },
            "answer": "B",
            "explanation": "Polysaccharide là polymer carbohydrate phức tạp gồm nhiều gốc monosaccharide liên kết với nhau, tiêu biểu là tinh bột và cellulose. Fructose và glucose là monosaccharide; saccharose là disaccharide."
        },
        {
            "id": 2,
            "question": "Nguyên tử nguyên tố $X^{2+}$ có cấu hình electron: $1s^2 2s^2 2p^6$. $X$ thuộc nhóm mấy trong bảng tuần hoàn các nguyên tố hóa học?",
            "options": {
                "A": "IIA.",
                "B": "VIA.",
                "C": "IA.",
                "D": "VIIIA."
            },
            "answer": "A",
            "explanation": "Nguyên tử X nhường 2 electron để tạo thành cation $X^{2+}$. Do đó, số electron của nguyên tử X = 10 + 2 = 12 (bằng số hiệu nguyên tử Z = 12). Cấu hình electron nguyên tử X là $1s^2 2s^2 2p^6 3s^2$ (Magnesium). Vì có 2 electron hóa trị ở phân lớp s nên X thuộc nhóm IIA, chu kì 3."
        },
        {
            "id": 3,
            "question": "Cho hexapeptide X: Gly-Ala-Gly-Val-Ala-Gly. Số liên kết peptide có trong phân tử X là",
            "options": {
                "A": "5.",
                "B": "3.",
                "C": "4.",
                "D": "6."
            },
            "answer": "A",
            "explanation": "Phân tử peptide mạch hở được tạo thành từ n gốc $\\alpha$-amino acid sẽ chứa (n - 1) liên kết peptide. Hexapeptide X được tạo từ 6 gốc $\\alpha$-amino acid nên số liên kết peptide = 6 - 1 = 5."
        },
        {
            "id": 4,
            "question": "Carbohydrate nào sau đây kém tan trong nước lạnh nhưng tan được trong nước nóng tạo dung dịch keo, nhớt?",
            "options": {
                "A": "Tinh bột.",
                "B": "Glucose.",
                "C": "Saccharose.",
                "D": "Cellulose."
            },
            "answer": "A",
            "explanation": "Tinh bột hầu như không tan trong nước lạnh. Khi ngâm vào nước nóng (từ 65°C trở lên), các hạt tinh bột ngậm nước, trương phồng và vỡ ra tạo thành dung dịch keo nhớt gọi là hồ tinh bột. Glucose và saccharose tan rất tốt trong nước lạnh; cellulose không tan trong cả nước lạnh và nước nóng."
        },
        {
            "id": 5,
            "question": "Nhỏ vài giọt nước bromine vào ống nghiệm chứa 2 mL dung dịch chất X, thu được kết tủa trắng. Chất X là",
            "options": {
                "A": "Aniline.",
                "B": "Dimethylamine.",
                "C": "Ethylamine.",
                "D": "Methylamine."
            },
            "answer": "A",
            "explanation": "Do ảnh hưởng của nhóm amino ($-NH_2$) đẩy electron vào vòng thơm, các vị trí ortho và para được hoạt hóa mạnh, aniline ($C_6H_5NH_2$) tác dụng ngay với nước bromine ở điều kiện thường tạo kết tủa trắng 2,4,6-tribromoaniline. Các aliphatic amine không có phản ứng tạo kết tủa trắng này."
        },
        {
            "id": 6,
            "question": "Phát biểu nào sau đây KHÔNG đúng?",
            "options": {
                "A": "Protein đơn giản có chứa thành phần phi protein.",
                "B": "Protein trong thức ăn giúp bổ sung các amino acid thiết yếu cho cơ thể.",
                "C": "Polypeptide có phản ứng màu biuret với $\\text{Cu(OH)}_2$ trong môi trường kiềm.",
                "D": "Amino acid là hợp chất hữu cơ tạp chức."
            },
            "answer": "A",
            "explanation": "Phát biểu A không đúng vì protein đơn giản là loại protein khi thủy phân hoàn toàn chỉ tạo ra hỗn hợp các $\\alpha$-amino acid (không chứa thành phần phi protein). Protein phức tạp mới là loại protein được tạo từ protein đơn giản liên kết với nhóm phi protein (như nucleic acid, lipid, carbohydrate,...)."
        },
        {
            "id": 7,
            "question": "Hiện tượng phú dưỡng là một biểu hiện của môi trường ao, hồ bị ô nhiễm do dư thừa các chất dinh dưỡng. Sự dư thừa dinh dưỡng chủ yếu do hàm lượng các ion nào sau đây vượt quá mức cho phép?",
            "options": {
                "A": "Chloride, sulfate.",
                "B": "Calcium, magnesium.",
                "C": "Nitrate, phosphate.",
                "D": "Sodium, potassium."
            },
            "answer": "C",
            "explanation": "Hiện tượng phú dưỡng xảy ra khi nguồn nước bị dư thừa các chất dinh dưỡng khoáng, chủ yếu do hàm lượng các ion nitrate ($NO_3^-$) và phosphate ($PO_4^{3-}$) vượt quá ngưỡng cho phép (từ phân bón nông nghiệp, chất tẩy rửa, nước thải), làm cho các loài tảo và thực vật phù du bùng nổ, gây suy giảm dưỡng khí oxy hòa tan."
        },
        {
            "id": 8,
            "question": "Phát biểu nào sau đây KHÔNG đúng?",
            "options": {
                "A": "Mỡ động vật, dầu thực vật có thể được dùng làm nguyên liệu để sản xuất xà phòng.",
                "B": "Một số ester có mùi thơm nên được dùng làm chất tạo hương trong công nghiệp thực phẩm và mĩ phẩm.",
                "C": "Chất béo là triester của glycerol và acid béo.",
                "D": "Phản ứng thủy phân ester trong môi trường acid còn gọi là phản ứng xà phòng hóa."
            },
            "answer": "D",
            "explanation": "Phát biểu D không đúng vì phản ứng thủy phân ester trong môi trường kiềm (dung dịch NaOH, KOH) đun nóng mới được gọi là phản ứng xà phòng hóa. Phản ứng thủy phân ester trong môi trường acid là phản ứng thuận nghịch."
        },
        {
            "id": 9,
            "question": "Phương pháp kết tinh dùng để tách các chất",
            "options": {
                "A": "có khối lượng riêng khác nhau.",
                "B": "có nguyên tử khối khác nhau.",
                "C": "có nhiệt độ sôi khác nhau.",
                "D": "có độ tan khác nhau."
            },
            "answer": "D",
            "explanation": "Phương pháp kết tinh dùng để tách và tinh chế các chất rắn dựa trên sự khác nhau về độ tan của các chất trong một dung môi xác định hoặc sự thay đổi độ tan theo nhiệt độ."
        },
        {
            "id": 10,
            "question": "Chất làm mất màu dung dịch bromine ở điều kiện thường là",
            "options": {
                "A": "$\\text{CH}_2=\\text{CH}_2$.",
                "B": "$\\text{CH}_3-\\text{CH}_2-\\text{CH}_3$.",
                "C": "$\\text{CH}_3-\\text{CH}_3$.",
                "D": "$\\text{CH}_4$."
            },
            "answer": "A",
            "explanation": "Ethylene ($\\text{CH}_2=\\text{CH}_2$) là alkene có liên kết đôi $C=C$, dễ dàng tham gia phản ứng cộng làm mất màu nâu đỏ của dung dịch bromine ở điều kiện thường: $\\text{CH}_2=\\text{CH}_2 + Br_2 \\rightarrow \\text{CH}_2Br-\\text{CH}_2Br$. Các alkane no không phản ứng với nước bromine ở điều kiện thường."
        },
        {
            "id": 11,
            "question": "Nhiều vụ ngộ độc rượu nghiêm trọng do sử dụng rượu được pha chế từ cồn công nghiệp có lẫn methanol. Công thức phân tử của methanol là",
            "options": {
                "A": "$\\text{C}_3\\text{H}_7\\text{OH}$.",
                "B": "$\\text{C}_2\\text{H}_5\\text{OH}$.",
                "C": "$\\text{CH}_3\\text{OH}$.",
                "D": "$\\text{C}_2\\text{H}_4(\\text{OH})_2$."
            },
            "answer": "C",
            "explanation": "Methanol có công thức phân tử là $\\text{CH}_3\\text{OH}$. Đây là một alcohol rất độc, khi vào cơ thể bị enzyme gan chuyển hóa thành formaldehyde và formic acid gây tổn thương dây thần kinh thị giác dẫn đến mù lòa và toan chuyển hóa gây tử vong."
        },
        {
            "id": 12,
            "question": "Phương trình nhiệt hóa học giữa nitrogen và oxygen như sau:$$\\text{N}_2(g) + \\text{O}_2(g) \\xrightarrow{t^\\circ} 2\\text{NO}(g) \\quad \\Delta_r H^\\circ_{298} = +180\\text{ kJ/mol}$$Kết luận nào sau đây đúng?",
            "options": {
                "A": "Phản ứng xảy ra thuận lợi ở điều kiện thường.",
                "B": "Phản ứng hoá học xảy ra có sự giải phóng năng lượng dưới dạng nhiệt.",
                "C": "Nitrogen và oxygen phản ứng mạnh hơn khi ở nhiệt độ thấp.",
                "D": "Phản ứng hóa học xảy ra có sự hấp thụ nhiệt năng từ môi trường."
            },
            "answer": "D",
            "explanation": "Biến thiên enthalpy chuẩn của phản ứng $\\Delta_r H^\\circ_{298} = +180\\text{ kJ/mol} > 0$ nên đây là phản ứng thu nhiệt. Phản ứng hóa học xảy ra có sự hấp thụ năng lượng dưới dạng nhiệt từ môi trường xung quanh."
        },
        {
            "id": 13,
            "question": "Phát biểu nào sau đây đúng?",
            "options": {
                "A": "Ở dạng mạch hở, glucose có 6 nhóm -OH liền kề.",
                "B": "Có thể phân biệt glucose và fructose bằng thuốc thử Tollens.",
                "C": "Phân tử tinh bột gồm nhiều gốc $\\beta$-glucose liên kết với nhau.",
                "D": "Saccharose không tham gia phản ứng tráng bạc."
            },
            "answer": "D",
            "explanation": "- A sai: Ở dạng mạch hở, glucose có 5 nhóm -OH liền kề và 1 nhóm -CHO.\\n- B sai: Trong môi trường kiềm của thuốc thử Tollens, fructose chuyển hóa thành glucose nên cả hai đều tráng bạc.\\n- C sai: Tinh bột được cấu tạo từ các gốc $\\alpha$-glucose.\\n- D đúng: Phân tử saccharose liên kết qua nguyên tử oxygen giữa C1 của glucose và C2 của fructose, làm mất nhóm -OH hemiacetal/hemiketal tự do, không mở vòng tạo aldehyde nên không có phản ứng tráng bạc."
        },
        {
            "id": 14,
            "question": "Trong các chất có công thức cấu tạo cho dưới đây, chất nào thuộc loại aldehyde?",
            "options": {
                "A": "$\\text{CH}_3\\text{COOH}$.",
                "B": "$\\text{HCHO}$.",
                "C": "$\\text{CH}_3\\text{Cl}$.",
                "D": "$\\text{C}_2\\text{H}_5\\text{OH}$."
            },
            "answer": "B",
            "explanation": "Formaldehyde ($\\text{HCHO}$) chứa nhóm carbonyl liên kết trực tiếp với nguyên tử hydrogen (nhóm formyl $-CHO$) nên là một aldehyde. $\\text{CH}_3\\text{COOH}$ là carboxylic acid, $\\text{CH}_3\\text{Cl}$ là dẫn xuất halogen, $\\text{C}_2\\text{H}_5\\text{OH}$ là alcohol."
        },
        {
            "id": 15,
            "question": "Yếu tố nào sau đây KHÔNG làm dịch chuyển cân bằng của một hệ phản ứng hóa học thuận nghịch?",
            "options": {
                "A": "Áp suất.",
                "B": "Nồng độ.",
                "C": "Chất xúc tác.",
                "D": "Nhiệt độ."
            },
            "answer": "C",
            "explanation": "Chất xúc tác làm tăng đồng thời tốc độ phản ứng thuận và phản ứng nghịch với mức độ như nhau, giúp hệ phản ứng nhanh đạt tới trạng thái cân bằng chứ không làm thay đổi nồng độ các chất ở trạng thái cân bằng, do đó không làm dịch chuyển cân bằng hóa học."
        },
        {
            "id": 16,
            "question": "Chất dùng để phân biệt hai dung dịch phenol và ethanol một cách nhanh chóng và rõ ràng nhất là",
            "options": {
                "A": "nước bromine.",
                "B": "dung dịch NaOH.",
                "C": "quỳ tím.",
                "D": "nước nóng."
            },
            "answer": "A",
            "explanation": "Dùng nước bromine. Phenol tác dụng ngay với nước bromine tạo kết tủa trắng 2,4,6-tribromophenol. Ethanol không phản ứng với nước bromine nên không làm mất màu hay tạo kết tủa."
        },
        {
            "id": 17,
            "question": "Cấu hình electron lớp ngoài cùng của các nguyên tử các nguyên tố halogen (nhóm VIIA) là",
            "options": {
                "A": "$ns^2 np^3$.",
                "B": "$ns^2 np^5$.",
                "C": "$ns^2 np^4$.",
                "D": "$ns^2 np^6$."
            },
            "answer": "B",
            "explanation": "Các nguyên tố halogen thuộc nhóm VIIA trong bảng tuần hoàn, nguyên tử có 7 electron ở lớp ngoài cùng với cấu hình chung là $ns^2 np^5$."
        },
        {
            "id": 18,
            "question": "Hợp chất nào sau đây chỉ chứa liên kết ion?",
            "options": {
                "A": "$\\text{HCl}$.",
                "B": "$\\text{NaCl}$.",
                "C": "$\\text{NH}_4\\text{NO}_3$.",
                "D": "$\\text{H}_2\\text{O}$."
            },
            "answer": "B",
            "explanation": "$\\text{NaCl}$ là hợp chất ion tạo bởi kim loại điển hình ($Na$) và phi kim điển hình ($Cl$), trong tinh thể chỉ chứa liên kết ion giữa $Na^+$ và $Cl^-$. Trong $\\text{NH}_4\\text{NO}_3$ vừa có liên kết ion giữa $NH_4^+$ và $NO_3^-$, vừa có liên kết cộng hóa trị bên trong các ion. $\\text{HCl}$ và $\\text{H}_2\\text{O}$ chỉ chứa liên kết cộng hóa trị có cực."
        }
    ],
    "part2": [
        {
            "id": 1,
            "title": "Thí nghiệm đo pH để so sánh lực base của một số amine và ammonia",
            "context": "Một nhóm học sinh tiến hành thí nghiệm đo pH để so sánh lực base của một số amine và ammonia trong dung môi nước với giả thuyết “Khi số lượng carbon trong phân tử amine càng nhiều thì lực base của amine càng tăng làm cho pH của dung dịch tăng”. Nhóm học sinh tiến hành như sau:\\n- Bước 1: Chuẩn bị các cốc chứa dung dịch của các chất: $\\text{NH}_3$, $\\text{CH}_3\\text{NH}_2$, $\\text{CH}_3\\text{CH}_2\\text{NH}_2$, $(\\text{CH}_3)_2\\text{NH}$ và $\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{NH}_2$ đều ở 25°C (mỗi cốc chỉ chứa 1 dung dịch, mỗi dung dịch chỉ chứa 1 chất tan có nồng độ 0,1M).\\n- Bước 2: Dùng thiết bị đo pH để đo giá trị pH của các dung dịch.\\n- Bước 3: Ghi kết quả đo được ở bảng sau:\\n<div style='overflow-x:auto; margin: 10px 0;'><table style='width:100%; border-collapse: collapse; text-align: center;'><thead><tr style='background:#f1f5f9;'><th style='padding:8px; border:1px solid #cbd5e1;'>Dung dịch ($C_M = 0,1\\text{ M}$)</th><th style='padding:8px; border:1px solid #cbd5e1;'>$\\text{NH}_3$</th><th style='padding:8px; border:1px solid #cbd5e1;'>$\\text{CH}_3\\text{NH}_2$</th><th style='padding:8px; border:1px solid #cbd5e1;'>$\\text{CH}_3\\text{CH}_2\\text{NH}_2$</th><th style='padding:8px; border:1px solid #cbd5e1;'>$\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{NH}_2$</th><th style='padding:8px; border:1px solid #cbd5e1;'>$(\\text{CH}_3)_2\\text{NH}$</th></tr></thead><tbody><tr><td style='padding:8px; border:1px solid #cbd5e1; font-weight:700;'>Giá trị pH</td><td style='padding:8px; border:1px solid #cbd5e1;'>11,1</td><td style='padding:8px; border:1px solid #cbd5e1;'>11,3</td><td style='padding:8px; border:1px solid #cbd5e1;'>11,4</td><td style='padding:8px; border:1px solid #cbd5e1;'>11,5</td><td style='padding:8px; border:1px solid #cbd5e1;'>11,7</td></tr></tbody></table></div>",
            "statements": {
                "a": "Từ kết quả thí nghiệm, kết luận giả thuyết ban đầu của nhóm học sinh là đúng.",
                "b": "$\\text{C}_2\\text{H}_5\\text{NH}_2$ có tên thay thế là ethylamine.",
                "c": "$\\text{NH}_3$ có lực base yếu hơn các amine được khảo sát.",
                "d": "Lực base của $(\\text{CH}_3)_2\\text{NH}$ lớn hơn của $\\text{CH}_3\\text{CH}_2\\text{NH}_2$."
            },
            "answers": {
                "a": "S",
                "b": "S",
                "c": "Đ",
                "d": "Đ"
            },
            "explanations": {
                "a": "Sai. Giả thuyết ban đầu không đúng vì $(\\text{CH}_3)_2\\text{NH}$ chỉ có 2 nguyên tử carbon nhưng có pH = 11,7 lớn hơn $\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{NH}_2$ có 3 carbon với pH = 11,5. Lực base không chỉ phụ thuộc số lượng carbon mà còn phụ thuộc vào bậc của amine và hiệu ứng solvat hóa trong dung môi nước.",
                "b": "Sai. Tên thay thế của $\\text{C}_2\\text{H}_5\\text{NH}_2$ là ethanamine. Ethylamine là tên gốc - chức.",
                "c": "Đúng. Dung dịch $\\text{NH}_3$ có pH = 11,1 (nhỏ nhất trong các chất khảo sát ở cùng nồng độ 0,1M) nên có lực base yếu nhất.",
                "d": "Đúng. Dung dịch $(\\text{CH}_3)_2\\text{NH}$ có pH = 11,7 lớn hơn pH của $\\text{CH}_3\\text{CH}_2\\text{NH}_2$ (pH = 11,4) nên lực base của dimethylamine mạnh hơn ethylamine."
            }
        },
        {
            "id": 2,
            "title": "Thí nghiệm điều chế ethyl acetate trong phòng thí nghiệm",
            "context": "Tiến hành thí nghiệm điều chế ethyl acetate theo các bước như hình vẽ dưới đây:<br><div style='text-align:center; margin: 12px 0;'><img src='" + b64_ethyl + "' style='max-width: 100%; max-height: 280px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);' alt='Thí nghiệm điều chế ethyl acetate'></div>- Bước 1: Cho 10 mL $\\text{C}_2\\text{H}_5\\text{OH}$ ($D = 0,78\\text{ g/cm}^3$) cùng với 10 mL $\\text{CH}_3\\text{COOH}$ ($D = 1,05\\text{ g/cm}^3$), vài giọt dung dịch $\\text{H}_2\\text{SO}_4$ đặc và lắc đều bình cầu.<br>- Bước 2: Đun nóng bình cầu đến 70°C trong khoảng từ 5 đến 6 phút.<br>- Bước 3: Các chất thu được ở bình nón được thêm tiếp vào 2 mL dung dịch $\\text{NaCl}$ bão hòa.",
            "statements": {
                "a": "Sau bước 2, trong bình cầu có phản ứng ester hóa sau:$$\\text{CH}_3\\text{COOH} + \\text{HOCH}_2\\text{CH}_3 \\xrightleftharpoons{\\text{H}_2\\text{SO}_4\\text{ đặc, } t^\\circ} \\text{CH}_3\\text{COOCH}_2\\text{CH}_3 + \\text{H}_2\\text{O}$$",
                "b": "Giả sử hiệu suất của phản ứng đạt 40%, khối lượng ester thu được là 5,97 gam (kết quả đã được làm tròn đến hàng phần trăm).",
                "c": "Ở bước 3, dung dịch $\\text{NaCl}$ bão hòa có vai trò làm tăng hiệu suất phản ứng ester hóa.",
                "d": "Sau bước 2, các chất $\\text{C}_2\\text{H}_5\\text{OH}$ và $\\text{CH}_3\\text{COOH}$ vẫn còn trong bình cầu."
            },
            "answers": {
                "a": "Đ",
                "b": "Đ",
                "c": "S",
                "d": "Đ"
            },
            "explanations": {
                "a": "Đúng. Đây là phương trình hóa học chính xác của phản ứng thuận nghịch este hóa điều chế ethyl acetate.",
                "b": "Đúng. Ta có:<br>$n_{\\text{C}_2\\text{H}_5\\text{OH}} = \\frac{10 \\times 0,78}{46} \\approx 0,1696\\text{ mol}$; $n_{\\text{CH}_3\\text{COOH}} = \\frac{10 \\times 1,05}{60} = 0,175\\text{ mol}$.<br>Vì $0,1696 < 0,175$ nên hiệu suất phản ứng tính theo alcohol $\\text{C}_2\\text{H}_5\\text{OH}$.<br>Khối lượng ester thu được với hiệu suất 40%: $m_{\\text{ester}} = 0,1696 \\times 88 \\times 40\\% \\approx 5,9687\\text{ g} \\approx 5,97\\text{ gam}$.",
                "c": "Sai. Dung dịch $\\text{NaCl}$ bão hòa được thêm vào bình nón sau khi ngưng tụ để làm tăng khối lượng riêng của lớp chất lỏng phía dưới và giảm độ tan của ethyl acetate, giúp ester tách lớp rõ rệt nổi lên trên, hoàn toàn không có vai trò làm tăng hiệu suất phản ứng.",
                "d": "Đúng. Phản ứng ester hóa là phản ứng thuận nghịch (hiệu suất không bao giờ đạt 100%) nên sau phản ứng các chất tham gia $\\text{C}_2\\text{H}_5\\text{OH}$ và $\\text{CH}_3\\text{COOH}$ vẫn còn dư trong bình cầu."
            }
        },
        {
            "id": 3,
            "title": "Cấu trúc, tính chất và độ tan của đường Lactose",
            "context": "Lactose, còn gọi là đường sữa, là một loại đường disaccharide được tạo thành từ một phân tử glucose và một phân tử galactose liên kết với nhau. Lactose chủ yếu được tìm thấy trong sữa và các sản phẩm từ sữa, như phô mai và sữa chua. Đây là nguồn cung cấp năng lượng quan trọng, đặc biệt là cho trẻ sơ sinh và trẻ nhỏ. Tuy nhiên, một số người gặp khó khăn trong việc tiêu hóa lactose do thiếu enzyme lactase, dẫn đến tình trạng không dung nạp lactose, gây ra các triệu chứng như đầy bụng và tiêu chảy khi tiêu thụ các sản phẩm chứa lactose. Trong công nghiệp thực phẩm, lactose được sử dụng như một chất làm ngọt nhẹ và cũng đóng vai trò quan trọng trong việc lên men các sản phẩm từ sữa. Cho công thức cấu tạo của lactose như hình bên:<br><div style='text-align:center; margin: 12px 0;'><img src='" + b64_lactose + "' style='max-width: 100%; max-height: 220px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);' alt='Công thức cấu tạo Lactose'></div>",
            "statements": {
                "a": "Công thức phân tử của lactose là $\\text{C}_{12}\\text{H}_{22}\\text{O}_{11}$.",
                "b": "Thủy phân 1 phân tử lactose trong môi trường acid thu được 2 phân tử glucose.",
                "c": "Lactose có phản ứng với thuốc thử Tollens khi đun nóng.",
                "d": "Độ tan trong nước của lactose ở 60°C là 37,2 gam/100 gam $\\text{H}_2\\text{O}$; ở 25°C là 18,9 gam/100 gam $\\text{H}_2\\text{O}$. Khi làm nguội 274,4 gam dung dịch lactose bão hoà ở 60°C xuống 25°C thì tách ra 36,0 gam lactose (làm tròn kết quả đến hàng phần chục)."
            },
            "answers": {
                "a": "Đ",
                "b": "S",
                "c": "Đ",
                "d": "S"
            },
            "explanations": {
                "a": "Đúng. Lactose là một disaccharide nên có công thức phân tử là $\\text{C}_{12}\\text{H}_{22}\\text{O}_{11}$.",
                "b": "Sai. Thủy phân hoàn toàn 1 phân tử lactose trong môi trường acid thu được 1 phân tử glucose và 1 phân tử galactose (không phải 2 phân tử glucose như maltose).",
                "c": "Đúng. Trong phân tử lactose, gốc glucose vẫn còn nhóm -OH hemiacetal tự do (có khả năng mở vòng tạo nhóm formyl -CHO) nên có tính khử và tham gia phản ứng tráng bạc với thuốc thử Tollens.",
                "d": "Sai.<br>Ở 60°C: 100 g nước hòa tan 37,2 g lactose tạo 137,2 g dung dịch bão hòa.<br>Trong 274,4 g dung dịch bão hòa ở 60°C (gấp $274,4 / 137,2 = 2$ lần) có: $m_{\\text{lactose}} = 37,2 \\times 2 = 74,4\\text{ g}$; $m_{\\text{nước}} = 100 \\times 2 = 200\\text{ g}$.<br>Khi làm nguội xuống 25°C, 200 g nước hòa tan tối đa: $18,9 \\times 2 = 37,8\\text{ g}$ lactose.<br>Khối lượng lactose kết tinh tách ra: $m = 74,4 - 37,8 = 36,6\\text{ gam}$ (không phải 36,0 gam)."
            }
        },
        {
            "id": 4,
            "title": "Cấu tạo, tính chất lưỡng tính và hiện tượng điện di của Lysine và Glutamic acid",
            "context": "Lysine (Lys) và glutamic acid (Glu) đều là amino acid. Tuy nhiên, chúng có sự khác biệt chính: lysine quan trọng cho sự tăng trưởng và phát triển cơ bắp, giúp tạo carnitine và vận chuyển chất béo để tạo năng lượng, là amino acid thiết yếu mà cơ thể không tự tổng hợp được, trong khi glutamic acid là tiền chất của nhiều amino acid khác và đóng vai trò quan trọng trong hệ thần kinh, trao đổi chất và chuyển hóa carbohydrate và thành phần chính tạo nên bột ngọt (MSG), là amino acid không thiết yếu mà cơ thể có thể tự sản xuất. Cho công thức cấu tạo của lysine và glutamic acid như sau:<br><div style='text-align:center; margin: 12px 0;'><img src='" + b64_lys_glu + "' style='max-width: 100%; max-height: 150px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);' alt='Công thức cấu tạo Lysine và Glutamic acid'></div>",
            "statements": {
                "a": "Peptide được tạo bởi Lys-Glu có công thức phân tử là $\\text{C}_6\\text{H}_{23}\\text{N}_3\\text{O}_6$.",
                "b": "Khi hòa tan vào nước, lysine cho dung dịch làm quỳ tím chuyển thành màu đỏ còn glutamic acid cho dung dịch làm quỳ tím chuyển thành màu xanh.",
                "c": "Trung hòa hoàn toàn 65,85 gam hỗn hợp X gồm Lys và Glu có tỉ lệ mol tương ứng là 2:1 thì cần tối đa 0,6 mol dung dịch NaOH.",
                "d": "Cho giá trị điểm đẳng điện của Lys ($pI = 9,7$) và Glu ($pI = 3,2$). Khi đặt vào điện trường $\\text{pH} = 6$ thì Lys di chuyển về cực dương còn Glu di chuyển về cực âm dựa theo tính chất điện di."
            },
            "answers": {
                "a": "S",
                "b": "S",
                "c": "Đ",
                "d": "S"
            },
            "explanations": {
                "a": "Sai. Phân tử Lys có CTPT $\\text{C}_6\\text{H}_{14}\\text{N}_2\\text{O}_2$, Glu có CTPT $\\text{C}_5\\text{H}_9\\text{NO}_4$. Dipeptide Lys-Glu có CTPT là $\\text{C}_6\\text{H}_{14}\\text{N}_2\\text{O}_2 + \\text{C}_5\\text{H}_9\\text{NO}_4 - \\text{H}_2\\text{O} = \\text{C}_{11}\\text{H}_{21}\\text{N}_3\\text{O}_5$.",
                "b": "Sai. Lysine có 2 nhóm amino ($-NH_2$) và 1 nhóm carboxyl ($-COOH$) nên dung dịch có tính base, làm quỳ tím chuyển sang màu xanh. Glutamic acid có 1 nhóm amino và 2 nhóm carboxyl nên dung dịch có tính acid, làm quỳ tím chuyển sang màu đỏ.",
                "c": "Đúng. Gọi $n_{\\text{Glu}} = x\\text{ mol} \\Rightarrow n_{\\text{Lys}} = 2x\\text{ mol}$.<br>Ta có: $m_X = 146 \\times 2x + 147 \\times x = 439x = 65,85 \\Rightarrow x = 0,15\\text{ mol}$.<br>Vậy $n_{\\text{Glu}} = 0,15\\text{ mol}$ và $n_{\\text{Lys}} = 0,30\\text{ mol}$.<br>Glu tác dụng với NaOH theo tỉ lệ 1:2 (có 2 nhóm -COOH); Lys tác dụng theo tỉ lệ 1:1 (có 1 nhóm -COOH).<br>$\\Rightarrow n_{\\text{NaOH}} = n_{\\text{Lys}} + 2 \\times n_{\\text{Glu}} = 0,30 + 2 \\times 0,15 = 0,60\\text{ mol}$.",
                "d": "Sai. Ở $\\text{pH} = 6$:<br>- Lysine có $pI = 9,7 > \\text{pH} = 6$ nên phân tử mang điện tích dương tổng cộng $\\Rightarrow$ di chuyển về phía cực âm (cathode).<br>- Glutamic acid có $pI = 3,2 < \\text{pH} = 6$ nên phân tử mang điện tích âm tổng cộng $\\Rightarrow$ di chuyển về phía cực dương (anode)."
            }
        }
    ],
    "part3": [
        {
            "id": 1,
            "question": "Acid béo omega-3 và omega-6 là các acid béo không no với liên kết đôi đầu tiên ở vị trí số 3 và 6 khi đánh số từ nhóm methyl ($-CH_3$). Acid béo omega-3 và omega-6 đều có vai trò quan trọng đối với cơ thể, giúp phòng ngừa nhiều loại bệnh tim mạch và viêm nhiễm. Linoleic acid có công thức cấu tạo như hình bên:<br><div style='text-align:center; margin: 8px 0;'><img src='" + b64_linoleic + "' style='max-width: 100%; max-height: 80px; border-radius: 6px;' alt='Công thức Linoleic acid'></div>Linoleic acid thuộc loại acid béo omega-x. Giá trị của x là bao nhiêu?",
            "answer": "6",
            "explanation": "Đánh số thứ tự từ nguyên tử carbon của nhóm methyl ($-CH_3$) ở đầu mạch: Carbon số 1 là carbon nhóm methyl, các carbon tiếp theo là số 2, 3, 4, 5. Liên kết đôi đầu tiên nằm giữa carbon số 6 và carbon số 7. Do liên kết đôi đầu tiên ở vị trí C số 6 tính từ nhóm methyl nên linoleic acid là acid béo omega-6. Vậy x = 6."
        },
        {
            "id": 2,
            "question": "Cho phản ứng cháy sau:$$\\text{C}(s) + \\text{O}_2(g) \\rightarrow \\text{CO}_2(g)$$Tiến hành các tác động sau:\\n(1) Giảm nhiệt độ phản ứng bằng cách phun nước.\\n(2) Phun khí $\\text{O}_2$ vào đám cháy.\\n(3) Phun khí $\\text{CO}_2$ vào đám cháy.\\n(4) Tăng diện tích bề mặt carbon bằng cách chia nhỏ nguyên liệu carbon.\\nHãy liệt kê các tác động để dập tắt đám cháy theo số thứ tự từ nhỏ đến lớn (Ví dụ: nếu chọn 1 và 2 thì ghi 12; chọn 1, 3 và 4 thì ghi 134,...).",
            "answer": "13",
            "explanation": "Để dập tắt đám cháy than carbon: (1) Phun nước làm hạ nhiệt độ phản ứng xuống dưới nhiệt độ cháy do nước thu nhiệt lớn khi bay hơi; (3) Phun khí $\\text{CO}_2$ nặng hơn không khí sẽ bao phủ bề mặt, cách ly chất cháy với oxygen trong không khí. Tác động (2) và (4) làm tăng nồng độ chất phản ứng và diện tích tiếp xúc sẽ làm đám cháy bùng phát mạnh hơn. Do đó các tác động giúp dập tắt đám cháy là 1 và 3, viết theo thứ tự là 13."
        },
        {
            "id": 3,
            "question": "Đun nóng một loại mỡ động vật với dung dịch KOH, sản phẩm thu được có chứa muối potassium stearate. Phân tử khối của potassium stearate là bao nhiêu amu?",
            "answer": "322",
            "explanation": "Stearic acid có công thức là $\\text{C}_{17}\\text{H}_{35}\\text{COOH}$. Muối potassium stearate có công thức là $\\text{C}_{17}\\text{H}_{35}\\text{COOK}$.\\nPhân tử khối $M = 17 \\times 12 + 35 \\times 1 + 12 + 16 \\times 2 + 39 = 204 + 35 + 44 + 39 = 322\\text{ amu}$."
        },
        {
            "id": 4,
            "question": "Xà phòng hóa hoàn toàn 600 gam chất béo A với lượng vừa đủ dung dịch chứa 2 mol KOH. Sản phẩm thu được sau phản ứng gồm hỗn hợp muối carboxylate và 58,88 gam glycerol. Sau khi thêm các chất phụ gia cần thiết thì thu được xà phòng (các muối carboxylate trong xà phòng chiếm 60% khối lượng xà phòng). Biết mỗi bánh xà phòng có trọng lượng là 90g, số bánh xà phòng sản xuất được là bao nhiêu? (Kết quả làm tròn ở phép tính cuối cùng đến hàng đơn vị nguyên).",
            "answer": "12",
            "explanation": "Khối lượng KOH phản ứng: $m_{\\text{KOH}} = 2 \\times 56 = 112\\text{ g}$.\\nÁp dụng định luật bảo toàn khối lượng:\\n$m_{\\text{muối}} = m_{\\text{chất béo}} + m_{\\text{KOH}} - m_{\\text{glycerol}} = 600 + 112 - 58,88 = 653,12\\text{ g}$.\\nKhối lượng xà phòng thu được: $m_{\\text{xà phòng}} = \\frac{653,12}{60\\%} \\approx 1088,533\\text{ g}$.\\nSố bánh xà phòng sản xuất được: $N = \\frac{1088,533}{90} \\approx 12,09 \\rightarrow 12\\text{ bánh}$."
        },
        {
            "id": 5,
            "question": "Phần trăm khối lượng nguyên tố nitrogen trong alanine là a%. Giá trị của a là bao nhiêu? (Kết quả làm tròn đến hàng phần mười).",
            "answer": "15,7",
            "explanation": "Alanine có công thức cấu tạo $\\text{CH}_3-\\text{CH}(\\text{NH}_2)-\\text{COOH}$, công thức phân tử $\\text{C}_3\\text{H}_7\\text{NO}_2$.\\nPhân tử khối: $M = 3 \\times 12 + 7 \\times 1 + 14 + 2 \\times 16 = 89\\text{ amu}$.\\nPhần trăm khối lượng nitrogen: $a\\% = \\frac{14}{89} \\times 100\\% \\approx 15,7303\\% \\approx 15,7\\%$. Vậy a = 15,7."
        },
        {
            "id": 6,
            "question": "Ngành công nghiệp sản xuất nhiên liệu sinh học để phát triển bền vững cần áp dụng các công nghệ mới theo hướng thân thiện môi trường, rơm rạ là một loại phế phẩm nông nghiệp có thể dùng làm một nguồn nguyên liệu để sản xuất ethanol tạo xăng sinh học thay vì đốt gây ô nhiễm môi trường. Để sản xuất 100,0 L xăng E5 (ethanol chiếm 5% về thể tích) thì cần m kg rơm rạ. Biết cellulose chiếm 35% khối lượng khô của rơm rạ, việc tách cellulose ra khỏi rơm rạ thường đạt hiệu suất 40%. Trong khi đó, hiệu suất của quá trình chuyển hoá cellulose thành ethanol đạt 60%. Khối lượng riêng của ethanol là 0,8 g/mL. Giá trị của m là bao nhiêu? (Kết quả làm tròn ở phép tính cuối cùng đến hàng phần mười).",
            "answer": "83,9",
            "explanation": "Thể tích ethanol nguyên chất có trong 100 L xăng E5: $V_{\\text{ethanol}} = 100 \\times 5\\% = 5\\text{ L} = 5000\\text{ mL}$.\\nKhối lượng ethanol: $m_{\\text{ethanol}} = 5000 \\times 0,8 = 4000\\text{ g} = 4\\text{ kg}$.\\nPhương trình chuyển hóa cellulose thành ethanol:\\n$(\\text{C}_6\\text{H}_{10}\\text{O}_5)_n + n\\text{H}_2\\text{O} \\xrightarrow{} 2n\\text{C}_2\\text{H}_5\\text{OH} + 2n\\text{CO}_2$\\nCứ 162 kg cellulose lý thuyết tạo ra $2 \\times 46 = 92\\text{ kg}$ ethanol.\\nKhối lượng rơm rạ thực tế cần dùng:\\n$m = \\frac{4 \\times 162}{2 \\times 46 \\times 60\\% \\times 40\\% \\times 35\\%} = \\frac{648}{92 \\times 0,60 \\times 0,40 \\times 0,35} = \\frac{648}{7,728} \\approx 83,851\\text{ kg} \\approx 83,9\\text{ kg}$."
        }
    ]
}

# --- 1. Tạo file Markdown (.md) cho DOCX ---
md_lines = [
    "# BỘ GIÁO DỤC VÀ ĐÀO TẠO - TRƯỜNG THPT",
    "## KỲ THI TỐT NGHIỆP TRUNG HỌC PHỔ THÔNG NĂM 2026",
    "### BÀI THI: KHOA HỌC TỰ NHIÊN - MÔN: HÓA HỌC",
    "### ĐỀ ÔN TẬP TỚI HẾT CHƯƠNG 3 - MÃ ĐỀ: 01",
    "*Thời gian làm bài: 50 phút (Không kể thời gian phát đề)*",
    "",
    "Họ và tên thí sinh: ................................................................. Số báo danh: .............................",
    "",
    "Cho biết nguyên tử khối: H = 1; C = 12; N = 14; O = 16; Na = 23; Mg = 24; S = 32; Cl = 35,5; K = 39; Ca = 40; Fe = 56; Cu = 64; Br = 80; Ag = 108; Ba = 137.",
    "Các kí hiệu và chữ viết tắt: s: rắn; l: lỏng; g: khí; aq: dung dịch nước.",
    "",
    "---",
    "",
    "## PHẦN I. CÂU TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN (4,5 ĐIỂM)",
    "Thí sinh trả lời từ Câu 1 đến Câu 18. Mỗi câu hỏi thí sinh chỉ chọn một phương án. Mỗi câu trả lời đúng thí sinh được 0,25 điểm.",
    ""
]

for q in quiz_data["part1"]:
    clean_q = re.sub(r'<br\s*/?>', ' ', q['question'])
    md_lines.append(f"Câu {q['id']}: {clean_q}")
    for k, v in q['options'].items():
        clean_v = re.sub(r'<br\s*/?>', ' ', v)
        md_lines.append(f"{k}. {clean_v}")
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
    # Markdown context format
    if q['id'] == 1:
        md_lines.append("Một nhóm học sinh tiến hành thí nghiệm đo pH để so sánh lực base của một số amine và ammonia trong dung môi nước với giả thuyết “Khi số lượng carbon trong phân tử amine càng nhiều thì lực base của amine càng tăng làm cho pH của dung dịch tăng”. Nhóm học sinh tiến hành như sau:")
        md_lines.append("- Bước 1: Chuẩn bị các cốc chứa dung dịch của các chất: $\\text{NH}_3$, $\\text{CH}_3\\text{NH}_2$, $\\text{CH}_3\\text{CH}_2\\text{NH}_2$, $(\\text{CH}_3)_2\\text{NH}$ và $\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{NH}_2$ đều ở 25°C (mỗi cốc chỉ chứa 1 dung dịch, mỗi dung dịch chỉ chứa 1 chất tan có nồng độ 0,1M).")
        md_lines.append("- Bước 2: Dùng thiết bị đo pH để đo giá trị pH của các dung dịch.")
        md_lines.append("- Bước 3: Ghi kết quả đo được ở bảng sau:")
        md_lines.append("| Dung dịch ($C_M = 0,1\\text{ M}$) | NH3 | CH3NH2 | CH3CH2NH2 | CH3CH2CH2NH2 | (CH3)2NH |")
        md_lines.append("| :--- | :---: | :---: | :---: | :---: | :---: |")
        md_lines.append("| Giá trị pH | 11,1 | 11,3 | 11,4 | 11,5 | 11,7 |")
    elif q['id'] == 2:
        md_lines.append("Tiến hành thí nghiệm điều chế ethyl acetate theo các bước như hình vẽ:")
        md_lines.append("![Hình vẽ thí nghiệm điều chế ethyl acetate](dau-ra/lop-12/de-kiem-tra/images/ethyl_acetate_experiment.jpg)")
        md_lines.append("- Bước 1: Cho 10 mL $\\text{C}_2\\text{H}_5\\text{OH}$ ($D = 0,78\\text{ g/cm}^3$) cùng với 10 mL $\\text{CH}_3\\text{COOH}$ ($D = 1,05\\text{ g/cm}^3$), vài giọt dung dịch $\\text{H}_2\\text{SO}_4$ đặc và lắc đều bình cầu.")
        md_lines.append("- Bước 2: Đun nóng bình cầu đến 70°C trong khoảng từ 5 đến 6 phút.")
        md_lines.append("- Bước 3: Các chất thu được ở bình nón được thêm tiếp vào 2 mL dung dịch $\\text{NaCl}$ bão hòa.")
    elif q['id'] == 3:
        md_lines.append("Lactose, còn gọi là đường sữa, là một loại đường disaccharide được tạo thành từ một phân tử glucose và một phân tử galactose liên kết với nhau. Lactose chủ yếu được tìm thấy trong sữa và các sản phẩm từ sữa, như phô mai và sữa chua. Đây là nguồn cung cấp năng lượng quan trọng, đặc biệt là cho trẻ sơ sinh và trẻ nhỏ. Tuy nhiên, một số người gặp khó khăn trong việc tiêu hóa lactose do thiếu enzyme lactase, dẫn đến tình trạng không dung nạp lactose, gây ra các triệu chứng như đầy bụng và tiêu chảy khi tiêu thụ các sản phẩm chứa lactose. Trong công nghiệp thực phẩm, lactose được sử dụng như một chất làm ngọt nhẹ và cũng đóng vai trò quan trọng trong việc lên men các sản phẩm từ sữa. Cho công thức cấu tạo của lactose như hình bên:")
        md_lines.append("![Công thức cấu tạo của đường Lactose](dau-ra/lop-12/de-kiem-tra/images/lactose_structure.png)")
    elif q['id'] == 4:
        md_lines.append("Lysine (Lys) và glutamic acid (Glu) đều là amino acid. Tuy nhiên, chúng có sự khác biệt chính: lysine quan trọng cho sự tăng trưởng và phát triển cơ bắp, giúp tạo carnitine và vận chuyển chất béo để tạo năng lượng, là amino acid thiết yếu mà cơ thể không tự tổng hợp được, trong khi glutamic acid là tiền chất của nhiều amino acid khác và đóng vai trò quan trọng trong hệ thần kinh, trao đổi chất và chuyển hóa carbohydrate và thành phần chính tạo nên bột ngọt (MSG), là amino acid không thiết yếu mà cơ thể có thể tự sản xuất. Cho công thức cấu tạo của lysine và glutamic acid như sau:")
        md_lines.append("![Công thức cấu tạo của Lysine và Glutamic acid](dau-ra/lop-12/de-kiem-tra/images/lys_glu_structure.jpg)")

    for k, v in q['statements'].items():
        clean_v = re.sub(r'<br\s*/?>', ' ', v)
        md_lines.append(f"{k}) {clean_v}")
    md_lines.append("")

md_lines.extend([
    "---",
    "",
    "## PHẦN III. CÂU TRẮC NGHIỆM TRẢ LỜI NGẮN (1,5 ĐIỂM)",
    "Thí sinh trả lời từ Câu 1 đến Câu 6. Mỗi câu trả lời đúng thí sinh được 0,25 điểm.",
    ""
])

for q in quiz_data["part3"]:
    if q['id'] == 1:
        md_lines.append("Câu 1: Acid béo omega-3 và omega-6 là các acid béo không no với liên kết đôi đầu tiên ở vị trí số 3 và 6 khi đánh số từ nhóm methyl ($-CH_3$). Acid béo omega-3 và omega-6 đều có vai trò quan trọng đối với cơ thể, giúp phòng ngừa nhiều loại bệnh tim mạch. Linoleic acid có công thức cấu tạo như hình bên:")
        md_lines.append("![Công thức cấu tạo của Linoleic acid](dau-ra/lop-12/de-kiem-tra/images/linoleic_acid_structure.png)")
        md_lines.append("Linoleic acid thuộc loại acid béo omega-x. Giá trị của x là bao nhiêu?")
    else:
        clean_q = re.sub(r'<br\s*/?>', ' ', q['question'])
        md_lines.append(f"Câu {q['id']}: {clean_q}")
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
    "| 1 | B | 7 | C | 13 | D |",
    "| 2 | A | 8 | D | 14 | B |",
    "| 3 | A | 9 | D | 15 | C |",
    "| 4 | A | 10 | A | 16 | A |",
    "| 5 | A | 11 | C | 17 | B |",
    "| 6 | A | 12 | D | 18 | B |",
    "",
    "### BẢNG ĐÁP ÁN PHẦN II",
    "| Câu | Lệnh hỏi | Đáp án (Đ/S) | Câu | Lệnh hỏi | Đáp án (Đ/S) |",
    "| :---: | :---: | :---: | :---: | :---: | :---: |",
    "| 1 | a | S | 3 | a | Đ |",
    "| 1 | b | S | 3 | b | S |",
    "| 1 | c | Đ | 3 | c | Đ |",
    "| 1 | d | Đ | 3 | d | S |",
    "| 2 | a | Đ | 4 | a | S |",
    "| 2 | b | Đ | 4 | b | S |",
    "| 2 | c | S | 4 | c | Đ |",
    "| 2 | d | Đ | 4 | d | S |",
    "",
    "### BẢNG ĐÁP ÁN PHẦN III",
    "| Câu | Lời giải tóm tắt | Đáp số |",
    "| :---: | :--- | :---: |",
    "| 1 | Đánh số từ nhóm methyl, liên kết đôi đầu tiên ở C số 6 -> omega-6 | 6 |",
    "| 2 | Hạ nhiệt độ bằng nước (1) và cách ly oxygen bằng CO2 (3) -> 13 | 13 |",
    "| 3 | C17H35COOK có M = 17*12 + 35 + 44 + 39 = 322 amu | 322 |",
    "| 4 | m_muối = 600 + 112 - 58,88 = 653,12g -> m_xà phòng = 1088,53g -> 12 bánh | 12 |",
    "| 5 | %N trong alanine (C3H7NO2) = 14 / 89 * 100% = 15,7% | 15,7 |",
    "| 6 | m = (4 * 162) / (92 * 0,60 * 0,40 * 0,35) = 83,85 kg -> 83,9 kg | 83,9 |",
    "",
    "---",
    "",
    "### LỜI GIẢI CHI TIẾT TỪNG CÂU",
    ""
])

# Thêm lời giải chi tiết
md_lines.append("#### PHẦN I")
for q in quiz_data["part1"]:
    clean_exp = q['explanation'].replace('\\n', ' ')
    md_lines.append(f"Câu {q['id']}: Đáp án {q['answer']}. {clean_exp}")
    md_lines.append("")

md_lines.append("#### PHẦN II")
for q in quiz_data["part2"]:
    md_lines.append(f"Câu {q['id']}: {q['title']}")
    for k, exp in q['explanations'].items():
        clean_exp = exp.replace('<br>', ' ').replace('\\n', ' ')
        md_lines.append(f"{k}) {clean_exp}")
    md_lines.append("")

md_lines.append("#### PHẦN III")
for q in quiz_data["part3"]:
    clean_exp = q['explanation'].replace('\\n', ' ')
    md_lines.append(f"Câu {q['id']}: Đáp số {q['answer']}. {clean_exp}")
    md_lines.append("")

# Ghi file MD
md_path = os.path.join("dau-ra", "lop-12", "de-kiem-tra", "de-on-tap-toi-het-chuong-3-hoa-hoc-12.md")
os.makedirs(os.path.dirname(md_path), exist_ok=True)
with open(md_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))
print(f"Đã tạo file Markdown: {md_path}")

# --- 2. Xuất Word DOCX ---
docx_path = os.path.join("dau-ra", "lop-12", "de-kiem-tra", "de-on-tap-toi-het-chuong-3-hoa-hoc-12.docx")
create_styled_document(md_path, docx_path)
print(f"Đã tạo file Word DOCX: {docx_path}")

# --- 3. Xuất HTML Trắc Nghiệm Trực Tuyến ---
import shutil
html_path = os.path.join("dau-ra", "lop-12", "de-kiem-tra", "de-on-tap-toi-het-chuong-3-hoa-hoc-12.html")
generate_quiz_html(quiz_data, html_path)
print(f"Đã tạo file HTML (dau-ra): {html_path}")

# Đồng thời lưu vào thư mục lop-12/ để sẵn sàng làm bài trên web
web_path = os.path.join("lop-12", "de-on-tap-toi-het-chuong-3.html")
os.makedirs("lop-12", exist_ok=True)
shutil.copy(html_path, web_path)
print(f"Đã tạo file HTML (lop-12 web): {web_path}")

print("=== HOÀN TẤT TẠO BỘ ĐỀ ÔN TẬP TỚI HẾT CHƯƠNG 3 HÓA HỌC 12 ===")
