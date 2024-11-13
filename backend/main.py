# Import
from fastapi import FastAPI, requests, HTTPException, Form, Depends, status, Request
from fastapi_sqlalchemy import DBSessionMiddleware, db
from sqlalchemy.orm import Session
from typing import List
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from fastapi import File, UploadFile
import os
from dotenv import load_dotenv
from datetime import timedelta
from random import randint
import tensorflow as tf
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


import models
import schemas
import utility



app = FastAPI() 

#CORS error...... resolved
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = "*",
    allow_headers = ["*"]
    
)
app.add_middleware(DBSessionMiddleware, db_url ='postgresql://postgres:1234@localhost:5432/bonefracture')

# app.mount("/static", StaticFiles(directory="../frontend"), name = "static")
# templates = Jinja2Templates(directory='../frontend')

loaded_model = None


@app.on_event("startup")
async def startup_event():
    global loaded_model
   
    if not os.path.exists('fracture_detection_model.keras'):
        utility.run_notebook('bone_fracture_model.ipynb')
    loaded_model = tf.keras.models.load_model("fracture_detection_model.keras")

@app.on_event("shutdown")
async def shutdown_event():
    global loaded_model
    loaded_model = None
        


@app.post("/test-fracture")
async def test_fracture_using_cnn(file: UploadFile):
    try:
        
        preprocessed_img = await utility.load_preprocessed_image(file)        
        prediction = loaded_model.predict(preprocessed_img)
        class_names = ['fractured','not fractured']
        predicted_class = (prediction > 0.5).astype("int32")        
        return {"predicted_class ": f"{class_names[predicted_class[0][0]]}"}
        
    except Exception as e :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail =str(e))

@app.post("/register")
async def create_user(user_data : schemas.UserBase):
    try:
        new_user = models.User(**user_data.dict())
        db.session.add(new_user)
        db.session.commit()
        db.session.refresh(new_user)
        return {"message": "Registration successful"}
    except Exception as e:
        db.session.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        db.session.close()
 
@app.post("/token")
async def log_in(form_data : dict):
    username = form_data['username']
    password = form_data['password']
    
    user = db.session.query(models.User).filter(models.User.username == username).first()
    
    if not user :
        return False
    if password != user.password :
        return False    
    access_token_expires = timedelta(minutes=30)
    
    access_token = utility.create_access_token(
        data={"email": user.email}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token,}
    