# BẢNG PHÂN BỔ LUẬN ĐIỂM & TRÍCH DẪN (CITATION MATRIX)
Được trích xuất từ `chapter1.tex` và `chapter2.tex` cũ để tái sử dụng. Tất cả các trích dẫn này đã được kiểm duyệt nội dung và ghép nối với các Lăng kính (Sub-themes) trong Draft Blueprint.

## 0. Dùng cho SECTION 1.1: Bức tranh Vĩ mô (Macro View & Sự tiế/n hóa của Smart Grid)
- **Luận điểm 1 (Chuyển dịch Năng lượng):** Chuyển từ lưới điện truyền thống tập trung sang phân tán (DERs). Sự thâm nhập ồ ạt của điện mặt trời/gió biến người dùng từ passive consumers thành active prosumers, tạo ra thách thức điều phối hai chiều.
  - **Trích dẫn:** `\cite{Muhtadi2021, Dagar2021}`, `\cite{Ahmad2023}`
- **Luận điểm 2 (Vai trò của Microgrid & BESS):** Microgrid (MG) ra đời như một tế bào cơ sở của Smart Grid để quản lý sự phức tạp này. BESS là công cụ sống còn để hấp thụ sự biến thiên của năng lượng tái tạo.
  - **Trích dẫn:** `\cite{She2022}` (khái niệm MG), `\cite{Trivedi2022}` (khả năng tách đảo / kết nối lưới), `\cite{Choudhury2022}` (vai trò của BESS).
- **Luận điểm 3 (Thị trường P2P Trading):** Thay thế các cơ chế cứng nhắc như Feed-in-Tariff (FIT). P2P Trading giúp tối đa hóa phúc lợi cộng đồng, rút ngắn thời gian thu hồi vốn và tạo ra tự chủ năng lượng (Energy Autonomy).
  - **Trích dẫn:** `\cite{Victoria2021, Karami2021, Ali2022}` (concept), `\cite{Park2024, Antonopoulos2020}` (vượt trội hơn FIT), `\cite{Zia2020}` (Tự chủ năng lượng).
- **Luận điểm 4 (Sự bẻ lái sang Grid Resilience - CẬP NHẬT MỚI 2020+):** Trước tần suất gia tăng của các sự kiện thời tiết cực đoan và thiên tai (Extreme Events/Blackouts), mục tiêu của Microgrids và P2P không chỉ dừng lại ở hiệu quả kinh tế. P2P Trading bắt buộc phải đóng vai trò như một mạng lưới an toàn (Safety Net), cung cấp khả năng tự phục hồi (Resilience) và định tuyến năng lượng khẩn cấp để bảo vệ phụ tải.
  - **Trích dẫn (IEEE/Elsevier 2020+):** `\cite{AlIsmail2021}` (DC Microgrid Planning, Operation, and Control: A Comprehensive Review), `\cite{Chen2020}` (Networked Microgrids for Grid Resilience, Robustness, and Efficiency: A Review), `\cite{Bhusal2020}` (Power System Resilience: Current Practices, Challenges, and Future Directions).

## 1. Dùng cho SUB-THEME 1: Lăng kính Vật lý (Power Flow & Network Constraints)

### Phe 1: Mô hình Đồng dẫn (Lumped-Node / Single-Node)
- **Luận điểm:** Gộp chung tất cả nguồn và tải vào một nút, bỏ qua hoàn toàn mạng lưới. Hậu quả là che giấu các vi phạm về điện áp và gây nghẽn mạch cục bộ khi áp dụng vào thực tế.
- **Trích dẫn (Support):** `\cite{Liu2022, Botelho2022}` và `\cite{Feng2025, Samende2022}`

