# CẤU TRÚC 3 LỚP CHO BÁO CÁO: MÔ HÌNH TOÁN HỌC VÀ THUẬT TOÁN (CHƯƠNG 2, 3, 4)

## LỚP 1 (CHƯƠNG 2): CẤU TRÚC VÀ THAM SỐ (System Architecture & Parameters)
*Mục đích: Thiết lập "Sân chơi" và "Luật chơi". Trả lời câu hỏi "Hệ thống có gì?"*
- **2.1. Cấu trúc liên kết P2P:** Mô tả đồ thị mạng (Network Topology) của MG1234 kết nối lưới chính.
- **2.2. Các phần tử năng lượng:** Phương trình hoạt động cơ bản của Nguồn tái tạo (PV/WT), Tải ưu tiên/không ưu tiên, Hệ thống lưu trữ (BESS), và Nguồn dự phòng (Diesel/Micro-turbine).
- **2.3. Tham số hệ thống:** Bảng dữ liệu đầu vào (Capacity, SOC min/max, Ramp-rate, Value of Lost Load - VOLL, v.v.).

## LỚP 2 (CHƯƠNG 3): BÀI TOÁN TỐI ƯU AC-OPF VÀ SOCP LOCAL ATC
*Mục đích: Xây dựng bộ não lõi. Trả lời câu hỏi "Làm sao để tối ưu hệ thống một cách phân tán?"*
- **3.1. Bài toán AC-OPF gốc:** Trình bày phương trình trào lưu công suất phi tuyến (Non-linear).
- **3.2. Cải biến nón bậc hai (SOCP Relaxation):** Chứng minh toán học cách nới lỏng để biến AC-OPF thành bài toán lồi (Convex), đảm bảo tìm được nghiệm tối ưu toàn cục.
- **3.3. Thuật toán ATC (Analytical Target Cascading):** 
  - Cấu trúc bài toán Coordinator (Lưới chính/Thị trường trung tâm).
  - Cấu trúc bài toán Local (Tối ưu riêng rẽ từng MG).
  - Cơ chế trao đổi biến (Công suất trao đổi P, Q và giá bóng $\lambda$). Tiêu chuẩn hội tụ (Convergence criteria).

## LỚP 3 (CHƯƠNG 4): ĐIỀU KHIỂN DỰ BÁO MÔ HÌNH (MPC) VẬN HÀNH THỜI GIAN THỰC
*Mục đích: Lắp bộ não (Lớp 2) vào thực chiến. Trả lời câu hỏi "Hệ thống phản ứng thế nào khi có sự cố đứt cáp?"*
- **4.1. Khái niệm Rolling Horizon trong MPC:** Cách hệ thống trượt khung thời gian để liên tục cập nhật trạng thái mới nhất của Pin (SOC) và dự báo nguồn/tải.
- **4.2. Tích hợp MPC và ATC:** Sơ đồ khối (Flowchart) kết hợp: MPC đóng vai trò "Vòng lặp ngoài" (Outer Loop - Cập nhật trạng thái thời gian), ATC-SOCP đóng vai trò "Vòng lặp trong" (Inner Loop - Giải bài toán ở mỗi bước thời gian).
- **4.3. Cơ chế kích hoạt khẩn cấp (Emergency Mode):** Công thức định nghĩa lại cấu trúc liên kết mạng khi một liên kết bị đứt (sự cố N-2 hoặc Islanding).
