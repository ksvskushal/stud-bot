
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

# local import
from instance.config import app_config
from flask import request, jsonify, abort
# initialize sql-alchemy
db = SQLAlchemy()

from app.models import Updatelist

def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/updatelists/', methods=['POST', 'GET'])
    def updatelists():
        if request.method == "POST":
            data = str(request.data.get('data', ''))
            if data:
                updatelist = Updatelist(data=data)
                updatelist.save()
                response = jsonify({
                    'id': updatelist.id,
                    'data': updatelist.data,
                    'date_created': updatelist.date_created,
                    'date_modified': updatelist.date_modified
                })
                response.status_code = 201
                return response
        else:
            # GET
            updatelists = Updatelist.get_all()
            results = []

            for updatelist in updatelists:
                obj = {
                    'id': updatelist.id,
                    'data': updatelist.data,
                    'date_created': updatelist.date_created,
                    'date_modified': updatelist.date_modified
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response
    
    @app.route('/updatelists/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def bucketlist_manipulation(id, **kwargs):
     # retrieve a updatelist using it's ID
        updatelist = Updatelist.query.filter_by(id=id).first()
        if not updatelist:
            return {
            "error": "The given id was not found"
         }, 404

        if request.method == 'DELETE':
            updatelist.delete()
            return {
            "message": "updatelist {} deleted successfully".format(updatelist.id) 
         }, 200

        elif request.method == 'PUT':
            data = str(request.data.get('data', ''))
            updatelist.data = data
            updatelist.save()
            response = jsonify({
                'id': updatelist.id,
                'data': updatelist.data,
                'date_created': updatelist.date_created,
                'date_modified': updatelist.date_modified
            })
            response.status_code = 200
            return response
        else:
            # GET
            response = jsonify({
                'id': updatelist.id,
                'data': updatelist.data,
                'date_created': updatelist.date_created,
                'date_modified': updatelist.date_modified
            })
            response.status_code = 200
            return response

    return app



