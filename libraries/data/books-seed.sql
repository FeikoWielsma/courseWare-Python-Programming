-- data/books-seed.sql
--
-- The twenty Mystery books from data/books-fixture.html, as a plain SQL script.
-- Rebuilds data/books.db without running the scraper, so the pandas block has
-- something to read even if the scraping demos were never run :
--
--   uv run demos/04-web-scraping/12_rebuilding_from_seed.py
--
-- Regenerate it by scraping again; the timestamps are fixed on purpose so that
-- re-running the scraper produces a readable diff.

DROP TABLE IF EXISTS books;

CREATE TABLE books (
    id           INTEGER PRIMARY KEY,
    title        TEXT    NOT NULL,
    price_gbp    REAL    NOT NULL,
    rating       INTEGER NOT NULL,
    availability TEXT    NOT NULL,
    category     TEXT    NOT NULL,
    url          TEXT    NOT NULL UNIQUE,
    first_seen   TEXT    NOT NULL,
    last_seen    TEXT    NOT NULL
);

INSERT INTO books
    (title, price_gbp, rating, availability, category, url, first_seen, last_seen)
VALUES
    ('Sharp Objects', 47.82, 4, 'In stock', 'Mystery', 'https://books.toscrape.com/catalogue/sharp-objects_997/index.html', '2026-03-02T09:00:00+00:00', '2026-03-02T09:00:00+00:00'),
    ('In a Dark, Dark Wood', 19.63, 1, 'In stock', 'Mystery', 'https://books.toscrape.com/catalogue/in-a-dark-dark-wood_963/index.html', '2026-03-02T09:00:00+00:00', '2026-03-02T09:00:00+00:00'),
    ('The Past Never Ends', 56.50, 4, 'In stock', 'Mystery', 'https://books.toscrape.com/catalogue/the-past-never-ends_942/index.html', '2026-03-02T09:00:00+00:00', '2026-03-02T09:00:00+00:00'),
    ('A Murder in Time', 16.64, 1, 'In stock', 'Mystery', 'https://books.toscrape.com/catalogue/a-murder-in-time_877/index.html', '2026-03-02T09:00:00+00:00', '2026-03-02T09:00:00+00:00'),
    ('The Murder of Roger Ackroyd (Hercule Poirot #4)', 44.10, 4, 'In stock', 'Mystery', 'https://books.toscrape.com/catalogue/the-murder-of-roger-ackroyd-hercule-poirot-4_852/index.html', '2026-03-02T09:00:00+00:00', '2026-03-02T09:00:00+00:00'),
    ('The Last Mile (Amos Decker #2)', 54.21, 2, 'In stock', 'Mystery', 'https://books.toscrape.com/catalogue/the-last-mile-amos-decker-2_754/index.html', '2026-03-02T09:00:00+00:00', '2026-03-02T09:00:00+00:00'),
    ('That Darkness (Gardiner and Renner #1)', 13.92, 1, 'In stock', 'Mystery', 'https://books.toscrape.com/catalogue/that-darkness-gardiner-and-renner-1_743/index.html', '2026-03-02T09:00:00+00:00', '2026-03-02T09:00:00+00:00'),
    ('Tastes Like Fear (DI Marnie Rome #3)', 10.69, 1, 'In stock', 'Mystery', 'https://books.toscrape.com/catalogue/tastes-like-fear-di-marnie-rome-3_742/index.html', '2026-03-02T09:00:00+00:00', '2026-03-02T09:00:00+00:00'),
    ('A Time of Torment (Charlie Parker #14)', 48.35, 5, 'In stock', 'Mystery', 'https://books.toscrape.com/catalogue/a-time-of-torment-charlie-parker-14_657/index.html', '2026-03-02T09:00:00+00:00', '2026-03-02T09:00:00+00:00'),
    ('A Study in Scarlet (Sherlock Holmes #1)', 16.73, 2, 'In stock', 'Mystery', 'https://books.toscrape.com/catalogue/a-study-in-scarlet-sherlock-holmes-1_656/index.html', '2026-03-02T09:00:00+00:00', '2026-03-02T09:00:00+00:00'),
    ('Poisonous (Max Revere Novels #3)', 26.80, 3, 'In stock', 'Mystery', 'https://books.toscrape.com/catalogue/poisonous-max-revere-novels-3_627/index.html', '2026-03-02T09:00:00+00:00', '2026-03-02T09:00:00+00:00'),
    ('Murder at the 42nd Street Library (Raymond Ambler #1)', 54.36, 4, 'In stock', 'Mystery', 'https://books.toscrape.com/catalogue/murder-at-the-42nd-street-library-raymond-ambler-1_624/index.html', '2026-03-02T09:00:00+00:00', '2026-03-02T09:00:00+00:00'),
    ('Most Wanted', 35.28, 3, 'In stock', 'Mystery', 'https://books.toscrape.com/catalogue/most-wanted_623/index.html', '2026-03-02T09:00:00+00:00', '2026-03-02T09:00:00+00:00'),
    ('Hide Away (Eve Duncan #20)', 11.84, 1, 'In stock', 'Mystery', 'https://books.toscrape.com/catalogue/hide-away-eve-duncan-20_620/index.html', '2026-03-02T09:00:00+00:00', '2026-03-02T09:00:00+00:00'),
    ('Boar Island (Anna Pigeon #19)', 59.48, 3, 'In stock', 'Mystery', 'https://books.toscrape.com/catalogue/boar-island-anna-pigeon-19_613/index.html', '2026-03-02T09:00:00+00:00', '2026-03-02T09:00:00+00:00'),
    ('The Widow', 27.26, 2, 'In stock', 'Mystery', 'https://books.toscrape.com/catalogue/the-widow_609/index.html', '2026-03-02T09:00:00+00:00', '2026-03-02T09:00:00+00:00'),
    ('Playing with Fire', 13.71, 3, 'In stock', 'Mystery', 'https://books.toscrape.com/catalogue/playing-with-fire_602/index.html', '2026-03-02T09:00:00+00:00', '2026-03-02T09:00:00+00:00'),
    ('What Happened on Beale Street (Secrets of the South Mysteries #2)', 25.37, 5, 'In stock', 'Mystery', 'https://books.toscrape.com/catalogue/what-happened-on-beale-street-secrets-of-the-south-mysteries-2_506/index.html', '2026-03-02T09:00:00+00:00', '2026-03-02T09:00:00+00:00'),
    ('The Bachelor Girl''s Guide to Murder (Herringford and Watts Mysteries #1)', 52.30, 5, 'In stock', 'Mystery', 'https://books.toscrape.com/catalogue/the-bachelor-girls-guide-to-murder-herringford-and-watts-mysteries-1_491/index.html', '2026-03-02T09:00:00+00:00', '2026-03-02T09:00:00+00:00'),
    ('Delivering the Truth (Quaker Midwife Mystery #1)', 20.89, 4, 'In stock', 'Mystery', 'https://books.toscrape.com/catalogue/delivering-the-truth-quaker-midwife-mystery-1_464/index.html', '2026-03-02T09:00:00+00:00', '2026-03-02T09:00:00+00:00');
