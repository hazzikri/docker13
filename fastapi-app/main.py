from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from datetime import datetime

app = FastAPI(
    title="FastAPI Docker Tutorial",
    description="Simple FastAPI application for Docker learning",
    version="1.0.0"
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/hello")
async def hello_api():
    return {
        "message": "Hello from FastAPI!",
        "status": "success",
        "timestamp": datetime.now().isoformat(),
        "framework": "FastAPI",
        "python_version": "3.9+"
    }

@app.get("/api/info")
async def app_info():
    return {
        "app_name": "FastAPI Docker Tutorial",
        "version": "1.0.0",
        "framework": "FastAPI",
        "docs_url": "/docs",
        "redoc_url": "/redoc",
        "status": "running"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "FastAPI App",
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)