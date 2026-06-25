# Phản hồi từ Giáo viên Hướng dẫn (Cập nhật ngày 23/06/2026)

## I. Yêu cầu gốc từ GVHD
1. Cải thiện tên đề tài bỏ "A" ở đầu và tìm cách để không viết tắt MPC và ATC.
2. Sửa template theo template mẫu (Cách dòng và thụt lề).
3. Sửa tháng giao đề tài sang tháng 2.
4. Nhiều ảnh bị mờ.
5. Các time $t=x$ phải thêm đơn vị "h" vào.
6. Không để tên các case lỗi là "long/short fault" nữa mà phải đổi đi.
7. Phần conclusion cần viết dài ra.
8. Thêm conclusion và discussion vào các đoạn.

## II. Phân tích Deadline & Chiến thuật giải quyết

### Deadline 1: Ngày 24/06 - Nộp tên đề tài
- **Ưu tiên Tối thượng:** 
  - Thiết kế các lựa chọn tên đề tài mới đảm bảo không dùng từ viết tắt (Analytical Target Cascading, Model Predictive Control), giữ nguyên cấu trúc học thuật và loại bỏ các mạo từ không cần thiết theo yêu cầu.
  - Cập nhật lập tức vào bìa luận văn (`DATN.tex`) và tờ Giao nhiệm vụ Đồ án.

### Deadline 2: Ngày 28/06 - Nộp quyển (Bản cứng)
*Được chia thành 3 lớp ưu tiên để tránh bị dồn việc:*

**Lớp 1: Cấu trúc lõi & Biểu đồ (Khó, tốn thời gian chạy code)**
- Thay đổi thuật ngữ "long/short fault" thành bộ tên gọi chuẩn mực hơn (ví dụ: Transient Fault, Sustained Fault). Đòi hỏi phải sửa cả LaTeX và chạy lại code Python để thay thế Legend trong các biểu đồ Chương 6.
- Bổ sung các đoạn tiểu kết (Conclusion) và thảo luận (Discussion) vào cuối mỗi chương (Chương 3, 4, 5, 6).
- Mở rộng phần General Conclusion (Chương 7) bằng cách tổng hợp lại các phát hiện cốt lõi đã gặt hái.

**Lớp 2: Rà soát Hiển thị & Định lượng (Cần tỉ mỉ)**
- Kiểm tra toàn bộ ảnh trong thư mục `chapters/Imagine`. Xuất lại ảnh bị mờ với chất lượng 300/600 dpi hoặc chuyển sang ảnh vector.
- Quét toàn bộ luận văn và thay thế các điểm "$t=x$" thành "$t=x$ h" (Kể cả trong label trục của biểu đồ).

**Lớp 3: Format Hành chính (Dễ, làm cuối cùng)**
- Đổi "Tháng giao đề tài" sang Tháng 2.
- Tinh chỉnh `\linespread` và `\parindent` cho khớp template mẫu. (Chỉ làm bước này khi text đã fix 100% để tránh nhảy dòng).

## III. Tích hợp vào Hệ thống
- Các công việc này đã được chia thành các `TODO` list trong `ACTION_PLAN.md` để giao phó cho các Sub-Agents thực thi.
