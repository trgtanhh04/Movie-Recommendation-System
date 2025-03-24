import pickle
import requests

# Load dữ liệu
movies = pickle.load(open('pickle/movie_list.pkl', 'rb'))
similarity = pickle.load(open('pickle/similarity.pkl', 'rb'))

def fetch_poster(movie_id):
    """Lấy ảnh poster phim từ API TMDB."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    response = requests.get(url).json()
    return f"https://image.tmdb.org/t/p/w500/{response['poster_path']}"

def recommend(movie_name):
    """Gợi ý phim dựa trên độ tương đồng."""
    if movie_name not in movies['title'].values:
        return [], []
    
    index = movies[movies['title'] == movie_name].index[0]
    distances = sorted(enumerate(similarity[index]), key=lambda x: x[1], reverse=True)
    
    recommended_names = []
    recommended_posters = []
    
    for i in distances[1:6]:  # Lấy 5 phim tương tự
        movie_id = movies.iloc[i[0]]['movie_id']
        recommended_names.append(movies.iloc[i[0]]['title'])
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_names, recommended_posters
