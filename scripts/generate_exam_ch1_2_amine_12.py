"""
Script: generate_exam_ch1_2_amine_12.py
Purpose: Tạo bộ Đề ôn tập Hóa học 12: Chương 1, 2 và Chương 3 (đến phần Amine)
Quy chuẩn:
- Phần I: 18 câu trắc nghiệm nhiều lựa chọn (A, B, C, D)
- Phần II: 4 câu trắc nghiệm Đúng / Sai (a, b, c, d có ngữ cảnh thực tế & thí nghiệm, trong đó có 2 câu chứa 1 ý tính toán định lượng)
- Phần III: 6 câu trắc nghiệm Trả lời ngắn (tính toán, đếm số phát biểu)
- Phần IV: TUYỆT ĐỐI KHÔNG CÓ TỰ LUẬN (Chuẩn Lớp 12 Bộ GD&ĐT)
- Xuất đồng thời:
  1. File Markdown (.md)
  2. File Word (.docx) chuẩn A4, margins 2-2-2-1.5, Justified, số trang footer, không gạch đầu dòng đáp án
  3. File Web HTML (.html) chuẩn vatli102, đếm ngược 50 phút, MathJax, chấm điểm tự động, lời giải chi tiết, đồng bộ Google Sheet
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

quiz_data = {
    "title": "ĐỀ ÔN TẬP HÓA HỌC 12: CHƯƠNG 1, 2 VÀ CHƯƠNG 3 (ĐẾN AMINE)",
    "badge": "HÓA HỌC 12 - CHUẨN ĐỀ THI TỐT NGHIỆP THPT",
    "duration": 50,
    "grade": 12,
    "google_sheet_url": "https://script.google.com/macros/s/AKfycbwRRiM81mghvA7cInvJgb4rPLzWOAE3s44wer0BJcURQ4hWwoykS19pkNQ9LyzH6Q8lTQ/exec",
    "part1": [
        {
            "id": 1,
            "question": "Ester no, đơn chức, mạch hở có công thức phân tử $\\text{C}_2\\text{H}_4\\text{O}_2$ có tên gọi là",
            "options": {
                "A": "methyl formate.",
                "B": "ethyl formate.",
                "C": "methyl acetate.",
                "D": "acetic acid."
            },
            "answer": "A",
            "explanation": "Ester no, đơn chức, mạch hở có 2 nguyên tử carbon là $\\text{HCOOCH}_3$, có tên gọi là methyl formate. Công thức $\\text{CH}_3\\text{COOH}$ cũng có CTPT $\\text{C}_2\\text{H}_4\\text{O}_2$ nhưng thuộc loại carboxylic acid."
        },
        {
            "id": 2,
            "question": "Ở điều kiện phòng ($25^\\circ\\text{C}$), chất béo nào sau đây ở trạng thái lỏng?",
            "options": {
                "A": "Tristearin.",
                "B": "Triolein.",
                "C": "Tripalmitin.",
                "D": "Bơ thực vật đã hydrogen hóa."
            },
            "answer": "B",
            "explanation": "Triolein $[(\\text{C}_{17}\\text{H}_{33}\\text{COO})_3\\text{C}_3\\text{H}_5]$ chứa các gốc acid béo không no oleic acid (có 1 liên kết đôi $C=C$ dạng cis), làm giảm nhiệt độ nóng chảy (nóng chảy ở $-5^\\circ\\text{C}$) nên ở nhiệt độ phòng ($25^\\circ\\text{C}$) tồn tại ở thể lỏng. Tristearin và tripalmitin chứa gốc acid béo no nên là chất rắn."
        },
        {
            "id": 3,
            "question": "Đun nóng ethyl acetate ($\\text{CH}_3\\text{COOCH}_2\\text{CH}_3$) với dung dịch $\\text{NaOH}$ vừa đủ thu được alcohol nào sau đây?",
            "options": {
                "A": "Methanol ($\\text{CH}_3\\text{OH}$).",
                "B": "Ethanol ($\\text{C}_2\\text{H}_5\\text{OH}$).",
                "C": "Glycerol [$\\text{C}_3\\text{H}_5(\\text{OH})_3$].",
                "D": "Propan-1-ol ($\\text{C}_3\\text{H}_7\\text{OH}$)."
            },
            "answer": "B",
            "explanation": "Phản ứng xà phòng hóa: $\\text{CH}_3\\text{COOCH}_2\\text{CH}_3 + \\text{NaOH} \\xrightarrow{t^\\circ} \\text{CH}_3\\text{COONa} + \\text{C}_2\\text{H}_5\\text{OH}$. Alcohol thu được là ethanol."
        },
        {
            "id": 4,
            "question": "Isoamyl acetate là ester có mùi thơm quyến rũ của chuối chín, thường được dùng làm hương liệu thực phẩm. Công thức cấu tạo của isoamyl acetate là",
            "options": {
                "A": "$\\text{CH}_3\\text{COOCH}_2\\text{CH}_2\\text{CH}(\\text{CH}_3)_2$.",
                "B": "$\\text{HCOOCH}_2\\text{CH}_2\\text{CH}(\\text{CH}_3)_2$.",
                "C": "$\\text{CH}_3\\text{COOCH}(\\text{CH}_3)\\text{CH}_2\\text{CH}_2\\text{CH}_3$.",
                "D": "$\\text{CH}_3\\text{COOCH}_2\\text{CH}(\\text{CH}_3)_2$."
            },
            "answer": "A",
            "explanation": "Gốc acetate là $\\text{CH}_3\\text{COO}-$, gốc isoamyl là $-\\text{CH}_2\\text{CH}_2\\text{CH}(\\text{CH}_3)_2$. Do đó, công thức của isoamyl acetate là $\\text{CH}_3\\text{COOCH}_2\\text{CH}_2\\text{CH}(\\text{CH}_3)_2$."
        },
        {
            "id": 5,
            "question": "Thành phần giặt rửa chính của xà phòng truyền thống là",
            "options": {
                "A": "muối sodium hoặc potassium của acid béo.",
                "B": "muối sodium của alkylbenzenesulfonic acid.",
                "C": "ester của glycerol với nitric acid.",
                "D": "hỗn hợp các alkane chuỗi dài."
            },
            "answer": "A",
            "explanation": "Xà phòng truyền thống thu được từ phản ứng xà phòng hóa chất béo với kiềm ($\text{NaOH}$ hoặc $\text{KOH}$), thành phần hoạt động bề mặt chính là muối sodium hoặc potassium của các acid béo chuỗi dài như sodium stearate, sodium palmitate, sodium oleate."
        },
        {
            "id": 6,
            "question": "Để chuyển hóa chất béo lỏng (dầu thực vật) thành chất béo rắn (bơ thực vật, shortening) tiện lợi cho bảo quản và làm bánh, người ta sử dụng phản ứng nào sau đây?",
            "options": {
                "A": "Hydrogen hóa (cộng $\\text{H}_2$, xúc tác $\\text{Ni}$, $t^\\circ$).",
                "B": "Xà phòng hóa trong dung dịch kiềm.",
                "C": "Thủy phân trong môi trường acid vô cơ.",
                "D": "Oxy hóa bằng dung dịch $\\text{KMnO}_4$."
            },
            "answer": "A",
            "explanation": "Phản ứng hydrogen hóa làm no các liên kết đôi $C=C$ chưa bão hòa trong gốc acid béo của chất béo lỏng: $(\\text{C}_{17}\\text{H}_{33}\\text{COO})_3\\text{C}_3\\text{H}_5 + 3\\text{H}_2 \\xrightarrow{\\text{Ni}, t^\\circ} (\\text{C}_{17}\\text{H}_{35}\\text{COO})_3\\text{C}_3\\text{H}_5$. Sản phẩm là chất béo no ở dạng rắn."
        },
        {
            "id": 7,
            "question": "Carbohydrate nào sau đây thuộc loại monosaccharide?",
            "options": {
                "A": "Glucose.",
                "B": "Saccharose.",
                "C": "Tinh bột.",
                "D": "Cellulose."
            },
            "answer": "A",
            "explanation": "Monosaccharide là carbohydrate đơn giản nhất không thể thủy phân được, tiêu biểu là glucose và fructose. Saccharose là disaccharide; tinh bột và cellulose là polysaccharide."
        },
        {
            "id": 8,
            "question": "Dung dịch chất nào sau đây hòa tan được $\\text{Cu(OH)}_2$ ở nhiệt độ phòng tạo thành dung dịch phức đồng màu xanh lam đậm đặc trưng?",
            "options": {
                "A": "Glucose.",
                "B": "Ethanol.",
                "C": "Ethyl acetate.",
                "D": "Benzaldehyde."
            },
            "answer": "A",
            "explanation": "Glucose phân tử có 5 nhóm hydroxy ($-OH$) kề nhau, có tính chất của polyalcohol (polyol) liền kề nên hòa tan được $\\text{Cu(OH)}_2$ ở nhiệt độ thường tạo phức chất đồng(II) có màu xanh lam đậm."
        },
        {
            "id": 9,
            "question": "Thuốc thử đặc trưng dùng để nhận biết hồ tinh bột bằng phản ứng tạo màu xanh tím ở nhiệt độ phòng là",
            "options": {
                "A": "dung dịch iodine ($\\text{I}_2$).",
                "B": "dung dịch $\\text{AgNO}_3$ trong $\\text{NH}_3$.",
                "C": "dung dịch $\\text{Cu(OH)}_2$ trong $\\text{NaOH}$.",
                "D": "nước bromine."
            },
            "answer": "A",
            "explanation": "Phân tử amylose trong tinh bột có dạng xoắn hình lò xo. Khi cho dung dịch iodine vào, các phân tử iodine len lỏi vào trong lòng ống xoắn tạo phức chất hấp thụ ánh sáng có màu xanh tím. Khi đun nóng màu xanh tím biến mất, để nguội màu xanh tím xuất hiện trở lại."
        },
        {
            "id": 10,
            "question": "Cellulose là polymer thiên nhiên mạch không phân nhánh được tạo nên bởi các mắt xích nào sau đây?",
            "options": {
                "A": "$\\beta$-glucose liên kết với nhau qua liên kết $\\beta$-1,4-glycosidic.",
                "B": "$\\alpha$-glucose liên kết với nhau qua liên kết $\\alpha$-1,4-glycosidic.",
                "C": "$\\alpha$-glucose liên kết với nhau qua liên kết $\\alpha$-1,6-glycosidic.",
                "D": "$\\beta$-fructose liên kết với nhau qua liên kết $\\beta$-2,1-glycosidic."
            },
            "answer": "A",
            "explanation": "Cellulose có cấu tạo mạch thẳng kéo dài không phân nhánh, gồm nhiều mắt xích $\\beta$-D-glucose liên kết với nhau bởi các liên kết $\\beta$-1,4-glycosidic. Liên kết $\\alpha$-1,4 và $\\alpha$-1,6 có trong cấu trúc tinh bột (amylose và amylopectin)."
        },
        {
            "id": 11,
            "question": "Phát biểu nào sau đây đúng về saccharose ($\\text{C}_{12}\\text{H}_{22}\\text{O}_{11}$)?",
            "options": {
                "A": "Saccharose tham gia phản ứng tráng bạc với thuốc thử Tollens.",
                "B": "Thủy phân hoàn toàn saccharose trong môi trường acid chỉ thu được glucose.",
                "C": "Phân tử saccharose cấu tạo từ một gốc $\\alpha$-glucose và một gốc $\\beta$-fructose liên kết qua nguyên tử oxygen.",
                "D": "Saccharose là một polysaccharide chiếm tỉ lệ lớn trong bông nõn."
            },
            "answer": "C",
            "explanation": "Saccharose là disaccharide tạo bởi một gốc $\\alpha$-glucose và một gốc $\\beta$-fructose liên kết qua liên kết $\\alpha,\\beta$-1,2-glycosidic. Do liên kết này đã khóa các nhóm hemiacetal/hemiketal nên saccharose không có nhóm formyl tự do, không tráng bạc. Khi thủy phân saccharose thu được hỗn hợp gồm cả glucose và fructose."
        },
        {
            "id": 12,
            "question": "Trong y tế, dung dịch chất nào sau đây có nồng độ 5% được dùng làm dịch truyền tĩnh mạch trực tiếp nhằm hồi phục sức khỏe nhanh chóng cho người bệnh suy nhược?",
            "options": {
                "A": "Glucose.",
                "B": "Fructose.",
                "C": "Saccharose.",
                "D": "Maltose."
            },
            "answer": "A",
            "explanation": "Glucose là chất dinh dưỡng thiết yếu cung cấp năng lượng trực tiếp cho tế bào mà không cần qua quá trình thủy phân phức tạp. Dung dịch glucose 5% là dung dịch đẳng trương với máu người, được truyền trực tiếp qua tĩnh mạch để bù nước và nạp năng lượng khẩn cấp cho bệnh nhân."
        },
        {
            "id": 13,
            "question": "Hợp chất hữu cơ nào sau đây thuộc loại amine bậc hai?",
            "options": {
                "A": "$\\text{CH}_3\\text{NH}_2$.",
                "B": "$\\text{CH}_3-\\text{NH}-\\text{C}_2\\text{H}_5$.",
                "C": "$(\\text{CH}_3)_3\\text{N}$.",
                "D": "$\\text{C}_6\\text{H}_5\\text{NH}_2$."
            },
            "answer": "B",
            "explanation": "Bậc của amine là số nguyên tử hydrogen trong phân tử $\\text{NH}_3$ được thay thế bởi gốc hydrocarbon. $\\text{CH}_3-\\text{NH}-\\text{C}_2\\text{H}_5$ (ethylmethylamine) có nguyên tử N liên kết với 2 gốc hydrocarbon nên là amine bậc hai. $\\text{CH}_3\\text{NH}_2$ và $\\text{C}_6\\text{H}_5\\text{NH}_2$ là amine bậc một; $(\\text{CH}_3)_3\\text{N}$ là amine bậc ba."
        },
        {
            "id": 14,
            "question": "Amine có công thức cấu tạo thu gọn $\\text{CH}_3\\text{CH}_2\\text{NH}_2$ có tên thay thế (theo danh pháp IUPAC) là",
            "options": {
                "A": "ethylamine.",
                "B": "ethanamine.",
                "C": "dimethylamine.",
                "D": "aminoethane."
            },
            "answer": "B",
            "explanation": "Theo IUPAC: Tên thay thế của amine đơn chức mạch hở = Tên alkane tương ứng + amine (bỏ chữ e cuối nếu có) $\\rightarrow$ ethanamine. 'Ethylamine' là tên gốc - chức."
        },
        {
            "id": 15,
            "question": "Ở điều kiện thường ($25^\\circ\\text{C}$, 1 bar), chất nào sau đây là chất lỏng, hầu như không tan trong nước và chìm xuống đáy ống nghiệm?",
            "options": {
                "A": "Methylamine ($\\text{CH}_3\\text{NH}_2$).",
                "B": "Ethylamine ($\\text{C}_2\\text{H}_5\\text{NH}_2$).",
                "C": "Aniline ($\\text{C}_6\\text{H}_5\\text{NH}_2$).",
                "D": "Dimethylamine [$(\\text{CH}_3)_2\\text{NH}$]."
            },
            "answer": "C",
            "explanation": "Methylamine, dimethylamine, trimethylamine và ethylamine là những chất khí ở điều kiện thường, tan rất nhiều trong nước. Aniline ($\\text{C}_6\\text{H}_5\\text{NH}_2$) là chất lỏng không màu (để lâu chuyển màu nâu đen do bị oxy hóa bởi không khí), rất ít tan trong nước, có khối lượng riêng lớn hơn nước ($D \\approx 1,02\\text{ g/mL}$) nên chìm xuống đáy."
        },
        {
            "id": 16,
            "question": "Dãy nào sau đây sắp xếp các chất theo chiều lực base giảm dần?",
            "options": {
                "A": "$(\\text{CH}_3)_2\\text{NH} > \\text{CH}_3\\text{NH}_2 > \\text{NH}_3 > \\text{C}_6\\text{H}_5\\text{NH}_2$.",
                "B": "$\\text{C}_6\\text{H}_5\\text{NH}_2 > \\text{NH}_3 > \\text{CH}_3\\text{NH}_2 > (\\text{CH}_3)_2\\text{NH}$.",
                "C": "$(\\text{CH}_3)_2\\text{NH} > \\text{C}_6\\text{H}_5\\text{NH}_2 > \\text{CH}_3\\text{NH}_2 > \\text{NH}_3$.",
                "D": "$\\text{CH}_3\\text{NH}_2 > (\\text{CH}_3)_2\\text{NH} > \\text{NH}_3 > \\text{C}_6\\text{H}_5\\text{NH}_2$."
            },
            "answer": "A",
            "explanation": "Nhóm alkyl (methyl) đẩy electron (+I) làm tăng mật độ electron trên nguyên tử N, làm tăng lực base: $(\\text{CH}_3)_2\\text{NH} > \\text{CH}_3\\text{NH}_2 > \\text{NH}_3$. Gốc phenyl hút electron (-C) làm giảm mạnh mật độ electron trên N, khiến tính base của aniline yếu hơn ammonia: $\\text{NH}_3 > \\text{C}_6\\text{H}_5\\text{NH}_2$."
        },
        {
            "id": 17,
            "question": "Mùi tanh đặc trưng của cá nước ngọt chủ yếu do các amine gây ra (tiêu biểu là trimethylamine). Để khử mùi tanh của cá trước khi nấu, phương pháp dân gian khoa học và hiệu quả nhất là",
            "options": {
                "A": "ngâm cá trong nước vôi trong [$\\text{Ca(OH)}_2$].",
                "B": "rửa cá bằng giấm ăn hoặc nước cốt chanh.",
                "C": "rửa cá bằng dung dịch baking soda ($\\text{NaHCO}_3$).",
                "D": "ngâm cá trong nước xà phòng loãng."
            },
            "answer": "B",
            "explanation": "Các amine gây mùi tanh có tính base. Giấm ăn chứa acetic acid ($\\text{CH}_3\\text{COOH}$) hoặc chanh chứa citric acid phản ứng trung hòa các amine tạo thành muối tan, không bay hơi và dễ bị rửa trôi theo dòng nước, làm mất hoàn toàn mùi tanh."
        },
        {
            "id": 18,
            "question": "Nhỏ dung dịch nitrous acid ($\\text{HNO}_2$) vào ống nghiệm chứa ethylamine ($\\text{CH}_3\\text{CH}_2\\text{NH}_2$) ở nhiệt độ thường, hiện tượng quan sát được là",
            "options": {
                "A": "xuất hiện kết tủa trắng.",
                "B": "có bọt khí không màu thoát ra.",
                "C": "dung dịch chuyển sang màu xanh thẫm.",
                "D": "xuất hiện kết tủa màu vàng cam."
            },
            "answer": "B",
            "explanation": "Amine bậc 1 mạch no (như ethylamine) phản ứng với nitrous acid ($\\text{HNO}_2$) sinh ra alcohol tương ứng, giải phóng bọt khí nitrogen ($\\text{N}_2$): $\\text{C}_2\\text{H}_5\\text{NH}_2 + \\text{HNO}_2 \\rightarrow \\text{C}_2\\text{H}_5\\text{OH} + \\text{N}_2 \\uparrow + \\text{H}_2\\text{O}$."
        }
    ],
    "part2": [
        {
            "id": 1,
            "title": "Thí nghiệm điều chế ethyl acetate trong phòng thí nghiệm",
            "context": "Tiến hành thí nghiệm điều chế ethyl acetate theo các bước thực nghiệm sau:<br><div style='text-align:center; margin: 12px 0;'><img src='" + b64_ethyl + "' style='max-width: 100%; max-height: 280px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);' alt='Thí nghiệm điều chế ethyl acetate'></div>- Bước 1: Cho vào ống nghiệm sạch 6,0 gam $\\text{CH}_3\\text{COOH}$ nguyên chất, 4,6 gam $\\text{C}_2\\text{H}_5\\text{OH}$ khan và vài giọt dung dịch $\\text{H}_2\\text{SO}_4$ đặc, lắc đều.<br>- Bước 2: Đặt ống nghiệm vào cốc nước nóng có nhiệt độ $65^\\circ\\text{C} - 70^\\circ\\text{C}$ trong khoảng 5 - 7 phút.<br>- Bước 3: Làm lạnh ống nghiệm dưới vòi nước, sau đó rót từ từ 2 mL dung dịch $\\text{NaCl}$ bão hòa vào ống nghiệm.",
            "statements": {
                "a": "Dung dịch $\\text{H}_2\\text{SO}_4$ đặc đóng vai trò vừa làm chất xúc tác cho phản ứng, vừa hút nước làm dịch chuyển cân bằng về phía tạo ester.",
                "b": "Thêm dung dịch $\\text{NaCl}$ bão hòa ở bước 3 nhằm mục đích làm tăng khối lượng riêng của lớp chất lỏng phía dưới, giúp ethyl acetate nhẹ hơn nổi lên trên và tách lớp rõ nét.",
                "c": "Để phản ứng diễn ra nhanh hơn và đạt hiệu suất cao nhất, có thể đun sôi hỗn hợp trực tiếp trên ngọn lửa đèn cồn ở nhiệt độ cao trên $150^\\circ\\text{C}$.",
                "d": "Giả sử sau bước 2, phản ứng este hóa đạt hiệu suất 60%, khối lượng ethyl acetate thu được là 5,28 gam."
            },
            "answers": {
                "a": "Đ",
                "b": "Đ",
                "c": "S",
                "d": "Đ"
            },
            "explanations": {
                "a": "Đúng. $\\text{H}_2\\text{SO}_4$ đặc cung cấp ion $H^+$ làm xúc tác phản ứng thuận nghịch este hóa và có tính háo nước cực mạnh, hấp thụ $\\text{H}_2\\text{O}$ sinh ra, làm cân bằng chuyển dịch theo chiều thuận.",
                "b": "Đúng. Dung dịch $\\text{NaCl}$ bão hòa có khối lượng riêng lớn ($D \\approx 1,2\\text{ g/mL}$) và làm giảm độ tan của ethyl acetate trong nước (hiệu ứng 'muối tích'), giúp lớp ester tách riêng biệt nổi lên trên.",
                "c": "Sai. Ethanol (nhiệt độ sôi $78,3^\\circ\\text{C}$) và ethyl acetate (nhiệt độ sôi $77,1^\\circ\\text{C}$) đều là các chất lỏng dễ bay hơi và dễ bắt lửa. Nếu đun sôi trực tiếp ở nhiệt độ cao, các chất sẽ bay hơi thoát ra ngoài làm hao hụt sản phẩm, giảm hiệu suất và có nguy cơ hỏa hoạn.",
                "d": "Đúng. Ta có:<br>$n_{\\text{CH}_3\\text{COOH}} = \\frac{6,0}{60} = 0,1\\text{ mol}$; $n_{\\text{C}_2\\text{H}_5\\text{OH}} = \\frac{4,6}{46} = 0,1\\text{ mol}$.<br>Phương trình phản ứng: $\\text{CH}_3\\text{COOH} + \\text{C}_2\\text{H}_5\\text{OH} \\xrightleftharpoons{\\text{H}_2\\text{SO}_4, t^\\circ} \\text{CH}_3\\text{COOC}_2\\text{H}_5 + \\text{H}_2\\text{O}$.<br>Theo lý thuyết: $n_{\\text{ester (LT)}} = 0,1\\text{ mol} \\Rightarrow m_{\\text{ester (LT)}} = 0,1 \\times 88 = 8,8\\text{ gam}$.<br>Với hiệu suất phản ứng 60%: $m_{\\text{ester (TT)}} = 8,8 \\times 60\\% = 5,28\\text{ gam}$."
            }
        },
        {
            "id": 2,
            "title": "Sản xuất và chuyển hóa carbohydrate trong thực tiễn đời sống và công nghiệp",
            "context": "Trong công nghiệp sản xuất xăng sinh học E5 và ngành thực phẩm, tinh bột và cellulose là hai nguồn nguyên liệu sinh khối vô cùng phong phú. Quá trình chuyển hóa sinh hóa bao gồm thủy phân tinh bột trong hạt ngô hoặc sắn thành glucose nhờ enzyme amylase, sau đó lên men glucose thành ethanol nhờ nấm men (yeast) ở điều kiện yếm khí (kị khí):<br>$$\\text{Tinh bột } (\\text{C}_6\\text{H}_{10}\\text{O}_5)_n \\xrightarrow{+\\text{H}_2\\text{O}, \\text{ enzyme}} n\\text{C}_6\\text{H}_{12}\\text{O}_6 \\text{ (glucose)}$$$$\\text{C}_6\\text{H}_{12}\\text{O}_6 \\xrightarrow{\\text{men rượu}, 30-35^\\circ\\text{C}} 2\\text{C}_2\\text{H}_5\\text{OH} + 2\\text{CO}_2 \\uparrow$$",
            "statements": {
                "a": "Tinh bột trong tự nhiên tồn tại dưới hai dạng cấu trúc phân tử: amylose (mạch không phân nhánh) và amylopectin (mạch phân nhánh).",
                "b": "Trong giai đoạn lên men glucose thành ethanol, cần sục liên tục khí oxygen vào bồn lên men để nấm men hô hấp hiếu khí tạo ra lượng ethanol tối đa.",
                "c": "Dung dịch glucose thu được sau khi thủy phân tinh bột có khả năng tham gia phản ứng tráng bạc khi đun nóng nhẹ với thuốc thử Tollens.",
                "d": "Từ 1 tấn hạt ngô chứa 64,8% tinh bột về khối lượng (các chất còn lại không tạo ethanol), với hiệu suất toàn bộ quá trình đạt 75%, khối lượng ethanol sinh học thu được là 276 kg."
            },
            "answers": {
                "a": "Đ",
                "b": "S",
                "c": "Đ",
                "d": "Đ"
            },
            "explanations": {
                "a": "Đúng. Tinh bột gồm amylose (chiếm khoảng 20-30%, cấu trúc mạch xoắn không phân nhánh liên kết qua $\\alpha$-1,4-glycosidic) và amylopectin (chiếm 70-80%, cấu trúc phân nhánh liên kết qua cả $\\alpha$-1,4 và $\\alpha$-1,6-glycosidic).",
                "b": "Sai. Lên men rượu là quá trình sinh học kị khí (không có oxygen). Nếu sục oxygen, nấm men sẽ chuyển sang hô hấp hiếu khí tạo $\\text{CO}_2$ và $\\text{H}_2\\text{O}$, hoặc vi khuẩn acetic sẽ oxy hóa ethanol thành acetic acid (bị chua hóa), làm mất sản phẩm ethanol.",
                "c": "Đúng. Glucose chứa nhóm formyl ($-CHO$) nên có tính khử mạnh, khử ion $\\text{Ag}^+$ trong thuốc thử Tollens $[\\text{Ag}(\\text{NH}_3)_2]\\text{OH}$ tạo lớp tráng bạc kim loại sáng bóng.",
                "d": "Đúng. Khối lượng tinh bột nguyên chất trong 1 tấn (1000 kg) hạt ngô là: $m_{\\text{tinh bột}} = 1000 \\times 64,8\\% = 648\\text{ kg}$.<br>Sơ đồ chuyển hóa: $(\\text{C}_6\\text{H}_{10}\\text{O}_5)_n \\rightarrow 2n\\text{C}_2\\text{H}_5\\text{OH}$.<br>Cứ 162 kg tinh bột theo lý thuyết tạo ra $2 \\times 46 = 92\\text{ kg}$ ethanol.<br>Khối lượng ethanol lý thuyết: $m_{\\text{LT}} = \\frac{648 \\times 92}{162} = 4 \\times 92 = 368\\text{ kg}$.<br>Do hiệu suất toàn bộ quá trình đạt 75%, khối lượng ethanol thực tế thu được là: $m_{\\text{TT}} = 368 \\times 75\\% = 276\\text{ kg}$."
            }
        },
        {
            "id": 3,
            "title": "Khảo sát tính chất vật lí và hóa học của aniline",
            "context": "Aniline ($\\text{C}_6\\text{H}_5\\text{NH}_2$) là một amine thơm đơn chức quan trọng, được sử dụng rộng rãi trong tổng hợp phẩm nhuộm azo, dược phẩm (như paracetamol) và chất tăng tốc lưu hóa cao su. Tiến hành chuỗi thí nghiệm khảo sát tính chất của aniline như sau:<br>- Thí nghiệm 1: Cho 1 mL aniline vào ống nghiệm chứa 3 mL nước cất, lắc mạnh rồi để yên.<br>- Thí nghiệm 2: Thêm tiếp 2 mL dung dịch $\\text{HCl}$ 1M vào ống nghiệm sau thí nghiệm 1, lắc đều.<br>- Thí nghiệm 3: Rót từ từ dung dịch $\\text{NaOH}$ 1M vào ống nghiệm sau thí nghiệm 2 cho đến khi dư kiềm.<br>- Thí nghiệm 4: Cho 1 mL aniline vào ống nghiệm mới, sau đó nhỏ từ từ nước bromine vào.",
            "statements": {
                "a": "Ở thí nghiệm 1, aniline hầu như không tan trong nước cất, tạo nhũ tương đục và chìm xuống đáy ống nghiệm vì khối lượng riêng của aniline lớn hơn nước.",
                "b": "Ở thí nghiệm 2, hỗn hợp trở nên trong suốt, đồng nhất do aniline đã phản ứng với $\\text{HCl}$ tạo thành muối phenylammonium chloride ($\\text{C}_6\\text{H}_5\\text{NH}_3\\text{Cl}$) tan tốt trong nước.",
                "c": "Ở thí nghiệm 3, dung dịch vẫn giữ nguyên trạng thái trong suốt do không có phản ứng hóa học nào xảy ra giữa muối amine và dung dịch base mạnh.",
                "d": "Ở thí nghiệm 4, nước bromine bị mất màu và xuất hiện kết tủa trắng của 2,4,6-tribromoaniline do nhóm amino ($-NH_2$) làm tăng mật độ electron ở vị trí ortho và para của vòng benzene."
            },
            "answers": {
                "a": "Đ",
                "b": "Đ",
                "c": "S",
                "d": "Đ"
            },
            "explanations": {
                "a": "Đúng. Do gốc phenyl ($\\text{C}_6\\text{H}_5-$) kị nước lớn nên aniline rất ít tan trong nước ($D = 1,02\\text{ g/mL} > 1\\text{ g/mL}$), phân lớp và chìm xuống đáy.",
                "b": "Đúng. Aniline thể hiện tính base yếu, tác dụng với acid mạnh: $\\text{C}_6\\text{H}_5\\text{NH}_2 + \\text{HCl} \\rightarrow \\text{C}_6\\text{H}_5\\text{NH}_3\\text{Cl}$. Muối ion này tan rất tốt trong nước tạo dung dịch đồng nhất trong suốt.",
                "c": "Sai. Vì $\\text{NaOH}$ là base mạnh hơn tính base của aniline nên sẽ đẩy amine yếu ra khỏi muối: $\\text{C}_6\\text{H}_5\\text{NH}_3\\text{Cl} + \\text{NaOH} \\rightarrow \\text{C}_6\\text{H}_5\\text{NH}_2 + \\text{NaCl} + \\text{H}_2\\text{O}$. Aniline tự do không tan trong nước lại bị tách ra làm dung dịch vẩn đục trở lại.",
                "d": "Đúng. Đôi electron tự do trên nguyên tử N liên hợp với hệ electron $\\pi$ của vòng benzene làm tăng mật độ electron tại các vị trí ortho và para, giúp phản ứng thế với bromine diễn ra rất dễ dàng ở điều kiện thường tạo kết tủa trắng 2,4,6-tribromoaniline."
            }
        },
        {
            "id": 4,
            "title": "Phân biệt và nhận biết các hợp chất hữu cơ bằng phương pháp hóa học",
            "context": "Có 4 lọ hóa chất mất nhãn đựng 4 chất lỏng hoặc dung dịch riêng biệt: Ethyl acetate ($\\text{CH}_3\\text{COOCH}_2\\text{CH}_3$), Glucose ($\\text{C}_6\\text{H}_{12}\\text{O}_6$ 2%), Glycerol [$\\text{C}_3\\text{H}_5(\\text{OH})_3$], và Dimethylamine [$(\\text{CH}_3)_2\\text{NH}$]. Một học sinh thiết kế quy trình thực nghiệm nhận biết gồm 3 bước:<br>- Bước 1: Nhúng giấy quỳ tím vào 4 mẫu thử.<br>- Bước 2: Với các mẫu thử không làm đổi màu quỳ tím, cho lần lượt tác dụng với $\\text{Cu(OH)}_2$ ở nhiệt độ phòng.<br>- Bước 3: Đun nóng nhẹ các hỗn hợp thu được ở bước 2 xuất hiện phức màu xanh lam đậm.",
            "statements": {
                "a": "Sau bước 1, mẫu thử duy nhất làm quỳ tím chuyển sang màu xanh là dung dịch dimethylamine do amine này có tính base mạnh.",
                "b": "Ở bước 2, ethyl acetate có thể hòa tan được $\\text{Cu(OH)}_2$ ở nhiệt độ phòng tạo dung dịch màu xanh lam đặc trưng.",
                "c": "Ở bước 3, mẫu thử tạo kết tủa đỏ gạch $\\text{Cu}_2\\text{O}$ khi đun nóng là dung dịch glucose, mẫu còn lại giữ nguyên màu xanh lam là glycerol.",
                "d": "Bằng quy trình 3 bước thực nghiệm trên, người ta hoàn toàn có thể phân biệt và nhận biết chính xác cả 4 lọ mất nhãn."
            },
            "answers": {
                "a": "Đ",
                "b": "S",
                "c": "Đ",
                "d": "Đ"
            },
            "explanations": {
                "a": "Đúng. Dimethylamine là aliphatic secondary amine, có tính base mạnh hơn ammonia, trong dung dịch điện li yếu tạo ion $\\text{OH}^-$ làm quỳ tím chuyển màu xanh.",
                "b": "Sai. Ethyl acetate là ester, không có các nhóm hydroxy liền kề nên hoàn toàn không phản ứng và không hòa tan được $\\text{Cu(OH)}_2$ ở nhiệt độ thường.",
                "c": "Đúng. Glucose có nhóm formyl ($-CHO$) nên khi đun nóng với $\\text{Cu(OH)}_2$ trong môi trường kiềm sẽ bị oxy hóa thành muối gluconate đồng thời khử $\\text{Cu(II)}$ thành kết tủa đỏ gạch $\\text{Cu}_2\\text{O}$. Glycerol không có nhóm aldehyde nên chỉ giữ nguyên màu xanh lam của phức đồng(II) glycerol.",
                "d": "Đúng. Bước 1 nhận ra dimethylamine (quỳ hóa xanh). Bước 2 nhận ra ethyl acetate (không hòa tan $\\text{Cu(OH)}_2$). Bước 3 đun nóng phân biệt được glucose (kết tủa đỏ gạch) và glycerol (không có kết tủa đỏ gạch)."
            }
        }
    ],
    "part3": [
        {
            "id": 1,
            "question": "Thủy phân hoàn toàn 17,6 gam ethyl acetate ($\\text{CH}_3\\text{COOCH}_2\\text{CH}_3$) bằng 250 mL dung dịch $\\text{NaOH}$ 1M, đun nóng. Sau khi các phản ứng xảy ra hoàn toàn, cô cạn dung dịch đến khối lượng không đổi thu được $m$ gam chất rắn khan. Giá trị của $m$ là bao nhiêu?",
            "answer": "18,4",
            "explanation": "Ta có:<br>$n_{\\text{ester}} = \\frac{17,6}{88} = 0,2\\text{ mol}$; $n_{\\text{NaOH}} = 0,25 \\times 1 = 0,25\\text{ mol}$.<br>Phương trình phản ứng: $\\text{CH}_3\\text{COOCH}_2\\text{CH}_3 + \\text{NaOH} \\rightarrow \\text{CH}_3\\text{COONa} + \\text{C}_2\\text{H}_5\\text{OH}$.<br>Do $0,2 < 0,25$ nên $\\text{NaOH}$ còn dư sau phản ứng: $n_{\\text{NaOH dư}} = 0,25 - 0,2 = 0,05\\text{ mol}$.<br>Chất rắn khan thu được gồm muối $\\text{CH}_3\\text{COONa}$ (0,2 mol) và $\\text{NaOH dư}$ (0,05 mol):<br>$m = 0,2 \\times 82 + 0,05 \\times 40 = 16,4 + 2,0 = 18,4\\text{ gam}$."
        },
        {
            "id": 2,
            "question": "Acid béo omega-6 là loại acid béo không no thiết yếu đối với hoạt động trí não và tim mạch, có liên kết đôi đầu tiên ở vị trí carbon số 6 khi đánh số từ nhóm methyl ($-CH_3$) ở đầu mạch carbon. Linoleic acid (một acid béo omega-6) có công thức cấu tạo thu gọn:<br>$$\\text{CH}_3-(\\text{CH}_2)_4-\\text{CH}=\\text{CH}-\\text{CH}_2-\\text{CH}=\\text{CH}-(\\text{CH}_2)_7-\\text{COOH}$$Trong một phân tử linoleic acid có bao nhiêu liên kết đôi giữa các nguyên tử carbon ($C=C$)?",
            "answer": "2",
            "explanation": "Quan sát công thức cấu tạo của linoleic acid: $\\text{CH}_3-(\\text{CH}_2)_4-\\text{CH}=\\text{CH}-\\text{CH}_2-\\text{CH}=\\text{CH}-(\\text{CH}_2)_7-\\text{COOH}$.<br>Phân tử có 2 liên kết đôi $C=C$ (tại các vị trí giữa C số 6 với C số 7, và C số 9 với C số 10 khi đánh số từ nhóm methyl đầu mạch). Đáp số là 2."
        },
        {
            "id": 3,
            "question": "Cho 360 gam glucose ($\\text{C}_6\\text{H}_{12}\\text{O}_6$) lên men rượu với hiệu suất của toàn bộ quá trình đạt 75%. Toàn bộ lượng khí $\\text{CO}_2$ sinh ra được hấp thụ hoàn toàn vào dung dịch nước vôi trong [$\\text{Ca(OH)}_2$] dư, thu được $m$ gam kết tủa trắng. Giá trị của $m$ là bao nhiêu?",
            "answer": "300",
            "explanation": "Ta có: $n_{\\text{glucose}} = \\frac{360}{180} = 2,0\\text{ mol}$.<br>Phương trình phản ứng lên men rượu: $\\text{C}_6\\text{H}_{12}\\text{O}_6 \\xrightarrow{\\text{men}} 2\\text{C}_2\\text{H}_5\\text{OH} + 2\\text{CO}_2$.<br>Lượng $\\text{CO}_2$ sinh ra theo lý thuyết: $n_{\\text{CO}_2\\text{ (LT)}} = 2 \\times 2,0 = 4,0\\text{ mol}$.<br>Vì hiệu suất phản ứng đạt 75% nên lượng $\\text{CO}_2$ thực tế thu được là: $n_{\\text{CO}_2\\text{ (TT)}} = 4,0 \\times 75\\% = 3,0\\text{ mol}$.<br>Hấp thụ vào $\\text{Ca(OH)}_2$ dư: $\\text{CO}_2 + \\text{Ca(OH)}_2 \\rightarrow \\text{CaCO}_3 \\downarrow + \\text{H}_2\\text{O}$.<br>Khối lượng kết tủa $\\text{CaCO}_3$: $m = 3,0 \\times 100 = 300\\text{ gam}$."
        },
        {
            "id": 4,
            "question": "Cho 9,0 gam ethylamine ($\\text{CH}_3\\text{CH}_2\\text{NH}_2$) phản ứng vừa đủ với dung dịch hydrochloric acid ($\\text{HCl}$). Sau khi phản ứng hoàn toàn, cô cạn cẩn thận dung dịch thu được $m$ gam muối ethylammonium chloride ($\\text{C}_2\\text{H}_5\\text{NH}_3\\text{Cl}$). Giá trị của $m$ là bao nhiêu?",
            "answer": "16,3",
            "explanation": "Khối lượng mol của ethylamine: $M = 45\\text{ g/mol}$.<br>Số mol ethylamine: $n = \\frac{9,0}{45} = 0,2\\text{ mol}$.<br>Phương trình phản ứng: $\\text{C}_2\\text{H}_5\\text{NH}_2 + \\text{HCl} \\rightarrow \\text{C}_2\\text{H}_5\\text{NH}_3\\text{Cl}$.<br>Theo phương trình: $n_{\\text{muối}} = n_{\\text{amine}} = 0,2\\text{ mol}$.<br>Khối lượng mol của muối ethylammonium chloride: $M_{\\text{muối}} = 45 + 36,5 = 81,5\\text{ g/mol}$.<br>Khối lượng muối thu được: $m = 0,2 \\times 81,5 = 16,3\\text{ gam}$."
        },
        {
            "id": 5,
            "question": "Cho 4,65 gam aniline ($\\text{C}_6\\text{H}_5\\text{NH}_2$) phản ứng hoàn toàn với lượng dư nước bromine. Khối lượng kết tủa trắng 2,4,6-tribromoaniline ($\\text{C}_6\\text{H}_2\\text{Br}_3\\text{NH}_2$) thu được là bao nhiêu gam?",
            "answer": "16,5",
            "explanation": "Khối lượng mol của aniline: $M_{\\text{aniline}} = 93\\text{ g/mol}$.<br>Số mol aniline: $n_{\\text{aniline}} = \\frac{4,65}{93} = 0,05\\text{ mol}$.<br>Phương trình hóa học: $\\text{C}_6\\text{H}_5\\text{NH}_2 + 3\\text{Br}_2 \\rightarrow \\text{C}_6\\text{H}_2\\text{Br}_3\\text{NH}_2 \\downarrow + 3\\text{HBr}$.<br>Khối lượng mol của kết tủa 2,4,6-tribromoaniline: $M = 93 + 3 \\times 79 = 330\\text{ g/mol}$.<br>Khối lượng kết tủa thu được: $m = 0,05 \\times 330 = 16,5\\text{ gam}$."
        },
        {
            "id": 6,
            "question": "Cho các phát biểu sau:\\n(1) Triolein có phản ứng cộng hydrogen (xúc tác $\\text{Ni}, t^\\circ$) tạo thành tristearin.\\n(2) Fructose có khả năng tham gia phản ứng tráng bạc trong môi trường kiềm.\\n(3) Ở điều kiện thường, methylamine và ethylamine là những chất khí có mùi khai, tan nhiều trong nước.\\n(4) Phân tử saccharose được cấu tạo từ hai gốc $\\alpha$-glucose liên kết với nhau.\\n(5) Aniline không làm đổi màu quỳ tím ẩm.\\n(6) Xà phòng hóa chất béo bằng dung dịch $\\text{NaOH}$ luôn thu được glycerol.\\nSố phát biểu đúng là bao nhiêu?",
            "answer": "5",
            "explanation": "Xét từng phát biểu:<br>- (1) Đúng: Triolein $[(\\text{C}_{17}\\text{H}_{33}\\text{COO})_3\\text{C}_3\\text{H}_5]$ không no cộng $3\\text{H}_2$ tạo chất béo no tristearin $[(\\text{C}_{17}\\text{H}_{35}\\text{COO})_3\\text{C}_3\\text{H}_5]$.<br>- (2) Đúng: Trong môi trường kiềm của thuốc thử Tollens, fructose chuyển hóa đồng phân thành glucose nên có phản ứng tráng bạc.<br>- (3) Đúng: Các amine bậc thấp $\\text{CH}_3\\text{NH}_2, (\\text{CH}_3)_2\\text{NH}, (\\text{CH}_3)_3\\text{N}$ và $\\text{C}_2\\text{H}_5\\text{NH}_2$ là chất khí ở điều kiện thường, mùi khai độc, tan tốt trong nước.<br>- (4) Sai: Phân tử saccharose cấu tạo từ 1 gốc $\\alpha$-glucose và 1 gốc $\\beta$-fructose (maltose mới cấu tạo từ 2 gốc $\\alpha$-glucose).<br>- (5) Đúng: Aniline có tính base cực yếu do ảnh hưởng hút electron của vòng thơm nên dung dịch không làm đổi màu quỳ tím.<br>- (6) Đúng: Chất béo là triester của acid béo với glycerol nên thủy phân trong kiềm luôn sinh ra glycerol.<br>Vậy có 5 phát biểu đúng là: (1), (2), (3), (5), (6). Đáp số là 5."
        }
    ]
}

# --- 1. Tạo file Markdown (.md) ---
md_lines = [
    "# ĐỀ ÔN TẬP HÓA HỌC 12: CHƯƠNG 1, 2 VÀ CHƯƠNG 3 (ĐẾN PHẦN AMINE)",
    "**Môn:** Hóa học 12 — Chuẩn cấu trúc Đề thi Tốt nghiệp THPT mới nhất",
    "**Thời gian làm bài:** 50 phút (không kể thời gian giao đề)",
    "",
    "> Ghi chú thí sinh: Cho biết nguyên tử khối của các nguyên tố: H = 1; C = 12; N = 14; O = 16; Na = 23; Cl = 35,5; Ca = 40; Br = 80; Ag = 108.",
    "",
    "---",
    "",
    "## PHẦN I. CÂU TRẮC NGHIỆM NHIỀU LỰA CHỌN (4,5 ĐIỂM)",
    "Thí sinh trả lời từ Câu 1 đến Câu 18. Mỗi câu hỏi thí sinh chỉ chọn một phương án.",
    ""
]

for q in quiz_data["part1"]:
    md_lines.append(f"Câu {q['id']}: {q['question']}")
    for k, v in q['options'].items():
        md_lines.append(f"{k}. {v}")
    md_lines.append("")

md_lines.extend([
    "---",
    "",
    "## PHẦN II. CÂU TRẮC NGHIỆM ĐÚNG / SAI (4,0 ĐIỂM)",
    "Thí sinh trả lời từ Câu 1 đến Câu 4. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn Đúng hoặc Sai.",
    "Barem điểm: Đúng 1 ý được 0,10 điểm; Đúng 2 ý được 0,25 điểm; Đúng 3 ý được 0,50 điểm; Đúng 4 ý được 1,00 điểm.",
    ""
])

for q in quiz_data["part2"]:
    md_lines.append(f"Câu {q['id']}: {q['title']}")
    if q['id'] == 1:
        md_lines.append("Tiến hành thí nghiệm điều chế ethyl acetate theo các bước thực nghiệm sau:")
        md_lines.append("![Thí nghiệm điều chế ethyl acetate](dau-ra/lop-12/de-kiem-tra/images/ethyl_acetate_experiment.jpg)")
        md_lines.append("- Bước 1: Cho vào ống nghiệm sạch 6,0 gam $\\text{CH}_3\\text{COOH}$ nguyên chất, 4,6 gam $\\text{C}_2\\text{H}_5\\text{OH}$ khan và vài giọt dung dịch $\\text{H}_2\\text{SO}_4$ đặc, lắc đều.")
        md_lines.append("- Bước 2: Đặt ống nghiệm vào cốc nước nóng có nhiệt độ $65^\\circ\\text{C} - 70^\\circ\\text{C}$ trong khoảng 5 - 7 phút.")
        md_lines.append("- Bước 3: Làm lạnh ống nghiệm dưới vòi nước, sau đó rót từ từ 2 mL dung dịch $\\text{NaCl}$ bão hòa vào ống nghiệm.")
    elif q['id'] == 2:
        md_lines.append("Trong công nghiệp sản xuất xăng sinh học E5 và ngành thực phẩm, tinh bột và cellulose là hai nguồn nguyên liệu sinh khối vô cùng phong phú. Quá trình chuyển hóa sinh hóa bao gồm thủy phân tinh bột trong hạt ngô hoặc sắn thành glucose nhờ enzyme amylase, sau đó lên men glucose thành ethanol nhờ nấm men (yeast) ở điều kiện yếm khí (kị khí):")
        md_lines.append("$$\\text{Tinh bột } (\\text{C}_6\\text{H}_{10}\\text{O}_5)_n \\xrightarrow{+\\text{H}_2\\text{O}, \\text{ enzyme}} n\\text{C}_6\\text{H}_{12}\\text{O}_6 \\text{ (glucose)}$$")
        md_lines.append("$$\\text{C}_6\\text{H}_{12}\\text{O}_6 \\xrightarrow{\\text{men rượu}, 30-35^\\circ\\text{C}} 2\\text{C}_2\\text{H}_5\\text{OH} + 2\\text{CO}_2 \\uparrow$$")
    elif q['id'] == 3:
        md_lines.append("Aniline ($\\text{C}_6\\text{H}_5\\text{NH}_2$) là một amine thơm đơn chức quan trọng, được sử dụng rộng rãi trong tổng hợp phẩm nhuộm azo, dược phẩm (như paracetamol) và chất tăng tốc lưu hóa cao su. Tiến hành chuỗi thí nghiệm khảo sát tính chất của aniline như sau:")
        md_lines.append("- Thí nghiệm 1: Cho 1 mL aniline vào ống nghiệm chứa 3 mL nước cất, lắc mạnh rồi để yên.")
        md_lines.append("- Thí nghiệm 2: Thêm tiếp 2 mL dung dịch $\\text{HCl}$ 1M vào ống nghiệm sau thí nghiệm 1, lắc đều.")
        md_lines.append("- Thí nghiệm 3: Rót từ từ dung dịch $\\text{NaOH}$ 1M vào ống nghiệm sau thí nghiệm 2 cho đến khi dư kiềm.")
        md_lines.append("- Thí nghiệm 4: Cho 1 mL aniline vào ống nghiệm mới, sau đó nhỏ từ từ nước bromine vào.")
    elif q['id'] == 4:
        md_lines.append("Có 4 lọ hóa chất mất nhãn đựng 4 chất lỏng hoặc dung dịch riêng biệt: Ethyl acetate ($\\text{CH}_3\\text{COOCH}_2\\text{CH}_3$), Glucose ($\\text{C}_6\\text{H}_{12}\\text{O}_6$ 2%), Glycerol [$\\text{C}_3\\text{H}_5(\\text{OH})_3$], và Dimethylamine [$(\\text{CH}_3)_2\\text{NH}$]. Một học sinh thiết kế quy trình thực nghiệm nhận biết gồm 3 bước:")
        md_lines.append("- Bước 1: Nhúng giấy quỳ tím vào 4 mẫu thử.")
        md_lines.append("- Bước 2: Với các mẫu thử không làm đổi màu quỳ tím, cho lần lượt tác dụng với $\\text{Cu(OH)}_2$ ở nhiệt độ phòng.")
        md_lines.append("- Bước 3: Đun nóng nhẹ các hỗn hợp thu được ở bước 2 xuất hiện phức màu xanh lam đậm.")

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
    "| 1 | A | 7 | A | 13 | B |",
    "| 2 | B | 8 | A | 14 | B |",
    "| 3 | B | 9 | A | 15 | C |",
    "| 4 | A | 10 | A | 16 | A |",
    "| 5 | A | 11 | C | 17 | B |",
    "| 6 | A | 12 | A | 18 | B |",
    "",
    "### BẢNG ĐÁP ÁN PHẦN II",
    "| Câu | Lệnh hỏi | Đáp án (Đ/S) | Câu | Lệnh hỏi | Đáp án (Đ/S) |",
    "| :---: | :---: | :---: | :---: | :---: | :---: |",
    "| 1 | a | Đ | 3 | a | Đ |",
    "| 1 | b | Đ | 3 | b | Đ |",
    "| 1 | c | S | 3 | c | S |",
    "| 1 | d | Đ | 3 | d | Đ |",
    "| 2 | a | Đ | 4 | a | Đ |",
    "| 2 | b | S | 4 | b | S |",
    "| 2 | c | Đ | 4 | c | Đ |",
    "| 2 | d | Đ | 4 | d | Đ |",
    "",
    "### BẢNG ĐÁP ÁN PHẦN III",
    "| Câu | Lời giải tóm tắt | Đáp số |",
    "| :---: | :--- | :---: |",
    "| 1 | m_rắn = m(CH3COONa: 0,2 mol) + m(NaOH dư: 0,05 mol) = 16,4 + 2,0 = 18,4 g | 18,4 |",
    "| 2 | Linoleic acid có 2 liên kết đôi C=C mạch carbon -> x = 2 | 2 |",
    "| 3 | n(glucose) = 2 mol -> n(CO2 tt) = 2 * 2 * 75% = 3 mol -> m(CaCO3) = 300 g | 300 |",
    "| 4 | n(C2H5NH2) = 0,2 mol -> m(C2H5NH3Cl) = 0,2 * 81,5 = 16,3 g | 16,3 |",
    "| 5 | n(aniline) = 0,05 mol -> m(kết tủa) = 0,05 * 330 = 16,5 g | 16,5 |",
    "| 6 | Các phát biểu đúng gồm: (1), (2), (3), (5), (6) -> 5 phát biểu | 5 |",
    "",
    "---",
    "",
    "### LỜI GIẢI CHI TIẾT TỪNG CÂU",
    "",
    "#### PHẦN I"
])

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
md_path = os.path.join("dau-ra", "lop-12", "de-kiem-tra", "de-on-tap-chuong-1-2-den-amine-hoa-hoc-12.md")
os.makedirs(os.path.dirname(md_path), exist_ok=True)
with open(md_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))
print(f"Đã tạo file Markdown: {md_path}")

# --- 2. Xuất Word DOCX ---
docx_path = os.path.join("dau-ra", "lop-12", "de-kiem-tra", "de-on-tap-chuong-1-2-den-amine-hoa-hoc-12.docx")
create_styled_document(md_path, docx_path)
print(f"Đã tạo file Word DOCX: {docx_path}")

# --- 3. Xuất HTML Trắc Nghiệm Trực Tuyến ---
html_path = os.path.join("dau-ra", "lop-12", "de-kiem-tra", "de-on-tap-chuong-1-2-den-amine-hoa-hoc-12.html")
generate_quiz_html(quiz_data, html_path)
print(f"Đã tạo file HTML (dau-ra): {html_path}")

# Đồng thời lưu vào thư mục lop-12/ để sẵn sàng làm bài trên web
web_path = os.path.join("lop-12", "de-on-tap-chuong-1-2-den-amine.html")
os.makedirs("lop-12", exist_ok=True)
shutil.copy(html_path, web_path)
print(f"Đã tạo file HTML (lop-12 web): {web_path}")

print("=== HOÀN TẤT CẬP NHẬT BỘ ĐỀ ÔN TẬP CHƯƠNG 1, 2 VÀ CHƯƠNG 3 (ĐẾN AMINE) HÓA HỌC 12 ===")
