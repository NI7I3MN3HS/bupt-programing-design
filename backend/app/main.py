from sql_app.database import Base,engine,SessionLocal
from sql_app import models
#创建表
Base.metadata.create_all(bind=engine)
db = SessionLocal()

# 添加用户数据到表中
follow = models.Follow(follower_id=1,followed_id=2)
db.add(follow)
db.commit()
db.refresh(follow)