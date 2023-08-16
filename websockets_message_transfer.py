import asyncio
import nest_asyncio
import websockets
import json
import heapq
import time

nest_asyncio.apply()

N = 10
heap = []
ordered_messages = []
WS_URL = "wss://test-ws.skns.dev/raw-messages"
SEND_URL = "wss://test-ws.skns.dev/ordered-messages/nikishina"
# WS_URL = "ws://127.0.0.1:7890"
# SEND_URL = "ws://127.0.0.1:7888"

def validate_message_order(messages_for_validation):
    for i in range(1, len(messages_for_validation)):
        if messages_for_validation[i]['id'] < messages_for_validation[i - 1]['id']:
            print("Messages are not ordered by 'id'")
    print("Messages are ordered by 'id'")

async def process_messages():
    async with websockets.connect(WS_URL) as websocket:
        while len(heap)<N:
            message = await websocket.recv()
            try:
                parsed_message = json.loads(json.dumps(message))
                parsed_message=json.loads(parsed_message.replace("\'", "\""))
                heapq.heappush(heap, (parsed_message['id'], parsed_message))
            except json.JSONDecodeError:
                print("Invalid JSON format:", message)
            except websockets.exceptions.ConnectionClosedOK:
                print("Connection closed by client")

        ordered_messages = [heapq.heappop(heap)[1] for _ in range(len(heap))]
        validate_message_order(ordered_messages)
        
    async with websockets.connect(SEND_URL) as websocket:
        for ordered_message in ordered_messages:
            try:
                await websocket.send(str(ordered_message))
            except websockets.exceptions.ConnectionClosedOK:
                print("ConnectionClosedOK error encountered during sending.")

start_time = time.time()
asyncio.get_event_loop().run_until_complete(process_messages())
end_time = time.time()
total_time_taken=end_time - start_time

print(f"Total time taken: {total_time_taken:.4f} seconds")