## Goal
Nâng cấp và chuyển đổi toàn bộ báo cáo Đồ án Tốt nghiệp (DATN) từ thuật toán ADMM cũ sang kiến trúc mới: **Analytical Target Cascading (ATC) & Model Predictive Control (MPC)**. Quản lý toàn bộ vòng đời tác chiến thông qua "Supreme Source of Truth" tại `agy-memory/SESSION_STATE.md`.

## Constraints
- Tuyệt đối tuân thủ kiến trúc hệ thống hiện tại: Hierarchical ATC, thuật toán MPC & SOCP.
- Không tự ý sửa đổi code lõi (`main.py`, `build_model.py`, v.v.), trừ khi có lỗi hoặc yêu cầu thêm kịch bản mới. `Transfer folder` là nguồn dữ liệu chuẩn.
- Mọi nhiệm vụ LaTeX phải tuân thủ nghiêm ngặt quy trình biên dịch 4 lớp (`pdflatex` -> `bibtex` -> `pdflatex` -> `pdflatex`).

## Progress & Changelog
**Các Tác Vụ Gần Đây (Compacted):**
- **Academic Citation Search (Task 9):** Tác nhân Trinh sát (Researcher) đã dò tìm thành công các bài báo chất lượng cao (2023-2025) từ IEEE và ScienceDirect. Tư lệnh đã trực tiếp phê duyệt và đưa vào các phương trình: SOCP (Chapter 2), ATC (Chapter 3), MPC (Chapter 4). Task 9 hoàn tất.
- **Citation Matrix Algorithm (Task 9.1):** Lên ý tưởng/Tư duy biểu diễn Citation Matrix dưới dạng Lưu đồ Thuật toán (Algorithm Block) theo 3 lăng kính (Physical, Spatial, Temporal). Đã code demo nhưng quyết định Rollback về commit `11efb19` để chờ ý kiến duyệt chính thức từ Thầy hướng dẫn (Supervisor) nhằm đảm bảo an toàn.
- **Format Audit (Task 7):** Đã sửa lỗi tràn lề `Overfull \hbox` và lệch hàng tại các hệ phương trình DistFlow, ATC, AC-OPF trong Chapter 2 và 3. Tối ưu hóa Inline math.
- **Chỉnh sửa Phần Kết quả Chapter 5 (Task 10.5):** Cập nhật Hình 5.5, 5.6 và 5.9. Thay thế văn bản Base Fault thành chuẩn IEEE (nhấn mạnh sự cách ly $P_{tie}=0$).
- **Algorithm Flowcharts & Timeline (Task 9 & 9.5):** Hoàn thành vẽ Lưu đồ TikZ cho thuật toán 3-Mode State Machine và sơ đồ trục thời gian Rolling Horizon (MPC).
- **Academic Reviewer Panel (Task 11):** Triển khai đồng thời 5 tác nhân (EIC, Methodology, Domain, Perspective, DA) quét toàn bộ luận văn. Tổng hợp 30 báo cáo review thành `need_update.md` với quyết định "Minor Revision".

## Key Decisions
1. **Kiến trúc Top-Down (Chapter 6):** Sử dụng `Transfer folder/Result_data/report_result` để viết kết quả.
2. **Quy tắc Đơn vị:** Dữ liệu Pyomo chuẩn hóa `S_base = 1MVA` -> 1 pu = 1 MWh/MW.
3. **Nâng cấp Radar Kiểm duyệt:** Skill `deep-logic-audit` giờ đây là tiêu chuẩn vàng để ép buộc phân tích phải có nền tảng Toán học/Vật lý.
4. **Hủy diệt "Trading Q":** Tuyệt đối không cho P2P mua bán công suất phản kháng. Q chỉ phục vụ "Local Support".
5. **Bẻ lái sang Resilience:** Trong bối cảnh Extreme Events, hệ thống không chỉ tìm kiếm cực tiểu chi phí (FIT/P2P thông thường) mà còn đóng vai trò "Safety Net".
6. **ATC Multiplier Standards:** Chốt sử dụng chuẩn $\lambda, \rho$ thay cho $\alpha, \beta$ cho biến phạt tuyến tính và bậc hai.
7. **Terminological Precision:** Sử dụng thuật ngữ "Distributed" thay vì "Decentralized" cho hệ thống điều khiển có giao tiếp qua Coordinator (DSO), tránh vi phạm tiêu chuẩn nghiêm ngặt của giới hàn lâm.

## Next Steps
- Quét các ảnh độ phân giải thấp và yêu cầu render lại theo DPI chuẩn (Task 4).
- Cập nhật thuật ngữ tên lỗi (Task 6) và viết Conclusion/Discussion cho các chương (Task 7 & 8).
- Tiến hành biên dịch thử nghiệm bản PDF mới nhất.

## Critical Context
**Cấu hình mạng (Topology P2P):** 1 Utility Grid & 4 Microgrids.
- **MG1 (Nặng tải, 36 nodes):** Gã khổng lồ xuất khẩu (Surplus Island). Liên kết MG4, MG3.
- **MG2 (Solar-only, 30 nodes):** Hố đen (Massive Sink) khi mất PV.
- **MG3 (Nhẹ tải/Dư thừa, 21 nodes):** Cứu tinh xuất khẩu. Liên kết MG1, MG2, MG4.
- **MG4 (Nặng tải & Nhiều PV, 35 nodes):** Trạm trung chuyển (Transit Corridor) chịu phạt tổn hao $I^2X$.

## Folder Structure Summary
- **Tài liệu đặc tả và Memory**: `agy-memory/`, `workspace/`
- **Dữ liệu nguồn và Thuật toán**: `Transfer folder/` (`main.py`, `build_model.py`, `Result_data/`)
- **Ảnh minh họa (Visualizations)**: `chapters/Imagine/`

## Asset Pointers
- `D:\Latex\DATN\workspace\Idea.md`
- `D:\Latex\DATN\workspace\ACTION_PLAN.md`
- `D:\Latex\DATN\chapters\chapter1.tex`
- `D:\Latex\DATN\chapters\chapter2.tex`
- `D:\Latex\DATN\chapters\chapter3.tex`
- `D:\Latex\DATN\chapters\chapter4.tex`
- `D:\Latex\DATN\chapters\chapter5.tex`
- `D:\Latex\DATN\chapters\Imagine\ATC_Evolution.tex`
- `D:\Latex\DATN\need_update.md`
