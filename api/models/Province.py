from marshmallow import fields, Schema, validate
import datetime
from  . import db

class Province(db.Model):
    __tablename__   =   'province'
    
    id_province = db.Column(db.Integer,  primary_key=True)
    nom_province = db.Column(db.String,  nullable=False)
    
    def __init__(self, data):
        self.id_province = data.get('id_province')
        self.nom_province = data.get('nom_province')
    
    def save(self):
        print("======= EREGISTREMENT =======")
        db.session.add(self)
        db.session.commit()
    
    def update(self, data):
        for key, item in data.items():
            if key == 'nom_province':
                self.nom_province = data.get('nom_province')
            setattr(self, key, item)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod
    def get_all_province():
        return Province.query.all()
    
    @staticmethod
    def get_one_province():
        return Province.query.get(id_province)     
    
    def _repr(self):
        return '<data {} >'.format(self.id_province)
    
class ProvinceSchema(Schema):
    id_province = fields.Int(dump_only=True)
    nom_province = fields.Str(required=True)
    class Meta:
        model: Province       