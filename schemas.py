"""
This page details the schema specifying the JSON formats for validation purposes.
"""

from jsonschema import validate
import re

pattern = "^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"

FriendsPairSchema = {
    "$schema": "http://json-schema.org/schema#",
    "title": "Friends Pair",
    "type" : "object",
    "properties" : {
        "friends" : {
            "type" : "array",
            "items" : {
                "type" : "string",
                "format" : "email",
                "pattern" : pattern
            },
            "minItems": 2,
            "maxItems": 2,
            "uniqueItems": True
        }
    },
    "required": ["friends"]
}

SingleEmailSchema = {
    "$schema": "http://json-schema.org/schema#",
    "title": "Single Email",
    "type" : "object",
    "properties" : {
        "email" : {
            "type" : "string",
            "format" : "email",
            "pattern" : pattern,
            "minItems": 1,
            "maxItems": 1
        }
    },
    "required": ["email"]
}

RequestorTargetSchema = {
    "$schema": "http://json-schema.org/schema#",
    "title": "Requestor-Target Pair",
    "type" : "object",
    "properties" : {
        "requestor" : {
            "type" : "string",
            "format" : "email",
            "pattern" : pattern,
            "minItems": 1,
            "maxItems": 1
        },
        "target" : {
            "type" : "string",
            "format" : "email",
            "pattern" : pattern,
            "minItems": 1,
            "maxItems": 1
        },
    },
    "required": ["requestor", "target"]
}

SenderTextSchema = {
    "$schema": "http://json-schema.org/schema#",
    "title": "Sender-Text Pair",
    "type" : "object",
    "properties" : {
        "sender" : {
            "type" : "string",
            "format" : "email",
            "pattern": pattern,
            "minItems": 1,
            "maxItems": 1
        },
        "text" : {
            "type" : "string",
            "minItems": 1,
            "maxItems": 1
        },
    },
    "required": ["sender", "text"]
}

def validate_friends_pair(jsonReq):
    validate(jsonReq, FriendsPairSchema)

def validate_single_email(jsonReq):
    validate(jsonReq, SingleEmailSchema)

def validate_requestor_target(jsonReq):
    validate(jsonReq, RequestorTargetSchema)

def validate_sender_text(jsonReq):
    validate(jsonReq, SenderTextSchema)