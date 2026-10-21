# App del TP: recibe el texto de una noticia y muestra las personas, lugares y organizaciones que detecta el modelo.

import streamlit as st  # librería que arma la página web
from transformers import pipeline  # herramienta que carga y usa el modelo ya entrenado

NOMBRES = {"PER": "Persona", "LOC": "Lugar", "ORG": "Organización", "MISC": "Otro"}  # nombres legibles para cada tipo de entidad

@st.cache_resource  # guarda el modelo en memoria para no volver a cargarlo en cada clic
def cargar_modelo():  # función que arma el extractor una sola vez
    return pipeline("ner", model="Babelscape/wikineural-multilingual-ner", aggregation_strategy="simple")  # carga el modelo desde Hugging Face

st.title("Extractor de entidades en noticias")  # título de la página
st.write("Pegá el texto de una noticia en español y la app marca personas, lugares y organizaciones.")  # explicación para quien la usa

texto = st.text_area("Texto de la noticia", height=200)  # caja donde se pega la noticia

if st.button("Analizar"):  # cuando se hace clic en el botón
    if not texto.strip():  # si la caja está vacía
        st.warning("Escribí o pegá un texto primero.")  # avisa que falta el texto
    else:  # si hay texto
        ner = cargar_modelo()  # obtiene el modelo (la primera vez tarda)
        resultado = ner(texto)  # analiza el texto: esto es la inferencia
        if not resultado:  # si el modelo no encontró nada
            st.info("No se detectó ninguna entidad.")  # lo informa
        for e in resultado:  # recorre cada entidad detectada
            st.write(f"{NOMBRES.get(e['entity_group'], e['entity_group'])}: {e['word']} ({e['score']:.2f})")  # muestra tipo, texto y seguridad
