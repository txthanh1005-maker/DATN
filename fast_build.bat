@echo off
echo ============================================================
echo      SUPER FAST LATEX COMPILER (DRAFT MODE OPTIMIZATION)
echo ============================================================
echo.
echo Bước 1/4: Chạy pdflatex lần 1 (Draft Mode - Bỏ qua render PDF)
pdflatex -draftmode -interaction=nonstopmode DATN.tex > nul
if %ERRORLEVEL% NEQ 0 (
    echo [!] Cảnh báo ở Bước 1, vẫn tiếp tục...
)

echo Bước 2/4: Chạy bibtex để tạo danh mục tài liệu tham khảo
bibtex DATN > nul

echo Bước 3/4: Chạy pdflatex lần 2 (Draft Mode - Cập nhật trích dẫn)
pdflatex -draftmode -interaction=nonstopmode DATN.tex > nul

echo Bước 4/4: Chạy pdflatex lần cuối (Render file PDF hoàn chỉnh)
pdflatex -interaction=nonstopmode DATN.tex

echo.
echo ============================================================
echo [x] DONE! QUÁ TRÌNH BIÊN DỊCH HOÀN TẤT.
echo File DATN.pdf đã sẵn sàng.
echo ============================================================
pause
