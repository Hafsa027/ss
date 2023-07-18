import pymongo

client = pymongo.MongoClient()

tdb= client["first-db"];

tcoll = tdb["employee"]
tdict={"name": "Hafsa", "age": "20"}
x=tcoll.insert_one(tdict)
