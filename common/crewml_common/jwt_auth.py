from fastapi import Header, HTTPException
async def get_current_user(authorization: str = Header(...), oidc_issuer: str = None, audience: str = None):
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=401, detail="Missing bearer token")
    return {"sub":"demo","roles":["planner"]}
