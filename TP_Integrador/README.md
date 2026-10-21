# TP Integrador: extractor de entidades en noticias

Aplicación web desarrollada con Streamlit para identificar entidades nombradas en textos periodísticos en español. La app analiza un texto ingresado por el usuario y detecta entidades como personas, lugares y organizaciones utilizando un modelo preentrenado de Hugging Face.

## Descripción del proyecto

El objetivo del proyecto es facilitar la extracción de información relevante desde noticias o artículos. A partir de un texto cualquiera, la aplicación aplica un modelo de reconocimiento de entidades nombradas (NER) y devuelve las entidades encontradas junto con una estimación de confianza.

La solución usa:

- Python
- Streamlit para la interfaz web
- Transformers para la inferencia del modelo
- PyTorch en versión CPU
- Modelo: `Babelscape/wikineural-multilingual-ner`

## Funcionalidades

- Ingreso de texto libre en una caja de edición
- Detección automática de entidades en español
- Clasificación por tipo de entidad:
  - Persona
  - Lugar
  - Organización
  - Otros
- Visualización del texto detectado y su puntaje de confianza
- Carga del modelo cacheada para evitar recargas repetidas

## Requisitos

- Python 3.10 o superior
- pip actualizado
- Conexión a internet para descargar el modelo desde Hugging Face
- CPU compatible con PyTorch (no se requiere GPU)

## Instalación

1. Clonar el repositorio o descargar la carpeta del proyecto.
2. Crear un entorno virtual:

```bash
python -m venv .venv
```

3. Activar el entorno virtual:

En Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

En Linux/macOS:

```bash
source .venv/bin/activate
```

4. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

Desde la raíz del proyecto, ejecutar:

```bash
streamlit run app.py
```

Luego abrir la URL que indique Streamlit, normalmente:

```text
http://localhost:8501
```

## Uso

1. Pegá o escribí el texto de una noticia en la caja de texto.
2. Hacé clic en el botón `Analizar`.
3. La aplicación mostrará las entidades detectadas con su tipo y nivel de confianza.

## Estructura del proyecto

```text
TP_Integrador/
├── app.py               # Aplicación principal en Streamlit
├── README.md            # Documentación del proyecto
├── requirements.txt      # Dependencias del proyecto
├── notebook.ipynb       # Notebook de exploración o pruebas
└── .venv/               # Entorno virtual (si se crea localmente)
```

## Nota importante

La primera vez que se ejecuta la app, puede tardar unos segundos en descargar el modelo de IA desde Hugging Face. Luego, la carga queda en caché y la aplicación responde más rápido.

## Autoría

Proyecto académico del Seminario de Actualización · IFTS N.º 18 · 2026.
