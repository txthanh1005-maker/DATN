## Goal
Nâng cấp và chuyển đổi toàn bộ báo cáo Đồ án Tốt nghiệp (DATN) từ thuật toán ADMM cũ sang kiến trúc mới: **Analytical Target Cascading (ATC) & Model Predictive Control (MPC)**. Quản lý toàn bộ vòng đời tác chiến thông qua "Supreme Source of Truth" tại `agy-memory/SESSION_STATE.md`.

## Constraints
- Tuyệt đối tuân thủ kiến trúc hệ thống hiện tại: Hierarchical ATC, thuật toán MPC & SOCP.
- Không tự ý sửa đổi code lõi (`main.py`, `build_model.py`, v.v.), trừ khi có lỗi hoặc yêu cầu thêm kịch bản mới. `Transfer folder` là nguồn dữ liệu chuẩn.
- Mọi nhiệm vụ LaTeX phải tuân thủ nghiêm ngặt quy trình biên dịch 4 lớp (`pdflatex` -> `bibtex` -> `pdflatex` -> `pdflatex`).

## Progress & Changelog
**Các Tác Vụ Gần Đây (Compacted):**
- **Hoàn thiện Section 3.4 & 3.6 (AC-OPF & Final Formulation):** Tái cấu trúc thành công mô hình toán học Local SOCP. Đã rẽ nhánh rõ ràng thành 2 dạng thức: Formulation I (Normal Mode - tối ưu kinh tế) và Formulation II (Emergency Mode - tối ưu sinh tồn). 
- **Tổng quát hóa Mô hình Sự cố:** Áp dụng biến chỉ báo $\Gamma_E(t)$ và tập hợp lỗi $\Omega_{fault}$ để xử lý chung mọi tình huống đứt gãy thành phần (đứt lưới, sập nguồn, v.v.), thay vì giới hạn ở lỗi lưới chính. Tích hợp chặt chẽ cơ chế cắt tải (cả P và Q tỉ lệ thuận) và mở khóa dự phòng DG.
- **Hoàn thành Section 3.5 (SOCP Relaxation):** Trình bày quá trình lồi hóa SOCP và chứng minh tính Exactness vững chắc của mạng hình tia nhờ $F_{loss}$ và cơ chế PV Curtailment tự do.
- **Pivot Cấu trúc (Bottom-Up Approach):** Đã chuyển đổi phương pháp tiếp cận Chapter 3 và 4 (Local -> Spatial -> Temporal). Gộp thành công Section 3.2 và 3.3. Đã cập nhật `Idea.md`.
- **Review & Refine Chapter 3 (Local SOCP):** Đã qua kiểm duyệt (Passed) bởi Domain Reviewer và English Teacher. Chốt giả định vật lý (Q_tie=0, xử lý giới hạn bằng hàm phạt ở ATC) và tinh chỉnh văn phong học thuật khách quan.
- **Khởi tạo Chapter 4 (ATC) & Hoàn thành Task 3.4.1:** Đã trình bày tổng quan ATC và bài toán Coordinator. Khắc phục thành công 4 lỗi toán học (dấu $P_{sell}$, $\lambda$ update, Adaptive Residual Balancing cho $\rho$) theo Python codebase. Đã thống nhất danh pháp đổi MG0 thành Utility Grid.
- **Hoàn thành Task 3.4.2:** Đã viết Section 4.3 tích hợp hàm phạt ATC vào Local SOCP. Chốt quy tắc "Ánh xạ Không gian" (Spatial Mapping) trong Nomenclature.md: sử dụng biến $P_{tie,ij,t}$ để mô tả dòng điện định hướng, giải quyết hoàn toàn sự lệch pha giữa Toán học vô hướng và Lập trình Python (vốn chỉ định nghĩa `P_trade[node]`). Loại bỏ hoàn toàn chuẩn L2 sai lệch.
- **Hoàn thành Task 3.4.3 & Tái cấu trúc Section 4.2:** Trình bày thành công thuật toán lặp ATC tại Section 4.4. Đã phát hiện và tiêu diệt triệt để tàn dư toán học ADMM lỗi thời ở Section 4.2. Đồng bộ hóa 100% định nghĩa Primal/Dual Residual giữa báo cáo LaTeX và logic code Python.
- **Nghiệm thu toàn diện Chapter 4 (Holistic Review):** Tiến hành đợt càn quét (Deep Fix) khắc phục 4 lỗi toán học (Global penalty sum, sai dấu lambda, lệch pha chỉ số k). Kiểm duyệt văn phong học thuật và biên dịch pdflatex (4 lớp) đạt 100% PASS. Đóng băng hoàn toàn Chapter 4 (Spatial Coordination).
## Key Decisions
1. **Kiến trúc Bottom-Up (Chapter 3, 4, 5):**
   - **Chapter 3 (Local Optimization):** Đi từ các phương trình cơ bản AC-OPF, thiết lập SOCP Relaxation (Giải thích rạch ròi trạng thái Normal/Exact và Emergency/Inexact).
   - **Chapter 4 (Spatial Coordination):** Tách riêng bài toán phối hợp không gian ATC(h) với khung thời gian linh hoạt (24h hoặc 5h) thành một chương độc lập.
   - **Chapter 5 (Temporal Coordination):** Giới thiệu logic MPC. Trình bày cách quy trình 3 giai đoạn của MPC tích hợp thuật toán lõi ATC SOCP (ở Chapter 4) để xử lý các tình huống Emergency.
