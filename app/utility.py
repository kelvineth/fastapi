from passlib.context import CryptContext
cwd_context=CryptContext(schemes=["bcrypt"] ,deprecated="auto")


def hash(password:str):
    return cwd_context.hash(password)


def verify(plain_password,hashed_password):
    return cwd_context.verify(plain_password,hashed_password)