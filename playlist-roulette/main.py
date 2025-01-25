from diagrams import Diagram
from diagrams.aws.general import User, Users
from diagrams.aws.network import APIGateway
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.programming.framework import Nextjs

with Diagram("Playlist Roulette", show=False):
    host = User("Host")
    players = Users("Players")

    web = Nextjs("Game Web Application")

    connect = Lambda("Connect")
    disconnect = Lambda("Disconnect")
    create_game = Lambda("Create Game")
    
    ws = APIGateway("Websocket API Gateway")
    api = APIGateway("Game Rest API Gateway")

    connections = Dynamodb("Connections Table")
    games = Dynamodb("Games Table")

    host >> web
    players >> web
    web >> ws
    web >> api
    ws >> connect >> connections
    ws >> disconnect >> connections
    api >> create_game >> games
