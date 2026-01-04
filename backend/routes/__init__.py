from fastapi import APIRouter
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import all route modules here
from routes.users import router as users_router

# You can add more routers as you create more route files
# from .other_routes import router as other_router

def setup_routes(app):
    """Setup all routes for the application."""
    api_router = APIRouter(prefix="/api")
    
    # Include all route modules
    api_router.include_router(users_router, prefix="/users", tags=["users"])
    # api_router.include_router(other_router, prefix="/other", tags=["other"])
    
    app.include_router(api_router)
