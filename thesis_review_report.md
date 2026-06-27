# BÁO CÁO REVIEW ĐỒ ÁN TỐT NGHIỆP
## Trường Điện - Điện tử, Đại học Bách khoa Hà Nội (HUST)

**Đề tài:** Resilience-Oriented Peer-to-Peer Energy Trading in Multi-Microgrids via Network-Constrained Distributed Predictive Control

**Sinh viên:** Trịnh Xuân Thành (20222744)
**GVHD:** PGS. Nguyễn Đức Tuyên
**Người review:** Giảng viên phản biện (mô phỏng)
**Ngày review:** 27/06/2026

---

## TỔNG QUAN

Luận văn gồm 86 trang (PDF), 6 chương, 55 tài liệu tham khảo (bbl). Kiến trúc SOCP + ATC + MPC cho P2P energy trading trong multi-microgrid.

**Đánh giá chung:** Luận văn có chất lượng khoa học tốt, kiến trúc 3 tầng được xây dựng logic chặt chẽ, mô phỏng toàn diện. Tuy nhiên, có một số lỗi cần sửa trước khi bảo vệ.

---

## 1. LỖI LOGIC (Trừ điểm nặng)

### Lỗi L-01: Mâu thuẫn SOC constraint giữa Day-Ahead và MPC
- **Vị trí:** Chapter 2 (Eq. 2.9c, dòng 68 chapter2.tex) vs Chapter 4 (Section 4.3.3, Eq. 4.7)
- **Mức độ:** Major
- **Mô tả:** Eq. (2.9c) thiết lập hard constraint `SOC_{i,0} = SOC_{i,24} = SOC^{ini}` (energy neutrality bắt buộc). Tuy nhiên Chapter 4 giới thiệu slack variable `S_{SOC,i}` và penalty `J_{SOC} = β_{SOC} * S_{SOC,i}²` (Eq. 4.7) cho phép vi phạm constraint cuối horizon. Hai cách tiếp cận này mâu thuẫn nhau: một bên là hard equality constraint, bên kia là soft penalty.
- **Tác động:** Hội đồng sẽ hỏi: "Vậy cuối cùng SOC cuối ngày có bị ép bằng SOC đầu ngày không? Hai formulation có consistent không?"
- **Đề xuất:** Cần giải thích rõ: (1) Day-Ahead dùng hard constraint (2.9c), (2) MPC Emergency Mode dùng soft penalty thay thế hard constraint. Nêu rõ khi nào constraint nào được kích hoạt.

### Lỗi L-02: Coordinator Problem được gọi là "SOCP" nhưng không có SOC constraint
- **Vị trí:** Chapter 3, Section 3.2, dòng 33 chapter3.tex
- **Mức độ:** Minor
- **Mô tả:** Câu "The optimization SOCP problem is given by:" nhưng Eq. (3.1) chỉ là bài toán Augmented Lagrangian (quadratic) với một linear equality constraint. Không có yếu tố Second-Order Cone nào. Gọi đây là "SOCP" là sai thuật ngữ.
- **Tác động:** Gây nhầm lẫn về bản chất toán học của bài toán coordinator.
- **Đề xuất:** Sửa thành "optimization problem" hoặc "Augmented Lagrangian problem."

### Lỗi L-03: Khẳng định "exponentially reduce" mà không có bằng chứng
- **Vị trí:** Chapter 6, Section 6.4, dòng 457 DATN.tex
- **Mức độ:** Minor
- **Mô tả:** Câu "Transition toward asynchronous or event-triggered consensus algorithms to exponentially reduce communication overhead..." - Khẳng định "exponentially reduce" quá mạnh và không có chứng minh toán học hay trích dẫn.
- **Tác động:** Hội đồng có thể yêu cầu justification cho "exponentially."
- **Đề xuất:** Đổi thành "significantly reduce" hoặc bổ sung citation.

