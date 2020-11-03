# This file will be used for all the functions of the MongDB database

import pymongo
from pymongo import MongoClient

# Connecting to the Cluster
cluster = MongoClient(
    "mongodb+srv://abhijeet:1584@cluster0.3vcng.mongodb.net/test?retryWrites=true&w=majority")
print('Connected to mongodb')

db = cluster['test']  # Setting the Database from the Cluster
collection = db['test']  # Setting the collection from the Database


def update_user(userid, serverid):
    ID = userid + serverid
    member_list = collection.find({'_id': ID})  # Fetching whole data
    data = []
    xp = 0
    for member in member_list:
        xp = member['xp']
        data.append(member)

    if not data:
        new_user(userid=userid,serverid=serverid)

    else:
        xp += 1
        collection.update_one({'_id':ID},{'$set':{'xp':xp}})


def new_user(userid, serverid):
    ID = userid + serverid
    collection.insert_one({"_id": ID, 'level': 0, 'xp': 1, 'next_level': 10})


def level_passed(userid, serverid):
    ID = userid + serverid
    lst = collection.find({"_id": ID})
    data = []
    for item in lst:
        data.append(item)
    if not data:
        new_user(userid=userid, serverid=serverid)
        return False

    if data[0]['xp'] >= data[0]['next_level']:
        level = data[0]['level']
        level += 1
        next_level = data[0]['next_level']
        next_level += 60
        collection.update_many({'_id':ID}, {'$set':{'level':level, 'next_level': next_level}})
        return True        

def retrive_data(userid,serverid):
    ID = userid + serverid
    lst = collection.find({'_id':ID})
    for item in lst:
        return item