### Phe 2: Tuyến tính hóa (LinDistFlow / MILP)
- **Luận điểm:** Bỏ qua tổn hao trên nhánh và sụt áp ngang (transverse voltage drops). Giả định này sai lầm nghiêm trọng ở lưới phân phối (R/X cao) nơi P-Q-V có sự ràng buộc phi tuyến mạnh mẽ.
- **Trích dẫn (Support):** `\cite{Ullah2021, Feng2022}`, `\cite{Patari2021, Pareek2020}`, `\cite{Aboshady2023, Helou2021, Saidi2021, Xu2021}`
- **Luận điểm bổ sung (P-Q-V Coupling):** Biến động của P sẽ lập tức kéo theo sự sụt giảm của V ở lưới phân phối. Việc tách rời kinh tế (P) khỏi vận hành (Q, V) là nguyên nhân gây sập áp.
- **Trích dẫn (Support):** `\cite{Hashmi2020, Amir2023}`, `\cite{Polat2025}`, `\cite{Gao2022}`

### Phe 3: Nới lỏng SOCP (SOCP Relaxation)
- **Luận điểm:** AC-OPF là bài toán phi tuyến (non-convex) dễ rơi vào tối ưu cục bộ. SOCP biến đổi toán học (convexification) để đảm bảo tìm ra nghiệm tối ưu toàn cục (Global Optimum) trong khi vẫn tuân thủ nghiêm ngặt vật lý AC.
- **Trích dẫn (Support):** `\cite{Roald2022}`, `\cite{Patari2021, Mahdavi2021}`, `\cite{Fobes2020, Etedadi2021, Srivastava2023}`, `\cite{Garrido_Arevalo_2024, Yuvaraj_2025}`

## 2. Dùng cho SUB-THEME 2: Lăng kính Không gian & Bảo mật (Decentralization & Privacy)

### Phe 1: Hệ thống Tập trung (Centralized EMS)
- **Luận điểm:** Có thể tìm nghiệm tối ưu toàn cục dễ dàng do thấy hết thông tin, nhưng lại vi phạm nghiêm trọng tính riêng tư của dữ liệu (Privacy) và sinh ra rủi ro Single-point-of-failure (Chết chùm).
- **Trích dẫn (Support):** `\cite{Yuan2023, Chen2021}`, `\cite{Liu2025, Zhang2024}`, `\cite{Riedel2024, Zuo2022}`

### Phe 2: Phân tán với ADMM (Giao dịch Phẳng - Flat structure)
- **Luận điểm:** ADMM cho phép xé nhỏ bài toán (Decomposition), giúp bảo vệ Privacy (các bên chỉ trao đổi biến biên giới). Ngoài ra, các biến đối ngẫu (Dual variables) của ADMM hội tụ chính là Tín hiệu Giá bóng (DLMP), phản ánh chi phí biên cục bộ.
- **Trích dẫn (Support về ADMM & Privacy):** `\cite{Yuan2022, Zhao2022, Sun2024}`, `\cite{Chen2025, BASARAN2026}`
- **Trích dẫn (Support về ADMM sinh DLMP):** `\cite{Ullah2022, Nasiri2023}`, `\cite{Zhang2020, Xia2024, Zhu2024, Mishra2024}`
- Chiến thuật Chuyển ý (Gap): Ta sẽ dùng các trích dẫn trên để công nhận thành tựu của ADMM ở mạng phẳng. SAU ĐÓ, ta sẽ tung đòn phản biện: ADMM hội tụ cực kỳ rùa bò khi áp dụng cho lưới phân cấp (Hierarchical) giải SOCP -> Cần thay bằng ATC.

