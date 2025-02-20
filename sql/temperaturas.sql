DROP TABLE IF EXISTS temperatura CASCADE;

DROP TABLE IF EXISTS pais CASCADE;

CREATE TABLE pais (
    pais_codigo CHAR(2) NOT NULL,
    pais_nombre VARCHAR(30) NOT NULL,
    CONSTRAINT pais_pk PRIMARY KEY (pais_codigo)
);

CREATE TABLE temperatura (
    temperatura_paiscodigo CHAR(2) NOT NULL,
    temperatura_anio SMALLINT NOT NULL,
    temperatura_celsius NUMERIC(6,2) NOT NULL,
    temperatura_fahrenheit NUMERIC(6,2),
    CONSTRAINT temperatura_pk PRIMARY KEY (temperatura_paiscodigo, temperatura_anio),
    CONSTRAINT temperatura_fk_pais FOREIGN KEY (temperatura_paiscodigo)
        REFERENCES pais(pais_codigo)
);

INSERT INTO pais (pais_codigo, pais_nombre)
    VALUES
        ('uy', 'Uruguay'),
        ('ar', 'Argentina'),
        ('br', 'Brazil')
;

INSERT INTO temperatura (temperatura_paiscodigo, temperatura_anio, temperatura_celsius, temperatura_fahrenheit)
    VALUES
        ('uy', 2010, 16.5, NULL),
        ('uy', 2011, 16.7, NULL),
        ('uy', 2012, 16.9, NULL),
        ('uy', 2013, 17.1, NULL),
        ('uy', 2014, 17.3, NULL),
        ('uy', 2015, 17.5, NULL),
        ('uy', 2016, 17.7, NULL),
        ('uy', 2017, 17.9, NULL),
        ('uy', 2018, 18.1, NULL),
        ('uy', 2019, 18.3, NULL),
        ('uy', 2020, 18.5, NULL),
        ('uy', 2021, 18.7, NULL),
        ('uy', 2022, 18.9, NULL),
        ('uy', 2023, 19.1, NULL),
        ('uy', 2024, 19.3, NULL),
        ('uy', 2025, 19.5, NULL),
        ('ar', 2010, 17.0, NULL),
        ('ar', 2011, 17.3, NULL),
        ('ar', 2012, 17.6, NULL),
        ('ar', 2013, 17.9, NULL),
        ('ar', 2014, 18.2, NULL),
        ('ar', 2015, 18.5, NULL),
        ('ar', 2016, 18.8, NULL),
        ('ar', 2017, 19.1, NULL),
        ('ar', 2018, 19.4, NULL),
        ('ar', 2019, 19.7, NULL),
        ('ar', 2020, 20.0, NULL),
        ('ar', 2021, 20.3, NULL),
        ('ar', 2022, 20.6, NULL),
        ('ar', 2023, 20.9, NULL),
        ('ar', 2024, 21.2, NULL),
        ('ar', 2025, 21.5, NULL),
        ('br', 2010, 24.00, NULL),
        ('br', 2011, 24.25, NULL),
        ('br', 2012, 24.50, NULL),
        ('br', 2013, 24.75, NULL),
        ('br', 2014, 25.00, NULL),
        ('br', 2015, 25.25, NULL),
        ('br', 2016, 25.50, NULL),
        ('br', 2017, 25.75, NULL),
        ('br', 2018, 26.00, NULL),
        ('br', 2019, 26.25, NULL),
        ('br', 2020, 26.50, NULL),
        ('br', 2021, 26.75, NULL),
        ('br', 2022, 27.00, NULL),
        ('br', 2023, 27.25, NULL),
        ('br', 2024, 27.50, NULL),
        ('br', 2025, 27.75, NULL)
;