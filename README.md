# Hệ Thống Gợi Ý Phim (Movie Recommender System)

Đây là một hệ thống gợi ý phim sử dụng dữ liệu từ Kaggle để đưa ra danh sách phim tương tự dựa trên nội dung. Hệ thống áp dụng các thuật toán Machine Learning để cải thiện trải nghiệm người dùng.

---

## Các loại hệ thống gợi ý
- **Hệ thống dựa trên nội dung (Content-Based):** Đề xuất dựa trên các đặc điểm của phim.
- **Hệ thống lọc cộng tác (Collaborative Filtering):** Đề xuất dựa trên hành vi và sở thích của người dùng.
- **Hệ thống kết hợp (Hybrid-Based):** Kết hợp cả hai phương pháp trên để tăng độ chính xác.

---

## Cấu Trúc Dự Án
```
MOVIE RECOMMENDER SYSTEM  
 ├── data  
 │   ├── tmdb_5000_credits.csv  
 │   └── tmdb_5000_movies.csv  
 ├── demo  
 │   ├── img1.png  
 │   └── img2.png  
 ├── pickle  
 │   ├── movie_list.pkl  
 ├── setup  
 │   ├── setup.py  
 │   └── setup.sh  
 ├── app.py  
 ├── demo.py  
 ├── movie_recommendation.ipynb  
 ├── recommendation.py  
 └── requirements.txt  
```

---

## Demo Dự Án
Đây là một ứng dụng web sử dụng **Streamlit** để gợi ý phim dựa trên sở thích của người dùng. Hệ thống có thể đề xuất các bộ phim tương tự bằng cách sử dụng thuật toán **Cosine Similarity**.

### Mô Hình Hoạt Động:
1. Hệ thống chuyển đổi thông tin phim thành vector đặc trưng.
2. Tính toán mức độ tương đồng giữa các phim bằng **Cosine Similarity**.
3. Xuất ra danh sách các phim tương tự với phim mà người dùng quan tâm.

<p align="center">
  <img src="https://github.com/trgtanhh04/Movie-Recommendation-System/blob/main/demo/img1.png" width="48%" alt="Dashboard">
  <img src="https://github.com/trgtanhh04/Movie-Recommendation-System/blob/main/demo/img2.png" width="48%" alt="Dashboard">
</p>

---

## Dữ Liệu Sử Dụng

**Bộ dữ liệu:** [TMDB 5000 Movies Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata)

### Thuật Toán Sử Dụng:
- **Cosine Similarity:** Một phương pháp đo độ tương đồng giữa hai vector.
  - Nếu giá trị là **0**, hai phim hoàn toàn khác nhau.
  - Nếu giá trị là **1**, hai phim hoàn toàn giống nhau.

**Công thức tính Cosine Similarity:**

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*dGWOzgAYv9NUkWvkETQUTQ.png" width="60%" alt="Cosine Similarity Formula">
</p>

- Trong đó:
  - \( A \) và \( B \) là hai vector đặc trưng của hai bộ phim.
  - \( A \cdot B \) là tích vô hướng giữa hai vector.
  - \( \|A\| \) và \( \|B\| \) là độ dài (norm) của hai vector.

- **Giá trị Cosine Similarity dao động từ -1 đến 1:**
  - **1:** Hai bộ phim giống nhau hoàn toàn.
  - **0:** Hai bộ phim không liên quan.
  - **-1:** Hai bộ phim hoàn toàn trái ngược nhau.

---

## Cách Chạy Dự Án

### Các Bước Thực Hiện:

**1. Clone repository:**
```bash
git clone https://github.com/your-repo/Movie-Recommender-System.git
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

## Đóng Góp
Mọi đóng góp để cải thiện dự án đều được chào đón! Vui lòng fork repository này và gửi một pull request.

---
