import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

EXPORT_DIR = os.path.join("vatli102_export", "hoa")
os.makedirs(EXPORT_DIR, exist_ok=True)

# ==========================================
# 1. READ ORIGINAL HOA INDEX
# ==========================================
with open('scripts/vatli102_hoa_index.html', 'r', encoding='utf-8') as f:
    hoa_index = f.read()

# Update Action Status Card in Hero
old_hero_card = '''            <!-- Action Status Card -->
            <div class="bg-white/10 backdrop-blur-md p-5 rounded-2xl border border-white/20 text-center w-full md:w-80 shadow-xl space-y-3 shrink-0">
                <div class="text-xs text-amber-300 font-extrabold uppercase tracking-wider flex items-center justify-center gap-1.5">
                    <i class="fa-solid fa-spinner fa-spin"></i> TIẾN ĐỘ BIÊN SOẠN
                </div>
                <div class="text-lg font-extrabold text-white">Đang Hoàn Thiện Bài Học</div>
                <p class="text-xs text-slate-300">Ban chuyên môn đang biên soạn các bài giảng chuẩn SGK và ngân hàng đề thi tự động chấm điểm.</p>
                <button onclick="openSubscribeModal()" class="w-full py-2.5 bg-amber-400 hover:bg-amber-300 text-slate-900 font-extrabold text-xs rounded-xl shadow-md transition-all">
                    🔔 Nhận thông báo khi có bài mới
                </button>
            </div>'''

new_hero_card = '''            <!-- Action Status Card -->
            <div class="bg-white/15 backdrop-blur-md p-5 rounded-2xl border border-white/30 text-center w-full md:w-80 shadow-2xl space-y-3 shrink-0">
                <div class="text-xs text-emerald-300 font-extrabold uppercase tracking-wider flex items-center justify-center gap-1.5">
                    <i class="fa-solid fa-circle-check"></i> ĐÃ PHÁT HÀNH HỌC LIỆU
                </div>
                <div class="text-lg font-extrabold text-white">Hóa Học 12: Đã Có 3 Đề Thi</div>
                <p class="text-xs text-slate-200">Đã kích hoạt hệ thống làm bài trực tuyến, tự động chấm điểm tức thì và lưu kết quả về Google Sheets.</p>
                <a href="/hoa/lop-12/" class="w-full py-2.5 bg-gradient-to-r from-amber-400 to-amber-300 hover:from-amber-300 hover:to-amber-200 text-slate-900 font-extrabold text-xs rounded-xl shadow-md transition-all flex items-center justify-center gap-2">
                    <i class="fa-solid fa-file-pen text-purple-800"></i> Vào Xem & Làm Đề Lớp 12
                </a>
            </div>'''

if old_hero_card in hoa_index:
    hoa_index = hoa_index.replace(old_hero_card, new_hero_card)
else:
    print("Warning: old_hero_card pattern mismatch, continuing...")

# Update Notice Banner
old_notice = '''        <!-- Thông báo từ Ban Chuyên Môn -->
        <div class="bg-blue-50 border border-blue-200 rounded-2xl p-5 flex items-start gap-4 shadow-sm">
            <div class="w-10 h-10 rounded-xl bg-blue-600 text-white flex items-center justify-center text-lg shrink-0 shadow-sm mt-0.5">
                <i class="fa-solid fa-circle-info"></i>
            </div>
            <div class="space-y-1">
                <h3 class="font-extrabold text-blue-900 text-sm">Học liệu Môn Hóa Học đang được cập nhật từng bài</h3>
                <p class="text-xs text-blue-800 leading-relaxed">
                    Hệ thống sẽ lần lượt xuất bản đầy đủ các bài giảng Lý thuyết chuẩn mực, Trắc nghiệm online chấm điểm tự động gửi kết quả về Google Sheets và Ngân hàng đề thi ôn tập định kỳ cho từng khối lớp dưới đây.
                </p>
            </div>
        </div>'''

new_notice = '''        <!-- Thông báo từ Ban Chuyên Môn -->
        <div class="bg-emerald-50 border border-emerald-200 rounded-2xl p-5 flex items-start gap-4 shadow-sm">
            <div class="w-10 h-10 rounded-xl bg-emerald-600 text-white flex items-center justify-center text-lg shrink-0 shadow-sm mt-0.5">
                <i class="fa-solid fa-circle-check"></i>
            </div>
            <div class="space-y-1">
                <h3 class="font-extrabold text-emerald-900 text-sm">Đã phát hành Hệ thống Khảo thí Trắc nghiệm Hóa Học 12 (Chuẩn Cấu Trúc 2026)</h3>
                <p class="text-xs text-emerald-800 leading-relaxed">
                    Học sinh lớp 12 hiện có thể làm trực tuyến <strong>Đề 1, Đề 2, Đề 3</strong> ôn tập toàn diện kiến thức Chương 1, 2, 3. Đề có đồng hồ đếm giờ 50 phút, chấm điểm tức thì, xem lời giải chi tiết và tự động đồng bộ kết quả vào Google Sheets của giáo viên.
                </p>
            </div>
        </div>'''

