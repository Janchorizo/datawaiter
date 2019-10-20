if __name__ == '__main__':
	from .server import create_app

	app = create_app()
	app.run()