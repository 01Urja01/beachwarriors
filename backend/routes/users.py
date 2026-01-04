from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List, Optional
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import execute_query, execute_update

router = APIRouter()


class UserCreate(BaseModel):
    name: str
    email: EmailStr


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    created_at: str


@router.get("/", response_model=List[UserResponse])
async def get_users():
    """Get all users."""
    try:
        users = execute_query("SELECT id, name, email, created_at FROM users")
        return [dict(user) for user in users]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    """Get a specific user by ID."""
    try:
        users = execute_query("SELECT id, name, email, created_at FROM users WHERE id = ?", (user_id,))
        if not users:
            raise HTTPException(status_code=404, detail="User not found")
        return dict(users[0])
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreate):
    """Create a new user."""
    try:
        user_id = execute_update(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (user.name, user.email)
        )
        users = execute_query("SELECT id, name, email, created_at FROM users WHERE id = ?", (user_id,))
        return dict(users[0])
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: int):
    """Delete a user by ID."""
    try:
        execute_update("DELETE FROM users WHERE id = ?", (user_id,))
        return None
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
