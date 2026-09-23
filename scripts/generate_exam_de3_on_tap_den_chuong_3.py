"""
Script: generate_exam_de3_on_tap_den_chuong_3.py
Purpose: Chuyển đổi và tạo bộ Đề số 3 ôn tập tới hết Chương 3 - Hóa học 12:
- Phần 1: 18 câu trắc nghiệm nhiều lựa chọn
- Phần 2: 4 câu trắc nghiệm Đúng / Sai (bối cảnh thực tế & thí nghiệm)
- Phần 3: 6 câu trắc nghiệm trả lời ngắn (tính toán / đếm số phát biểu đúng)
- Không có phần tự luận (chuẩn Lớp 12 Bộ GD&ĐT)
- Xuất file Markdown (.md)
- Xuất file Word (.docx) chuẩn A4, căn lề Trên 2cm, Dưới 2cm, Trái 2cm, Phải 1.5cm, Justified, số trang footer, không gạch đầu dòng ở đáp án
- Xuất file Web (.html) chuẩn vatli102.com, MathJax, đếm ngược 50 phút, tự chấm điểm, giải chi tiết, đồng bộ Google Sheet tự động
"""

import os
import sys
import base64
import json
import re
import shutil

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath("."))

from scripts.export_to_docx import create_styled_document
from scripts.export_to_html_quiz import generate_quiz_html

IMAGE_DIR = os.path.join("dau-ra", "lop-12", "de-kiem-tra", "images")

def get_base64_img(filename):
    path = os.path.join(IMAGE_DIR, filename)
    if not os.path.exists(path):
        return ""
    mime = "image/jpeg" if filename.endswith(('.jpg', '.jpeg')) else "image/png"
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode('utf-8')
    return f"data:{mime};base64,{data}"

b64_tyr = get_base64_img("de3_p1_Image21.png")
b64_phe_tyr = get_base64_img("de3_p3_Image43.jpg")
b64_elec = get_base64_img("de3_p3_Image44.png")
b64_pep_a = get_base64_img("de3_p3_Image45.png")