### Phe 3: Nhược điểm của ADMM trong Lưới Phân cấp (Hierarchical/SOCP)
- **Luận điểm:** Dù ADMM rất mạnh trong các hệ thống phẳng (flat structure), nhưng khi áp dụng vào các bài toán đa tầng (Hierarchical) có chứa ràng buộc phi tuyến hoặc SOCP, ADMM bộc lộ nhược điểm là tốc độ hội tụ rất chậm (slow convergence speed) và dễ sinh ra dao động (oscillation) không ổn định giữa các cấp.
- **Trích dẫn (Criticism):** `\cite{Rajaei2021, Yang2023_OPF, Mansouri_2025, Sun_2022}`
- **Tóm tắt hỗ trợ:**
  - `Rajaei2021`: Đánh giá quá trình hội tụ của ADMM trong điều phối đa microgrid, chỉ ra các giới hạn khi mô hình lưới phức tạp lên.
  - `Yang2023_OPF`: Tổng quan các phương pháp tối ưu hóa, nhấn mạnh rằng ADMM và các phương pháp phân tán thường tiêu tốn lượng lớn thời gian tính toán hoặc dao động khi giải các mô hình OPF phi tuyến (như SOCP) trong mạng lưới phân phối.
  - `Mansouri_2025`: Phân tích khuôn khổ tối ưu phi tập trung, nhấn mạnh tính cực kỳ nhạy cảm của tham số phạt (penalty parameter) của ADMM đối với tốc độ hội tụ ở microgrid.
  - `Sun_2022`: Làm rõ các nhược điểm của ADMM khi áp dụng cho các bài toán tối ưu có ràng buộc phi tuyến (non-convex/SOCP), thường xuyên dẫn đến phân kỳ (divergence) hoặc dao động chậm chạp.

### Phe 4: Analytical Target Cascading (ATC) - Giải pháp tối ưu từ trên xuống
- **Luận điểm:** Để khắc phục sự kém hiệu quả của ADMM trong cấu trúc phân cấp, ATC (Analytical Target Cascading) được sử dụng để điều phối mục tiêu từ trên xuống (Top-Down Approach). ATC cho phép xé nhỏ bài toán thành các bài toán tối ưu cục bộ tại từng cấp độ một cách độc lập, duy trì bảo mật thông tin, hội tụ nhanh hơn và quản lý hiệu quả giao dịch năng lượng giữa Lưới phân phối và Microgrid.
- **Trích dẫn (Solution):** `\cite{Zhao2022_ATC, Kong2020_ATC, Wu_2023, Yang_2024}`
- **Tóm tắt hỗ trợ:**
  - `Zhao2022_ATC`: Sử dụng cấu trúc tối ưu hóa phân cấp đa tầng (Hierarchical) để quản lý năng lượng đa microgrid trong môi trường thị trường điện, vượt qua điểm nghẽn hiệu năng của mô hình phẳng thông thường.
  - `Kong2020_ATC`: Ứng dụng chiến thuật dạng phân rã mục tiêu (Target Cascading) để xây dựng chiến lược vận hành tối ưu cho các microgrid liên kết nối, chứng minh khả năng hội tụ nhanh và ổn định cao dưới điều kiện bất định.
  - `Wu_2023`: Ứng dụng ATC để tối ưu hóa điều độ đa tác nhân trong microgrid, phân tách bài toán một cách hiệu quả giúp tăng tốc độ hội tụ và giảm thiểu overhead trao đổi dữ liệu.
  - `Yang_2024`: Đề xuất phương pháp ATC giải quyết bài toán vận hành mạng lưới phân phối chủ động và CCHP microgrid, vượt trội về khả năng xử lý bài toán phi tuyến phân cấp.

## 3. Dùng cho SUB-THEME 3: Lăng kính Thời gian & Sức chống chịu (MPC)

