from models import Base
from session import Session


if __name__ == "__main__":
    session = Session()
    Base.metadata.create_all(
        session.get_bind()
    )
