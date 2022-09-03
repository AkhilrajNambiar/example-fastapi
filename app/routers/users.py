from .. import models, schemas, utils
from fastapi import Body, HTTPException, Response, status, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
  prefix="/users",
  tags=["Users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user_with_same_email = db.query(models.User).filter_by(email = user.email).first()
    if user_with_same_email is None:
        hashed_password = utils.get_hashed_password(user.password)
        user.password = hashed_password
        new_user = models.User(
            **user.dict()
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="A user with this email already exists!!"
    )


@router.get("/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter_by(id=user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No user found with the provided id!"
        )
    return user