import pandas as pd
import streamlit as st

import pickle

movies_dict =pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommender System')

option = st.selectbox(
'How would you like to be contacted?',
movies['title'].values)