<img src="Imagenes/readme.jpg" alt="Imagen creada con inteligencia artificial y editada con Microsoft Paint" style="border-radius: 15px;">

*Imagen creada con inteligencia artificial y editada con Microsoft Paint*


# CONTROL DE EMOCIONES
El Ministerio para el Bienestar Emocional (**MBE**), organismo dependiente de la 'Unión Directiva para el Bien Común' (**UDBC**), nos ha pedido a la **“Organización de Asuntos Informáticos”** que desarrollemos un modelo que, dada la foto, reconozca la emoción en la cara del sujeto y, según sea esta y las necesidades del momento, dictamine qué sustancias administrar.

El ser humano medio no tiene la capacidad de elegir/manejar sus emociones conforme a lo necesario para un mundo y convivencia adecuados, por lo que la UDBC, a través del MBE y siguiendo las obligaciones morales, monitoreará dichas emociones con ayuda del modelo de aprendizaje automático que presentamos en este readme. Gracias al sistema conectado de cámaras de cuidados de la población, esta puede ser monitoreada mientras se desplaza en sus cápsulas de transporte unipersonal, mientras trabaja en sus cubículos laborales, en los ascensores y, en general, en todos los aspectos de la vida. Cuando una expresión detectada no concuerde con lo necesario para la armonía y el bienestar, una sustancia será administrada por los aspersores ambientales y/o las fuentes de bebidas refrescantes. 

<img src="Imagenes/MBE.jpg" width="200">


Para el entrenamiento de dicho modelo se empleará el dataset [“FER-2013 (Facial Expression Recognition 2013)”](https://www.kaggle.com/datasets/msambare/fer2013)
, el cual contiene 35,887 imágenes en escala de grises de rostros de tamaño 48x48 píxeles. Etiquetadas con siete emociones: ira, disgusto, miedo, felicidad, tristeza, sorpresa y neutro, este era, según ChatGPT (el predecesor del actual “Pensamiento Descentralizado”), un dataset popular en la comunidad de investigación en reconocimiento de emociones faciales.

Una vez el programa sepa la emoción que el individuo siente, a este se le administrará una sustancia según algunos criterios.
