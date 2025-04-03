# Hệ Thống Gợi Ý Phim (Movie Recommender System)
Đây là một hệ thống gợi ý phim sử dụng dữ liệu từ Kaggle để đưa ra danh sách phim tương tự dựa trên nội dung. Sử dụng Machine Learning 

**Các loại hệ thống gợi ý**
-  Hệ thống dựa trên nội dung (Content-Based)
-  Hệ thống lọc cộng tác (Collaborative Filtering)
-  Hệ thống kết hợp (Hybrid-Based)

## Cấu Trúc Dự Án
```
MOVIE RECOMMENDER SYSTEM  
 |- data  
 | |- tmdb_5000_credits.csv  
 | |_tmdb_5000_movies.csv  
 |-  demo  
 | |- img1.png  
 | |_ img2.png  
 |- pickle  
 | |-  movie_list.pkl  
 | |_  similarity.pkl  
 |- setup  
 | |- setup.py  
 | |_ setup.sh  
 |- .gitattributes  
 |- .gitignore  
 |- app.py  
 |- demo.py  
 |- movie_recommendation.ipynb  
 |- Procfile  
 |- recommendation.py  
 |_ requirements.txt  
```

## Demo dự án
Đây là một ứng dụng web sử dụng Streamlit để gợi ý phim dựa trên sở thích của người dùng. Hệ thống có thể đề xuất các bộ phim tương tự bằng cách sử dụng thuật toán Cosine Similarity.

Mô hình hoạt động:
- Hệ thống chuyển đổi thông tin phim thành vector.

- Tính toán mức độ tương đồng giữa các phim bằng Cosine Similarity.

- Xuất ra danh sách phim tương tự với phim mà người dùng quan tâm.
<p align="center">
  <img src=https://github.com/trgtanhh04/Movie-Recommendation-System/blob/main/demo/img1.png width="48%" alt="Dashboard">
  <img src=https://github.com/trgtanhh04/Movie-Recommendation-System/blob/main/demo/img2.png width="48%" alt="Dashboard">
</p>

---
## Dữ liệu sử dụng

**Bộ dữ liệu:** [TMDB 5000 Movies Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata)

Thuật toán sử dụng:

-  Cosine Similarity: Một phương pháp đo độ tương đồng giữa hai vector.
-  Nếu giá trị là 0, hai phim hoàn toàn khác nhau.
-  Nếu giá trị là 1, hai phim hoàn toàn giống nhau.
-  Để biết thêm chi tiết, tham khảo: Cosine Similarity

**Cosine Similarity** là một độ đo khoảng cách giữa hai vector trong không gian nhiều chiều, thường được sử dụng để đánh giá mức độ tương đồng giữa hai tập dữ liệu. Công thức tính như sau:
```
\[
\text{Cosine Similarity} = \frac{A \cdot B}{\|A\| \times \|B\|}
\]
```

Trong đó:
- \( A \) và \( B \) là hai vector đặc trưng của hai bộ phim.
- \( A \cdot B \) là tích vô hướng giữa hai vector.
- \( \|A\| \) và \( \|B\| \) là độ dài (norm) của hai vector.

Giá trị Cosine Similarity dao động từ -1 đến 1:
- **1**: Hai bộ phim giống nhau hoàn toàn.
- **0**: Hai bộ phim không liên quan.
- **-1**: Hai bộ phim hoàn toàn trái ngược nhau.

---
## Cách chạy dự án
### Các bước thực hiện:
**1. Clone repository:**
```bash
https://github.com/your-repo/Movie-Recommender-System.git
```

**2. Tạo môi trường conda:**
```bash
conda create -n movie python=3.7.10 -y
conda activate movie
```

**3. Cài đặt các thư viện cần thiết:**
```bash
pip install -r requirements.txt
```

**4. Chạy mô hình và sinh file dữ liệu:**
```bash
python movie_recommendation.ipynb  
```

**5. Chạy ứng dụng Streamlit:**
```bash
streamlit run app.py
```
---

# So sánh ba mô hình Machine Learning

## 1. Giới thiệu
Dự án này nhằm so sánh ba mô hình Machine Learning: Logistic Regression, Random Forest và XGBoost. Mục tiêu là đánh giá hiệu suất và chọn ra mô hình tốt nhất dành cho bài toán dự báo.

## 2. Mô hình so sánh

### 2.1 Logistic Regression
- Là một mô hình tháng tuyến đơn giản, dễ hiểu và dễ triển khai.
- Thích hợp với các bài toán dự báo nhị phân.
- Hiệu suất không cao khi dữ liệu phức tạp và không tuyến tính.

### 2.2 Random Forest
- Là mô hình tập hợp cây quyết định, giảm overfitting so với cây quyết định đơn lẻ.
- Không yêu cầu nhiều xử lý dữ liệu, hoạt động tốt trên tập dữ liệu lớn.
- Hiệu suất tốt nhưng có thể chậm hơn so với các mô hình khác.

### 2.3 XGBoost
- Là mô hình boosting dựa trên cây quyết định, tối ưu hóa tốc độ và hiệu suất.
- Xử lý tốt các dữ liệu phức tạp, giảm thiểu overfitting.
- Thường được dùng trong các cuộc thi Machine Learning nhờ hiệu suất vượt trội.
