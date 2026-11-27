#!/usr/bin/env python3
"""ASGI app with Starlette: HTML page on / and WebSocket echo on /ws."""
import asyncio
import websockets
from starlette import applications, responses, routing

    
async def homepage(request):
    """Return the HTML page."""
    return responses.HTMLResponse("<h1>WebSocket Echo</h1>")


async def websocket_endpoint(websocket):
    """Accept the connection and echo the text message back."""
    await websocket.accept()
    async for message in websocket.iter_text():
        await websocket.send_text(message)


app = applications.Starlette(routes=[
    routing.Route("/", homepage),
    routing.WebSocketRoute("/ws", websocket_endpoint),
])
