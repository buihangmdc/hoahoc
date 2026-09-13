# 🔧 FIX GUIDE — 3 Critical Issues

**Priority:** 🔴 CÓ NGAY  
**Time:** 2–3 giờ  
**Impact:** HIGH (Core functionality)

---

## FIX #1: Agent Data Flow (extracted_content Pipeline)

### Problem
```
agent-tai-lieu-phong-cach outputs:
  {
    "content": "...",
    "recommendations": [...]
  }

agent-video-ngan-fast inputs:
  {
    "mon": "...",
    "lop": 12,
    "chu_de": "...",
    "phong_cach": "..."  
    ❌ MISSING: extracted_content!
  }

→ Extracted content LOST between agents!
```

### Solution

#### 1A: Update agent-video-ngan-fast Input Schema

**File:** `agents/agent-video-ngan-fast.md` — UPDATE SECTION "Input"

```markdown
## Input

```json
{
  "mon": "Vật lý",
  "lop": 12,
  "chu_de": "Nhiệt học",
  "phong_cach": "Công Thức Động",
  "thoi_luong": "60 giây",
  "dau_ra": ["Script video", "Prompt ảnh"],
  
  "extracted_content": {  // ← NEW
    "original_text": "...",
    "formulas": ["ΔU = Q + A_outside", ...],
    "definitions": [...],
    "examples": [...]
  },
  
  "source_file": "/path/to/file.pdf"  // ← NEW (optional)
}
```
```

#### 1B: Update generate_script() Function

**File:** `agents/agent-video-ngan-fast.md` — UPDATE SECTION "Step 3: Generate Script"

```python
def generate_script(
  mon, lop, chu_de, phong_cach,
  extracted_content=None,  # ← NEW PARAM
  knowledge_base=None
):
  """
  Generate script từ extracted content (nếu có) hoặc knowledge base
  """
  
  # Load preset
  preset = load_preset(phong_cach)
  
  # Chọn source data
  if extracted_content:
    # Use extracted (100% match source file)
    primary_formulas = extracted_content["formulas"]
    primary_examples = extracted_content["examples"]
    primary_definitions = extracted_content["definitions"]
    source = "extracted"
  else:
    # Fallback to knowledge base
    knowledge = load_knowledge_base(mon, lop, chu_de)
    primary_formulas = knowledge.get("formulas", [])
    primary_examples = knowledge.get("examples", [])
    primary_definitions = knowledge.get("definitions", [])
    source = "knowledge_base"
  
  # Generate script (sử dụng primary data)
  script = f"""
  SCRIPT VIDEO — {chu_de} (60s)
  [Source: {source}]
  
  SCENE 1 (HOOK):
  Hook story từ {source}...
  
  SCENE 2 (MAIN):
  Công thức chính: {primary_formulas[0] if primary_formulas else "..."}
  
  SCENE 3 (EXAMPLE):
  Ví dụ từ {source}: {primary_examples[0] if primary_examples else "..."}
  
  ...
  """
  
  # Validation: Ensure all extracted formulas are in script
  if extracted_content:
    for formula in primary_formulas:
      assert formula in script, f"Formula missing: {formula}"
  
  return script
```

#### 1C: Update Quality Check

**File:** `agents/agent-video-ngan-fast.md` — UPDATE SECTION "Quality Checks"

```python
def quality_check(script, extracted_content=None):
  checks = {
    "Science accuracy": check_science_accuracy(script),
    "Timing ≈ 60s": check_timing(script),
    "Copy-paste ready": check_copy_paste(script),
    "No placeholder": check_placeholder(script),
  }
  
  # NEW: If extracted_content provided, verify match
  if extracted_content:
    checks["Extracted match"] = all([
      formula in script 
      for formula in extracted_content["formulas"]
    ])
  
  return {
    "status": "PASS" if all(checks.values()) else "FAIL",
    "details": checks
  }
```

---

## FIX #2: Form File Upload Handler

### Problem
```
Form accepts file upload:
  [Upload button]
       ↓
  File saved locally
       ↓
  ❌ agent-tai-lieu-phong-cach NEVER CALLED!
       ↓
  File never analyzed
       ↓
  User sees no recommendations
       ↓
  User picks random phong cách → WRONG!
```

### Solution

#### 2A: Add File Upload Handler in Form

**File:** `mau/onboarding-widget.html` — UPDATE File Upload Section

