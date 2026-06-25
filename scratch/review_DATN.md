# Báo cáo Đánh giá (Peer Review Report) - DATN.tex
**Tác giả:** Trịnh Xuân Thành
**Tiêu đề:** A Fault-Adaptive Peer-to-Peer Energy Trading Framework for Enhancing Multi-Microgrid Resilience via ATC and MPC

---

## 1. Editor-in-Chief (EIC)
**Đánh giá tổng quan:**
Đề tài thể hiện tính nguyên bản cao và đóng góp quan trọng trong lĩnh vực vận hành liên lưới Microgrid (MMG). Việc phát hiện ra hai nghịch lý (Tie-line Congestion Paradox và Voltage Paradox) cùng với khái niệm "Negative Premium" làm tăng đáng kể giá trị khoa học. Khung hệ thống 3 chế độ kết hợp ATC và MPC rất ấn tượng.
- **Quyết định đề xuất:** Major Revision (do cần làm rõ một số giả định cốt lõi từ Devil's Advocate).

## 2. Methodology Reviewer (Reviewer 1)
**Trọng tâm:** Tính chặt chẽ của thiết kế nghiên cứu và thuật toán (SOCP AC-OPF, ATC, MPC).
- **CRITICAL:** Khẳng định "ATC hội tụ trong tối đa 91 giây" (Abstract) cần được chứng minh rõ trong điều kiện mô phỏng nào (phần cứng, số lượng MG, chuẩn giao tiếp). MPC rolling horizon có thể bị tắc nghẽn nếu ATC không hội tụ đúng hạn trong thời gian thực.
- **MAJOR:** Việc sử dụng SOCP convex relaxation cho AC-OPF yêu cầu điều kiện KKT nghiêm ngặt (exactness). Lỗi xấp xỉ có thể xảy ra khi lưới quá tải hoặc sụt áp mạnh. Cần đảm bảo relaxation gap luôn xấp xỉ 0.
- **MINOR:** Khuyến nghị bổ sung flowchart hoặc pseudocode cụ thể cho sự tương tác giữa MPC (temporal) và ATC (spatial) trong Abstract hoặc Giới thiệu để người đọc dễ hình dung sớm.

## 3. Domain Reviewer (Reviewer 2)
**Trọng tâm:** Chuyên môn Hệ thống Điện, khả năng phục hồi, và quản lý năng lượng.
- **CRITICAL:** Trong "Voltage Paradox", việc cắt giảm công suất tác dụng (active power curtailment) để cứu điện áp do tổn thất $I^2X$ là một giải pháp vật lý có cơ sở nhưng rất cực đoan. Tại sao không đề cập đến giới hạn P/Q của Inverter (Smart Inverters) ngay từ đầu để bơm thêm Q cục bộ thay vì cắt P? (Tuy đã nhắc ở Future Work, nhưng đây là lỗ hổng lớn về mặt vận hành thực tế).
- **MAJOR:** Chuẩn hóa đơn vị 1MVA base power có thể làm méo mó các thông số của Microgrid vốn thường ở mức vài chục đến vài trăm kVA. Cần đảm bảo ma trận trở kháng (impedance matrix) không bị ill-conditioned khi scale theo 1MVA base.
- **MINOR:** "100% Critical Load survival rate" - Cần định nghĩa rõ trong bài Critical Load chiếm bao nhiêu % tổng tải. Nếu chỉ chiếm 5%, thì 100% survival rate không quá ý nghĩa.

## 4. Perspective Reviewer (Reviewer 3)
**Trọng tâm:** Góc nhìn kinh tế - kỹ thuật và ứng dụng thực tiễn.
- **MAJOR:** Hiện tượng "Negative Premium" (chi phí vận hành sau sự cố thấp hơn trước sự cố do giải phóng năng lượng tái tạo dư thừa) mang tính đột phá về lý thuyết kinh tế năng lượng. Tuy nhiên, liệu điều này có dẫn đến "Moral Hazard" - nơi các MG cố tình tự ngắt khỏi lưới chính (islanding) để trục lợi từ thị trường P2P? Cần phân tích cơ chế khuyến khích (incentive mechanism) để ngăn chặn điều này.
- **MINOR:** Hạn chế về trao đổi Q (không buôn bán Q P2P) là một giả định hợp lý để giảm độ phức tạp cho ATC, nhưng cần nhấn mạnh hơn về tổn thất kinh tế khi các MG không thể hỗ trợ Q cho nhau.

## 5. Devil's Advocate
**Trọng tâm:** Thử thách các lập luận cốt lõi và phát hiện ngụy biện.
- **Strongest Counter-Argument:** Sự thành công của khung kiến trúc này phụ thuộc hoàn toàn vào hệ thống truyền thông (communication) giữa các MG để chạy thuật toán phân tán ATC. Trong điều kiện "Extreme Weather Events" (như bão, lụt), hệ thống truyền thông thường là điểm mù bị hỏng đầu tiên. Việc giả định truyền thông hoàn hảo trong khi lưới điện bị đứt gãy là một nghịch lý logic (Logical Fallacy - Cherry-picking assumptions). Nếu mất truyền thông, khung P2P này sẽ sụp đổ.
- **CRITICAL:** Việc cấm trao đổi Q (No P2P Q trading) kết hợp với hiện tượng dòng công suất lớn đi qua đường dây liên kết (transit currents) chính là nguyên nhân gốc rễ gây ra "Voltage Paradox". Lập luận rằng "ATC cap được giá" (Tie-line Congestion Paradox) chỉ đúng trên giấy khi bỏ qua sự sụp đổ điện áp vật lý do thiếu Q. 
- **MAJOR:** Sự ép buộc cắt tải P để cứu điện áp có thể do mô hình chưa tối ưu hóa Q cục bộ (BESS inverter, PV inverter). Khẳng định "AC-OPF necessity" là đúng, nhưng giải pháp "load shedding P" là thụ động (passive) chứ không phải thích ứng (fault-adaptive).

---
## TỔNG HỢP VÀ ĐỀ XUẤT (EDITORIAL SYNTHESIS)
**Đánh giá sự đồng thuận:**
Hội đồng đánh giá cao cấu trúc và các phát hiện lý thuyết (Paradoxes). Tuy nhiên, có sự lo ngại lớn từ Domain và Devil's Advocate về tính thực tiễn của giả định truyền thông và cách xử lý sự cố sụt áp bằng cắt tải P thay vì bù Q.

**Roadmap Chỉnh sửa (Revision Roadmap):**
1. **[CRITICAL] Phân tích độ nhạy truyền thông (Communication Failure):** Cần thêm một kịch bản hoặc đoạn thảo luận về cách hệ thống hoạt động nếu mất tín hiệu ATC (fallback to local control).
2. **[CRITICAL] Làm rõ giới hạn của 1MVA Base & SOCP Gap:** Thêm một chú thích (remark) chứng minh relaxation gap = 0 ngay cả khi sụt áp nặng.
3. **[MAJOR] Tái định hình "Voltage Paradox":** Phải thừa nhận rằng cắt tải P là "last resort" (biện pháp cuối cùng) do thiếu hạ tầng bù Q tĩnh/động, chứ không phải là một "phương pháp tối ưu hóa hoàn hảo". Nêu bật hơn nữa vai trò của "Future Work" về Smart Inverters.
4. **[MINOR] Khái niệm hóa "Moral Hazard" trong P2P:** Thảo luận ngắn ở chương 5 hoặc kết luận về hành vi thị trường khi có Negative Premium.

**Quyết định cuối cùng:** MAJOR REVISION. Các lập luận toán học tốt nhưng cần làm rõ ranh giới của các giả định vật lý và truyền thông.
