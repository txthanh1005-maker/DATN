# TỔNG HỢP LỘ TRÌNH CHỈNH SỬA TOÀN DIỆN (CẬP NHẬT 22/06)

Dựa trên việc đối chiếu 5 báo cáo của từng chương (`need_update_chap1.md` đến `need_update_chap5.md`) và tệp quyết định biên tập (`need_update_vi.md`), dưới đây là bản tổng hợp cuối cùng. Bản tổng hợp này chia làm 2 phần: Các lỗi hệ thống xuất hiện xuyên suốt toàn bộ luận văn và Các lỗi kỹ thuật độc lập nằm rải rác ở từng chương.

---

## PHẦN 1: CÁC LỖI HỆ THỐNG XUYÊN SUỐT (COMMON ISSUES)
Đây là những điểm mù về tư duy hoặc các giả định chưa chặt chẽ lặp đi lặp lại qua nhiều chương. Cần phải thêm "Assumptions" (Giả định) hoặc Disclaimer (Từ chối trách nhiệm) thống nhất từ đầu đến cuối.

### 1. Ảo tưởng Quán tính (Infinite Inertia Fallacy) & Ổn định quá độ
- **Biểu hiện:** Ở các Chương 1, 2, 4, 5, tác giả liên tục tuyên bố hệ thống "sống sót 100%" và "ngăn sụp đổ tần số" khi Islanding, nhưng lại dùng mô hình AC-OPF tĩnh (1 giờ/bước) và đùn đẩy trách nhiệm ổn định mili-giây cho Primary Control.
- **Giải pháp chung:** Phải định hình rõ ràng *Scope & Boundary*. Luận văn chỉ giải quyết phần lập lịch tĩnh (Steady-state Secondary/Tertiary Energy Scheduling). Không giải quyết độ ổn định quá độ (Transient/Frequency Stability). Cần bỏ các cụm từ "prevent frequency collapse" ở Chương 5.

### 2. Sự ngây thơ về Hạ tầng Viễn thông (Communication Dependency)
- **Biểu hiện:** Thuật toán ATC (Chương 3) và MPC (Chương 4) đòi hỏi mạng truyền thông liên tục, không độ trễ giữa Master-Slave. Nhưng luận văn lại áp dụng cho trường hợp bão lũ/sự cố cực đoan (N-2) - thời điểm mà mạng viễn thông dễ sập nhất. Ở Chương 1 cũng gọi ATC là "phi tập trung" trong khi bản chất nó là "chủ - tớ".
- **Giải pháp chung:** Đổi chữ "Decentralized" thành "Hierarchical Distributed". Thêm 1 mục thảo luận/giả định về "Zero-latency communication" hoặc đánh giá tác động của mất gói tin (Packet loss) đối với khả năng hội tụ của ATC.

### 3. Phương trình Vật lý & Tiêu chuẩn Lưới điện
- **Biểu hiện:** Bỏ quên vai trò của Công suất phản kháng ($Q$). Chương 1 giả định Inverter cho Q miễn phí; Chương 2 lại đặt $Q_{PV}=0, Q_{WT}=0$ (vi phạm IEEE 1547) và bỏ quên $Q_{tie}$ trong phương trình DistFlow; Chương 4 chỉ điều khiển $P$.
- **Giải pháp chung:** Bổ sung ngay $Q$ vào các phương trình cân bằng công suất, giới hạn P-Q của Inverter, và trích dẫn chuẩn IEEE 1547.

### 4. Rủi ro về Toán học SOCP & Khả năng Hội tụ ATC
- **Biểu hiện:** SOCP yêu cầu lưới hình tia (Strictly radial topology). Nếu cấu trúc lưới thay đổi tạo ra vòng lặp (Meshed) hoặc có dòng công suất ngược (Reverse Power Flow) làm chạm ngưỡng điện áp (Chương 2, 5, vi.md), hoặc nếu hàm phạt VOLL là hàm bậc thang rời rạc (Chương 1), tính lồi (Convexity) và độ chính xác (Exactness) của SOCP sẽ sụp đổ.
- **Giải pháp chung:** Cần chứng minh hội tụ/phân tích độ nhạy cho các tham số ATC ($\tau$, $\mu$). Nêu rõ yêu cầu lưới hình tia cho SOCP.

