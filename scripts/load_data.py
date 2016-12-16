import pandas
from flask_script import Command
from app.models.secex_2016_exp import SecexExp
from app import db

class LoadData(Command):

    "Loads secex 2016 exp data"

    data_frame = pandas.read_csv('data/EXP_2016_MUN.csv', header=None, sep=";", lineterminator='\n')
    for i in range(len(data_frame)):
        print(i) 
    
    #     row = row.split(';')
    #     product = SecexExp()
    #     product.co_ano = row[0]
    #     product.co_mes = row[1]
    #     product.co_sh4 = row[2]
    #     product.co_pais = row[3]
    #     product.co_uf = row[4]
    #     product.co_porto = row[5]
    #     product.co_mun_geo = row[6]
    #     product.kg_liquido = row[7]
    #     product.vl_fob = row[8]
    #     db.session.add(product)

    # db.session.commit()
