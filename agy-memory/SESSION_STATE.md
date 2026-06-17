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

## Key Decisions
1. **Kiến trúc Bottom-Up (Chapter 3 & 4):**
   - **Chapter 3 (Local & Spatial):** Đi từ các phương trình cơ bản AC-OPF, thiết lập SOCP Relaxation (Giải thích rạch ròi trạng thái Normal/Exact và Emergency/Inexact). Sau đó nâng lên bài toán phối hợp không gian ATC(h) với khung thời gian linh hoạt (24h hoặc 5h).
   - **Chapter 4 (Temporal):** Giới thiệu logic MPC. Trình bày cách quy trình 3 giai đoạn của MPC tích hợp thuật toán lõi ATC SOCP (ở Chapter 3) để xử lý các tình huống Emergency.
2. **Kiến trúc 5 Tầng Bài Báo (The Holy Trinity + Market Depth):** Cấu trúc mở rộng từ 4 lên 5 tầng. Bổ sung Tầng 5 tập trung sâu vào ranh giới thị trường: Biểu đồ Giá ATC ($\lambda$) minh họa tín hiệu thị trường P2P dưới áp lực đứt gãy kết nối.
3. **Quy tắc Đơn vị (Critical Unit Rule):** Dữ liệu Pyomo chuẩn hóa `S_base = 1MVA` -> 1 pu = 1 MWh/MW.
4. **Luận điểm "100% Critical Load Protected" & "Negative Premium":** Tiền phạt đền bù cắt tải MPC trung bình bằng đúng 100,000 cents/MWh (không có tải ưu tiên bị cắt).
5. **Quy chuẩn Code LaTeX:** Bắt buộc dùng môi trường `equation`/`subequations`. Quản lý trích dẫn tách bạch qua file `.bib`. Mọi code đều phải được kiểm duyệt toán học (domain_reviewer) chéo với `main.py`.
6. **Quản lý Thuật ngữ & Viết tắt:** Mọi từ viết tắt (Abbreviations) PHẢI được định nghĩa và lưu trữ tại `workspace/Abbreviations.md`. Bắt buộc chỉ dùng từ viết tắt từ sau khi định nghĩa.
7. **Kỷ luật Ký hiệu Toán học (Nomenclature Rule):** MỖI LẦN viết công thức toán học, BẮT BUỘC phải tham chiếu và tuân thủ 100% các ký hiệu đã chốt trong `workspace/Nomenclature.md`.
8. **Kế thừa Section 3.3:** Section 3.4 sẽ KHÔNG viết lại các ràng buộc linh kiện (DG, BESS, PV, WT) do đã được mô tả chi tiết ở Section 3.3.
9. **Technical Relaxations (Theo phản biện 17/06/2026):** $Q_{tie} = 0$ (không xuất khẩu Q). Các giới hạn cân bằng $P_{tie}$ toàn cục, ranh giới an toàn của BESS và Main Grid được kiểm soát linh hoạt qua hàm phạt trong thuật toán điều phối ATC thay vì dùng hard constraints ở mô hình Local SOCP.

## Next Steps
- Kích hoạt **Task 2.3.3 (Phối hợp Không gian với thuật toán ATC)**: Trình bày bài toán ATC để điều phối công suất P2P giữa các MG. Xây dựng phương trình của Coordinator và Local MGs.

## Critical Context
**Cấu hình mạng (Topology P2P):** 1 Main Grid (MG0) & 4 Microgrids.
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
- `D:\Latex\DATN\chapters\chapter3.tex`
