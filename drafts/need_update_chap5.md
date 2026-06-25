# REVISION ROADMAP: CHAPTER 5 (RESULTS & ANALYSIS)

Dựa trên kết quả thanh tra chéo (Peer Review) từ toàn bộ Hội đồng 5 Sub-agent (EIC, Methodology, Domain, Perspective, Devil's Advocate), dưới đây là danh sách các hạng mục cần cập nhật trong bản thảo `chapter5.tex`.

## 1. ĐIỂM SÁNG ĐƯỢC HỘI ĐỒNG KHEN NGỢI (STRENGTHS)
- **Mô phỏng vật lý phi tuyến AC-OPF xuất sắc:** Việc mô tả hiện tượng "Mượn đường" (Wheeling Current) làm tăng vọt tổn thất công suất phản kháng ($I^2X$), dẫn đến sụt áp và buộc MG4 phải tự ngắt tải của chính mình để cứu hệ thống, là một đóng góp rất sâu sắc về mặt học thuật.
- **Giải mã "Tie-line Congestion Paradox":** Giải thích bằng toán học (điều kiện KKT) lý do giá điện ($LMP$) bị tách rời khi đường dây bị nghẽn (đạt giới hạn truyền tải) được đánh giá cực kỳ cao.
- **Tính kinh tế của P2P:** Phân tích "Negative Premium" (chi phí âm) nhờ tận dụng năng lượng tái tạo kẹt (stranded renewables) thay vì chạy máy phát cục bộ đắt tiền.

## 2. LỖ HỔNG CHÍ MẠNG VỀ TOÁN HỌC & LẬP LUẬN (CRITICAL/MAJOR)
- **Sự ngụy biện về Thời gian hội tụ (91 giây):**
  - **Lỗi:** Tác giả cho rằng thuật toán mất 91 giây (45 vòng lặp) để hội tụ khi mất điện lưới (Islanding) là "khả thi trong thời gian thực" vì nó nằm trong chu kỳ 1 giờ của MPC. 
  - **Phản biện:** Thực tế vật lý, khi mất lưới (mất Slack Bus), hệ thống cần phải cân bằng công suất và đáp ứng quán tính trong vài **mili-giây**. Việc bắt hệ thống chờ 91 giây để thuật toán tính toán xong sẽ dẫn đến sập toàn lưới (Blackout) tức khắc.
  - **Hướng sửa:** Phải đính chính lại rằng thuật toán chỉ giải quyết bài toán Lập lịch Kinh tế (Economic Dispatch) ở cấp độ Secondary/Tertiary sau khi hệ thống đã được cứu bởi Điều khiển Sơ cấp (Primary Droop Control). Xóa bỏ hoàn toàn các cụm từ "ngăn chặn sụp đổ tần số" (prevent frequency collapse).
- **Tính hiển nhiên của "Graceful Degradation":**
  - **Lỗi:** Tác giả tự hào rằng thuật toán "tự động" ưu tiên tải quan trọng (Critical Load). Nhưng thực tế, tác giả đã gán trọng số hàm mục tiêu $VOLL_{critical} \gg VOLL_{normal}$. Việc Solver cắt tải có trọng số thấp trước là điều hiển nhiên của toán học.
  - **Hướng sửa:** Giảm bớt tông điệu tự hào. Ghi nhận đây là sự tuân thủ chặt chẽ của Solver vào hàm mục tiêu thay vì một "khám phá mới".

## 3. LỖ HỔNG VỀ PHƯƠNG PHÁP LUẬN & THỰC TIỄN (MAJOR/MINOR)
- **Sự phi lý về lợi ích (Incentive Incompatibility):**
  - Việc bắt MG4 phải tự cắt tải của chính mình để làm "đường truyền tải" (Wheeling Hub) cho MG2 mượn đường là phi lý về mặt kinh tế nếu các MG thuộc sở hữu độc lập. Cần bổ sung bàn luận về cơ chế bồi thường (Compensation Mechanism) cho MG4.
- **Ngây thơ về hạ tầng Viễn thông (Cyber-Physical Dependency):**
  - Việc lặp 45 lần để giải bài toán trong lúc xảy ra bão lớn/sự cố (N-2) mặc định rằng mạng viễn thông hoạt động hoàn hảo 100%. Cần bổ sung giả định (Assumption) về hệ thống liên lạc độ trễ bằng không (Zero-latency communication) hoặc thừa nhận rủi ro rớt mạng (Packet loss).
- **Thiếu phân tích độ nhạy (Sensitivity Analysis) của MPC:**
  - Cần giải thích tại sao chọn Prediction Horizon = 1 giờ (dẫn đến hiện tượng BESS "tích trữ mù quáng"). Dù EIC nhận định đây là tính năng an toàn thực tế, nhưng vẫn cần bàn luận thêm về việc dùng 2h-4h sẽ ảnh hưởng đến tải tính toán ra sao.
- **Tiêu chuẩn lưới điện (Grid Codes):**
  - Cần trích dẫn tiêu chuẩn IEEE 1547 để bảo vệ mức giới hạn điện áp (0.90 - 1.05 p.u.).

---
**✅ MỆNH LỆNH THỰC THI:** 
Giữ nguyên các phân tích AC-OPF và hiện tượng "Wheeling Current". Gỡ bỏ các từ ngữ khẳng định giải quyết được "Ổn định Tần số" (Frequency Stability). Bổ sung Disclaimer (Từ chối trách nhiệm) ở đầu chương về Giả định Viễn thông hoàn hảo (Perfect Communication), Mạng P2P hợp tác vô điều kiện (Fully cooperative actors), và Tách bạch rõ ranh giới điều khiển tĩnh (Steady-state AC-OPF) so với điều khiển động (Transient Primary Control).
