from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///:memory:")
with engine.begin() as connection:
    connection.execute(text("CREATE TABLE book (title TEXT, rating INTEGER)"))
    connection.execute(
        text("INSERT INTO book VALUES (:title, :rating)"),
        [{"title": "Sharp Objects", "rating": 4}, {"title": "The Widow's Tale", "rating": 2}],
    )

with engine.connect() as connection:
    # The parameter is sent separately from the statement, so the database never
    # parses the value as SQL. This is the only correct way.
    statement = text("SELECT title FROM book WHERE rating >= :floor")
    print(connection.execute(statement, {"floor": 3}).scalars().all())

    # An apostrophe in ordinary data breaks a formatted query outright. Same lesson
    # as the scraping block, one layer up.
    hostile = "The Widow's Tale"
    try:
        connection.execute(text(f"SELECT rating FROM book WHERE title = '{hostile}'"))
    except Exception as error:
        print(type(error).__name__)

    safe = text("SELECT rating FROM book WHERE title = :title")
    print(connection.execute(safe, {"title": hostile}).scalar_one())
