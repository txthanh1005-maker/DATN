# Implementation Plan: Tái thiết Mặt tiền (Front-matter Overhaul) & Tổng kết Luận văn

## Overview
Chiến dịch cuối cùng nhằm đồng bộ hóa toàn bộ các phần râu ria của Luận văn (Title, Abstract, Introduction) với thuật toán cốt lõi thực tế đang chạy ở các Chương 4, 5, 6 là **MPC (Model Predictive Control)** và **ATC (Analytical Target Cascading)** thay vì ADMM như dự định ban đầu. Đồng thời, hoàn thiện nốt Chương 7 (Conclusion).

## Architecture Decisions
- Xóa bỏ hoàn toàn "ADMM" khỏi Title, Abstract và các phần mở đầu.
- **Motivation mới:** Mở rộng bài toán từ "tối ưu hóa phân tán thông thường" sang "điều phối không gian-thời gian (spatio-temporal) dưới điều kiện thiếu hụt tầm nhìn (limited foresight) và giới hạn vật lý của lưới phân phối". 
- **Keywords chủ đạo mới:** *Model Predictive Control (MPC), Analytical Target Cascading (ATC), Rolling Horizon, Graceful Degradation, Negative Resilience Premium.*

## Task List

### Phase 1: Front-matter Overhaul
- **Task 0: Kiểm kê Luận điểm và Trích dẫn (Citation Matrix Extraction)**
  - **Trạng thái:** `[x] DONE`
  - **Người thực hiện:** Tư lệnh / CEO
  - **Mô tả:** Đọc quét file `chapter2.tex` cũ, chắt lọc các luận điểm logic và các khối trích dẫn `\cite{}` có giá trị để ánh xạ vào cấu trúc mới. Đã tạo file `workspace/Citation_Matrix.md` làm tài nguyên cho người viết.

- **Task 1: Cập nhật Tên Đề tài (Title)**
  - **Trạng thái:** `[x] DONE`
  - **Người thực hiện:** Tư lệnh / CEO
  - **Mô tả:** Đã cập nhật `DATN.tex` thành: *"A Fault-Adaptive Peer-to-Peer Energy Trading Framework for Enhancing Multi-Microgrid Resilience via ATC and MPC"*.

- **Task 2.1: Viết Section 1.1 (Macro View)**
  - **Trạng thái:** `[x] DONE`
  - **Người thực hiện:** Sĩ quan Tác chiến (LaTeX Writer) + Domain Reviewer
  - **Mô tả:** Viết đoạn giới thiệu (1-2 trang) về bối cảnh lưới điện phân tán, Microgrid, BESS. Nhấn mạnh sự lỗi thời của FIT và vai trò của P2P. Chốt hạ bằng việc bẻ lái sang Resilience (Extreme Events) để dọn đường cho MPC. Đã trích dẫn đủ các bài báo nền tảng.

- **Task 2.2: Viết Section 1.2 (The Physical Layer - Power Flow & Constraints)**
  - **Trạng thái:** `[x] DONE`
  - **Người thực hiện:** `@latex_writer`
  - **Mô tả:** Viết đánh giá các mô hình lưới. Lật đổ Lumped Node và DC-OPF/LinDistFlow do sai số P-Q-V ở lưới R/X cao. Tôn vinh SOCP là công cụ bắt buộc để đồng bộ dòng tiền P2P và an toàn điện áp, đặc biệt khi cắt lưới (Islanding). Nhấn mạnh: Không giao dịch Q.

- **Task 2.3: Viết Section 1.3 (The Spatial Layer - Decentralization & Privacy)**
  - **Trạng thái:** `[x] DONE`
  - **Người thực hiện:** `@latex_writer`
  - **Mô tả:** Phân tích điểm yếu của ADMM ở cấu trúc phân cấp (Hierarchical) khi giải SOCP. Khẳng định sức mạnh của ATC trong việc bảo mật dữ liệu và tự động sinh giá bóng (DLMP) chặt chẽ bằng toán học.

- **Task 2.4: Viết Section 1.4 (The Temporal Layer - Dynamics & Grid Resilience)**
  - **Trạng thái:** `[x] DONE`
  - **Người thực hiện:** `@latex_writer`
  - **Mô tả:** Phá hủy mô hình tĩnh (Static Day-ahead) trước các sự kiện "Thiên nga đen". Đưa cơ chế Rolling Horizon của MPC vào. Trình bày rào cản tính toán (Tractability) và khái niệm "Dynamic Value of Lost Load (VoLL)" / Graceful Degradation để bảo vệ Critical Load.

- **Task 2.5: Viết Section 1.5 (Research Gap, Motivation & Objectives)**
  - **Trạng thái:** `[x] DONE`
  - **Người thực hiện:** `@latex_writer`
  - **Mô tả:** Chốt lại Master Gap: Thiếu mô hình thống nhất kết hợp SOCP-ATC-MPC. Đề ra 4 Mục tiêu nghiên cứu (Objectives) để giải quyết lỗ hổng này. Mọi thuật ngữ ADMM cũ phải được xóa sạch.

