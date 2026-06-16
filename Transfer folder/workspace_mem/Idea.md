# Bản Đặc Tả Kế Hoạch (Idea) - Chiến dịch Phân tích và Xuất bản Báo cáo (The 5-Stage Architecture)
*(Tạo bởi Meta-Agent / CEO)*

## 1. Mục tiêu (Objective)
- Xây dựng bài báo học thuật chuẩn Q1 IEEE dựa trên khung phân tích Top-Down 4 Tầng.
- Chứng minh sức mạnh của "Bộ Ba Thần Thánh" (MPC, SOCP, ATC) trong việc vận hành lưới điện khẩn cấp.
- Giải quyết dứt điểm các tác vụ từ Task 4.5.5 đến Task 6 (Vẽ biểu đồ, Viết Intro/Methodology, Phân tích kết quả).

## 2. Đầu ra dự kiến (Expected Deliverables)
- **Tập hợp Đồ thị Chuyên sâu (Visual Assets):** Hoàn thiện các đồ thị còn thiếu ở Tầng 2, 3 và 4 (Đồ thị SOC so sánh MPC vs Foresight, Đồ thị Voltage/Q, Đồ thị Convergence).
- **Tài liệu Phân tích Chi tiết (Analysis Reports):** Bản nháp nội dung phân tích (Case Study & Analysis) dựa trên các đồ thị.
- **Tài liệu Thuyết minh Toán học (Math Formulation):** Công thức toán học AC-OPF, SOCP Relaxation, ATC Pricing và cơ chế MPC Rolling Horizon.

## 3. Quyết định Kiến trúc & Cốt lõi Học thuật (Core Theme)
*Hệ thống điều khiển phi tập trung P2P đạt được Khả năng phục hồi không mất phí (Zero-Cost Resilience) và Bảo vệ tuyệt đối 100% tải quan trọng dưới sự cố N-2 nhờ giải phóng năng lượng tái tạo mắc kẹt.*
- **Stage 1 (Macro):** Khẳng định sự tối ưu kinh tế và khả năng tiệm cận Global Optimum của MPC.
- **Stage 2 (Intra-MG):** Chứng minh sự linh hoạt của BESS dưới điều khiển của MPC (Không sạc đón đầu nhưng vẫn sinh tồn) và việc tận dụng năng lượng bị cắt bỏ.
- **Stage 3 (AC Physics):** Bảo chứng vật lý cho hệ thống thông qua điều khiển Công suất phản kháng (Q), Tổn hao lưới điện (Loss) và Điện áp (V) bằng thư giãn SOCP. (Trực quan hóa: Voltage Profile theo trục thời gian với dải Max-Min-Mean; Load Shedding tách riêng cho từng Microgrid).
- **Stage 4 (Algorithm & Market):** Cơ chế định giá khan hiếm (Scarcity Pricing) điều tiết tự động thông qua ATC với thời gian giải đáp ứng thực tế.
- **Stage 5 (Market Depth):** Chứng minh ranh giới kỹ thuật thông qua biểu đồ ATC Pricing Dynamics ($\lambda$) của 5 đường liên kết mạng trên cùng 1 đồ thị, minh họa tự động hóa định giá khan hiếm của thị trường P2P.

## 4. Ranh giới Dự án (Boundaries & Scope)
- **Luôn thực hiện (Always Do):** Mọi đồ thị xuất ra phải tuân thủ nghiêm ngặt "Quy tắc Đơn vị" (Per Unit chuyển sang MW/MWh). Đồ thị phải được lưu bằng hàm `plot_ieee_graphs` (Pyomo). Đối với Tầng 4, phải đo lường Wall-clock Time cho Day-Ahead và Perfect Foresight, kết hợp với CPU Time cho từng giờ của MPC (HourTime graph). Đồ thị hội tụ phải hiển thị cho TẤT CẢ các giờ xảy ra sự cố (Convergence for all fault hours).
- **Tuyệt đối KHÔNG (Never Do):** Không tự ý sửa đổi logic điều khiển lõi của mô phỏng gốc (`build_model.py`, `main.py`). Chỉ được chèn thêm biến đếm thời gian (time) và mảng lưu phần dư hội tụ (Residuals) vào các hàm hiện có, không làm thay đổi luồng dữ liệu tối ưu.
- **Xin phép trước (Ask First):** Khi muốn bổ sung một chỉ số mới ngoài 4 Tầng đã định nghĩa.

## 5. Success Criteria (Tiêu chuẩn Thành công)
- Các file hình ảnh cho cả 4 Tầng đều đã được xuất thành công vào `Result_data/report_result/`.
- Tài liệu Phân tích (Analysis) làm nổi bật được lợi ích của MPC, SOCP và ATC mà không bị trùng lặp.
- Mạch văn logic, dẫn chứng toán học mạch lạc.

## 6. Open Questions
- Liệu ta có cần thêm cấu hình phân tích độ nhạy (Sensitivity Analysis) vào Tầng cuối cùng không? (Đợi quyết định từ Tư lệnh).
