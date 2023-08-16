# Messages transfer with WebSoockets
Python code demonstrates a method to order and process messages received from a WebSocket connection. 
The code uses asynchronous programming, a heap data structure and the websockets library.

## Functionality
Python code establishes a WebSocket connection to receive messages (WS_URL) and a separate WebSocket connection to send ordered messages (SEND_URL). 
It processes incoming messages, orders them based on their 'id' field using a N-sized heap and then sends the ordered messages over the sending WebSocket connection.
The messages received from WS_URL follow the format {"id": int, "text": int}, where "id" represents the message ID and "text" represents the message content.

## Sources
WebSockets:

WS_URL = "wss://test-ws.skns.dev/raw-messages"

SEND_URL = "wss://test-ws.skns.dev/ordered-messages/nikishina"

## Usage Instructions
Ensure you have Python3+ installed on your system.
Install the required dependencies (websockets v.11.0.3, nest_asyncio v.1.5.1) by running the following command:

```
pip install websockets
```
and
```
pip install nest_asyncio
```
Run the script using the following command:
```
websockets_message_transfer.py
```

## Description
WebSocket Communication: The websockets library is used to establish WebSocket connections with two different URLs: WS_URL for receiving messages and SEND_URL for sending ordered messages.

Asynchronous Programming: The script extensively uses asynchronous programming. This allows concurrent processing of incoming and outgoing messages, improving performance and responsiveness.

Heap Data Structure: The heapq module is employed to maintain heap for efficient ordering of incoming messages. The heap ensures that messages with lower 'id' values are processed first.

Message Processing Loop: The process_messages() function receives messages from the WebSocket connection specified by WS_URL. It processes each message, extracts the 'id', and inserts it into the heap. This loop continues until a certain number of messages (N) are processed.

Message Sending Loop: Once the required number of messages is received and ordered in the heap, the script establishes a new WebSocket connection using SEND_URL. It then sends the ordered messages over this connection in the order determined by the heap.

Error Handling: The script includes error handling using try-except blocks to handle cases such as invalid JSON format or connection closures. These error handlers ensure that the program continues running smoothly even in the presence of errors.

Message Order Validation: The validate_message_order() function ensures that the ordered messages are correctly ordered by their 'id' fields. It checks for any violations in the ordering and provides feedback on whether the ordering is correct.

Timing and Performance Measurement: The script measures the total time taken for the entire process, including receiving, ordering, and sending messages. This provides insights into the efficiency of the implementation and helps identify potential performance bottlenecks.