if old_notice in hoa_index:
    hoa_index = hoa_index.replace(old_notice, new_notice)

# Update Grade 12 Card in hoa_index
grade_12_card_regex = r'<div class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm hover:shadow-md transition-all flex flex-col justify-between space-y-4">\s*<div class="space-y-3">\s*<div class="flex items-center justify-between">\s*<span class="text-xs font-extrabold px-2\.5 py-1 rounded-full bg-purple-100 text-purple-800 border-purple-200">Hóa Học Lớp 12</span>\s*<span class="text-\[11px\] font-bold text-amber-600 bg-amber-50 px-2 py-0\.5 rounded"><i class="fa-solid fa-clock"></i> Sắp phát hành</span>.*?</div>\s*<div class="pt-3 border-t border-slate-100">\s*<button onclick="openSubscribeModal\(\)".*?</button>\s*</div>\s*</div>'

new_grade_12_card = '''            <div class="bg-white rounded-2xl border-2 border-indigo-500 shadow-md hover:shadow-lg transition-all flex flex-col justify-between space-y-4 relative overflow-hidden">
                <div class="absolute -right-8 -top-8 w-20 h-20 bg-indigo-50 rounded-full pointer-events-none"></div>
                <div class="space-y-3 relative z-10">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-extrabold px-2.5 py-1 rounded-full bg-purple-100 text-purple-800 border-purple-200">Hóa Học Lớp 12</span>
                        <span class="text-[11px] font-bold text-emerald-700 bg-emerald-100 px-2.5 py-0.5 rounded-full flex items-center gap-1"><i class="fa-solid fa-circle-check"></i> Đã có 3 đề thi</span>
                    </div>
                    <h3 class="font-extrabold text-slate-900 text-base">Hóa Học Lớp 12</h3>
                    <p class="text-slate-500 text-xs font-medium">Este - Lipit • Cacbohiđrat • Hợp chất chứa Nitrogen • Kim loại</p>
                    <div class="pt-2 border-t border-slate-100">
                        <div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-2">Các chủ đề trọng tâm:</div>
                        <ul class="text-xs text-slate-700 space-y-1.5 font-medium">
                            <li class="flex items-start gap-2"><i class="fa-solid fa-angle-right text-indigo-500 mt-1 text-[10px] shrink-0"></i> <span>Chương 1: Este - Lipit và chất giặt rửa tổng hợp</span></li>
                            <li class="flex items-start gap-2"><i class="fa-solid fa-angle-right text-indigo-500 mt-1 text-[10px] shrink-0"></i> <span>Chương 2: Cacbohiđrat (Glucose, Fructose, Saccharose, Tinh bột, Cellulose)</span></li>
                            <li class="flex items-start gap-2"><i class="fa-solid fa-angle-right text-indigo-500 mt-1 text-[10px] shrink-0"></i> <span>Chương 3: Hợp chất chứa Nitrogen (Amine, Amino acid, Peptide, Protein)</span></li>
                            <li class="flex items-start gap-2"><i class="fa-solid fa-angle-right text-indigo-500 mt-1 text-[10px] shrink-0"></i> <span>Chương 4: Polymer và vật liệu polymer</span></li>
                            <li class="flex items-start gap-2"><i class="fa-solid fa-angle-right text-indigo-500 mt-1 text-[10px] shrink-0"></i> <span>Chương 5: Pin điện và điện phân</span></li>
                            <li class="flex items-start gap-2"><i class="fa-solid fa-angle-right text-indigo-500 mt-1 text-[10px] shrink-0"></i> <span>Chương 6: Đại cương về kim loại và phức chất</span></li>
                        </ul>
                    </div>
                </div>
                <div class="pt-3 border-t border-slate-100 relative z-10 space-y-2">
                    <a href="/hoa/lop-12/" class="w-full py-2.5 bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 text-white font-extrabold text-xs rounded-xl shadow-md transition-all flex items-center justify-center gap-1.5">
                        <i class="fa-solid fa-graduation-cap"></i> <span>Vào Xem Đề Thi Hóa 12 (3 Đề)</span>
                    </a>
                </div>
            </div>'''

hoa_index = re.sub(grade_12_card_regex, new_grade_12_card, hoa_index, flags=re.DOTALL)

