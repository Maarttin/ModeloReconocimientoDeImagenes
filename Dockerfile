# Usa una imagen base que tenga Python y TensorFlow
FROM python:3.9

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el código y el modelo al contenedor
COPY . /app

RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Instala las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto que usará la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

