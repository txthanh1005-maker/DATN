## Goal
Nâng cấp và chuyển đổi toàn bộ báo cáo Đồ án Tốt nghiệp (DATN) từ thuật toán ADMM cũ sang kiến trúc mới: **Analytical Target Cascading (ATC) & Model Predictive Control (MPC)**. Quản lý toàn bộ vòng đời tác chiến thông qua "Supreme Source of Truth" tại `agy-memory/SESSION_STATE.md`.

## Constraints
- Tuyệt đối tuân thủ kiến trúc hệ thống hiện tại: Hierarchical ATC, thuật toán MPC & SOCP.
- Không tự ý sửa đổi code lõi (`main.py`, `build_model.py`, v.v.), trừ khi có lỗi hoặc yêu cầu thêm kịch bản mới. `Transfer folder` là nguồn dữ liệu chuẩn.
- Mọi nhiệm vụ LaTeX phải tuân thủ nghiêm ngặt quy trình biên dịch 4 lớp (`pdflatex` -> `bibtex` -> `pdflatex` -> `pdflatex`).

## Progress & Changelog
**Các Tác Vụ Gần Đây (Compacted):**
- **Thesis Review Bug Fixes (HUST Examiner Simulation):** Hoàn thành 100% Kế hoạch tác chiến 6 mục tiêu. Sửa các lỗi nguy hiểm bao gồm: Thuật ngữ SOCP thành ACP, tham chiếu chéo "Chapter 3" thay vì "Chapter 4", thêm `\resizebox` chống tràn lề TikZ, sửa lỗi chính tả tên file ảnh, và làm rõ ranh giới điện áp Normal (0.95 p.u.) vs Emergency (0.90 p.u.).
- **Alignment with Thesis Assignment:** Bổ sung xuất sắc phần đối chiếu mục tiêu ở Chapter 6, chứng minh mạch lạc ĐATN đã đạt 100% 5 mục tiêu nghiên cứu (Review literature, Architecture, ATC, MPC, Simulation).
- **Hallucination Detection:** Bắt được 2 lỗi ảo giác của Reviewer Subagent (N-01 và N-03) qua việc cross-check trực tiếp với mã nguồn.
- Tất cả các nhiệm vụ trong `ACTION_PLAN.md` đã được đánh dấu `[x] DONE` và Luận văn đã sạch lỗi logic để ra Hội đồng.

## Key Decisions
1. **Kiến trúc Top-Down (Chapter 6):** Sử dụng `Transfer folder/Result_data/report_result` để viết kết quả.
2. **Quy tắc Đơn vị:** Dữ liệu Pyomo chuẩn hóa `S_base = 1MVA` -> 1 pu = 1 MWh/MW.
3. **Nâng cấp Radar Kiểm duyệt:** Skill `deep-logic-audit` giờ đây là tiêu chuẩn vàng để ép buộc phân tích phải có nền tảng Toán học/Vật lý.
4. **Hủy diệt "Trading Q":** Tuyệt đối không cho P2P mua bán công suất phản kháng. Q chỉ phục vụ "Local Support".
5. **Bẻ lái sang Resilience:** Trong bối cảnh Extreme Events, hệ thống không chỉ tìm kiếm cực tiểu chi phí (FIT/P2P thông thường) mà còn đóng vai trò "Safety Net".
6. **Terminological Precision:** Sử dụng thuật ngữ "Distributed, Dynamic, Multi-period" thay vì "Spatial, Temporal", tránh vi phạm tiêu chuẩn nghiêm ngặt của giới hàn lâm.

## Next Steps
- Toàn bộ Action Plan từ đợt Review đã hoàn tất 100%. 
- Tiến hành chạy Fast Build `pdflatex -> bibtex -> pdflatex*2` để ra file PDF hoàn chỉnh.
- Đề xuất dọn dẹp các file cache trung gian. Đợi lệnh nộp quyển từ Tư lệnh!
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
- `D:\Latex\DATN\mass_replace.py`
