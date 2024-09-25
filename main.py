import json

# Membaca data followers
with open('./data/followers_1.json') as f:
    followers_data = json.load(f)

follower = []
for item in followers_data:
    for j in item["string_list_data"]:
        follower.append(j["value"])

# Membaca data following
with open('./data/following.json') as f:
    following_data = json.load(f)

following = []
for item in following_data["relationships_following"]:
    for j in item["string_list_data"]:
        following.append(j["value"])

# Menemukan orang yang diikuti tetapi tidak mengikuti balik
not_following_back = [user for user in following if user not in follower]

# Mencetak hasil
for user in not_following_back:
    print("https://www.instagram.com/" + user)
