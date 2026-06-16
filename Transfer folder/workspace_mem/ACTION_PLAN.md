# ACTION PLAN - XỬ LÝ CÁC TÁC VỤ TỒN ĐỌNG VÀ TRIỂN KHAI 4-STAGE ARCHITECTURE

*Dựa trên những phát hiện học thuật chấn động ở Stage 1 (Negative Premium & 100% Critical Load Protected), kế hoạch đã được tái cấu trúc hoàn toàn. Toàn bộ Task 4.5 cũ đã được loại bỏ. Các công việc xuất biểu đồ mới và phân tích sẽ được dồn vào Task 5 và Task 6 theo thiết kế Top-Down 4 Tầng.*

## Các hạng mục đã hoàn tất (Task 0 đến Task 4.4)
Tất cả các Task từ khảo sát tài liệu (Task 0), cấu hình kịch bản lỗi N-2 (Task 1), tối ưu Hybrid Warm-Start (Task 2), đến xây dựng hệ thống Benchmark 3 Models (Task 4.4) đều đã hoàn tất `[x] DONE`. Dữ liệu gốc đã xuất thành công. Đã chứng minh được bản chất của ATC và MPC.

---

## Task 5: Data Export & Visualizations (4-Stage Architecture Blueprint)
*Nhiệm vụ: Vẽ và xuất các đồ thị chứng minh cho Tầng 2, 3 và 4.*

### Task 5.1: Tầng 2 - Đồ thị Động lực học & Phản ứng của MPC
- **Tình trạng:** `[x] DONE`
- **Agent phụ trách:** `agents/code_generator.md` & `agents/latex_writer.md`
- **Chi tiết thực thi:**
  - *Ghi chú:* Đồ thị EMS đã có sẵn trong `Result_data\foresight_model` và `Result_data\current_method`.
  - Vẽ 4 đồ thị So sánh đường cong Pin (SOC Curve) riêng biệt cho cả 4 Microgrids.
  - Viết bản phân tích chi tiết (Detailed Analysis) cho Tầng 2, đánh giá phản ứng của từng MG (kẻ gánh vác, người gặp nạn) trong pha sự cố.
- **Tiêu chí nghiệm thu:** Sinh ra 4 file đồ thị SOC và 1 file `.md` phân tích lưu vào `Result_data/report_result/stage_2`.

### Task 5.2: Tầng 3 - Vật lý Điện Xoay chiều (Voltage, Q & Loss)
- **Tình trạng:** `[x] DONE`
- **Agent phụ trách:** `agents/code_generator.md`
- **Chi tiết thực thi:**
  - Viết script vẽ đồ thị Voltage Profile Curve theo trục thời gian (Horizon 1-24h). Vẽ dạng multiple lines cho tất cả các nodes của từng MG, làm nổi bật (highlight) dải Max-Min và đường giá trị Mean. Tách thành 4 đồ thị riêng biệt cho 4 MGs (MG1 đến MG4). Kẻ vạch an toàn $0.9$ và $1.1$.
  - Vẽ biểu đồ Stacked Bar Load Shedding riêng biệt cho 4 Microgrids (MG1, MG2, MG3, MG4), bất kể có cắt tải hay không, để so sánh đồng bộ. Thể hiện $P_{shed\_normal}$ (đỏ) và $P_{shed\_critical}$ (đen). Chứng minh thanh đen luôn bằng 0.
- **Tiêu chí nghiệm thu:** Sinh ra các file đồ thị png lưu vào `Result_data/report_result/stage_3`.

### Task 5.3: Tầng 4 - Scalability & Convergence
- **Tình trạng:** `[>] IMPLEMENTING`
- **Chi tiết thực thi:** Nhiệm vụ này được chia làm 2 sub-tasks.

