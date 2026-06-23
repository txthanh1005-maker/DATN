# REVISION ROADMAP: CHAPTER 4 (TEMPORAL COORDINATION WITH MPC)

Dựa trên kết quả thanh tra chéo (Peer Review) từ 4 Sub-agent (EIC, Domain, Perspective, Devil's Advocate), dưới đây là danh sách các hạng mục cần cập nhật trong bản thảo `chapter4.tex`. 

*(Lưu ý: Báo cáo của Methodology Expert bị chậm trễ, nhưng 4 báo cáo hiện tại đã đủ để chỉ ra các lỗ hổng hệ thống cốt lõi).*

## 1. CÁC LỖ HỔNG CHÍ MẠNG VỀ ỔN ĐỊNH LƯỚI (CRITICAL)
- **Nghịch lý "Simplification Trap" ở trạng thái Islanding:**
  - **Lỗi:** Mô hình sử dụng MPC (với bước thời gian lớn) và chỉ cân bằng Công suất tác dụng ($P$) để khẳng định MG có thể sống sót sau sự cố $N-2$ (Islanding). Điều này hoàn toàn bỏ qua thực tế vật lý: lưới có thể sụp đổ trong vài mili-giây đầu tiên do thiếu hụt quán tính (Inertia) và thay đổi tần số đột ngột (RoCoF).
  - **Hướng sửa:** Cần bổ sung ngay các ràng buộc về **Quán tính lưới tối thiểu (Minimum Grid Inertia)** và **Đáp ứng tần số sơ cấp (Primary Frequency Response)** vào bài toán quy hoạch, hoặc phải thêm Giả định (Assumption) cực kỳ chặt chẽ ở đầu chương rằng lớp điều khiển sơ cấp (Primary Control) đã hoàn toàn lo liệu phần quá độ này ở cấp độ mili-giây.

## 2. CÁC LỖ HỔNG VỀ VẬT LÝ VÀ ĐIỆN LỰC (MAJOR)
- **Bỏ qua khả năng hỗ trợ Công suất phản kháng ($Q$) của Inverter:**
  - **Lỗi:** BESS và các DGs (PV, WT) hiện tại chỉ được điều khiển phát $P$. Điều này vi phạm tiêu chuẩn lưới điện hiện đại (ví dụ: IEEE 1547-2018).
  - **Hướng sửa:** Bổ sung các biến điều khiển $Q_{BESS}, Q_{PV}, Q_{WT}$ và giới hạn công suất biểu kiến (P-Q capability curve) của Inverter vào bài toán để kiểm soát điện áp ($V$).
- **Khả năng hội tụ của thuật toán phân tán trong thời gian thực:**
  - **Lỗi:** Nhúng một vòng lặp ATC (đòi hỏi nhiều lần lặp) vào bên trong mỗi bước thời gian thực của MPC (Mode 2). Nếu mạng chậm hoặc thuật toán không hội tụ kịp, hệ thống sẽ bị treo tín hiệu điều khiển khẩn cấp.
  - **Hướng sửa:** Thêm phân tích giới hạn thời gian tính toán (Computational Tractability bounds) cho vòng lặp ATC, và đưa ra giải pháp "Fallback" (kế hoạch dự phòng) nếu không hội tụ kịp.

## 3. THỰC TIỄN & CHIẾN LƯỢC (MINOR)
- **Sự ngây thơ về hạ tầng Viễn thông:** Giả định rằng mạng truyền thông vẫn hoạt động hoàn hảo không độ trễ (Zero-latency) đúng vào thời điểm cấu trúc lưới đang bị tàn phá nặng nề (N-2). Cần thêm phần bàn luận về sự suy giảm viễn thông (Communication delay).
- **Tính thực tiễn của ngắt tải (Load Shedding):** Chi phí ngắt tải (Penalty) hiện tại được gán cứng tĩnh. Cần gắn nó với khái niệm **VOLL (Value of Lost Load)** động trong thực tế dựa trên các hợp đồng Demand Response (DR).

---
**✅ MỆNH LỆNH THỰC THI:** 
Sửa ngay những thiếu sót về ràng buộc Quán tính lưới và Hỗ trợ công suất phản kháng $Q$ của Inverter. Bổ sung các "Assumptions" chặt chẽ về việc bỏ qua độ trễ mạng viễn thông.
