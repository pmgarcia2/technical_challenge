-- Create 'aerolineas' tables and insert values
CREATE TABLE aerolineas (
    ID_AEROLINEA INT PRIMARY KEY,
    NOMBRE_AEROLINEA VARCHAR(50)
);

BULK INSERT aerolineas
FROM 'C:\Users\paulm\OneDrive\Documentos\Trabajo\XalDigital\technical_challenge\tables\aerolineas.csv'
WITH (FIELDTERMINATOR = ',', ROWTERMINATOR = '\n');

-- Create 'aeropuertos' tables and insert values
CREATE TABLE aeropuertos (
    ID_AEROPUERTO INT PRIMARY KEY,
    NOMBRE_AEROPUERTO VARCHAR(50)
);

BULK INSERT aeropuertos
FROM 'C:\Users\paulm\OneDrive\Documentos\Trabajo\XalDigital\technical_challenge\tables\aeropuertos.csv'
WITH (FIELDTERMINATOR = ',', ROWTERMINATOR = '\n');

-- Create 'movimientos' tables and insert values
CREATE TABLE movimientos (
    ID_MOVIMIENTO INT PRIMARY KEY,
    DESCRIPCION VARCHAR(10)
);

BULK INSERT movimientos
FROM 'C:\Users\paulm\OneDrive\Documentos\Trabajo\XalDigital\technical_challenge\tables\movimientos.csv'
WITH (FIELDTERMINATOR = ',', ROWTERMINATOR = '\n');

-- Create 'vuelos' tables and insert values
CREATE TABLE vuelos (
    ID_AEROLINEA INT,
    ID_AEROPUERTO INT,
    ID_MOVIMIENTO INT,
    DIA DATE,
);

BULK INSERT vuelos
FROM 'C:\Users\paulm\OneDrive\Documentos\Trabajo\XalDigital\technical_challenge\tables\vuelos.csv'
WITH (FIELDTERMINATOR = ',', ROWTERMINATOR = '\n');

-- Verify tables created and values ​​loaded
SELECT *
FROM vuelos;

-- 1. ¿Cuál es el nombre aeropuerto que ha tenido mayor movimiento durante el año?
SELECT aeropuertos.NOMBRE_AEROPUERTO, COUNT(*) as TOTAL_MOVIMIENTOS
FROM vuelos
JOIN aeropuertos ON vuelos.ID_AEROPUERTO = aeropuertos.ID_AEROPUERTO
WHERE YEAR(vuelos.DIA) = '2021'
GROUP BY vuelos.ID_AEROPUERTO, aeropuertos.NOMBRE_AEROPUERTO
ORDER BY TOTAL_MOVIMIENTOS DESC;

-- 2. ¿Cuál es el nombre aerolínea que ha realizado mayor número de vuelos durante el año?
SELECT aerolineas.NOMBRE_AEROLINEA, COUNT(*) as TOTAL_VUELOS
FROM vuelos
JOIN aerolineas ON vuelos.ID_AEROLINEA = aerolineas.ID_AEROLINEA
WHERE YEAR(vuelos.DIA) = '2021'
GROUP BY vuelos.ID_AEROLINEA, aerolineas.NOMBRE_AEROLINEA
ORDER BY TOTAL_VUELOS DESC;

-- 3. ¿En qué día se han tenido mayor número de vuelos?
SELECT DIA, COUNT(*) as TOTAL_VUELOS_POR_DIA
FROM vuelos
GROUP BY DIA
ORDER BY TOTAL_VUELOS_POR_DIA DESC;

-- 4. ¿Cuáles son las aerolíneas que tienen mas de 2 vuelos por día?
SELECT aerolineas.NOMBRE_AEROLINEA, COUNT(*) as TOTAL_VUELOS
FROM vuelos
JOIN aerolineas ON vuelos.ID_AEROLINEA = aerolineas.ID_AEROLINEA
GROUP BY vuelos.ID_AEROLINEA, aerolineas.NOMBRE_AEROLINEA, vuelos.DIA
HAVING COUNT(*) > 2;