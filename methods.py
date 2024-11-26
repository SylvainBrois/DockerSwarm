import os

import mysql.connector
from mysql.connector import Error


def db_check_connection():
    db_user = os.getenv('MYSQL_USER')
    db_pass = os.getenv('MYSQL_PASS')
    db_name = os.getenv('MYSQL_DATABASE')
    db_host = os.getenv('MYSQL_HOST')
    db_port = os.getenv('MYSQL_PORT')
    try:
        # Tentative de connexion à la base de données
        connection = mysql.connector.connect(
            user=db_user,
            password=db_pass,
            host=db_host,
            port=db_port,
            database=db_name
        )
        if connection.is_connected():
            return "Connexion réussie à la base de données."
    except Error as e:
        return f"Erreur lors de la connexion à la base de données : {e} {os.getenv('MYSQL_HOST')} {os.getenv('MYSQL_PORT')}"
    finally:
        # Fermeture de la connexion si elle est ouverte
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Connexion fermée.")