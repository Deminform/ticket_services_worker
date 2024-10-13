from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime
from src.database.db import engine


Base = declarative_base()


class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    role_name = Column(String(50), nullable=False)


# Таблиця notes, де зберігатимуться назви завдань
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120), nullable=False)
    last_name = Column(String(120), nullable=False)
    email = Column(String(120), nullable=False)
    password = Column(String(40), nullable=False)
    phone = Column(String(15), nullable=True)
    created_at = Column(DateTime, default=datetime.now())
    role_id = Column(Integer, ForeignKey(Role.id, ondelete="CASCADE"))


class ServiceCatalog(Base):
    __tablename__ = "service_catalog"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)


class OrderStatus(Base):
    __tablename__ = "order_statuses"
    id = Column(Integer, primary_key=True)
    status = Column(String(255), nullable=False)


class TicketStatus(Base):
    __tablename__ = "ticket_statuses"
    id = Column(Integer, primary_key=True)
    status = Column(String(255), nullable=False)


# Таблиця records, де зберігатимуться записи справ для завдання з таблиці notes - зв'язок one-to-many, поле note_id
class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)
    service_id = Column(Integer, ForeignKey(ServiceCatalog.id, ondelete="CASCADE"))
    status = Column(Integer, ForeignKey(OrderStatus.id, ondelete="CASCADE"))
    client_id = Column(Integer, ForeignKey(User.id, ondelete="CASCADE"))
    manager_id = Column(Integer, ForeignKey(User.id, ondelete="CASCADE"))


class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True)
    tickets_status = Column(Integer, ForeignKey(TicketStatus.id, ondelete="CASCADE"))
    description = Column(String, nullable=False)
    title = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)
    order_id = Column(Integer, ForeignKey(Order.id, ondelete="CASCADE"))


class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    user_id = Column(Integer,ForeignKey(User.id, ondelete="CASCADE"))
    created_at = Column(DateTime, default=datetime.now())
    ticket_id = Column(Integer, ForeignKey(Ticket.id, ondelete="CASCADE"))


Base.metadata.create_all(engine)
