import pickle
import pandas as pd

# Load dữ liệu
movies = pickle.load(open('pickle/movie_list.pkl', 'rb'))

# Kiểm tra danh sách cột
print("Các cột có trong movies:", movies.columns)