#### Task 5.3.1: Vi phẫu mã nguồn để trích xuất Metrics
- **Tình trạng:** `[x] DONE`
- **Agent phụ trách:** `agents/code_generator.md`
- **Chi tiết thực thi:**
  - Sửa `build_model.py`: Thu thập mảng `history_r` cho TẤT CẢ các giờ sự cố (thay vì chỉ t=9) vào dict `convergence_all_hours`.
  - Sửa `main.py`: Xuất dữ liệu `convergence_all_hours` vào `Result_data/stage4_metrics.json`.
- **Tiêu chí nghiệm thu:** Chạy thành công `main.py` và có file `stage4_metrics.json` chứa dữ liệu hợp lệ.

#### Task 5.3.2: Vẽ đồ thị Tầng 4
- **Tình trạng:** `[x] DONE`
- **Agent phụ trách:** `agents/code_generator.md`
- **Chi tiết thực thi:**
  - Vẽ biểu đồ Bar Chart cho Thời gian tính toán CPU qua 24 giờ (HourTime Graph).
  - Vẽ biểu đồ Line Chart thể hiện đường cong hội tụ (Convergence curve của Residuals) cho TẤT CẢ các giờ sự cố (All Fault Hours).
- **Tiêu chí nghiệm thu:** Sinh ra các file đồ thị png lưu vào `Result_data/report_result/stage_4`.

---

## Task 6: Viết Báo cáo & Phân tích (Top-Down Approach)
*Nhiệm vụ: Viết báo cáo chuẩn học thuật IEEE trình bày "Câu chuyện cốt lõi" dựa trên số liệu của Task 5.*

### Task 6.1: Viết phân tích Tầng 1 và Tầng 2 (Economics & Temporal Dynamics)
- **Tình trạng:** `[ ] TODO`
- **Agent phụ trách:** `agents/latex_writer.md`
- **Chi tiết thực thi:**
  - Đưa bảng Benchmark (Eco Gap 2.49%, Negative Premium) vào luận điểm đầu tiên.
  - Phân tích sự vượt trội của MPC so với Foresight thông qua đồ thị SOC vừa xuất.
- **Tiêu chí nghiệm thu:** Hoàn thiện bản nháp phân tích phần 1 & 2.

### Task 6.2: Viết phân tích Tầng 3 và Tầng 4 (AC Physics & Algorithmic Scalability)
- **Tình trạng:** `[x] DONE`
- **Agent phụ trách:** `agents/latex_writer.md`
- **Chi tiết thực thi:**
  - Dùng Voltage Profile và Shedding Bar để chứng minh bài toán vật lý AC-OPF thành công.
  - Dùng Dual-Axis Lamda và CPU Time để chứng minh cơ chế ATC thời gian thực.
- **Tiêu chí nghiệm thu:** Hoàn thiện bản nháp phân tích phần 3 & 4.

---

## Task 7: Tầng 5 - Market Depth (ATC Pricing Dynamics)
*Nhiệm vụ: Trực quan hóa tiến trình định giá thị trường nội bộ.*

### Task 7.1: Trích xuất dữ liệu Lambda
- **Tình trạng:** `[x] DONE`
- **Agent phụ trách:** `agents/code_generator.md`
- **Chi tiết thực thi:** 
  - Lưu mảng giá trị đối ngẫu $\lambda$ (Dual multipliers / Price) của 5 đường liên kết mạng P2P qua 24 giờ.

### Task 7.2: Vẽ đồ thị Price
- **Tình trạng:** `[x] DONE`
- **Agent phụ trách:** `agents/code_generator.md`
- **Chi tiết thực thi:**
  - Vẽ 1 đồ thị thể hiện giá $\lambda$ của 5 đường liên kết trên cùng 1 trục thời gian (24h).

### Task 7.3: Viết phân tích Tầng 5
- **Tình trạng:** `[x] DONE`
- **Agent phụ trách:** `agents/latex_writer.md`
- **Chi tiết thực thi:** Dựa vào đồ thị $\lambda$ để chứng minh hiệu quả tín hiệu thị trường tự động (Scarcity Pricing).
