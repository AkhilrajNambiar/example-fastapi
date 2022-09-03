from datetime import timedelta, datetime
from jose import JWTError, jwt
from . import schemas, models, database
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings

# This scheme identifies which path function to check for the Oauth Token
oauth_scheme = OAuth2PasswordBearer(tokenUrl="login")

# To learn more about JWT visit this timestamp in the fastapi course
# https://www.youtube.com/watch?v=0sOvCWFmrtA&t=23570s

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token(data: dict):
  to_encode = data.copy()
  # It has to be datetime.utcnow() else, the expiration time does not work
  expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  # Also, the key for setting up the expiration time should always be 'exp', else it throws an "Can't convert datetime to JSON exception!"
  to_encode.update({"exp": expire})
  access_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return access_token


def verify_access_token(token: str, credential_exception):
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    id: str = payload.get("user_id")
    if id is None:
      raise credential_exception
    token_data = schemas.TokenData(id=id)
    return token_data
  except JWTError:
    raise credential_exception

  
# This function when passed as a dependency first validates the access-token
# and then returns the TokenData
def get_current_user(token: str = Depends(oauth_scheme), db: Session = Depends(database.get_db)):
  credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
  token_data = verify_access_token(token, credentials_exception)
  user = db.query(models.User).filter_by(id = token_data.id).first()
  return user
