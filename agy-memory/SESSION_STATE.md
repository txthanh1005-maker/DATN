## Goal
Nâng cấp và chuyển đổi toàn bộ báo cáo Đồ án Tốt nghiệp (DATN) từ thuật toán ADMM cũ sang kiến trúc mới: **Analytical Target Cascading (ATC) & Model Predictive Control (MPC)**. Quản lý toàn bộ vòng đời tác chiến thông qua "Supreme Source of Truth" tại `agy-memory/SESSION_STATE.md`.

## Constraints
- Tuyệt đối tuân thủ kiến trúc hệ thống hiện tại: Hierarchical ATC, thuật toán MPC & SOCP.
- Không tự ý sửa đổi code lõi (`main.py`, `build_model.py`, v.v.), trừ khi có lỗi hoặc yêu cầu thêm kịch bản mới. `Transfer folder` là nguồn dữ liệu chuẩn.
- Mọi nhiệm vụ LaTeX phải tuân thủ nghiêm ngặt quy trình biên dịch 4 lớp (`pdflatex` -> `bibtex` -> `pdflatex` -> `pdflatex`).

## Progress & Changelog
**Các Tác Vụ Gần Đây (Compacted):**
- **Deep Logic & Redundancy Audit (Chapter 3 & 4):** Đã "gọt" lặp ý, sửa cấu trúc TikZ chữ U, và sắp xếp lại luồng logic theo nguyên tắc Nhân - Quả (cơ chế $N-2$ và hàm phạt $S_{SOC}$).
- **Deep Logic & Redundancy Audit (Chapter 5):** Đã thiết lập lại luồng logic của AC-OPF, tổn hao $I^2X$, và cạn kiệt $Q$. Nắn lại các đoạn chuyển tiếp mà không làm mất tính toàn vẹn đồ thị.
- **Deep Logic & Redundancy Audit (DATN.tex - Mở bài & Kết bài):** 
  - Khắc phục lỗi đảo ngược luồng logic vật lý ở Voltage Paradox và Future Work.
  - Xén gọt lặp ý (Redundancy) ở Conclusion để biến nó thành bản đúc kết uy lực thay vì nhắc lại cơ chế đã có ở Abstract. Loại bỏ triệt để từ ngữ sáo rỗng (Fluff).
- **Format Audit (Task 7):** Đã sửa lỗi tràn lề `Overfull \hbox` và lệch hàng (Misaligned) tại các hệ phương trình DistFlow, ATC, AC-OPF trong Chapter 2 và 3. Tối ưu hóa Inline math.
- **Chỉnh sửa Phần Kết quả Chapter 5 (Task 10.5):** Tư lệnh đã đích thân chỉ đạo "phẫu thuật" thành công các Hình 5.5, 5.6 và 5.9. Thay thế văn bản Base Fault thành chuẩn IEEE (nhấn mạnh sự cách ly $P_{tie}=0$), đính chính vai trò tối ưu hóa chi phí của BESS (so với máy phát bù Q), và nêu bật sự tương phản vận hành vật lý giữa MG2 (đủ Q) và MG4 (thiếu Q).
- **Task 9 (Algorithm Flowcharts):** Đã hoàn thành vẽ Lưu đồ TikZ cho thuật toán 3-Mode State Machine ở Chương 4. Đã sử dụng `latex_writer` để vẽ và `logic_flow_checker` để xác minh độ chính xác của các phân nhánh (Mode 1, 2, 3) và tham số Rolling Horizon.
- **Task 9.5 (MPC Rolling Horizon):** Đã hoàn thành vẽ sơ đồ trục thời gian (Timeline) thể hiện cơ chế Rolling Horizon của thuật toán MPC (Day-ahead vs Real-time). Đã kiểm chứng tính đồng bộ với mô hình Pyomo.
- **Trạng thái:** Đã HOÀN TẤT gần như toàn bộ kế hoạch. Chờ chèn các hình minh họa phụ trợ (Task 10) và nộp bài.

## Key Decisions
1. **Kiến trúc Top-Down (Chapter 6):** Sử dụng `Transfer folder/Result_data/report_result` để viết kết quả.
2. **Quy tắc Đơn vị:** Dữ liệu Pyomo chuẩn hóa `S_base = 1MVA` -> 1 pu = 1 MWh/MW.
3. **Nâng cấp Radar Kiểm duyệt:** Skill `deep-logic-audit` giờ đây là tiêu chuẩn vàng để ép buộc phân tích phải có nền tảng Toán học/Vật lý (Ví dụ: Định luật KKT, $I^2X$).
4. **Hủy diệt "Trading Q":** Tuyệt đối không cho P2P mua bán công suất phản kháng. Q chỉ phục vụ "Local Support".
5. **Bẻ lái sang Resilience:** Trong bối cảnh Extreme Events, hệ thống không chỉ tìm kiếm cực tiểu chi phí (FIT/P2P thông thường) mà còn đóng vai trò "Safety Net".
6. **Citation Granularity:** Ép buộc băm nhỏ trích dẫn (Tối đa 2 bài/câu), đâm thẳng vào luận điểm kỹ thuật, cắt bỏ ngôn từ "fluff".
7. **Anti-Hallucination Protocol:** Kích hoạt xác thực OpenAlex để thanh trừng mọi bài báo ảo giác.
8. **Defense Matrix Integration:** Sử dụng toán học tuyệt đối thay thế cho các ngôn từ so sánh sáo rỗng.
9. **Logic Flow & Redundancy Protocol:** Áp dụng quy tắc thép: "So What?" và "Ngữ cảnh -> Nguyên nhân Vật lý -> Hệ quả Vật lý -> Phản ứng Thuật toán".

## Next Steps
- **Khởi động lại Hình ảnh (Task 9.5 & 10):** Triển khai vẽ sơ đồ MPC Rolling Horizon (Task 9.5) trên trục thời gian, sau đó mới chèn các hình minh họa phụ trợ khác ở Chương 2 (Task 10).
- **Project Closure (Task 11):** Cập nhật danh sách Publications, thông tin trang bìa, và biên dịch lại PDF lần cuối.

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
- `D:\Latex\DATN\chapters\chapter3.tex`
- `D:\Latex\DATN\chapters\chapter4.tex`
- `D:\Latex\DATN\chapters\chapter6.tex`
- `D:\Latex\DATN\.agents\skills\deep-logic-audit\SKILL.md`
