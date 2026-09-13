"""
Script: export_to_html_quiz.py
Purpose: Export Chemistry worksheets and chapter exams into interactive HTML quizzes matching vatli102.com style:
- Part 1: Multiple Choice (16 questions for Grade 10/11, 18 questions for Grade 12)
- Part 2: True/False with contextual statements (2 questions for Grade 10/11, 4 questions for Grade 12)
- Part 3: Short answer / numeric calculations (4 questions for Grade 10/11, 6 questions for Grade 12)
- MathJax 3 support for chemistry formulas & equations
- Confetti celebration, timer, scoring, detailed explanations
- No essay part in HTML (Docx only)
"""

import os
import json
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>📝 {{TITLE}} - Trắc Nghiệm Online Hóa Học</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <script>
        window.MathJax = {
            tex: {
                inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
                displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
                processEscapes: true
            },
            options: {
                skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
            }
        };
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        :root {
            --primary: #0284c7;
            --primary-hover: #0369a1;
            --secondary: #0d9488;
            --bg-body: #f8fafc;
            --card-bg: #ffffff;
            --text-dark: #0f172a;
            --text-muted: #64748b;
            --border: #e2e8f0;
        }

        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-body);
            color: var(--text-dark);
            line-height: 1.65;
            padding-bottom: 40px;
        }

        p, .question-title, .tf-row > div:first-child, .explanation-box, .score-desc, .form-group label {
            text-align: justify;
        }

        .sticky-header {
            position: sticky; top: 0; z-index: 1000;
            background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px);
            border-bottom: 1px solid var(--border); box-shadow: 0 4px 15px rgba(0, 0, 0, 0.04);
        }
        .header-container {
            max-width: 920px; margin: 0 auto; padding: 10px 15px;
            display: flex; justify-content: space-between; align-items: center;
        }
        .site-logo { display: flex; align-items: center; gap: 8px; text-decoration: none; }
        .logo-text {
            font-size: 1.25rem; font-weight: 800;
            background: linear-gradient(135deg, #0284c7, #0d9488);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }
        .nav-links { display: flex; gap: 18px; align-items: center; }
        .timer-badge {
            background: #fee2e2; color: #ef4444; padding: 4px 10px; border-radius: 8px;
            font-weight: 800; font-size: 0.9rem; display: flex; align-items: center; gap: 5px;
        }

        .quiz-container { max-width: 920px; margin: 20px auto; padding: 0 15px; min-height: 80vh; }

        .exam-banner {
            background: linear-gradient(135deg, #0f172a, #0369a1, #0f766e); color: white;
            padding: 2.2rem 1.5rem; border-radius: 20px; text-align: center; margin-bottom: 20px;
            box-shadow: 0 10px 25px rgba(15,23,42,0.25);
        }
        .exam-banner h1 { font-size: 1.7rem; font-weight: 800; margin-bottom: 8px; }
        .exam-banner p { font-size: 0.95rem; color: #e0f2fe; text-align: center; }
        .badge-exam { display: inline-block; background: rgba(255,255,255,0.2); padding: 4px 14px; border-radius: 20px; font-size: 0.82rem; font-weight: 700; margin-top: 10px; }

        .login-card {
            background: white; border-radius: 16px; padding: 30px 20px; text-align: center;
            border: 1px solid var(--border); box-shadow: 0 10px 25px rgba(0,0,0,0.05); margin-bottom: 30px;
        }
        .form-group { margin-bottom: 15px; text-align: left; max-width: 400px; margin-left: auto; margin-right: auto; }
        .form-group label { display: block; font-weight: 700; font-size: 0.85rem; margin-bottom: 5px; color: #334155; }
        .form-control { width: 100%; padding: 10px 14px; border: 1px solid var(--border); border-radius: 8px; font-size: 0.95rem; outline: none; }
        .btn-start {
            background: linear-gradient(135deg, var(--primary), var(--primary-hover)); color: white; border: none;
            padding: 12px 30px; border-radius: 10px; font-weight: 700; font-size: 1rem; cursor: pointer;
            box-shadow: 0 4px 14px rgba(2,132,199,0.3); transition: all 0.2s; width: 100%; max-width: 400px; margin-top: 10px;
        }
        .btn-start:hover { transform: translateY(-2px); }

        .student-info-bar {
            background: #f1f5f9; padding: 10px 16px; border-radius: 10px; margin-bottom: 20px;
            display: flex; justify-content: space-between; align-items: center; font-size: 0.9rem; font-weight: 600;
        }

        .progress-container { margin-bottom: 25px; }
        .progress-bar-bg { width: 100%; height: 8px; background: #e2e8f0; border-radius: 4px; overflow: hidden; }
        .progress-bar-fill { height: 100%; width: 0%; background: linear-gradient(90deg, #0284c7, #0d9488); transition: width 0.3s; }
        .progress-text { display: flex; justify-content: space-between; font-size: 0.82rem; color: var(--text-muted); margin-top: 5px; }

        .section-header {
            background: #f0f9ff; color: #0369a1; padding: 12px 18px; border-radius: 12px;
            font-weight: 800; font-size: 1.05rem; margin: 30px 0 15px 0; border-left: 5px solid #0284c7;
        }

        .question-card {
            background: var(--card-bg); border: 1px solid var(--border); border-radius: 14px;
            padding: 18px; margin-bottom: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.02);
            transition: border-color 0.2s;
        }
        .question-card:hover { border-color: #cbd5e1; }
        .question-num { font-weight: 800; color: var(--primary); margin-right: 6px; }
        .question-title { font-size: 0.98rem; font-weight: 600; margin-bottom: 12px; color: #1e293b; line-height: 1.6; }
        .question-context {
            background: #f8fafc; border-left: 4px solid var(--primary);
            padding: 12px 16px; border-radius: 8px; margin-bottom: 14px;
            font-size: 0.94rem; color: #334155; line-height: 1.65; text-align: justify;
        }

        .options-grid { display: flex; flex-direction: column; gap: 8px; }
        .option-item {
            display: flex; align-items: center; gap: 10px; padding: 10px 14px;
            border: 1px solid var(--border); border-radius: 8px; cursor: pointer;
            transition: all 0.15s; font-size: 0.92rem;
        }
        .option-item:hover { background: #f8fafc; border-color: #94a3b8; }
        .option-item.selected { background: #f0f9ff; border-color: var(--primary); color: #0369a1; font-weight: 600; }
        .option-label { font-weight: 700; width: 22px; height: 22px; display: flex; align-items: center; justify-content: center; border-radius: 50%; background: #f1f5f9; font-size: 0.8rem; flex-shrink: 0; }
        .option-item.selected .option-label { background: var(--primary); color: white; }

        .tf-row { display: flex; justify-content: space-between; align-items: center; padding: 10px 12px; border-bottom: 1px solid #f1f5f9; gap: 10px; }
        .tf-row:last-child { border-bottom: none; }
        .tf-btns { display: flex; gap: 6px; flex-shrink: 0; }
        .tf-btn {
            padding: 5px 14px; border: 1px solid var(--border); border-radius: 6px;
            background: white; font-size: 0.82rem; font-weight: 700; cursor: pointer; transition: all 0.15s;
        }
        .tf-btn.active-true { background: #10b981; border-color: #10b981; color: white; }
        .tf-btn.active-false { background: #ef4444; border-color: #ef4444; color: white; }

        .short-answer-box { display: flex; align-items: center; gap: 12px; margin-top: 10px; flex-wrap: wrap; }
        .short-input {
            padding: 10px 14px; border: 1.5px solid var(--border); border-radius: 8px;
            font-size: 1rem; width: 160px; font-weight: 700; outline: none; transition: all 0.2s;
        }
        .short-input:focus { border-color: var(--primary); }
        .short-input.input-correct { border-color: #22c55e !important; background: #f0fdf4 !important; color: #166534 !important; }
        .short-input.input-incorrect { border-color: #ef4444 !important; background: #fef2f2 !important; color: #991c1c !important; }

        .option-item.correct {
            background: #dcfce7 !important; border-color: #22c55e !important; color: #15803d !important; font-weight: 700;
        }
        .option-item.correct .option-label { background: #22c55e !important; color: white !important; }
        .option-item.incorrect {
            background: #fee2e2 !important; border-color: #ef4444 !important; color: #b91c1c !important;
        }
        .option-item.incorrect .option-label { background: #ef4444 !important; color: white !important; }

        .explanation-box {
            margin-top: 14px; padding: 14px 16px; border-radius: 10px; background: #f8fafc;
            border-left: 4px solid var(--primary); font-size: 0.9rem; color: #334155; display: none;
        }
        .explanation-box.show { display: block; }

        .btn-submit {
            display: block; width: 100%; max-width: 340px; margin: 30px auto 15px auto; padding: 14px 24px;
            background: linear-gradient(135deg, #10b981, #059669); color: white; border: none;
            border-radius: 12px; font-size: 1.1rem; font-weight: 800; cursor: pointer;
            box-shadow: 0 6px 20px rgba(16,185,129,0.3); transition: all 0.2s;
        }
        .btn-submit:hover { transform: translateY(-2px); }

        .results-panel {
            display: none; background: white; border-radius: 20px; padding: 35px 25px;
            border: 1px solid var(--border); box-shadow: 0 10px 30px rgba(0,0,0,0.08);
            margin-top: 30px; text-align: center;
        }
        .score-circle {
            width: 120px; height: 120px; border-radius: 50%;
            background: linear-gradient(135deg, #0284c7, #0d9488); color: white;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            margin: 0 auto 15px auto; box-shadow: 0 8px 20px rgba(2,132,199,0.35);
        }
        .score-val { font-size: 2.3rem; font-weight: 900; line-height: 1; }
        .score-max { font-size: 0.8rem; font-weight: 700; opacity: 0.9; margin-top: 2px; }
        .score-title { font-size: 1.5rem; font-weight: 800; color: #0f172a; margin-bottom: 6px; }
        .score-desc { font-size: 0.95rem; color: var(--text-muted); margin-bottom: 20px; text-align: center; }

        .details-summary {
            display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 12px;
            margin: 20px 0; text-align: center;
        }
        .summary-card { background: #f8fafc; border: 1px solid var(--border); border-radius: 12px; padding: 14px 10px; }
        .summary-num { font-size: 1.35rem; font-weight: 800; margin-bottom: 2px; }
        .summary-label { font-size: 0.8rem; color: var(--text-muted); font-weight: 600; }

        footer {
            background: #0f172a; color: #94a3b8; text-align: center; padding: 25px 15px;
            font-size: 0.85rem; margin-top: 50px;
        }
    </style>
</head>
<body>

    <header class="sticky-header">
        <div class="header-container">
            <a href="#" class="site-logo">
                <span class="logo-text">🧪 Hóa Học Online</span>
            </a>
            <div class="nav-links">
                <span id="timerBadge" class="timer-badge" style="display:none;"><i class="fa-regular fa-clock"></i> <span id="timerText">{{DURATION}}:00</span></span>
            </div>
        </div>
    </header>

    <div class="quiz-container">
        <div class="exam-banner">
            <span class="badge-exam">{{BADGE}}</span>
            <h1 style="margin-top: 10px;">{{TITLE}}</h1>
            <p>Thời gian: {{DURATION}} phút • Bối cảnh thực tế & Suy luận lí thuyết nâng cao</p>
        </div>

        <div id="loginCard" class="login-card">
            <h2 style="font-size: 1.3rem; margin-bottom: 8px; color: #1e293b;">Thông Tin Học Sinh</h2>
            <p style="font-size: 0.88rem; color: #64748b; margin-bottom: 20px;">Vui lòng điền Họ tên và Lớp để bắt đầu làm bài và nhận kết quả tự động.</p>
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
                    <span>Tiến độ làm bài</span>
                    <span id="progressCount">0 / {{TOTAL_QUESTIONS}} câu</span>
                </div>
            </div>

            <div class="section-header">
                📌 PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn ({{PART1_COUNT}} câu)
            </div>
            <p style="font-size: 0.88rem; color: #64748b; margin-bottom: 15px;">Thí sinh trả lời từ Câu 1 đến Câu {{PART1_COUNT}}. Mỗi câu chọn 1 phương án đúng.</p>
            <div id="part1Container"></div>

            <div class="section-header">
                📌 PHẦN II. Câu trắc nghiệm đúng / sai ({{PART2_COUNT}} câu)
            </div>
            <p style="font-size: 0.88rem; color: #64748b; margin-bottom: 15px;">Thí sinh chọn Đúng hoặc Sai cho mỗi ý a, b, c, d. Barem điểm: Đúng 1 ý = 0,1đ; Đúng 2 ý = 0,25đ; Đúng 3 ý = 0,5đ; Đúng 4 ý = 1,0đ.</p>
            <div id="part2Container"></div>

            <div class="section-header">
                📌 PHẦN III. Câu trắc nghiệm trả lời ngắn ({{PART3_COUNT}} câu)
            </div>
            <p style="font-size: 0.88rem; color: #64748b; margin-bottom: 15px;">Thí sinh điền đáp số ngắn gọn vào ô trống (dạng số hoặc số lượng phát biểu đúng).</p>
            <div id="part3Container"></div>

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
                <div class="score-title" id="scoreTitle">Hoàn Thành Bài Làm!</div>
                <div class="score-desc" id="scoreDesc">Xem hướng dẫn giải chi tiết cho từng câu hỏi bên dưới.</div>

                <div class="details-summary">
                    <div class="summary-card">
                        <div class="summary-num" style="color: #22c55e;" id="correctCountText">0</div>
                        <div class="summary-label">Số ý trả lời đúng</div>
                    </div>
                    <div class="summary-card">
                        <div class="summary-num" style="color: #ef4444;" id="incorrectCountText">0</div>
                        <div class="summary-label">Số ý trả lời sai</div>
                    </div>
                    <div class="summary-card">
                        <div class="summary-num" style="color: #0284c7;" id="gradeText">0.0/10</div>
                        <div class="summary-label">Tổng điểm đạt được</div>
                    </div>
                    <div class="summary-card">
                        <div class="summary-num" style="color: #0d9488;" id="timeSpentText">--:--</div>
                        <div class="summary-label">Thời gian làm bài</div>
                    </div>
                <div id="sheetSyncStatus" style="display: none; margin: 15px auto; padding: 12px 18px; border-radius: 10px; font-size: 0.92rem; font-weight: 600; background: #f0fdf4; border: 1.5px solid #86efac; color: #166534; max-width: 550px; text-align: center;"></div>
            </div>
        </div>
    </div>

    <footer>
        <p>Hệ thống Học tập & Kiểm tra Hóa học Online theo Chương trình GDPT 2018</p>
    </footer>

    <script>
        const part1Data = {{PART1_JSON}};
        const part2Data = {{PART2_JSON}};
        const part3Data = {{PART3_JSON}};
        const GOOGLE_SHEET_URL = "{{GOOGLE_SHEET_URL}}";

        let userPart1 = {};
        let userPart2 = {};
        let userPart3 = {};
        let examSubmitted = false;
        let timerInterval = null;
        let totalTimeSeconds = {{DURATION}} * 60;
        let timeRemaining = totalTimeSeconds;

        function sendResultsToGoogleSheet(data) {
            if (!GOOGLE_SHEET_URL || GOOGLE_SHEET_URL.trim() === "" || GOOGLE_SHEET_URL.includes("DAN_LINK")) {
                return;
            }
            const statusEl = document.getElementById("sheetSyncStatus");
            if (statusEl) {
                statusEl.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Đang tự động lưu kết quả vào Google Sheet của giáo viên...';
                statusEl.style.display = 'block';
            }

            fetch(GOOGLE_SHEET_URL, {
                method: 'POST',
                mode: 'no-cors',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            })
            .then(() => {
                if (statusEl) {
                    statusEl.innerHTML = '<i class="fa-solid fa-circle-check" style="color: #16a34a;"></i> <strong>Đã lưu kết quả thành công</strong> vào sổ điểm Google Sheet của giáo viên!';
                }
            })
            .catch((err) => {
                console.error("Lỗi đồng bộ Google Sheet:", err);
                if (statusEl) {
                    statusEl.innerHTML = '<i class="fa-solid fa-circle-info" style="color: #0284c7;"></i> Đã hoàn thành bài làm trên hệ thống.';
                }
            });
        }

        function startExam() {
            const name = document.getElementById('studentName').value.trim();
            const sClass = document.getElementById('studentClass').value.trim();
            if (!name || !sClass) {
                alert('Vui lòng nhập đầy đủ Họ tên và Lớp trước khi bắt đầu!');
                return;
            }
            document.getElementById('displayName').innerText = name;
            document.getElementById('displayClass').innerText = sClass;
            document.getElementById('loginCard').style.display = 'none';
            document.getElementById('examWorkspace').style.display = 'block';
            document.getElementById('timerBadge').style.display = 'flex';

            renderPart1();
            renderPart2();
            renderPart3();
            startTimer();
            if (window.MathJax) { MathJax.typesetPromise(); }
        }

        function startTimer() {
            timerInterval = setInterval(() => {
                if (timeRemaining <= 0) {
                    clearInterval(timerInterval);
                    alert('Hết giờ làm bài! Hệ thống tự động nộp bài.');
                    submitExam();
                    return;
                }
                timeRemaining--;
                const mins = Math.floor(timeRemaining / 60);
                const secs = timeRemaining % 60;
                document.getElementById('timerText').innerText = 
                    `${mins < 10 ? '0' : ''}${mins}:${secs < 10 ? '0' : ''}${secs}`;
            }, 1000);
        }

        function formatContent(str) {
            if (str === null || str === undefined) return '';
            return String(str).replace(/\\n/g, '<br>');
        }

        function renderPart1() {
            const container = document.getElementById('part1Container');
            let html = '';
            part1Data.forEach((q, idx) => {
                html += `
                <div class="question-card" id="card-p1-${q.id}">
                    <div class="question-title">
                        <span class="question-num">Câu ${idx + 1}:</span> ${formatContent(q.question)}
                    </div>
                    <div class="options-grid">
                        ${Object.entries(q.options).map(([k, v]) => `
                            <div class="option-item" id="opt-${q.id}-${k}" onclick="selectPart1(${q.id}, '${k}')">
                                <span class="option-label">${k}</span>
                                <span>${formatContent(v)}</span>
                            </div>
                        `).join('')}
                    </div>
                    <div class="explanation-box" id="exp-p1-${q.id}">
                        <strong>💡 Hướng dẫn giải:</strong><br>${formatContent(q.explanation)}
                    </div>
                </div>`;
            });
            container.innerHTML = html;
        }

        function selectPart1(qId, option) {
            if (examSubmitted) return;
            userPart1[qId] = option;
            const q = part1Data.find(item => item.id === qId);
            Object.keys(q.options).forEach(k => {
                const el = document.getElementById(`opt-${qId}-${k}`);
                if (el) el.classList.remove('selected');
            });
            const selectedEl = document.getElementById(`opt-${qId}-${option}`);
            if (selectedEl) selectedEl.classList.add('selected');
            updateProgress();
        }

        function renderPart2() {
            const container = document.getElementById('part2Container');
            let html = '';
            part2Data.forEach((q, idx) => {
                if (!userPart2[q.id]) userPart2[q.id] = {};
                html += `
                <div class="question-card" id="card-p2-${q.id}">
                    <div class="question-title">
                        <span class="question-num">Câu ${idx + 1}:</span> <strong>${formatContent(q.title || '')}</strong>
                    </div>
                    ${q.context ? `<div class="question-context">${formatContent(q.context)}</div>` : ''}
                    <div class="tf-table">
                        ${Object.entries(q.statements).map(([k, text]) => `
                            <div class="tf-row">
                                <div style="font-size: 0.92rem; line-height: 1.55;"><strong>${k})</strong> ${formatContent(text)}</div>
                                <div class="tf-btns">
                                    <button class="tf-btn" id="btn-tf-${q.id}-${k}-true" onclick="selectPart2(${q.id}, '${k}', 'Đ')">Đúng</button>
                                    <button class="tf-btn" id="btn-tf-${q.id}-${k}-false" onclick="selectPart2(${q.id}, '${k}', 'S')">Sai</button>
                                </div>
                            </div>
                        `).join('')}
                    </div>
                    <div class="explanation-box" id="exp-p2-${q.id}">
                        <strong>💡 Hướng dẫn giải chi tiết:</strong><br>
                        ${Object.entries(q.explanations || {}).map(([k, exp]) => `<strong>${k})</strong> ${formatContent(exp)}`).join('<br>')}
                    </div>
                </div>`;
            });
            container.innerHTML = html;
        }

        function selectPart2(qId, key, val) {
            if (examSubmitted) return;
            userPart2[qId][key] = val;
            const btnT = document.getElementById(`btn-tf-${qId}-${key}-true`);
            const btnF = document.getElementById(`btn-tf-${qId}-${key}-false`);
            if (val === 'Đ') {
                btnT.classList.add('active-true');
                btnF.classList.remove('active-false');
            } else {
                btnF.classList.add('active-false');
                btnT.classList.remove('active-true');
            }
            updateProgress();
        }

        function renderPart3() {
            const container = document.getElementById('part3Container');
            let html = '';
            part3Data.forEach((q, idx) => {
                html += `
                <div class="question-card" id="card-p3-${q.id}">
                    <div class="question-title">
                        <span class="question-num">Câu ${idx + 1}:</span> ${formatContent(q.question)}
                    </div>
                    <div class="short-answer-box">
                        <label style="font-size: 0.9rem; font-weight: 600;">Đáp số:</label>
                        <input type="text" class="short-input" id="input-p3-${q.id}" oninput="recordPart3(${q.id}, this.value)" placeholder="Nhập số...">
                    </div>
                    <div class="explanation-box" id="exp-p3-${q.id}">
                        <strong>💡 Đáp án chuẩn:</strong> <code>${q.answer}</code><br>
                        <strong>Hướng dẫn giải chi tiết:</strong><br>${formatContent(q.explanation)}
                    </div>
                </div>`;
            });
            container.innerHTML = html;
        }

        function recordPart3(qId, val) {
            if (examSubmitted) return;
            userPart3[qId] = val.trim();
            updateProgress();
        }

        function updateProgress() {
            let answered = Object.keys(userPart1).length;
            part2Data.forEach(q => {
                if (userPart2[q.id]) answered += Object.keys(userPart2[q.id]).length > 0 ? 1 : 0;
            });
            answered += Object.keys(userPart3).filter(k => userPart3[k] !== '').length;
            const total = part1Data.length + part2Data.length + part3Data.length;
            const pct = Math.min(100, Math.round((answered / total) * 100));
            document.getElementById('progressFill').style.width = pct + '%';
            document.getElementById('progressCount').innerText = `${answered} / ${total} câu`;
        }

        function confirmSubmitExam() {
            if (confirm('Bạn có chắc chắn muốn nộp bài và kết thúc bài thi không?')) {
                submitExam();
            }
        }

        function submitExam() {
            examSubmitted = true;
            clearInterval(timerInterval);
            document.getElementById('btnSubmit').style.display = 'none';

            let totalPoints = 0;
            let totalCorrectItems = 0;
            let totalIncorrectItems = 0;

            const p1Weight = {{PART1_WEIGHT}};
            part1Data.forEach(q => {
                const userAns = userPart1[q.id];
                const isCorrect = userAns === q.answer;
                if (isCorrect) {
                    totalPoints += p1Weight;
                    totalCorrectItems++;
                } else {
                    totalIncorrectItems++;
                }
                Object.keys(q.options).forEach(k => {
                    const el = document.getElementById(`opt-${q.id}-${k}`);
                    if (k === q.answer) el.classList.add('correct');
                    else if (k === userAns) el.classList.add('incorrect');
                });
                document.getElementById(`exp-p1-${q.id}`).classList.add('show');
            });

            const p2Scale = [0, 0.1, 0.25, 0.5, 1.0];
            part2Data.forEach(q => {
                let subCorrect = 0;
                Object.entries(q.answers).forEach(([k, correctVal]) => {
                    const userVal = (userPart2[q.id] && userPart2[q.id][k]) ? userPart2[q.id][k] : '';
                    if (userVal === correctVal) {
                        subCorrect++;
                        totalCorrectItems++;
                    } else {
                        totalIncorrectItems++;
                    }
                });
                totalPoints += p2Scale[subCorrect];
                document.getElementById(`exp-p2-${q.id}`).classList.add('show');
            });

            const p3Weight = {{PART3_WEIGHT}};
            part3Data.forEach(q => {
                const userVal = (userPart3[q.id] || '').replace(',', '.').replace(/\\s+/g, '');
                const correctVal = String(q.answer).replace(',', '.').replace(/\\s+/g, '');
                const inputEl = document.getElementById(`input-p3-${q.id}`);
                inputEl.disabled = true;
                if (userVal !== '' && (userVal === correctVal || Math.abs(parseFloat(userVal) - parseFloat(correctVal)) < 0.05)) {
                    totalPoints += p3Weight;
                    totalCorrectItems++;
                    inputEl.classList.add('input-correct');
                } else {
                    totalIncorrectItems++;
                    inputEl.classList.add('input-incorrect');
                }
                document.getElementById(`exp-p3-${q.id}`).classList.add('show');
            });

            const finalScore = Math.min(10.0, Math.max(0.0, totalPoints)).toFixed(2);
            document.getElementById('scoreCircle').innerText = finalScore;
            document.getElementById('gradeText').innerText = `${finalScore}/10`;
            document.getElementById('correctCountText').innerText = totalCorrectItems;
            document.getElementById('incorrectCountText').innerText = totalIncorrectItems;

            const spentSeconds = totalTimeSeconds - timeRemaining;
            const sMins = Math.floor(spentSeconds / 60);
            const sSecs = spentSeconds % 60;
            document.getElementById('timeSpentText').innerText = 
                `${sMins < 10 ? '0' : ''}${sMins}:${sSecs < 10 ? '0' : ''}${sSecs}`;

            document.getElementById('resultsPanel').style.display = 'block';
            document.getElementById('resultsPanel').scrollIntoView({ behavior: 'smooth' });

            sendResultsToGoogleSheet({
                timestamp: new Date().toLocaleString("vi-VN", { timeZone: "Asia/Ho_Chi_Minh" }),
                studentName: document.getElementById('displayName').innerText,
                studentClass: document.getElementById('displayClass').innerText,
                score: finalScore,
                correctCount: totalCorrectItems,
                incorrectCount: totalIncorrectItems,
                timeSpent: document.getElementById('timeSpentText').innerText,
                examTitle: "{{TITLE}}"
            });

            if (window.MathJax && window.MathJax.typesetPromise) {
                MathJax.typesetPromise();
            }

            if (parseFloat(finalScore) >= 7.0 && typeof confetti === 'function') {
                confetti({ particleCount: 100, spread: 70, origin: { y: 0.6 } });
            }
        }
    </script>
</body>
</html>"""

def generate_quiz_html(data, output_path):
    grade = data.get('grade', 10)
    part1 = data.get('part1', [])
    part2 = data.get('part2', [])
    part3 = data.get('part3', [])

    if grade == 12:
        p1_weight = 0.25
        p3_weight = 0.25
    else:
        p1_weight = 0.25
        p3_weight = 1.0

    html = HTML_TEMPLATE
    html = html.replace('{{TITLE}}', data.get('title', 'Bài Tập Trắc Nghiệm Hóa Học'))
    html = html.replace('{{BADGE}}', data.get('badge', f'HÓA HỌC {grade} - GDPT 2018'))
    html = html.replace('{{DURATION}}', str(data.get('duration', 45 if grade < 12 else 50)))
    html = html.replace('{{TOTAL_QUESTIONS}}', str(len(part1) + len(part2) + len(part3)))
    html = html.replace('{{PART1_COUNT}}', str(len(part1)))
    html = html.replace('{{PART2_COUNT}}', str(len(part2)))
    html = html.replace('{{PART3_COUNT}}', str(len(part3)))
    html = html.replace('{{PART1_WEIGHT}}', str(p1_weight))
    html = html.replace('{{PART3_WEIGHT}}', str(p3_weight))
    default_sheet = "https://script.google.com/macros/s/AKfycbwRRiM81mghvA7cInvJgb4rPLzWOAE3s44wer0BJcURQ4hWwoykS19pkNQ9LyzH6Q8lTQ/exec"
    html = html.replace('{{GOOGLE_SHEET_URL}}', data.get('google_sheet_url') or default_sheet)
    html = html.replace('{{PART1_JSON}}', json.dumps(part1, ensure_ascii=False))
    html = html.replace('{{PART2_JSON}}', json.dumps(part2, ensure_ascii=False))
    html = html.replace('{{PART3_JSON}}', json.dumps(part3, ensure_ascii=False))

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Đã xuất file HTML trắc nghiệm online thành công: {output_path}')

if __name__ == '__main__':
    if len(sys.argv) > 2:
        json_in = sys.argv[1]
        html_out = sys.argv[2]
        with open(json_in, 'r', encoding='utf-8') as f:
            d = json.load(f)
        generate_quiz_html(d, html_out)
    else:
        print('Cách dùng: py scripts/export_to_html_quiz.py <quiz_data.json> <output.html>')