# Add Featured Exam Section to hoa_index right after the grade cards grid
exam_cards_section = '''        <!-- Kho Đề Thi Trắc Nghiệm Hóa Học 12 -->
        <section id="lop12" class="space-y-6 pt-4">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-200 pb-4">
                <div>
                    <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-bold bg-purple-100 text-purple-800 mb-1">
                        <i class="fa-solid fa-fire text-amber-500"></i> HÓA HỌC LỚP 12 • GDPT 2018
                    </div>
                    <h2 class="text-xl sm:text-2xl font-extrabold text-slate-900 flex items-center gap-2">
                        <i class="fa-solid fa-file-pen text-indigo-600"></i> Đề Ôn Tập & Khảo Thí Trắc Nghiệm Hóa Học 12
                    </h2>
                    <p class="text-xs sm:text-sm text-slate-500 mt-0.5">
                        Chuẩn cấu trúc Bộ GD&ĐT 2026: 18 câu Trắc nghiệm nhiều lựa chọn + 4 câu Đúng/Sai + 6 câu Trả lời ngắn. Chấm điểm & lưu Google Sheets tự động.
                    </p>
                </div>
                <a href="/hoa/lop-12/" class="inline-flex items-center gap-1 px-4 py-2 rounded-xl bg-indigo-50 hover:bg-indigo-100 text-indigo-700 font-bold text-xs transition-colors shrink-0">
                    Xem trọn bộ Hóa 12 <i class="fa-solid fa-arrow-right"></i>
                </a>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <!-- Đề 1 -->
                <div class="bg-white rounded-2xl border border-slate-200 hover:border-purple-400 p-5 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between space-y-4 group">
                    <div class="space-y-3">
                        <div class="flex items-center justify-between">
                            <span class="text-[11px] font-extrabold px-2.5 py-1 rounded-lg bg-blue-100 text-blue-800">ĐỀ SỐ 1</span>
                            <span class="text-[11px] font-bold text-slate-500 flex items-center gap-1"><i class="fa-regular fa-clock text-amber-500"></i> 50 phút</span>
                        </div>
                        <h3 class="font-extrabold text-slate-900 text-base group-hover:text-purple-700 transition-colors">
                            Ôn Tập Chương 1, 2 và Chương 3 (Đến Amine)
                        </h3>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            Bao quát Este, Lipid, Xà phòng, Carbohydrate và Amine. Ma trận chuẩn 28 câu phân hóa theo mức độ Biết, Hiểu, Vận dụng.
                        </p>
                        <div class="pt-2 border-t border-slate-100 flex flex-wrap gap-1.5 text-[11px]">
                            <span class="px-2 py-0.5 rounded bg-slate-100 text-slate-700 font-semibold">18 TN 4 lựa chọn</span>
                            <span class="px-2 py-0.5 rounded bg-slate-100 text-slate-700 font-semibold">4 câu Đúng/Sai</span>
                            <span class="px-2 py-0.5 rounded bg-slate-100 text-slate-700 font-semibold">6 câu Trả lời ngắn</span>
                        </div>
                    </div>
                    <div class="pt-3 border-t border-slate-100 space-y-2">
                        <a href="/hoa/lop-12/de-1/" class="w-full py-2.5 bg-indigo-600 hover:bg-indigo-700 text-white font-extrabold text-xs rounded-xl shadow-md transition-all flex items-center justify-center gap-2">
                            <i class="fa-solid fa-play"></i> Bắt Đầu Làm Đề 1
                        </a>
                    </div>
                </div>

                <!-- Đề 2 -->
                <div class="bg-white rounded-2xl border border-slate-200 hover:border-purple-400 p-5 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between space-y-4 group">
                    <div class="space-y-3">
                        <div class="flex items-center justify-between">
                            <span class="text-[11px] font-extrabold px-2.5 py-1 rounded-lg bg-purple-100 text-purple-800">ĐỀ SỐ 2 (MÃ 01)</span>
                            <span class="text-[11px] font-bold text-slate-500 flex items-center gap-1"><i class="fa-regular fa-clock text-amber-500"></i> 50 phút</span>
                        </div>
                        <h3 class="font-extrabold text-slate-900 text-base group-hover:text-purple-700 transition-colors">
                            Ôn Tập Tới Hết Chương 3 (Hợp Chất Chứa N)
                        </h3>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            Ôn trọn vẹn Este, Lipid, Carbohydrate, Amine, Amino acid, Peptide và Protein. Đính kèm phổ hồng ngoại IR và thực nghiệm.
                        </p>
                        <div class="pt-2 border-t border-slate-100 flex flex-wrap gap-1.5 text-[11px]">
                            <span class="px-2 py-0.5 rounded bg-slate-100 text-slate-700 font-semibold">18 TN 4 lựa chọn</span>
                            <span class="px-2 py-0.5 rounded bg-slate-100 text-slate-700 font-semibold">4 câu Đúng/Sai</span>
                            <span class="px-2 py-0.5 rounded bg-slate-100 text-slate-700 font-semibold">6 câu Trả lời ngắn</span>
                        </div>
                    </div>
                    <div class="pt-3 border-t border-slate-100 space-y-2">
                        <a href="/hoa/lop-12/de-2/" class="w-full py-2.5 bg-purple-600 hover:bg-purple-700 text-white font-extrabold text-xs rounded-xl shadow-md transition-all flex items-center justify-center gap-2">
                            <i class="fa-solid fa-play"></i> Bắt Đầu Làm Đề 2
                        </a>
                    </div>
                </div>

                <!-- Đề 3 -->
                <div class="bg-white rounded-2xl border border-slate-200 hover:border-purple-400 p-5 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between space-y-4 group">
                    <div class="space-y-3">
                        <div class="flex items-center justify-between">
                            <span class="text-[11px] font-extrabold px-2.5 py-1 rounded-lg bg-emerald-100 text-emerald-800">ĐỀ SỐ 3 (CHUẨN 2026)</span>
                            <span class="text-[11px] font-bold text-slate-500 flex items-center gap-1"><i class="fa-regular fa-clock text-amber-500"></i> 50 phút</span>
                        </div>
                        <h3 class="font-extrabold text-slate-900 text-base group-hover:text-purple-700 transition-colors">
                            Ôn Tập Tới Hết Chương 3 (Bộ Đề Nâng Cao)
                        </h3>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            Thiết kế theo cấu trúc định dạng chuẩn năm 2026. Phân tích thực tế sản xuất xà phòng, phản ứng màu Biuret, bài toán phân hóa.
                        </p>
                        <div class="pt-2 border-t border-slate-100 flex flex-wrap gap-1.5 text-[11px]">
                            <span class="px-2 py-0.5 rounded bg-slate-100 text-slate-700 font-semibold">18 TN 4 lựa chọn</span>
                            <span class="px-2 py-0.5 rounded bg-slate-100 text-slate-700 font-semibold">4 câu Đúng/Sai</span>
                            <span class="px-2 py-0.5 rounded bg-slate-100 text-slate-700 font-semibold">6 câu Trả lời ngắn</span>
                        </div>
                    </div>
                    <div class="pt-3 border-t border-slate-100 space-y-2">
                        <a href="/hoa/lop-12/de-3/" class="w-full py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-xs rounded-xl shadow-md transition-all flex items-center justify-center gap-2">
                            <i class="fa-solid fa-play"></i> Bắt Đầu Làm Đề 3
                        </a>
                    </div>
                </div>
            </div>
        </section>
'''

