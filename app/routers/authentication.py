from fastapi import APIRouter,HTTPException,status,Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from ..import schemas,models,oauth2
from sqlalchemy.orm import Session
from ..database import get_db
from ..import utility


router=APIRouter(
    tags=['Authentication']
)

@router.post("/login",response_model=schemas.Token)
def logins(user_credentials:OAuth2PasswordRequestForm=Depends() ,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.email==user_credentials.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"invalid credentials")

    if not utility.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f'not avalable')
    
    
    access_token=oauth2.create_acess_token(data={'user_id':user.id})
    return{'access_token' : access_token , "token_type": "bearer"}

    

    return {'data':'token access'}