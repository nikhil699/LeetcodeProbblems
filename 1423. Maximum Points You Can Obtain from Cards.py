# Time: O(k) — we try k+1 combinations
# Space: O(1) — constant extra space
 1

Graph and disjoint set related question
# 1. Why do we prefer using a char[] over string to store passwords in Java?
# 1) what is marker interface
# 2) Why use a marker interface?
# 3) when to use interface and abstract class?
# 4) what is the use of constructor in java?
# 5) what is static method
# 6) can we use static method in constructor
# 7) what is the contract between hashcode and equals methods
# 8) what is failfast iteration and how will we resolve
# 9) what are virtualthreads
# 10) diff between map vs flatmap in java8
# 11) what are sealed classes
# 12) what are spring boot advantages
# 13) what is application context
# 14) what are the scope in spring
# 15) diff between prototype and request scope
# 16) what are components of kafka
# 17) what is partition in kafka
# 18) how to handle if consumer keeps on failing
# 2. What are java streams and describe their lifecycle?
# How do you Authenticate when somebody trying to access your API?
# 3. Write a java program using streams to:
# Filter employees with age > 18
# Sort them by last name and then by age
# Return only their email id's in a list
# 5)What is Difference between JWT token and Bearer token?
# 6)How do you authorize bearer token?
# 4. Write a java stream program to find the player with the highest runs. If multiple players have the same highest score, return a default player.
# 16)What is Dependency Injection?
# 17)what are the types in Dependency Injection?
# 18)What is the best way in Dependency Injection?
# 19)What is Immutability means ? is String is Immutable?
# 20)How do you make Immutability in Custom Objects?
# 21)What is Encapsulation?
# 22)In Encapsulation can we make fields as Public?
# 23)I want to create a custom object to String that is Immutable how do you create?
# 24)can you override fields in Java?
# 25)Can you tell me some of the Pitfall methods or issues in Java Streams?
# 5. How do you maintain data consistency across microservices?
# 1. Design a URL shortening service like bitly.
# 2. Design a distributed key-value store like Redis.
# 3. Design a scalable social network like Facebook.
# 4. Design a scalable recommendation system like Netflix.
# 5. Design a distributed file system like Hadoop's HDFS.
# 6. Design a real-time messaging system like WhatsApp.
# 7. Design a web crawler like Google.
# 8. Design a distributed cache like Memcached.
# 9. Design a content delivery network (CDN) like Cloudflare.
# 10. Design a scalable search engine like Google.
# 11. Design a ride-sharing system like Uber.
# 12. Design a video streaming service like YouTube.
# 13. Design an online food delivery system like Zomato.
# 14. Design a collaborative document editing system like Google Docs.
# 15. Design an e-commerce platform like Amazon.
# 16. Design a recommendation system for an online marketplace.
# 17. Design a fault-tolerant distributed database system.
# 18. Design a scalable event-driven system like Twitter.
# 19. Design a scalable photo-sharing platform like Instagram.
# 20. Design a distributed task scheduling system.
# 6. In a dynamic cloud environment, how do microservices discover and communicate with each other?

# 7. Circuit breaker pattern?, How is it implemented in microservices?

# 8. What is a rate limiter?

# 9. Authentication vs Authorization. How do you implement them in an application?

# 10. What happens when a prototype-scoped bean is injected into a singleton-scoped bean in spring?

# 11. What are zero downtime deployment strategies?

# Low-Level Design → Focused on core interview-ready problems like a Quiz Platform, Parking Lot System, Rate Limiter, 
# and Multithreaded Task Scheduler in Java. Emphasized clean OOP, SOLID principles, design patterns, 
# and proper concurrency handling — practiced consistently, not just before interviews.


# • Behavioral Rounds → Gave them equal weight. Prepared well-structured stories 
# for real scenarios — conflict resolution, taking ownership, and learnings from failure. 
# These rounds can absolutely impact the final decision.


# • DSA with Patterns → Prioritized depth over volume. Revisited core patterns like DP, 
# Union-Find, and Sliding Window until I could solve confidently. Categorized problems by technique — not 
# just solving for the sake of it.
# Round 2: LLD + System Design + SQL
# I was asked to explain the architecture and design decisions of the projects I worked on at my previous company.
# Follow-up questions included:
#  ⚙️ How did you handle configuration management and service-to-service communication?
#  📈 What challenges did you face in scaling?
#  🔄 How did you handle failures and retries in distributed systems?
#  🧠 Where did you use caching and what kind

# 1st I was asked about OOPS concept.
# 2nd I was asked abstract class, its implementation, etc.
# Then I was asked how Abstract class is different from interface and to implement interface.
# Then, some code snippets were given to me and I was asked for code-pair and do some operations on abstract class 
# and interfaces examples. This was very complex to be honest and java concepts to the core were tested here. 
# Then, I was asked if 2 interfaces can be implemented by abstract.
# Next, I was asked to implement polymorphism.
# Then threading in java was asked and was to create the thread(extending the class, implementing runnable 
# interface, implementing callable).
# Then, a LLD snapshot was given and I was given api contracts, I had to design models their data-types, 
# repository, service and controller(only pseudo-code was asked). Then, I was asked to use SQL for data implementation 
# as earlier I was using in-memory storage.





class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        total = 0

        for i in range(0,k):
            total = total + cardPoints[i]
        
        maximumResult = total

        for i in range(0,k):
            total = total - cardPoints[k - 1 - i]
            total = total + cardPoints[n - 1 - i]
            maximumResult = max(maximumResult,total)
        
        return maximumResult



sol = Solution()
cardPoints = [1,2,3,4,5,6,1]
k = 3

print(sol.maxScore(cardPoints,k))