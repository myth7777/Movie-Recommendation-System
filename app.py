import streamlit as st
import pickle 
import pandas as pd
import requests

def fetch_poster(movie_id):
     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=14b8dea609b01673874d693807e9267c&language=en-US'.format(movie_id))
     data = response.json()
     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
     
def recommend(movie):
        
        # if movie not in mov_list['title'].values: 
        #     st.error(f"Movie '{movie}' not found in the list.")
        #     return []

        mov_idx = mov_list[mov_list['title'] == movie].index[0]
        distances = similarity[mov_idx]
        movies_list = sorted(list(enumerate(distances)), reverse = True, key=lambda x:x[1])[1:6]

        recommend_movies_poster = []

        recommended_movies = []
        for i in movies_list:
            movie_id = mov_list.iloc[i[0]].id

            recommended_movies.append(mov_list.iloc[i[0]].title)
            
            #fetch poster from API
            recommend_movies_poster.append(fetch_poster(movie_id))

        return recommended_movies, recommend_movies_poster

movies_dict = pickle.load(open('movies.pkl', 'rb'))
mov_list = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected = st.selectbox("Which movie you want to watch?",mov_list['title'])

st.write("You selected:", selected)

if st.button("Get Recommendations", type="primary"):
    names,posters = recommend(selected)
    col1, col2, col3, col4, col5 = st.columns(5)

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