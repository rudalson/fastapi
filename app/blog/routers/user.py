from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from blog import schemas, database, models
from sqlalchemy.orm import Session
from blog.repository import user


router = APIRouter(
    prefix='/user',
    tags=['Users']
)
get_db = database.get_db


@router.post('', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get(id, db)


@router.get('', response_model=List[schemas.ShowUser])
def all(db: Session = Depends(get_db)):
    return user.get_all(db)