### Lỗi L-04: Khẳng định "100% survival rate" cần qualification rõ hơn
- **Vị trí:** Abstract (dòng 208 DATN.tex) và Chapter 5, Section 5.2.1, 5.4.4
- **Mức độ:** Minor
- **Mô tả:** "100% survival rate for Critical Loads" chỉ được chứng minh trên 1 testbed cụ thể với 1 kịch bản fault cụ thể. Khẳng định này nghe như một mathematical guarantee tổng quát.
- **Tác động:** Hội đồng sẽ hỏi: "Liệu kết quả này có đúng cho MỌI cấu hình MG và MỌI kịch bản fault không?"
- **Đề xuất:** Thêm qualifier: "achieved 100% survival rate for critical loads across all tested scenarios on the proposed testbed."

### Lỗi L-05: Mâu thuẫn ngưỡng voltage giữa các phần
- **Vị trí:** Chapter 5, Section 5.3.2 (dòng 239) nói "[0.95, 1.05] p.u." vs Section 5.4.3 (dòng 355) nói "0.90 p.u." vs Chapter 6 (dòng 447) nói "0.90 p.u."
- **Mức độ:** Major
- **Mô tả:** Section 5.3.2 nói "statutory hard limits of [0.95, 1.05] p.u." nhưng Section 5.4.3 và Chapter 6 nói voltage được giữ trên "0.90 p.u." Hai giá trị 0.95 p.u. và 0.90 p.u. mâu thuẫn nhau về "statutory threshold."
- **Tác động:** Đây là mâu thuẫn nghiêm trọng về thông số kỹ thuật. Hội đồng sẽ hỏi: "Giới hạn voltage thực tế dùng trong mô phỏng là bao nhiêu?"
- **Đề xuất:** Thống nhất: nêu rõ soft limit = [0.95, 1.05] cho Normal Mode, hard statutory limit = [0.90, 1.10] cho Emergency Mode. Giải thích rõ ở Section 5.1 hoặc Chapter 2.

### Lỗi L-06: Chapter 4 tham chiếu sai nội bộ
- **Vị trí:** Chapter 4, Section 4.3.1, dòng 205 chapter4.tex
- **Mức độ:** Major
- **Mô tả:** Câu "This baseline schedule is derived from the 24-hour ATC SOCP optimization problem described in Chapter 4 (Eq. 3.5)." - Chapter 4 tự tham chiếu chính nó ("described in Chapter 4"). Baseline được thiết lập ở Day-Ahead phase, nên phải tham chiếu "Chapter 3" hoặc "Section 4.1.1."
- **Tác động:** Hội đồng thấy chapter tự tham chiếu sẽ đánh giá thiếu chặt chẽ.
- **Đề xuất:** Sửa thành "described in Chapter 3 (Eq. 3.5)" hoặc cung cấp reference chính xác.

---

## 2. LỖI TRÌNH BÀY (Trừ điểm trực tiếp)

### Lỗi T-01: Overfull \vbox ở Chapter 1
- **Vị trí:** Trang đầu Chapter 1 (DATN.log dòng 1175)
- **Mức độ:** Minor
- **Mô tả:** "Overfull \vbox (2.49832pt too high) has occurred while \output is active" - Nội dung tràn khung trang.
- **Tác động:** Có thể gây chồng lấn footer hoặc header. Mặc dù nhỏ (2.5pt), hội đồng khắt khe vẫn sẽ trừ điểm.
- **Đề xuất:** Thêm `\vspace` hoặc điều chỉnh nội dung trang.

