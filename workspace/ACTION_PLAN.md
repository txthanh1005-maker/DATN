# Implementation Plan: Bổ sung Stage 6 (Robustness & Sensitivity Analysis) vào Chapter 6

## Overview
Chiến dịch này nhằm bổ sung mục `6.6 Robustness & Sensitivity Analysis (The Stress Test Matrix)` vào cuối file `chapters/chapter6.tex`. Dựa trên yêu cầu cấu trúc lại của Tư lệnh sau khi đối chiếu 4 biểu đồ, chúng ta sẽ **không** chia theo Level (Temporal/Spatial). Thay vào đó, chúng ta sẽ **phân tích đồng thời cả 4 kịch bản lỗi xuyên suốt 3 Lăng kính Kỹ thuật (Metrics)**: Định tuyến công suất (P2P), Ổn định điện áp (Voltage), và Sự hy sinh kinh tế (Cost/Shedding). Mục tiêu tối thượng là chứng minh hệ thống MPC có thể tự động hy sinh Normal Load để giữ vững `0.0 MWh` Critical Load Shedding.

## Architecture Decisions
- **Metric-Driven Slicing:** Các tiểu mục (6.6.1 đến 6.6.3) được cấu trúc theo 3 chỉ số kỹ thuật thay vì theo cấu hình lỗi. Mỗi tiểu mục sẽ đối chiếu cả 4 cấu hình lỗi (2-MG Short/Long, 3-MG Short/Long) để thấy sự tịnh tiến của mức độ nghiêm trọng.
- **Ngôn ngữ:** Học thuật, sắc bén, tuân thủ tiêu chuẩn `deep-logic-audit`. Giải thích hiện tượng thông qua lăng kính Vật lý/Toán học (như giới hạn nhiệt Tie-line, độ sụt áp I*Z), tuyệt đối không đoán mò.

## Task List

### Phase 1: Mở đầu và Cấu trúc (Đã hoàn thành)
- **Task 1: Khởi tạo Section 6.6 và Intro**
  - **Trạng thái:** `[x] DONE`
  - **Mô tả:** Thêm tiêu đề mục 6.6 và định nghĩa rõ ràng 4 cấu hình Deficit MGs (2-MG/3-MG Short/Long). Đã chuẩn hóa thuật ngữ "Autonomous Critical Load Prioritization".

### Phase 2: Triển khai 3 Lăng kính Kỹ thuật (Metrics)
- **Task 2: Viết mục 6.6.1 (Active Power Routing & Network Endurance)**
  - **Trạng thái:** `[x] DONE`
  - **Người thực hiện:** `@latex_writer`
  - **Mô tả:** Xóa nội dung 6.6.1 cũ và viết lại. Nhúng hình `Stage6_P2P.png`. Phân tích đồng thời 4 panel (Base, 3-MG Short, 2-MG Long, 3-MG Long). Chuyển trọng tâm sang cách mạng lưới định tuyến lại (re-routing) công suất P2P khi số lượng Deficit MGs và thời gian tăng lên. Nhấn mạnh việc các tie-line (đặc biệt khi MG1 sập) bị ép lên giới hạn vật lý.
  - **Acceptance criteria:**
    - [ ] Phân tích được sự khác biệt bề rộng các dải màu (P2P flows) giữa 4 kịch bản.

- **Task 3: Viết mục 6.6.2 (Voltage Stability & Security Margins)**
  - **Trạng thái:** `[x] DONE`
  - **Người thực hiện:** `@latex_writer`
  - **Mô tả:** Nhúng hình `Stage6_Voltage.png`. Phân tích đường bao điện áp (Voltage Envelope) của 3 trường hợp lỗi so với Hard Cap 0.9 p.u. và Soft Cap 0.95 p.u. 
  - **Acceptance criteria:**
    - [ ] Giải thích hiện tượng sụt áp (voltage sag) dưới góc độ vật lý dòng tải $I \times Z$.
    - [ ] Chứng minh thuật toán vẫn giữ được an ninh hệ thống (chạm ngưỡng 0.925 p.u. ở 19:00 trong 3-MG Long nhưng không thủng đáy 0.9).

- **Task 4: Viết mục 6.6.3 (Autonomous Critical Load Prioritization & Economic Cost)**
  - **Trạng thái:** `[x] DONE`
  - **Người thực hiện:** `@latex_writer`
  - **Mô tả:** Nhúng 2 hình `Stage6_CostShedding.png` (diễn biến thời gian) và `Robustness_Cost_vs_Shedding copy.png` (tổng kết 4 kịch bản).
  - **Acceptance criteria:**
    - [ ] Phân tích sự tăng phi mã của True Economic Cost và Normal Load Shedding khi thảm họa kéo dài.
    - [ ] Nhấn mạnh "bằng chứng thép": Critical Load Shedding LUÔN LUÔN = `Crit 0.0` trong mọi kịch bản để chứng minh luận điểm "Autonomous Critical Load Prioritization".

### Checkpoint: Complete
- [ ] File LaTeX biên dịch mượt mà 4 biểu đồ.
- [ ] Vượt qua vòng kiểm duyệt logic `deep-logic-audit`.
- [ ] Ready for review by Tư lệnh.
