import datetime
path = "log/" + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + ".txt"
with open(path,"w",encoding="utf-8") as f:
    pass
def reback(user_name,user_id,command):
    print(f"{datetime.datetime.utcnow()} used {command} by {user_name} {user_id}")
    with open(path, "a",encoding="utf-8") as LogFile:
        LogFile.write(f"{datetime.datetime.now()} used {command} by {user_name} {user_id}\n")