### Lỗi T-02: Overfull \hbox ở Chapter 4 (TikZ flowchart)
- **Vị trí:** Chapter 4, TikZ flowchart (lines 196-197 chapter4.tex), trang 33 (DATN.log dòng 1340)
- **Mức độ:** Major
- **Mô tả:** "Overfull \hbox (24.75204pt too wide)" - TikZ diagram tràn lề trang gần 25pt (~8.7mm). Đây là lỗi tràn lề nghiêm trọng, rất dễ thấy bằng mắt thường.
- **Tác động:** Hội đồng sẽ trừ điểm trình bày trực tiếp vì nội dung bị cắt ở lề phải.
- **Đề xuất:** Thu nhỏ TikZ diagram bằng \resizebox hoặc giảm node distance.

### Lỗi T-03: Caption Warning cho Algorithm 2
- **Vị trí:** Chapter 4, dòng 249 chapter4.tex (DATN.log dòng 1354-1361)
- **Mức độ:** Minor
- **Mô tả:** Dùng `\captionof{algorithm}` bên ngoài environment float, gây hai warnings: "\setcaptiontype outside box or environment" và "hypcap=true will be ignored." Algorithm 2 không được bao bọc trong `\begin{algorithm}` environment.
- **Tác động:** Algorithm 2 có thể không xuất hiện đúng trong List of Algorithms và hyperlink không hoạt động.
- **Đề xuất:** Bao bọc trong `\begin{algorithm}[H]...\end{algorithm}` environment chuẩn.

### Lỗi T-04: Hyperref Warnings cho subsubsection titles
- **Vị trí:** Chapter 2, Sections 2.5.1 và 2.5.2 (DATN.log dòng 1255-1284)
- **Mức độ:** Minor
- **Mô tả:** 8 hyperref warnings "Token not allowed in a PDF string: removing math shift / \Gamma / subscript" - Do tiêu đề mục chứa ký hiệu toán học `$\Gamma_E(t) = 0$` và `$\Gamma_E(t) = 1$` trong bookmark PDF.
- **Tác động:** PDF bookmark sẽ hiển thị không đúng (mất ký hiệu toán).
- **Đề xuất:** Dùng `\texorpdfstring` cho titles có math.

### Lỗi T-05: Đánh số chương không tự động
- **Vị trí:** Toàn bộ DATN.tex và các chapter files
- **Mức độ:** Major
- **Mô tả:** Tất cả chương đều dùng `\section*{CHAPTER X. ...}` (starred, không tự động đánh số) rồi thủ công `\setcounter{section}{X}`. Cách này rất dễ lỗi: figure/table/equation counter phải reset thủ công mỗi chương. Sự thủ công này dẫn đến việc Chapter 3 reset `\setcounter{equation}{0}` nhưng KHÔNG reset figure/table counter.
- **Tác động:** Nếu thêm figure vào Chapter 2, số figure Chapter 3 sẽ tiếp tục đếm sai. Hội đồng sẽ hỏi về tính nhất quán.
- **Đề xuất:** Cân nhắc chuyển sang \section thông thường hoặc đảm bảo tất cả counter được reset đồng nhất.

### Lỗi T-06: Thiếu reset figure/table counter ở Chapter 3
- **Vị trí:** Chapter 3, dòng 1-6 chapter3.tex
- **Mức độ:** Major
- **Mô tả:** Chapter 3 chỉ reset `\setcounter{equation}{0}` mà KHÔNG reset `\setcounter{figure}{0}` và `\setcounter{table}{0}` như các chapter khác làm. Điều này gây đánh số figure tiếp tục từ Chapter 2.
- **Tác động:** Figures trong Chapter 3 bị đánh số sai (tiếp tục từ Chapter 2 thay vì bắt đầu từ 3.1). Ví dụ: Figure 3.1 thực tế sẽ hiển thị là Figure 3.5 hoặc tương tự.
- **Đề xuất:** Thêm `\setcounter{figure}{0}` và `\setcounter{table}{0}` vào đầu chapter3.tex.

