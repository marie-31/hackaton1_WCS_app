import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import datetime
import time 




DATE_TIME = "date/time"
DATA_URL = (
"http://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"
)

'## Présentation de streamlit'
"""
Streamlit est un framework open-source spécialement conçu pour les ingénieurs en machine learning et les Data scientists.
Les données présentées sont les prises en charge Uber à New York
"""

@st.cache # Permet de mettre en cache et conserver les données une fois chargées => plus de performance après première exécution
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    data[DATE_TIME] = pd.to_datetime(data[DATE_TIME])
    return data

data = load_data(10000)
data

# Ajout du slider et affichage des données filtrées
hour = st.slider("Heure de la journée", 0, 23)
'### Heure sélectionnée' , hour
data = data[data[DATE_TIME].dt.hour == hour]
#data

hist = np.histogram(data[DATE_TIME].dt.minute, bins=60, range=(0, 60))[0]
'### Distribution des commandes par minute entre %i:00 et %i:00' % (hour, (hour + 1) % 24)
chart_data = pd.DataFrame({"minute": range(60), "pickups": hist})

st.altair_chart(alt.Chart(chart_data)
.mark_area(
interpolate='step-after',
).encode(
x=alt.X("minute:Q", scale=alt.Scale(nice=False)),
y=alt.Y("pickups:Q"),
tooltip=['minute', 'pickups']
), use_container_width=True)

# Saisie d'un texte
texte = st.text_input('Entrez un texte ')
if texte : 'Vous avez entré', texte



# Choisir une heure
timeOfTheDay= st.time_input("Choisir l'heure", datetime.time(8, 45,00))
'Heure:', timeOfTheDay



"Renseignez vos coordonnées GPS"
## Définir des coordonnées GPS
latitude= st.number_input("Choisir la latitude ", min_value=data['lat'].min(),max_value=data['lat'].max())
longitude= st.number_input("Choisir la longitude ", min_value=data['lon'].min(),max_value=data['lon'].max())
'Vos coordonnées GPS (latitude,longitude) : ', (latitude,longitude)


