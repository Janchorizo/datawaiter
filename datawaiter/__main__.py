import sys
import click 

from . import defaults

@click.command()
@click.option(
    '--root-folder',
    '-f',
    type=click.Path(exists=True, writable=True, resolve_path=True),
    default=defaults.ROOT_FOLDER,
    help=f'Root folder where the {defaults.DATA_FOLDER} folder will be placed to hold the uploaded files. Defaults to {defaults.ROOT_FOLDER}.',
)
@click.option(
    '--initial-file',
    '-i',
    type=click.File('r'),
    help='Initial file to be served upon server startup. Any connection will have access to it.',
)
@click.option(
    '--session-based/--shared',
    '-d/-e',
    default=defaults.USE_SESSIONS,
    help='Whether to have per session data upload and serve or a shared folder. Defaults to ' \
    	+ ('using sessions.' if defaults.USE_SESSIONS else 'not use sessions.')
)
@click.option(
    '--maintain/--remove',
    '-m/-r',
    'persistent_data',
    default=defaults.PERSISTENT_DATA,
    help='Whether to preserve or not the uploaded files (and the session if applicable) after server shutdown. Defaults to ' \
    	+ ('preserve the uploaded data.' if defaults.PERSISTENT_DATA else 'remove all generated files and folders.')
)
@click.option(
    '--port',
    '-p',
    default=defaults.PORT,
    help=f'The port to which to bind the server. Defaults to {defaults.PORT}.'
)
def main(root_folder, initial_file, session_based, persistent_data, port):
	from .server import create_app
	app = create_app(root_folder, initial_file, session_based, persistent_data)
	app.run(port=port)

if __name__ == '__main__':
	main()