### Luận điểm 1: Sự thất bại của Tối ưu hóa Tĩnh (The Failure of Static Optimization)
- **Luận điểm:** Tối ưu hóa tĩnh (Static Optimization) hoặc điều độ thuần túy trước một ngày (pure day-ahead dispatch) thường dựa trên các dự báo tất định. Cách tiếp cận này bộc lộ sai số chết người và tính kém an toàn khi đối mặt với các sự kiện cực đoan bất ngờ (extreme events/blackouts) hoặc sai số dự báo thời gian thực. Việc chỉ dựa vào một bản chụp (single static snapshot) dẫn đến vi phạm nghiêm trọng các ràng buộc vật lý, rã lưới hoặc sụp đổ toàn bộ hệ thống (grid collapse).
- **Trích dẫn (Criticism):** `\cite{Liu2020Robust, Huynh2024Water, Zhang2020Day, Hou2023Day, Hussain2020Resilient}`
- **Tóm tắt hỗ trợ:**
  - `Liu2020Robust`: Phê phán mô hình day-ahead tĩnh dù có dùng robust optimization đi nữa vẫn không đủ linh hoạt trong thời gian thực, dẫn đến kết quả phân bổ năng lượng bảo thủ và dễ tổn thương nếu biến động nằm ngoài khoảng uncertainty set.
  - `Huynh2024Water`: Cho thấy việc chỉ dùng dữ liệu dự báo day-ahead tĩnh dẫn đến vi phạm đáng kể các ràng buộc và chi phí phạt (penalty costs) tăng vọt khi phụ tải thực tế thay đổi mạnh bất thường.
  - `Zhang2020Day` & `Hou2023Day`: Phân tích sự thiếu hụt của mô hình đa mục tiêu trước một ngày khi không có vòng lặp cập nhật liên tục (continuous update loop), làm sụt giảm độ tin cậy của microgrid.
  - `Hussain2020Resilient`: Chỉ ra rằng khi các microgrid gặp gián đoạn đột ngột (islanding events) khỏi lưới chính, các chiến lược tĩnh hoàn toàn thất bại trong việc cân bằng công suất nội bộ, gây sụp đổ hệ thống.

### Luận điểm 2: Khoảng trống của Tối ưu hóa Ngẫu nhiên & Bền vững (The Pitfalls of Stochastic & Robust Optimization)
- **Luận điểm:** Để khắc phục nhược điểm của tối ưu hóa tĩnh, Tối ưu hóa Ngẫu nhiên (Stochastic Optimization - SO) và Tối ưu hóa Bền vững (Robust Optimization - RO) là hai phương pháp tiêu chuẩn. Tuy nhiên, SO bộc lộ điểm yếu chí mạng là phụ thuộc hoàn toàn vào hàm mật độ xác suất (PDFs) chính xác, điều gần như bất khả thi khi đối phó với các sự kiện "Thiên nga đen" (Black Swan) hoặc thời tiết cực đoan. Ngược lại, RO giải quyết sự vô định bằng các tập bất định (uncertainty sets) và tối ưu cho kịch bản tồi tệ nhất (worst-case), khiến mô hình trở nên cực kỳ bảo thủ (conservative), gây lãng phí kinh tế và dẫn đến khối lượng tính toán khổng lồ không thể giải quyết được (intractable).
- **Trích dẫn (Criticism):** `\cite{Wang2020DRO, Hussain2021Resilience, Zhang2020Adaptive, Chen2022Robust, Liu2021Distributionally}`
- **Tóm tắt hỗ trợ:**
  - `Wang2020DRO`: Phê phán Tối ưu hóa ngẫu nhiên (SO) truyền thống vì yêu cầu phải biết chính xác phân phối xác suất (PDF) của các biến năng lượng tái tạo, dẫn đến sai lệch nghiêm trọng khi dữ liệu lịch sử không phản ánh đúng tương lai.
  - `Hussain2021Resilience`: Nhấn mạnh rằng đối với các sự kiện thời tiết cực đoan, các mô hình dựa trên PDF như SO hoàn toàn bất lực vì chúng không thể nắm bắt được xác suất của các rủi ro có đuôi phân phối dày (fat-tail risks).
  - `Zhang2020Adaptive`: Phân tích sự bảo thủ (conservatism) của Tối ưu hóa bền vững (RO). Khi liên tục chuẩn bị cho kịch bản tồi tệ nhất (worst-case), RO bắt buộc hệ thống dự trữ năng lượng quá mức, đánh đổi sự an toàn bằng chi phí vận hành cực kỳ đắt đỏ.
  - `Chen2022Robust`: Chỉ ra rằng mô hình RO hai giai đoạn (two-stage) cho microgrid thường tạo ra các bài toán min-max-min, dẫn đến sự bùng nổ độ phức tạp và bất khả thi về mặt tính toán (intractable) khi áp dụng trong thực tế.
  - `Liu2021Distributionally`: Kết luận rằng sự kém chính xác của SO và tính bảo thủ của RO là động lực để chuyển sang các cách tiếp cận kết hợp (như DRO) hoặc điều khiển liên tục (như MPC) nhằm bù đắp điểm yếu của nhau.

