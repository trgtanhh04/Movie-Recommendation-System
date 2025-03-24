import streamlit as st
from recommendation import recommend  # Đổi tên module

# Tiêu đề ứng dụng
st.title("Movie Recommendation System")

# Lấy danh sách phim
import pickle
movies = pickle.load(open('pickle/movie_list.pkl', 'rb'))
movie_list = movies['title'].values

# Chọn phim
selected_movie = st.selectbox("Enter name film:", movie_list)

# Nút hiển thị gợi ý
if st.button("Show recommendation"):
    recommended_names, recommended_posters = recommend(selected_movie)

    if recommended_names:
        cols = st.columns(5)  # Hiển thị 5 phim theo hàng ngang
        for i in range(5):
            with cols[i]:
                st.text(recommended_names[i])
                st.image(recommended_posters[i])
    else:
        st.error("Không tìm thấy phim trong danh sách!")