quiz_data = {
    "title": "ĐỀ SỐ 3: ÔN TẬP TỚI HẾT CHƯƠNG 3 - MÔN HÓA HỌC 12",
    "badge": "HÓA HỌC 12 - CHUẨN THI TỐT NGHIỆP THPT 2026",
    "duration": 50,
    "grade": 12,
    "google_sheet_url": "https://script.google.com/macros/s/AKfycbwRRiM81mghvA7cInvJgb4rPLzWOAE3s44wer0BJcURQ4hWwoykS19pkNQ9LyzH6Q8lTQ/exec",
    "part1": [
        {
            "id": 1,
            "question": "Từ phổ khối lượng, phân tử khối của ester X được xác định là 88. Công thức phù hợp với X là",
            "options": {
                "A": "$\\text{CH}_3\\text{CH}_2\\text{OH}$.",
                "B": "$\\text{CH}_3\\text{COOC}_2\\text{H}_5$.",
                "C": "$\\text{C}_3\\text{H}_7\\text{COOH}$.",
                "D": "$\\text{HCOOC}_2\\text{H}_5$."
            },
            "answer": "B",
            "explanation": "Phân tử khối $M = 88$ tương ứng với công thức phân tử $\\text{C}_4\\text{H}_8\\text{O}_2$. Trong các phương án: $\\text{CH}_3\\text{CH}_2\\text{OH}$ là alcohol ($M = 46$); $\\text{C}_3\\text{H}_7\\text{COOH}$ là carboxylic acid ($M = 88$); $\\text{HCOOC}_2\\text{H}_5$ là ester ($M = 74$); $\\text{CH}_3\\text{COOC}_2\\text{H}_5$ là ester ($M = 88$). Đề yêu cầu X là ester nên công thức phù hợp là $\\text{CH}_3\\text{COOC}_2\\text{H}_5$ (ethyl acetate)."
        },
        {
            "id": 2,
            "question": "Tính chất nào sau đây không phải là tính chất thích hợp giúp ethyl methanoate ($\\text{HCOOC}_2\\text{H}_5$) được sử dụng trong sản xuất một số loại nước hoa?",
            "options": {
                "A": "Khả năng dễ cháy.",
                "B": "Có mùi thơm dễ chịu.",
                "C": "Không độc hại.",
                "D": "Nhiệt độ sôi thấp."
            },
            "answer": "A",
            "explanation": "Trong công nghiệp nước hoa và mĩ phẩm, ester được sử dụng nhờ có mùi thơm đặc trưng dễ chịu (mùi hoa quả đào/mận), độ an toàn sinh học cao (không độc hại đối với cơ thể người ở nồng độ cho phép) và nhiệt độ sôi thấp giúp dễ bay hơi tỏa hương. Tính chất dễ cháy không phải là yếu tố hữu ích giúp ứng dụng trong nước hoa mà ngược lại là một nguy cơ cháy nổ cần lưu ý khi tồn trữ."
        },
        {
            "id": 3,
            "question": "Phát biểu nào sau đây không đúng?",
            "options": {
                "A": "Triolein có khả năng tham gia phản ứng cộng hydrogen khi đun nóng có xúc tác, áp suất thích hợp.",
                "B": "Các chất béo thường không tan trong nước và nhẹ hơn nước.",
                "C": "Chất béo bị thủy phân khi đun nóng trong dung dịch kiềm.",
                "D": "Chất béo là triester của ethylene glycol với các acid béo."
            },
            "answer": "D",
            "explanation": "Phát biểu D không đúng vì chất béo là triester của glycerol với các acid béo (còn gọi là triglyceride), không phải là triester của ethylene glycol (ethylene glycol là alcohol hai chức có 2 nhóm -OH, không thể tạo triester)."
        },
        {
            "id": 4,
            "question": "Ester X có công thức phân tử $\\text{C}_4\\text{H}_8\\text{O}_2$. Thủy phân X trong dung dịch $\\text{H}_2\\text{SO}_4$ loãng, đun nóng thu được sản phẩm gồm methyl alcohol và chất hữu cơ Y. Công thức của Y là",
            "options": {
                "A": "$\\text{C}_2\\text{H}_5\\text{COOH}$.",
                "B": "$\\text{HCOOH}$.",
                "C": "$\\text{CH}_3\\text{COOH}$.",
                "D": "$\\text{C}_2\\text{H}_5\\text{OH}$."
            },
            "answer": "A",
            "explanation": "Thủy phân ester sinh ra methyl alcohol ($\\text{CH}_3\\text{OH}$) chứng tỏ ester X có gốc alcohol là $-\\text{CH}_3$, dạng cấu tạo là $\\text{RCOOCH}_3$. Do X có công thức phân tử $\\text{C}_4\\text{H}_8\\text{O}_2$ nên gốc acyl R là $\\text{C}_2\\text{H}_5-$. Phương trình phản ứng: $\\text{C}_2\\text{H}_5\\text{COOCH}_3 + \\text{H}_2\\text{O} \\xrightleftharpoons{\\text{H}^+, t^\\circ} \\text{C}_2\\text{H}_5\\text{COOH} + \\text{CH}_3\\text{OH}$. Chất hữu cơ Y là propanoic acid ($\\text{C}_2\\text{H}_5\\text{COOH}$)."
        },
        {
            "id": 5,
            "question": "Phát biểu nào sau đây đúng?",
            "options": {
                "A": "Phân tử cellulose được cấu tạo từ các gốc fructose.",
                "B": "Fructose không có phản ứng tráng bạc.",
                "C": "Amylopectin có cấu trúc mạch phân nhánh.",
                "D": "Saccharose không tham gia phản ứng thủy phân."
            },
            "answer": "C",
            "explanation": "Amylopectin là thành phần chính của tinh bột, có cấu trúc mạch phân nhánh nhờ các liên kết $\\alpha$-1,4-glycoside ở mạch chính và liên kết $\\alpha$-1,6-glycoside tại điểm nhánh. Phân tử cellulose cấu tạo từ các gốc $\\beta$-glucose; fructose có phản ứng tráng bạc trong môi trường kiềm (chuyển hóa thành glucose); saccharose là disaccharide bị thủy phân thành glucose và fructose."
        },
        {
            "id": 6,
            "question": "Polysaccharide X là chất rắn, ở dạng bột vô định hình, màu trắng và được tạo thành trong cây xanh nhờ quá trình quang hợp. Thủy phân X, thu được monosaccharide Y. Phát biểu nào sau đây đúng?",
            "options": {
                "A": "Y tác dụng được với nước bromine.",
                "B": "X có phản ứng tráng bạc.",
                "C": "Phân tử khối của Y là 162.",
                "D": "X dễ tan trong nước lạnh."
            },
            "answer": "A",
            "explanation": "Polysaccharide X màu trắng, bột vô định hình, tổng hợp qua quang hợp là tinh bột ($(\\text{C}_6\\text{H}_{10}\\text{O}_5)_n$). Thủy phân hoàn toàn tinh bột thu được monosaccharide Y là glucose ($\\text{C}_6\\text{H}_{12}\\text{O}_6, M = 180$). Glucose chứa nhóm aldehyde ($-CH=O$) nên tác dụng với dung dịch nước bromine làm mất màu nâu đỏ và sinh ra gluconic acid: $\\text{CH}_2\\text{OH}[\\text{CHOH}]_4\\text{CHO} + \\text{Br}_2 + \\text{H}_2\\text{O} \\rightarrow \\text{CH}_2\\text{OH}[\\text{CHOH}]_4\\text{COOH} + 2\\text{HBr}$."
        },
        {
            "id": 7,
            "question": "Các gốc $\\alpha$-glucose trong phân tử tinh bột tạo dạng mạch amylopectin phân nhánh, xoắn lại. Phần phân nhánh liên kết với nhau bởi liên kết",
            "options": {
                "A": "$\\alpha$-1,4-glycoside.",
                "B": "$\\alpha$-1,3-glycoside.",
                "C": "$\\alpha$-1,6-glycoside.",
                "D": "$\\beta$-1,2-glycoside."
            },
            "answer": "C",
            "explanation": "Trong phân tử amylopectin, các mắt xích $\\alpha$-glucose trong chuỗi mạch chính liên kết với nhau bởi liên kết $\\alpha$-1,4-glycoside. Các điểm phân nhánh liên kết với nhau thông qua nguyên tử C1 của gốc glucose này với C6 của gốc glucose mạch chính tạo liên kết $\\alpha$-1,6-glycoside."
        },
        {
            "id": 8,
            "question": "Phát biểu nào sau đây đúng?",
            "options": {
                "A": "Glucose bị thủy phân trong môi trường acid.",
                "B": "Tinh bột là chất lỏng ở nhiệt độ thường.",
                "C": "Cellulose thuộc loại disaccharide.",
                "D": "Dung dịch saccharose hòa tan được $\\text{Cu(OH)}_2$."
            },
            "answer": "D",
            "explanation": "Saccharose có nhiều nhóm hydroxy ($-OH$) kề nhau nên ở nhiệt độ phòng, dung dịch saccharose hòa tan được kết tủa $\\text{Cu(OH)}_2$ tạo dung dịch phức đồng(II) màu xanh lam đặc trưng. Glucose là monosaccharide không bị thủy phân; tinh bột là chất rắn; cellulose là polysaccharide."
        },
        {
            "id": 9,
            "question": "[Sở GD Hải Phòng] Hợp chất X ($\\text{CH}_3\\text{NHCH}_3$) là chất khí ở điều kiện thường, tan nhiều trong nước và có mùi khó chịu. Hợp chất X có tên gọi là",
            "options": {
                "A": "propylamine.",
                "B": "diethylamine.",
                "C": "dimethylamine.",
                "D": "ethylmethylamine."
            },
            "answer": "C",
            "explanation": "Hợp chất $\\text{CH}_3\\text{NHCH}_3$ có hai nhóm methyl ($\\text{CH}_3-$) liên kết với nhóm $-\\text{NH}-$, tên theo danh pháp gốc - chức là dimethylamine (theo danh pháp thay thế là N-methylmethanamine)."
        },
        {
            "id": 10,
            "question": "[Sở Cà Mau lần 2 – Đề 1] Công thức cấu tạo thu gọn của ethylmethylamine là",
            "options": {
                "A": "$\\text{CH}_3\\text{CH}_2\\text{NHCH}_2\\text{CH}_3$.",
                "B": "$\\text{CH}_3\\text{CH}_2\\text{NHCH}_3$.",
                "C": "$\\text{CH}_3\\text{NHCH}_2\\text{CH}_2\\text{CH}_3$.",
                "D": "$\\text{CH}_3\\text{NHCH}_3$."
            },
            "answer": "B",
            "explanation": "Ethylmethylamine là amine bậc II có gốc ethyl ($\\text{CH}_3\\text{CH}_2-$) và gốc methyl ($\\text{CH}_3-$) liên kết với nguyên tử nitrogen: $\\text{CH}_3\\text{CH}_2\\text{NHCH}_3$."
        },
        {
            "id": 11,
            "question": "[Sở GD Hải Dương] Công thức của Tyrosine (Tyr) như hình sau:<br><div style='text-align:center; margin: 10px 0;'><img src='" + b64_tyr + "' style='max-width:240px; height:auto; border-radius:6px;' alt='Tyrosine'></div>Phát biểu nào sau đây đúng?",
            "options": {
                "A": "Tyr tác dụng được với dung dịch NaOH nhưng không tác dụng với dung dịch HCl.",
                "B": "Tyr không tác dụng với dung dịch nước bromine.",
                "C": "Tyr có 1 nhóm chức -OH phenol.",
                "D": "Số nguyên tử carbon trong phân tử Tyr là 10."
            },
            "answer": "C",
            "explanation": "Tyrosine (Tyr) có công thức cấu tạo là p-HO-C₆H₄-CH₂-CH(NH₂)-COOH (công thức phân tử C₉H₁₁NO₃, có 9 nguyên tử carbon). Nhóm -OH gắn trực tiếp vào vòng benzene nên là nhóm -OH phenol (nhận xét C đúng). Do có nhóm -OH phenol hoạt hóa mạnh vòng thơm ở các vị trí ortho, Tyr dễ dàng tác dụng với nước bromine tạo kết tủa trắng thế Br. Đồng thời Tyr có cả nhóm amino (-NH₂) và nhóm carboxyl (-COOH) nên là amino acid có tính lưỡng tính, tác dụng được với cả dung dịch HCl và dung dịch NaOH."
        },
        {
            "id": 12,
            "question": "[NAP – Vip 14] Phần trăm khối lượng của nguyên tố carbon trong phân tử aniline là",
            "options": {
                "A": "83,72%.",
                "B": "75,00%.",
                "C": "78,26%.",
                "D": "77,42%."
            },
            "answer": "D",
            "explanation": "Aniline có công thức phân tử $\\text{C}_6\\text{H}_7\\text{N}$ ($M = 6 \\times 12 + 7 \\times 1 + 14 = 93\\text{ g/mol}$). Khối lượng của nguyên tố carbon trong một phân tử là $6 \\times 12 = 72\\text{ amu}$. Phần trăm khối lượng carbon là: $\\%C = \\frac{72}{93} \\times 100\\% \\approx 77,42\\%$."
        },
        {
            "id": 13,
            "question": "[NAP– ĐỀ 29] Cá là một loại thực phẩm giàu dinh dưỡng và tốt cho cơ thể. Tuy nhiên nhiều người cảm thấy khó chịu vì cá thường có mùi tanh. Mùi tanh làm cá mất đi mùi vị và tính hấp dẫn của nó. Trong cá (đặc biệt là cá mè) có chứa một lượng hỗn hợp các amine (nhiều nhất là trimethylamine $(\\text{CH}_3)_3\\text{N}$) và một số chất khác. Phương pháp hóa học đơn giản để khử mùi tanh của cá trước khi nấu là",
            "options": {
                "A": "Rửa cá bằng các chất chua tự nhiên như giấm ăn, nước chanh....",
                "B": "Rửa cá với dung dịch nước vôi trong, sau đó rửa lại bằng nước sạch.",
                "C": "Rửa cá thật kĩ bằng nước sạch.",
                "D": "Rửa cá với các dung dịch acid mạnh như $\\text{HCl}, \\text{H}_2\\text{SO}_4$..., sau đó rửa lại bằng nước sạch."
            },
            "answer": "A",
            "explanation": "Mùi tanh của cá gây ra chủ yếu bởi các amine (tính base). Khi rửa cá bằng các dung dịch acid hữu cơ yếu tự nhiên và an toàn cho thực phẩm như giấm ăn (chứa acetic acid) hay chanh (chứa citric acid), acid sẽ phản ứng với amine tạo thành các muối tan không bay hơi, loại bỏ mùi tanh hiệu quả và an toàn."
        },
        {
            "id": 14,
            "question": "[Chuyên KHTN HN-L3] Các amine $\\text{CH}_3\\text{NH}_2, \\text{CH}_3\\text{NHCH}_3, \\text{CH}_3\\text{CH}_2\\text{NH}_2$ tan nhiều trong nước. Nguyên nhân là do các amine này",
            "options": {
                "A": "hình thành lực tương tác van der Waals lớn giữa các phân tử.",
                "B": "tạo được liên kết hydrogen với nước.",
                "C": "tạo được liên kết hydrogen liên phân tử với nhau.",
                "D": "đều ở thể khí nên dễ phân tán vào nước."
            },
            "answer": "B",
            "explanation": "Các amine mạch ngắn (nhỏ) tan tốt và tan nhiều trong nước nhờ nguyên tử nitrogen mang cặp electron tự do và các liên kết $\\text{N}-\\text{H}$ phân cực có khả năng tạo liên kết hydrogen mạnh với các phân tử nước."
        },
        {
            "id": 15,
            "question": "[Sở GD Nghệ An – L2] Dung dịch nào sau đây làm quỳ tím chuyển sang màu xanh?",
            "options": {
                "A": "Glycine.",
                "B": "Glutamic acid.",
                "C": "Aniline.",
                "D": "Ethylamine."
            },
            "answer": "D",
            "explanation": "Ethylamine ($\\text{C}_2\\text{H}_5\\text{NH}_2$) là aliphatic amine bậc I có tính base mạnh hơn ammonia do gốc ethyl đẩy electron, khi tan trong nước phân li cho môi trường kiềm ($\\text{pH} > 7$) làm quỳ tím hóa xanh. Glycine có 1 nhóm $-\\text{NH}_2$ và 1 nhóm $-\\text{COOH}$ (môi trường trung tính, không đổi màu quỳ); glutamic acid có 2 nhóm $-\\text{COOH}$ và 1 nhóm $-\\text{NH}_2$ (quỳ hóa đỏ); aniline có tính base rất yếu do vòng benzene hút electron nên không làm đổi màu quỳ tím."
        },
        {
            "id": 16,
            "question": "[Sở Vĩnh Phúc Lần 3] Amine nào sau đây là chất khí ở điều kiện thường?",
            "options": {
                "A": "Trimethylamine.",
                "B": "Ethylmethylamine.",
                "C": "Propan-2-amine.",
                "D": "Propan-1-amine."
            },
            "answer": "A",
            "explanation": "Ở điều kiện thường, chỉ có 4 amine ở thể khí gồm: methylamine, dimethylamine, trimethylamine và ethylamine. Ethylmethylamine, propan-1-amine và propan-2-amine đều là chất lỏng ở điều kiện thường."
        },
        {
            "id": 17,
            "question": "Phản ứng giữa albumin (có trong lòng trắng trứng) với $\\text{Cu(OH)}_2$ trong môi trường kiềm còn được gọi là",
            "options": {
                "A": "phản ứng thủy phân.",
                "B": "sự đông tụ protein.",
                "C": "phản ứng màu biuret.",
                "D": "sự biến tính protein."
            },
            "answer": "C",
            "explanation": "Phản ứng giữa các hợp chất có từ 2 liên kết peptide trở lên (tripeptide, polypeptide, protein như albumin) với $\\text{Cu(OH)}_2$ trong môi trường kiềm tạo hợp chất phức màu tím đặc trưng được gọi là phản ứng màu biuret."
        },
        {
            "id": 18,
            "question": "[Sở GD Tuyên Quang– L2] Cho các dung dịch: $\\text{C}_6\\text{H}_5\\text{NH}_2, \\text{CH}_3\\text{NH}_2, \\text{H}_2\\text{NCH}_2\\text{COOH}$ và $\\text{H}_2\\text{N}-[\\text{CH}_2]_4-\\text{CH}(\\text{NH}_2)-\\text{COOH}$. Trong các dung dịch trên, có bao nhiêu dung dịch làm đổi màu quỳ tím?",
            "options": {
                "A": "4.",
                "B": "3.",
                "C": "2.",
                "D": "1."
            },
            "answer": "C",
            "explanation": "Xét từng dung dịch: (1) $\\text{C}_6\\text{H}_5\\text{NH}_2$ (aniline): không đổi màu quỳ tím. (2) $\\text{CH}_3\\text{NH}_2$ (methylamine): quỳ tím hóa xanh. (3) $\\text{H}_2\\text{NCH}_2\\text{COOH}$ (glycine): không đổi màu quỳ tím. (4) $\\text{H}_2\\text{N}-[\\text{CH}_2]_4-\\text{CH}(\\text{NH}_2)-\\text{COOH}$ (lysine, có 2 nhóm $-\\text{NH}_2$, 1 nhóm $-\\text{COOH}$): quỳ tím hóa xanh. Vậy có đúng 2 dung dịch làm đổi màu quỳ tím."
        }
    ],
    "part2": [
        {
            "id": 1,
            "title": "Thí nghiệm thủy phân ethyl acetate trong môi trường kiềm",
            "context": "Phản ứng thủy phân ester trong môi trường kiềm được biểu diễn như sau:<br>$$\\text{R-COO-R'} + \\text{NaOH} \\rightarrow \\text{RCOONa} + \\text{R'OH}$$Một nhóm học sinh dự đoán <em>\"Nồng độ NaOH càng lớn thì tốc độ phản ứng thủy phân càng lớn\"</em>. Từ đó, học sinh tiến hành thí nghiệm ở nhiệt độ không đổi ($60^\\circ\\text{C}$) nhưng thay đổi nồng độ NaOH để kiểm tra dự đoán trên như sau:<br>- Bước 1: Thêm 4 mL ethyl acetate ($d = 0,9\\text{ g/mL}$) vào một ống nghiệm chứa 20 mL dung dịch NaOH nồng độ C (mol/L). Các giá trị nồng độ này không giống nhau giữa các thí nghiệm.<br>- Bước 2: Ngâm ống nghiệm trong nồi nước nóng (nhiệt độ nước khoảng $60^\\circ\\text{C}$) và đo thời gian cho đến khi phần chất lỏng trong ống nghiệm trở nên đồng nhất.<br>Kết quả thí nghiệm được cho ở bảng sau:<br><table style='margin:10px auto; border-collapse:collapse; text-align:center;'><thead><tr style='background:#f1f5f9;'><th style='padding:6px 12px; border:1px solid #cbd5e1;'>Nồng độ NaOH (mol/L)</th><td style='padding:6px 12px; border:1px solid #cbd5e1;'>4,0</td><td style='padding:6px 12px; border:1px solid #cbd5e1;'>3,6</td><td style='padding:6px 12px; border:1px solid #cbd5e1;'>3,2</td><td style='padding:6px 12px; border:1px solid #cbd5e1;'>2,8</td><td style='padding:6px 12px; border:1px solid #cbd5e1;'>2,4</td><td style='padding:6px 12px; border:1px solid #cbd5e1;'>2,0</td></tr></thead><tbody><tr><th style='padding:6px 12px; border:1px solid #cbd5e1;'>Thời gian hỗn hợp đồng nhất (phút)</th><td style='padding:6px 12px; border:1px solid #cbd5e1;'>5,2</td><td style='padding:6px 12px; border:1px solid #cbd5e1;'>6,0</td><td style='padding:6px 12px; border:1px solid #cbd5e1;'>7,0</td><td style='padding:6px 12px; border:1px solid #cbd5e1;'>8,2</td><td style='padding:6px 12px; border:1px solid #cbd5e1;'>9,5</td><td style='padding:6px 12px; border:1px solid #cbd5e1;'>11,0</td></tr></tbody></table>",
            "statements": {
                "a": "Phản ứng thủy phân ethyl acetate xảy ra ở bước 2 của các thí nghiệm.",
                "b": "Sau bước 1, phần chất lỏng trong các ống nghiệm tách thành hai lớp.",
                "c": "Phản ứng thủy phân hoàn toàn tại thời điểm hỗn hợp trong ống nghiệm đồng nhất.",
                "d": "Kết quả thí nghiệm chứng tỏ dự đoán của học sinh ban đầu là sai."
            },
            "answers": {
                "a": "Đ",
                "b": "Đ",
                "c": "Đ",
                "d": "S"
            },
            "explanations": {
                "a": "Đúng. Ở bước 1 tiến hành ở nhiệt độ phòng, phản ứng thủy phân xảy ra rất chậm. Khi đưa vào nồi nước nóng khoảng 60°C ở bước 2, nhiệt độ cao thúc đẩy phản ứng thủy phân xảy ra với tốc độ đo đạc được.",
                "b": "Đúng. Ethyl acetate nhẹ hơn nước ($d = 0,9\\text{ g/mL}$) và không tan trong dung dịch NaOH nên nổi lên trên tạo thành hai lớp chất lỏng phân cách rõ rệt.",
                "c": "Đúng. Sản phẩm sinh ra gồm sodium acetate và ethyl alcohol đều tan vô hạn trong nước. Do đó khi toàn bộ lượng ethyl acetate đã bị thủy phân hết, hỗn hợp trong ống nghiệm trở nên trong suốt, đồng nhất.",
                "d": "Sai. Khi nồng độ NaOH tăng từ 2,0 M lên 4,0 M, thời gian cần để hỗn hợp đồng nhất giảm dần từ 11,0 phút xuống 5,2 phút, nghĩa là tốc độ phản ứng tăng lên khi tăng nồng độ NaOH. Điều này chứng tỏ dự đoán ban đầu của học sinh là ĐÚNG."
            }
        },
        {
            "id": 2,
            "title": "Cấu trúc và phản ứng hóa học đặc trưng của cellulose",
            "context": "Cellulose là carbohydrate có nhiều ứng dụng quan trọng trong đời sống và sản xuất. Hai tính chất hóa học quan trọng của cellulose là phản ứng thủy phân trong môi trường acid và phản ứng của nhóm -OH.<br>- Khi cho cellulose phản ứng với $\\text{HNO}_3$ đặc nóng có $\\text{H}_2\\text{SO}_4$ đặc làm xúc tác sẽ tạo thành hỗn hợp cellulose trinitrate và cellulose dinitrate.<br>- Khi cho cellulose phản ứng với lượng dư $(\\text{CH}_3\\text{CO})_2\\text{O}$ trong $\\text{CH}_3\\text{COOH}$ có $\\text{H}_2\\text{SO}_4$ đặc làm xúc tác sẽ tạo thành cellulose triacetate $[\\text{C}_6\\text{H}_7\\text{O}_2(\\text{OCOCH}_3)_3]_n$. Thủy phân không hoàn toàn cellulose triacetate trong dung dịch $\\text{CH}_3\\text{COOH}$ sẽ tạo ra cellulose diacetate.",
            "statements": {
                "a": "Trong cấu trúc phân tử cellulose diacetate, mỗi mắt xích có chứa một nhóm hydroxy (-OH).",
                "b": "Phản ứng của cellulose với $\\text{HNO}_3$ đặc nóng thuộc loại phản ứng thủy phân trong môi trường acid.",
                "c": "Từ 16,20 tấn cellulose, với hiệu suất phản ứng tính theo cellulose là 90%, sẽ sản xuất được tối đa 26,73 tấn cellulose trinitrate.",
                "d": "Hỗn hợp của cellulose triacetate và cellulose diacetate gọi là tơ cellulose acetate, có dạng sợi, mềm mại, thường được dùng làm vải may mặc."
            },
            "answers": {
                "a": "Đ",
                "b": "S",
                "c": "Đ",
                "d": "Đ"
            },
            "explanations": {
                "a": "Đúng. Mỗi mắt xích cellulose nguyên bản có 3 nhóm -OH: $[\\text{C}_6\\text{H}_7\\text{O}_2(\\text{OH})_3]_n$. Khi tạo diacetate, 2 nhóm -OH bị acetyl hóa, còn lại 1 nhóm -OH tự do: $[\\text{C}_6\\text{H}_7\\text{O}_2(\\text{OH})(\\text{OCOCH}_3)_2]_n$.",
                "b": "Sai. Phản ứng giữa cellulose với $\\text{HNO}_3$ xúc tác $\\text{H}_2\\text{SO}_4$ đặc là phản ứng este hóa (phản ứng thế nhóm -OH bằng nhóm nitrate $-ONO_2$), không phải phản ứng thủy phân.",
                "c": "Đúng. Phương trình: $[\\text{C}_6\\text{H}_7\\text{O}_2(\\text{OH})_3]_n + 3n\\text{HNO}_3 \\rightarrow [\\text{C}_6\\text{H}_7\\text{O}_2(\\text{ONO}_2)_3]_n + 3n\\text{H}_2\\text{O}$. Cứ 162 gam cellulose tạo ra 297 gam cellulose trinitrate. Với 16,20 tấn cellulose và hiệu suất $H = 90\\%$, lượng cellulose trinitrate thu được là: $16,20 \\times \\frac{297}{162} \\times 0,90 = 26,73\\text{ tấn}$.",
                "d": "Đúng. Hỗn hợp cellulose triacetate và cellulose diacetate được kéo thành sợi gọi là tơ acetate, có đặc tính mềm mại, bóng mịn, ít nhăn và được dùng phổ biến trong dệt may thời trang."
            }
        },
        {
            "id": 3,
            "title": "[Sở Yên Bái-L2] Nghiên cứu điện di hỗn hợp Phe, Tyr và dipeptide Phe-Tyr",
            "context": "Dipeptide Phe-Tyr có cấu trúc:<br><div style='text-align:center; margin: 10px 0;'><img src='" + b64_phe_tyr + "' style='max-width:320px; height:auto; border-radius:6px;' alt='Phe-Tyr'></div>Hỗn hợp của dipeptide Phe-Tyr và hai amino acid thành phần (Phe và Tyr) đã được tiến hành điện di trong dung dịch đệm $\\text{pH} = 12$. Tại điều kiện này, thông tin của ba chất được cung cấp như sau:<br><table style='margin:10px auto; border-collapse:collapse; text-align:center;'><thead><tr style='background:#f1f5f9;'><th style='padding:6px 16px; border:1px solid #cbd5e1;'>Chất</th><th style='padding:6px 16px; border:1px solid #cbd5e1;'>Điện tích tại pH = 12</th><th style='padding:6px 16px; border:1px solid #cbd5e1;'>Kích thước tương đối</th></tr></thead><tbody><tr><td style='padding:6px 16px; border:1px solid #cbd5e1;'>Phe-Tyr</td><td style='padding:6px 16px; border:1px solid #cbd5e1;'>-2</td><td style='padding:6px 16px; border:1px solid #cbd5e1;'>Lớn</td></tr><tr><td style='padding:6px 16px; border:1px solid #cbd5e1;'>Tyr</td><td style='padding:6px 16px; border:1px solid #cbd5e1;'>-2</td><td style='padding:6px 16px; border:1px solid #cbd5e1;'>Nhỏ</td></tr><tr><td style='padding:6px 16px; border:1px solid #cbd5e1;'>Phe</td><td style='padding:6px 16px; border:1px solid #cbd5e1;'>-1</td><td style='padding:6px 16px; border:1px solid #cbd5e1;'>Nhỏ</td></tr></tbody></table>Vào cuối thí nghiệm thu được những kết quả sau: Ba chấm P, R, S là đại diện cho ba chất Phe hoặc Tyr hoặc Phe-Tyr (không theo thứ tự). Các chấm R và S vẫn nằm rất gần nhau.<br><div style='text-align:center; margin: 10px 0;'><img src='" + b64_elec + "' style='max-width:420px; height:auto; border-radius:6px;' alt='Dien di'></div>",
            "statements": {
                "a": "Kích thước phân tử càng lớn thì khả năng di chuyển về phía điện cực càng kém.",
                "b": "Chất có giá trị điện tích càng nhỏ thì khả năng di chuyển về phía điện cực càng tốt.",
                "c": "Chất P là Tyr.",
                "d": "Amino acid Phe có khả năng di chuyển với tốc độ gần như dipeptide Phe-Tyr trong điện trường."
            },
            "answers": {
                "a": "Đ",
                "b": "S",
                "c": "Đ",
                "d": "Đ"
            },
            "explanations": {
                "a": "Đúng. Phân tử có kích thước càng lớn sẽ chịu lực ma sát và lực cản của môi trường càng nhiều khi chuyển động, do đó khả năng di chuyển trong điện trường càng kém hơn.",
                "b": "Sai. Tốc độ di chuyển phụ thuộc vào độ lớn của điện tích (điện tích càng lớn về độ lớn tuyệt đối thì lực điện trường kéo càng mạnh) và kích thước phân tử (tỉ số điện tích / kích thước). Không thể kết luận giá trị điện tích càng nhỏ thì di chuyển càng tốt.",
                "c": "Đúng. Tyr có điện tích -2 (độ lớn điện tích 2) và kích thước nhỏ nên có mật độ điện tích lớn nhất, chịu lực điện trường mạnh và lực cản nhỏ nên di chuyển xa nhất về phía cực dương (+). Do đó chấm P ở vị trí xa nhất chính là Tyr.",
                "d": "Đúng. Phe có điện tích -1, kích thước nhỏ; Phe-Tyr có điện tích -2, kích thước lớn gấp đôi. Do tỉ số điện tích/kích thước của Phe và Phe-Tyr xấp xỉ nhau nên chúng di chuyển với vận tốc tương đương nhau, tương ứng với hai chấm R và S nằm sát cạnh nhau."
            }
        },
        {
            "id": 4,
            "title": "Cấu trúc và tính chất hóa học của peptide A",
            "context": "Cho peptide A có cấu tạo như sau:<br><div style='text-align:center; margin: 10px 0;'><img src='" + b64_pep_a + "' style='max-width:320px; height:auto; border-radius:6px;' alt='Peptide A'></div>",
            "statements": {
                "a": "Trong phân tử A có 3 liên kết peptide.",
                "b": "Công thức phân tử của A là $\\text{C}_{13}\\text{H}_{24}\\text{N}_4\\text{O}_6$.",
                "c": "Thuỷ phân hoàn toàn 66,4 gam A trong dung dịch NaOH dư thu được 86,8 gam hỗn hợp muối.",
                "d": "Peptide A có khả năng hòa tan $\\text{Cu(OH)}_2$ trong môi trường kiềm tạo ra dung dịch có màu tím đặc trưng."
            },
            "answers": {
                "a": "S",
                "b": "Đ",
                "c": "S",
                "d": "Đ"
            },
            "explanations": {
                "a": "Sai. Phân tử peptide A gồm 3 gốc amino acid liên kết với nhau: Glycine (đầu N) - Lysine (ở giữa) - Glutamic acid (đầu C). Đây là một tripeptide, do đó chỉ có 2 liên kết peptide ($-CONH-$).",
                "b": "Đúng. Tripeptide được tạo từ Gly ($\\text{C}_2\\text{H}_5\\text{NO}_2$), Lys ($\\text{C}_6\\text{H}_{14}\\text{N}_2\\text{O}_2$) và Glu ($\\text{C}_5\\text{H}_9\\text{NO}_4$) tách đi 2 phân tử $\\text{H}_2\\text{O}$: CTPT của A là $\\text{C}_2\\text{H}_5\\text{NO}_2 + \\text{C}_6\\text{H}_{14}\\text{N}_2\\text{O}_2 + \\text{C}_5\\text{H}_9\\text{NO}_4 - 2\\text{H}_2\\text{O} = \\text{C}_{13}\\text{H}_{24}\\text{N}_4\\text{O}_6$ ($M = 332\\text{ g/mol}$).",
                "c": "Sai. Số mol $n_A = \\frac{66,4}{332} = 0,2\\text{ mol}$. Do amino acid Glu có 2 nhóm $-\\text{COOH}$ nên khi thủy phân hoàn toàn trong NaOH dư, 1 mol A tác dụng với 4 mol NaOH (2 mol NaOH cắt 2 liên kết peptide + 2 mol NaOH trung hòa 2 nhóm carboxyl của Glu), tạo ra 1 mol Gly-Na ($M=97$), 1 mol Lys-Na ($M=168$) và 1 mol $\\text{Glu-Na}_2$ ($M=191$). Khối lượng muối thực tế thu được = $0,2 \\times (97 + 168 + 191) = 0,2 \\times 456 = 91,2\\text{ gam} \\neq 86,8\\text{ gam}$.",
                "d": "Đúng. Phân tử A là tripeptide có 2 liên kết peptide nên có phản ứng màu biuret đặc trưng với $\\text{Cu(OH)}_2$ trong dung dịch kiềm tạo phức màu tím."
            }
        }
    ],
    "part3": [
        {
            "id": 1,
            "question": "Ethanol có thể được sản xuất từ cellulose hoặc tinh bột. Loại ethanol này được dùng để sản xuất xăng E5 (xăng chứa 5% ethanol về thể tích). Lượng ethanol thu được từ 1 tấn mùn cưa (chứa 50% cellulose, phần còn lại là chất trơ) có thể dùng để pha chế bao nhiêu lít xăng E5? Biết hiệu suất quá trình sản xuất ethanol từ cellulose là 60% và ethanol có khối lượng riêng là $0,8\\text{ g mL}^{-1}$. (Kết quả làm tròn đến hàng đơn vị).",
            "answer": "4259",
            "explanation": "Khối lượng cellulose trong 1 tấn mùn cưa: $m = 1000 \\times 50\\% = 500\\text{ kg} = 500\\,000\\text{ g}$.<br>Sơ đồ: $(\\text{C}_6\\text{H}_{10}\\text{O}_5)_n \\xrightarrow{+\\text{H}_2\\text{O}} n\\text{C}_6\\text{H}_{12}\\text{O}_6 \\xrightarrow{\\text{men}} 2n\\text{C}_2\\text{H}_5\\text{OH} + 2n\\text{CO}_2$.<br>Khối lượng ethanol theo lý thuyết: $m_{\\text{LT}} = 500 \\times \\frac{2 \\times 46}{162} = 283,951\\text{ kg}$.<br>Khối lượng ethanol thực tế với hiệu suất 60%: $m_{\\text{TT}} = 283,951 \\times 0,60 = 170,370\\text{ kg} = 170\\,370\\text{ g}$.<br>Thể tích ethanol thu được: $V_{\\text{ethanol}} = \\frac{170\\,370\\text{ g}}{0,8\\text{ g/mL}} = 212\\,963\\text{ mL} = 212,963\\text{ lít}$.<br>Thể tích xăng E5 pha chế được: $V_{\\text{E5}} = \\frac{212,963}{0,05} \\approx 4259\\text{ lít}$."
        },
        {
            "id": 2,
            "question": "Cho dãy các chất: tripalmitin, phenol, ethyl alcohol, benzene, acetic acid, methyl formate. Có bao nhiêu chất trong dãy phản ứng với dung dịch NaOH?",
            "answer": "4",
            "explanation": "Các chất phản ứng với dung dịch NaOH gồm:<br>1. Tripalmitin: chất béo (ester) phản ứng thủy phân xà phòng hóa.<br>2. Phenol: có tính acid yếu phản ứng trung hòa NaOH tạo sodium phenolate.<br>3. Acetic acid: carboxylic acid phản ứng trung hòa NaOH tạo sodium acetate.<br>4. Methyl formate: ester phản ứng thủy phân trong dung dịch kiềm.<br>(Ethyl alcohol và benzene không phản ứng với dung dịch NaOH).<br>Vậy có tất cả 4 chất phản ứng."
        },
        {
            "id": 3,
            "question": "(Trích đề khảo sát chất lượng THPT lần 1.2025 – Thanh Hoá). Khi thủy phân không hoàn toàn pentapeptide A có công thức Val-Ala-Gly-Ala-Gly thì dung dịch thu được có tối đa bao nhiêu peptide có thể tham gia phản ứng màu biuret?",
            "answer": "6",
            "explanation": "Để tham gia phản ứng màu biuret, peptide phải có từ 2 liên kết peptide trở lên (tức là từ tripeptide trở lên). Khi thủy phân không hoàn toàn pentapeptide Val-Ala-Gly-Ala-Gly, các peptide có $\\ge 3$ mắt xích amino acid gồm:<br>- 1 pentapeptide: Val-Ala-Gly-Ala-Gly.<br>- 2 tetrapeptide: Val-Ala-Gly-Ala và Ala-Gly-Ala-Gly.<br>- 3 tripeptide: Val-Ala-Gly, Ala-Gly-Ala và Gly-Ala-Gly.<br>Tổng cộng có $1 + 2 + 3 = 6$ peptide tham gia phản ứng màu biuret (các dipeptide như Val-Ala, Ala-Gly, Gly-Ala không tham gia)."
        },
        {
            "id": 4,
            "question": "[Sở Tây Ninh-L1] Nhỏ dung dịch của mỗi chất: glycine, ethylamine, aniline, lysine, glutamic acid vào các mẩu giấy quỳ tím riêng rẽ. Có bao nhiêu dung dịch làm giấy quỳ tím chuyển thành màu xanh?",
            "answer": "2",
            "explanation": "Xét từng chất:<br>- Glycine: 1 nhóm $-\\text{NH}_2$, 1 nhóm $-\\text{COOH} \\rightarrow$ môi trường trung tính, không đổi màu quỳ.<br>- Ethylamine: amine no bậc I, tính base mạnh $\\rightarrow$ quỳ tím hóa xanh (1).<br>- Aniline: tính base cực yếu do vòng thơm hút electron $\\rightarrow$ không đổi màu quỳ.<br>- Lysine: 2 nhóm $-\\text{NH}_2$, 1 nhóm $-\\text{COOH} \\rightarrow$ tính base chiếm ưu thế, quỳ tím hóa xanh (2).<br>- Glutamic acid: 1 nhóm $-\\text{NH}_2$, 2 nhóm $-\\text{COOH} \\rightarrow$ tính acid chiếm ưu thế, quỳ tím hóa đỏ.<br>Vậy có đúng 2 dung dịch làm quỳ tím hóa xanh."
        },
        {
            "id": 5,
            "question": "(Cụm Đô Lương). Bột ngọt (monosodiumglutamate) là một loại gia vị, được sản xuất từ dung dịch NaOH 40% và tinh thể glutamic acid (chứa 81% khối lượng acid) bằng cách dùng dung dịch NaOH trung hòa dung dịch glutamic acid đến pH = 6,8. Sau đó đem lọc, cô đặc và kết tinh dung dịch sản phẩm bằng phương pháp sấy chân không ở nhiệt độ thấp. Bột ngọt thu được có độ tinh khiết 99%. Giả thiết hiệu suất của cả quá trình tính theo glutamic acid là 95%. Để thu được 1 tấn bột ngọt cần m tấn tinh thể glutamic acid. Tính m? (kết quả làm tròn đến phần trăm).",
            "answer": "1,12",
            "explanation": "Phương trình phản ứng: $\\text{C}_5\\text{H}_9\\text{NO}_4 + \\text{NaOH} \\rightarrow \\text{C}_5\\text{H}_8\\text{NO}_4\\text{Na} + \\text{H}_2\\text{O}$.<br>Khối lượng mol: Glutamic acid = $147\\text{ g/mol}$; Monosodium glutamate (MSG) = $169\\text{ g/mol}$.<br>Khối lượng MSG nguyên chất trong 1 tấn bột ngọt: $m_{\\text{MSG}} = 1 \\times 99\\% = 0,99\\text{ tấn}$.<br>Theo phương trình phản ứng, khối lượng glutamic acid lý thuyết cần dùng: $m_{\\text{glu (LT)}} = 0,99 \\times \\frac{147}{169} \\approx 0,8611\\text{ tấn}$.<br>Vì hiệu suất quá trình là 95% và tinh thể chỉ chứa 81% khối lượng acid, khối lượng tinh thể thực tế cần dùng là:<br>$$m = \\frac{0,8611}{0,95 \\times 0,81} = \\frac{1 \\times 0,99 \\times 147}{169 \\times 0,95 \\times 0,81} \\approx 1,12\\text{ tấn}.$$"
        },
        {
            "id": 6,
            "question": "(Sở Phú Thọ -L1). Để làm đậu phụ từ đậu tương, ban đầu người ta xay đậu tương với nước lọc và đun sôi. Sau đó, thêm nước chua vào dung dịch nước đậu tương đã được nấu chín, khi đó \"óc đậu\" sẽ bị kết tủa. Sau khi trải qua quá trình lọc, ép, chế biến, sẽ thu được thành phẩm đậu phụ. Nước chua có thể làm từ nước đậu phụ lên men hoặc giấm ăn. Để thu hồi đậu phụ nhanh và mịn, thay vì dùng nước chua để làm óc đậu, người ta có thể sử dụng thạch cao với hàm lượng an toàn với sức khỏe là không quá $1\\text{ g} / 1\\text{ kg}$ đậu phụ.<br>Cho các nhận xét sau:<br>(a) Nước chua có tính acid nên làm protein trong nước đậu bị đông tụ.<br>(b) Thành phần chính của thạch cao là calcium carbonate.<br>(c) Bản chất sự tạo thành \"óc đậu\" từ nước đậu có quá trình đông tụ protein.<br>(d) Nếu hàm lượng thạch cao vượt ngưỡng $1\\text{ g} / 1\\text{ kg}$ đậu phụ thì ảnh hưởng không tốt đến sức khỏe người tiêu dùng.<br>Có bao nhiêu nhận xét đúng?",
            "answer": "3",
            "explanation": "Xét các nhận xét:<br>(a) ĐÚNG. Nước chua chứa các acid hữu cơ (như acetic acid, lactic acid) làm thay đổi pH của dung dịch nước đậu về gần điểm đẳng điện của protein đậu nành, gây ra sự đông tụ protein.<br>(b) SAI. Thành phần chính của thạch cao là calcium sulfate ($\\text{CaSO}_4$), không phải calcium carbonate ($\\text{CaCO}_3$).<br>(c) ĐÚNG. Óc đậu chính là khối protein bị đông tụ và kết tủa dưới tác dụng của nhiệt độ và môi trường acid hoặc ion đa điện tích ($Ca^{2+}$).<br>(d) ĐÚNG. Thạch cao nếu dùng vượt ngưỡng an toàn quy định sẽ gây lắng đọng, tăng nguy cơ sỏi thận và ảnh hưởng tiêu cực tới sức khỏe người dùng.<br>Vậy có đúng 3 nhận xét đúng: (a), (c), (d)."
        }
    ]
}