### Luận điểm 3: Giải pháp MPC - Chân trời cuốn và Sức chống chịu (The MPC Solution - Rolling Horizon & Resilience)
- **Luận điểm:** Điều khiển dự báo mô hình (Model Predictive Control - MPC) sử dụng cơ chế "Chân trời cuốn" (Rolling Horizon / Sliding Window). Cơ chế này liên tục tính toán lại (continuous re-optimization) và cập nhật dữ liệu dự báo mới nhất ở mỗi bước thời gian. Nhờ đó, Microgrid đạt được trạng thái "Suy thoái êm ái" (Graceful Degradation), tự động sa thải tải ưu tiên kém để bảo vệ các phụ tải trọng yếu, cực tiểu hóa Giá trị tổn thất phụ tải (Value of Lost Load - VoLL) và sống sót qua các đợt mất điện diện rộng.
- **Trích dẫn (Solution):** `\cite{Elkazaz2020Energy, Ghosh2021Impact, Wei2023Novel, Qiu2021Microgrid, Solanki2020Smart}`
- **Tóm tắt hỗ trợ:**
  - `Elkazaz2020Energy`: Chứng minh cơ chế rolling horizon của MPC cho phép cập nhật liên tục sai số dự báo tải và nguồn tái tạo, điều chỉnh SoC của BESS một cách linh hoạt, giữ cho microgrid không bị quá tải.
  - `Ghosh2021Impact`: Đánh giá tác động của chiến lược tối ưu cuốn (rolling optimization) trong các sự kiện cực đoan, giúp chủ động cắt giảm tải không thiết yếu (proactive load shedding) để duy trì sự sống cho các node quan trọng (giảm thiểu VoLL).
  - `Qiu2021Microgrid`: Tích hợp Robust Optimization vào MPC, sử dụng cửa sổ cuốn (sliding window) để tái tối ưu hóa, đảm bảo sự cân bằng và bảo vệ hệ thống khỏi vi phạm giới hạn kỹ thuật trong điều kiện nhiễu loạn cao.
  - `Solanki2020Smart`: Sử dụng MPC cho phụ tải thông minh (smart loads) thời gian thực. Khẳng định cơ chế rolling horizon giúp giảm thiểu hàm phạt VoLL cực kỳ hiệu quả thông qua việc tái lập kế hoạch đáp ứng nhu cầu sau mỗi khoảng thời gian cực ngắn.
  - `Wei2023Novel`: Đưa ra chứng minh toán học về sự hội tụ và khả năng thích ứng tức thời của rolling-horizon trong MPC, giải quyết bài toán biến động thông số phi tuyến mà điều độ tĩnh không làm được.

---
**Ghi chú Constraint:** Dù `chapter2.tex` cũ có nhắc đến việc "Co-optimization of P and Q", ta sẽ LỌC BỎ phần nói về "giao dịch Q" (Trading Q) dựa theo lệnh của Tư lệnh. $Q$ sẽ chỉ được đề cập dưới góc độ vật lý để duy trì ổn định áp (SOCP constraint) bên trong MG, không xuất hiện ở hàm mục tiêu P2P Trading.

## 4. DEFENSE MATRIX: Phản biện 3 Lỗ hổng Logic (Cập nhật 2026)

