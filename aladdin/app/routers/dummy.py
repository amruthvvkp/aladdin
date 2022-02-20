from fastapi import APIRouter

router = APIRouter()


@router.get('/dummy_route')
def dummy_route(item: str):
    return {'THe item is': item}
