# # app/routers/todo_router.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, crud, database, deps, models

router = APIRouter(prefix="/todos", tags=["todos"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.ToDoOut)
def create_todo(payload: schemas.ToDoCreate, db: Session = Depends(get_db), current_user: models.User = Depends(deps.get_current_user)):
    return crud.create_todo(db, payload, current_user.id)

@router.get("/", response_model=list[schemas.ToDoOut])
def list_todos(db: Session = Depends(get_db), current_user: models.User = Depends(deps.get_current_user)):
    return crud.get_todos_for_user(db, current_user.id)

@router.get("/{todo_id}", response_model=schemas.ToDoOut)
def get_todo(todo_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(deps.get_current_user)):
    todo_obj = crud.get_todo_for_user(db, todo_id, current_user.id)
    if not todo_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return todo_obj

@router.put("/{todo_id}", response_model=schemas.ToDoOut)
def update_todo(todo_id: int, payload: schemas.ToDoCreate, db: Session = Depends(get_db), current_user: models.User = Depends(deps.get_current_user)):
    todo_obj = crud.get_todo_for_user(db, todo_id, current_user.id)
    if not todo_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return crud.update_todo(db, todo_obj, payload.dict())

@router.delete("/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(deps.get_current_user)):
    todo_obj = crud.get_todo_for_user(db, todo_id, current_user.id)
    if not todo_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    crud.delete_todo(db, todo_obj)
    return {"ok": True}









# app/routers/todo_router.py
# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from .. import schemas, crud, models
# from ..deps import get_db, get_current_user

# router = APIRouter(prefix="/todos", tags=["todos"])

# @router.post("/", response_model=schemas.ToDoOut)
# def create_todo(payload: schemas.ToDoCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
#     return crud.create_todo(db, payload, current_user.id)

# @router.get("/", response_model=list[schemas.ToDoOut])
# def list_todos(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
#     return crud.get_todos_for_user(db, current_user.id)