### Lỗ hổng 1: SOCP Exactness & Inverter Capacity ($S_{max}$)
- **Phản biện:** Việc nới lỏng SOCP (SOCP Relaxation) được chứng minh toán học là **exact (chính xác tuyệt đối)** khi áp dụng trên các mạng phân phối hình tia (radial topology). Việc bỏ qua Q trong giao dịch P2P là hợp lý vì lưới phân phối thường có biến tần phân tán cung cấp hỗ trợ Q tại chỗ như một dịch vụ phụ trợ (ancillary service), và với dung lượng định mức $S_{max}$, khi ưu tiên giao dịch $P$, phần công suất phản kháng $Q$ vẫn nằm trong giới hạn $S_{max}^2 \ge P^2 + Q^2$.
- **Trích dẫn (Support):** `\cite{Montoya2021Mixed, Angle2020SOCP}` (SOCP exactness trong radial networks), `\cite{Inverter2021Review}` (Hỗ trợ Q của Inverter).

### Lỗ hổng 2: ATC vs ADMM (Vertical vs Horizontal Consensus)
- **Phản biện:** Domain Reviewer cho rằng ADMM ưu việt hơn là không chính xác trong bối cảnh lưới điện đa cấp. Trong các bài toán tối ưu phi tuyến nhiều tầng (như giữa Lưới phân phối và các Microgrids), ADMM theo dạng hội tụ phẳng (horizontal/flat consensus) gặp khó khăn lớn về thời gian giải và thường xuyên dao động. Ngược lại, ATC (Analytical Target Cascading) theo mô hình phân cấp từ trên xuống (master-slave/vertical) kiểm soát chặt chẽ thông điệp trao đổi giữa các tầng, giúp hội tụ nhanh và ổn định hơn với các ràng buộc phi tuyến.
- **Trích dẫn (Support):** `\cite{MultiMG2021Architecture}` (Kiến trúc phân cấp và lên lịch), và các tài liệu liên quan đến điều khiển đa Microgrid.

### Lỗ hổng 3: MPC + ATC Real-Time Feasibility (Warm-start)
- **Phản biện:** Việc áp dụng kết hợp MPC và các thuật toán tối ưu phân cấp (như ATC) hoàn toàn khả thi trong thời gian thực (Real-Time Feasibility). Thay vì giải bài toán từ đầu ở mỗi bước thời gian, mô hình MPC tái sử dụng kết quả từ chu kỳ ngay trước đó làm "điểm khởi tạo ấm" (Warm-start). Việc này kết hợp với giới hạn số lần lặp (limited iterations) của ATC đảm bảo tính toán xong trước khi chu kỳ điều khiển tiếp theo diễn ra, chống lại sự sụp đổ hệ thống.
- **Trích dẫn (Support):** `\cite{RobustMPC2022ATC, MPC2023Review}` (Distributed Robust MPC và tính khả thi trong thời gian thực).

## 5. BỌC THÉP PHƯƠNG TRÌNH TOÁN HỌC (Cập nhật Giai đoạn 2)
Danh sách 5 bài báo Q1 (IEEE/Elsevier) được bổ sung để bảo vệ tuyệt đối các phương trình cốt lõi trong luận văn:

### 5.1. Định giá Biên nút (LMP) & Điều kiện KKT (Chapter 5)
- **Luận điểm:** Khi xảy ra nghẽn mạch trên đường dây liên kết, giá trị thỏa hiệp $\lambda$ giữa các Microgrid sẽ bị tách rời khỏi giá LMP nội bộ. Mối quan hệ toán học được xác định chặt chẽ bởi điều kiện KKT là $\lambda = LMP_{deficit} - \mu$, với $\mu$ là giá trị bóng (shadow price) của nghẽn mạch.
- **Trích dẫn:** `\cite{Ullah2022_LMP}` (Applied Energy, 2022).

### 5.2. Hàm Phạt Giữ Dung Lượng Pin (Terminal SOC Penalty) (Chapter 4)
- **Luận điểm:** Để hệ thống có thể chống chọi qua các giai đoạn sự cố kéo dài (Graceful Degradation), thuật toán MPC phải tích hợp hàm phạt Terminal SOC ($J_{SOC}$) ở cuối mỗi chân trời cuốn để ngăn việc BESS bị xả kiệt hoàn toàn.
- **Trích dẫn:** `\cite{Palangari2025_MPC}` (IEEE Transactions on Transportation Electrification, 2025).

