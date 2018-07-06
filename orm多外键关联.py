from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@localhost/test_code",encoding='utf-8')

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    billing_address_id = Column(Integer, ForeignKey("address.id"))
    shipping_address_id = Column(Integer, ForeignKey("address.id"))

    billing_address = relationship("Address",foreign_keys=[billing_address_id])
    #多外键关联需要使用foreign_keys去指定外键名，否则插入数据时会报错
    shipping_address = relationship("Address",foreign_keys=[shipping_address_id])



class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(64))
    city = Column(String(32))
    state = Column(String(32))

    def __repr__(self):
        return self.street

Base.metadata.create_all(engine)

Session_class = sessionmaker(bind=engine)
session = Session_class()

# insert_dic = Address(street='wuluju',city='haidian',state='BJ')
# insert_dic1 = Address(street='guoanjie',city='lubeiqu',state='TS')
# session.add_all([insert_dic,insert_dic1])
#
# c1 = Customer(name='test',billing_address=insert_dic,shipping_address=insert_dic1)
# c2 = Customer(name='tom',billing_address=insert_dic1,shipping_address=insert_dic)
#
# session.add_all([c1,c2])
# session.commit()

obj = session.query(Customer).filter(Customer.name=='jack').first()
print(obj.name,obj.billing_address,obj.shipping_address)