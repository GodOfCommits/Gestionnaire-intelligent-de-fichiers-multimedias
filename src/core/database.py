import os

import psycopg2

from src.core.scanner import scan_directory
from src.utils.hash_getter import get_file_hash
from src.utils.logger import log_info
from src.utils.metadata_getter import get_metadata
from src.utils.size_getter import calculate_size


def update_file_database(current_directory):
    current_files_info = []
    current_files = scan_directory(current_directory)
    current_authors = {}  # { an_author_name: an amount of files (an int) }
    current_categories = []  # [ a_category_name: an amount of files (an int) ]
    current_ownerships = []  # [ a_category_or_author_name: a path of a file (a str) ]

    for file in current_files:
        file_path = os.path.join(current_directory, file)
        file_size = calculate_size(file_path)
        file_hash = get_file_hash(file_path)
        authors, title = get_metadata(file_path)

        # Insert to the current files info
        current_files_info.append((file_path, file_size, file_hash, title, authors))

        # Increase the amount of files for each author
        for author in authors:
            if author in current_authors:
                current_authors[author] += 1
            else:
                current_authors[author] = 1

        # Insert the ownership into the database
        for author in authors:
            current_ownerships.append((author, file_path))


    database_files_info = get_all_files()
    database_file_paths = [file[1] for file in database_files_info]

    database_authors_categories_info = get_authors_categories()
    database_authors_categories_names = [category[0] for category in database_authors_categories_info]
    database_authors_categories_amount = [category[1] for category in database_authors_categories_info]

    database_ownerships_info = get_ownerships()
    database_ownerships_names = [ownership[0] for ownership in database_ownerships_info]
    database_ownerships_paths = [ownership[1] for ownership in database_ownerships_info]


def get_all_files():
    """Retrieve all files from the database."""
    conn, cursor = connect_db()
    query = "SELECT * FROM files;"
    cursor.execute(query)
    files = cursor.fetchall()  # This will return a list of tuples
    conn.close()

    log_info(f"Retrieved {len(files)} files from the database.")
    return files


def get_authors_categories():
    """Retrieve all authors_categories from the database."""
    conn, cursor = connect_db()
    query = "SELECT * FROM authors_categories;"
    cursor.execute(query)
    authors_categories = cursor.fetchall()  # This will return a list of tuples
    conn.close()

    log_info(f"Retrieved {len(authors_categories)} authors_categories from the database.")
    return authors_categories


def get_ownerships():
    """Retrieve all ownerships from the database."""
    conn, cursor = connect_db()
    query = "SELECT * FROM ownerships;"
    cursor.execute(query)
    ownerships = cursor.fetchall()  # This will return a list of tuples
    conn.close()

    log_info(f"Retrieved {len(ownerships)} ownerships from the database.")
    return ownerships


def delete_file(file_hash):
    conn, cursor = connect_db()
    query = "DELETE FROM files WHERE file_hash = %s;"
    cursor.execute(query, (file_hash,))
    conn.commit()
    conn.close()

    log_info(f"File with hash {file_hash} has been deleted.")
    return


def insert_file_data(file_path, file_size, file_hash, creator=None, title=None):
    if check_file_exists(file_hash):
        return
    conn, cursor = connect_db()
    query = """
        INSERT INTO files (title, creator, file_path, file_size, file_hash)
        VALUES (%s, %s, %s, %s, %s);
    """
    cursor.execute(query, (file_path, file_size, file_hash, creator, title))
    conn.commit()
    conn.close()

    log_info(f"File {title} has been inserted into the database.")
    return


def check_file_exists(file_hash):
    """Check if a file with the given hash already exists in the database."""
    conn, cursor = connect_db()
    query = "SELECT * FROM files WHERE file_hash = %s;"
    cursor.execute(query, (file_hash,))
    result = cursor.fetchone()  # If the file exists, it returns a tuple
    conn.close()

    log_info(f"Checked if file with hash {file_hash} exists in the database.")
    return result is not None


def connect_db():
    conn = psycopg2.connect(
        dbname="dieugamer",
        user="dieugamer",
        password="dieugamer",
        host="localhost",
        port="5432"
    )

    log_info("Connected to the database.")
    return conn, conn.cursor()
