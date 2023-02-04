import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db = connection.school
students = db.students


def find():
    print("find, reporting for duty")


def find_one():
    print("find one, reporting for duty")


def delete_one():
    print("delete, reporting for duty")


def delete_many():
    print("delete many, reporting for duty")


if __name__ == '__main__':
    find()
    find_one()
    delete_one()
    delete_many()

query = {'last_name': 'smith'}

students.delete_many(query)



query = {'last_name': 'smith'}

cursor = students.find(query)


for doc in cursor:
    print(doc)


query = {'last_name': 'smith'}

result = students.delete_one(query)
print(result.deleted_count)


query = {'last_name': 'smith'}

cursor = students.find(query)


for doc in cursor:
    print(doc)


query = {'last_name': 'smith'}

result = students.delete_many(query)
print(result.deleted_count)
