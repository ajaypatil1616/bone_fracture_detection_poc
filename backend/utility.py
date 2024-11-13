import subprocess
from PIL import Image
import numpy as np
from fastapi import UploadFile
from datetime import datetime, timedelta, date
from jose import JWTError, jwt
from typing import List, Optional

def run_notebook(notebook_path):
    command = f"jupyter nbconvert --to notebook --execute {notebook_path} --output executed_notebook.ipynb"
    subprocess.run(command, shell=True, check= True)
    
async def load_preprocessed_image(uploaded_file: UploadFile, img_height = 180, img_width = 180):
    img = Image.open(uploaded_file.file).convert('RGB')
    img = img.resize((img_height, img_width))
    img_array = np.array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis = 0)
    return img_array

def create_access_token(data: dict, 
                        expires_delta : Optional[timedelta]=None):
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else :
        expire = datetime.utcnow() + timedelta(minutes= 30)
    
    data.update({"exp":expire})
    
    access_token = jwt.encode(data, 'ajaypatil@16161616', algorithm= 'HS256')
    return access_token

