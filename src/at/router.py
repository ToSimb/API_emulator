import time

from fastapi import APIRouter, HTTPException
from fastapi.responses import Response

from myException import MyException427, MyException428, MyException429, MyException527, MyException528
from at.schemas import AgentScheme, SchemeJson

router = APIRouter(
    prefix="/at",
    tags=["PC AT"]
)

@router.post("/agent-scheme")
async def api_gent_scheme(agent_scheme: AgentScheme, agent_id: int = None, agent_reg_id: str = None):
    all_agent_scheme = {
        "scheme_revision": agent_scheme.scheme_revision,
        "metric_info_list": agent_scheme.metric_info_list,
        "scheme": {
            "metrics": agent_scheme.scheme.metrics,
            "templates": agent_scheme.scheme.templates,
            "item_id_list": agent_scheme.scheme.item_id_list,
            "join_id_list": agent_scheme.scheme.join_id_list,
            "item_info_list": agent_scheme.scheme.item_info_list
        }
    }
    try:
        if agent_reg_id == None and agent_id == None:
            raise MyException428("428")
        item_id_list = all_agent_scheme["scheme"]["item_id_list"].copy()
        if agent_id:
            print(agent_id)
            i = 10
            for item_id in item_id_list:
                item_id["item_id"] = i
                i += 1
            json_agent_return = {
                "agent_id": agent_id,
                "item_id_list": item_id_list
            }
            return json_agent_return
        if agent_reg_id:
            i = 1
            for item_id in item_id_list:
                item_id["item_id"] = i
                i += 1
            json_agent_return = {
                "agent_id": 1,
                "item_id_list": item_id_list
            }
            return json_agent_return
    except MyException428 as e:
        raise HTTPException(status_code=428, detail={"error_msg": str(e)})
    except Exception as e:
        error_str = f"Exception: {e}."
        raise HTTPException(status_code=527, detail={"error_msg": error_str})

@router.post("/params")
async def params_data(params: dict, agent_id: int):
    print(params)
    time.sleep(1)
    return Response(status_code=200)

@router.get("/check")
async def get_checks(agent_id: int, user_query_interval_revision: int):
    try:
        print("CHECK - agent_id:", agent_id)
        if user_query_interval_revision == 2:
            return Response(status_code=227)
        else:
            return Response(status_code=200)
    except Exception as e:
        error_str = f"{e}."
        raise HTTPException(status_code=527, detail={"error_msg": error_str})