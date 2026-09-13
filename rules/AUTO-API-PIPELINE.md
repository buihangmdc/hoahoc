# HỢP ĐỒNG PIPELINE MEDIA TỰ ĐỘNG

**Phiên bản:** 2.0  
**Trạng thái:** Kiến trúc và cổng an toàn; không mặc định có adapter nhà cung cấp.

## 1. Điều kiện được chạy

Chỉ chạy render khi:

1. GATE 1, 2, 3 đã PASS.
2. `CLIP-MANIFEST.json` qua `scripts/validate_package.py --mode strict`.
3. Có `config/tool-capabilities.json` hợp lệ và ít nhất một tool `enabled` cho từng công đoạn.
4. Capability chưa hết hạn xác minh; URL nguồn là tài liệu chính thức.
5. Khóa API được cấp qua biến môi trường hoặc secret store, không nằm trong repo/log.
6. Người vận hành đã xác nhận chi phí tối đa và quyền sử dụng dữ liệu/media.

Nếu thiếu một điều kiện, pipeline dừng ở `PLAN_ONLY`; không tuyên bố đã tạo media.

## 2. Chuỗi xử lý

```text
production package
→ package validation
→ capability validation
→ cost/duration plan
→ image/keyframe adapter (nếu cần)
→ video adapter
→ TTS adapter
→ post-production adapter
→ kiểm tồn tại, duration, codec và checksum
→ human review
→ release manifest
```

Mỗi adapter nhận input chuẩn hóa và trả `job_id`, trạng thái, thời điểm, provider/model thực tế, tham số, chi phí báo cáo, đường dẫn tệp và checksum. Không ghi token, request header hoặc dữ liệu cá nhân vào log.

## 3. Cấu hình năng lực

Dùng [mẫu capability](../config/tool-capabilities.example.json). Không ghi tên phiên bản, giới hạn clip, giá hoặc nhận xét “tốt nhất” trong skill/rule; các dữ liệu biến động chỉ sống trong cấu hình có:

- `verified_at`, `expires_at`;
- `official_source_url`;
- mode hỗ trợ, duration, aspect ratio, audio/camera/reference image;
- currency, billing unit và giá nếu đã xác minh;
- `enabled=false` cho mục chưa xác minh.

Chạy:

```text
python scripts/validate_tool_capabilities.py config/tool-capabilities.json
```

## 4. An toàn và tính trung thực

- Không gửi ảnh/giọng học sinh khi chưa có quyền phù hợp.
- Không clone giọng hoặc khuôn mặt nếu thiếu đồng ý và phạm vi sử dụng.
- Không nhờ model sinh chữ/công thức khoa học rồi coi là bản duyệt; thêm bằng hậu kỳ từ lớp nội dung đã khóa.
- Retry phải có giới hạn; job lỗi không tự tăng chi phí vô hạn.
- Media chỉ mang trạng thái `READY` khi tệp tồn tại và validator kiểm được đường dẫn.

## 5. Trạng thái triển khai hiện tại

Repository cung cấp validator và hợp đồng adapter. Adapter gọi API cụ thể chưa được coi là production cho tới khi có mã thực thi, test tích hợp bằng tài khoản sandbox và capability được xác minh từ tài liệu chính thức. Mọi đoạn mã minh họa cũ không phải bằng chứng triển khai.
