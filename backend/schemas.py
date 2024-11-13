from pydantic import BaseModel, EmailStr, Field, ValidationError, field_validator
from typing import List, Optional
from datetime import datetime, date
from fastapi import HTTPException, status
import re

class TestFractureBase(BaseModel):
    predicted_class : str 
    
class UserBase(BaseModel):
    username : str
    password : str
    email : EmailStr

    