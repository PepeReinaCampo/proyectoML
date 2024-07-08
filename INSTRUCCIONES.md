<img src="Imagenes/int.jpeg" alt="Imagen creada con inteligencia artificial." style="border-radius: 15px;">

*Imagen creada con inteligencia artificial.*


## **INSTRUCCIONES**

1. **Crea la carpeta:** Puedes llamarla como quieras, por ejemplo **"Proyecto ML"**.

2. **En la carpeta principal crea otra carpeta:** Llámala **"datos"**, dentro de "datos" crea otra carpeta que se llame **"fer2013"**. Descarga el dataset "fer2013" desde este [enlace](https://www.kaggle.com/datasets/nicolejyt/facialexpressionrecognition?select=fer2013.csv) y descomprímelo (dentro de la carpeta 'fer2013'). 
**¡OJO!** Es importate que el archivo se llame **fer2013.csv**

3. **Dentro de la carpeta 'fer2013':** Crea una carpeta que se llame **"dataframe_individuales"**. No necesitas guardar nada, el código lo hará.

4. **Descarga el notebook 'EDA_FER2013.ipynb':** Guárdalo en la carpeta principal (la que puede llamarse "Proyecto ML"). Si ya tenías el dataset "fer2013" descargado y las carpetas creadas, al correr 'EDA_FER2013' se crearán automáticamente 3 archivos y se guardarán en la carpeta "dataframe_individuales".  
>Si esto no pasa puede ser que no tengas las carpetas con los mismos nombres.

   **¡ESPERA, ESPERA....LO SÉ!... ¡NO SE VEN LAS IMÁGENES!**
   Aunque es algo opcional y no afecta al funcionamiento, es estético y hace que sea menos pesado. Descarga la carpeta **'Imagenes'**, guárdala en la carpeta principal. Ahora podrás ver las imágenes en los notebooks. 🤔 ¿Tienes curiosidad por saber qué prompts he utilizado para la creación de las imágenes? Pues están en el archivo **"PROMPTS.md"**. ¿Quién lo diría... ¿eh?

5. **Descarga el archivo "Data_augmentation_fer2013.ipynb":** Guárdalo en la carpeta principal, ejecútalo y en la carpeta "fer2013" aparecerá un archivo CSV llamado **"fer2013_blc"**. "Blc" significa balanceado, es el resultado de aplicar técnicas de data augmentation al dataset fer2013 original. 

6. **Crea una carpeta llamada 'AffectNet' dentro de 'datos':** Dentro de **'datos'**, crea una carpeta llamada **'AffectNet_original'**. Dentro de esta carpeta, descarga y descomprime el dataset que encontrarás en este [enlace](https://www.kaggle.com/datasets/noamsegal/affectnet-training-data). Se habrá creado una carpeta llamada **'archive'** que contiene varias carpetas y un archivo CSV.  
  
7. **Crea una carpeta llamada 'expresiones individuales'** dentro de la carpeta **'AffectNet'**. No necesitas guardar nada, el código lo hará.

8. Elimina el archivo **'labels.csv'** y la carpeta **'contempt'**. Las carpetas restantes son: **Neutral, Happiness, Sad, Surprise, Fear, Disgust y Anger**. Como puedes ver, coinciden con **'FER2013'**. Cambia manualmente el nombre de las carpetas siguiendo el siguiente diccionario: **Neutral → 6, Happiness → 3, Sad → 4, Surprise → 5, Fear → 2, Disgust → 1 y Anger → 0**.  
  
**9. Descarga el archivo 'Preparado_AffectNet.ipynb':** Deberás ir cambiando los nombres de los dataframes y alguna cosa más; está indicado donde debes cambiar. En la carpeta **'expresiones individuales'** irán apareciendo archivos CSV a medida que lo vayas corriendo. Cuando tengas los 7 archivos descomenta el apartado **CONCATENADO Y GUARDADO DE LOS DATASETS**. Ahora tienes un archivo CSV llamado **'df_AffectNet_formato'**, este estará en la carpeta **'AffectNet'**. Tendrá el mismo formato que **'FEr2013'**.  

**10. Descarga el archivo 'EDA_AffectNet.ipynb':** Correlo entero, si te interesa puedes echar un vistazo... Lo más importante es que ahora tendrás 3 datasets nuevos en la carpeta **"AffectNet"**




11. **Crea una carpeta llamada 'modelos_entrenados':** Aquí no tienes que guardar nada, solo esperar. Ni te imaginas lo que aparecerá aquí.

12. **Descarga el archivo "Modelos_expresiones.ipynb":** Ejecuta todo el notebook; tómate tu tiempo, tardará un rato. Está bastante explicado, no es sencillo, pero está bien explicado, todo lo bien explicado que desde la **OAI** hemos podido.

## 🎁 **BUENO BUENO... LO SÉ, NO TIENES TIEMPO, PUEDES DESCARGARTE LOS MODELOS YA ENTRENADOS SI LO PREFIERES.** 😆  

# **🛠️ LO DEMÁS ESTÁ EN CONSTRUCCIÓN 🚧 🏗️**  

## **CONSIDERACIONES IMPORTANTES**
Para la creación y entrenamiento del proyecto, el ordenador utilizado tenía las siguientes características:

> **Software**
> - **Versión de keras:** 3.4.1
> - **Versión de python:** 3.12.3
> - **Versión de sklearn:** 1.4.2
> - **Versión de tensorflow:** 2.16.1
> - **Versión de Microsoft Windows:** Windows 11 Pro, 10.0.22631.3810
>  
> **Hardware**
> - **Procesador:** Intel64 Family 6 Model 165 Stepping 2 GenuineIntel @ 2.59 GHz
> - **Memoria RAM:** 16.2 GB
> - **Almacenamiento:** SSD de 500 GB
> - **Tarjeta Gráfica:** NVIDIA GeForce GTX 1660 Ti
> - **Red:**
>   - **Wi-Fi:** Intel(R) Wi-Fi 6 AX201
>   - **Ethernet:** Realtek PCIe GbE Family Controller