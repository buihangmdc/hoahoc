# README — FRAMEWORK KIỂM ĐỊNH CHUẨN (v1.0)

**Ngày phát hành:** 2026-06-23  
**Trạng thái:** Bắt buộc áp dụng cho tất cả bài dạy lớp 12

---

## 🎯 Tổng quan

Hệ thống AI Agent giáo viên đã được **nâng cấp với framework kiểm định 3 cấp** để đảm bảo:

✅ **Độ chính xác khoa học** (công thức, đơn vị, điều kiện áp dụng)  
✅ **Chất lượng sư phạm** (mục tiêu rõ, hoạt động có sản phẩm)  
✅ **Tiêu chuẩn sản xuất** (thời lượng, file, continuity)  

**Bắt buộc:** Mỗi sản phẩm (bài dạy, script, prompt, video) phải **PASS tất cả 3 GATE** trước khi bàn giao.

---

## 📦 Nội dung nâng cấp

### 1. Knowledge Base Chuẩn
**File:** `kho-tai-lieu/vat-ly/KNOWLEDGE-BASE-CHUAN.md`

Tài liệu tham chiếu **duy nhất** cho fact-checking:
- ✓ Công thức chuẩn (SGK KNTT, CTGDPT 2018)
- ✓ Đơn vị SI, hằng số, phạm vi áp dụng
- ✓ Quy ước dấu, hướng vectơ, điều kiện
- ✓ Ví dụ standard cho từng topic

**Quy tắc:** Nếu dùng công thức gì → tra `KNOWLEDGE-BASE-CHUAN` → đối chiếu với output → ghi rõ nếu sai.

### 2. Validation Framework
**File:** `rules/VALIDATION-FRAMEWORK.md`

Framework 3-gate với:
- **GATE 1:** Nội dung khoa học (BLOCKER/MAJOR/MINOR)
- **GATE 2:** Sư phạm (mục tiêu, hoạt động, đánh giá)
- **GATE 3:** Quy trình (thời lượng, file, continuity)

Mỗi gate có **checklist cụ thể** → khi check → gán severity.

### 3. Agent Kiểm định Vật lý Chuyên gia
**File:** `agents/kiem-dinh-vat-ly-chuan.md`

Làm **GATE 1** — Kiểm tra khoa học:
- Đọc `KNOWLEDGE-BASE-CHUAN.md`
- Extract claims từ input
- So sánh từng claim
- Gán BLOCKER/MAJOR/MINOR
- Viết report cụ thể (dòng, section, fix)

### 4. Command Kiểm định Chuẩn
**File:** `commands/kiem-dinh-chuan.md`

Lệnh mới: `/kiem-dinh-chuan [file]`

Chạy 3-gate tuần tự:
```
Đầu vào
 ↓ GATE 1 ← kiem-dinh-vat-ly-chuan
 ↓ GATE 2 ← kien-truc-su-giao-an
 ↓ GATE 3 ← quan-ly-san-xuat
 ↓
Output: 4 report (GATE1, GATE2, GATE3, SUMMARY)
```

---

## 🚀 Cách dùng

### Bước 1: Tạo sản phẩm
Dùng các lệnh bình thường:
```
/tao-bai-day-vat-ly "Định luật I Nhiệt động lực học"
```

### Bước 2: Kiểm định
Sau khi xong, chạy:
```
/kiem-dinh-chuan dau-ra/bai-day/vat-ly/lop-12/dinh-luat-1-nhiet/2026-06-23/
```

### Bước 3: Đọc Report
Kiểm tra 3 report:
- `REPORT-GATE1.md` — Công thức, đơn vị, dấu, vectơ có sai?
- `REPORT-GATE2.md` — Mục tiêu, hoạt động, đánh giá có đủ?
- `REPORT-GATE3.md` — Thời lượng, file, continuity có chuẩn?
- `SUMMARY-VALIDATION.md` — PASS hay FAIL?

### Bước 4: Sửa (nếu BLOCKER)
Nếu có 🔴 BLOCKER:
1. Đọc report → xác định vấn đề
2. Sửa file gốc
3. Chạy lại `/kiem-dinh-chuan`

**Chỉ khi PASS mới bàn giao.**

---

## ⚠️ Quy tắc Bắt buộc

### BLOCKER (🔴 Không được phép)
Sản phẩm **cấm bàn giao** nếu có:

**Khoa học (GATE 1):**
- Công thức sai (ví dụ: ΔU = Q mà quên − A)
- Đơn vị sai (K vs °C lẫn)
- Quy ước dấu không rõ
- Chiều lực/dòng/từ sai
- Xài công thức ngoài điều kiện áp dụng mà không warning

**Sư phạm (GATE 2):**
- Mục tiêu không rõ (không observable, không measure)
- Không có hoạt động học sinh hay chỉ là "nghe giáo viên"
- Không có đánh giá

**Quy trình (GATE 3):**
- Tệp thiếu (script vs storyboard không khớp)
- Prompt không độc lập ("như cảnh trước")