### Phase 2: Project Conclusion
- **Task 3: Viết Chapter 7 (Conclusion & Future Work)**
  - **Trạng thái:** `[x] DONE`
  - **Người thực hiện:** `@latex_writer`
  - **Mô tả:** Viết nội dung Chapter 7 trực tiếp vào file `DATN.tex`. Tuân thủ tuyệt đối 4 Trụ cột Conclusion (Algorithmic Architecture, Physical Resilience, Tie-line Congestion Paradox, Graceful Degradation) và 3 Hướng Future Work (RL/Stochastic MPC, Hardware/STATCOM, Dynamic Switch Control) đã chốt tại `Idea.md`. Không dùng từ ngữ sáo rỗng.

- **Task 4: Viết lại Abstract (Tóm tắt)**
  - **Trạng thái:** `[x] DONE`
  - **Người thực hiện:** `@latex_writer`
  - **Mô tả:** Viết nội dung Abstract trực tiếp vào file `DATN.tex` (khoảng dòng 210). Bám sát Spec trong `Idea.md`: Nêu bật SOCP/ATC/MPC, 100% Critical Load, Negative Premium, Tie-line/Voltage Paradox. Viết bằng tiếng Anh học thuật chuẩn IEEE (250-300 từ).

### Phase 3: Final Polish & Formatting
- **Task 5: Đẩy lùi số thứ tự các Chương (Shift Chapters Up) [ƯU TIÊN 1]**
  - **Trạng thái:** `[x] DONE`
  - **Người thực hiện:** `@code_generator` / `@latex_writer`
  - **Mô tả:** Do Chương 2 đã bị lược bỏ, cần đổi tên file và cập nhật `\input{}` trong `DATN.tex` để đẩy Chương 3 thành 2, Chương 4 thành 3, v.v. Sửa toàn bộ đánh số (ví dụ từ Chapter 7 thành Chapter 6).
- **Task 6: Truy quét và điền các vị trí "xx" (Fill Placeholders)**
  - **Trạng thái:** `[x] DONE`
  - **Người thực hiện:** `@latex_writer`
  - **Mô tả:** Tìm toàn bộ chuỗi "xx" trong các file `.tex` và điền số liệu/text/trích dẫn chính xác.
- **Task 7: Rà soát căn lề biến số và công thức toán học**
  - **Trạng thái:** `[ ] TODO`
  - **Người thực hiện:** `@domain_reviewer` / `@latex_writer`
  - **Mô tả:** Đảm bảo mọi phương trình SOCP, ATC, MPC đúng format. Kiểm tra tính đồng nhất của các biến số ($I^2X$, $\lambda$, $P_{tie}$).
- **Task 8: Quy chuẩn lại các phần viết tắt (Abbreviations)**
  - **Trạng thái:** `[>] IMPLEMENTING`
  - **Người thực hiện:** `@latex_writer`
  - **Mô tả:** Cập nhật List of Abbreviations trong file danh mục. Quan trọng: Lọc và xóa toàn bộ các cụm từ đang viết dư thừa dưới dạng `Full word (Abbreviation)` (ví dụ: Analytical Target Cascading (ATC), Model Predictive Control (MPC), v.v.) trong các chương và chuyển đổi 100% về dạng viết tắt `Abbreviation`, đảm bảo tính thống nhất.
- **Task 9: Bổ sung Lưu đồ Thuật toán (Algorithm Flowcharts)**
  - **Trạng thái:** `[ ] TODO`
  - **Người thực hiện:** `@latex_writer`
  - **Mô tả:** Thêm sơ đồ minh họa cho cấu trúc 3-Mode State Machine và kiến trúc ATC-MPC.
- **Task 10: Chèn thêm hình minh họa (Illustrative Figures) & Dàn trang**
  - **Trạng thái:** `[ ] TODO`
  - **Người thực hiện:** `@latex_writer`
  - **Mô tả:** Nhúng các hình minh họa phụ trợ. Thực hiện cuối cùng để tránh vỡ float/layout.

### Phase 4: Project Closure
- **Task 11: Final Review & Publications**
  - **Trạng thái:** `[ ] TODO`
  - **Người thực hiện:** Tư lệnh
  - **Mô tả:** Tư lệnh tự điền danh sách các bài báo khoa học đã đăng (hoặc comment/xóa nếu chưa có). Cập nhật Ngày/Tháng ở trang bìa. Chạy lệnh Compile cuối cùng để ra file PDF hoàn chỉnh.

### Checkpoint: Ready for Defense
- [ ] Mọi dấu vết của "ADMM" đã bị xóa sạch khỏi mặt tiền.
- [ ] Tư lệnh đã verify bản PDF cuối cùng và sẵn sàng nộp cho Hội đồng.
