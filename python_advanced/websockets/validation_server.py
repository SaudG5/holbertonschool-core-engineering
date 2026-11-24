#!/usr/bin/env python3
"""A WebSocket server that validates incoming messages."""
import asyncio
import websockets


async def connection_handler(websocket):
    """Reply ERR:EMPTY for empty messages, else OK:<message>."""
    async for message in websocket:
        if message.strip() == "":
            await websocket.send("ERR:EMPTY")
        else:
            await websocket.send(f"OK:{message}")


async def main():
    """Start the server on localhost:8765."""
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
