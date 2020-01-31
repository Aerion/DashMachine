import os
from flask import request
from flask_restful import Resource
from dashmachine.version import version


class GetVersion(Resource):
    def get(self):
        return {"Version": version}


class ServerShutdown(Resource):
    def get(self):
        os.system("shutdown now")
        return {"Done"}


class ServerReboot(Resource):
    def get(self):
        os.system("reboot")
        return {"Done"}
