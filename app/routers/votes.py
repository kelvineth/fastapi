from fastapi import Depends,status,HTTPException,APIRouter
from sqlalchemy.orm import Session
from ..import models,schemas
from ..database import get_db
from typing import List,Optional
from ..import oauth2

router=APIRouter( 
    prefix="/votes",
    tags=["votes"]
        )

@router.post("/",status_code=status.HTTP_201_CREATED)
def vote(votes:schemas.Votes,db:Session=Depends(get_db), current_user:schemas.User=Depends(oauth2.get_current_user)):
    post=db.query(models.Post).filter(models.Post.id==vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='the post does not wxist')

    vote_query=db.query(models.Votes).filter(models.Votes.posts_id==votes.post_id,models.Votes.user_id==current_user.id)
    found_vote=vote_query.first()

    if (votes.dir==1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"user with {current_user.id} has aalready voted on {votes.post_id}")
        
        new_vote=models.Votes(post_id=vote.post_id , user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        db.refresh(new_vote)
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='vote does not exist')
        vote_query.delete(synchronize_session=False)
        db.commit()

        return{"message":"was successful"}