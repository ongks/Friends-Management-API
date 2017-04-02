import re


def add_friend_request(req_dict, friends, get_updates, block):
    """Establishes friend connection between the two specified emails;
    friends will also automatically subscribe updates to one another"""
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

    # check if keys exist in updates dict
    if not get_updates.has_key(email0):
        get_updates[email0] = []
    if not get_updates.has_key(email1):
        get_updates[email1] = []

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

    if not email0 in get_updates[email1]:
        get_updates[email1].append(email0)

    if not email1 in get_updates[email0]:
        get_updates[email0].append(email1)

    return {"success": True}



def list_friends_request(req_dict, friends):
    """List all friends of the user with the specified email"""
    email = req_dict["email"]

    #check if the email exists in friends dict
    if not friends.has_key(email):
        friends[email] = []

    list_of_friends = friends[email]

    return {"success": True, "friends": list_of_friends, "count": len(list_of_friends)}



def list_mutual_friends_request(req_dict, friends):
    """List all mutual friends between the two users specified"""
    email1 = req_dict["friends"].pop()
    email0 = req_dict["friends"].pop()

    #check if keys exist in friends dict
    if not friends.has_key(email0):
        friends[email0] = []
    if not friends.has_key(email1):
        friends[email1] = []

    mutual_list = []
    for i in friends[email0]:
        if i in friends[email1]:
            mutual_list.append(i)

    return {"success": True, "friends": mutual_list, "count": len(mutual_list)}



def sub_updates_request(req_dict, get_updates, block):
    """Allows user to receive updates from target"""
    target = req_dict["target"]
    req = req_dict["requestor"]

    #check if keys exist in updates dict
    if not get_updates.has_key(req):
        get_updates[req] = []

    # check if keys exist in block dict
    if not block.has_key(req):
        block[req] = []

    #check if user has blocked requested user
    if target in block[req]:
        return {"success": False, "message": "Requested user has been blocked."}

    #check if user is already following the target
    if target in get_updates[req]:
        return {"success": False, "message": "You are already following this user."}
    else:
        get_updates[req].append(target)
        return {"success": True}



def block_updates_request(req_dict, get_updates, block):
    """Allows user to block updates from target"""
    target = req_dict["target"]
    req = req_dict["requestor"]

    #check if keys exist in updates dict
    if not get_updates.has_key(req):
        get_updates[req] = []

    # check if keys exist in block dict
    if not block.has_key(req):
        block[req] = []

    #check if user has blocked requested user
    if target in block[req]:
        return {"success": False, "message": "You have already blocked this user."}
    else:
        # remove target from req's update list
        if target in get_updates[req]:
            get_updates[req].remove(target)
        block[req].append(target)
        return {"success": True}



def list_recipients_request(req_dict, friends, get_updates, block):
    """returns a list of recipients who will receive updates from the sender"""
    sender = req_dict["sender"]
    text = req_dict["text"]

    if not friends.has_key(sender):
        friends[sender] = []

    friend_list = friends[sender]
    updates_list = []
    for i in get_updates:
        if sender in get_updates[i]:
            updates_list.append(i)

    combined_list = friend_list + list(set(updates_list) - set(friend_list))

    #find emails in the text
    pattern = "^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"
    matched_list = re.findall(pattern, text)

    final_recipient_list = combined_list + list(set(matched_list) - set(combined_list))

    for i in final_recipient_list:
        if sender in block[i]:
            final_recipient_list.remove(i)

    return {"success": True, "recipients": final_recipient_list}