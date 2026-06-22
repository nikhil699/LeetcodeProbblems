# 0(n * k * k)
class Solution(object):
    def domain_Count_Problem(self, cpdomains):
        frequencyMap = {}

        for item in cpdomains: # 0(n)
            count, domain = item.split(" ") # pure string scan karne padte hai agar length l hai to 0(l)
            parts = domain.split(".") # 0(l)

            for i in range(len(parts)): # 0(K)
                subdomain = ".".join(parts[i:]) # 0(K)
                if subdomain not in frequencyMap: # 0(1)
                    frequencyMap[subdomain] = int(count)
                else:
                    frequencyMap[subdomain] += int(count)
        

        return frequencyMap

            

sol = Solution()

cpdomains = [
    "900 google.com",
    "50 mail.google.com",
    "1 yahoo.com"
]

print(sol.domain_Count_Problem(cpdomains))