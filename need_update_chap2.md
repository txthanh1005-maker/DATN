# REVISION ROADMAP: CHAPTER 2 (PROBLEM FORMULATION)

Dựa trên kết quả thanh tra chéo (Peer Review) từ toàn bộ Hội đồng 5 Sub-agent (EIC, Methodology, Domain, Perspective, Devil's Advocate), dưới đây là danh sách các hạng mục cần cập nhật trong bản thảo `chapter2.tex`.

## 1. ĐIỂM SÁNG ĐƯỢC HỘI ĐỒNG KHEN NGỢI (STRENGTHS)
- **Kiến trúc hàm mục tiêu thống nhất:** Việc dùng biến nhị phân $\Gamma_E(t)$ để chuyển đổi linh hoạt giữa vận hành bình thường (Tối ưu kinh tế) và Khẩn cấp (Bảo vệ tải trọng yếu thông qua VOLL) được EIC đánh giá là một giải pháp cực kỳ thực tiễn cho EMS.
- **Bảo toàn tính chính xác của SOCP:** Cơ chế dùng "cắt giảm công suất ảo" (virtual curtailment) thay vì "tổn thất ảo" (virtual loss) để ngăn Solver lợi dụng Relaxation Gap trong trường hợp phát thừa (over-generation) là một đóng góp toán học rất sắc bén.

## 2. LỖ HỔNG CHÍ MẠNG VỀ VẬT LÝ LƯỚI & TOÁN HỌC (CRITICAL/MAJOR)
- **Sự nhầm lẫn Toán học (SOCP vs. MISOCP):**
  - **Lỗi:** Tác giả liên tục gọi bài toán là SOCP, nhưng lại sử dụng các biến nhị phân (Binary variables) cho trạng thái BESS và DG. Thực chất đây là bài toán MISOCP (Mixed-Integer SOCP), một dạng NP-hard tốn rất nhiều thời gian giải.
  - **Hướng sửa:** Đổi tên bài toán thành MISOCP. Xóa bỏ các biến nhị phân sạc/xả của BESS ($u_{ch}, u_{dis}$) vì hàm mục tiêu đã có chi phí suy giảm ($F_{BESS}$), Solver sẽ tự động không bao giờ cho phép sạc/xả cùng lúc. Điều này giúp giảm tải tính toán khổng lồ.
- **Lỗi thiếu sót Phương trình Vật lý Tie-line:**
  - **Lỗi:** Phương trình DistFlow (11a) có $P_{tie}$ nhưng phương trình (11b) lại thiếu mất công suất phản kháng $Q_{tie}$ và ràng buộc điện áp biên giữa các MG. Điều này vi phạm nghiêm trọng định luật Kirchhoff đối với lưới điện xoay chiều (AC).
  - **Hướng sửa:** Bổ sung $Q_{tie}$ vào phương trình cân bằng công suất phản kháng và thêm ràng buộc giới hạn công suất cho đường dây liên kết.
- **Ảo tưởng về Quán tính vô hạn (Infinite Inertia Fallacy):**
  - **Lỗi:** Bài toán khẳng định bảo vệ hệ thống trước sự cố mất điện lưới (Islanding) nhưng chỉ giải bằng hàm mục tiêu tĩnh (Steady-state AC-OPF) với bước thời gian 1 giờ, bỏ qua hoàn toàn các ràng buộc về Quán tính, Đáp ứng Tần số Sơ cấp và RoCoF.
  - **Hướng sửa:** Làm rõ giới hạn của nghiên cứu (rằng mô hình chỉ giải quyết lớp lập lịch kinh tế Secondary/Tertiary sau khi hệ thống đã ổn định xong trong vài giây đầu).
- **Trống vắng Slack Bus trong chế độ Islanding:**
  - **Lỗi:** Khi $\Gamma_E(t) = 1$ và mất lưới, phương trình DistFlow sẽ vô nghiệm vì thiếu nút Slack Bus để thiết lập điện áp tham chiếu.
  - **Hướng sửa:** Bổ sung phương trình chỉ định DG lớn nhất (Grid-forming Inverter) làm Slack Bus.
- **Sự sụp đổ của SOCP Relaxation:** (Theo Devil's Advocate)
  - **Lỗi:** Nếu xuất hiện dòng công suất ngược (Reverse Power Flow) làm điện áp chạm ngưỡng trên ($V^{\max}$), SOCP sẽ bị Relaxation Gap (mất tính chính xác).

## 3. LỖ HỔNG VỀ PHƯƠNG PHÁP LUẬN & THỰC TIỄN (MAJOR/MINOR)
- **Lãng phí Năng lực Smart Inverter:**
  - **Lỗi:** Việc gán cứng $Q_{PV}=0, Q_{WT}=0$ vi phạm tiêu chuẩn IEEE 1547-2018 hiện hành.
  - **Hướng sửa:** Cho phép PV/WT tham gia bơm công suất phản kháng $S_{max}^2 \ge P^2 + Q^2$ thay vì đẩy toàn bộ gánh nặng điều áp cho DG.
- **Tính Deterministic quá ngây thơ:**
  - Lỗi giả định công suất điện mặt trời/gió là con số dự báo tĩnh (Deterministic forecast) mà bỏ qua tính bất định (Uncertainty). 
- **Chi phí suy giảm BESS phi thực tế:**
  - Cần nâng cấp mô hình hóa tuyến tính vòng đời pin lên hàm phạt chu kỳ (Cyclic aging).
- **Giao dịch P2P thiếu phí truyền tải (DSO Wheeling Charges):**
  - Cần thêm hàm chi phí cho $P_{tie,j,t}$ để bù đắp cơ sở hạ tầng của DSO.

---
**✅ MỆNH LỆNH THỰC THI:** 
1. Đổi tên toàn bộ bài toán thành MISOCP. 
2. Xóa bỏ các biến nhị phân sạc/xả BESS để tăng tốc độ tính toán.
3. Bổ sung ngay $Q_{tie}$ vào phương trình (11b).
4. Gỡ bỏ giả định $Q_{PV}=0$. 
5. Cập nhật Disclaimer về giới hạn ổn định tần số động (Transient Stability).
