from fastapi import APIRouter, FastAPI


router = APIRouter(prefix="/api")


@router.get("/mail")
async def root():
    return {"message": "Send an email now."}