### 5.3. Giá Trị Tổn Thất Phụ Tải (VOLL) & Phân Cấp Tải (Chapter 2 & 4)
- **Luận điểm:** Việc thiết lập hệ số VOLL cao khổng lồ (với $C_{shed}^{critical} \gg C_{shed}^{normal}$) trong hàm mục tiêu là yếu tố tiên quyết để hệ thống ưu tiên hi sinh tải thường, bảo vệ tuyệt đối tải quan trọng khi tách đảo khẩn cấp.
- **Trích dẫn:** `\cite{Hamilton2023_VOLL}` (IEEE PECI, 2023).

### 5.4. Tự Động Tinh Chỉnh Tham Số Phạt (Adaptive $\rho$) (Chapter 3)
- **Luận điểm:** Trong điều phối phân tán (như ATC/ADMM), việc cập nhật linh hoạt tham số phạt $\rho$ dựa trên sự cân bằng giữa thặng dư nguyên thủy và đối ngẫu ($r$ và $s$) là chìa khóa để tăng tốc hội tụ và ổn định vòng lặp.
- **Trích dẫn:** `\cite{Mavromatis2021_AdaptiveRho}` (IEEE Transactions on Power Systems, 2021).

### 5.5. Ràng Buộc Vận Hành Toàn Diện Phần Cứng Microgrid (Chapter 2)
- **Luận điểm:** Các phương trình giới hạn công suất cho Máy phát (DG), Pin lưu trữ (BESS), Năng lượng tái tạo (RE), và cơ chế cắt tải (Load Shedding) trong môi trường AC-OPF.
- **Trích dẫn:** `\cite{Nakiganda2023_Microgrid}` (IEEE Transactions on Power Systems, 2023).

### 5.6. Mô Hình Trào Lưu Công Suất Nhánh (DistFlow) (Chapter 2)
- **Luận điểm:** Xây dựng hệ phương trình sụt áp và cân bằng công suất P-Q chính xác cho lưới phân phối hình tia (radial distribution networks).
- **Trích dẫn:** `\cite{Chowdhury2023_SOCP_ThreePhase}` (IEEE Transactions on Smart Grid, 2023).

### 5.7. Nới Lỏng Nón Bậc Hai (SOCP Relaxation) (Chapter 2)
- **Luận điểm:** Chứng minh toán học cho việc chuyển đổi bài toán phi tuyến AC-OPF thành dạng lồi (convex) bằng nới lỏng nón bậc hai, đảm bảo tìm được nghiệm tối ưu toàn cục.
- **Trích dẫn:** `\cite{Chowdhury2025_SOCP_Coopt}` (IEEE Transactions on Industry Applications, 2025).

### 5.8. Hàm Phạt Mục Tiêu Phân Tán (ATC Augmented Lagrangian) (Chapter 3)
- **Luận điểm:** Thiết lập hàm mục tiêu cục bộ bằng cách áp dụng phương pháp nhân tử Lagrange tăng cường (Augmented Lagrangian) để ép các Microgrid tuân thủ thỏa hiệp giao dịch năng lượng với lưới chính.
- **Trích dẫn:** `\cite{ATC_Coopt_2025}` (Wang et al., IEEE Transactions on Power Systems, 2025).

### 5.9. Cơ Chế Chân Trời Cuốn Trong MPC (Rolling Horizon) (Chapter 4)
- **Luận điểm:** Sử dụng cửa sổ dự báo cuốn liên tục trong thời gian thực để tái tối ưu hóa lịch trình năng lượng và cập nhật trạng thái SOC của BESS, phản ứng tức thì với các sự cố bất ngờ.
- **Trích dẫn:** `\cite{Hermans2024_MPC}` (Applied Energy, 2024).
