from fastapi import FastAPI, Response
from backend.app.core.config import get_config

def create_app():
    app_instance = FastAPI(title="RealKEstate", version="1.0.0")
    app_instance.state.env = get_config()
    
    # routers
    
    @app_instance.get("/health")
    def health():
        return Response(content="ok" media_type="text/plain", status_code=200)
    
    return app_instance

app = create_app