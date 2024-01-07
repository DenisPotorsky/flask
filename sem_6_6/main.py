from typing import List

import uvicorn
from fastapi import FastAPI
import sqlalchemy
import databases

from sem_6_6.models import Users, UsersIn, Orders, Goods, GoodsIn, OrdersIn

app = FastAPI()

DATABASE_URL = "sqlite:///databases.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(30)),
    sqlalchemy.Column("lastname", sqlalchemy.String(128)),
    sqlalchemy.Column("password", sqlalchemy.String(128)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
)
goods = sqlalchemy.Table(
    "goods",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String(30)),
    sqlalchemy.Column("description", sqlalchemy.String(128)),
    sqlalchemy.Column("status", sqlalchemy.String(30)),
    sqlalchemy.Column("price", sqlalchemy.Float),
)
orders = sqlalchemy.Table(
    "orders",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column(
        "user_id", sqlalchemy.String(128), sqlalchemy.ForeignKey("users.id")
    ),
    sqlalchemy.Column(
        "goods_id", sqlalchemy.String(128), sqlalchemy.ForeignKey("goods.id")
    ),
    sqlalchemy.Column("order_date", sqlalchemy.String(20)),
    sqlalchemy.Column("order_status", sqlalchemy.String(20)),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)


@app.get("/users/", response_model=List[Users])
async def get_all_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get("/users/{user_id}/", response_model=Users)
async def get_one_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.post("/users/", response_model=Users)
async def create_user(user: UsersIn):
    query = users.insert().values(
        name=user.name, lastname=user.lastname, email=user.email, password=user.password
    )
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


@app.put("/users/{user_id}/", response_model=Users)
async def update_user(user_id: int, new_user=UsersIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": new_user}


@app.delete("/users/{user_id}/")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {"message": "User deleted"}


@app.get("/goods/", response_model=List[Goods])
async def get_all_goods():
    query = goods.select()
    return await database.fetch_all(query)


@app.get("/goods/{good_id}/", response_model=Goods)
async def get_one_good(good_id: int):
    query = goods.select().where(goods.c.id == good_id)
    return await database.fetch_one(query)


@app.post("/goods/", response_model=Goods)
async def create_good(good: GoodsIn):
    query = goods.insert().values(
        title=good.title,
        description=good.description,
        status=good.status,
        price=good.price,
    )
    last_record_id = await database.execute(query)
    return {**good.dict(), "id": last_record_id}


@app.put("/goods/{good_id}/", response_model=Goods)
async def update_good(goods_id: int, new_goods=GoodsIn):
    query = goods.update().where(goods.c.id == goods_id).values(**new_goods.dict())
    await database.execute(query)
    return {**new_goods.dict(), "id": new_goods}


@app.delete("/goods/{good_id}/")
async def delete_good(good_id: int):
    query = goods.delete().where(goods.c.id == good_id)
    await database.execute(query)
    return {"message": "Good deleted"}


@app.get("/orders/", response_model=List[Orders])
async def get_all_orders():
    query = orders.select()
    return await database.fetch_all(query)


@app.get("/orders/{order_id}/", response_model=Orders)
async def get_one_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)


@app.post("/orders/", response_model=Orders)
async def create_orders(order: OrdersIn):
    query = orders.insert().values(
        user_id=order.id_users,
        goods_id=order.id_goods,
        order_date=order.order_date,
        order_status=order.order_status,
    )
    last_record_id = await database.execute(query)
    return {**order.dict(), "id": last_record_id}


@app.put("/orders/{order_id}/", response_model=Orders)
async def update_orders(order_id: int, new_order=OrdersIn):
    query = orders.update().where(orders.c.id == order_id).values(**new_order.dict())
    await database.execute(query)
    return {**new_order.dict(), "id": new_order}


@app.delete("/orders/{order_id}/")
async def delete_orders(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {"message": "Order deleted"}


if __name__ == "__main__":
    uvicorn.run("sem_6_6.main:app", port=8005, reload=True)
