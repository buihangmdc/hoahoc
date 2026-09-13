# 🔍 QUALITY REVIEW — Nâng Cấp Bộ AI Agent

**Ngày review:** 2026-06-25  
**Reviewer:** Architecture Analysis  
**Status:** 🔴 CÓ CÁI CẦN SỬA — Chi tiết dưới đây

---

## 📊 REVIEW SUMMARY

| Khía cạnh | Đánh giá | Mức độ |
|-----------|---------|-------|
| Architecture | ✅ Logic tốt | 8/10 |
| Integration | ⚠️ Thiếu điểm | 6/10 |
| Data Flow | ❌ Có lỗ hổng | 5/10 |
| Error Handling | ⚠️ Chưa đầy đủ | 6/10 |
| UX/Performance | ✅ Tốt | 8/10 |
| Documentation | ✅ Chi tiết | 9/10 |

**Kết luận:** Cần sửa 3 điểm chính trước khi implement

---

## 🔴 CRITICAL ISSUES (Phải sửa)

### Issue #1: Agent Phân Tích ← → Agent Video Ngắn (DATA FLOW BREAK)

**Vấn đề:**
```
agent-tai-lieu-phong-cach
  ├─ Extract content
  ├─ Recommend phong cách (TOP 3)
  └─ OUTPUT: {content, recommendations}
       ↓
  ❌ AI AGENT VIDEO NGẮN KHÔNG NHẬN INPUT NÀY!
  
agent-video-ngan-fast
  ├─ Cần input: (mon, lop, chu_de, phong_cach, extracted_content)
  └─ Nhưng form chỉ gửi: (mon, lop, chu_de, phong_cach)
  
  → extracted_content BỊ MẤT!
```

**Fix:**
```python
# agent-video-ngan-fast cần update input:

def create_video(params):
  input_schema = {
    "mon": str,
    "lop": int,
    "chu_de": str,
    "phong_cach": str,
    "extracted_content": dict,  # ← NEW (optional)
    "source_file": str,         # ← NEW (optional, file path)
  }
  
  # If extracted_content provided:
  #   Use extracted formulas + examples (100% match)
  # Else:
  #   Use knowledge base
```

**Impact:** HIGH (prompt accuracy phụ thuộc vào cái này)

---

### Issue #2: File Upload ← → Agent Phân Tích (INTEGRATION GAP)

**Vấn đề:**
```
Form onboarding
  ├─ Upload file
  └─ ❌ KHÔNG CÓ LOGIC GỌI agent-tai-lieu-phong-cach!
       ↓
File được lưu, nhưng KHÔNG ĐƯỢC PHÂN TÍCH
       ↓
User không thấy gợi ý phong cách
       ↓
User phải chọn manually (phải chọn sai)
```

**Fix:**
```python
# form-onboarding cần thêm:

@on_file_upload
def handle_file_upload(file):
  # 1. Save file temporarily
  temp_path = save_uploaded_file(file)
  
  # 2. Call agent phân tích
  analysis = agent_tai_lieu_phong_cach.run({
    "file_path": temp_path,
    "mon": form_data["mon"],
    "lop": form_data["lop"]
  })
  
  # 3. Display recommendations
  display_recommendations(analysis["recommendations"])
  
  # 4. Store for later use
  form_data["extracted_content"] = analysis["content"]
  form_data["source_file"] = temp_path
```

**Impact:** HIGH (user experience, accuracy)

---

### Issue #3: Continuity Chain Between Clips (VIDEO PROMPT FLAW)

**Vấn đề:**
```
VIDEO PROMPT đó nói:
  "START STATE: Formula "ΔU = Q + A" already visible..."
  "END STATE: Formula at top (dim)..."

Nhưng IMAGE PROMPT của SCENE 2-A nói:
  "Công thức chính: ΔU = Q + A_outside"
  "Tiêu đề "FIRST LAW" teo nhỏ lên"

❌ KHÔNG KHỚP!
   - Video prompt nói "ΔU = Q + A"
   - Image prompt nói "ΔU = Q + A_outside"
   
   → Khi AI tool sinh video, continuity sẽ lỏng!
```

