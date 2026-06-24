## Goal
Nâng cấp và chuyển đổi toàn bộ báo cáo Đồ án Tốt nghiệp (DATN) từ thuật toán ADMM cũ sang kiến trúc mới: **Analytical Target Cascading (ATC) & Model Predictive Control (MPC)**. Quản lý toàn bộ vòng đời tác chiến thông qua "Supreme Source of Truth" tại `agy-memory/SESSION_STATE.md`.

## Constraints
- Tuyệt đối tuân thủ kiến trúc hệ thống hiện tại: Hierarchical ATC, thuật toán MPC & SOCP.
- Không tự ý sửa đổi code lõi (`main.py`, `build_model.py`, v.v.), trừ khi có lỗi hoặc yêu cầu thêm kịch bản mới. `Transfer folder` là nguồn dữ liệu chuẩn.
- Mọi nhiệm vụ LaTeX phải tuân thủ nghiêm ngặt quy trình biên dịch 4 lớp (`pdflatex` -> `bibtex` -> `pdflatex` -> `pdflatex`).

## Progress & Changelog
**Các Tác Vụ Gần Đây (Compacted):**
- **Terminology Restructuring (Task 6):** Hoàn thành chuẩn hóa 100% tên kịch bản lỗi trong `chapter5.tex` (Base Fault $\rightarrow$ Islanded Fault, PF $\rightarrow$ Perfect Foresight, 2-MG/3-MG $\rightarrow$ Transient/Sustained/Cascading Fault). Đã tạo file hướng dẫn `image_label_fixes.md` cho Python và Reviewer Subagent đã xác nhận tất cả 10 ảnh đồ thị kết quả được xuất lại hoàn hảo, không còn nhãn cũ hay lỗi đè layout.
- **Deep Logic Audit & Surgical Fixes (Task 12):** Hoàn thành rà soát logic chuyên sâu 3 bước bằng `logic_flow_checker`. Triển khai "phẫu thuật thẩm mỹ" an toàn: bổ sung chứng minh thuật toán cho ADMM, cô đọng Fluff phần SO/RO, và thắt chặt nguyên nhân vật lý $N-2$ cho Mode 2 MPC (Chapter 1 & 4). Rút gọn tiêu đề Chapter 2 thành "System Architecture and Modeling" để chống tràn lề.
- **Academic Citation Search & Matrix (Task 9 & 9.1):** Trinh sát (Researcher) đã dò tìm và chèn trích dẫn toán học thành công vào các phương trình SOCP, ATC, MPC. Cập nhật Citation Matrix dạng Pseudo-code/Algorithm vào Chương 1.
- **Format Audit & Visualizations (Task 7 & 9.5):** Sửa lỗi tràn lề `Overfull \hbox`. Hoàn thành vẽ Lưu đồ TikZ cho thuật toán 3-Mode State Machine và sơ đồ trục thời gian Rolling Horizon (MPC). Tất cả ảnh phân giải thấp đã được cập nhật bản nét.

## Key Decisions
1. **Kiến trúc Top-Down (Chapter 6):** Sử dụng `Transfer folder/Result_data/report_result` để viết kết quả.
2. **Quy tắc Đơn vị:** Dữ liệu Pyomo chuẩn hóa `S_base = 1MVA` -> 1 pu = 1 MWh/MW.
3. **Nâng cấp Radar Kiểm duyệt:** Skill `deep-logic-audit` giờ đây là tiêu chuẩn vàng để ép buộc phân tích phải có nền tảng Toán học/Vật lý.
4. **Hủy diệt "Trading Q":** Tuyệt đối không cho P2P mua bán công suất phản kháng. Q chỉ phục vụ "Local Support".
5. **Bẻ lái sang Resilience:** Trong bối cảnh Extreme Events, hệ thống không chỉ tìm kiếm cực tiểu chi phí (FIT/P2P thông thường) mà còn đóng vai trò "Safety Net".
6. **Terminological Precision:** Sử dụng thuật ngữ "Distributed, Dynamic, Multi-period" thay vì "Spatial, Temporal", tránh vi phạm tiêu chuẩn nghiêm ngặt của giới hàn lâm (Electrical Engineering Context).

## Next Steps
- Củng cố lập luận (Task 7 & 8 - HIGH): Viết tiểu mục "Conclusion/Discussion" ở cuối *từng chương* (Chương 1, 2, 3, 4) và mở rộng "General Conclusion".
- Biên dịch PDF lần cuối để kiểm tra tổng thể.

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
