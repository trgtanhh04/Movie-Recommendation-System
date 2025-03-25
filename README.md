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

