from models import Base, Article
from session import Session


if __name__ == "__main__":
    session = Session()
    Base.metadata.create_all(
        session.get_bind()
    )

    article = session.query(Article).get(1)
    for hashtag in article.hashtags:
        print(hashtag.hashtag)
