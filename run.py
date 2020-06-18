import uvicorn

from src.utils.create_app import create_app
from src.utils.log_config import LOGGING_CONFIG
from fastapi.logger import logger

app = create_app()

@app.on_event("shutdown")
def shutdown_event():
    logger.info('shut down')


@app.on_event("startup")
async def startup_event2():
    logger.info('startup99999')


if __name__ == "__main__":
    uvicorn.run('run:app', host="0.0.0.0", port=8000, workers=4, reload=True, log_config=LOGGING_CONFIG,
                log_level='info', use_colors=False)

