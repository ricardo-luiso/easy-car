from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException
from jose import JWTError
from .auth import decode_access_token
from api.routers import usuario
from .database import AsyncSessionLocal

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials.strip()
    
    # Sanity check
    if token.count(".") != 2:
        raise HTTPException(status_code=401, detail="Token malformado")
    
    try:
        payload = decode_access_token(token)
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Token inválido")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
    
    db = AsyncSessionLocal()
    user = db.query(usuario).filter_by(username=username).first()
    db.close()
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user