```html
<!-- THÊM AFTER file-list section -->
<div id="analysis-result" style="display:none; margin-top:16px; padding:12px; background:#E6F1FB; border-radius:8px;">
  <p style="font-weight:500; color:#185FA5; margin:0 0 8px 0;">📊 Phân tích nội dung</p>
  <div id="analysis-content"></div>
</div>

<!-- THÊM SCRIPT HANDLER -->
<script>
document.getElementById('file-input').addEventListener('change', async function(e) {
  const files = [...this.files];
  
  if (files.length > 0) {
    // 1. Display file list (existing code)
    // ... (keep existing code)
    
    // 2. NEW: Call analysis agent for FIRST file only
    const firstFile = files[0];
    await analyzeFileWithAgent(firstFile);
  }
});

async function analyzeFileWithAgent(file) {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('mon', selMon);
  formData.append('lop', selLop);
  
  try {
    // Call backend endpoint that triggers agent-tai-lieu-phong-cach
    const response = await fetch('/api/analyze-file', {
      method: 'POST',
      body: formData
    });
    
    const result = await response.json();
    
    if (result.status === 'success') {
      // Display recommendations
      displayRecommendations(result.recommendations);
      
      // Store extracted content for next step
      window.EXTRACTED_CONTENT = result.extracted_content;
    } else {
      console.error('Analysis failed:', result.error);
    }
  } catch (error) {
    console.error('Error calling analysis:', error);
  }
}

function displayRecommendations(recommendations) {
  const resultDiv = document.getElementById('analysis-result');
  let html = '<p style="margin:0 0 6px 0; font-size:12px; color:#0C447C;"><strong>Gợi ý phong cách:</strong></p>';
  
  recommendations.forEach((rec, idx) => {
    html += `
      <div style="margin:4px 0; padding:6px 8px; background:white; border-radius:4px; border-left:3px solid #378ADD;">
        <span style="font-weight:500; color:#185FA5;">${idx+1}. ${rec.preset}</span>
        <span style="color:#666; font-size:11px;"> (${rec.confidence}%)</span>
        <p style="margin:2px 0 0 0; font-size:11px; color:#666;">${rec.reason}</p>
      </div>
    `;
  });
  
  resultDiv.innerHTML = html;
  resultDiv.style.display = 'block';
}
</script>
```

#### 2B: Create Backend Endpoint

**File:** `api/analyze-file.py` — NEW FILE

```python
from flask import request, jsonify
from agents.agent_tai_lieu_phong_cach import AgentPhânTíchTàiLiệu

@app.route('/api/analyze-file', methods=['POST'])
def analyze_file_endpoint():
  """
  Endpoint để handle file upload từ form
  """
  try:
    file = request.files['file']
    mon = request.form.get('mon')
    lop = request.form.get('lop')
    
    # 1. Save file temporarily
    temp_path = save_uploaded_file(file)
    
    # 2. Call agent
    agent = AgentPhânTíchTàiLiệu()
    result = agent.run({
      "file_path": temp_path,
      "mon": mon,
      "lop": int(lop)
    })
    
    if result['status'] == 'error':
      return jsonify({
        "status": "error",
        "error": result['error']
      }), 400
    
    # 3. Return recommendations + extracted content
    return jsonify({
      "status": "success",
      "recommendations": result['recommendations'],
      "extracted_content": result['extracted_content'],
      "analysis": result['analysis']
    })
  
  except Exception as e:
    return jsonify({
      "status": "error",
      "error": str(e)
    }), 500
```

---

## FIX #3: Standardize Công Thức Ký Hiệu

### Problem
```
INCONSISTENCY across prompts:

IMAGE PROMPT 2-A:
  "ΔU = Q + A_outside"  ✓

VIDEO PROMPT 2-A:
  "ΔU = Q + A"  ❌ (missing "_outside")

IMAGE PROMPT 3-A:
  "ΔU = Q − A"  ❌ (should be "A_outside")

→ Confusion! Which one is correct?
```

### Solution

#### 3A: STANDARDIZE to "A_outside"

**Rule:** ALL formulas use `A_outside` (NEVER just "A")
- Why? SGK KNTT defines it explicitly
- Why? Clarity + no ambiguity

#### 3B: Audit & Fix All Files

**Check these files:**

1. **IMAGE-PROMPTS-MOTION-TYPE.md**
   - [ ] IMAGE 1: ✓ (no formula yet, OK)
   - [ ] IMAGE 2: Change "ΔU = Q + A" → "ΔU = Q + A_outside"
   - [ ] IMAGE 3: ✓ (no formula, OK)
   - [ ] IMAGE 4: Change "ΔU = Q − A" → "ΔU = Q − A_outside"
   - [ ] IMAGE 5: Change "ΔU = Q + A" → "ΔU = Q + A_outside"

