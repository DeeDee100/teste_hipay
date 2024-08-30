from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import IntegrityError
from app.database.database import get_db
from app.database import models
from app import schemas

router = APIRouter(tags=["Users"])

@router.get("/")
def get_all_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


@router.get("/")
def get_roles(db: Session = Depends(get_db)):
    return (
        db.query(
            models.User.name,
            models.User.email,
            models.Roles.description.label("role_description"),
            models.Claims.description.label("claim_description"),
        )
        .join(models.Roles, models.User.role_id == models.Roles.id)
        .join(models.UserClaims, models.User.id == models.UserClaims.user_id)
        .join(models.Claims, models.Claims.id == models.UserClaims.claim_id)
        .all()
    )


@router.get("/{user_id}")
def get_user_role_by_id(user_id: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    return user.role_id

@router.post("/", status_code=status.HTTP_201_CREATED)
def register_user(user: schemas.UserEntry, db: Session = Depends(get_db)):
    new_user = models.User(**user.dict())
    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)
        return {"message": user.dict()}
    except IntegrityError as err:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail={"message": err.args})
