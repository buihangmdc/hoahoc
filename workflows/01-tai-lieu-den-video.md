# WF-01 — Tài liệu đến video bài giảng

## Đầu vào

Đặt PDF/DOCX/PPTX/TXT/ảnh vào `tai-lieu-dau-vao/<mon>/lop-<n>/`, sau đó chạy `/tai-lieu-thanh-video`.

## Pipeline

```text
Tài liệu gốc
→ manifest + hash
→ source map
→ knowledge brief
→ kiểm định chương trình/khoa học  [chạy WF-04 → 3-gate: KNOWLEDGE-BASE-CHUAN + kiem-dinh-su-pham + quan-ly-san-xuat]
→ learning design
→ kịch bản + storyboard
→ continuity bible
→ keyframe + thumbnail prompts
→ video prompts từng shot
→ voice-over + subtitle + editing notes
→ quality report
→ production package
```

## Cổng dừng

- Dừng nếu không xác định được môn/lớp/phạm vi tài liệu.
- Dừng nếu nội dung nguồn mâu thuẫn khoa học mà chưa giải quyết.
- Không dừng ở outline khi người dùng yêu cầu gói hoàn chỉnh.

