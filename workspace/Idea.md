# Spec: Kế hoạch Phân tích Kết quả & Viết Chapter 6 (Top-Down Approach)

## 1. Mục tiêu (Objective & Success Criteria)
- **Objective:** Lập kế hoạch và triển khai viết Chapter 6 (Results and Discussion) dựa trên 5 Stage kết quả mô phỏng trong `Transfer folder/Result_data/report_result/`.
- Áp dụng phương pháp tiếp cận **Top-Down**: Đi từ vĩ mô (Kinh tế tổng thể) xuống vi mô (Điều phối kỹ thuật tại MG) và cuối cùng là hiệu năng thuật toán & tín hiệu thị trường.
- **Liên kết chặt chẽ với những đóng góp cốt lõi (Contributions):**
  1. Bảo vệ 100% Critical Load (Security).
  2. The Denominator Effect (Tiệm cận hoàn hảo với Perfect Foresight).
  3. Synergistic Negative Premium (Mạng P2P giải phóng năng lượng tái tạo, tăng sức chống chịu nhưng lại giảm chi phí).
- **Success Criteria:**
  - Hoàn thành bộ khung sườn (Outline) cho Chapter 6 thể hiện rõ mạch logic Top-Down.
  - Phân chia các Task rõ ràng để xử lý dần các Stage 1-5, nhúng hình ảnh và diễn giải vào file LaTeX.
  - Nhận được sự đồng thuận của Tư lệnh về hướng đi trước khi tạo ACTION_PLAN.md.

## 2. Giả định (Assumptions)
- Dữ liệu ở `Transfer folder/Result_data` là dữ liệu chuẩn cuối cùng (Supreme Source of Truth), không cần chạy lại mô phỏng Python.
- Các file phân tích gốc như `Analysis_Stage1_Report.md` chứa logic cốt lõi sẽ được dùng làm nền tảng lý luận trong bài luận.
- Định dạng báo cáo tuân thủ chuẩn LaTeX IEEE / Thesis hiện tại của dự án.

## 3. Cấu trúc Top-Down dự kiến cho Chapter 6 (Tech Stack & Structure)
- **6.0 (Pre-flight Task): Khảo sát Dàn trang Ảnh (Image Layout Survey):** Nháp thử cấu trúc layout LaTeX (ví dụ: hình ảnh 4-panel cho 4 MGs, hình ảnh side-by-side) bằng `\begin{figure}` hoặc `subfigure` để đảm bảo không bị vỡ bố cục trước khi nhúng toàn bộ data.
- **6.1 System Configuration & Simulation Scenarios:** (Tổng quan) **Di dời toàn bộ nội dung Section 3.1 (Peer-to-Peer Interconnection Topology) xuống đây**. Bổ sung thêm thông số cấu hình mạng lưới (dung lượng các nguồn, tải) và định nghĩa chi tiết 3 kịch bản so sánh (Base Fault, Perfect Foresight, Current MPC). 
- **Tránh từ ngữ cảm xúc:** Dùng ngôn ngữ khoa học, lạnh lùng (aggressively -> heavily, frantically -> rapidly, savior -> supporting MGs).

## 4. Phase 4: Algorithmic Scalability & Market Dynamics (Stage 4 & 5)
- **Objective:** Prove the computational robustness and economic intelligence of the decentralized MPC-ATC framework.
- **Stage 4 (Algorithmic Convergence - Section 6.5):**
  - **CPU Time:** So sánh Perfect Foresight (Monolithic bottleneck, ~584s) và MPC (Rolling horizon, ~413s total). Nhấn mạnh max CPU time của 1 bước MPC khi xảy ra sự cố chỉ là ~91s (tại t=10), hoàn toàn đáp ứng được thời gian thực (Real-Time Feasibility).
  - **ATC Convergence:** Phân tích sự hội tụ của thuật toán ATC (Decentralized Coordination). Dù có sự cố đứt gãy lưới, các Microgrid vẫn đàm phán thành công mức giao dịch P2P, residual decay về 0.0 chỉ trong 3-4 steps.
