def add_friend_request(req_dict, friends, block):
    """Establishes friend connection between the two specified emails"""
    email1 = req_dict["friends"].pop()
    email0 = req_dict["friends"].pop()

    #check if keys exist in friends dict
    if not friends.has_key(email0):
        friends[email0] = []
    if not friends.has_key(email1):
        friends[email1] = []

    # check if keys exist in block dict
    if not block.has_key(email0):
        block[email0] = []
    if not block.has_key(email1):
        block[email1] = []

    #check if user has blocked requested user, or vice versa
    if email1 in block[email0]:
        return {"success": False, "message": "Requested user has been blocked."}
    if email0 in block[email1]:
        return {"success": False, "message": "You are blocked by the other user."}

    #check if they are already friends
    if email0 in friends[email1] and email1 in friends[email0]:
        return {"success": False, "message": "You are already friends with the user."}

    if not email0 in friends[email1]:
        friends[email1].append(email0)

    if not email1 in friends[email0]:
        friends[email0].append(email1)

    return {"success": True}