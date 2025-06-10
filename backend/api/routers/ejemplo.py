from fastapi import APIRouter
router=APIRouter()
@router.get("/") #localhost/8000:/ejemplo/
async def hola_mundo():
    return {"mensaje": "Hola mundo"}