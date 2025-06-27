# so the rate limiter being here as supopose any new request come i will check wheather that request being
# comes in a time span of 60 sec if yes then check the size of the rate limitter if it is in boundry then allow that request
# Time Complexity : 0(1) since each user request is added and removed from the queue at most once per 60s window.
# Space Complexity : 0(U * L) where U is the number of users and L is the limit each user can store up to L timestamps
from collections import defaultdict, deque
import queue


class RateLimiter:
    def __init__(self,limit):
        self.limit = limit
        self.user_requests = defaultdict(deque)
    
    def allowRequest(self,userId,timestamp):

        q = self.user_requests[userId]

        while q and timestamp - q[0] >= 60:
            q.popleft()
        

        if len(q) < self.limit:
            q.append(timestamp)
            return True

        else:
            return False


# Test Cases for RateLimiter

def test_rate_limiter():
    print("Test 1: Basic single user within limit")
    rl = RateLimiter(3)
    assert rl.allowRequest("user1", 1) == True
    assert rl.allowRequest("user1", 10) == True
    assert rl.allowRequest("user1", 20) == True
   

    print("Test 2: Exceeding limit")
    assert rl.allowRequest("user1", 30) == False  # 4th request within 60s

    print("Test 3: Sliding window - old requests removed")
    assert rl.allowRequest("user1", 62) == True  # First request (at 1) is now outside 60s window

    print("Test 4: Multiple users")
    assert rl.allowRequest("user2", 5) == True
    assert rl.allowRequest("user2", 15) == True
    assert rl.allowRequest("user2", 25) == True
    assert rl.allowRequest("user2", 35) == False

    print("Test 5: Requests at the same timestamp")
    rl2 = RateLimiter(2)
    assert rl2.allowRequest("user3", 100) == True
    assert rl2.allowRequest("user3", 100) == True
    assert rl2.allowRequest("user3", 100) == False

    print("Test 6: No requests for a long time")
    assert rl2.allowRequest("user3", 200) == True  # All previous requests are more than 60s old

    print("All test cases passed!")

test_rate_limiter()


    
