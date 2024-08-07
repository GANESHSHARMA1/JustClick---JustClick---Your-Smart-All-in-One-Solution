from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://<Username>:<Password>@justclick.ps3ayrm.mongodb.net/test?appName=JustClick"

client = MongoClient(uri, server_api=ServerApi('1'))


db = client["ATS"]
jobs_collection = db["jobs"]


job_openings = [
    {
        "title": "Software Engineer",
        "description": "Develop and maintain web applications.",
        "location": "San Francisco, CA",
        "salary": "120000"
    },
    {
        "title": "Data Scientist",
        "description": "Analyze and interpret complex data sets.",
        "location": "New York, NY",
        "salary": "110000"
    },
    {
        "title": "Product Manager",
        "description": "Oversee product development from concept to launch.",
        "location": "Austin, TX",
        "salary": "130000"
    }
]


result = jobs_collection.insert_many(job_openings)

print(f"Inserted job openings with IDs: {result.inserted_ids}")


client.close()
