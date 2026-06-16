## Goal
Nâng cấp và chuyển đổi toàn bộ báo cáo Đồ án Tốt nghiệp (DATN) từ thuật toán ADMM cũ sang kiến trúc mới: **Analytical Target Cascading (ATC) & Model Predictive Control (MPC)**. Quản lý toàn bộ vòng đời tác chiến thông qua "Supreme Source of Truth" tại `agy-memory/SESSION_STATE.md`.

## Constraints
- Tuyệt đối tuân thủ kiến trúc hệ thống hiện tại: Hierarchical ATC, thuật toán MPC & SOCP.
- Không tự ý sửa đổi code lõi (`main.py`, `build_model.py`, v.v.), trừ khi có lỗi hoặc yêu cầu thêm kịch bản mới. `Transfer folder` là nguồn dữ liệu chuẩn.
- Mọi nhiệm vụ LaTeX phải tuân thủ nghiêm ngặt quy trình biên dịch 4 lớp (`pdflatex` -> `bibtex` -> `pdflatex` -> `pdflatex`).

## Progress & Changelog
**Các Tác Vụ Gần Đây (Compacted):**
- **Khởi tạo .gitignore:** Đã tạo file `.gitignore` loại bỏ các file rác sinh ra trong quá trình biên dịch LaTeX, các file backup, và các tài liệu tham khảo nặng để chuẩn bị push GitHub.
- **Hoàn thành Master Plan (Idea.md & ACTION_PLAN.md):** Đã chốt cấu trúc báo cáo 3 Lớp (Chương 2, 3, 4) và cấu trúc Kết quả 5 Tầng (Chương 5). Lịch trình được phân rã chi tiết theo chiều dọc (Vertical Slicing) xuống tận cấp độ 1.2.1, 1.2.2.
- **Cập nhật Toplogy:** Cập nhật lại bản chất của MG4 thành lưới nặng tải và có nhiều điện mặt trời (thay vì làm máy phát dự phòng như trước).
- **(Historical) Phân tích Tầng 4 & 5:** Đã hoàn thiện đồ thị CPU, Residuals, Convergence, và Scarcity Pricing Lambda, chứng minh MPC đủ năng lực Real-Time (~91s).

## Key Decisions
1. **Kiến trúc 5 Tầng Bài Báo (The Holy Trinity + Market Depth):** Cấu trúc mở rộng từ 4 lên 5 tầng. Bổ sung Tầng 5 tập trung sâu vào ranh giới thị trường: Biểu đồ Giá ATC ($\lambda$) minh họa tín hiệu thị trường P2P dưới áp lực đứt gãy kết nối.
2. **Quy tắc Đơn vị (Critical Unit Rule):** Dữ liệu Pyomo chuẩn hóa `S_base = 1MVA` -> 1 pu = 1 MWh/MW.
3. **Luận điểm "100% Critical Load Protected" & "Negative Premium":** Tiền phạt đền bù cắt tải MPC trung bình bằng đúng 100,000 cents/MWh (không có tải ưu tiên bị cắt).
4. **Quy chuẩn Code LaTeX:** Bắt buộc dùng môi trường `equation`/`subequations`. Quản lý trích dẫn tách bạch qua file `.bib`. Mọi code đều phải được kiểm duyệt toán học (domain_reviewer) chéo với `main.py`.

## Next Steps
- Kích hoạt **Step 3 (Execution Delegation)**: Phái cử Sub-agent `@latex_writer` tiến hành **Task 1.2.1** (Viết cấu trúc mạng Topology 4-MGs cho Chương 2).
- Xác minh tính chính xác của bản draft Chương 2 với `System_Architecture_and_Data.md`.

## Critical Context
**Cấu hình mạng (Topology P2P):** 1 Main Grid (MG0) & 4 Microgrids.
- **MG1 (Nặng tải, 36 nodes):** Liên kết MG4, MG3.
- **MG2 (Solar-only, 30 nodes):** Liên kết MG3, MG4.
- **MG3 (Nhẹ tải/Dư thừa, 21 nodes):** Cứu tinh. Liên kết MG1, MG2, MG4.
- **MG4 (Nặng tải & Nhiều PV, 35 nodes):** Liên kết MG1, MG2, MG3. (Đã cập nhật).
**Cơ chế hoạt động kép:**
- *Day-ahead Scheduling:* Tối ưu hóa lợi ích kinh tế (24h).
- *Emergency MPC:* Chạy cuốn (rolling horizon) khung 5 giờ, kích hoạt cơ chế cách ly lỗi (N-2), bù phản kháng, và chia sẻ P2P.

## Folder Structure Summary
- **Tài liệu đặc tả và Memory**: `agy-memory/`, `workspace/`
- **Dữ liệu nguồn và Thuật toán**: `Transfer folder/` (`main.py`, `build_model.py`, `Result_data/`)

## Asset Pointers
- `D:\Latex\DATN\workspace\Idea.md`
- `D:\Latex\DATN\workspace\ACTION_PLAN.md`
- `D:\Latex\DATN\Transfer folder\System_Architecture_and_Data.md`
- `D:\Code\P2P_trading_withQV_MG1234\P2P_trading_withQV_MG1234\Result_data\report_result\stage_1\Analysis_Stage1_Report.md` (Historical)
- `D:\Code\P2P_trading_withQV_MG1234\P2P_trading_withQV_MG1234\Result_data\report_result\stage_2\Analysis_Stage2.md` (Historical)
- `D:\Code\P2P_trading_withQV_MG1234\P2P_trading_withQV_MG1234\Result_data\report_result\stage_3\Analysis_Stage3.md` (Historical)
- `D:\Code\P2P_trading_withQV_MG1234\P2P_trading_withQV_MG1234\Result_data\report_result\stage_4\Analysis_Stage4.md` (Historical)
- `D:\Code\P2P_trading_withQV_MG1234\P2P_trading_withQV_MG1234\Result_data\report_result\stage_5\Analysis_Stage5.md` (Historical)
