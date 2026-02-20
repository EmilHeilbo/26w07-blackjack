# Example code from https://fastapi.tiangolo.com/advanced/websockets/

import logging
from typing import Annotated

from fastapi import (
  Cookie,
  Depends,
  FastAPI,
  Query,
  WebSocket,
  WebSocketException,
  status,
)
from fastapi.responses import HTMLResponse

api = FastAPI()


@api.get("/")
async def get():
  try:
    with open("src/web/index.html", "r") as f:
      html = f.read()
      logging.info("f.read() from html:")
      logging.info(html)
      f.close()
      return HTMLResponse(html)
  except OSError as e:
    logging.fatal(f"Error reading lobby.html: {e}")
    exit(-1)
  except Exception as e:
    logging.fatal(f"Unexpected error: {e}")
    exit(-1)


async def get_cookie_or_token(
  websocket: WebSocket,
  session: Annotated[str | None, Cookie()] = None,
  token: Annotated[str | None, Query()] = None,
):
  if session is None and token is None:
    raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
  return session or token


@api.websocket("/items/{item_id}/ws")
async def websocket_endpoint(
  *,
  websocket: WebSocket,
  item_id: str,
  q: int | None = None,
  cookie_or_token: Annotated[str, Depends(get_cookie_or_token)],
):
  await websocket.accept()
  while True:
    data = await websocket.receive_text()
    await websocket.send_text(
      f"Session cookie or query token value is: {cookie_or_token}"
    )
    if q is not None:
      await websocket.send_text(f"Query parameter q is: {q}")
    await websocket.send_text(f"Message text was: {data}, for item ID: {item_id}")
