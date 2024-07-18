<img src="notebooks_y_mas/Imagenes/docu.jpg" alt="Imagen creada con inteligencia artificial." style="border-radius: 15px;">

*Imagen creada con inteligencia artificial.*


# CONTROL DE EMOCIONES
El Ministerio para el Bienestar Emocional (**MBE**), organismo dependiente de la 'Unión Directiva para el Bien Común' (**UDBC**), nos ha pedido a la Organización de Asuntos Informáticos (**OAI**) que desarrollemos un modelo que, dada la foto, reconozca la emoción en la cara del sujeto y, según sea esta y las necesidades del momento, dictamine qué sustancias administrar.  


<img src="notebooks_y_mas/Imagenes/UDBC.jpg" alt="Logotipo de MBE" width="200">  
  
>Logotipo de UDBC.

El ser humano medio no tiene la capacidad de elegir/manejar sus emociones conforme a lo necesario para un mundo y convivencia adecuados, por lo que la UDBC, a través del MBE y siguiendo las obligaciones morales, monitoreará dichas emociones con ayuda del modelo de aprendizaje automático que presentamos en este readme. Gracias al sistema conectado de cámaras de cuidados de la población, esta puede ser monitoreada mientras se desplaza en sus cápsulas de transporte unipersonal, mientras trabaja en sus cubículos laborales, en los ascensores y, en general, en todos los aspectos de la vida. Cuando una expresión detectada no concuerde con lo necesario para la armonía y el bienestar, una sustancia será administrada por los aspersores ambientales y/o las fuentes de bebidas refrescantes. 

<img src="notebooks_y_mas/Imagenes/mini.jpg" alt="Logotipo de MBE" width="150">  

>Logotipo de MBE