### Lỗi T-07: Hình ảnh file name không chuyên nghiệp
- **Vị trí:** Chapter 1, dòng 64 chapter1.tex
- **Mức độ:** Minor
- **Mô tả:** File hình `z7956779224645_7ae6f3c694e347667ff8f318347f2b26.jpg` - đây là filename tự sinh từ Zalo hoặc Facebook. Không chuyên nghiệp cho luận văn.
- **Tác động:** Nếu hội đồng kiểm tra mã nguồn, sẽ đánh giá thiếu cẩn thận.
- **Đề xuất:** Đổi tên file thành descriptive name, ví dụ: `opf_tradeoff_comparison.jpg`.

### Lỗi T-08: File hình có tên chứa dấu cách
- **Vị trí:** Nhiều nơi: "MG structure.jpg", "SOCP relaxation.png", "microgrid connetion.png", "ATC Iterative Sequence Flow.png"
- **Mức độ:** Minor
- **Mô tả:** File names chứa dấu cách có thể gây lỗi trên một số hệ thống LaTeX.
- **Tác động:** Rủi ro portability.
- **Đề xuất:** Thay dấu cách bằng underscore.

### Lỗi T-09: Lỗi chính tả trong tên file hình
- **Vị trí:** Chapter 3, dòng 14 chapter3.tex
- **Mức độ:** Minor
- **Mô tả:** File tên "microgrid connetion.png" - sai chính tả, phải là "connection."
- **Tác động:** Thiếu chuyên nghiệp.
- **Đề xuất:** Rename thành "microgrid_connection.png".

---

## 3. LỖI NGÔN NGỮ

### Lỗi N-01: Lặp từ "distributed distributed"
- **Vị trí:** Trang THESIS ASSIGNMENT, dòng 142 DATN.tex
- **Mức độ:** ⚠️ Critical
- **Mô tả:** "Design a distributed distributed coordination framework..." - Từ "distributed" bị lặp 2 lần. Đây là lỗi rất dễ thấy nằm ngay ở trang ĐỀ BÀI CHÍNH THỨC.
- **Tác động:** Hội đồng đọc đề bài và thấy lỗi chính tả ngay lập tức sẽ ấn tượng xấu. Đây là trang có chữ ký giảng viên.
- **Đề xuất:** Sửa thành "Design a distributed coordination framework..."

### Lỗi N-02: Thiếu dấu chấm cuối câu ở Section 1.2
- **Vị trí:** Chapter 1, Section 1.2, cuối đoạn về SOCP (dòng 56 chapter1.tex)
- **Mức độ:** Minor
- **Mô tả:** Đoạn kết thúc bằng "...accelerating computational speed and inherently preserving the strict AC physics of the grid \cite{Low2014_SOCP}" THIẾU dấu chấm (.) trước khi sang đoạn mới.
- **Tác động:** Lỗi ngữ pháp cơ bản.
- **Đề xuất:** Thêm dấu chấm sau `\cite{Low2014_SOCP}`.

### Lỗi N-03: Câu bắt đầu không có chủ ngữ
- **Vị trí:** Chapter 2, Section 2.3, dòng 98 chapter2.tex
- **Mức độ:** Minor
- **Mô tả:** "AC-OPF model. Operating at the foundational level..." - Fragment sentence. "AC-OPF model" đứng một mình không phải câu hoàn chỉnh.
- **Tác động:** Văn phong không học thuật.
- **Đề xuất:** Ghép lại: "The AC-OPF model operates at the foundational level..."

### Lỗi N-04: Sử dụng "MG" vừa để chỉ Microgrid vừa Main Grid
- **Vị trí:** Chapter 5, Section 5.1, dòng 11 chapter5.tex
- **Mức độ:** Major
- **Mô tả:** "one Main Grid (MG0) and four interconnected MGs (MG1, MG2, MG3, and MG4)." Ở đây "MG0" viết tắt cho Main Grid, nhưng List of Abbreviations định nghĩa MG = Microgrid. Gọi Main Grid là "MG0" gây nhầm lẫn nghiêm trọng.
- **Tác động:** Hội đồng sẽ hỏi: "MG0 là Microgrid hay Main Grid?"
- **Đề xuất:** Gọi Main Grid là "Utility Grid" hoặc "Grid0" để phân biệt rõ.

