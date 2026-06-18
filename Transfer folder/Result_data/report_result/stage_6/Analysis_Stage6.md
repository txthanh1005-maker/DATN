# Stage 6: Robustness & Sensitivity Analysis (Stress Test Matrix)

**Title Proposal:** Stress Test Matrix: Evaluating Algorithm Resilience Across Fault Complexity Depths

Để chứng minh tính bền vững tuyệt đối (Robustness) của cơ chế điều khiển MPC-ATC đề xuất, hệ thống Mạng lưới Microgrid (MMG) không chỉ được kiểm tra dưới các sự cố đơn lẻ (N-1) mà còn bị đẩy đến giới hạn sụp đổ thông qua một ma trận kiểm thử 3 tầng (3-Level Stress Test Matrix). Ma trận này leo thang độ phức tạp của sự cố theo 3 chiều sâu: Thời gian (Temporal), Không gian (Spatial), và Tổ hợp (Spatiotemporal).

---

## 1. Level 1: Temporal Depth - Kéo dài sự cố (Temporal Stress)

- **Kịch bản:** Mất kết nối lưới điện chính (Grid Loss) xảy ra cục bộ tại MG2 và MG4 nhưng bị kéo dài cực đoan trong **11 tiếng liên tục** (từ giờ 9 đến giờ 19). Năng lượng tái tạo (PV) vẫn hoạt động bình thường.
- **Mục tiêu lý thuyết (Theoretical Objective):** Đánh giá **Sức bền năng lượng (Energy Endurance)** và tính ưu việt của "Tầm nhìn xa" (Look-ahead horizon) trong cơ chế dự báo MPC.
- **Hệ quả phân tích:**
  - Sự cố kéo dài làm triệt tiêu hoàn toàn bộ đệm năng lượng (BESS) nếu chỉ dùng các thuật toán cận thị (Myopic). 
  - Tuy nhiên, kết quả từ đồ thị SOC chứng minh MPC đã dự báo trước sự cố (thông qua cập nhật liên tục), ra lệnh sạc trước (Pre-charging) cho Pin trong các giờ 1-8. 
  - Khi sự cố xảy ra, các MG bị đứt lưới vẫn sống sót nhờ xả Pin từ từ và nhập khẩu điện (P2P) từ các MG lân cận. 
  - **Tiểu kết Tầng 1:** Hệ thống hoàn toàn có thể chịu đựng lỗi kéo dài nếu đường truyền không gian (tie-lines) và PV cục bộ vẫn thông suốt.

---

## 2. Level 2: Spatial Depth - Lan rộng và chồng chéo sự cố (Spatial Stress)

- **Kịch bản:** Phạm vi sự cố lan rộng ra 3/4 mạng lưới (MG1, MG2, MG4). Đặc biệt, áp dụng mô hình **Thảm họa kép (Double Fault):** Mất Grid (giờ 9-15) đi kèm với Sập toàn bộ điện mặt trời (PV Loss) từ giờ 11-15.
- **Mục tiêu lý thuyết:** Đánh giá phản ứng của thị trường nội bộ trước **Tình trạng khan hiếm tột độ (Extreme Scarcity)** và rào cản vật lý (Network Squeeze / Congestion).
- **Hệ quả phân tích:**
  - Ở Giờ 11, lượng năng lượng thiếu hụt nhảy vọt. MG1, MG2, MG4 đồng loạt tranh giành mua điện từ nguồn duy nhất còn sống sót (MG3). 
  - Nút thắt truyền tải (Tie-line congestion) và sụt giảm điện áp (Voltage limits) bị kích hoạt ở mức tối đa. 
  - **Về mặt toán học:** Sự khan hiếm đẩy giá bóng đối ngẫu (Dual variables $\lambda$) lên cao chót vót. Áp lực chạm biên điện áp khiến thuật toán ADMM/ATC giằng co quyết liệt tại điểm cực hạn.
  - **Về mặt vật lý:** Hệ thống tự động kích hoạt cơ chế "Tự vệ" (Self-defense mechanism) - bắt buộc cắt bỏ Tải Thường (Normal Load Shedding) để giữ mức điện áp AC-OPF trong giới hạn an toàn.
  - **Tiểu kết Tầng 2:** Đây là minh chứng sắc bén cho hiệu ứng *Scarcity Pricing* (Định giá theo sự khan hiếm). Thuật toán đã chấp nhận hy sinh tính tối ưu kinh tế (Total Cost) để duy trì sự sống sót của vật lý lưới.

---

## 3. Level 3: Spatiotemporal Depth - Siêu thảm họa tổ hợp (Spatiotemporal Extreme)

- **Kịch bản:** Đây là "Black Swan Event" (Sự kiện thiên nga đen) kết hợp sự tàn khốc của cả hai tầng trên: Mất Grid VÀ mất PV trên diện rộng (3 MGs), đồng thời bị kéo dài vắt kiệt qua 11 tiếng (Giờ 9 đến 19).
- **Mục tiêu lý thuyết:** Kiểm tra **Giới hạn chịu đựng tối hậu (Ultimate Resilience Limit)** và khả năng "Suy thoái có kiểm soát" (Graceful Degradation).
- **Hệ quả phân tích:**
  - Dưới sức ép tột độ, cạn kiệt cả năng lượng dự trữ lẫn nguồn phát, thuật toán buộc phải hy sinh kinh tế (Total Cost tăng vọt do chi phí phạt cắt tải khổng lồ). 
  - Lượng Normal Load Shedding diễn ra trên quy mô lớn và kéo dài liên tục. Thuật toán MPC-ATC phân tán đẩy mạng lưới vào chế độ sinh tồn cực đoan.
- **Giá trị cốt lõi (Core Academic Takeaway):** 
  - Dù mạng lưới bị dồn vào bước đường cùng, đồ thị Load Shedding vẫn kiêu hãnh chứng minh: **100% Tải Ưu Tiên (Critical Load) KHÔNG BAO GIỜ BỊ CẮT!** 
  - Thuật toán phân tán đã thành công rực rỡ trong việc tự động hóa quá trình ra quyết định: Linh hoạt hy sinh các mục tiêu thứ cấp (chi phí, tải phụ) để bảo vệ tuyệt đối mạch máu sinh tử của toàn bộ hệ thống MMG.
