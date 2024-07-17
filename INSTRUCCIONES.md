<img src="notebooks_y_mas/Imagenes/intr.jpeg" alt="Imagen creada con inteligencia artificial y editada con Microsoft Paint" style="border-radius: 15px">

*Imagen creada con inteligencia artificial.*


## **INSTRUCCIONES**

1. **📁 Crea la carpeta principal:** Puedes llamarla como quieras, por ejemplo **"Proyecto ML"**.
  
2. **📁 En la carpeta principal crea otra carpeta:** Llámala **"notebooks_y_mas"**

3. **📁 En la carpeta "notebooks_y_mas" crea otra carpeta:** Llámala **"datos"**, dentro de "datos" crea otra carpeta que se llame **"fer2013"**. Descarga el dataset "fer2013" desde este [enlace](https://www.kaggle.com/datasets/nicolejyt/facialexpressionrecognition?select=fer2013.csv) y descomprímelo (dentro de la carpeta 'fer2013').   
👁️👁️ **¡OJO!** Es importante que el archivo se llame **fer2013.csv**

4. **📁 Dentro de la carpeta 'fer2013':** Crea una carpeta que se llame **"dataframe_individuales"**. No necesitas guardar nada, el código lo hará.

5. **Descarga el notebook 'EDA_FER2013.ipynb':** Guárdalo en la carpeta "notebooks_y_mas". Si ya tenías el dataset "fer2013" descargado y las carpetas creadas, al correr 'EDA_FER2013' se crearán automáticamente 3 archivos y se guardarán en la carpeta "dataframe_individuales".  
>Si esto no pasa puede ser que no tengas las carpetas con los mismos nombres.

   **¡ESPERA, ESPERA....LO SÉ!... ¡NO SE VEN LAS IMÁGENES!**
   Aunque es algo opcional y no afecta al funcionamiento, es estético y hace que sea menos pesado. Descarga la carpeta **'Imagenes'**, guárdala en la carpeta "notebooks_y_mas". Ahora podrás ver las imágenes en los notebooks. 🤔 ¿Tienes curiosidad por saber qué prompts he utilizado para la creación de las imágenes? Pues están en el archivo **"PROMPTS.md"**. ¿Quién lo diría... ¿eh?

6. **Descarga el archivo "Data_augmentation_fer2013.ipynb":** Guárdalo en la carpeta "notebooks_y_mas", ejecútalo y en la carpeta "fer2013" aparecerá un archivo CSV llamado **"fer2013_blc"**. "Blc" significa balanceado, es el resultado de aplicar técnicas de data augmentation al dataset fer2013 original. 

7. **📁 Crea una carpeta llamada 'AffectNet' dentro de 'datos':** Dentro de 'AffectNet', crea una carpeta llamada **'AffectNet_original'**. Dentro de esta carpeta, descarga y descomprime el dataset que encontrarás en este [enlace](https://www.kaggle.com/datasets/noamsegal/affectnet-training-data). Se habrá creado una carpeta llamada **'archive'** que contiene varias carpetas y un archivo CSV.  
  
8. **📁Crea una carpeta llamada 'expresiones individuales'** dentro de la carpeta **'AffectNet'**. No necesitas guardar nada, el código lo hará.

9. De 'AffectNet_original' elimina el archivo **'labels.csv'** y la carpeta **'contempt'**. Las carpetas restantes son: **Neutral, Happiness, Sad, Surprise, Fear, Disgust y Anger**. Como puedes ver, coinciden con **'FER2013'**. Cambia manualmente el nombre de las carpetas siguiendo el siguiente diccionario: **Neutral → 6, Happiness → 3, Sad → 4, Surprise → 5, Fear → 2, Disgust → 1 y Anger → 0**.  
  
10. **Descarga el archivo 'Preparado_AffectNet.ipynb':** Deberás ir cambiando los nombres de los dataframes y alguna cosa más; está indicado donde debes cambiar. En la carpeta **'expresiones individuales'** irán apareciendo archivos CSV a medida que lo vayas corriendo. Cuando tengas los 7 archivos descomenta el apartado **CONCATENADO Y GUARDADO DE LOS DATASETS**. Ahora tienes un archivo CSV llamado **'df_AffectNet_formato'**, este estará en la carpeta **'AffectNet'**. Tendrá el mismo formato que **'FEr2013'**.  

11. **Descarga el archivo 'EDA_AffectNet.ipynb', guárdalo en 'notebooks_y_mas':** Córrelo entero, si te interesa puedes echar un vistazo... Lo más importante es que ahora tendrás 3 datasets nuevos en la carpeta **"AffectNet"** 
  
12. **Descarga el archivo 'Data_augmentation_AffectNet', guárdalo en 'notebooks_y_mas':** Córrelo entero. Al terminar de correr, tendrás un archivo CSV llamado **'affe_balanceado.csv'**. Este aparecerá en la carpeta 'AffectNet'; es el dataset 'AffectNet' en el mismo formato que "FER2013" tras ser balanceado. También aparecerá dentro de la carpeta 'datos' el archivo CSV **'df_final.csv'**, el cual es fruto de la unión de los datasets 'FER2013' y 'AffectNet', debido a los diferentes cambios del proyecto, este dataset no será utilizado, pero puedes experimentar con él. 
  
13. **📁 Crea una carpeta llamada 'modelos_entrenados', guárdalo en 'notebooks_y_mas':** Aquí no tienes que guardar nada, solo esperar. Ni te imaginas lo que aparecerá aquí.  
## 🎁 **BUENO BUENO... LO SÉ, NO TIENES TIEMPO, PUEDES DESCARGARTE LOS MODELOS YA ENTRENADOS SI LO PREFIERES.** 😆  
  
14. **Descarga el archivo "Modelos_expresiones.ipynb":** Ejecuta todo el notebook; tómate tu tiempo, tardará un rato. Está bastante explicado, no es sencillo, pero está bien explicado, todo lo bien explicado que desde la **OAI** hemos podido. Ya tienes 2 modelos, uno entrenado con "FER2013" y otro reentrenado con "AffectNet".

15. **En la carpeta principal, crea una carpeta llamada 'Imagenes_prueba_emociones'**. Guarda en ella una buena colección de fotografías en formato JPG de caras humanas con distintos gestos; serán las imágenes que el programa usará como prueba final. Mientras mejor esté encuadrada la cara, mejor funcionará. El nombre de cada fotografía será el nombre de la persona.  
🤫 *Por respeto a la intimidad y propiedad intelectual, no se ha subido esta carpeta al repositorio.*  
  
16. **En la carpeta 'notebooks_y_mas' descarga el archivo 'gvatilo.py'**  
  
17. **En la carpeta principal descarga 'el programa'**
>Ya puedes usarlo. 🎉🎊🥳

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