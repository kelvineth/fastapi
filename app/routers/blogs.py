from fastapi import Depends,status,HTTPException,APIRouter
from sqlalchemy.orm import Session
from ..import models,schemas
from ..database import get_db
from typing import List,Optional
from ..import oauth2
from sqlalchemy import func

router=APIRouter(
    prefix="/blogs",
    tags=["blogs"]
)

@router.get("/")
def test_file(db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user),limit:int =10 ,skip:int=0,search:Optional[str]=""):
    blog=db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    result=db.query(models.Post,func.count(models.Votes.posts_id).label("votes")).join(models.Votes,models.Votes.posts_id==models.Post.id,isouter=True).group_by(models.Post.id).all()
    return  result
#(model.Blog.owner_id==current_user.id)

@router.get("/{id}",response_model=schemas.Post)
def al_post(id,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    al_post=db.query(models.Post).filter(models.Post.id==id).first()
    if not al_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not available")
    return al_post

@router.post("/",response_model=schemas.Post)
def create(request:schemas.PostBase,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    
    #title=request.title,content=request.contents,published=request.published
    create=models.Post(owner_id=current_user.id,**request.dict())
    db.add(create)
    db.commit()
    db.refresh(create)
    return create

@router.delete("/{id}")
def delete(id,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    delete=db.query(models.Post).filter(models.Post.id==id)
    delete1=delete.first()
    if not delete1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'deleted {id}')

    if delete1.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="cant perform that function")
    delete.delete(synchronize_session=False)
    db.commit()
    return 'updated'

@router.put("/{id}")
def update(id,request:schemas.PostBase,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    updat=db.query(models.Post).filter(models.Post.id==id)

    updated=updat.first()
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'its not found')
    if updated.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="cant perform that function")
    updat.update(request.dict() , synchronize_session=False)
    db.commit()
    return {'data':updat.first()}
    