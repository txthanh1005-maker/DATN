## Goal
Nâng cấp và chuyển đổi toàn bộ báo cáo Đồ án Tốt nghiệp (DATN) từ thuật toán ADMM cũ sang kiến trúc mới: **Analytical Target Cascading (ATC) & Model Predictive Control (MPC)**. Quản lý toàn bộ vòng đời tác chiến thông qua "Supreme Source of Truth" tại `agy-memory/SESSION_STATE.md`.

## Constraints
- Tuyệt đối tuân thủ kiến trúc hệ thống hiện tại: Hierarchical ATC, thuật toán MPC & SOCP.
- Không tự ý sửa đổi code lõi (`main.py`, `build_model.py`, v.v.), trừ khi có lỗi hoặc yêu cầu thêm kịch bản mới. `Transfer folder` là nguồn dữ liệu chuẩn.
- Mọi nhiệm vụ LaTeX phải tuân thủ nghiêm ngặt quy trình biên dịch 4 lớp (`pdflatex` -> `bibtex` -> `pdflatex` -> `pdflatex`).

## Progress & Changelog
**Các Tác Vụ Gần Đây (Compacted):**
- **Tiến vào Giai đoạn Phase 3 (Final Polish & Formatting):**
  - **Hoàn thành Task 5:** Đã gỡ bỏ Chapter 2 cũ, đổi tên và đẩy lùi số thứ tự các chương (3->2, 4->3, 5->4, 6->5, 7->6) và kết dính lại file `DATN.tex`.
  - **Hoàn thành Task 6:** Điền thành công thông tin cá nhân (MSSV 20222744, Class K67, Email) vào Declaration of Originality.
- **Hoàn thành Task 4 (Viết lại Abstract):** Đã nén toàn bộ luận văn thành 264 từ tiếng Anh chuẩn IEEE cực mạnh.
- **Hoàn thành Task 3 (Chapter 7 - Conclusion & Future Work):** Tổng hợp xuất sắc 4 Trụ cột học thuật và 3 Hướng Future Work. Đã pass 2 vòng Red Teaming.
- **Hoàn thành Chapter 1 & 6:** Đã xử lý triệt để, xóa trích dẫn ảo giác, vá lỗ hổng toán học và chốt hạ AC-OPF.

## Key Decisions
1. **Kiến trúc Top-Down (Chapter 6):** Sử dụng `Transfer folder/Result_data/report_result` để viết kết quả.
2. **Quy tắc Đơn vị:** Dữ liệu Pyomo chuẩn hóa `S_base = 1MVA` -> 1 pu = 1 MWh/MW.
3. **Nâng cấp Radar Kiểm duyệt:** Skill `deep-logic-audit` giờ đây là tiêu chuẩn vàng để ép buộc phân tích phải có nền tảng Toán học/Vật lý (Ví dụ: Định luật KKT, $I^2X$).
4. **Hủy diệt "Trading Q":** Tuyệt đối không cho P2P mua bán công suất phản kháng. Q chỉ phục vụ "Local Support".
5. **Bẻ lái sang Resilience:** Trong bối cảnh Extreme Events, hệ thống không chỉ tìm kiếm cực tiểu chi phí (FIT/P2P thông thường) mà còn đóng vai trò "Safety Net".
6. **Citation Granularity:** Ép buộc băm nhỏ trích dẫn (Tối đa 2 bài/câu), đâm thẳng vào luận điểm kỹ thuật, cắt bỏ ngôn từ "fluff" và "hyperbole" theo tiêu chuẩn IEEE.
7. **Anti-Hallucination Protocol:** Kích hoạt xác thực OpenAlex để thanh trừng mọi bài báo ảo giác. Không nhân nhượng với hàng giả.
8. **Defense Matrix Integration:** Sử dụng toán học tuyệt đối (Radial topology, S_max inverter, Vertical vs Horizontal Consensus, Warm-start) thay thế cho các ngôn từ so sánh sáo rỗng.

## Next Steps
- **Tiếp tục hoàn thiện Phase 3:**
  - **Task 7:** Rà soát căn lề biến số và công thức toán học.
  - **Task 8:** Quy chuẩn lại các phần viết tắt (Đã update List nhưng tạm lùi trạng thái về TODO theo lệnh Tư lệnh).
  - **Task 9 & 10:** Bổ sung Lưu đồ thuật toán và Hình minh họa.
- Bàn giao quyền biên dịch cuối cùng (Task 11) cho Tư lệnh.

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
