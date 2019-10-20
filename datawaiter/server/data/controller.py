from flask import Flask, jsonify
from flask_restplus import Api, Resource, Namespace

#api = Api(bp, title="Another API with separate Swagger docs", version="0.1.0")
api = Namespace('data', description='Dataframe based operations')

@api.route("/dataset")
class DatasetList(Resource):
    def get(self):
        """
        returns a list of available datasets
        """    

        return jsonify("healthy")

    def post(self):
        """
        Uploads and adds a new dataset named as the filename
        """

@api.route("/dataset/<string:name>")
class Dataset(Resource):
    def get(self, name):
        """
        returns a JSON formated version of the selected dataset
        """    

        return jsonify("healthy")

    def put(self, name):
        """
        Uploads and adds a new dataset named as the filename
        """

@api.route("/columns")
class ColumnsList(Resource):
    def get(self):
        """
        returns a list of available columns
        """    

        return jsonify("healthy")

@api.route("/columns/<string:name>")
class Column(Resource):
    def get(self, name):
        """
        returns a JSON formated version of the selected dataset
        """    

        return jsonify("healthy")