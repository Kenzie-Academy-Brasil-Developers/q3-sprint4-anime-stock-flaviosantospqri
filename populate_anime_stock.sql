DROP TABLE IF EXISTS animes;

CREATE TABLE IF NOT EXISTS animes(
    id BIGSERIAL PRIMARY KEY,
    anime VARCHAR(100) NOT NULL UNIQUE,
    released_date DATE NOT NULL,
    seasons INTEGER NOT NULL
);

INSERT INTO animes(anime, released_date, seasons)
VALUES
('Naruto Classic', '21-09-1999', 9),
('Naruto Shipudden', '15-02-2007', 20),
('Dragon Ball', '26-02-1986', 5),
('Yu-Gi-Oh', '04-04-1998', 4);
