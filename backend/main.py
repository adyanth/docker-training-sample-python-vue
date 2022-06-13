from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from pathlib import Path

from apiv1 import api as apiv1

app = FastAPI()

ui = Path.cwd() / "ui"

app.mount("/ui", StaticFiles(directory=ui, html=True), name="ui")

app.mount("/api/v1", apiv1)


@app.get("/")
async def root():
    return RedirectResponse("/ui/")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", workers=1, port=8080)
