import json

topManager1 = {
    "id": 1,
    "name": "Cassandra"
}
topManager2 = {
    "id": 2,
    "name": "Pythonia",
}
middleManager1 = {
    "id": 3,
    "managerId": topManager1["id"],
    "name": "Ruby"
}
middleManger2 = {
    "id": 4,
    "managerId": topManager2["id"],
    "name": "Monilla"
}
bottomManager = {
    "id": 5,
    "managerId": middleManager1["id"],
    "name": "Nona"
}
user1 = {
    "id": 6,
    "managerId": bottomManager["id"],
    "name": "Richard"
}
user2 = {
    "id": 7,
    "managerId": middleManager1["id"],
    "name": "Paul"
}
user3 = {
    "id": 8,
    "managerId": bottomManager["id"],
    "name": "Kris"
}

users = [user1, topManager1, middleManager1, middleManger2, bottomManager, user2, user3, topManager2]


def get_management_tree(users):
    output = []
    for user in users:
        # O(n^2)log(n)
        if not "managerId" in user:
            team = find_team_members(users, user)
            temp = { "id": user["id"], "name": user["name"], "team": team}
            output.append(temp)
    return output 

def find_team_members(users, manager):
#     log(n)
    team = []
    for user in users:
        if "managerId" in user and user["managerId"] == manager["id"]:
            user["team"] = find_team_members(users, user)
            team.append(user)
    return team



print(json.dumps(get_management_tree(users), indent=4))
# 
# output = [
#   {
#     "id": 1,
#     "name": "Cassandra",
#     "team": [
#       {
#         "id": 3,
#         "managerId": 1,
#         "name": "Ruby",
#         "team": [
#           {
#             "id": 5,
#             "managerId": 3,
#             "name": "Nona",
#             "team": [
#               {
#                 "id": 6,
#                 "managerId": 5,
#                 "name": "Richard",
#                 "team": []
#               },
#               {
#                 "id": 8,
#                 "managerId": 5,
#                 "name": "Kris",
#                 "team": []
#               }
#             ]
#           },
#           {
#             "id": 7,
#             "managerId": 3,
#             "name": "Paul",
#             "team": []
#           }
#         ]
#       }
#     ]
#   },
#   {
#     "id": 2,
#     "name": "Pythonia",
#     "team": [
#       {
#         "id": 4,
#         "managerId": 2,
#         "name": "Monilla",
#         "team": []
#       }
#     ]
#   }
# ]