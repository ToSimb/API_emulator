from fastapi import APIRouter, HTTPException

from freon.service import open_json

router = APIRouter(
    prefix="/freon",
    tags=["Freon"]
)

@router.get("/{name_str}")
async def api_fb(name_str: str):
    try:
        result = open_json(name_str)
        return result
    except FileNotFoundError:
        return ("нет такого файла")
    except Exception as e:
        error_str = f"Exception: {e}."
        raise HTTPException(status_code=527, detail={"error_msg": error_str})