2. **VIDEO-PROMPTS-MOTION-TYPE.md**
   - [ ] VIDEO 1: ✓ (only title, OK)
   - [ ] VIDEO 2: Change formula to "ΔU = Q + A_outside"
   - [ ] VIDEO 3: Change formula to "ΔU = Q + A_outside"
   - [ ] VIDEO 4: Change formula to "ΔU = Q − A_outside" ← IMPORTANT!
   - [ ] VIDEO 5: Change to "ΔU = Q + A_outside"

3. **SCRIPT-VIDEO-NHIET-HOC-60S.md**
   - [ ] All formulas: Use "A_outside"

4. **VOICE-SCRIPT-TTS.md**
   - [ ] When reading ΔU = Q + A: Say "Delta U bằng Q cộng A ngoài"
   - [ ] Check: is "ngoài" clear enough or need "công ngoài"?

#### 3C: Add to Validation

**Add to quality_check():**
```python
def check_formula_consistency(script, image_prompts, video_prompts):
  """
  Verify ALL formulas use A_outside (not just A)
  """
  ALLOWED_FORMULAS = {
    "ΔU = Q + A_outside",
    "ΔU = Q - A_outside",
    "ΔU = Q − A_outside",  # with em-dash
    "Q > 0, A > 0 ⟹ ΔU = Q − A_outside"
  }
  
  all_text = script + str(image_prompts) + str(video_prompts)
  
  # Check for BAD patterns
  bad_patterns = [
    "ΔU = Q + A ",      # A without _outside
    "ΔU = Q - A ",
    "ΔU = Q − A ",
    " = A[^_]",         # A not followed by _
  ]
  
  for pattern in bad_patterns:
    if re.search(pattern, all_text):
      raise ValueError(f"Found inconsistent formula: {pattern}")
  
  return True
```

---

## 📋 IMPLEMENTATION CHECKLIST

### Fix #1: Data Flow
- [ ] Update `agents/agent-video-ngan-fast.md` input schema
- [ ] Update `generate_script()` function
- [ ] Update quality_check with extracted_content validation
- [ ] Test: extracted_content flows from agent 1 → agent 2

### Fix #2: File Upload Handler  
- [ ] Add HTML file analysis section to onboarding-widget.html
- [ ] Create `/api/analyze-file` endpoint
- [ ] Test: upload file → agent called → recommendations shown
- [ ] Test: extracted_content saved and passed forward

### Fix #3: Formula Consistency
- [ ] Audit all IMAGE PROMPTS (5 files)
- [ ] Audit all VIDEO PROMPTS (5 files)
- [ ] Audit SCRIPT + VOICE SCRIPT
- [ ] Add formula consistency check to validation
- [ ] Test: all formulas use A_outside consistently

---

## 🧪 TEST CASES (After Fixes)

### Test 1: End-to-End with File Upload
```
1. User uploads: SGK Vật lý 12 Chương Nhiệt học
2. System calls agent-tai-lieu-phong-cach
3. Shows recommendations: "Công Thức Động (100%)"
4. User clicks "Công Thức Động"
5. agent-video-ngan-fast called with:
   - mon="Vật lý", lop=12, chu_de="Nhiệt học"
   - extracted_content={formulas: [...], ...}
6. Script generated using extracted_content
7. All formulas match exactly
8. Displayed: Script + 5 Image + 5 Video Prompts
✅ PASS: extracted_content flowed correctly
```

### Test 2: Formula Consistency
```
1. Generate script for Nhiệt học with PRESET-07
2. Check all formulas in:
   - IMAGE PROMPTS: All use "A_outside"?
   - VIDEO PROMPTS: All use "A_outside"?
   - SCRIPT: All use "A_outside"?
3. OCR and verify each formula
✅ PASS: No inconsistency found
```

### Test 3: Without File Upload (Fallback)
```
1. User skip file upload, select "Công Thức Động"
2. System uses knowledge_base instead of extracted_content
3. Script still generated correctly
4. Quality check passes
✅ PASS: Fallback works
```

---

## 🚀 START HERE

**Order of implementation:**
1. **FIX #1** (1 hour): Update data flow in agents
2. **FIX #2** (1 hour): Add file upload handler
3. **FIX #3** (0.5 hour): Fix formula consistency
4. **Test** (0.5 hour): Verify all 3 fixes work
5. **Deploy** → Ready for Phase 2 (Major Fixes)

**Total time:** 3 hours 🎯

---

**Sẵn sàng code!** Code rồi sẽ "xịn" 100%
