
# Implementing Image Store and Retrieval in MongoDb using Django


## Features

- Images/Files will be stored in the form of chunks
- No need to save to lengthy base64 encoding directly in columns

  
## Implementation

- These are the library files needed to be include ->

```bash 
    import json,base64,gridfs
    from pymongo import MongoClient
    from bson.objectid import ObjectId
```
## Connection with MongoDB
```bash 
    connection = MongoClient("localhost", 27017)
    database = connection['test_database']
    fs = gridfs.GridFS(database)
```
This can be declared globally so that every function can use fs variable 
## Storing Image/File in MongoDB

```bash 
    profile_pic = request.FILES.get("profile_pic")
    x = base64.b64encode(profile_pic.read())
    test_var = fs.put(x, filename=str(profile_pic))
```
## Note:
- str(profile_pic) is used because profile_pic is a object
- Always use request.FILES.get to retrieve image from the POST data
- profile_pic is a object <MultiValueDict: {'profile_pic': [<InMemoryUploadedFile: testocr.jpeg (image/jpeg)>]}>
- We cannot directly store a object in MongoDB
- test_var contains the image_id of image where it is stored
- So we need to convert this object to Base64 encoding.We will use the following code to convert the object into base64 String :

```bash 
    x = base64.b64encode(profile_pic.read())
```


## Retrieve Image/File from MongoDB

```bash 
    def fetch_image(image_id):
        outputdata = fs.get(ObjectId(image_id)).read()
        # print(outputdata)
        result = outputdata.decode('utf-8')
        return(result)

    def home(request):
        hospital_list = UserData.objects.all()
        x = []
        for i in hospital_list:
            x.append(fetch_image(i.profile_pic))
        return render(request,'index.html',{'hospital_list':hospital_list,"image_list":x})

```
- This is how the image/file will be stored in database
```bash 
    {
    "_id": {
        "$oid": "60d8f0b6fdb5bd38bc88eaf4"
        },
        "filename": "logo.png",
        "md5": "7c9ee4a4316637f273147a02ff771b3f",
        "chunkSize": 261120,
        "length": 28344,
        "uploadDate": {
            "$date": "2021-06-27T21:42:14.656Z"
        }
    }
```

- Firstly, in order to retrieve the image/file we have to get the id of json
- Then we have convert this id to ObjectId type (Otherwise, fs.find() will not work)
- Then using the ObjectId object we can find the chunkSize
- Then we have to decode the base64 encoding to get the file contents
