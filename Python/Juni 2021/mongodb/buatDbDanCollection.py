import pymongo

conn = pymongo.MongoClient("mongodb://localhost:27017/")
db = conn["db_barang"]
coll = db["barang"]
data = {
    "nama" : "Realme 3 Pro",
    "stok" : 2,
    "harga" : 2500000
}
coll.insert_one(data)
