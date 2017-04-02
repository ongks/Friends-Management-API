# Friends Management API
"Friends Management" is an API that aims to assist users who wish to build their own social network with simple features like “Friend”, “Block”, “Receive Updates”.

## Installation
Run the start.sh to pip install the necessary modules.

## Usage
A browser extension such as Postman can allow the user to send JSON requests through the API. The data type must be specified as “JSON (application/json)”.

## URL
The general URL is in the form /api/v0/

## Method
The API accepts only request types of GET and POST.

## Features
* **Add Friend**

This feature allows a user to add another user as a friend, on the condition that neither of the users have blocked the other. Both users will be added to each other’s update subscription by default.
The API should receive the following JSON request:

```
{
  friends:
    [
      'andy@example.com',
      'john@example.com'
    ]
}
```

The API should return the following JSON response on success:

```
{
  "success": true
}
```

It will return either of the following JSON response on failure, in cases of invalid JSON request, user has blocked the target, target has blocked the user or if user is already friends with the target:
```
{
  "success": false
  "message" : "Invalid JSON request.",
}

{
  "success": false
  "message" : "Requested user has been blocked.",
}

{
  "success": false
  "message" : "You are blocked by the other user.",
}

{
  "success": false
  "message" : "You are already friends with the user.",
}
```


* **List all friends**

A user can look at the full list of his/her friends through this feature.

The API should receive the following JSON request:

```
{
  email: 'andy@example.com'
}
```

The API should return the following JSON response on success:

```
{
  "success": true,
  "friends" :
    [
      'john@example.com'
    ],
  "count" : 1   
}
```

It will return the following JSON response on failure, in cases of invalid JSON request:
```
{
  "success": false
  "message" : "Invalid JSON request.",
}
```

* **List mutual friends**

A user can also request for a list of mutual friends between another user and himself/herself.

The API should receive the following JSON request:

```
{
  friends:
    [
      'andy@example.com',
      'john@example.com'
    ]
}
```

The API should return the following JSON response on success:

```
{
  "success": true,
  "friends" :
    [
      'common@example.com'
    ],
  "count" : 1   
}
```

It will return the following JSON response on failure, in cases of invalid JSON request:
```
{
  "success": false
  "message" : "Invalid JSON request.",
}
```

* **Subscribe to updates**

A user can also subscribe to updates from another user. However, the user will not be considered friends with target user.

The API should receive the following JSON request:

```
{
  "requestor": "lisa@example.com",
  "target": "john@example.com"
}
```

The API should return the following JSON response on success:

```
{
  "success": true
}
```

It will return either of the following JSON response on failure, in cases of invalid JSON request, user has blocked the target or if user is already following the target:
```
{
  "success": false
  "message" : "Invalid JSON request.",
}

{
  "success": false
  "message" : "Requested user has been blocked.",
}

{
  "success": false
  "message" : "You are already following this user.",
}
```

* **Block updates**

A user can choose not to receive further updates from a target user with this feature. 
If they are connected as friends, then the user will no longer receive notifications from the target user.
If they are not connected as friends, then no new friends connection can be added.

The API should receive the following JSON request:

```
{
  "requestor": "andy@example.com",
  "target": "john@example.com"
}
```

The API should return the following JSON response on success:

```
{
  "success": true
}
```

It will return either of the following JSON response on failure, in cases of invalid JSON request, user has blocked the target or if user is already following the target:
```
{
  "success": false
  "message" : "Invalid JSON request.",
}

{
  "success": false
  "message" : "You have already blocked this user.",
}
```

* **List all recipient email addresses**

This feature allows a user to view all who are eligible of receiving updates from a specified sender email.

The eligibility to receive updates include:

- having a friend connection with the sender
- has subscribed to updates from the sender
- has not blocked updates from the sender
- has been @mentioned in the text

The API should receive the following JSON request:

```
{
  "sender":  "john@example.com",
  "text": "Hello World! kate@example.com"
}
```

The API should return the following JSON response on success:

```
{
  "success": true
  "recipients":
    [
      "lisa@example.com",
      "kate@example.com"
    ]
}
```

It will return following JSON response on failure, in cases of invalid JSON request:
```
{
  "success": false
  "message" : "Invalid JSON request.",
}
```

## Remarks
The API was built using the Flask framework with Python due to the ease of deployment on a local host. While Java was considered as an option, the large number of steps required to deploy it for testing makes it a poor choice for development.
