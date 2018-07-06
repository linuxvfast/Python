from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey,Table,DATE
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:123456@localhost/test_code?charset=utf8",echo=True)

Base = declarative_base()

#orm自动维护
book_m2m_author = Table('book_m2m_author', Base.metadata,
                        Column('book_id',Integer,ForeignKey('books.id')),
                        Column('author_id',Integer,ForeignKey('authors.id')),
                        )

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    pub_date = Column(DATE)
    authors = relationship('Author',secondary=book_m2m_author,backref='books')

    def __repr__(self):
        return self.name

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return self.name

Base.metadata.create_all(engine)

Session_class = sessionmaker(bind=engine)
session = Session_class()

b1 = Book(name="c++语言",pub_date='2014-07-06')
# b2 = Book(name="linux",pub_date='2014-08-06')
# b3 = Book(name="java",pub_date='2015-05-06')
# b4 = Book(name="php",pub_date='2016-05-12')
a1 = Author(name="guo")
a2 = Author(name="zhang")
# a3 = Author(name="Rain")
#
b1.authors = [a1,a2]
# b2.authors = [a1, a2, a3]
#
# session.add_all([b1, b2, b3, b4, a1, a2, a3])
session.add_all([b1,a1,a2])
#删除数据
# book_obj=session.query(Book).filter(Book.id=='9').first()
# session.delete(book_obj)
# session.commit()

# book_obj = session.query(Book).filter(Book.name=='python').first()
# print(book_obj.name,book_obj.authors)
#
# auth_obj = session.query(Author).filter(Author.name=='Alex').first()
# print(auth_obj.name,auth_obj.books)
#
session.commit()