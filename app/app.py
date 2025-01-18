from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from openai import AsyncOpenAI

from app.config import config

templates = Jinja2Templates(directory="templates")
app = FastAPI(docs_url=None, include_in_schema=False)

openai = AsyncOpenAI(api_key=config.openai_token.get_secret_value())

app.mount("/static", StaticFiles(directory="static"), name="static")
