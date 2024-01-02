from fastapi import APIRouter, HTTPException
from property_manager_api.web.api.work_orders.schema import (
    MaintenaceRequestText,
    MaintenaceRequest,
)
from property_manager.main import convert_to_service_order

router = APIRouter()


@router.post("/", response_model=MaintenaceRequest)
async def transform_work_order(
    incoming_message: MaintenaceRequestText,
) -> MaintenaceRequest:
    """
    Transforms a tenant maintenance request message into structured request.

    :param incoming_message: incoming message.
    :returns: structured request.
    """
    try:
        transformed_data = convert_to_service_order(incoming_message.message)
        if not isinstance(transformed_data, dict):
            raise ValueError("Returned data is not a dictionary")
        return MaintenaceRequest(data=transformed_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