# --- TẠO NỘI DUNG MARKDOWN (.md) ---
md_lines = [
    "# BỘ GIÁO DỤC VÀ ĐÀO TẠO - TRƯỜNG THPT",
    "## KỲ THI TỐT NGHIỆP TRUNG HỌC PHỔ THÔNG NĂM 2026",
    "### BÀI THI: KHOA HỌC TỰ NHIÊN - MÔN: HÓA HỌC",
    "### ĐỀ SỐ 3: ÔN TẬP TỚI HẾT CHƯƠNG 3 - HÓA HỌC 12",
    "*Thời gian làm bài: 50 phút (Không kể thời gian phát đề)*",
    "",
    "Họ và tên thí sinh: ................................................................. Số báo danh: .............................",
    "",
    "Cho biết nguyên tử khối: H = 1; C = 12; N = 14; O = 16; Na = 23; Mg = 24; S = 32; Cl = 35,5; K = 39; Ca = 40; Fe = 56; Cu = 64; Br = 80; Ag = 108; Ba = 137.",
    "",
    "---",
    "",
    "## MA TRẬN & BẢN ĐẶC TẢ ĐỀ KIỂM TRA",
    "",
    "| Chủ đề kiến thức | Nhận biết (Phần I) | Thông hiểu (Phần I + II) | Vận dụng (Phần II + III) | Tổng số lệnh hỏi | Điểm số |",
    "| :--- | :---: | :---: | :---: | :---: | :---: |",
    "| **Chương 1: Ester - Lipid** | 2 câu | 2 câu + 2 ý Đ/S | 2 ý Đ/S + 1 câu TLN | 9 | 2,75 |",
    "| **Chương 2: Carbohydrate** | 2 câu | 2 câu + 2 ý Đ/S | 2 ý Đ/S + 1 câu TLN | 9 | 2,75 |",
    "| **Chương 3: Hợp chất chứa Nitrogen** | 5 câu | 5 câu + 4 ý Đ/S | 4 ý Đ/S + 4 câu TLN | 22 | 4,50 |",
    "| **Tổng cộng** | **9 câu** | **15 câu / ý** | **16 câu / ý** | **40 lệnh hỏi** | **10,0 điểm** |",
    "",
    "---",
    "",
    "## PHẦN I. CÂU TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN (4,5 ĐIỂM)",
    "Thí sinh trả lời từ Câu 1 đến Câu 18. Mỗi câu hỏi thí sinh chỉ chọn một phương án. Mỗi câu trả lời đúng thí sinh được 0,25 điểm.",
    ""
]