Para el entrenamiento del modelo que reconoce la emoción se empleará el dataset ["FER-2013 (Facial Expression Recognition 2013)"](https://www.kaggle.com/datasets/nicolejyt/facialexpressionrecognition?select=fer2013.csv), el cual contiene 35,887 imágenes en escala de grises. Las imágenes son fotografías casi exclusivamente de rostros, de tamaño 48x48 píxeles y están etiquetadas con siete emociones: 'Asco', 'Enojo', 'Felicidad', 'Miedo', 'Sorpresa', 'Tristeza' y 'Neutral'. Este dataset fue popular en la comunidad de investigación en reconocimiento de emociones faciales durante la era de ChatGPT, el predecesor del actual 'Pensamiento Descentralizado'.

La cúpula de **OAI** ha ordenado que se explique bien el proyecto, de forma que se facilmente entendible incluso por aquellas persona con poca formacion en ela materia.
Por ello el proyecto esta dividido en los siguintes documentos.  
   
 -["El programa"](https://github.com/PepeReinaCampo/proyectoML/blob/main/INSTRUCCIONES.md): *VER ABAJO*
 
 -["PROMPTS"](https://github.com/PepeReinaCampo/proyectoML/blob/main/PROMPTS.md): La estética y el tiempo son aspectos importantes. Es crucial que los documentos sean atractivos y no resulten densos; por eso, se han añadido imágenes creadas con un servicio de inteligencia artificial de la época. Estas imágenes fueron rescatadas de las bases de datos mencionadas en la idea de negocio. En este documento se muestran los prompts utilizados.   

-["INSTRUCCIONES"](https://github.com/PepeReinaCampo/proyectoML/blob/main/INSTRUCCIONES.md): Nuestro departamento, siguiendo las órdenes de la cúpula de la OAI, ha creado unas instrucciones para que cualquiera, con algunas nociones en el manejo de datos y programación, pueda recrear ***El programa*** en casa.  
  
-["Idea de negocio"](https://github.com/PepeReinaCampo/proyectoML/blob/main/Idea%20de%20negocio.pptx): En este documento se muestra como planteamos resolver el problema, digamos que es el folleto informativo.

-["EDA_FER2013"](https://github.com/PepeReinaCampo/proyectoML/blob/main/notebooks_y_mas/EDA_FER2013.ipynb):En este documento se realiza un estudio del conjunto de datos principal utilizado para entrenar los modelos.  
  
-["Data_augmentation_fer2013"](https://github.com/PepeReinaCampo/proyectoML/blob/main/notebooks_y_mas/Data_augmentation_fer2013.ipynb): Durante el análisis exploratorio, se observó un desbalance en las distintas clases, lo cual podría suponer un problema debido a las tecnologías de aquella época. Este documento aborda y soluciona dicho problema, equilibrando las clases en los 3 datasets, generando un único dataset balanceado.
  
-["Preparado_AffectNet"](https://github.com/PepeReinaCampo/proyectoML/blob/main/notebooks_y_mas/Preparado_AffectNet.ipynb): Buscando mejorar el modelo, nos encontramos con el dataset 'AffectNet', el cual tenía un formato diferente al de 'FER2013'. En este notebook, lo transformamos al mismo formato que 'FER2013'. Al final del notebook, tienes información sobre dicho dataset.  
  
-["Data_augmentation_AffectNet"](https://github.com/PepeReinaCampo/proyectoML/blob/main/notebooks_y_mas/Data_augmentation_AffectNet.ipynb): Una vez habíamos transformado este dataset al mismo formato que FER2013, nos encontramos con el mismo problema, las clases estaban desbalanceadas, por lo que hicimos lo mismo que con el anterior. Este dataset estaba menos desbalanceado.  
  
-["EDA_AffectNet"](https://github.com/PepeReinaCampo/proyectoML/blob/main/notebooks_y_mas/EDA_AffectNet.ipynb): Al igual que con el EDA de FER2013, en este documento se realiza un estudio del conjunto de datos.  
  
-["Modelos_expresiones"](https://github.com/PepeReinaCampo/proyectoML/blob/main/Data_augmentation_fer2013.ipynb): En este documento se carga el dataset FER2013 y se entrena un modelo CNN. Posteriormente, se carga el modelo entrenado junto con el dataset AffectNet para un reentrenamiento. Ambos datasets cargados son versiones balanceadas, creadas en los notebooks 'Data_augmentation'. El documento 'Modelos_expresiones' proporciona explicaciones y razonamientos para que, aunque sea algo complejo, sea fácil de leer y entender los resultados.
  
-["gvatilo"](https://github.com/PepeReinaCampo/proyectoML/blob/main/notebooks_y_mas/gvatilo.py): Esta es la función que organiza todo. Usando el modelo entrenado o reentrenado y la información que reciba de la llamada, devolverá toda la información que veremos a través del programa. En el mismo archivo Python hay una pequeña explicación sobre dicha función.




<img src="notebooks_y_mas/Imagenes/OAI.jpg" alt="Logotipo de MBE" width="150">  

>Logotipo de OAI
  
***"El programa"*** (los servicios de marketing y comunicación aún no le han dado nombre) que presentamos aquí solicitará introducir la emoción necesaria, e irá estudiando a los individuos que requieran vigilancia. El programa devolverá la emoción detectada y la sustancia que se administrará, pudiendo en una fase inicial requerir supervisión humana.

Esto será solo en una primera fase; cuando el producto entre en producción será completamente autónomo, dependiendo únicamente de las órdenes de la cúpula dirigente de MBE, quienes dictaminarán las emociones necesarias.

Las sustancias que serán administradas están en la siguiente tabla:

<table>
    <thead>
        <tr>
            <th>Emoción Detectada</th>
            <th>Emoción Adecuada</th>
            <th>Sustancia por Administrar</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="7" align="center">Neutral</td>
            <td align="center">Neutral</td>
            <td align="center">POSTPLACEBO</td>
        </tr>
        <tr>
            <td align="center">Enojo</td>
            <td align="center">DIMETOVELOCETINA-BUTIL</td>
        </tr>
        <tr>
            <td align="center">Asco</td>
            <td align="center">CLOROCHOLEXSINA</td>
        </tr>
        <tr>
            <td align="center">Miedo</td>
            <td align="center">DIMETIL-NEPTODEXTROXIDO</td>
        </tr>
        <tr>
            <td align="center">Felicidad</td>
            <td align="center">LIQUALENSINA</td>
        </tr>
        <tr>
            <td align="center">Tristeza</td>
            <td align="center">OXSOMA-BUTIL</td>
        </tr>
        <tr>
            <td align="center">Sorpresa</td>
            <td align="center">2-10-EMEDIOXINA</td>
        </tr>
        <tr>
            <td rowspan="7" align="center">Enojo</td>
            <td align="center">Neutral</td>
            <td align="center">NEUTROLINOXONA</td>
        </tr>
        <tr>
            <td align="center">Enojo</td>
            <td align="center">POSTPLACEBO</td>
        </tr>
        <tr>
            <td align="center">Asco</td>
            <td align="center">METACHOLEXSINA</td>
        </tr>
        <tr>
            <td align="center">Miedo</td>
            <td align="center">FEAREANEFRINA</td>
        </tr>
        <tr>
            <td align="center">Felicidad</td>
            <td align="center">OXITOACERVEXINA</td>
        </tr>
        <tr>
            <td align="center">Tristeza</td>
            <td align="center">CLOROMETANOXIFINAFLUORIDA</td>
        </tr>
        <tr>
            <td align="center">Sorpresa</td>
            <td align="center">2-10-EMEDIOXINA</td>
        </tr>
        <tr>
            <td rowspan="7" align="center">Asco</td>
            <td align="center">Neutral</td>
            <td align="center">NEUTROLINOXONA</td>
        </tr>
        <tr>
            <td align="center">Enojo</td>
            <td align="center">SYNTHEISITISEINA</td>
        </tr>
        <tr>
            <td align="center">Asco</td>
            <td align="center">POSTPLACEBO</td>
        </tr>
        <tr>
            <td align="center">Miedo</td>
            <td align="center">FEAREANEFRINA</td>
        </tr>
        <tr>
            <td align="center">Felicidad</td>
            <td align="center">LIQUALENSINA</td>
        </tr>
        <tr>
            <td align="center">Tristeza</td>
            <td align="center">CLOROMETANOXIFINAFLUORIDA</td>
        </tr>
        <tr>
            <td align="center">Sorpresa</td>
            <td align="center">2-10-EMEDIOXINA</td>
        </tr>
        <tr>
            <td rowspan="7" align="center">Miedo</td>
            <td align="center">Neutral</td>
            <td align="center">NEUTROLINOXONA</td>
        </tr>
        <tr>
            <td align="center">Enojo</td>
            <td align="center">KOROBININA</td>
        </tr>
        <tr>
            <td align="center">Asco</td>
            <td align="center">METACHOLEXSINA</td>
        </tr>
        <tr>
            <td align="center">Miedo</td>
            <td align="center">POSTPLACEBO</td>
        </tr>
        <tr>
            <td align="center">Felicidad</td>
            <td align="center">LIQUALENSINA</td>
        </tr>
        <tr>
            <td align="center">Tristeza</td>
            <td align="center">OXSOMA-BUTIL</td>
        </tr>
        <tr>
            <td align="center">Sorpresa</td>
            <td align="center">2-10-EMEDIOXINA</td>
        </tr>
        <tr>
            <td rowspan="7" align="center">Felicidad</td>
            <td align="center">Neutral</td>
            <td align="center">NEUTROLINOXONA</td>
        </tr>
        <tr>
            <td align="center">Enojo</td>
            <td align="center">IRAXCITUR</td>
        </tr>
        <tr>
            <td align="center">Asco</td>
            <td align="center">CLOROCHOLEXSINA</td>
        </tr>
        <tr>
            <td align="center">Miedo</td>
            <td align="center">FEAREANEFRINA</td>
        </tr>
        <tr>
            <td align="center">Felicidad</td>
            <td align="center">POSTPLACEBO</td>
        </tr>
        <tr>
            <td align="center">Tristeza</td>
            <td align="center">OXSOMA-BUTIL</td>
        </tr>
        <tr>
            <td align="center">Sorpresa</td>
            <td align="center">2-10-EMEDIOXINA</td>
        </tr>
        <tr>
            <td rowspan="7" align="center">Tristeza</td>
            <td align="center">Neutral</td>
            <td align="center">NEUTROLINOXONA</td>
        </tr>
        <tr>
            <td align="center">Enojo</td>
            <td align="center">DIMETOVELOCETINA-BUTIL</td>
        </tr>
        <tr>
            <td align="center">Asco</td>
            <td align="center">METACHOLEXSINA</td>
        </tr>
        <tr>
            <td align="center">Miedo</td>
            <td align="center">DIMETIL-NEPTODEXTROXIDO</td>
        </tr>
        <tr>
            <td align="center">Felicidad</td>
            <td align="center">OXITOACERVEXINA</td>
        </tr>
        <tr>
            <td align="center">Tristeza</td>
            <td align="center">POSTPLACEBO</td>
        </tr>
        <tr>
            <td align="center">Sorpresa</td>
            <td align="center">2-10-EMEDIOXINA</td>
        </tr>
        <tr>
            <td rowspan="7" align="center">Sorpresa</td>
            <td align="center">Neutral</td>
            <td align="center">NEUTROLINOXONA</td>
        </tr>
        <tr>
            <td align="center">Enojo</td>
            <td align="center">SYNTHEISITISEINA</td>
        </tr>
        <tr>
            <td align="center">Asco</td>
            <td align="center">CLOROCHOLEXSINA</td>
        </tr>
        <tr>
            <td align="center">Miedo</td>
            <td align="center">IRAXCITURIOL-AMINA</td>
        </tr>
        <tr>
            <td align="center">Felicidad</td>
            <td align="center">OXITOACERVEXINA</td>
        </tr>
        <tr>
            <td align="center">Tristeza</td>
            <td align="center">OXSOMA-BUTIL</td>
         </tr>  
        <tr>
            <td align="center">Sorpresa</td>
            <td align="center">POSTPLACEBO</td> 
        </tr>
    </tbody>
</table>


