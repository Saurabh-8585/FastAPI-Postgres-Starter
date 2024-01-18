from fastapi import APIRouter, HTTPException, Depends, Body
from sqlalchemy.orm import Session
import psycopg2.extras

from src.routes import get_raw_db, get_db

router = APIRouter()


@router.get('/get_all_users')
def get_user(
        rdb: Session = Depends(get_raw_db),

):
    try:
        cursor = rdb.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = f"select * from users"
        cursor.execute(query)
        data=cursor.fetchall()
        return data
    except Exception as e:
        print(e)


@router.post('/add_user')
def add_user(
        user_name: str = Body(...),
        user_address: str = Body(...),
        user_age: int = Body(...),
        rdb: Session = Depends(get_raw_db),
        db: Session = Depends(get_db),

):
    try:
        cursor = rdb.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = f"INSERT INTO users( u_name,u_address,u_age) values( '{user_name}','{user_address}',{user_age})"
        cursor.execute(query)
        rdb.commit()
        return True
    except Exception as e:
        print(e)
