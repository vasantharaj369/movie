import streamlit as st
import pickle
import requests

df = pickle.load(open('df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def fetch(movie_id):
  response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=5e3c045812562ead4c5c7c2630700256&language=en-US'.format(movie_id))
  data = response.json()
  return 'https://image.tmdb.org/t/p/w500' + data['poster_path']
def recomend(movie):
  movie_index = df[df['title'] == movie].index[0]
  distances = similarity[movie_index]
  movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x: x[1])[1:6]
  recommend_movies = []
  recommend_movies_posters = []
  for i in movies_list:
    movie_id = df.iloc[i[0]].movie_id
    recommend_movies.append(df.iloc[i[0]].title)
    recommend_movies_posters.append(fetch(movie_id))
  return recommend_movies, recommend_movies_posters


st.title('Movie Recommendation System')
movie_selected = st.selectbox('Enter the movie ', df['title'].unique())

if st.button('Recommend'):
  names, posters = recomend(movie_selected)
  col1, col2, col3, col4, col5= st.columns(5)
  with col1:
    st.text(names[0])
    st.image(posters[0])
  with col2:
    st.text(names[1])
    st.image(posters[1])
  with col3:
    st.text(names[2])
    st.image(posters[2])
  with col4:
    st.text(names[3])
    st.image(posters[3])
  with col5:
    st.text(names[4])
    st.image(posters[4])