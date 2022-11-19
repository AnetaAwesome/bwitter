from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    nickname = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    first_name = Column(String(50))
    last_name = Column(String(50))

    articles = relationship("Article", back_populates="author")


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(Text)
    created_on = Column(DateTime, default=datetime.now)
    modified_on = Column(
        DateTime,
        default=datetime.now,
        onupdate=datetime.now
    )
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", back_populates="articles")
    hashtags = relationship(
        "Hashtag",
        secondary="articles_hashtags",
        back_populates="articles"
    )


class Hashtag(Base):
    __tablename__ = "hashtags"

    id = Column(Integer, primary_key=True)
    hashtag = Column(String(20), nullable=False, unique=True)

    articles = relationship(
        "Article",
        secondary="articles_hashtags",
        back_populates="hashtags"
    )


association_table = Table(
    "articles_hashtags",
    Base.metadata,
    Column("article_id", ForeignKey("articles.id"), primary_key=True),
    Column("hashtag_id", ForeignKey("hashtags.id"), primary_key=True),
)
