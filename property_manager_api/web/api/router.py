from fastapi.routing import APIRouter
from property_manager_api.web.api import docs
from property_manager_api.web.api import work_orders
from property_manager_api.web.api import monitoring

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(docs.router)
api_router.include_router(work_orders.router, prefix="/work-order", tags=["work orders"])