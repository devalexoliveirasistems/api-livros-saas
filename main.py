from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from gemini import analyze_text
from auth import verify_key
import json

app = FastAPI(title="API de Análise de Livros")


class RequestBody(BaseModel):
    text: str


@app.post("/analyze")
def analyze(data: RequestBody, authorization: str = Header(None)):

    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Sem API key"
        )

    if not verify_key(authorization):
        raise HTTPException(
            status_code=403,
            detail="API key inválida"
        )

    result = analyze_text(data.text)

    try:
        return json.loads(result)
    except:
        return {"raw": result}