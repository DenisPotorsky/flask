from pydantic import BaseModel, Field


class Users(BaseModel):
    __tablename__ = 'users'
    id: int
    name: str = Field(..., max_length=30, title='Name')
    lastname: str = Field(max_length=128, title='Lastname')
    password: str = Field(max_length=128, title='Password')
    email: str = Field(..., title='Email')


class Goods(BaseModel):
    __tablename__ = 'goods'
    id: int
    title: str = Field(..., max_length=30, title='Title')
    description: str = Field(max_length=128, title='Description')
    status: str = Field(..., title='Status')
    price: float = Field(..., title='Price')


class Orders(BaseModel):
    __tablename__ = 'orders'
    id: int
    id_users: int = Field(..., title='id_users')
    id_goods: int = Field(...,title='id_goods')
    order_date: str = Field(..., title='Order date')
    order_status: str = Field(..., title='Order status')


class UsersIn(BaseModel):
    name: str = Field(..., max_length=30, title='Name')
    lastname: str = Field(max_length=128, title='Lastname')
    password: str = Field(max_length=128, title='Password')
    email: str = Field(..., title='Email')


class GoodsIn(BaseModel):
    title: str = Field(..., max_length=30, title='Title')
    description: str = Field(max_length=128, title='Description')
    status: str = Field(..., title='Status')
    price: float = Field(..., title='Price')


class OrdersIn(BaseModel):
    id_users: int = Field(..., title='id_users')
    id_goods: int = Field(..., title='id_goods')
    order_date: str = Field(..., title='Order date')
    order_status: str = Field(..., title='Order status')

