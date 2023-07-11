# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>

¡Bienvenidos a mi primer proyecto! 

<hr>  

## **Descripción del problema (Contexto y rol a desarrollar)**

En este proyecto haremos del rol de un **`Data Scientist`** suponiendo que se nos ha proporcionado un conjunto de datos relacionados al stremaing, siendo nuestra encomienda proporcionar un modelo de ML que soluciona un problema de negocio: un sistema de recomendación de películas que aún no ha sido puesto en marcha y un deploy listo para consumir por los departamentos de Analytics y Machine Learning, para el cual se nos ha solicitado los siguientes 6 requerimientos:

1.- Se ingresa un idioma. Debe devolver la cantidad de películas producidas en ese idioma.

2.- Se ingresa una película. Debe devolver la duración y el año.

3.- Se ingresa la franquicia, retornando la cantidad de películas, ganancia total y promedio
    
4.- Se ingresa un país, retornando la cantidad de películas producidas en el mismo.
    
5.- Se ingresa la productora, entregándote el revunue total y la cantidad de películas que realizó. 
    
6.- Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma, en formato lista.

## Estructura de este proyecto

A continuación se expone una breve descripción de como está conformado este proyecto:

+ Se nos proporcionó dos data set llamados *movies_dataset.csv* y *credits.csv* los cuales se encuentran es su estado original (datos anidados y sin transformar) en la carpeta *Data_Original*. Estos son datos sobre películas.

+ La extracción, transformación y carga (ETL) de los data sets arriba mencionados la podemos encontrar en la carpeta *ETL* en el archivo llamado *movies_dataset.csv*.

+ Posterior al ETL de los datos, en la carpeta *EDA.ipynb* podemos hallar el Exploratory Data Analisis de los datos ya transformados en el ETL.

+ La carpeta *FastAPI* contiene un archivo llamado *main.py* el cual es el cuerpo de nuestra API en FastAPI, el archivo *Querys_Testeo.ipynb* contiene un testeo de las funciones que se usan en la API y finalmente la fuente de datos de la que se nutre: *movies_dataset.csv* que también tomada de la carpeta del ETL 

https://testapi-lqx0.onrender.com/docs

+ En la carpeta *Sistema_de_Recomendacion* se puede hallar el sistema de recomendación de películas.

+ Finalmente tenemos la carpeta *Imagenes* donde contenemos las imágenes usadas en este archivo *README.md*.


