# Spec: Kế hoạch Viết Chapter 1 & Chapter 6 (Top-Down Approach)

## 0. Cập nhật Spec cho Chapter 1 (Introduction & Literature Review)
- **Mục tiêu:** Gộp Chapter 1 và 2 cũ thành một chương Introduction duy nhất, phân rã theo 3 Lăng kính (Physical, Spatial, Temporal).
- **Ràng buộc Mới (Constraints):**
  - Tuyệt đối không giao dịch Công suất phản kháng ($Q$). $Q$ chỉ được sinh ra và quản lý nội bộ để đảm bảo an toàn điện áp. 
  - Gộp các góp ý phản biện: Nhấn mạnh "Dynamic Value of Lost Load (VoLL)", Islanding Physics, và Computational Tractability (Độ phức tạp tính toán của MPC+ATC+SOCP).
  - Không có "Fluff" trong toán học.
  - **Quy tắc Trích dẫn (Citation Granularity):** Tuyệt đối băm nhỏ các trích dẫn và cắm sát vào từng luận điểm chi tiết. Giới hạn TỐI ĐA 2 bài báo cho mỗi cụm/câu. Không dồn 1 cục (3-4 bài báo) ở cuối câu dài. Cắt ngắn câu văn, đi trực diện vào bản chất kỹ thuật.

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
- **6.6 Robustness & Sensitivity Analysis (The Stress Test Matrix):** Phân tích sức bền của hệ thống qua ma trận 4 kịch bản lỗi dưới góc độ 3 Lăng kính Kỹ thuật (Metrics). **Tiêu chuẩn mục tiêu khi viết: Phải tuân thủ nghiêm ngặt Mạch logic Nhân quả Top-Down:**
  - **6.6.1 (Nguyên nhân khởi nguồn - Tầng Lưới): Active Power Routing & Network Endurance**
    - *Hình ảnh:* `Stage6_P2P.png`.
    - *Nội dung:* Sự thiếu hụt công suất lan rộng ép mạng lưới phải vắt kiệt công suất truyền tải P2P (mở rộng dải màu), đẩy các đường Tie-line lên sát giới hạn nhiệt. Dòng điện (I) tăng đột biến.
  - **6.6.2 (Hệ quả Vật lý - Tầng Áp): Voltage Stability & Security Margins**
    - *Hình ảnh:* `Stage6_Voltage.png`.
    - *Nội dung:* Dòng tải (I) khổng lồ dội xuống mạng lưới sinh ra độ sụt áp nghiêm trọng ($I \times Z$). Đường bao điện áp (Voltage Envelope) bị kéo tụt đâm thủng Soft Cap, lùi về sát vùng tử địa Hard Cap (0.90 p.u.).
  - **6.6.3 (Quyết định Sinh tử - Tầng Kinh tế & Mục tiêu): Autonomous Critical Load Prioritization & Economic Cost**
    - *Hình ảnh:* `Stage6_CostShedding.png` và `Robustness_Cost_vs_Shedding copy.png`.
    - *Nội dung:* Để ngăn điện áp ở 6.6.2 thủng đáy, thuật toán buộc phải hy sinh: Cắt đứt phụ tải thường (Normal Load Shedding tăng phi mã, đẩy Cost lên cao) nhằm giảm tải dòng $I$. **Cú chốt hạ:** Sự tàn nhẫn này đổi lại Bằng chứng thép là Critical Load Shedding vĩnh viễn bị khóa chặt ở `0.0 MWh` (Hoàn thành mục tiêu 100%).

## 4. Ranh giới (Boundaries)
- **Luôn luôn:** Diễn giải kết quả thông qua lăng kính "Contributions" đã định hình (Tuyệt đối không dừng lại ở việc mô tả biểu đồ tăng giảm đơn thuần). Bám sát các con số cốt lõi (như 15.4260 MWh vs 2.9130 MWh).
- **Hỏi ý kiến trước (ASK FIRST):** Bố cục lại số lượng hình ảnh nếu có quá nhiều hình trong 1 Section làm vỡ cấu trúc LaTeX.
- **Nghiêm cấm (FORBIDDEN):** Tự ý bịa số liệu. Mọi con số phải trích xuất chuẩn xác từ các file `.md` và `.csv` trong folder `report_result`.

---

# Spec: Kế hoạch Viết Chapter 7 (Conclusion & Future Work)

