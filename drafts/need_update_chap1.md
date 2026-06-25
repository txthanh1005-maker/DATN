# REVISION ROADMAP: CHAPTER 1 (INTRODUCTION)

Dựa trên kết quả thanh tra chéo (Peer Review) từ toàn bộ Hội đồng 5 Sub-agent (EIC, Methodology, Domain, Perspective, Devil's Advocate), dưới đây là danh sách các hạng mục cần cập nhật trong phần mở đầu `chapter1.tex`.

## 1. ĐIỂM SÁNG ĐƯỢC HỘI ĐỒNG KHEN NGỢI (STRENGTHS)
- **Kiến trúc Tri-layer xuất sắc:** Việc kết hợp SOCP (bảo toàn vật lý AC), ATC (điều phối phân cấp không gian) và MPC (đáp ứng động thời gian thực) thành một "Tri-layer Cooperative Resilience Architecture" được toàn bộ hội đồng đánh giá là bước tiến cực kỳ đột phá.
- **Biện luận sắc sảo (Master Gap):** Việc chỉ ra nhược điểm của các phương pháp cũ (DC-OPF thiếu Q, ADMM gây dao động, và EMS tập trung dễ sập) tạo ra động lực nghiên cứu (Motivation) cực kỳ thuyết phục.

## 2. LỖ HỔNG CHÍ MẠNG VỀ LẬP LUẬN & LOGIC (CRITICAL/MAJOR)
- **Mâu thuẫn về "Phi tập trung" (Internal Contradiction on Decentralization):**
  - **Lỗi:** Tác giả chê hệ thống tập trung (Centralized EMS) là "điểm nghẽn rủi ro" (single point of failure) khi mất viễn thông. NHƯNG, sau đó lại đề xuất dùng ATC (Analytical Target Cascading). Thuật toán ATC bản chất là kiến trúc Master-Slave (Chủ-Tớ) hướng từ trên xuống. Nếu đứt mạng, nút Master của ATC cũng sẽ sập hệt như EMS tập trung.
  - **Hướng sửa:** Phải đính chính lại rằng ATC không phải là "Decentralized" (Phi tập trung hoàn toàn) mà là **"Distributed/Hierarchical"** (Phân tán theo phân cấp). Cần bổ sung giả định rằng hạ tầng mạng giữa Master-Slave được bảo vệ vững chắc.
- **Ảo tưởng Quán tính (Infinite Inertia Fallacy):**
  - **Lỗi:** Tác giả tuyên bố giải quyết sự cố mất lưới nhưng lại đẩy toàn bộ trách nhiệm giữ ổn định tần số mili-giây cho "Primary Control layer" và coi như nó tự động hoạt động hoàn hảo. Devil's Advocate và Domain Expert chỉ ra rằng trong lưới có nhiều Inverter (Low-inertia), việc gán gọn trách nhiệm này là thiếu trách nhiệm nghiên cứu.
  - **Hướng sửa:** Phải làm rõ ranh giới nghiên cứu (Boundary) ngay từ Chapter 1: Luận văn KHÔNG giải quyết độ ổn định quá độ (Transient/Frequency Stability), mà chỉ tập trung vào Lập lịch Năng lượng Khẩn cấp (Emergency Energy Scheduling) ở cấp độ Secondary/Tertiary. Thêm trích dẫn IEEE PES-TR71.
- **Rủi ro rớt Toán học do VOLL:**
  - Nếu hàm phạt VOLL (Value of Lost Load) thiết kế dưới dạng bậc thang rời rạc (discrete steps), SOCP sẽ mất tính lồi và không thể hội tụ (Convergence Proof bị đe dọa).

## 3. LỖ HỔNG VỀ THỰC TIỄN & CHIẾN LƯỢC (MAJOR/MINOR)
- **Sự ngây thơ về Công suất phản kháng (Q):**
  - **Lỗi:** Cho rằng Inverter tự động dùng công suất thừa để phát Q hỗ trợ lưới ($S_{max}^2 \ge P^2 + Q^2$). Trong thực tế sự cố, Inverter sẽ dồn 100% công suất vào $P$ để cứu tải, dẫn đến $Q=0$ đúng vào lúc lưới cần điều áp nhất. Hơn nữa, việc phát Q miễn phí là phi lý về kinh tế (Incentive Incompatibility).
- **Rào cản Pháp lý của "Graceful Degradation":**
  - Cắt điện ưu tiên dựa trên VOLL nghe rất hay về toán học, nhưng vi phạm sự công bằng xã hội (Equity). DSOs cần các hợp đồng sa thải phụ tải tự nguyện chứ không thể tự ý cắt.

---
**✅ MỆNH LỆNH THỰC THI:** 
1. **Tinh gọn phần mở bài:** Rút ngắn lịch sử Smart Grid, tiến thẳng vào SOCP-ATC-MPC.
2. **Chèn kết quả định lượng (Quantitative hooks):** Đưa trước 1-2 con số kết quả (giảm X% VOLL) vào Introduction.
3. **Sửa từ ngữ:** Thay "Decentralized" bằng "Hierarchical Distributed" khi mô tả ATC.
4. **Bổ sung Scope/Boundary:** Từ chối trách nhiệm về Transient/Frequency Stability rõ ràng ở mục Scope of the Thesis. Thêm điều kiện viễn thông hoàn hảo.
