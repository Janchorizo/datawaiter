import os
import flask
from flask import Flask, request, jsonify, render_template_string, Response
from flask_restplus import Api, Resource, Namespace
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#api = Api(bp, title="Another API with separate Swagger docs", version="0.1.0")
api = Namespace('data', description='Dataframe based operations')

@api.route("/dataset")
class DatasetList(Resource):
    def get(self):
        """
        returns a list of available datasets
        """    

        app = flask.current_app
        root_folder = app.config['data_folder'] \
                if not app.config['session_based'] \
                else os.path.join(app.config['data_folder'], 'SESSION_NAME_IN_COOKIES')

        return jsonify(os.listdir(root_folder))

    def post(self):
        """
        Uploads and adds a new dataset named as the filename
        """

        app = flask.current_app

        if 'file' not in request.files:
            return jsonify({'success': False})

        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            root_folder = app.config['data_folder'] \
                if not app.config['session_based'] \
                else os.path.join(app.config['data_folder'], 'SESSION_NAME_IN_COOKIES')

            file_folder = f'{len(os.listdir(root_folder))}__{filename}'
            file_folder_path = os.path.join(root_folder,file_folder)
            os.mkdir(file_folder_path)

            file.save(os.path.join(file_folder_path, app.config['raw_files_name']))
            file.save(os.path.join(file_folder_path, app.config['stat_files_name']))

            return flask.redirect("/home")


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

        print(request)

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