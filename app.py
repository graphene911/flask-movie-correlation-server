from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from Resource.movie import MovieInfoResource, MovieListResource, MovieSearchResource
from Resource.rating import MovieRatingResource, RatingListResource
from Resource.recommend import MovieRecomResource

from Resource.user import UserLoginResource, UserLogoutResource, UserRegisterResource, jwt_blacklist
from config import Config


app = Flask(__name__)

# 환경변수 셋팅
app.config.from_object(Config)

# JWT Token Library 만들기
jwt = JWTManager(app)


# 로그아웃 된 토큰이 들어있는 set을 jwt에 알려준다.
@jwt.token_in_blocklist_loader
def check_if_otken_is_revoked(jwt_header, jwt_payload) :
    jti = jwt_payload['jti']
    return jti in jwt_blacklist

api = Api(app)

api.add_resource(UserRegisterResource, '/users/register')
api.add_resource(UserLoginResource, '/users/login')
api.add_resource(UserLogoutResource, '/users/logout')
api.add_resource(MovieListResource, '/movie')
api.add_resource(MovieInfoResource, '/movie/<int:movie_id>')
api.add_resource(MovieSearchResource, '/movie/search')
api.add_resource(RatingListResource, '/rating')
api.add_resource(MovieRatingResource, '/movie/<int:movie_id>/rating')
api.add_resource(MovieRecomResource, '/movie/recommend')


if __name__ == '__main__' :
    app.run()