for q in quiz_data["part1"]:
    if q['id'] == 11:
        md_lines.append("Câu 11: [Sở GD Hải Dương] Công thức của Tyrosine (Tyr) như hình sau:")
        md_lines.append("![](dau-ra/lop-12/de-kiem-tra/images/de3_p1_Image21.png)")
        md_lines.append("Phát biểu nào sau đây đúng?")
    else:
        clean_q = re.sub(r'<br\s*/?>', ' ', q['question'])
        md_lines.append(f"Câu {q['id']}: {clean_q}")
    for opt_k in ["A", "B", "C", "D"]:
        md_lines.append(f"{opt_k}. {q['options'][opt_k]}")
    md_lines.append("")

md_lines.extend([
    "---",
    "",
    "## PHẦN II. CÂU TRẮC NGHIỆM ĐÚNG / SAI (4,0 ĐIỂM)",
    "Thí sinh trả lời từ Câu 1 đến Câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.",
    "- Thí sinh chỉ lựa chọn chính xác 01 ý trong 01 câu được 0,10 điểm.",
    "- Thí sinh chỉ lựa chọn chính xác 02 ý trong 01 câu được 0,25 điểm.",
    "- Thí sinh chỉ lựa chọn chính xác 03 ý trong 01 câu được 0,50 điểm.",
    "- Thí sinh lựa chọn chính xác cả 04 ý trong 01 câu được 1,00 điểm.",
    ""
])