**Fix:**
```
Standardize across ALL prompts:

✅ ALWAYS dùng: ΔU = Q + A_outside
   (không bao giờ tắt "_outside")

Kiểm tra lại:
  - IMAGE PROMPT 1, 2, 3, 4, 5: ✓ "A_outside"?
  - VIDEO PROMPT 1, 2, 3, 4, 5: ✓ "A_outside"?
  - SCRIPT: ✓ "A_outside"?
  
❌ HIỆN TẠI: Không consistent!
```

**Impact:** MEDIUM (visual quality)

---

## 🟡 MAJOR ISSUES (Nên sửa)

### Issue #4: Agent Metadata (MISSING INFO)

**Vấn đề:**
```
Agent không có:
  - Input validation (required fields?)
  - Output schema (formal spec)
  - Timeout handling
  - Fallback logic
  - Caching (OCR results heavy)
  
Example:
  agent-tai-lieu-phong-cach.run({
    "file_path": "abc.pdf"  # ← Valid path? File exists?
  })
  
  ❌ No validation → crash if missing file
```

**Fix:**
```python
# Add to each agent:

class Agent:
  INPUT_SCHEMA = {
    "file_path": {
      "type": "str",
      "required": True,
      "validate": lambda x: Path(x).exists(),
      "error": "File not found"
    },
    # ... etc
  }
  
  OUTPUT_SCHEMA = {
    "status": "success | error",
    "data": {...},
    "errors": [...]
  }
  
  def validate_input(self, params):
    for field, spec in self.INPUT_SCHEMA.items():
      if spec.get("required") and field not in params:
        raise ValueError(f"Missing required field: {field}")
```

**Impact:** MEDIUM (robustness)

---

### Issue #5: Timing Validation (INCOMPLETE)

**Vấn đề:**
```
Script nói: "60 giây"

Nhưng KHÔNG CÓ:
  ❌ Check timing thực tế = 60s?
  ❌ Nếu không = 60s, phải sửa scene nào?
  ❌ Flexible window là bao nhiêu? (±2s? ±5s?)
  
Example:
  Scene 1: 8s
  Scene 2: 12s
  Scene 3: 25s
  Scene 4: 10s
  Scene 5: 8s
  TOTAL: 63s
  
  ❌ QUA 60s → Cần sửa!
  ❌ Script không nói phải sửa scene nào!
```

**Fix:**
```python
def validate_timing(script_scenes):
  total = sum([s.duration for s in script_scenes])
  
  if abs(total - 60) > 2:  # Flexible ±2s
    # Adjust scenes
    excess = total - 60
    # Reduce longest scenes first
    scenes_sorted = sorted(script_scenes, key=lambda x: x.duration, reverse=True)
    
    for scene in scenes_sorted:
      if excess <= 0:
        break
      reduction = min(excess, scene.duration - 5)  # Min 5s per scene
      scene.duration -= reduction
      excess -= reduction
  
  return script_scenes, total
```

**Impact:** MEDIUM (quality)

---

## 🟠 MINOR ISSUES (Nice to have)

### Issue #6: Cache OCR Results
```
❌ Mỗi lần user upload PDF → OCR lại (slow!)
✅ Cache results → Nhanh hơn

Implement:
  - Redis cache (extracted content)
  - TTL: 24 giờ
  - Key: md5(file_path + file_modified_time)
```

### Issue #7: User Feedback Loop
```
❌ Gợi ý phong cách không có feedback
✅ Add: "Đúng không? [👍 Đúng] [👎 Sai]"
  → Improve recommendation ranking
```

### Issue #8: Parallel Processing
```
❌ Extract → Analyze → Recommend (tuần tự, slow)
✅ Extract + (Parallel) → Analyze + Recommend
  → Faster (25% improvement)
```

---

## ✅ WHAT'S GOOD

### Strength #1: Clear Separation of Concerns
```
✓ agent-tai-lieu-phong-cach: Analysis only
✓ agent-video-ngan-fast: Generation only
✓ Dễ test, dễ maintain, dễ mở rộng
```

