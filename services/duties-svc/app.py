from fastapi import FastAPI, Depends, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator
from common.crewml_common.jwt_auth import get_current_user
app = FastAPI(title="duties-svc", version="v1.0.0")
Instrumentator().instrument(app).expose(app, endpoint="/metrics", include_in_schema=False)
def Protected(dep=Depends(get_current_user)): return dep
@app.get("/health")
def health(): return {"ok":True,"service":"duties-svc"}
@app.get('/api/duties/info')
def info(user=Protected()): return {'service':'duties-svc'}