for q in quiz_data["part2"]:
    md_lines.append(f"Câu {q['id']}: {q['title']}")
    # Chuyển context sang Markdown chuẩn
    ctx_md = q['context']
    ctx_md = ctx_md.replace('<br>', '\n')
    ctx_md = ctx_md.replace('<em>', '*').replace('</em>', '*')
    # Bỏ các thẻ img base64 trong context md, thay bằng đường dẫn ảnh gốc
    if q['id'] == 1:
        ctx_md = re.sub(r'<table.*</table>', '', ctx_md, flags=re.DOTALL)
        md_lines.append(ctx_md.strip())
        md_lines.append("")
        md_lines.append("| Nồng độ NaOH (mol/L) | 4,0 | 3,6 | 3,2 | 2,8 | 2,4 | 2,0 |")
        md_lines.append("| :--- | :---: | :---: | :---: | :---: | :---: | :---: |")
        md_lines.append("| Thời gian hỗn hợp đồng nhất (phút) | 5,2 | 6,0 | 7,0 | 8,2 | 9,5 | 11,0 |")
    elif q['id'] == 2:
        md_lines.append(ctx_md.strip())
    elif q['id'] == 3:
        clean_ctx = re.sub(r'<div.*?>.*?</div>', '', ctx_md, flags=re.DOTALL)
        clean_ctx = re.sub(r'<table.*</table>', '', clean_ctx, flags=re.DOTALL)
        parts = clean_ctx.split("Hỗn hợp của dipeptide")
        md_lines.append(parts[0].strip())
        md_lines.append("![Dipeptide Phe-Tyr](dau-ra/lop-12/de-kiem-tra/images/de3_p3_Image43.jpg)")
        md_lines.append("")
        md_lines.append("Hỗn hợp của dipeptide " + parts[1].strip())
        md_lines.append("")
        md_lines.append("| Chất | Điện tích tại pH = 12 | Kích thước tương đối |")
        md_lines.append("| :--- | :---: | :---: |")
        md_lines.append("| Phe-Tyr | -2 | Lớn |")
        md_lines.append("| Tyr | -2 | Nhỏ |")
        md_lines.append("| Phe | -1 | Nhỏ |")
        md_lines.append("")
        md_lines.append("![Sơ đồ điện di](dau-ra/lop-12/de-kiem-tra/images/de3_p3_Image44.png)")
    elif q['id'] == 4:
        clean_ctx = re.sub(r'<div.*?>.*?</div>', '', ctx_md, flags=re.DOTALL)
        md_lines.append(clean_ctx.strip())
        md_lines.append("![Peptide A](dau-ra/lop-12/de-kiem-tra/images/de3_p3_Image45.png)")
    
    md_lines.append("")
    for stmt_k in ["a", "b", "c", "d"]:
        md_lines.append(f"{stmt_k}) {q['statements'][stmt_k]}")
    md_lines.append("")

