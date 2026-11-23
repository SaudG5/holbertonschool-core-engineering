#!/usr/bin/env python3
"""WebSocket Echo Server"""
import asyncio
import websockets

async def connection_handler(websocket):
    """Handle incoming WebSocket connections and echo messages back to the client."""
    async for message in websocket:
        await websocket.send(message)

async def main():
    """Start the WebSocket server and listen for incoming connections."""
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()  

if __name__ == "__main__":
    asyncio.run(main())
