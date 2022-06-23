from http import HTTPStatus
from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
from mysql.connector.errors import Error
from mysql_connection import get_connection
import mysql.connector
import pandas as pd



class MovieRecomResource(Resource) :
    @jwt_required()
    def get(self) :

        # 1. 클라이언트로부터 데이터를 받아온다.
        user_id = get_jwt_identity

        # 2. 추천을 위한 상관계수 데이터프레임을 읽어온다.
        df = pd.read_csv('data/movie_correlation.csv', index_col = 'title')
        # print(df)

        # 3. 이 유저의 별점 정보를 DB에서 가져온다.
        
        
        

        




        return

