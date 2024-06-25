<img src="Imagenes/readme.jpg" alt="Imagen creada con inteligencia artificial y editada con Microsoft Paint" style="border-radius: 15px;">

*Imagen creada con inteligencia artificial y editada con Microsoft Paint*


# CONTROL DE EMOCIONES
El Ministerio para el Bienestar Emocional (**MBE**), organismo dependiente de la 'Unión Directiva para el Bien Común' (**UDBC**), nos ha pedido a la Organización de Asuntos Informáticos (**OAI**) que desarrollemos un modelo que, dada la foto, reconozca la emoción en la cara del sujeto y, según sea esta y las necesidades del momento, dictamine qué sustancias administrar.  


<img src="Imagenes/UDBC.jpg" alt="Logotipo de MBE" width="200">  
  
>Logotipo de UDBC.

El ser humano medio no tiene la capacidad de elegir/manejar sus emociones conforme a lo necesario para un mundo y convivencia adecuados, por lo que la UDBC, a través del MBE y siguiendo las obligaciones morales, monitoreará dichas emociones con ayuda del modelo de aprendizaje automático que presentamos en este readme. Gracias al sistema conectado de cámaras de cuidados de la población, esta puede ser monitoreada mientras se desplaza en sus cápsulas de transporte unipersonal, mientras trabaja en sus cubículos laborales, en los ascensores y, en general, en todos los aspectos de la vida. Cuando una expresión detectada no concuerde con lo necesario para la armonía y el bienestar, una sustancia será administrada por los aspersores ambientales y/o las fuentes de bebidas refrescantes. 

<img src="Imagenes/mini.jpg" alt="Logotipo de MBE" width="150">  

>Logotipo de MBE

Para el entrenamiento del modelo que reconoce la emoción se empleará el dataset ["FER-2013 (Facial Expression Recognition 2013)"](https://www.kaggle.com/datasets/msambare/fer2013), el cual contiene 35,887 imágenes en escala de grises. Las imágenes son fotografías casi exclusivamente de rostros, de tamaño 48x48 píxeles y están etiquetadas con siete emociones: ira, disgusto, miedo, felicidad, tristeza, sorpresa y neutro. Este dataset fue popular en la comunidad de investigación en reconocimiento de emociones faciales durante la era de ChatGPT, el predecesor del actual 'Pensamiento Descentralizado'.

La cúpula de **OAI** nos ha solicitado que cualquier dataset sea estudiado y explicado de forma clara. Por ello, en el notebook **"EDA_FER2013"** se ha analizado el dataset "FER2013". Además, los comandos utilizados para generar las imágenes mostradas en el presente informe están indicados en el archivo "PROMPTS".


<img src="Imagenes/OAI.jpg" alt="Logotipo de MBE" width="150">  

>Logotipo de OAI
  
El programa que presentamos aquí solicitará introducir la emoción necesaria para cada grupo social, también pedirá introducir una fotografía y el programa devolverá la emoción detectada y la sustancia que se administrará.

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
            <td align="center">VELOCET</td>
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
            <td align="center">B</td>
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
            <td align="center">W</td>
        </tr>
        <tr>
            <td align="center">Felicidad</td>
            <td align="center">AD</td>
        </tr>
        <tr>
            <td align="center">Tristeza</td>
            <td align="center">AK</td>
        </tr>
        <tr>
            <td align="center">Sorpresa</td>
            <td align="center">AR</td>
        </tr>
        <tr>
            <td rowspan="7" align="center">Asco</td>
            <td align="center">Neutral</td>
            <td align="center">C</td>
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
            <td align="center">X</td>
        </tr>
        <tr>
            <td align="center">Felicidad</td>
            <td align="center">LIQUALENSINA</td>
        </tr>
        <tr>
            <td align="center">Tristeza</td>
            <td align="center">AL</td>
        </tr>
        <tr>
            <td align="center">Sorpresa</td>
            <td align="center">AS</td>
        </tr>
        <tr>
            <td rowspan="7" align="center">Miedo</td>
            <td align="center">Neutral</td>
            <td align="center">D</td>
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
            <td align="center">AM</td>
        </tr>
        <tr>
            <td align="center">Sorpresa</td>
            <td align="center">AT</td>
        </tr>
        <tr>
            <td rowspan="7" align="center">Felicidad</td>
            <td align="center">Neutral</td>
            <td align="center">E</td>
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
            <td align="center">Z</td>
        </tr>
        <tr>
            <td align="center">Felicidad</td>
            <td align="center">POSTPLACEBO</td>
        </tr>
        <tr>
            <td align="center">Tristeza</td>
            <td align="center">AN</td>
        </tr>
        <tr>
            <td align="center">Sorpresa</td>
            <td align="center">AU</td>
        </tr>
        <tr>
            <td rowspan="7" align="center">Tristeza</td>
            <td align="center">Neutral</td>
            <td align="center">F</td>
        </tr>
        <tr>
            <td align="center">Enojo</td>
            <td align="center">M</td>
        </tr>
        <tr>
            <td align="center">Asco</td>
            <td align="center">METACHOLEXSINA</td>
        </tr>
        <tr>
            <td align="center">Miedo</td>
            <td align="center">AA</td>
        </tr>
        <tr>
            <td align="center">Felicidad</td>
            <td align="center">AH</td>
        </tr>
        <tr>
            <td align="center">Tristeza</td>
            <td align="center">POSTPLACEBO</td>
        </tr>
        <tr>
            <td align="center">Sorpresa</td>
            <td align="center">AV</td>
        </tr>
        <tr>
            <td rowspan="7" align="center">Sorpresa</td>
            <td align="center">Neutral</td>
            <td align="center">G</td>
        </tr>
        <tr>
            <td align="center">Enojo</td>
            <td align="center">N</td>
        </tr>
        <tr>
            <td align="center">Asco</td>
            <td align="center">CLOROCHOLEXSINA</td>
        </tr>
        <tr>
            <td align="center">Miedo</td>
            <td align="center">IRAXCITUR</td>
        </tr>
        <tr>
            <td align="center">Felicidad</td>
            <td align="center">AI</td>
        </tr>
        <tr>
            <td align="center">Tristeza</td>
            <td align="center">AP</td>
        </tr>
        <tr>
            <td align="center">Sorpresa</td>
            <td align="center">POSTPLACEBO</td>
        </tr>
    </tbody>
</table>

