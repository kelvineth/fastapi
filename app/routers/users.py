from fastapi import Depends,status,HTTPException,APIRouter
from sqlalchemy.orm import Session
from ..import models,schemas
from ..database import get_db
from typing import List
from .. import utility


router=APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/",response_model=schemas.sendOut)
def create(user:schemas.User,db:Session=Depends(get_db)):
    hashed_password=utility.hash(user.password)
    user.password=hashed_password
    new_user=models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{id}",response_model=schemas.sendOut)
def get_user(id,db:Session=Depends(get_db)):
    get_user=db.query(models.User).filter(models.User.id==id).first()
    if not get_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"user with {id} unavailable")
    return get_user
