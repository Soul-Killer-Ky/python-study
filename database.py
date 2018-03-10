# 导入:
from sqlalchemy import Column, String, create_engine, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'gr_user_role'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    admin_id = Column(Integer)
    group_id = Column(Integer)
    create_time = Column(DateTime)
    create_by = Column(String(150))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/gaore_platform')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id>0).one()
# 打印类型和对象的name属性:
#print('type:', type(user))
#print('name:', user.admin_id)
# 关闭Session:
print(user)
session.close()