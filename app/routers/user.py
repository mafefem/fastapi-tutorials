from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.Usercreate, db: Session = Depends(get_db)):

    #hash the password
    hashed_passwd = utils.hash(user.password)
    user.password = hashed_passwd

    new_user = models.User(**user.dict())
    db.add(new_user)

    is_email = db.query(models.User).filter(models.User.email == user.email).first()
    if is_email:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The email trying to use is already exist {user.email}")

    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} does not exist")

    return user
