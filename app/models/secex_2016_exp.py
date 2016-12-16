from sqlalchemy import Column, Integer, String, BigInteger
from app import db


class SecexExp(db.Model):
    __tablename__ = 'secex_2016_exp'

    id = Column(Integer, primary_key=True)
    co_ano = Column(String) 
    co_mes = Column(String) 
    co_sh4 = Column(String) 
    co_pais = Column(String)             
    co_uf = Column(String) 
    co_porto = Column(String)        
    co_mun_geo = Column(String) 
    kg_liquido = Column(BigInteger) 
    vl_fob = Column(BigInteger)

    def __iter__(self):
        yield 'id', self.id
        yield 'co_ano', self.co_ano
        yield 'co_mes', self.co_mes
        yield 'co_sh4', self.co_sh4
        yield 'co_pais', self.co_pais
        yield 'co_uf', self.co_uf
        yield 'co_porto', self.co_porto
        yield 'co_mun_geo', self.co_mun_geo
        yield 'kg_liquido', self.kg_liquido
        yield 'vl_fob', self.vl_fob