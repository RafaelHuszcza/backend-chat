# from flask_socketio import emit, join_room, leave_room
# from . import socketio, db
# import asyncio
# import threading

# class RoomManager:
#     def __init__(self):
#         self.rooms = {}

#     def start_room(self, room_id):
#         if room_id not in self.rooms:
#             thread = threading.Thread(target=self.room_thread, args=(room_id,))
#             thread.daemon = True
#             thread.start()
#             self.rooms[room_id] = thread

#     def room_thread(self, room_id):
#         while True:
#             # Aqui você pode adicionar lógica para executar em cada sala
#             pass

# room_manager = RoomManager()

# @socketio.on('join')
# def on_join(data):
#     username = data['username']
#     room = data['room']
#     join_room(room)
#     emit('message', f'{username} has entered the room.', room=room)
#     room_manager.start_room(room)

# @socketio.on('leave')
# def on_leave(data):
#     username = data['username']
#     room = data['room']
#     leave_room(room)
#     emit('message', f'{username} has left the room.', room=room)

# @socketio.on('message')
# def handle_message(data):
#     room = data['room']
#     msg = data['message']
#     username = data['username']
#     message = f'{username}: {msg}'
#     query = "INSERT INTO messages (room_id, content) VALUES ($1, $2)"
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     loop.run_until_complete(db.execute(query, room, message))
#     emit('message', message, room=room)
