# Final Time Complexity
# Step 1: O(N)
# Step 2: O(M + N)
# → Total: O(N) + O(M + N) = O(M + 2N)

# Time Complexity: O(M+N)
# Space Complexity: O(N)



from collections import defaultdict           # O(1) — just importing

def numMatchingSubseq(s, words):
    waiting = defaultdict(list)              # O(1) — empty buckets created

    # Step 1: Har word ka first letter bucket mein daalo
    for word in words:                       # O(W)
        it = iter(word)                      # O(1)
        waiting[next(it)].append(it)         # O(1) per word → total O(N)
        # N = total characters in all words (e.g., "a" = 1, "ace" = 3 → N = 1+2+3+3 = 9)

    count = 0                                # O(1)

    # Step 2: Go through string s = "abcde"
    for c in s:                              # O(M), M = len(s)
        current = waiting[c]                 # O(1)
        waiting[c] = []                      # O(1)

        for it in current:                   # Har char in word = O(1), total = O(N)
            nxt = next(it, None)             # O(1)
            if nxt:
                waiting[nxt].append(it)      # O(1)
            else:
                count += 1                   # O(1)

    return count                             # O(1)


s = "abcde"
words = ["a","bb","acd","ace"]

print(numMatchingSubseq(s,words))