# Insert the exam cards section right after the grade cards container
hoa_index = hoa_index.replace('            </div>\n        </div>\n\n        <!-- Khung Đăng Ký Theo Dõi Nhận Bài Học Mới -->', '            </div>\n        </div>\n\n' + exam_cards_section + '\n\n        <!-- Khung Đăng Ký Theo Dõi Nhận Bài Học Mới -->')

with open(os.path.join(EXPORT_DIR, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(hoa_index)

print("Đã tạo vatli102_export/hoa/index.html")

# ==========================================
# 2. CREATE HOA LOP-12 HUB (hoa/lop-12/index.html)
# ==========================================
lop12_hub_html = '''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hóa Học Lớp 12 - Hệ Thống Khảo Thí & Đề Thi Chuẩn GDPT 2018 | Vatli102.com</title>
    <meta name="description" content="Chuyên trang Hóa Học 12 tại Vatli102.com: Ngân hàng đề thi trắc nghiệm online 50 phút chuẩn cấu trúc Bộ GD&ĐT 2026, tự động chấm điểm và lưu kết quả.">
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Plus Jakarta Sans', sans-serif; }
        .no-scrollbar::-webkit-scrollbar { display: none; }
        .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
    </style>
</head>
<body class="bg-slate-50 text-slate-800 min-h-screen flex flex-col antialiased">

    <!-- Top Navigation Bar -->
    <header class="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-16 gap-4">
                <!-- Logo -->
                <a href="/" class="flex items-center gap-3 group">
                    <img src="/favicon.svg" alt="Vatli102" class="w-9 h-9 rounded-xl shadow-md shadow-blue-500/20 group-hover:scale-105 transition-transform">
                    <div class="flex flex-col">
                        <span class="font-extrabold text-lg text-slate-900 leading-none tracking-tight group-hover:text-blue-600 transition-colors">Vatli102.com</span>
                        <span class="text-[10px] text-slate-500 font-semibold tracking-wider uppercase mt-1">Cổng Học Liệu GDPT 2018</span>
                    </div>
                </a>

                <!-- Back & Switcher Button -->
                <div class="flex items-center gap-2">
                    <a href="/hoa/" class="px-3 py-1.5 rounded-xl bg-purple-50 hover:bg-purple-100 text-purple-700 text-xs font-bold transition-colors flex items-center gap-1.5">
                        <i class="fa-solid fa-flask-vial"></i> <span>Môn Hóa Học</span>
                    </a>
                    <a href="/" class="px-3 py-1.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold transition-colors flex items-center gap-1.5">
                        <i class="fa-solid fa-house"></i> <span>Trang chủ</span>
                    </a>
                </div>
            </div>
        </div>

        <!-- Navigation Menu Bar -->
        <nav class="bg-gradient-to-r from-blue-950 via-indigo-950 to-slate-950 text-white overflow-x-auto no-scrollbar border-t border-blue-800/50 shadow-inner">
            <div class="max-w-[1360px] mx-auto px-2 sm:px-3 lg:px-4 flex items-center gap-1 text-xs font-semibold whitespace-nowrap py-1.5">
                <a href="/" class="px-2.5 py-1.5 rounded-lg hover:bg-white/10 text-slate-200 transition-colors flex items-center gap-1.5 shrink-0">
                    <i class="fa-solid fa-house text-blue-400"></i> <span>Trang chủ</span>
                </a>
                <a href="/hoa/" class="px-3 py-1.5 rounded-lg bg-purple-700 text-white transition-colors flex items-center gap-1.5 shrink-0 font-extrabold shadow-sm">
                    <i class="fa-solid fa-flask-vial text-purple-300"></i> <span>Môn Hóa Học</span>
                </a>
                <a href="/hoa/lop-12/" class="px-3 py-1.5 rounded-lg bg-indigo-600 text-white transition-colors flex items-center gap-1.5 shrink-0 font-extrabold shadow-sm">
                    <i class="fa-solid fa-graduation-cap text-cyan-300"></i> <span>Hóa Học 12</span>
                </a>
                <span class="h-4 w-px bg-slate-700 mx-0.5 shrink-0"></span>
                <a href="/#lop12" class="px-2.5 py-1.5 rounded-lg hover:bg-white/10 text-slate-200 transition-colors flex items-center gap-1.5 shrink-0">
                    <i class="fa-solid fa-atom text-cyan-400"></i> <span>Vật Lí 12</span>
                </a>
                <a href="/toan/" class="px-2.5 py-1.5 rounded-lg hover:bg-white/10 text-slate-200 transition-colors flex items-center gap-1.5 shrink-0">
                    <i class="fa-solid fa-square-root-variable text-indigo-400"></i> <span>Toán Học</span>
                </a>
                <a href="/sinh/" class="px-2.5 py-1.5 rounded-lg hover:bg-white/10 text-slate-200 transition-colors flex items-center gap-1.5 shrink-0">
                    <i class="fa-solid fa-dna text-emerald-400"></i> <span>Sinh Học</span>
                </a>
            </div>
        </nav>
    </header>

    <!-- Hero Banner -->
    <section class="bg-gradient-to-r from-purple-900 via-indigo-900 to-slate-900 text-white py-10 px-4 relative overflow-hidden">
        <div class="absolute inset-0 opacity-10 bg-[radial-gradient(#38bdf8_1px,transparent_1px)] [background-size:16px_16px]"></div>
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-6 relative z-10">
            <div class="space-y-3 text-center md:text-left max-w-3xl">
                <!-- Breadcrumb -->
                <div class="flex items-center justify-center md:justify-start gap-2 text-xs text-slate-300">
                    <a href="/" class="hover:text-white">Trang chủ</a>
                    <i class="fa-solid fa-chevron-right text-[10px] text-slate-400"></i>
                    <a href="/hoa/" class="hover:text-white">Môn Hóa Học</a>
                    <i class="fa-solid fa-chevron-right text-[10px] text-slate-400"></i>
                    <span class="text-amber-300 font-bold">Hóa Học Lớp 12</span>
                </div>
                <h1 class="text-3xl sm:text-4xl font-extrabold tracking-tight">
                    HÓA HỌC LỚP 12
                </h1>
                <p class="text-slate-200 text-sm sm:text-base leading-relaxed">
                    Hệ thống khảo thí trắc nghiệm trực tuyến chuẩn định dạng cấu trúc mới nhất của Bộ Giáo Dục & Đào Tạo năm 2026. Tự động chấm điểm, hiển thị đáp án chi tiết và đồng bộ kết quả.
                </p>
                <div class="flex flex-wrap items-center justify-center md:justify-start gap-2 pt-2 text-xs">
                    <span class="px-3 py-1 rounded-full bg-white/10 font-bold border border-white/20"><i class="fa-solid fa-check text-emerald-400"></i> 3 Đề thi online</span>
                    <span class="px-3 py-1 rounded-full bg-white/10 font-bold border border-white/20"><i class="fa-solid fa-clock text-amber-400"></i> 50 phút / đề</span>
                    <span class="px-3 py-1 rounded-full bg-white/10 font-bold border border-white/20"><i class="fa-solid fa-table text-cyan-400"></i> Đồng bộ Google Sheets</span>
                </div>
            </div>

            <!-- Stats Badge -->
            <div class="bg-white/10 backdrop-blur-md p-6 rounded-2xl border border-white/20 text-center w-full md:w-72 shadow-xl space-y-3 shrink-0">
                <div class="text-xs text-amber-300 font-extrabold uppercase tracking-wider">
                    <i class="fa-solid fa-chart-simple"></i> CẤU TRÚC 10 ĐIỂM
                </div>
                <div class="space-y-1.5 text-xs text-slate-200">
                    <div class="flex justify-between border-b border-white/10 pb-1">
                        <span>Phần 1: Nhiều lựa chọn</span>
                        <strong class="text-white">18 câu (4.5 đ)</strong>
                    </div>
                    <div class="flex justify-between border-b border-white/10 pb-1">
                        <span>Phần 2: Đúng / Sai</span>
                        <strong class="text-white">4 câu (4.0 đ)</strong>
                    </div>
                    <div class="flex justify-between">
                        <span>Phần 3: Trả lời ngắn</span>
                        <strong class="text-white">6 câu (1.5 đ)</strong>
                    </div>
                </div>
                <div class="pt-2">
                    <span class="text-[11px] font-bold text-emerald-300 bg-emerald-950/60 px-3 py-1 rounded-full border border-emerald-400/30">
                        ✓ Tự Động Chấm Điểm Tức Thì
                    </span>
                </div>
            </div>
        </div>
    </section>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 flex-1 w-full space-y-10">

        <!-- Danh sách Đề Thi -->
        <section class="space-y-6">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-200 pb-4">
                <div>
                    <h2 class="text-2xl font-extrabold text-slate-900 flex items-center gap-2.5">
                        <i class="fa-solid fa-list-check text-purple-600"></i> Danh Sách Đề Ôn Tập Trắc Nghiệm Trực Tuyến
                    </h2>
                    <p class="text-xs sm:text-sm text-slate-500 mt-1">
                        Học sinh điền Họ tên và Lớp trước khi bắt đầu. Hệ thống tự động khóa bài khi hết 50 phút.
                    </p>
                </div>
                <span class="text-xs font-bold text-purple-700 bg-purple-50 px-3 py-1.5 rounded-xl border border-purple-200 self-start sm:self-auto">
                    3 đề đã sẵn sàng
                </span>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">

                <!-- Đề 1 -->
                <div class="bg-white rounded-2xl border-2 border-slate-200 hover:border-indigo-500 p-6 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between space-y-5 group">
                    <div class="space-y-4">
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-extrabold px-3 py-1 rounded-lg bg-indigo-100 text-indigo-800">ĐỀ THI SỐ 01</span>
                            <span class="text-xs font-bold text-slate-500 flex items-center gap-1.5"><i class="fa-regular fa-clock text-amber-500"></i> 50 phút</span>
                        </div>
                        <div>
                            <h3 class="font-extrabold text-slate-900 text-lg group-hover:text-indigo-600 transition-colors leading-snug">
                                Ôn Tập Chương 1, 2 và Chương 3 (Đến Amine)
                            </h3>
                            <p class="text-xs text-slate-500 mt-1">Phạm vi: Este, Lipid, Xà phòng, Carbohydrate, Cấu tạo & tính chất Amine.</p>
                        </div>
                        <div class="bg-slate-50 rounded-xl p-3 space-y-1.5 text-xs text-slate-600 border border-slate-100">
                            <div class="flex items-center justify-between">
                                <span><i class="fa-solid fa-circle-question text-indigo-500"></i> Phần 1: Nhiều lựa chọn</span>
                                <span class="font-bold text-slate-800">18 câu (4.5đ)</span>
                            </div>
                            <div class="flex items-center justify-between">
                                <span><i class="fa-solid fa-circle-check text-emerald-500"></i> Phần 2: Đúng / Sai</span>
                                <span class="font-bold text-slate-800">4 câu (4.0đ)</span>
                            </div>
                            <div class="flex items-center justify-between">
                                <span><i class="fa-solid fa-pen-to-square text-amber-500"></i> Phần 3: Trả lời ngắn</span>
                                <span class="font-bold text-slate-800">6 câu (1.5đ)</span>
                            </div>
                        </div>
                    </div>
                    <div class="space-y-2 pt-2 border-t border-slate-100">
                        <a href="/hoa/lop-12/de-1/" class="w-full py-3 bg-indigo-600 hover:bg-indigo-700 text-white font-extrabold text-sm rounded-xl shadow-md transition-all flex items-center justify-center gap-2">
                            <i class="fa-solid fa-play"></i> Làm Đề Số 1 Ngay
                        </a>
                        <div class="text-center text-[11px] text-slate-400">Đường dẫn tắt: <a href="/hoa/de1/" class="text-indigo-600 hover:underline">/hoa/de1/</a></div>
                    </div>
                </div>

                <!-- Đề 2 -->
                <div class="bg-white rounded-2xl border-2 border-slate-200 hover:border-purple-500 p-6 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between space-y-5 group">
                    <div class="space-y-4">
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-extrabold px-3 py-1 rounded-lg bg-purple-100 text-purple-800">ĐỀ THI SỐ 02</span>
                            <span class="text-xs font-bold text-slate-500 flex items-center gap-1.5"><i class="fa-regular fa-clock text-amber-500"></i> 50 phút</span>
                        </div>
                        <div>
                            <h3 class="font-extrabold text-slate-900 text-lg group-hover:text-purple-600 transition-colors leading-snug">
                                Ôn Tập Tới Hết Chương 3 (Hợp Chất Chứa N)
                            </h3>
                            <p class="text-xs text-slate-500 mt-1">Phạm vi: Este, Lipid, Carbohydrate, Amine, Amino acid, Peptide & Protein (Mã 01).</p>
                        </div>
                        <div class="bg-slate-50 rounded-xl p-3 space-y-1.5 text-xs text-slate-600 border border-slate-100">
                            <div class="flex items-center justify-between">
                                <span><i class="fa-solid fa-circle-question text-purple-500"></i> Phần 1: Nhiều lựa chọn</span>
                                <span class="font-bold text-slate-800">18 câu (4.5đ)</span>
                            </div>
                            <div class="flex items-center justify-between">
                                <span><i class="fa-solid fa-circle-check text-emerald-500"></i> Phần 2: Đúng / Sai</span>
                                <span class="font-bold text-slate-800">4 câu (4.0đ)</span>
                            </div>
                            <div class="flex items-center justify-between">
                                <span><i class="fa-solid fa-pen-to-square text-amber-500"></i> Phần 3: Trả lời ngắn</span>
                                <span class="font-bold text-slate-800">6 câu (1.5đ)</span>
                            </div>
                        </div>
                    </div>
                    <div class="space-y-2 pt-2 border-t border-slate-100">
                        <a href="/hoa/lop-12/de-2/" class="w-full py-3 bg-purple-600 hover:bg-purple-700 text-white font-extrabold text-sm rounded-xl shadow-md transition-all flex items-center justify-center gap-2">
                            <i class="fa-solid fa-play"></i> Làm Đề Số 2 Ngay
                        </a>
                        <div class="text-center text-[11px] text-slate-400">Đường dẫn tắt: <a href="/hoa/de2/" class="text-purple-600 hover:underline">/hoa/de2/</a></div>
                    </div>
                </div>

                <!-- Đề 3 -->
                <div class="bg-white rounded-2xl border-2 border-slate-200 hover:border-emerald-500 p-6 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between space-y-5 group">
                    <div class="space-y-4">
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-extrabold px-3 py-1 rounded-lg bg-emerald-100 text-emerald-800">ĐỀ THI SỐ 03</span>
                            <span class="text-xs font-bold text-slate-500 flex items-center gap-1.5"><i class="fa-regular fa-clock text-amber-500"></i> 50 phút</span>
                        </div>
                        <div>
                            <h3 class="font-extrabold text-slate-900 text-lg group-hover:text-emerald-600 transition-colors leading-snug">
                                Ôn Tập Tới Hết Chương 3 (Chuẩn Cấu Trúc 2026)
                            </h3>
                            <p class="text-xs text-slate-500 mt-1">Phạm vi: Toàn diện Chương 1, 2, 3 với phổ hồng ngoại IR, phản ứng màu Biuret, bài toán phân hóa.</p>
                        </div>
                        <div class="bg-slate-50 rounded-xl p-3 space-y-1.5 text-xs text-slate-600 border border-slate-100">
                            <div class="flex items-center justify-between">
                                <span><i class="fa-solid fa-circle-question text-emerald-500"></i> Phần 1: Nhiều lựa chọn</span>
                                <span class="font-bold text-slate-800">18 câu (4.5đ)</span>
                            </div>
                            <div class="flex items-center justify-between">
                                <span><i class="fa-solid fa-circle-check text-emerald-500"></i> Phần 2: Đúng / Sai</span>
                                <span class="font-bold text-slate-800">4 câu (4.0đ)</span>
                            </div>
                            <div class="flex items-center justify-between">
                                <span><i class="fa-solid fa-pen-to-square text-amber-500"></i> Phần 3: Trả lời ngắn</span>
                                <span class="font-bold text-slate-800">6 câu (1.5đ)</span>
                            </div>
                        </div>
                    </div>
                    <div class="space-y-2 pt-2 border-t border-slate-100">
                        <a href="/hoa/lop-12/de-3/" class="w-full py-3 bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-sm rounded-xl shadow-md transition-all flex items-center justify-center gap-2">
                            <i class="fa-solid fa-play"></i> Làm Đề Số 3 Ngay
                        </a>
                        <div class="text-center text-[11px] text-slate-400">Đường dẫn tắt: <a href="/hoa/de3/" class="text-emerald-600 hover:underline">/hoa/de3/</a></div>
                    </div>
                </div>

            </div>
        </section>

        <!-- Khung Chương Trình Học Kì I & II Hóa Học 12 -->
        <section class="bg-white rounded-3xl border border-slate-200 p-6 sm:p-8 shadow-sm space-y-6">
            <div class="border-b border-slate-100 pb-4">
                <span class="text-xs font-bold text-purple-600 uppercase tracking-wider">CHƯƠNG TRÌNH GDPT 2018</span>
                <h3 class="text-xl font-extrabold text-slate-900 mt-1">Cấu Trúc Các Chương Môn Hóa Học Lớp 12</h3>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 text-xs">
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-100 space-y-2">
                    <div class="font-bold text-indigo-700 text-sm flex items-center gap-2">
                        <span class="w-6 h-6 rounded-lg bg-indigo-100 text-indigo-700 flex items-center justify-center text-xs">1</span>
                        Chương 1: Este - Lipit
                    </div>
                    <p class="text-slate-600">Este, chất béo, xà phòng và chất giặt rửa tổng hợp. Phản ứng xà phòng hóa và ứng dụng thực tiễn.</p>
                </div>
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-100 space-y-2">
                    <div class="font-bold text-indigo-700 text-sm flex items-center gap-2">
                        <span class="w-6 h-6 rounded-lg bg-indigo-100 text-indigo-700 flex items-center justify-center text-xs">2</span>
                        Chương 2: Cacbohiđrat
                    </div>
                    <p class="text-slate-600">Glucose, fructose, saccharose, maltose, tinh bột và cellulose. Cấu tạo, phản ứng tráng bạc và ứng dụng.</p>
                </div>
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-100 space-y-2">
                    <div class="font-bold text-indigo-700 text-sm flex items-center gap-2">
                        <span class="w-6 h-6 rounded-lg bg-indigo-100 text-indigo-700 flex items-center justify-center text-xs">3</span>
                        Chương 3: Hợp Chất Chứa N
                    </div>
                    <p class="text-slate-600">Amine, amino acid, peptide và protein. Tính bazơ của amin, phản ứng màu Biuret, đông tụ protein.</p>
                </div>
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-100 space-y-2">
                    <div class="font-bold text-slate-700 text-sm flex items-center gap-2">
                        <span class="w-6 h-6 rounded-lg bg-slate-200 text-slate-700 flex items-center justify-center text-xs">4</span>
                        Chương 4: Polymer
                    </div>
                    <p class="text-slate-600">Khái niệm, phân loại, cấu trúc, phương pháp điều chế và ứng dụng của polymer và vật liệu polymer.</p>
                </div>
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-100 space-y-2">
                    <div class="font-bold text-slate-700 text-sm flex items-center gap-2">
                        <span class="w-6 h-6 rounded-lg bg-slate-200 text-slate-700 flex items-center justify-center text-xs">5</span>
                        Chương 5: Pin & Điện Phân
                    </div>
                    <p class="text-slate-600">Cặp oxi hóa - khử, pin Galvani, thế điện cực chuẩn và các quá trình điện phân dung dịch/nóng chảy.</p>
                </div>
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-100 space-y-2">
                    <div class="font-bold text-slate-700 text-sm flex items-center gap-2">
                        <span class="w-6 h-6 rounded-lg bg-slate-200 text-slate-700 flex items-center justify-center text-xs">6</span>
                        Chương 6: Đại Cương Kim Loại
                    </div>
                    <p class="text-slate-600">Tính chất vật lí, hóa học của kim loại, ăn mòn kim loại, kim loại chuyển tiếp và phức chất.</p>
                </div>
            </div>
        </section>

    </main>

    <!-- Footer -->
    <footer class="bg-slate-900 text-slate-400 text-xs border-t border-slate-800 py-8 mt-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-4 text-center sm:text-left">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-4 border-b border-slate-800 pb-4">
                <a href="/" class="flex items-center gap-2.5">
                    <img src="/favicon.svg" alt="Vatli102" class="w-7 h-7 rounded-lg">
                    <span class="font-extrabold text-base text-white">Vatli102.com - Cổng Học Liệu Số Toàn Diện</span>
                </a>
                <div class="flex flex-wrap items-center gap-4 text-xs">
                    <a href="/" class="hover:text-white transition-colors">Trang chủ</a>
                    <a href="/hoa/" class="hover:text-white transition-colors">Môn Hóa Học</a>
                    <a href="/hoa/lop-12/" class="text-white font-bold">Hóa Học 12</a>
                    <a href="/gioi-thieu.html" class="hover:text-white transition-colors">Giới thiệu</a>
                    <a href="/lien-he.html" class="hover:text-white transition-colors">Liên hệ</a>
                </div>
            </div>
            <p class="text-[11px] text-slate-500">© 2026 Vatli102.com - Hệ thống bài giảng và bài tập số chuẩn mực theo chương trình GDPT 2018.</p>
        </div>
    </footer>

</body>
</html>'''

os.makedirs(os.path.join(EXPORT_DIR, "lop-12"), exist_ok=True)
with open(os.path.join(EXPORT_DIR, "lop-12", "index.html"), 'w', encoding='utf-8') as f:
    f.write(lop12_hub_html)

print("Đã tạo vatli102_export/hoa/lop-12/index.html")

print("\nHoàn tất chuẩn bị gói học liệu Môn Hóa cho Vatli102.com!")
