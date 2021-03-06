import os
import sys
import time
import psycopg2
from api.routines.upload_database import UploadDatabase


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celero_app.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    print("Waiting...", flush=True)
    # To wait the docker create the database
    time.sleep(5)
    upload_database = UploadDatabase()
    upload_database.upload_data('./api/resources/')
    print('Listening...', flush=True)
    main()
