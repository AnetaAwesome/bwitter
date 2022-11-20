from models import Base, Article, Hashtag
from session import Session


if __name__ == "__main__":
    session = Session()
    Base.metadata.create_all(
        session.get_bind()
    )

    article = session.query(Article).get(1)
    print(f"Hashtags in article: {article.title}")
    for hashtag in article.hashtags:
        print(hashtag.hashtag)

    hashtag = session.query(Hashtag).get(1)
    print(f"\nArticles with specific hashtag: {hashtag.hashtag}")

    for article in hashtag.articles:
        print(article.title)
