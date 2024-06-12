import asyncio

from src.routers.views.web_socket import start_server

def start_websocket_app():
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(start_server())
    event_loop.run_forever()