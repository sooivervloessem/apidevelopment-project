from fastapi import FastAPI, Path
from pydantic import BaseModel
from random import randint
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://localhost.tiangolo.com",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class KpopSong(BaseModel):
    song: str
    artist: str
    album: str | None = None
    release_date: str | None = None


kpop_songs = {"0": {
    "song": "Shut Down",
    "artist": "Blackpink",
    "album": "Born Pink",
    "release_date": "2022"
},
    "1": {
        "song": "After Like",
        "artist": "IVE",
        "album": "After Like",
        "release_date": "2022"
    }
}


@app.get("/kpop")
async def get_kpop_songs():
    return kpop_songs


@app.get("/kpop/random")
async def get_random_kpop_song():
    lower_limit = 0
    upper_limit = len(kpop_songs) - 1
    if (lower_limit > upper_limit):
        return {'error': 'The list of kpop songs may not be empty'}
    return kpop_songs[str(randint(lower_limit, upper_limit))]


@app.get("/kpop/{id}")
async def get_kpop_song_by_id(id: int):
    # async def get_kpop_song_by_id(*, id: int = Path(title="The ID of the song to get", ge=0, lt=len(kpop_songs))):
    if id >= len(kpop_songs):
        return {'error': 'There is no song matching that id.'}
    if id < 0:
        return {'error': 'Id cannot be less than 0.'}
    return kpop_songs[str(id)]


@app.post("/kpop", response_model=KpopSong)
async def create_kpop_song(kpop_song: KpopSong):
    kpop_songs[str(len(kpop_songs))] = kpop_song
    return kpop_song