md_lines.extend([
    "---",
    "",
    "## PHẦN III. CÂU TRẮC NGHIỆM TRẢ LỜI NGẮN (1,5 ĐIỂM)",
    "Thí sinh trả lời từ Câu 1 đến Câu 6. Mỗi câu trả lời đúng thí sinh được 0,25 điểm.",
    ""
])

for q in quiz_data["part3"]:
    clean_q = q['question'].replace('<br>', '\n')
    md_lines.append(f"Câu {q['id']}: {clean_q}")
    md_lines.append(f"Đáp số: {q['answer']}")
    md_lines.append("")

md_lines.extend([
    "---",
    "",
    "## ĐÁP ÁN VÀ HƯỚNG DẪN GIẢI CHI TIẾT",
    "",
    "### BẢNG ĐÁP ÁN PHẦN I",
    "| Câu | Đáp án | Câu | Đáp án | Câu | Đáp án |",
    "| :---: | :---: | :---: | :---: | :---: | :---: |",
    "| 1 | B | 7 | C | 13 | A |",
    "| 2 | A | 8 | D | 14 | B |",
    "| 3 | D | 9 | C | 15 | D |",
    "| 4 | A | 10 | B | 16 | A |",
    "| 5 | C | 11 | C | 17 | C |",
    "| 6 | A | 12 | D | 18 | C |",
    "",
    "### BẢNG ĐÁP ÁN PHẦN II",
    "| Câu | Lệnh hỏi | Đáp án (Đ/S) | Câu | Lệnh hỏi | Đáp án (Đ/S) |",
    "| :---: | :---: | :---: | :---: | :---: | :---: |",
    "| 1 | a | Đ | 3 | a | Đ |",
    "| 1 | b | Đ | 3 | b | S |",
    "| 1 | c | Đ | 3 | c | Đ |",
    "| 1 | d | S | 3 | d | Đ |",
    "| 2 | a | Đ | 4 | a | S |",
    "| 2 | b | S | 4 | b | Đ |",
    "| 2 | c | Đ | 4 | c | S |",
    "| 2 | d | Đ | 4 | d | Đ |",
    "",
    "### BẢNG ĐÁP ÁN PHẦN III",
    "| Câu | Lời giải tóm tắt | Đáp số |",
    "| :---: | :--- | :---: |",
    "| 1 | V = (500 * 92 / 162 * 0,60 / 0,8 / 0,05) = 4259,26 L -> 4259 L | 4259 |",
    "| 2 | Tripalmitin, phenol, acetic acid, methyl formate -> 4 chất | 4 |",
    "| 3 | 1 penta + 2 tetra + 3 tri = 6 peptide có phản ứng màu biuret | 6 |",
    "| 4 | Ethylamine và lysine làm quỳ tím hóa xanh -> 2 chất | 2 |",
    "| 5 | m = (1 * 0,99 * 147) / (169 * 0,95 * 0,81) = 1,12 tấn | 1,12 |",
    "| 6 | Các nhận xét đúng là (a), (c), (d) -> 3 nhận xét | 3 |",
    "",
    "---",
    "",
    "### LỜI GIẢI CHI TIẾT TỪNG CÂU",
    ""
])

