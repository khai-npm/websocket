import websockets


all_clients = []

async def send_message(message : str):
    for client in all_clients:
        await client.send(message)

async def new_client_connected(client_socket, path):
    print("new client connected!")
    all_clients.append(client_socket)

    while True:
        new_message = await client_socket.recv()
        print("client sent:", new_message)
        await send_message(new_message)

async def start_server():
    print("web socket started")
    await websockets.serve(new_client_connected, "localhost", 12345)