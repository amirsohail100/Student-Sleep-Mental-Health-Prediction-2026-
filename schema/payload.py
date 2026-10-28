from pydantic import BaseModel,Field
from typing import Literal

class GenerateRequest(BaseModel):
    age : int
    avg_sleep_hours : float
    screen_time_hours : float
    social_media_hours : float
    exercise_hours_per_week : float
    stress_level : int
    gpa : float
    feels_burned_out : int
    gender : Literal["Female","Male","Other"]
    education_level : Literal["High School","Undergraduate","Graduate"]

class GenerateResponse(BaseModel):
    pred_anxiety : str
    prob_anxiety : float