from fastapi import FastAPI
from app.controllers.chat_controller import router as chat_router
from app.config.settings import Settings

def create_app() -> FastAPI:
    """Create FastAPI application"""
    settings = Settings()
    
    app = FastAPI(
        title=settings.app_name,
        debug=settings.debug,
        version="1.0.0",
        description="AI Agent API Case Henrique Souza",
    )
    
    # Include routers
    app.include_router(chat_router)
    
    @app.get("/")
    async def root():
        return {"message": "AI Agent API is running!"}
    
    @app.get("/health")
    async def health_check():
        return {"status": "healthy"}
    
    return app

# Create app instance
app = create_app()

# Para desenvolvimento local
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