### Strength #2: Comprehensive Documentation
```
✓ 3 agents + 1 guide + 1 review
✓ Workflow diagram rõ ràng
✓ Error handling list
✓ Test cases cụ thể
```

### Strength #3: Quality Locks
```
✓ Science accuracy lock (formula, unit)
✓ Continuity anchor (clip to clip)
✓ Color system lock (hex codes)
✓ Timing lock (clip max 9s)
```

---

## 📝 FIXES CHECKLIST

### CRITICAL (DO FIRST)

- [ ] **Fix #1:** Update agent-video-ngan-fast input schema
  - Add: `extracted_content`, `source_file`
  - Update: Script generator sử dụng extracted content

- [ ] **Fix #2:** Add file upload handler in form
  - Call agent-tai-lieu-phong-cach khi file upload
  - Display recommendations
  - Store extracted_content for next step

- [ ] **Fix #3:** Standardize ký hiệu công thức
  - Kiểm tra lại ALL prompts: ΔU = Q + A_outside (100%)
  - Update IMAGE-PROMPTS-*.md
  - Update VIDEO-PROMPTS-*.md

### MAJOR (DO SECOND)

- [ ] **Fix #4:** Add Input/Output schema to agents
  - Validation function
  - Error messages

- [ ] **Fix #5:** Add timing validation
  - Hàm check total duration
  - Auto-adjust scenes nếu cần

### MINOR (DO THIRD)

- [ ] **Fix #6:** Implement caching (Redis)
- [ ] **Fix #7:** Add user feedback (rating)
- [ ] **Fix #8:** Parallelize Extract + Analyze

---

## 📋 REVISED IMPLEMENTATION PLAN

### Phase 1: Critical Fixes (2–3 giờ) ← **START HERE**
```
1. Update input schema (agents)
2. Add file upload handler (form)
3. Fix ký hiệu công thức (prompts)
4. Test: file upload → analyze → recommend
```

### Phase 2: Major Fixes (2 giờ)
```
5. Add input/output validation
6. Add timing validation
7. Test: create script → check timing
```

### Phase 3: Minor + Performance (3 giờ)
```
8. Implement caching
9. Add user feedback
10. Parallelize
11. Performance test
```

### Phase 4: Integration + Testing (2 giờ)
```
12. Wire everything together
13. End-to-end test
14. Edge case handling
```

**Revised Total:** 9–10 giờ (vs. 12–17 giờ trước)

---

## 🎯 SUCCESS CRITERIA (After Fixes)

✅ **Accuracy:**
- Extracted content match 100% source file ✓
- Prompt formulas = extracted formulas ✓
- Recommended phong cách đúng 85%+ ✓

✅ **Performance:**
- File upload → Display: < 15 phút ✓
- No timeout (files ≤ 50MB) ✓
- Cache hit rate: 70%+ ✓

✅ **UX:**
- 0 "có muốn xem không?" prompts ✓
- Clear error messages ✓
- User feedback captured ✓

✅ **Quality:**
- All ký hiệu consistent ✓
- Timing = 60s ± 2s ✓
- Continuity chain tested ✓

---

## 🚀 NEXT STEPS

1. **Review & Approve** fixes trên
2. **Allocate** developer (1 engineer)
3. **Start Phase 1** immediately (critical fixes)
4. **Test** sau mỗi phase
5. **Deploy** khi hết Phase 4

---

## 📞 QUESTIONS FOR CLARIFICATION

1. **Flexible timing window?** ±2s OK or need tighter?
2. **Cache strategy?** Redis / Local file cache?
3. **User feedback importance?** High priority or nice-to-have?
4. **File size limit?** 50MB OK or need bigger?
5. **Timeout limit?** 30 min OK or need faster?

---

**Review hoàn thành. Sẵn sàng code!** 🎯

Bạn muốn tôi:
1. ✅ **Fix ngay** 3 critical issues (2–3 giờ)?
2. 📋 **Revise blueprint** trước khi code?
3. 🧪 **Create test cases** để verify?
