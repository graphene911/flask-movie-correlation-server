import mysql.connector

def get_connection() :
    connection = mysql.connector.connect(
        host = 'graphene911-db.cett5e9xjv0f.ap-northeast-2.rds.amazonaws.com',
        database = 'movie_correlations_api_db',
        user = 'movie_user',
        password = 'movie1234'
    )
    return connection
    