# 🚀 NÂNG CẤP HỆ THỐNG — Chi Tiết & Hướng Dẫn

**Ngày:** 2026-06-25  
**Phiên bản:** 2.0 (Upgraded)  
**Trạng thái:** Blueprint sẵn sàng implement

---

## 📊 Tổng Quan Nâng Cấp

### Trước (v1.0)
```
User gửi yêu cầu
  ↓
AI tạo prompt
  ↓
Hiển thị sau khi hỏi "có muốn xem không?"
  ↓
Copy-paste (nếu cần)

❌ Vấn đề:
  - Chậm (2 bước hỏi)
  - Prompt mơ hồ (không extract chính xác)
  - Phong cách random (user chọn sai nhiều lần)
  - Tóm tắt (mất chi tiết)
```

### Sau (v2.0) — Nâng Cấp
```
User gửi yêu cầu
  ↓ (agent-tai-lieu-phong-cach)
Extract NGUYÊN VĂN + Gợi ý phong cách
  ↓
User xác nhận
  ↓ (agent-video-ngan-fast)
Tạo 5 files + HIỂN THỊ NGAY
  ↓
Copy-paste luôn (không hỏi)

✅ Cải thiện:
  - Nhanh (1 bước xác nhận)
  - Prompt chuẩn xác (extract 100%)
  - Phong cách smart (gợi ý analysis-based)
  - Chi tiết đầy đủ (không tóm tắt)
  - Hiển thị tự động (không hỏi)
```

---

## 📁 Files Mới Tạo

### Commands
- ✅ `commands/tao-video-ngan.md` — Command `/tao-video-ngan`

### Workflows
- ✅ `workflows/07-video-ngan-fast.md` — Workflow video ngắn

### Agents
- ✅ `agents/agent-video-ngan-fast.md` — Agent tạo video
- ✅ `agents/agent-tai-lieu-phong-cach.md` — **NEW** Agent analyze + recommend

### Guides
- ✅ `UPGRADE-GUIDE.md` — File này

---

## 🔧 Cách Implement

### STEP 1: Integrate Agent Phân Tích Tài Liệu (2–3 giờ)

#### 1A: File Upload Handler
```python
# Trong form onboarding, thêm:
@on_file_upload
def handle_file_upload(file):
  # Gọi agent-tai-lieu-phong-cach
  result = agent_tai_lieu_phong_cach.run({
    "file": file,
    "mon": selected_mon,
    "lop": selected_lop
  })
  
  # Hiển thị:
  # - Extracted content
  # - Top 3 phong cách (+ confidence)
  # - "Chọn phong cách nào?"
```

#### 1B: OCR + Text Extraction
```python
# Libraries cần:
# - PyPDF2 (PDF)
# - pytesseract + Pillow (OCR)
# - python-docx (DOCX)
# - langdetect (Vietnamese detection)

def extract_content(file):
  if file.endswith(".pdf"):
    return extract_pdf(file)
  elif file.endswith((".jpg", ".png")):
    return extract_image_via_ocr(file)
  elif file.endswith(".docx"):
    return extract_docx(file)
```

#### 1C: Content Analysis
```python
def analyze_content(text):
  # Detect content type
  # Count formulas
  # Count examples
  # Check complexity
  # → Return analysis dict
```

#### 1D: Preset Recommendation
```python
def recommend_presets(analysis):
  # Map analysis → Top 3 presets
  # Return with confidence %
  # Return with reason
```

---

### STEP 2: Upgrade `/tao-video-ngan` (3–4 giờ)

#### 2A: Script Generation
```python
def generate_script(
  mon, lop, chu_de, phong_cach,
  extracted_content=None  # NEW param
):
  # Load preset
  # Load knowledge base
  
  # If extracted_content provided:
  #   Use extracted formulas, examples, definitions
  #   Match 100% (không tự sáng tạo)
  # Else:
  #   Use knowledge base
  
  # Generate script
  # Return script
```

#### 2B: Quality Check
```python
def quality_check(script, extracted_content=None):
  checks = [
    ("Science accuracy", check_science),
    ("Timing = 60s", check_timing),
    ("Copy-paste ready", check_copy_paste),
    ("No placeholder", check_placeholder),
  ]
  
  if extracted_content:
    checks.append(
      ("Match extracted?", lambda: check_extracted_match(script, extracted_content))
    )
  
  # Return pass/fail + details
```

---

### STEP 3: Display Flow (2–3 giờ)

#### 3A: Auto-Display (Không hỏi)
```python
def create_and_display_video(params):
  # Generate files
  files = {
    "script": generate_script(...),
    "image_prompts": generate_image_prompts(...),
    "video_prompts": generate_video_prompts(...),
    "voice_script": generate_voice_script(...),
    "manifest": generate_manifest(...),
  }
  
  # Save to disk
  folder = create_output_folder()
  for name, content in files.items():
    save_file(f"{folder}/{name}.md", content)
  
  # Display in chat (NO "có muốn xem không?")
  display_message = format_display(files, folder)
  send_to_chat(display_message)
  
  return {
    "status": "SUCCESS",
    "files": files,
    "folder": folder,
    "display_sent": True
  }
```

---

## 🎯 Integration Map

