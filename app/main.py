from fastapi import FastAPI, File, UploadFile
from PIL import Image
import io
import tensorflow as tf
import numpy as np

# Cargar el modelo
model = tf.keras.models.load_model('/app/my_trained_model.h5')

# Inicializar la aplicación FastAPI
app = FastAPI()

# Ruta para clasificar una imagen
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Leer la imagen
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data))

    # Preprocesar la imagen para el modelo (ajusta esto según las necesidades de tu modelo)
    image = image.resize((224, 224))  # Ajusta el tamaño según lo que tu modelo espera
    image = np.array(image) / 255.0   # Normalizar los valores de píxeles si es necesario
    image = np.expand_dims(image, axis=0)  # Añadir una dimensión extra para batch_size

    # Realizar la predicción
    predictions = model.predict(image)

    # Obtener la clase predicha (ajusta según la salida de tu modelo)
    predicted_class = np.argmax(predictions, axis=-1)

    class_map = {0: "caballo", 1: "vaca"}
    return {"predicted_class": class_map[predicted_class[0]]}


