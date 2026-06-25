# Báo Cáo Đồ Án Tốt Nghiệp (DATN) - Cấu Trúc Không Gian Làm Việc

Đây là kho lưu trữ trung tâm của hệ thống biên dịch Đồ án Tốt nghiệp (LaTeX). Hệ thống vừa trải qua đợt "Thiết quân luật" và tái cấu trúc (tháng 6/2026) nhằm đảm bảo sự rõ ràng, bảo vệ cấu trúc lõi và phân tách hoàn toàn giữa tài liệu gốc, dự thảo và các kịch bản tự động hóa.

## 📂 Sơ Đồ Cấu Trúc Thư Mục (Đến Cấp 2)

```text
DATN/
├── agy-memory/                 # 🔴 [BỘ NHỚ AI] Lưu trữ nhận thức hệ thống
│   └── SESSION_STATE.md        # Nguồn chân lý tối cao (Supreme Source of Truth)
│
├── chapters/                   # 🔴 [MỨC 1 - LÕI] Nội dung luận văn
│   ├── Imagine/                # Khu vực chứa hình ảnh, đồ thị, sơ đồ khối
│   ├── SOCP ATC MPC/           # Các biểu đồ và sơ đồ thuật toán phức tạp
│   ├── chapter1.tex            # Giới thiệu & Tổng quan (SOTA Matrix)
│   ├── chapter2.tex            # Cơ sở lý thuyết về lưới điện & P2P
│   ├── chapter3.tex            # Mô hình Toán học (Objective Function)
│   ├── chapter4.tex            # Đề xuất thuật toán (ATC / MPC)
│   └── chapter5.tex            # Phân tích kịch bản mô phỏng
│
├── workspace/                  # 🔴 [MỨC 1 - LÕI] Không gian lập kế hoạch AI
│   ├── ACTION_PLAN.md          # Kế hoạch tác chiến tổng thể
│   ├── Idea.md                 # Định hướng ý tưởng cốt lõi
│   ├── Citation_Matrix.md      # Ma trận so sánh tính nguyên bản
│   ├── Nomenclature.md         # Bảng thuật ngữ tiêu chuẩn
│   └── Model & Algorithmlogic.md # Đặc tả logic thuật toán
│
├── QLDT upload/                # 🟡 [MỨC 2 - ĐẦU RA] Hồ sơ nộp trường
│   └── (Thành phẩm PDF để upload lên phòng Quản lý Đào tạo)
│
├── scripts/                    # 🟢 [MỨC 3 - CÔNG CỤ] Vũ khí tự động hóa
│   ├── check_cites.py          # Quét và bắt lỗi trích dẫn thiếu/thừa
│   ├── extract_pdf.py          # Trích xuất dữ liệu từ PDF
│   ├── mass_replace.py         # Kịch bản thay thế text diện rộng
│   └── verify_dois.py          # Xác thực mã DOI trong thư viện
│
├── drafts/                     # 🔵 [MỨC 4 - DỰ THẢO] Bản nháp & Nhật ký
│   ├── Draft_Intro_Blueprint.md# Bản vẽ phác thảo cấu trúc chương
│   ├── draft_chapter*_summary.tex # Các đoạn summary nháp cho từng chương
│   ├── need_update*.md         # Nhật ký ghi chú các lỗi cần khắc phục
│   └── ĐỒ_ÁN_TỐT_NGHIỆP_*.md   # Các văn bản backup/nháp dạng Markdown
│
├── scratch/                    # ⚪ [MỨC 5 - LƯU TRỮ TẠM] Khu vực kiểm duyệt
│   ├── domain_review_*.md      # Phiếu đánh giá chuyên sâu Vật lý/Toán học
│   ├── eic_review_*.md         # Phiếu đánh giá của Tổng biên tập AI
│   └── methodology_review_*.md # Phiếu đánh giá độ vững chắc của thuật toán
│
├── Transfer folder/            # 🌉 CẦU NỐI DỮ LIỆU (Liên kết phân khu Code)
│   ├── Result_data/            # Dữ liệu biểu đồ kết xuất từ thuật toán
│   ├── Source_data/            # Tham số lưới điện đầu vào (Data thô)
│   └── main.py, build_model.py # Mã nguồn cốt lõi sinh ra kết quả
│
├── DATN.tex                    # 🔴 File Main điều hướng toàn bộ Luận văn
├── references.bib              # 🔴 Thư viện trích dẫn chuẩn BibTeX
├── thesis_1side.cls            # 🔴 Tệp định dạng format chuẩn ĐHBK
└── *.bat                       # Các tệp lệnh biên dịch nhanh (run_latex, test_compile)
```

## 🛠 Quy Trình Vận Hành Tiêu Chuẩn
1. **Chỉnh sửa nội dung:** Chỉ can thiệp trực tiếp vào thư mục `chapters/` hoặc file `DATN.tex`.
2. **Quản lý trích dẫn:** Cập nhật vào `references.bib`, sau đó có thể dùng các kịch bản trong `scripts/` để kiểm duyệt tính toàn vẹn.
3. **Cập nhật số liệu/hình ảnh:** Dữ liệu mới nhất từ môi trường thuật toán Python sẽ được nạp thông qua `Transfer folder/Result_data`, sau đó chèn vào `chapters/Imagine/`.
4. **Biên dịch:** Chạy file `test_compile.bat` để thực thi chuỗi lệnh PDFLaTeX -> BibTeX -> PDFLaTeX.
