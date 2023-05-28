import streamlit as st
import pandas as pd
import numpy as np
import altair as ait
import matplotlib.pyplot as plt

st.title("Streamlit File uploader")

@st.cache(suppress_st_warning=True)
def load(Data):
    return pd.read_csv(Data)




uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    Df = load(uploaded_file)
    if uploaded_file is not None:
        st.write(Df.describe())
        st.success('Votre fichier est bien téléchargé, vous pouvez observer tous les détails statistiques')
else:
    st.warning('Vous devez importer votre fichier pour visualiser vos données')

Choice = ['Analyse bivariée','Analyse univariée']
st.sidebar.selectbox('Votre analyse',Choice)
Col1, Col2 = st.columns(2)
with Col1:
    if Choice == 'Analyse univariée':
        col = st.selectbox('Choisisez votre colonne',Df.columns)
        chart = ait.chart(Df).mark_bar().encode(
            x=col,
            y='count()',
        ).interactive()
        st.altair_chart(chart,use_container_width=True)