import streamlit as st
import pickle
import requests

#Heading
st.title("Your Personalised Movie Recommendation System")
st.header('Wandering what to watch?')
#Importing Pickle File
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

#Getting DropDown for movies
movies_names = movies['title'].values
selected_movie = st.selectbox("Select the movie from list?",movies_names)

#Fetching Movie Poster for recommend func.
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=0ca0046afe533e5849a9835f251617be&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

#Returning recommended movie
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:8]:
        #fetch the movie poster
        id1 = movies.iloc[i[0]].id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(id1))
    return recommended_movie_names,recommended_movie_posters

#creating Button
if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

