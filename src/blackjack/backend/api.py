# Example code from https://fastapi.tiangolo.com/advanced/websockets/

import logging
from contextlib import asynccontextmanager
from typing import Annotated
from uuid import uuid4

from fastapi import (
  Cookie,
  Depends,
  FastAPI,
  Response,
  WebSocket,
  WebSocketDisconnect,
  WebSocketException,
  status,
)

logging.basicConfig(format="%(levelname)s:     %(asctime)s - %(message)s")
LOG = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_app: FastAPI):
  # Startup
  logger = logging.getLogger("uvicorn.access")
  handler = logging.StreamHandler()
  handler.setFormatter(
    logging.Formatter("%(levelname)s:     %(asctime)s - %(message)s")
  )
  logger.addHandler(handler)
  yield
  # Shutdown


API = FastAPI(lifespan=lifespan)


class ConnectionManager:
  def __init__(self):
    self.active_connections: list[WebSocket] = []

  async def connect(self, websocket: WebSocket):
    await websocket.accept()
    self.active_connections.append(websocket)

  def disconnect(self, websocket: WebSocket):
    self.active_connections.remove(websocket)

  async def send_personal_message(self, message: str, websocket: WebSocket):
    await websocket.send_text(message)

  async def broadcast(self, message: str):
    for connection in self.active_connections:
      await connection.send_text(message)


manager = ConnectionManager()


@API.get("/")
async def get():
  try:
    with open("src/web/index.html") as f:
      html = f.read()
      f.close()
      return Response(html, media_type="text/html")
  except OSError as e:
    LOG.fatal(f"Error reading lobby.html: {e}")
    exit(-1)
  except Exception as e:
    LOG.fatal(f"Unexpected error: {e}")
    exit(-1)


@API.get("/script.js")
async def get_script():
  try:
    with open("src/web/script.js") as f:
      file = f.read()
      f.close()
      return Response(file, media_type="application/javascript")
  except OSError as e:
    LOG.fatal(f"Error reading script.mjs: {e}")
    exit(-1)
  except Exception as e:
    LOG.fatal(f"Unexpected error: {e}")
    exit(-1)


@API.get("/api/get-uuid")
async def get_uuid():
  return Response(str(uuid4()), media_type="text/plain")


async def get_token(
  _websocket: WebSocket,
  token: Annotated[str | None, Cookie()] = None,
):
  if token is None:
    raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
  return token


@API.websocket("/ws")
async def websocket_endpoint(
  *,
  websocket: WebSocket,
  token: Annotated[int, Depends(get_token)],
):
  await manager.connect(websocket)
  try:
    while True:
      data = await websocket.receive_text()
      await manager.send_personal_message(f"Your message: {data}", websocket)
      await manager.broadcast(f"Client #{token} sent: {data}")
  except WebSocketDisconnect:
    manager.disconnect(websocket)
    await manager.broadcast(f"Client #{token} left the chat")
