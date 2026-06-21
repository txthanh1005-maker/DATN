# Spec: Đánh giá Đồ án Tốt nghiệp (Academic Paper Review)

## 1. Mục tiêu (Objective & Success Criteria)
- **Objective:** Kích hoạt skill `academic-paper-reviewer` để tiến hành review chuyên sâu từng phần của Đồ án Tốt nghiệp (bao gồm file tổng `DATN.tex` chứa các thông tin bên lề, mở/kết luận, và 5 chương nội dung từ `chapter1.tex` đến `chapter5.tex`). Tổng hợp toàn bộ các khiếm khuyết, điểm yếu và yêu cầu chỉnh sửa vào một file duy nhất `workspace/need_update.md`.
- **Success Criteria:**
  - Lần lượt review độc lập 6 file: `DATN.tex` và từ `chapter1.tex` đến `chapter5.tex`.
  - Giữ nguyên sức mạnh của hội đồng review 5 thành viên (EIC, Methodology, Domain, Perspective, Devil's Advocate) để mổ xẻ từng phần.
  - File `workspace/need_update.md` được trình bày rõ ràng, phân loại các lỗi (CRITICAL, MAJOR, MINOR) cho từng phần.

## 2. Giả định (Assumptions)
- Dữ liệu nằm trong `D:\Latex\DATN\chapters\` và file gốc `D:\Latex\DATN\DATN.tex`.
- Do review từng chương riêng biệt (thay vì toàn bộ file tại một thời điểm), hội đồng Reviewer cần được cung cấp thông tin tổng thể (từ SESSION_STATE) để đánh giá không bị lệch khỏi bối cảnh toàn cục của DATN.
- Mục tiêu của chiến dịch này chỉ là ĐÁNH GIÁ (READ-ONLY) và TỔNG HỢP, không được phép thay đổi mã nguồn LaTeX.

## 3. Tech Stack & Structure (Phương án triển khai)
- **Skill:** Áp dụng nghiêm ngặt `academic-paper-reviewer` (Full Mode).
- **Quy trình (Từng bước cuốn chiếu):**
  - Quét `DATN.tex` (Tóm tắt, Lời mở đầu, Kết luận) -> Gọi hội đồng Review -> Trích xuất điểm yếu/lỗi -> Ghi vào `need_update.md`.
  - Lặp lại lần lượt cho `chapter1.tex` đến `chapter5.tex`.
  - Cuối cùng, Meta-Agent rà soát lại `need_update.md` để đảm bảo văn phong chuyên nghiệp và loại bỏ các hiểu lầm lặp lại giữa các chương.
- **Vai trò phân bổ:** Giao phó cho Sub-agent chuyên biệt đóng vai trò hội đồng review, Meta-Agent làm nhiệm vụ tóm tắt.

## 4. Ranh giới (Boundaries)
- **ALWAYS DO:** Bám sát tư duy phản biện (Devil's Advocate) và tiêu chuẩn IEEE/Luận văn xuất sắc để bóc tách vấn đề.
- **ASK FIRST:** Báo cáo ngay nếu phát hiện lỗi CRITICAL (sai lệch logic lõi, nghịch lý không thể bảo vệ).
- **FORBIDDEN:** Tuyệt đối không tự ý sửa trực tiếp vào bất kỳ file `.tex` nào. Quá trình này chỉ sinh ra báo cáo `need_update.md`.
