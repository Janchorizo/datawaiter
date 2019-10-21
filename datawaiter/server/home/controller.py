import os
import flask
from flask import Flask, render_template, Response
from flask_restplus import Api, Resource, Namespace

#api = Api(bp, title="Another API with separate Swagger docs", version="0.1.0")
api = Namespace('home', description='Homepage')

@api.route("/")
class Homepage(Resource):
    def get(self):
        """
        returns a list of available datasets
        """    

        app = flask.current_app
        root_folder = app.config['data_folder'] \
                if not app.config['session_based'] \
                else os.path.join(app.config['data_folder'], 'SESSION_NAME_IN_COOKIES')

        template_dir = os.path.dirname(os.path.abspath(__file__))
        print(template_dir, os.path.abspath(__file__))
        template = 'index.html'

        rules = list(app.url_map.iter_rules())
        upload_rule_filter = filter(lambda x:x.endpoint == 'data_dataset_list', rules)
        upload_path = list(upload_rule_filter)[0].rule

        data = {
        	'datasets': os.listdir(root_folder),
        	'num_datasets': len(os.listdir(root_folder)),
        	'using_sessions': app.config['session_based'],
        	'port': app.config['port'],
        	'persistent_data': app.config['persistent_data'],
        	'user': 'default',
        	'version': 0.1,
        	'upload_url': upload_path
        }

        return Response(render_template(template, args=data), mimetype='text/html')