import os
from pathlib import Path
from flask import Flask, jsonify
from flask_restplus import Api
import atexit

from . import defaults

def _clean_app(folder, root_folder, persistent_data):
	if not persistent_data:
		folder_path = os.path.join(root_folder, folder)

		for x in os.listdir(folder_path):
			x_path = os.path.join(folder_path, x)

			if Path(x_path).is_file():
				os.remove(x_path)
			elif Path(x_path).is_dir():
				if len(os.listdir(x_path)) == 0:
					os.rmdir(x_path)
				else:
					_clean_app(x, folder_path, persistent_data)

		os.rmdir(folder_path)


def create_app(root_folder=defaults.ROOT_FOLDER, 
		initial_file=None, 
		session_based=defaults.USE_SESSIONS, 
		persistent_data=defaults.PERSISTENT_DATA, 
		env=None):

    from .data import register_routes as register_data_routes

    cache_folder_path:str = os.path.join(root_folder, defaults.DATA_FOLDER)
    cache_folder:Path = Path(cache_folder_path)

    if not cache_folder.exists():
    	os.mkdir(cache_folder_path)
    	os.mkdir(os.path.join(cache_folder_path, 'SESSION_NAME_IN_COOKIES'))
    elif not cache_folder.is_dir():
    	raise Exception(f'Wrong root folder. {cache_folder_path} is not a folder.')

    app = Flask(__name__)
    app.config['data_folder'] = cache_folder_path
    app.config['initial_file'] = initial_file
    app.config['session_based'] = session_based
    app.config['persistent_data'] = persistent_data
    app.config['raw_files_name'] = defaults.RAW_FILES_NAME + '.csv'
    app.config['stat_files_name'] = defaults.STAT_FILES_NAME + '.csv'
    #app.config.from_object(config_by_name[env or "test"])
    api = Api(app, title="Flaskerific API", version="0.1.0", doc='/doc/')

    register_data_routes(api, app)

    @app.route("/health")
    def health():
        return jsonify("healthy")

    atexit.register(lambda: _clean_app(defaults.DATA_FOLDER, root_folder, persistent_data))

    return app