```
form-onboarding
  │
  ├─ [User uploads file]
  │    ↓
  │ agent-tai-lieu-phong-cach
  │    ├─ extract_content()
  │    ├─ analyze_content()
  │    └─ recommend_presets() → TOP 3
  │    ↓
  │ [Display: "Chọn phong cách nào?"]
  │
  └─ [User chọn phong cách]
       ↓
    agent-video-ngan-fast
       ├─ generate_script()
       ├─ generate_image_prompts()
       ├─ generate_video_prompts()
       ├─ generate_voice_script()
       ├─ save_files()
       └─ display_in_chat() ← AUTO (NO hỏi)
       ↓
    [Chat shows: Script + 5 Image Prompts + 5 Video Prompts + Voice]
       ↓
    [User copy & use]
```

---

## 📋 Implementation Checklist

### Phase 1: Setup (1 giờ)
- [ ] Update dependencies (pytesseract, PyPDF2, python-docx, etc.)
- [ ] Create `/temp/` folder for extracted content
- [ ] Create `/dau-ra/prompt-video/` folder structure

### Phase 2: Agent Phân Tích (3–4 giờ)
- [ ] Implement `extract_content()` (PDF + OCR + DOCX)
- [ ] Implement `analyze_content()` (type + complexity)
- [ ] Implement `recommend_presets()` (confidence-based)
- [ ] Add preset mapping (content type → presets)
- [ ] Test with sample SGK files

### Phase 3: Upgrade Video Agent (3–4 giờ)
- [ ] Update `generate_script()` with extracted_content param
- [ ] Update quality_check to verify extracted match
- [ ] Implement auto-display (no "có muốn xem không?")
- [ ] Add timing validation
- [ ] Test with 3–5 scenarios

### Phase 4: Integration (2–3 giờ)
- [ ] Wire agents together
- [ ] Test full flow (upload → analyze → recommend → create → display)
- [ ] Handle error cases
- [ ] Performance testing

### Phase 5: Testing & QA (2 giờ)
- [ ] Test with various file types (PDF, JPG, PNG, DOCX)
- [ ] Test with different subjects (Vật lý, Hóa, Sinh, Toán)
- [ ] Test with different presets
- [ ] Verify extracted content accuracy (100% match)
- [ ] Verify recommendations (user feedback)

---

## 🧪 Test Cases

### Test 1: PDF Upload (Vật lí)
```
Input: SGK Vật lí 12 — Chương Nhiệt học
Expected:
  1. Extract: [công thức, ví dụ, định nghĩa]
  2. Analyze: "formula_heavy", "high complexity"
  3. Recommend: Công Thức Động (100%), Viết Tay (70%)
  4. User chọn "Công Thức Động"
  5. Create & Display: Script + 5 prompts
```

### Test 2: JPG Upload (Toán)
```
Input: Ảnh công thức từ tài liệu tham khảo
Expected:
  1. OCR: Extract text + formulas
  2. Analyze: "step_by_step", "medium"
  3. Recommend: Viết Tay (100%), Công Thức Động (80%)
  4. Create & Display
```

### Test 3: Extracted Content Match
```
Input: File có nội dung cụ thể
Expected:
  - Script phải chứa 100% các formulas từ file
  - Ví dụ phải giống y hệt file (không tự sáng tạo)
  - Định nghĩa phải match từ ngữ gốc
```

---

## ⚠️ Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| OCR fail (ảnh mờ) | Ask user re-upload clearer image / use PDF instead |
| Extract sai (encoding) | Detect encoding, fallback to UTF-8 |
| Recommendation wrong | Add user feedback loop → improve ranking |
| Prompt mismatch | Quality check verifies extracted content match |
| Performance slow | Cache analyzed content, parallelize |

---

## 📈 Success Metrics

✅ **Speed:** < 20 phút từ upload đến display (vs. 30+ phút cũ)  
✅ **Accuracy:** 100% extracted content match (vs. 70–80% tóm tắt)  
✅ **User satisfaction:** Phong cách gợi ý đúng 85%+ lần đầu  
✅ **Efficiency:** 0 lần hỏi "có muốn xem không?" (vs. 2–3 lần cũ)  

---

## 🎓 Key Improvements

| Aspect | Before | After |
|--------|--------|-------|
| Input | Text → prompts | File → analyze → recommend → prompts |
| Accuracy | ~70% (summary) | 100% (extracted) |
| Auto-display | ❌ (hỏi trước) | ✅ (ngay lập tức) |
| Phong cách | Random | Smart recommendation |
| Workflow | Linear | Parallel (extract + analyze) |
| UX | 2–3 bước hỏi | 1 bước xác nhận |

---

## 🚀 Implementation Timeline

```
Week 1 (Jun 26-30):
  - Setup + Phase 1 ✓
  - Implement OCR + text extraction ✓

Week 2 (Jul 3-7):
  - Agent phân tích content ✓
  - Preset recommendation ✓

Week 3 (Jul 10-14):
  - Upgrade video agent ✓
  - Integration + testing ✓

Week 4 (Jul 17-21):
  - QA + edge cases ✓
  - Performance optimization ✓
  - Go live ✓

Total: ~4 weeks, 40–50 dev hours
```

---

## 📞 Next Steps

1. **Review** nâng cấp này với team
2. **Allocate** dev resources (1–2 engineers)
3. **Setup** development environment
4. **Start** Phase 1 implementation
5. **Test** continuously (parallel QA)

---

**Kiến trúc mới sẵn sàng! Bạn muốn tôi chi tiết hóa phần nào?** 🎯
