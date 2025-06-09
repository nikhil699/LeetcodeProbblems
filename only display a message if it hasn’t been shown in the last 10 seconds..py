# Problem Statement : "Design a program to hide duplicates of any message that has already been displayed within the past 10 seconds."

# That means:

# Print every incoming message ONLY if it has not been printed in the last 10 seconds.

# Do NOT print duplicates within the last 10 seconds.

# Older duplicates (more than 10 seconds ago) are fine to print again.



# Problem with hashmap ke ham remove nahe kar rahe hai 
# The last_seen map keeps growing forever — even for messages that haven’t appeared in hours or days.
# With billions of messages, this causes:
# Memory bloat
# Eventually crashes
# if message not in self.last_seen or timestamp - self.last_seen[message] >= 10:
#             self.last_seen[message] = timestamp
#             return True
#         return False


# Scalable Design Idea:
# Instead of keeping all old messages, we only care about messages within the last 10 seconds.
# We only care about messages seen in the last 10 seconds.
# So, instead of keeping everything forever, we'll:

# ham queue use karenge for tracking the timestanp and message when ever any new timestamp is greater that 10 then remove the 
# first entry from the queue and also if that entry available remove that tooo from set 

from collections import deque

class MessageLogger:
    def __init__(self):
        self.queue = deque()
        self.recent_messages = set()

    def log(self, timestamp, message):
        # Cleanup old messages
        while self.queue and timestamp - self.queue[0][0] >= 10:
            old_time, old_msg = self.queue.popleft()
            self.recent_messages.remove(old_msg)

        if message in self.recent_messages:
            return  # don't print

        print(message)
        self.queue.append((timestamp, message))
        self.recent_messages.add(message)

      



logger = MessageLogger()
inputs = [
    (10, "solar panel activated"),
    (11, "low battery warning"),
    (12, "tire one: low air pressure"),
    (13, "solar panel activated"),
    (14, "low battery warning"),
    (21, "solar panel activated"),
    (35, "solar panel activated"),
    (10, "solar panel activated")
]

for time, msg in inputs:
    logger.log(time, msg)
