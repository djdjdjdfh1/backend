from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import engine, get_db

app = FastAPI(
    title='Product API',
    description='제품관리'
)

# 라우터 설정
@app.get('/')
def root():
    return {'message': 'Welcome to the Product API'}