### 5. Rào cản Kinh tế - Pháp lý Thực tiễn
- **Biểu hiện:** Việc ép MG4 cắt tải ưu tiên để làm đường truyền tải cho MG2 ("Wheeling Hub" ở Chương 5) mà không có cơ chế bồi thường là phi lý. "Negative Premium" che giấu tổn thất xã hội. "Graceful Degradation" (Chương 1) đụng chạm tới công bằng xã hội (Equity) nếu tự ý cắt tải.
- **Giải pháp chung:** Cần thêm các bình luận (caveat) về phí truyền tải của DSO (Wheeling charges), hợp đồng sa thải tự nguyện (DR), và làm rõ Negative Premium chỉ là chi phí vận hành chứ không phải thiệt hại kinh tế - xã hội.

---

## PHẦN 2: CÁC LỖI KỸ THUẬT ĐỘC LẬP TỪNG CHƯƠNG (INDEPENDENT ISSUES)

### Chương 1 (Introduction)
- **Cần làm:** Tinh gọn phần lịch sử Smart Grid, đưa ngay 1-2 con số kết quả định lượng (giảm X% VOLL) vào mở bài để tăng tính hấp dẫn.

### Chương 2 (Problem Formulation)
- **Lỗi chí mạng 1:** Nhầm lẫn SOCP và MISOCP. Phải xóa bỏ biến nhị phân (Binary) sạc/xả BESS vì hàm phạt suy hao đã tự ngăn sạc/xả cùng lúc. Điều này giúp tránh bài toán NP-hard.
- **Lỗi chí mạng 2:** Thiếu nút Slack Bus thiết lập điện áp tham chiếu khi ở chế độ Islanding (Mất lưới).
- **Cần làm:** Cập nhật hàm chi phí BESS (thừa nhận hạn chế của suy hao tuyến tính). Thêm $Q_{tie}$.

### Chương 3 (ATC & MMG Coordination)
- **Lỗi chí mạng 1:** Phương trình cập nhật $P_{target}$ (Eq. 36, 39) bị sai toán học do bỏ quên thành phần nhân tử Lagrange $\lambda$, làm vỡ lý thuyết hội tụ.
- **Lỗi chí mạng 2:** Định nghĩa sai Phần dư Đối ngẫu (Dual Residual - Eq. 67). Lấy sai phân biến cục bộ thay vì biến đồng thuận.
- **Lỗi vật lý:** Phương trình $P_{target,ij} + P_{target,ji} = 0$ giả định dây dẫn không tổn thất. Cần thêm giới hạn truyền tải $P_{tie}^{max}$.

### Chương 4 (Temporal Coordination with MPC)
- **Lỗi thực thi thuật toán:** Việc nhúng vòng lặp ATC (nhiều lần lặp) vào bên trong mỗi bước thời gian thực của MPC có rủi ro đứng máy nếu thuật toán không hội tụ kịp.
- **Cần làm:** Cần thêm ranh giới giới hạn thời gian tính toán (Computational Tractability).

### Chương 5 (Results & Analysis)
- **Lỗi ngụy biện thời gian:** Đánh giá thuật toán mất 91 giây để giải là "đáp ứng thời gian thực để chặn sập tần số" là sai kiến thức điện lực. 91 giây là đủ cho Economic Dispatch, nhưng quá chậm để cứu tần số.
- **Sự hiển nhiên của Toán học:** Cắt tải theo trọng số VOLL là kết quả hiển nhiên của Solver, không nên mô tả như một phép màu tự động.
- **Bổ sung:** Giải thích "Tie-line Congestion Paradox" phải dựa trên lý thuyết định giá biên KKT (LMP). Cung cấp Link Source Code & Dữ liệu tái lập (Reproducibility).

---

## PHẦN 3: KẾ HOẠCH HÀNH ĐỘNG (ACTION PLAN)
1. **Ưu tiên 1 (Toán & Vật lý Core):** Sửa các phương trình ở Chương 3 (ATC KKT) và Chương 2 (xóa biến nhị phân BESS, thêm $Q_{tie}$, thêm Slack Bus).
2. **Ưu tiên 2 (Biện luận & Scope):** Sửa Chapter 1 và Chapter 5 để thiết lập "Assumptions" (Giả định về Viễn thông, Quán tính, Ranh giới Ổn định) nhằm chặn đứng các phản biện từ hội đồng.
3. **Ưu tiên 3 (Pháp lý & Kinh tế):** Bổ sung các bình luận về DSO, Negative Premium, VOLL Equity.
4. **Ưu tiên 4:** Định dạng lại Abstract, điền `references.bib`.
