from flask import Flask, jsonify
import os
import pymongo
import pandas as pd 

app = Flask(__name__)


@app.route('/')
def index():
    def gr(result):
        return [x for x in result]
    
    url = "mongodb+srv://dt_user:Edem_2023@cluster0.60xzxfx.mongodb.net"
    client = pymongo.MongoClient(url) #(os.getenv('URL_MONGODB'))
    db = client.app_dt

    collection = db.users
    projection = {'_id': 1, 'suscriptions': 1, 'gender' : 1, 'degree' : 1, 'age' : 1, 'following' : 1,
                    'skills' : 1, 'hobbies' : 1, "userType" : 1, "username" : 1}
    df_users = pd.DataFrame(gr(collection.find({}, projection)))
    return tuple(df_users.values)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
