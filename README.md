# Hệ Thống Gợi Ý Phim (Movie Recommender System)
Đây là một hệ thống gợi ý phim sử dụng dữ liệu từ TMDB để đưa ra danh sách phim tương tự dựa trên nội dung.

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
💡 *Hãy đóng góp nếu bạn có ý tưởng cải tiến hệ thống!*

