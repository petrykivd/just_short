from datetime import datetime

from .database import Base
from sqlalchemy import Column, Integer, String, Text, DateTime


class Link(Base):
    __tablename__ = "links"
    id = Column(Integer, primary_key=True)
    url = Column(Text, nullable=False)
    short_url = Column(String(120), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return "<Link %r>" % self.id