2. **Kiến trúc 5 Tầng Bài Báo (The Holy Trinity + Market Depth):** Cấu trúc mở rộng từ 4 lên 5 tầng. Bổ sung Tầng 5 tập trung sâu vào ranh giới thị trường: Biểu đồ Giá ATC ($\lambda$) minh họa tín hiệu thị trường P2P dưới áp lực đứt gãy kết nối.
3. **Quy tắc Đơn vị (Critical Unit Rule):** Dữ liệu Pyomo chuẩn hóa `S_base = 1MVA` -> 1 pu = 1 MWh/MW.
4. **Luận điểm "100% Critical Load Protected" & "Negative Premium":** Tiền phạt đền bù cắt tải MPC trung bình bằng đúng 100,000 cents/MWh (không có tải ưu tiên bị cắt).
5. **Quy chuẩn Code LaTeX:** Bắt buộc dùng môi trường `equation`/`subequations`. Quản lý trích dẫn tách bạch qua file `.bib`. Mọi code đều phải được kiểm duyệt toán học (domain_reviewer) chéo với `main.py`.
6. **Quản lý Thuật ngữ & Viết tắt:** Mọi từ viết tắt (Abbreviations) PHẢI được định nghĩa và lưu trữ tại `workspace/Abbreviations.md`. Bắt buộc chỉ dùng từ viết tắt từ sau khi định nghĩa.
7. **Kỷ luật Ký hiệu Toán học (Nomenclature Rule):** MỖI LẦN viết công thức toán học, BẮT BUỘC phải tham chiếu và tuân thủ 100% các ký hiệu đã chốt trong `workspace/Nomenclature.md`.
8. **Kế thừa Section 3.3:** Section 3.4 sẽ KHÔNG viết lại các ràng buộc linh kiện (DG, BESS, PV, WT) do đã được mô tả chi tiết ở Section 3.3.
9. **Technical Relaxations (Theo phản biện 17/06/2026):** $Q_{tie} = 0$ (không xuất khẩu Q). Các giới hạn cân bằng $P_{tie}$ toàn cục, ranh giới an toàn của BESS và Main Grid được kiểm soát linh hoạt qua hàm phạt trong thuật toán điều phối ATC thay vì dùng hard constraints ở mô hình Local SOCP.

## Next Steps
- Chuyển sang **Phase 4 (Temporal Coordination - Chapter 5)**.
- Kích hoạt **Task 4.5.1 (Write Section 5.1 - Khung thời gian MPC)**: Trình bày logic cuộn thời gian (Rolling Horizon) của MPC qua 3 giai đoạn (Day-ahead, Intraday, Real-time) và cách cập nhật trạng thái (SOC, dự báo).

## Critical Context
**Cấu hình mạng (Topology P2P):** 1 Utility Grid & 4 Microgrids.
- **MG1 (Nặng tải, 36 nodes):** Liên kết MG4, MG3.
- **MG2 (Solar-only, 30 nodes):** Liên kết MG3, MG4.
- **MG3 (Nhẹ tải/Dư thừa, 21 nodes):** Cứu tinh. Liên kết MG1, MG2, MG4.
- **MG4 (Nặng tải & Nhiều PV, 35 nodes):** Lưới phức hợp với biên độ dao động công suất mạnh. Liên kết với MG1, MG2, MG3.
**Cơ chế hoạt động kép:**
- *Day-ahead Scheduling:* Tối ưu hóa lợi ích kinh tế (24h).
- *Emergency MPC:* Chạy cuốn (rolling horizon) khung 5 giờ, kích hoạt cơ chế cách ly lỗi (N-2), bù phản kháng, và chia sẻ P2P.

## Folder Structure Summary
- **Tài liệu đặc tả và Memory**: `agy-memory/`, `workspace/`
- **Dữ liệu nguồn và Thuật toán**: `Transfer folder/` (`main.py`, `build_model.py`, `Result_data/`)

## Asset Pointers
- `D:\Latex\DATN\workspace\Idea.md`
- `D:\Latex\DATN\workspace\ACTION_PLAN.md`
- `D:\Latex\DATN\workspace\Abbreviations.md`
- `D:\Latex\DATN\workspace\Nomenclature.md`
- `D:\Latex\DATN\Transfer folder\System_Architecture_and_Data.md`
- `D:\Latex\DATN\chapters\chapter4.tex`
