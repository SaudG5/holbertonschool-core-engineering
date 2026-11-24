#!/usr/bin/env python3
"""A simple WebSocket client that connects to the echo server."""
import asyncio
import websockets


async def connect_and_send(uri: str, text: str) -> str:
    """Connect to uri, send text once, and return the reply."""
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        response = await websocket.recv()
        if len(response) == 0:
             print("ERR:EMPTY")
        else:
            print(f"OK:{response}")


async def main():
    """Send 'Hello WebSocket' to the server and print the reply."""
    response = await connect_and_send("ws://localhost:8765", "")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