### MAJOR (🟠 Phải sửa)
Sản phẩm có thể **chuyển GATE tiếp theo**, nhưng phải **sửa trước bàn giao**:
- Công thức đúng nhưng không nêu quy ước dấu
- Hoạt động có sản phẩm nhưng không phân hóa
- Thời lượng sai >5%

### MINOR (🟡 Có thể chấp nhận)
Gợi ý cải thiện cho lần sau:
- Ví dụ cũ (2000), có thể cập nhật
- Ngôn ngữ lỏng lẻo (không sai, chỉ cần làm rõ)

---

## 📋 Ví dụ Real-world

### Scenario 1: Bài về Định luật I

**Input:** Script 60s

```
"Nội năng thay đổi bằng nhiệt lượng trừ công."
```

**GATE 1 Check:**
- Phát biểu? ✓ Đúng (so KNOWLEDGE-BASE)
- Quy ước dấu? ❌ Không nêu → 🟠 MAJOR

**GATE 1 Report:**
```
🟠 MAJOR [Line 5, Script]:
  Issue: Quy ước dấu Q, A, ΔU không rõ
  Fix: Thêm: "Theo quy ước: Q > 0 khi hệ nhận nóng, 
               A > 0 khi hệ làm công lên ngoài"
```

**Action:** Sửa script → chạy lại `/kiem-dinh-chuan` → PASS GATE 1 → tiếp tục GATE 2.

---

### Scenario 2: Bài về Khí lí tưởng

**Input:** Script dùng công thức pV = nRT

```
"Với p = 101325 Pa, V = 22.4 L, tính T khi n = 1 mol."
```

**GATE 1 Check:**
- Công thức pV = nRT? ✓ Đúng
- Đơn vị nhất quán? ❌ V = 22.4 L (litre) nhưng công thức dùng m³ → 🔴 BLOCKER

**GATE 1 Report:**
```
🔴 BLOCKER [Line 7, Script]:
  Issue: Đơn vị không nhất quán. V = 22.4 L nhưng công thức pV = nRT dùng m³
  Fix: Thay V = 22.4 L = 0.0224 m³, hoặc dùng: nRT/p = 0.0224 m³ = 22.4 L
```

**Action:** Phải sửa trước khi tiếp tục (không skip BLOCKER).

---

## 🔗 Liên kết Tài liệu

| Tài liệu | Vị trí | Mục đích |
|----------|--------|---------|
| KNOWLEDGE-BASE-CHUAN | `kho-tai-lieu/vat-ly/KNOWLEDGE-BASE-CHUAN.md` | Tra cứu công thức, quy ước |
| VALIDATION-FRAMEWORK | `rules/VALIDATION-FRAMEWORK.md` | Quy trình 3-gate chi tiết |
| Agent Kiểm định VL | `agents/kiem-dinh-vat-ly-chuan.md` | Cách kiểm GATE 1 |
| Command | `commands/kiem-dinh-chuan.md` | Cách chạy lệnh |
| CLAUDE.md | `CLAUDE.md` | Tích hợp vào workflow chính |

---

## 📊 Timeline Áp dụng

| Giai đoạn | Mốc thời gian | Hành động |
|-----------|---------|----------|
| **Phát hành** | 2026-06-23 | Bắt đầu dùng `/kiem-dinh-chuan` cho bài mới |
| **Mandatory** | 2026-07-01 | Tất cả bài dạy lớp 12 phải pass 3-gate |
| **Extend** | 2026-08-01 | Áp dụng cho lớp 10–11 nếu thành công |

---

## ❓ FAQ

**Q1: Nếu tôi là giáo viên không có thời gian sửa BLOCKER?**  
A: Framework bắt buộc. Nếu tìm BLOCKER, cần sửa hoặc skip sản phẩm. Không được bàn giao mà có BLOCKER.

**Q2: Định luật I, tôi từng dạy với quy ước ΔU = Q + A, có được không?**  
A: SGK KNTT 2018 dùng ΔU = Q − A (công của hệ). Phải tuân theo SGK chính thức. Nếu khác, phải ghi chú rõ.

**Q3: Sử dụng `/kiem-dinh-chuan` có tính tiền/credits không?**  
A: Không. Là bước bắt buộc trong quy trình.

**Q4: MINOR có bắt buộc sửa không?**  
A: Không. MINOR là gợi ý cải thiện. Nhưng MAJOR phải sửa.

**Q5: Tôi làm video 3D, Knowledge Base vật lý có đủ không?**  
A: Có. Knowledge Base là khoa học, không liên quan kỹ thuật video. Video 3D dùng `studio-bible/PRESET-02-3D.md` riêng.

---

## 📞 Hỗ trợ

Nếu có thắc mắc về framework, đọc:
1. `rules/VALIDATION-FRAMEWORK.md` (quy trình chi tiết)
2. `agents/kiem-dinh-vat-ly-chuan.md` (cách check GATE 1)
3. `kho-tai-lieu/vat-ly/KNOWLEDGE-BASE-CHUAN.md` (công thức chuẩn)

Hoặc tạo issue với tag `[validation]` để giáo viên/chuyên gia kiểm tra.