md_lines.append("#### PHẦN I")
for q in quiz_data["part1"]:
    clean_exp = q['explanation'].replace('\\n', ' ').replace('<br>', ' ')
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
    clean_exp = q['explanation'].replace('\\n', ' ').replace('<br>', ' ')
    md_lines.append(f"Câu {q['id']}: Đáp số {q['answer']}. {clean_exp}")
    md_lines.append("")

# 1. Ghi file Markdown
md_path = os.path.join("dau-ra", "lop-12", "de-kiem-tra", "de-so-3-on-tap-den-chuong-3-hoa-hoc-12.md")
os.makedirs(os.path.dirname(md_path), exist_ok=True)
with open(md_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))
print(f"Đã tạo file Markdown: {md_path}")

# 2. Xuất file Word (.docx)
docx_path = os.path.join("dau-ra", "lop-12", "de-kiem-tra", "de-so-3-on-tap-den-chuong-3-hoa-hoc-12.docx")
create_styled_document(md_path, docx_path)
print(f"Đã tạo file Word (.docx): {docx_path}")

# 3. Xuất file Web tương tác (.html)
html_path = os.path.join("dau-ra", "lop-12", "de-kiem-tra", "de-so-3-on-tap-den-chuong-3-hoa-hoc-12.html")
generate_quiz_html(quiz_data, html_path)
print(f"Đã tạo file HTML trắc nghiệm online: {html_path}")

# 4. Lưu bản web vào thư mục lop-12/
web_path = os.path.join("lop-12", "de-so-3-on-tap-den-chuong-3.html")
os.makedirs("lop-12", exist_ok=True)
shutil.copy(html_path, web_path)
print(f"Đã tạo file HTML tại web root: {web_path}")

print("=== HOÀN TẤT XUẤT BẢN ĐỀ SỐ 3 ÔN TẬP TỚI HẾT CHƯƠNG 3 ===")
