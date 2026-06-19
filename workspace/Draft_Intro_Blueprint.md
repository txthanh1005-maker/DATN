# DÀN Ý CHI TIẾT CHAPTER 1 (INTRODUCTION AND LITERATURE REVIEW) - DEEP MODULAR BREAKDOWN

## 1. Mục tiêu và Giả định Mới
- Tích hợp 3 trục: SOCP (Vật lý), ATC (Không gian), MPC (Thời gian).
- **RÀNG BUỘC QUAN TRỌNG:** KHÔNG có thị trường giao dịch Công suất phản kháng ($Q$). $Q$ chỉ được sinh ra và quản lý nội bộ bên trong từng Microgrid để hỗ trợ điện áp cục bộ. P2P Trading chỉ áp dụng cho Công suất tác dụng ($P$).

## SUB-THEME 1: Lăng kính Vật lý (Power Flow & Network Constraints)
* **Chiến thuật biện luận:** Phá hủy tính hợp lý của các mô hình tuyến tính hóa trong môi trường lưới phân phối ($R/X$ cao).
* **Nhóm đồng thuận/Tranh luận:**
  1. **Phe 1 (Copper-plate/Lumped Node):** Phân tích các bài báo áp dụng P2P nhưng bỏ qua mạng lưới. *Chốt hạ:* Hệ quả tất yếu là nghẽn mạch cục bộ.
  2. **Phe 2 (LinDistFlow / MILP):** Phân tích các bài báo dùng mô hình DC-OPF. Phương pháp này gây sai số 5-10% ở $P-Q-V$ coupling và nguy cơ sụp áp.
  3. **Phe 3 (SOCP):** Phân tích SOCP để đạt Global Optimum.
* **Đóng chốt L2 Gap (Mô hình Toán học):** Rất ít nghiên cứu đưa SOCP vào P2P Trading trong điều kiện cắt lưới (Islanding). Khi mất kết nối lưới chính (mất Slack Bus vô hạn), nếu chỉ dùng DC-OPF, các hợp đồng tài chính P2P sẽ vỡ vụn vì sụp đổ điện áp vật lý. SOCP là công cụ bắt buộc để đồng bộ hóa dòng tiền P2P và giới hạn an toàn điện áp độc lập.

## SUB-THEME 2: Lăng kính Không gian & Bảo mật (Decentralization & Privacy)
* **Chiến thuật biện luận:** Phẫu thuật sự yếu kém của ADMM khi bị ép phải giải quyết các bài toán phân cấp.
* **Nhóm đồng thuận/Tranh luận:**
  1. **Phe 1 (Centralized EMS):** Dễ dàng tìm nghiệm tối ưu toàn cục nhưng vi phạm Privacy.
  2. **Phe 2 (ADMM ở cấu trúc phẳng):** Hoạt động cực tốt ở giao dịch P2P đơn tầng.
  3. **Phe 3 (ADMM ở cấu trúc phân cấp & SOCP):** Gặp ngay giới hạn hội tụ cực chậm, dao động nghiệm.
  4. **Phe 4 (Analytical Target Cascading - ATC):** Đưa ATC vào như vị cứu tinh cho bài toán phân cấp.
* **Đóng chốt L2 Gap (Cấu trúc Lưới):** Việc dùng ATC không chỉ vượt qua giới hạn hội tụ của ADMM ở cấu trúc đa tầng, mà còn tự động sinh ra tín hiệu giá DLMP cho P2P Trading thông qua hệ số phạt (penalty multipliers) một cách cực kỳ chặt chẽ về mặt toán học.

## SUB-THEME 3: Lăng kính Thời gian & Sức chống chịu (Temporal Dynamics & Grid Resilience)
* **Chiến thuật biện luận:** Đưa ra "Sự kiện Thiên nga đen" (Đứt lưới, Sập nguồn) để tiêu diệt các mô hình tĩnh.
* **Nhóm đồng thuận/Tranh luận:**
  1. **Phe 1 (Static Day-ahead Optimization):** Giải tối ưu 1 lần cho 24h. Sự tĩnh tại này sẽ sụp đổ toàn diện nếu có lỗi bất ngờ.
  2. **Phe 2 (Stochastic / Robust Optimization):** Tính toán quá nặng nề, khó áp dụng thời gian thực.
  3. **Phe 3 (Model Predictive Control - MPC):** Cơ chế Rolling Horizon phản xạ liên tục với bất định.
* **Đóng chốt L2 Gap (Động lực học & Thời gian đáp ứng):** Thiếu vắng một cơ chế điều khiển tối ưu thời gian thực đủ nhanh (Tractability) để giải bài toán phân cấp phi tuyến (ATC-SOCP). Khung học thuyết này phải có khả năng bẻ lái quỹ đạo tải để hy sinh tải thường (Graceful Degradation) nhằm tử thủ 100% Critical Load, dẫn đến sự hình thành "Dynamic Value of Lost Load (VoLL)" / Resilience Pricing thay vì chỉ tối ưu kinh tế ngày bình thường.

## TỔNG HỢP (THE MASTER GAP & OBJECTIVES)
* Một lỗ hổng nghiêm trọng tồn tại: Thiếu một khung lý thuyết thống nhất kết hợp sự chính xác vật lý của SOCP, khả năng phân cấp bảo mật của ATC, và phản xạ thời gian thực của MPC có khả năng giải quyết trong thời gian giới hạn (Tractability).
* Dẫn thẳng đến 4 Mục tiêu Nghiên cứu (Objectives).
