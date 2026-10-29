import os
import joblib
import pandas as pd

from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from schema.payload import GenerateRequest,GenerateResponse


models = {}

@asynccontextmanager
async def lifespan(app : FastAPI):

    models["model"] = joblib.load("model_pipeline.pkl")

    yield

    models.clear()


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.post("/predict",response_model=GenerateResponse)
def predict(data : GenerateRequest):
    user_df = pd.DataFrame([data.dict()])

    user_pre = models["preprocessor"].transform(user_df)

    prob = models["model"].predict(user_pre)

    return GenerateResponse(
        pred_anxiety = int(prob>=0.5),
        prob_anxiety = prob
    )
