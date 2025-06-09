# Design a logger system that receives a stream of messages along with their timestamps, 
# and it should print each message only if it hasn't been printed in the last 10 seconds.

# timestamp is strictly increasing (no need to evict old messages explicitly)
# Messages are strings
# You must return True if message should be printed, False otherwise

# Maintain a HashMap<message, last_printed_timestamp>
# For every incoming (timestamp, message):
# If message not in map → print, store timestamp
# If message seen before:
# If current time - last time >= 10 → update, print
# Else → don’t print
# agar mesaage ka timestamp 10 se chota hai aur wo already mere map mein hai to nahe print karaunga

# Time and Space Complexity
# Time: O(1) per call
# Space: O(N), N = number of distinct messages in 10 seconds

class Logger:
    def __init__(self):
        self.last_seen = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.last_seen or timestamp - self.last_seen[message] >= 10:
            self.last_seen[message] = timestamp
            return True
        return False


logger = Logger()
print(logger.shouldPrintMessage(1, "foo"))  # True
print(logger.shouldPrintMessage(2, "bar"))  # True
print(logger.shouldPrintMessage(3, "foo"))  # False
print(logger.shouldPrintMessage(10, "foo")) # False
print(logger.shouldPrintMessage(11, "foo")) # True