## 1. Mục tiêu (Objective & Success Criteria)
- Đúc kết toàn bộ giá trị cốt lõi của Luận văn qua 4 trụ cột học thuật sắc bén, triệt tiêu mọi cách diễn đạt dài dòng, sách giáo khoa.
- Đề xuất các hướng phát triển tương lai (Future Work) nhằm vá trực tiếp các điểm yếu (Pain points) vật lý và thuật toán đã bộc lộ ở Chương 6 (ví dụ: Sập áp do $I^2X$, Hoarding BESS do MPC).

## 2. Cấu trúc nội dung (Tech Stack & Structure)
### 7.1. Conclusion (4 Trụ cột Học thuật)
1. **Algorithmic Architecture:** Tích hợp thành công "Bottom-up Spatiotemporal 3-Mode State Machine". Thuật toán ATC đạt tốc độ hội tụ cực nhanh (max 91s) khi lưới bị sốc cấu trúc nhờ Warm-start.
2. **Physical Resilience & AC-OPF Necessity:** AC-OPF là bắt buộc. Phát hiện dòng điện quá cảnh (transit currents) sinh tổn hao vô công $I^2X$ làm sập áp. Hệ thống đã "cắt tải P chủ động" để triệt tiêu dòng $I$, cứu điện áp khỏi giới hạn 0.90 p.u.
3. **Market Pricing & Tie-line Congestion Paradox:** Khám phá nghịch lý tắc nghẽn. Giá đồng thuận ATC ($\lambda$) cách ly hoàn toàn khỏi sự bùng nổ giá cục bộ (VOLL) tại các điểm thiếu hụt, tuân thủ đúng giới hạn vật lý KKT của cáp truyền tải.
4. **Ultimate Security & Graceful Degradation:** Bảo vệ 100% Critical Loads. Đạt lợi ích kép "Negative Premium" nhờ định tuyến P2P giải phóng Stranded Energy, kết hợp cơ chế Graceful Degradation chủ động hy sinh tải thường khi cần thiết.

### 7.2. Future Work (Trị tận gốc Pain Points)
1. **Overcoming MPC "Hoarding" Syndrome:** Tích hợp Reinforcement Learning (RL) hoặc Adaptive SOC Penalty để BESS xả dứt khoát hơn. Kết hợp Stochastic MPC để trị bất định từ năng lượng tái tạo.
2. **Hardware & Reactive Power Support:** Tích hợp thiết bị bù vô công động (STATCOM, SVC) hoặc Smart Inverter (Volt-VAR control) để bơm Q, tháo gỡ triệt để việc MG4 phải cắt tải P oan uổng chỉ để giữ áp.
3. **Dynamic Topology Reconfiguration:** Tích hợp cơ chế điều khiển khóa điện động (Dynamic Switch Control) và cấu hình lại lưới điện thời gian thực để tự động cách ly vùng đứt gãy vật lý, mở ra các lộ tuyến dự phòng nhằm tối ưu hóa dòng công suất.

---

# Spec: Kế hoạch Viết Abstract (Tóm tắt Luận văn)

## 1. Mục tiêu (Objective)
- Cô đọng toàn bộ giá trị cốt lõi của luận văn trong khoảng 250-300 từ.
- Phải thể hiện được 3 yếu tố: Vấn đề (Motivation), Cỗ máy giải quyết (Methodology), và Kết quả đột phá (Key Findings).

## 2. Cấu trúc nội dung (Structure)
- **Background & Motivation (2-3 câu):** Sự yếu ớt của lưới điện phân phối trước các sự cố cực đoan (Extreme Events) và giới hạn của các mô hình quản lý tập trung, tuyến tính cũ.
- **Methodology (3-4 câu):** Đề xuất kiến trúc Bottom-up kết hợp 3 mũi nhọn: **SOCP** (đảm bảo vật lý thực AC-OPF, chống sập áp), **ATC** (tối ưu hóa phân tán bảo vệ quyền riêng tư), và **MPC** (cuốn chiếu thời gian, thích ứng với bất định).
- **Key Results (3-4 câu):** Nhấn mạnh các cực trị đạt được:
  - Bảo vệ thành công **100% Critical Loads**.
  - Hiện thực hóa **Negative Premium** (giảm chi phí nhờ P2P giải phóng Stranded Energy).
  - Khám phá **Tie-line Congestion Paradox** (Giá $\lambda$ ATC cách ly khỏi VOLL, tuân thủ giới hạn KKT) và **Voltage Paradox** (Hy sinh tải P để triệt tiêu dòng $I$, ngăn sập áp do $I^2X$).
- **Conclusion (1-2 câu chốt):** Một khung giao dịch năng lượng tự phục hồi (fault-adaptive), bảo mật và tuân thủ chặt chẽ giới hạn vật lý lưới điện.