### Lỗi N-05: Trộn lẫn tiếng Việt và tiếng Anh ở trang bìa
- **Vị trí:** Cover page, dòng 118 DATN.tex
- **Mức độ:** Minor
- **Mô tả:** "Hà Nội, June 2026" - Trộn tiếng Việt ("Hà Nội") và tiếng Anh ("June"). Tương tự dòng 149 "Hà Nội, .../02/2026."
- **Tác động:** Không nhất quán ngôn ngữ.
- **Đề xuất:** Thống nhất: hoặc "Ha Noi, June 2026" hoặc "Hà Nội, Tháng 6/2026." (Nếu luận văn viết bằng tiếng Anh, nên dùng "Hanoi, June 2026.")

---

## 4. LỖI CẤU TRÚC

### Lỗi C-01: Thiếu APPENDIX
- **Vị trí:** DATN.tex dòng 499-502
- **Mức độ:** Minor
- **Mô tả:** Appendix bị comment out (`% \section*{APPENDIX}`). Theo quy định BKHN, luận văn nên có phụ lục chứa: (1) code Python/Pyomo implementation, (2) dữ liệu đầu vào chi tiết (24h load/generation profiles), (3) network impedance data. Hiện tại các dữ liệu này không xuất hiện ở đâu trong luận văn.
- **Tác động:** Hội đồng không thể kiểm chứng tính tái lập (reproducibility) của kết quả mô phỏng.
- **Đề xuất:** Thêm Appendix với ít nhất: (A) Simulation code flowchart hoặc key code snippets, (B) Full 24h data profiles, (C) Network impedance tables.

### Lỗi C-02: Chapter 6 quá ngắn cho Conclusion
- **Vị trí:** DATN.tex dòng 418-462, ~2 trang
- **Mức độ:** Minor
- **Mô tả:** Chapter Conclusion chỉ có ~2 trang. Thiếu phần so sánh chi tiết kết quả đạt được vs mục tiêu ban đầu (từ THESIS ASSIGNMENT).
- **Tác động:** Hội đồng kỳ vọng Conclusion khoảng 3-4 trang với structured comparison.
- **Đề xuất:** Thêm subsection mapping rõ từng contribution lên từng objective trong Thesis Assignment.

### Lỗi C-03: Thiếu phần "Simulation Environment"
- **Vị trí:** Chapter 5
- **Mức độ:** Minor
- **Mô tả:** Không có thông পুরা rõ ràng về: (1) ngôn ngữ lập trình (Python? MATLAB?), (2) solver (Gurobi? CPLEX? MOSEK?), (3) hardware (CPU, RAM), (4) OS. Đây là thông tin bắt buộc cho reproducibility.
- **Tác động:** Hội đồng sẽ yêu cầu bổ sung.
- **Đề xuất:** Thêm 1 đoạn ngắn ở Section 5.1 nêu rõ simulation environment.

---

## 5. TÍNH HỌC THUẬT

