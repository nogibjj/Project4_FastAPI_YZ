import json
import os
from fastapi import FastAPI, HTTPException
import random
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from mangum import Mangum


class Movie(BaseModel):
    title: str
    image: str
    rating: float
    releaseYear: float
    genre: str
    

MOVIES_FILE = "movies.json"
MOVIES = []

if os.path.exists(MOVIES_FILE):
    with open(MOVIES_FILE, "r") as f:
        MOVIES = json.load(f)

app = FastAPI()
handler = Mangum(app)


@app.get("/")
async def root():
    return {"message": "Welcome to my movie store app!"}


@app.get("/random-movie")
async def random_movie():
    return random.choice(MOVIES)


@app.get("/list-movies")
async def list_movies():
    return {"movies": MOVIES}


@app.get("/movies_by_index/{index}")
async def movies_by_index(index: int):
    if index < len(MOVIES):
        return MOVIES[index]
    else:
        raise HTTPException(404, f"Movie index {index} out of range ({len(MOVIES)}).")


@app.get("/get-movie_by_title/{title}")
async def get_movie_by_title(title: str):
    for movie in MOVIES:
        if movie.title == title:
            return movie

    raise HTTPException(404, f"Movie title {title} not found in database.")
