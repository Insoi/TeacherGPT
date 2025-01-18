from __future__ import annotations

import json
from typing import Any, Dict, List, Union
from fastapi import Request
from fastapi.responses import RedirectResponse
from openai.types.chat.chat_completion import ChatCompletion

from app.app import openai, app, templates


@app.get("/favicon.ico")
def get_favicon():
    return RedirectResponse("https://em-content.zobj.net/source/sony/336/light-bulb_1f4a1.png")


@app.post("/chat")
async def post_chat(request: Request, history: List[Dict[str, str]]):
    response: ChatCompletion = await openai.chat.completions.create(
        messages=history,
        model="gpt-4o-mini",
        stream=False,
    )

    return {"role": "assistant", "content": response.choices[0].message.content}


@app.get("/")
async def get_index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.j2",
        # context={"chat": {"response": response.choices[0].message.content}},
    )
