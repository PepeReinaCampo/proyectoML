import os
import random
import numpy as np
import tensorflow as tf
import cv2
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

# Diccionario de emociones
emotions = {0: 'Enfado', 1: 'Asco', 2: 'Miedo', 3: 'Felicidad', 4: 'Tristeza', 5: 'Sorpresa', 6: 'Neutral'}

# Tabla de sustancias por administrar según emoción detectada y adecuada
sustancias_por_administrar = {
    ('Neutral', 'Neutral'): 'POSTPLACEBO',
    ('Neutral', 'Enfado'): 'DIMETOVELOCETINA-BUTIL',
    ('Neutral', 'Asco'): 'CLOROCHOLEXSINA',
    ('Neutral', 'Miedo'): 'DIMETIL-NEPTODEXTROXIDO',
    ('Neutral', 'Felicidad'): 'LIQUALENSINA',
    ('Neutral', 'Tristeza'): 'OXSOMA-BUTIL',
    ('Neutral', 'Sorpresa'): '2-10-EMEDIOXINA',
    ('Enfado', 'Neutral'): 'NEUTROLINOXONA',
    ('Enfado', 'Enfado'): 'POSTPLACEBO',
    ('Enfado', 'Asco'): 'METACHOLEXSINA',
    ('Enfado', 'Miedo'): 'FEAREANEFRINA',
    ('Enfado', 'Felicidad'): 'OXITOACERVEXINA',
    ('Enfado', 'Tristeza'): 'CLOROMETANOXIFINAFLUORIDA',
    ('Enfado', 'Sorpresa'): '2-10-EMEDIOXINA',
    ('Asco', 'Neutral'): 'NEUTROLINOXONA',
    ('Asco', 'Enfado'): 'SYNTHEISITISEINA',
    ('Asco', 'Asco'): 'POSTPLACEBO',
    ('Asco', 'Miedo'): 'FEAREANEFRINA',
    ('Asco', 'Felicidad'): 'LIQUALENSINA',
    ('Asco', 'Tristeza'): 'CLOROMETANOXIFINAFLUORIDA',
    ('Asco', 'Sorpresa'): '2-10-EMEDIOXINA',
    ('Miedo', 'Neutral'): 'NEUTROLINOXONA',
    ('Miedo', 'Enfado'): 'KOROBININA',
    ('Miedo', 'Asco'): 'METACHOLEXSINA',
    ('Miedo', 'Miedo'): 'POSTPLACEBO',
    ('Miedo', 'Felicidad'): 'LIQUALENSINA',
    ('Miedo', 'Tristeza'): 'OXSOMA-BUTIL',
    ('Miedo', 'Sorpresa'): '2-10-EMEDIOXINA',
    ('Felicidad', 'Neutral'): 'NEUTROLINOXONA',
    ('Felicidad', 'Enfado'): 'IRAXCITUR',
    ('Felicidad', 'Asco'): 'CLOROCHOLEXSINA',
    ('Felicidad', 'Miedo'): 'FEAREANEFRINA',
    ('Felicidad', 'Felicidad'): 'POSTPLACEBO',
    ('Felicidad', 'Tristeza'): 'OXSOMA-BUTIL',
    ('Felicidad', 'Sorpresa'): '2-10-EMEDIOXINA',
    ('Tristeza', 'Neutral'): 'NEUTROLINOXONA',
    ('Tristeza', 'Enfado'): 'DIMETOVELOCETINA-BUTIL',
    ('Tristeza', 'Asco'): 'METACHOLEXSINA',
    ('Tristeza', 'Miedo'): 'DIMETIL-NEPTODEXTROXIDO',
    ('Tristeza', 'Felicidad'): 'OXITOACERVEXINA',
    ('Tristeza', 'Tristeza'): 'POSTPLACEBO',
    ('Tristeza', 'Sorpresa'): '2-10-EMEDIOXINA',
    ('Sorpresa', 'Neutral'): 'NEUTROLINOXONA',
    ('Sorpresa', 'Enfado'): 'SYNTHEISITISEINA',
    ('Sorpresa', 'Asco'): 'CLOROCHOLEXSINA',
    ('Sorpresa', 'Miedo'): 'IRAXCITURIOL-AMINA',
    ('Sorpresa', 'Felicidad'): 'OXITOACERVEXINA',
    ('Sorpresa', 'Tristeza'): 'OXSOMA-BUTIL',
    ('Sorpresa', 'Sorpresa'): 'POSTPLACEBO',
} 

# Ruta del modelo
model_path = 'notebooks_y_mas/Modelos_entrenados/modelo_cnn.keras'
model = load_model(model_path)

def vigilante(emocion):
    # Seleccionar una imagen aleatoria de la carpeta
    image_folder = 'Imagenes_prueba_emociones'
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]
    selected_image = random.choice(image_files)
    image_path = os.path.join(image_folder, selected_image)

    # Cargar y preprocesar la imagen
    image = cv2.imread(image_path)
    image_resized = cv2.resize(image, (48, 48))  # Asumiendo que el modelo espera imágenes de 48x48
    image_gray = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)
    image_array = np.expand_dims(image_gray, axis=-1)
    image_array = np.expand_dims(image_array, axis=0)
    image_array = image_array / 255.0

    # Realizar la predicción
    predictions = model.predict(image_array)
    predicted_class = np.argmax(predictions)
    confidence = np.max(predictions)

    # Obtener nombre del archivo sin extensión
    subject_name = os.path.splitext(selected_image)[0]

    # Obtener la emoción detectada y adecuada
    emocion_detectada = emotions[predicted_class]
    emocion_adecuada = emotions[emocion]

    # Obtener la sustancia adecuada según la tabla
    sustancia_adecuada = sustancias_por_administrar[(emocion_detectada, emocion_adecuada)]

    # Mostrar la imagen original con los textos superpuestos 
    plt.figure(figsize=(8, 8))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(f"El sujeto se llama: {subject_name}\nLa expresión detectada es: {emocion_detectada}\nLa expresión adecuada es: {emocion_adecuada}\nSustancia adecuada: {sustancia_adecuada}\nLa confianza en la predicción es del: {confidence * 100:.2f}%")
    plt.axis('off')
    plt.show()
