# REVISION ROADMAP: CHAPTER 3 (ATC & MMG COORDINATION)

Dựa trên kết quả thanh tra chéo (Peer Review) từ Hội đồng 5 Sub-agent (EIC, Methodology, Domain, Perspective, Devil's Advocate), dưới đây là danh sách các hạng mục cần cập nhật khẩn cấp trong `chapter3.tex`.

## 1. CÁC LỖ HỔNG CHÍ MẠNG VỀ TOÁN HỌC (CRITICAL)
- **Sai lệch phương trình cập nhật Target (Eq. 36 & 39):**
  - **Lỗi:** Nghiệm phân tích cập nhật $P_{target}$ hiện tại đã làm rơi mất thành phần nhân tử Lagrange ($\lambda$). Việc mất feedback từ biến đối ngẫu phá vỡ lý thuyết hội tụ của ADMM/ATC.
  - **Hướng sửa:** Đạo hàm lại điều kiện KKT cho bài toán Coordinator. Phương trình đúng phải chứa hiệu số của nhân tử Lagrange: 
  $$P_{target,ij,t} = \frac{1}{2}(P_{tie,ij,t}^{*,k} - P_{tie,ji,t}^{*,k}) + \frac{1}{2\rho_{ij,t}^k}(\lambda_{ij,t}^k - \lambda_{ji,t}^k)$$
- **Định nghĩa sai Phần dư Đối ngẫu (Dual Residual - Eq. 67):**
  - **Lỗi:** Đang lấy sai phân của biến cục bộ ($P_{tie}$) thay vì biến đồng thuận ($P_{target}$). Điều này làm hỏng thuật toán Adaptive Residual Balancing.
  - **Hướng sửa:** Cập nhật lại công thức đo lường sự thay đổi của target variable: 
  $$s_{ij,t}^k = \rho_{ij,t}^k | P_{target,ij,t}^k - P_{target,ij,t}^{k-1} |$$
- **Thiếu chứng minh SOCP Exactness:** Cần bổ sung đoạn text khẳng định điều kiện topology (lưới phân phối hình tia - radial) để đảm bảo SOCP relaxation tại các MG nội bộ là hội tụ chính xác.

## 2. CÁC LỖ HỔNG VỀ VẬT LÝ VÀ ĐIỆN LỰC (MAJOR)
- **Nghịch lý đường dây "đồng nguyên chất" (Lossless P-only Ties):**
  - **Lỗi:** Mô hình ép buộc $P_{target,ij} + P_{target,ji} = 0$, giả định lưới không tổn thất ($I^2R = 0$) và bỏ qua công suất phản kháng ($Q$).
  - **Hướng sửa:** 
    - Thêm ràng buộc truyền tải công suất cực đại trên đường dây ($P_{tie}^{max}$) vào bài toán của Coordinator.
    - Cần biện luận rõ: Tại sao chỉ giao dịch $P$ trên mạng P2P? Trả lời: Công suất phản kháng $Q$ được giao cho các MG tự quản lý nội bộ (Local Support) để giữ vững điện áp ($V$), không tham gia đấu giá trên đường dây liên kết.
- **Biến động RES & Quán tính lưới:** Bổ sung giả định rằng ATC vận hành trong khuôn khổ hoàn hảo (deterministic foresight) của từng chu kỳ MPC, nhằm xử lý sự bất định của lưới có tích hợp nhiều RES.

## 3. THỰC TIỄN & CHIẾN LƯỢC (MINOR)
- **Rào cản Viễn thông:** Thêm giả định bài toán yêu cầu hạ tầng mạng truyền thông đồng bộ (Synchronous communication), bỏ qua độ trễ gói tin.
- **Hành vi thao túng của MGs:** Thêm giả định các MG là các "tác nhân tuân thủ tuyệt đối" (Rational & Compliant actors), không có hành vi đấu giá trục lợi (Gaming vulnerabilities).

---
**✅ MỆNH LỆNH THỰC THI:** 
Tập trung sửa trực tiếp các công thức (Eq. 36, 39, 67) và thuật toán (Algorithm 1) để bảo vệ tính toàn vẹn của nền tảng Toán học. Các vấn đề Điện lực & Thực tiễn có thể giải quyết bằng cách thêm "Assumptions" (Giả định) ở đầu chương.
