from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient.

        # Connection Variables
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 45565
        DB = 'aac'
        COL = 'animals'

        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # Complete this create method to implement the C in CRUD
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)  # data should be dictionary
            if insert != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Complete this read method to implement the R in CRUD
    def read(self, criteria):
        if criteria is not None:
            data = self.database.animals.find(criteria, {"_id": False})
            for document in data:
                print(document)
        else:
            data = self.database.animals.find({}, {"_id": False})

        return data
    
    # Complete this update method to implement the U in CRUD
    def update(self, initial, updateData):
        if initial is not None:
            updated = self.database.animals.update_many(initial, {"$set": updateData})
        else:
            return "No match found"

        return updated.raw_result
    
    # Complete this dedlete method to implement the D in CRUD
    def delete(self, deleteData):
        if deleteData is not None:
            deleted = self.database.animals.delete_many(deleteData)
        else:
            return "No match found"

        return deleted.raw_result
