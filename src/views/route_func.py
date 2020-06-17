from fastapi import APIRouter, Path, Query
from pony.orm import commit
from starlette.responses import FileResponse, Response
from starlette.requests import Request

from src.models import Post

router = APIRouter()


@router.post("/xuchao")
async def json_res(request: Request):
    print(request.url)
    print(request.pony_session)

    with request.pony_session:
        Post(title="第一篇文章", content="Hello world")
        commit()

        p = Post.get(post_pk=1)
        # print(p)
        print(p.post_pk, '|', p.title, '|', p.content)

    return Response('{"code":0000,"msg":"OK"}')

