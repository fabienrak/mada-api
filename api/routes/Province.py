from  flask import request, json, Response, Blueprint, g
from ..models.Province import  Province, ProvinceSchema
from marshmallow import ValidationError

province_api = Blueprint('province_api', __name__)
province_schema =  ProvinceSchema()

# Add province
@province_api.route('/add-province', methods=['POST'])
def create():
    req_data = request.get_json()
    try:
        data, error = province_schema.load(req_data, partial=False)
        province = Province(data)
        province.save()
        ser_data =  province_schema.dump(province).data
        
        return custom_response({'ser_data': ser_data}, 201)
    except  ValidationError as err:
        
        
        # valid_data = err.valid_data
        # if error:
        #     return custom_response(error, 400)
        return err.messages
    
    



# custom response
def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )