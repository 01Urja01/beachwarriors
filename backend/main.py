from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import setup_routes
from utils import init_database

app = FastAPI(
    title="Beach Warriors API",
    description="FastAPI application with SQLite database",
    version="1.0.0"
)

# CORS middleware - configure as needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database
init_database()

# Setup routes
setup_routes(app)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to Beach Warriors API!",
        "docs": "/docs",
        "version": "1.0.0"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}