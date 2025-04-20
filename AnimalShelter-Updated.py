from pymongo import MongoClient
from pymongo import cursor
from bson.objectid import ObjectId
from bson.json_util import dumps


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password) -> None:
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
    def create(self, data: dict) -> bool:
        if data is not None and type(data) is dict:  # ensures data is there and able to be searched
            try:
                self.database.animals.insert_one(data)  # data should be dictionary
                return True
            except Exception as e:
                print("An exception has occured ::", e)
            return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")
    
    #creates multiple files in the database
    def createMany(self, data: dict) -> bool:
        if data is not None and type(data) is dict:  # ensures data is there and able to be searched
            try:
                self.database.animals.insert_many(data)  # data should be dictionary
                return True
            except Exception as e:
                print("An exception has occured ::", e)
            return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Complete this read method to implement the R in CRUD
    def read(self, criteria: dict) -> cursor.Cursor:
        if criteria is not None and type(criteria) is dict:
            data = self.database.animals.find(criteria, {"_id": False})
            for document in data:
                print(document)
        else:
            data = self.database.animals.find({}, {"_id": False})

        return data
    
    # Complete this update method to implement the U in CRUD
    def update(self, initial: dict, updateData: dict) -> str:
        if (initial is not None and type(initial) is dict) and (updateData is not None and type(updateData) is dict):
            updated = self.database.animals.update_one(initial, updateData}) #preforms the data update
            return dumps(updated.raw_result) # updates the raw result using dumps
        else:
            raise Exception("Update error: Invalid parameters") # throws exception if file cannot be updated
    
    # Updates many files in the database
    def updateMany(self, initial: dict, updateData: dict) -> str:
        if (initial is not None and type(initial) is dict) and (updateData is not None and type(updateData) is dict):
            updated = self.database.animals.update_many(initial, updateData}) #preforms the data update
            return dumps(updated.raw_result) # updates the raw result using dumps
        else:
            raise Exception("Update error: Invalid parameters") # throws exception if file cannot be deleted

    
    # Complete this dedlete method to implement the D in CRUD
    def delete(self, remove: dict) -> str:
        if remove is not None and type(remove) is dict:
            delete = self.database.animals.delete_one(remove) # deletes one file form database
            return dumps(deleted.raw_result) # deletes file from raw results
        else:
            raise Exception("Delete error: Invalid parameters") # throws exception if file cannot be updated
    
    #deletes many files in the database
    def deleteMany(self, remove: dict) -> str:
        if remove is not None and type(remove) is dict:
            delete = self.database.animals.delete_many(remove) # deletes many file form database
            return dumps(deleted.raw_result) # deletes files from raw results
        else:
            raise Exception("Delete error: Invalid parameters") # throws exception if file cannot be deleted

