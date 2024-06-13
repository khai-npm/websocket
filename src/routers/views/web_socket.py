import websockets


all_clients = []

# gửi tin nhắn đến tất cả các client web đang kết nối tới server websocket
async def send_message(message : str):
    for client in all_clients:
        await client.send(message)


# setting đối với client đã connect được tới web socket
async def new_client_connected(client_socket, path):
    print("new client connected!")
    all_clients.append(client_socket)

    while True:
        new_message = await client_socket.recv()
        print("client sent:", new_message)
        await send_message(new_message)

# khởi chạy server websocket 
async def start_server():
    print("web socket started")
    await websockets.serve(new_client_connected, "localhost", 12345)