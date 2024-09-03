from pymongo import MongoClient, errors


class MongoDBClient:
   def __init__(
      self, 
      clusterPassword: str,
      # dbName: str
      ):
      self.clusterPassword = clusterPassword
      # if dbName:
         # self.connection_string = f"mongodb+srv://fast-api:{self.cluster_password}@fast-api-db.5ia3r.mongodb.net/{dbName}"
         
      self.connectionString = f"mongodb+srv://fast-api:{self.clusterPassword}@fast-api-db.5ia3r.mongodb.net/"
      self.client = None

   def connect(self):
      try:
         self.client = MongoClient( self.connectionString)
         return self.client
      except errors.ConnectionFailure as e:
         return {"_isError": True, "message": f"Failed to connect to MongoDB server: {str(e)}"}
      except errors.ConfigurationError as e:
         return {"_isError": True, "message": f"Configuration error: {str(e)}"}
      except Exception as e:
         return {"_isError": True, "message": f"An unexpected error occurred: {str(e)}"}

   def close(self):
        if self.client:
            self.client.close()
  
 