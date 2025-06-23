from fastapi import FastAPI
from api.routes import scrape_routes, ai_routes, version_routes

app = FastAPI()
app.include_router(scrape_routes.router)
app.include_router(ai_routes.router)
app.include_router(version_routes.router)
