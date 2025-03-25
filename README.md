# Hệ Thống Gợi Ý Phim (Movie Recommender System)
Đây là một hệ thống gợi ý phim sử dụng dữ liệu từ Kaggle để đưa ra danh sách phim tương tự dựa trên nội dung. Sử dụng Machine Learning 

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
<p align="center">
  <img src=https://github.com/trgtanhh04/Movie-Recommendation-System/blob/main/demo/img1.png width="48%" alt="Dashboard">
  <img src=https://github.com/trgtanhh04/Movie-Recommendation-System/blob/main/demo/img2.png width="48%" alt="Dashboard">
</p>

##  Cài Đặt và Chạy Dự Án

1. **Clone repo về máy:**  
   ```bash
   git clone <repo-link>
   ```

2. **Cài đặt các thư viện cần thiết:**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Chạy ứng dụng:**  
   ```bash
   python app.py
   ```

## Tính Năng Chính
Gợi ý phim dựa trên nội dung  
Sử dụng dữ liệu TMDB  
API xây dựng bằng Flask  

## Thông Tin Khác
- **Ngôn ngữ:** Python
- **Thư viện chính:** Pandas, Flask, Scikit-Learn
- **Dữ liệu:** TMDB Movies Dataset

---