### Lỗi H-01: Trùng lặp tài liệu tham khảo
- **Vị trí:** references.bib, entries "Ullah2022" (dòng 340) và "Ullah2022_LMP" (dòng 742)
- **Mức độ:** Major
- **Mô tả:** Hai bib entries cùng trỏ đến cùng một bài báo: Ullah & Park (2022) "DLMP integrated P2P2G energy trading..." với cùng DOI. Cả hai đều xuất hiện trong bibliography output (\bibitem #38 và #54).
- **Tác động:** Hội đồng sẽ nhận thấy danh sách tham khảo bị inflated. Hai entries trùng lặp = thiếu cẩn thận.
- **Đề xuất:** Gộp thành 1 entry duy nhất, thống nhất cite key.

### Lỗi H-02: Nhiều bib entries thiếu volume/pages
- **Vị trí:** references.bib - nhiều entries (ví dụ: Ahmad2023, Dagar2021, Muhtadi2021, v.v.)
- **Mức độ:** Minor
- **Mô tả:** Khoảng 20+ entries chỉ có journal + year, thiếu volume, number, pages. Điều này khiến references không đầy đủ theo chuẩn IEEE.
- **Tác động:** Hội đồng sẽ đánh giá chất lượng trích dẫn kém.
- **Đề xuất:** Bổ sung volume/pages cho các bài đã published.

### Lỗi H-03: Số lượng tài liệu tham khảo hạn chế
- **Vị trí:** DATN.bbl - 55 entries
- **Mức độ:** Minor
- **Mô tả:** 55 tài liệu cho một ĐATN cấp kỹ sư tại BKHN là ở mức chấp nhận được (thường yêu cầu ≥ 30-40). Tuy nhiên, comment ở dòng 492 DATN.tex ghi "Task 2 will populate this with >= 50 entries" cho thấy con số này vừa đủ ngưỡng.
- **Tác động:** Không bị trừ điểm nặng nhưng có thể thêm để tăng tính thuyết phục.
- **Đề xuất:** Bổ sung thêm 5-10 references, đặc biệt về resilience metrics và BESS degradation models.

### Lỗi H-04: Một số entries thiếu DOI
- **Vị trí:** references.bib - ATC_Coopt_2025 (dòng 735), Zhang2019_ADMM (thiếu volume/pages)
- **Mức độ:** Minor
- **Mô tả:** Entry "ATC_Coopt_2025" (Wang et al.) chỉ có title, journal, year - không có DOI, volume, hay pages. "Zhang2019_ADMM" thiếu volume.
- **Tác động:** Không thể verify nguồn.
- **Đề xuất:** Bổ sung đầy đủ metadata.

### Lỗi H-05: \bibliographystyle bị comment trong DATN.tex nhưng có trong class file
- **Vị trí:** DATN.tex dòng 493 vs thesis_1side.cls dòng 134
- **Mức độ:** Minor
- **Mô tả:** `\bibliographystyle{IEEEtran}` bị comment trong DATN.tex nhưng được define trong thesis_1side.cls. Tuy compile đúng, nhưng cấu trúc confusing.
- **Tác động:** Khó maintain.
- **Đề xuất:** Loại bỏ dòng comment trong DATN.tex để tránh nhầm lẫn.

---

## BẢNG TÓM TẮT LỖI

| # | Loại | ID | Mức độ | Vị trí | Tóm tắt |
|---|------|----|--------|--------|---------|
| 1 | Logic | L-01 | Major | Ch2 vs Ch4 | Mâu thuẫn SOC hard constraint vs soft penalty |
| 2 | Logic | L-02 | Minor | Ch3 §3.2 | Coordinator problem gọi sai là "SOCP" |
| 3 | Logic | L-03 | Minor | Ch6 §6.4 | "exponentially reduce" không có chứng minh |
| 4 | Logic | L-04 | Minor | Abstract, Ch5 | "100% survival" cần qualification |
| 5 | Logic | L-05 | Major | Ch5 §5.3.2 vs §5.4.3 | Mâu thuẫn ngưỡng voltage 0.95 vs 0.90 p.u. |
| 6 | Logic | L-06 | Major | Ch4 §4.3.1 | Chapter tự tham chiếu chính nó |
| 7 | Trình bày | T-01 | Minor | Ch1 trang 1 | Overfull vbox |
| 8 | Trình bày | T-02 | Major | Ch4 trang 33 | Overfull hbox 24.75pt - TikZ tràn lề |
| 9 | Trình bày | T-03 | Minor | Ch4 Algorithm 2 | Caption warning |
| 10 | Trình bày | T-04 | Minor | Ch2 §2.5.1-2 | Hyperref warnings trong PDF bookmark |
| 11 | Trình bày | T-05 | Major | Toàn bộ | Đánh số chương thủ công, dễ lỗi |
| 12 | Trình bày | T-06 | Major | Ch3 | Thiếu reset figure/table counter |
| 13 | Trình bày | T-07 | Minor | Ch1 | File hình tên Zalo/Facebook |
| 14 | Trình bày | T-08 | Minor | Nhiều nơi | File hình chứa dấu cách |
| 15 | Trình bày | T-09 | Minor | Ch3 | Lỗi chính tả "connetion" |
| 16 | Ngôn ngữ | N-01 | ⚠️ Critical | Thesis Assignment | "distributed distributed" lặp từ |
| 17 | Ngôn ngữ | N-02 | Minor | Ch1 §1.2 | Thiếu dấu chấm cuối đoạn |
| 18 | Ngôn ngữ | N-03 | Minor | Ch2 §2.3 | Fragment sentence |
| 19 | Ngôn ngữ | N-04 | Major | Ch5 §5.1 | MG dùng cho cả Microgrid và Main Grid |
| 20 | Ngôn ngữ | N-05 | Minor | Cover page | Trộn tiếng Việt-Anh |
| 21 | Cấu trúc | C-01 | Minor | Appendix | Thiếu Appendix (code, data) |
| 22 | Cấu trúc | C-02 | Minor | Ch6 | Conclusion quá ngắn |
| 23 | Cấu trúc | C-03 | Minor | Ch5 | Thiếu simulation environment |
| 24 | Học thuật | H-01 | Major | references.bib | Trùng lặp tài liệu (Ullah2022) |
| 25 | Học thuật | H-02 | Minor | references.bib | Thiếu volume/pages ~20 entries |
| 26 | Học thuật | H-03 | Minor | DATN.bbl | 55 refs - vừa đủ |
| 27 | Học thuật | H-04 | Minor | references.bib | Một số entries thiếu DOI |
| 28 | Học thuật | H-05 | Minor | DATN.tex | bibliographystyle confusing |

---

## THỐNG KÊ
- **Critical:** 1 lỗi
- **Major:** 8 lỗi
- **Minor:** 19 lỗi
- **Tổng:** 28 lỗi

---

## ĐÁNH GIÁ TỔNG THỂ

**Điểm mạnh:**
1. Kiến trúc 3 tầng (SOCP + ATC + MPC) logic chặt chẽ, có tính original cao
2. Phân tích kết quả sâu sắc: Tie-line Congestion Paradox, Voltage Paradox được giải thích xuất sắc
3. 3D Evaluation Framework (Horizontal + Vertical + Boundary) rất có hệ thống
4. Có 2 bài báo khoa học (1 hội nghị quốc tế, 1 tạp chí)
5. Văn phong tiếng Anh nhìn chung tốt, academic tone phù hợp

---

## ƯU TIÊN SỬA (PHẢI sửa trước bảo vệ)

| Ưu tiên | ID | Mô tả | Thời gian ước tính |
|---------|-----|-------|-------------------|
| 🔴 1 | N-01 | Sửa "distributed distributed" ở Thesis Assignment | 1 phút |
| 🔴 2 | T-06 | Thêm reset figure/table counter ở Chapter 3 | 1 phút |
| 🔴 3 | L-05 | Thống nhất ngưỡng voltage 0.95 vs 0.90 p.u. | 15 phút |
| 🔴 4 | T-02 | Fix TikZ overfull hbox (24.75pt tràn lề) | 10 phút |
| 🔴 5 | H-01 | Gộp duplicate reference (Ullah2022) | 5 phút |
| 🔴 6 | L-06 | Sửa self-reference ở Chapter 4 | 1 phút |

---

*Báo cáo review được thực hiện dựa trên phân tích mã nguồn LaTeX và log file compilation.*
