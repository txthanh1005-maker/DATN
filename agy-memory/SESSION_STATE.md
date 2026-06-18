## Goal
Nâng cấp và chuyển đổi toàn bộ báo cáo Đồ án Tốt nghiệp (DATN) từ thuật toán ADMM cũ sang kiến trúc mới: **Analytical Target Cascading (ATC) & Model Predictive Control (MPC)**. Quản lý toàn bộ vòng đời tác chiến thông qua "Supreme Source of Truth" tại `agy-memory/SESSION_STATE.md`.

## Constraints
- Tuyệt đối tuân thủ kiến trúc hệ thống hiện tại: Hierarchical ATC, thuật toán MPC & SOCP.
- Không tự ý sửa đổi code lõi (`main.py`, `build_model.py`, v.v.), trừ khi có lỗi hoặc yêu cầu thêm kịch bản mới. `Transfer folder` là nguồn dữ liệu chuẩn.
- Mọi nhiệm vụ LaTeX phải tuân thủ nghiêm ngặt quy trình biên dịch 4 lớp (`pdflatex` -> `bibtex` -> `pdflatex` -> `pdflatex`).

## Progress & Changelog
**Các Tác Vụ Gần Đây (Compacted):**
- **Hoàn thành Task 5 & 6:** Hoàn tất Section 6.4 và 6.5. Lập luận vật lý về "Trạm trung chuyển" của MG4 và Khẳng định CPU Time tối đa 91s. Hệ thống giá trị $\lambda$ thị trường nội bộ.
- **[QUAN TRỌNG] Hoàn tất Deep Logic Audit (Red Teaming) cho Section 6.1-6.5:** Pass 100%.
- **Hoàn thành Task 1 & 2 (Phase 1: Robustness & Sensitivity Analysis):** 
  - Khởi tạo Section 6.6. Giới thiệu Ma trận Stress 3 chiều (Temporal, Spatial, Spatiotemporal) thông qua 4 kịch bản lỗi: 2-MG Short/Long và 3-MG Short/Long.
  - Đã mapping chính xác **2-MG Short Fault** là **Current Method** (Baseline) phân tích ở các mục 6.2-6.5.
  - Phân tích Level 1 (Temporal Depth): MPC sống sót qua đợt đứt lưới 11 tiếng hoàn toàn dựa trên "khả năng phản xạ thời gian thực" (định tuyến P2P cực đại, tích trữ pin và cắt tải thường), loại bỏ triệt để lập luận sai về "khả năng tiên tri".
- **[QUAN TRỌNG] Tái cấu trúc Section 6.6:** Theo lệnh Tư lệnh, hủy bỏ cấu trúc phân tích theo kịch bản lỗi (Level 1, 2, 3). Chuyển sang mô hình **"Metric-Driven Slicing"**, tức là gộp cả 4 kịch bản lỗi vào phân tích đồng thời qua 3 Lăng kính Kỹ thuật: 6.6.1 (Active Power Routing), 6.6.2 (Voltage Stability), và 6.6.3 (Autonomous Critical Load Prioritization). Bằng chứng thép `Crit 0.0` được xác nhận trên biểu đồ.
- **Hoàn thành Task 2, 3, 4:** Hoàn tất 6.6.1 (Power Routing), 6.6.2 (Voltage Stability) và 6.6.3 (Critical Load Prioritization). Gọt sạch ngôn ngữ kịch tính, chứng minh sắc bén sự sụt áp I*Z và sự kiện ghim chặt Hard Cap 0.90 p.u, làm tiền đề buộc hệ thống phải sa thải tải thường ("Graceful Degradation").
- **[ĐỈNH CAO] Hoàn tất 4 vòng Blind Independent Audit cho Section 6.6:**
  - Tiêu diệt triệt để toàn bộ hạt sạn nhân hóa ("Fluff").
  - Sửa chuẩn xác các lỗi thuật ngữ toán học AC-OPF ("hard cap" thành "lower bound").
  - Khóa chặt luận điểm "fully exhaust normal load" bằng giới hạn cục bộ "locally available", bít hoàn toàn kẽ hở phản biện về đặc tính của AC-OPF so với DC-OPF.
- **Dự án Hoàn tất:** Toàn bộ Section 6.6 (Robustness & Sensitivity Analysis) đã đạt chuẩn mực học thuật sắc lạnh nhất của IEEE. Khối bê tông logic AC-OPF nguyên khối đã thành hình.

## Key Decisions
1. **Kiến trúc Top-Down (Chapter 6):** Sử dụng `Transfer folder/Result_data/report_result` để viết kết quả.
2. **Quy tắc Đơn vị:** Dữ liệu Pyomo chuẩn hóa `S_base = 1MVA` -> 1 pu = 1 MWh/MW.
3. **Nâng cấp Radar Kiểm duyệt:** Skill `deep-logic-audit` giờ đây là tiêu chuẩn vàng để ép buộc phân tích phải có nền tảng Toán học/Vật lý (Ví dụ: Định luật KKT, $I^2X$).
4. **Xóa bỏ mâu thuẫn thuật toán MPC:** Khẳng định tuyệt đối MPC là thuật toán mù tương lai (rolling horizon), mọi luận điểm liên quan đến "dự đoán" được thay thế bằng "Adaptive Routing".
5. **Dynamic Binding Constraint Pivot:** Giải thích hiện tượng sụt áp ít/cắt tải nhiều của AC-OPF bằng sự chuyển dịch mượt mà giữa Network Constraints và Generation Limits mà không cần If/Else heuristics.

## Next Steps
- DỰ ÁN ĐÃ HOÀN TẤT. Yêu cầu Tư lệnh phê duyệt tổng thể (Lệnh Compile PDF).
- Thực thi quy trình dọn dẹp hệ thống (Kill Subagents, dọn dẹp tmp/workspace nếu cần).

## Critical Context
**Cấu hình mạng (Topology P2P):** 1 Utility Grid & 4 Microgrids.
- **MG1 (Nặng tải, 36 nodes):** Gã khổng lồ xuất khẩu (Surplus Island). Liên kết MG4, MG3.
- **MG2 (Solar-only, 30 nodes):** Hố đen (Massive Sink) khi mất PV.
- **MG3 (Nhẹ tải/Dư thừa, 21 nodes):** Cứu tinh xuất khẩu. Liên kết MG1, MG2, MG4.
- **MG4 (Nặng tải & Nhiều PV, 35 nodes):** Trạm trung chuyển (Transit Corridor) chịu phạt tổn hao $I^2X$.

## Folder Structure Summary
- **Tài liệu đặc tả và Memory**: `agy-memory/`, `workspace/`
- **Dữ liệu nguồn và Thuật toán**: `Transfer folder/` (`main.py`, `build_model.py`, `Result_data/`)

## Asset Pointers
- `D:\Latex\DATN\workspace\Idea.md`
- `D:\Latex\DATN\workspace\ACTION_PLAN.md`
- `D:\Latex\DATN\chapters\chapter6.tex`
- `D:\Latex\DATN\.agents\skills\deep-logic-audit\SKILL.md`
