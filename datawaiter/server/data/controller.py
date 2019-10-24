import os
import flask
from flask import Flask, request, jsonify, render_template_string, Response
from flask_restplus import Api, Resource, Namespace
from werkzeug.utils import secure_filename
from pathlib import Path
import pandas as pd
import json

from .csv_process import CSV

ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#api = Api(bp, title="Another API with separate Swagger docs", version="0.1.0")
api = Namespace('data', description='Dataframe based operations')

@api.route("/datasets")
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

            csv_filepath = os.path.join(file_folder_path, app.config['raw_files_name'])
            processed_csv_filepath = os.path.join(file_folder_path, app.config['stat_files_name'])

            csv = CSV(file.read().decode('UTF-8'))
            if csv.is_valid:
                csv.save_csv_df(csv_filepath)
                csv.save_processed_csv_df(processed_csv_filepath)

            return flask.redirect("/home")


@api.route("/datasets/<string:csv_name>")
class Dataset(Resource):
    def get(self, csv_name):
        """
        returns a JSON formated version of the selected dataset
        """    

        app = flask.current_app

        # if user does not select file, browser also
        # submit an empty part without filename
        if csv_name == '':
            print('No selected file')
            return redirect(request.url)

        file_folder = secure_filename(csv_name)
        root_folder = app.config['data_folder'] \
            if not app.config['session_based'] \
            else os.path.join(app.config['data_folder'], 'SESSION_NAME_IN_COOKIES')

        file_folder_path = os.path.join(root_folder,file_folder)
        
        if Path(file_folder_path).exists() and Path(file_folder_path).is_dir():
            csv_filepath = os.path.join(file_folder_path, app.config['raw_files_name'])
            print(csv_filepath)
            df  = pd.read_csv(csv_filepath)

            return json.loads(df.to_json(orient='records'))

    def post(self, csv_name):
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
            filename = secure_filename(csv_name)

            root_folder = app.config['data_folder'] \
                if not app.config['session_based'] \
                else os.path.join(app.config['data_folder'], 'SESSION_NAME_IN_COOKIES')

            file_folder = f'{len(os.listdir(root_folder))}__{filename}'
            file_folder_path = os.path.join(root_folder,file_folder)
            os.mkdir(file_folder_path)

            file.save(os.path.join(file_folder_path, app.config['raw_files_name']))
            file.save(os.path.join(file_folder_path, app.config['stat_files_name']))

            return flask.redirect("/home")

@api.route("/datasets/<string:csv_name>/columns")
class ColumnsList(Resource):
    def get(self):
        """
        returns a list of available columns
        """    

        return jsonify("healthy")

@api.route("/datasets/<string:csv_name>/columns/<string:col_name>")
class Column(Resource):
    def get(self, csv_name, col_name):
        """
        returns a JSON formated version of the selected dataset
        """    

        return jsonify("healthy")