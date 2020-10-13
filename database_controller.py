import sqlite3

DBconnection = sqlite3.connect('Cookie.db')
DBcursor = DBconnection.cursor()

# we will use this format
# serverID (serverid)
# userID (userid)
# xp (experience points)
# lvl (level of the member)
# next_lvl (xp required to reach next level)

# CREATING TABLE (if not already existing)
def create_table():
    DBcursor.execute("CREATE TABLE IF NOT EXISTS cookie(serverID text, userID text, xp integer, lvl integer, next_lvl integer)")
    DBconnection.commit()

# ENTERING DATA
def new_entry(serverID, userID):
    DBcursor.execute(f"INSERT INTO cookie (serverID, userID, xp, lvl, next_lvl) VALUES ({serverID}, {userID}, {1},{0}, {10})")
    DBconnection.commit()

def fetch_data(serverID, userID):
    DBcursor.execute(f'SELECT * FROM cookie WHERE serverID = {serverID} AND userID = {userID}')
    row = DBcursor.fetchone()
    if row is None:
        print("no data")
        new_entry(serverID, userID)
    else:
        return row

def update_rank(serverID, userID): # This method will be used for incresing the rank and xp of the members in the server
    lst = fetch_data(serverID, userID)
    try:
        level = lst[3]
        next_level = lst[4]
        xp = lst[2]
        xp += 1
        # xp = str(xp)
        DBcursor.execute(f'UPDATE cookie SET xp = {xp} WHERE serverID = {serverID} AND userID = {userID}')
        DBconnection.commit()

        # Increasing the level (if xp reached)
        if xp >= next_level:
            level += 1
            DBcursor.execute(f'UPDATE cookie SET lvl = {level} WHERE serverID = {serverID} AND userID = {userID}')
            DBconnection.commit()
            next_level += 10
            DBcursor.execute(f'UPDATE cookie SET next_lvl = {next_level} WHERE serverID = {serverID} AND userID = {userID}')
            DBconnection.commit()
            return True
    except:
        pass


