def register_routes(api, app, root="api"):
    from .controller import api as home_api
	
    api.add_namespace(home_api, path=f"")    
    #app.register_blueprint(blueprint, url_prefix=f"/{root}/{BASE_ROUTE}")
