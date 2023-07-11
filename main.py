from fastapi import FastAPI
import pandas as pd

app = FastAPI(title='Proyecto 01',
              description='Proyecto Individual 01 - HENRY',
              version='1.0.1')

@app.get('/')
async def read_root():
    return {'Mi primera API'}
    
@app.on_event('startup')
async def startup():
    global movies_df
    movies_df = pd.read_csv('movies_dataset.csv') 

@app.get('/')
async def index():
    return {'Mi primera API (Monse Castillo)'}

@app.get('/about/')
async def about():
    return {'Proyecto Individual No. 1 de Data Science'}

# Devuelve la cantidad de películas producidas en el idioma dado.
@app.get('/peliculas_idioma/({Idioma})')
def peliculas_idioma(Idioma:str):
    num = movies_df[movies_df['lenguaje'] == Idioma].shape[0] 
    print(f"{num} películas fueron estrenadas en idioma {Idioma}")

# Se ingresa una película y devuelve la duración y el año.
@app.get('/peliculas_duracion/({Pelicula})')
def peliculas_duracion(Pelicula:str):
    duration = movies_df[movies_df['title'] == Pelicula]['runtime']
    anio = movies_df[movies_df['title'] == Pelicula]['release_year']
    print(f"La pelicula: {Pelicula}")
    print(f"tiene una duracion de: {duration}")
    print(f"Año de lanzamiento: {anio} ")

# Se ingresa la franquicia y retorna la cantidad de películas, ganancia total y promedio
@app.get('/franquicia/({Franquicia})')
def franquicia(Franquicia:str):
    cantidad_pelis = movies_df[movies_df['production_companies'] == Franquicia].shape[0]
    ganancia_total = movies_df[movies_df['production_companies'] == Franquicia]['revenue'].sum() 
    #ganancia_promedio = movies_df[movies_df['production_companies'] == Franquicia]['revenue'].promedio()
    print(f"La franquicia {Franquicia} posee {cantidad_pelis} peliculas con una ganancia total de: {ganancia_total}")

# Se ingresa un país y retorna la cantidad de películas producidas
@app.get('/peliculas_pais/({Pais})')
def peliculas_pais(Pais:str):
    cantidad_pelis = movies_df[movies_df['production_countries'] == Pais].shape[0]
    print(f"El país {Pais} ha producido {cantidad_pelis} películas")

@app.get('/productoras_exitosas/({Productora})')
def productoras_exitosas(Productora:str):
    cantidad_pelis = movies_df[movies_df['production_companies'] == Productora].shape[0]
    ganancia_total = movies_df[movies_df['production_companies'] == Productora]['revenue'].sum() 
    print(f"La Productora: {Productora} posee {cantidad_pelis} peliculas con una ganancia total de: {ganancia_total}")

@app.get('/get_director/({nombre_director})')
def get_director(nombre_director:str):
    movies_director = movies_df[movies_df['Director']==nombre_director]
    movies_director['title','release_year','budget','revenue','return']




