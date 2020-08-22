import asyncio
import websockets
from flask import Flask, request, render_template

async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, '127.0.0.1', 8765))
asyncio.get_event_loop().run_forever()