- **Stage 5 (Scarcity Pricing - Section 6.6):**
  - Đổi tên mục thành "Scarcity Pricing Dynamics (Stage 5)".
  - Phân tích tín hiệu giá nội bộ $\lambda$ (ATC multipliers). Giờ bình thường giá ổn định. Giờ có sự cố (Fault window t=9 đến t=15), giá $\lambda$ tăng vọt tạo thành "Scarcity Pricing" (Giá khan hiếm).
  - **Market Signaling:** Sự leo thang của giá $\lambda$ tự động tạo động lực kinh tế cho các MG thặng dư (MG2, MG3) xả BESS xuất điện để tối đa hóa lợi nhuận P2P, đồng thời ép các MG thâm hụt (MG1, MG4) mua điện với giá cao để bảo vệ Critical Load. Đây là minh chứng hệ thống không chỉ là Electrical Controller mà còn là một thị trường tự vận hành.

- **6.2 Macro-Economic Assessment & System Resilience (Dựa trên Stage 1):** (Vĩ mô) Phân tích True Economic Cost, Energy Mix. Bàn luận sâu về "100% Critical Load Protected" và "Negative Premium".
- **6.3 Spatiotemporal Energy Management (Dựa trên Stage 2):** (Hệ thống) Lập luận nhân quả phân tích sâu 3 kịch bản dựa trên EMS và BESS: (1) **Base Fault (Cô lập & Tự lực):** Biết trước lỗi nhưng không có P2P. EMS vắt kiệt BESS, xả dốc đứng, dẫn tới cắt cả Critical Load. (2) **Perfect Foresight (Toàn tri):** Biết trước 24h, có P2P. EMS sạc BESS trước khi lỗi và xả mượt mà. (3) **Current Method (MPC thực chiến):** Không biết khi nào hết lỗi, có P2P. EMS sinh hội chứng "Hoarding" BESS, dè dặt xả và cuống cuồng mua P2P để bù đắp, sinh ra Negative Premium nhưng vẫn bảo vệ 100% Critical Load. Yêu cầu chui sâu phân tích từng tổ hợp ảnh 4-panel (SOC và Active Power) của từng MGs để chứng minh hành vi này.
- **6.4 Local Power Quality & Voltage Stability (Dựa trên Stage 3):** (Vi mô/Vật lý) Khảo sát Load Shedding tại từng node (cột đen Critical bằng 0). Phân tích vai trò trung chuyển (Transmission Intermediary) của MG4 khiến nó chịu áp lực sụt áp khổng lồ, buộc các máy phát phải bơm Q kịch liệt. Khảo sát Voltage Profile: trong giờ bình thường áp nằm trong soft limits, khi có lỗi mở tung ra hard limits [0.95, 1.05] để tối đa hóa dung lượng truyền tải P2P.
- **6.5 Algorithmic Performance & Market Dynamics (Dựa trên Stage 4 & 5):** (Thuật toán) Chứng minh tính hội tụ của ATC, CPU time, sự hình thành tín hiệu giá giao dịch nội bộ ($\lambda$) và tổn hao mạng (Power Loss).
- **6.6 Robustness & Sensitivity Analysis (Dựa trên Stage 6):** (Sức bền/Stress Test) Bổ sung phân tích sâu về ma trận 3 tầng (3-Level Stress Test Matrix):
  - **Level 1 (Temporal Depth):** Kéo dài sự cố 11 tiếng để chứng minh hiệu quả pre-charging của MPC.
  - **Level 2 (Spatial Depth):** Chồng chéo sự cố (Mất Grid + PV Loss) để chứng minh hiện tượng Scarcity Pricing và tự vệ hệ thống.
  - **Level 3 (Spatiotemporal Depth):** Siêu thảm họa tổ hợp, kiểm tra Ultimate Resilience Limit và chứng minh 100% Critical Load được bảo vệ dưới áp lực cực đoan.

## 4. Ranh giới (Boundaries)
- **Luôn luôn:** Diễn giải kết quả thông qua lăng kính "Contributions" đã định hình (Tuyệt đối không dừng lại ở việc mô tả biểu đồ tăng giảm đơn thuần). Bám sát các con số cốt lõi (như 15.4260 MWh vs 2.9130 MWh).
- **Hỏi ý kiến trước (ASK FIRST):** Bố cục lại số lượng hình ảnh nếu có quá nhiều hình trong 1 Section làm vỡ cấu trúc LaTeX.
- **Nghiêm cấm (FORBIDDEN):** Tự ý bịa số liệu. Mọi con số phải trích xuất chuẩn xác từ các file `.md` và `.csv` trong folder `report_result`.
