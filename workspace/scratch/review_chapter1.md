# Báo cáo Đánh giá (Peer Review Report) - Chapter 1
**Tác giả:** Trịnh Xuân Thành
**Chương đánh giá:** Chương 1 - Introduction and Literature Review

---

## 1. Editor-in-Chief (EIC)
**Đánh giá tổng quan:**
Chương 1 được viết rất mạch lạc và có cấu trúc logic xuất sắc. Việc dẫn dắt từ tổng quan lưới điện thông minh, đi sâu vào từng khía cạnh (Physical - SOCP, Spatial - ATC, Temporal - MPC) và cuối cùng tổng hợp thành "Master Gap" mang tính thuyết phục cao. Lập luận chuyển đổi thị trường P2P từ "kinh tế đơn thuần" sang "nền tảng phục hồi" (Resilience backbone) là điểm sáng lớn nhất.
- **Quyết định đề xuất:** Minor Revision.

## 2. Methodology Reviewer (Reviewer 1)
**Trọng tâm:** Cơ sở toán học của SOCP, ATC và MPC.
- **CRITICAL:** Tại Mục 1.2 (Footnote 1), tác giả khẳng định rằng hàm mục tiêu chứa VOLL penalty sẽ ép (force) hệ thống siết chặt ranh giới hội tụ của SOCP (guarantees exactness). Đây là một tuyên bố toán học rất mạnh. Thường thì việc tối thiểu hóa tổn thất (loss minimization) mới đẩy SOCP về exactness. Việc dùng VOLL (load shedding penalty) để đảm bảo exactness cần được trích dẫn cụ thể hoặc giải thích cơ sở toán học rõ ràng hơn, tránh overclaim.
- **MAJOR:** Ở Mục 1.3, tác giả loại bỏ ADMM vì cho rằng nó gây ra "dao động" (oscillation) trong mô hình SOCP phân cấp đa tầng. Tuy nhiên, nhiều biến thể của ADMM (như Multi-block ADMM hoặc ALADIN) đã giải quyết được vấn đề này. Việc khẳng định ATC là giải pháp duy nhất / ưu việt tuyệt đối cần được viết lại với sắc thái cẩn trọng hơn (nuanced).
- **MINOR:** Mục 1.4 đề cập đến "warm-start mechanism" giúp giảm số vòng lặp ATC. Khuyến nghị thêm 1-2 câu giải thích cơ chế này hoạt động như thế nào giữa các bước thời gian (time steps).

## 3. Domain Reviewer (Reviewer 2)
**Trọng tâm:** Kỹ thuật Hệ thống Điện & Khả năng phục hồi (Resilience).
- **MAJOR:** Mục 1.2 giải thích việc DER dùng dung lượng Inverter dư thừa ($S_{max}^2 \ge P^2 + Q^2$) để bù Q cục bộ. Tuy nhiên, trong điều kiện sự cố cực đoan (HILP), việc thiếu hụt Q có thể vượt quá giới hạn $S_{max}$ của Inverter cục bộ. Bài viết cần có một sự thừa nhận (acknowledgement) ngắn về giới hạn vật lý của phương pháp "No P2P Q trading" ngay trong phần Mở đầu.
- **MINOR:** Cụm từ "Extreme weather events" và "prolonged outages" cần được định lượng sơ bộ (ví dụ: mất điện vài giờ hay vài ngày?) để làm rõ bối cảnh hoạt động của MPC rolling horizon.

## 4. Perspective Reviewer (Reviewer 3)
**Trọng tâm:** Góc nhìn Kinh tế - Kỹ thuật (Socio-economic impact).
- **MAJOR:** Kiến trúc Tri-layer này tập trung mạnh vào "Khả năng phục hồi" (Resilience). Tuy nhiên, độc giả sẽ thắc mắc: Trong điều kiện bình thường (Normal Operation - không có sự cố), liệu khung quản lý khắt khe này có làm giảm hiệu quả kinh tế so với thị trường P2P thông thường không? Cần 1-2 câu làm rõ sự đánh đổi (trade-off) này trong phần Motivation.
- **MINOR:** Tại Mục 1.3 (Privacy), tác giả nói ATC bảo vệ quyền riêng tư. Hãy liệt kê cụ thể 1-2 thông số được giấu kín (ví dụ: SOC của BESS, đường cong tải cục bộ, giá bid) để tăng tính thực tiễn.

## 5. Devil's Advocate
**Trọng tâm:** Thử thách các lập luận cốt lõi và phát hiện ngụy biện.
- **Strongest Counter-Argument:** Tại Mục 1.4, tác giả chỉ trích Robust Optimization (RO) là "open-loop" và quá bảo thủ, sau đó ca ngợi MPC như giải pháp tối ưu cho "HILP events". Đây là một ngụy biện logic (Overgeneralization). MPC chạy trên cơ sở dự báo tất định (deterministic predictions) trong cửa sổ thời gian (rolling window). Đối với HILP (ví dụ: bão làm đổ cột điện ngay lập tức), MPC không thể "dự báo" được sự kiện đứt gãy vật lý này. MPC chỉ phản ứng *sau khi* sự cố xảy ra. Do đó, việc nói MPC "proactively" (chủ động) đối phó với HILP events là chưa chính xác.
- **CRITICAL:** Khẳng định "The master gap lies in the absence of a unified framework..." (Mục 1.5.1) là một tuyên bố tuyệt đối (absolutist claim) rất nguy hiểm trong nghiên cứu khoa học. Rất khó để chứng minh "sự vắng mặt hoàn toàn" của một khung hệ thống kết hợp SOCP-ATC-MPC trong văn bản học thuật toàn cầu. Yêu cầu sửa thành "There is a significant lack of..." hoặc "Few studies have successfully integrated...".

---
## TỔNG HỢP VÀ ĐỀ XUẤT (EDITORIAL SYNTHESIS)
**Đánh giá sự đồng thuận:**
Hội đồng thống nhất rằng Chương 1 là một bản Introduction & Literature Review xuất sắc, dẫn dắt vấn đề logic và thuyết phục. Tuy nhiên, tác giả mắc phải một số lỗi "overclaim" (tuyên bố quá mức) về mặt toán học và định vị nghiên cứu.

**Roadmap Chỉnh sửa (Revision Roadmap):**
1. **[CRITICAL] Giảm nhẹ các tuyên bố tuyệt đối (Tone down absolute claims):** Sửa lại câu "absence of a unified framework" thành "significant lack of..." để tránh bị bắt bẻ. Xem xét lại khẳng định "MPC proactively prevents HILP events" (MPC phản ứng linh hoạt, nhưng không dự báo trước được thảm họa vật lý ngẫu nhiên).
2. **[CRITICAL] Làm rõ Footnote 1 về SOCP Exactness:** Cần giải thích cơ chế toán học hoặc trích dẫn tài liệu chứng minh VOLL penalty thực sự ép chặt (tighten) được SOCP relaxation gap.
3. **[MAJOR] Cân bằng lập luận:** Nêu nhận xét khách quan hơn về ADMM thay vì bác bỏ hoàn toàn; đồng thời thừa nhận giới hạn dung lượng $S_{max}$ khi bù Q cục bộ bằng Inverter.
4. **[MINOR] Cụ thể hóa thông tin:** Thêm ví dụ về dữ liệu được bảo mật (Privacy) và định lượng "prolonged outages" là trong khung thời gian nào.

**Quyết định cuối cùng:** MINOR REVISION. Chỉ cần tinh chỉnh câu chữ và làm rõ một số lập luận để tạo độ chặt chẽ tối đa.
