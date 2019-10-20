import sys
import click 

from . import defaults

@click.command()
@click.option(
    '--folder',
    '-f',
    type=click.Path(exists=True, writable=True, resolve_path=True),
    default=defaults.DATA_FOLDER,
    help=f'Folder to use for saving the uploaded and processed files. Defaults to {defaults.DATA_FOLDER}.',
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
def main(folder, initial_file, session_based, maintain, port):
	from .server import create_app
	print(folder, initial_file, session_based, maintain, port)
	app = create_app()
	app.run(port=port)

if __name__ == '__main__':
	main()