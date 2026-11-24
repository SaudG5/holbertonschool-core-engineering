#!/usr/bin/env python3
"""A simple WebSocket client that connects to the echo server."""
import asyncio
import websockets

async def connect_and_send(uri: str, text: str) -> str:
    """Connect to the WebSocket server, send a message, and receive the echo."""
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        response = await websocket.recv()
        return response

async def main():
    response = await connect_and_send("ws://localhost:8765", "Hello, WebSocket!")
    print(f"Received: {response}")

if __name__ == "__main__":
    asyncio.run(main())
