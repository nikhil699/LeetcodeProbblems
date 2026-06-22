# U = number of user_ips
# C = number of ad_clicks
# P = number of purchases

from collections import defaultdict

class Solution(object):
    def ad_Click_Conversion_Problem(self, user_ips, ad_clicks, purchases):
        ip_to_user = defaultdict(int)

        for IP, user in user_ips:
            ip_to_user[IP] = user
        
        user_purchases = set(purchases)

        click_count = defaultdict(int)
        conversion_count = defaultdict(int)

        for IP, item in ad_clicks:
            click_count[item] += 1

            user = ip_to_user[IP]

            if user in user_purchases:
                conversion_count[item] += 1
        
        result = []

        for adds in click_count:
            result.append(
                "{} of {} {}".format(
                    conversion_count[adds], click_count[adds], adds
                )
            )
        
        return result




sol = Solution()
user_ips = [
    ["122.121.0.1", "User1"],
    ["96.121.0.2", "User2"],
    ["92.130.6.145", "User3"],
    ["122.121.0.250", "User4"]
]
ad_clicks = [
    ["122.121.0.1", "Buy Wool Coats"],
    ["96.121.0.2", "Buy Wool Coats"],
    ["122.121.0.250", "Buy Wool Coats"],
    ["92.130.6.145", "2017 Pet Mittens"],
    ["122.121.0.1", "2017 Pet Mittens"],
    ["122.121.0.250", "The Best Hollywood Coats"]
]
purchases = [
    "User1",
    "User3"
]

print(sol.ad_Click_Conversion_Problem(user_ips, ad_clicks, purchases))