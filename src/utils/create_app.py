from fastapi import FastAPI
from src.views import route_func
from pony.orm import db_session
from starlette.requests import Request


def create_app():
    app = FastAPI(title='FastApi pony study',
                  description='这是使用fastapi与pony orm进行实践的项目',
                  version=0.1)

    @app.on_event("startup")
    def _enter_session():
        print('加载DB_session')
        session = db_session()
        Request.pony_session = session
        session.__enter__()

    @app.on_event("shutdown")
    async def _exit_session(exception):
        print('释放DB_session')
        session = getattr(Request, 'pony_session', None)
        if session is not None:
            session.__exit__(exc=exception)

    app.include_router(
        route_func.router,
        prefix="/items",
        tags=["items"],
        dependencies=[],
        responses={404: {"description": "Not found"}},
    )

    return app
