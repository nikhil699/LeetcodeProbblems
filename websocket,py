import threading  # Imports threading for concurrency
import time       # Imports time for sleeping and timestamping
import websocket  # Imports websocket-client for WebSocket connection
import statistics # Imports statistics for mean and median calculations
from queue import Queue # Imports Queue for thread-safe data transfer

class WebSocketMetricsProcessor:
    def __init__(self, ws_url, batch_interval_seconds=5):
        self.ws_url = ws_url                                    # Stores the WebSocket URL
        self.batch_interval = batch_interval_seconds            # Stores batch interval
        self.data_queue = Queue()                               # Thread-safe queue for received data
        self.metrics_lock = threading.Lock()                    # Lock for thread-safe metric computation
        self.running = False                                    # Flag to control threads

    def on_message(self, ws, message):
        try:
            num = float(message)                # Parses message to number
            self.data_queue.put(num)            # Adds number to queue
        except ValueError:
            pass                               # Ignores non-numeric messages

    def on_error(self, ws, error):
        print(f"WebSocket error: {error}")      # Logs error

    def on_close(self, ws, close_status_code, close_msg):
        print("WebSocket connection closed")    # Logs close event

    def on_open(self, ws):
        print("WebSocket connection established") # Logs open event

    def start_websocket(self):
        self.ws = websocket.WebSocketApp(
            self.ws_url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open
        )
        self.ws.run_forever()                    # Blocks and runs forever

    def batch_processor(self):
        while self.running:
            time.sleep(self.batch_interval)      # Waits for batch interval
            batch = []
            while not self.data_queue.empty():
                batch.append(self.data_queue.get()) # Drains queue
            if batch:
                with self.metrics_lock:
                    mean = statistics.mean(batch)       # Calculates mean
                    median = statistics.median(batch)   # Calculates median
                print(f"Batch metrics -> Mean: {mean}, Median: {median}") # Prints metrics

    def start(self):
        self.running = True                              # Sets running flag
        ws_thread = threading.Thread(target=self.start_websocket, daemon=True)
        batch_thread = threading.Thread(target=self.batch_processor, daemon=True)
        ws_thread.start()                                # Starts WebSocket thread
        batch_thread.start()                             # Starts batch processor thread

    def stop(self):
        self.running = False                             # Stops threads
        if hasattr(self, 'ws'):
            self.ws.close()                              # Closes WebSocket

# Example usage:
processor = WebSocketMetricsProcessor("ws://example.com/socket", batch_interval_seconds=10)
processor.start()
time.sleep(60)   # Runs for 60 seconds
processor.stop()


# ---

# - **Thread Safety**:
#   - Uses `Queue` for safe data sharing between threads.
#   - Protects metric calculation with `metrics_lock`.
# - **Batch Processing**:
#   - Aggregates and processes messages every `k` seconds.
# - **WebSocket**:
#   - Uses `websocket-client` library (`pip install websocket-client`).
#   - Handles message, error, open, and close events.
# - **Metrics**:
#   - Computes mean and median using Python's `statistics` module.
# - **Threading**:
#   - WebSocket and batch processing run on separate threads.

# ---

# **Time Complexity**:
# - Each batch: $O(n)$ for $n$ messages per interval.

# **Space Complexity**:
# - $O(n)$ for storing messages per batch.

# ---

# **Dry Run Example**:
# - Messages: `1, 2, 3, 4, 5` within interval.
# - Mean: $3.0$, Median: $3$

# ---

# **To use:** Replace `"ws://example.com/socket"` with the actual WebSocket endpoint. Start/stop processor as shown in comments.

# ---

# **FINAL ANSWER**