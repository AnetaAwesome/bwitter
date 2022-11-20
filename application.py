from models import Base, Article, Hashtag
from session import Session


if __name__ == "__main__":
    session = Session()
    Base.metadata.create_all(
        session.get_bind()
    )

    article_id = input("Provide article id: ")
    hashtag_id = input("Provide hashtag id: ")

    article = session.query(Article).get(article_id)
    if article is None:
        print("No such article")
    else:
        print(f"Hashtags in article: {article.title}")
        for hashtag in article.hashtags:
            print(hashtag.hashtag)

    hashtag = session.query(Hashtag).get(hashtag_id)
    if hashtag is None:
        print("No such hashtag")
    else:
        print(f"\nArticles with specific hashtag: {hashtag.hashtag}")
        for article in hashtag.articles:
            print(article.title)
