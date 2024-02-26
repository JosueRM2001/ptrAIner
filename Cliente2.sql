CREATE DATABASE  ptrAIner;
USE ptrAIner;

CREATE TABLE gymrat (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Identificacion VARCHAR(20) NOT NULL,
    Nombre VARCHAR(100) NOT NULL,
    Peso DECIMAL(5,2),
    Estatura DECIMAL(5,2),
    Edad INT,
    EjercicioFrecuente VARCHAR(50),
    TipoEjercicio VARCHAR(50),
    MedidaCintura DECIMAL(5,2),
    MedidaCadera DECIMAL(5,2),
    MedidaCuello DECIMAL(5,2),
    Alergias VARCHAR(255)
);
Select* from gymrat ;
INSERT INTO gymrat (Identificacion, Nombre, Peso, Estatura, Edad, EjercicioFrecuente, TipoEjercicio, MedidaCintura, MedidaCadera, MedidaCuello, Alergias)
VALUES
('123ABC', 'Juan Pérez', 70.5, 1.75, 30, 'Sí', 'Cardio', 80.0, 95.5, 38.0, 'Ninguna'),
('456DEF', 'María Rodríguez', 65.2, 1.68, 28, 'Sí', 'Pesas', 75.5, 90.0, 36.5, 'Polen'),
('789GHI', 'Carlos López', 80.0, 1.80, 35, 'No', NULL, 85.0, 100.0, 40.0, 'Gluten'),
('101JKL', 'Ana Martínez', 55.8, 1.60, 25, 'Sí', 'Yoga', 70.5, 85.5, 35.0, NULL),
('202MNO', 'Pedro García', 75.3, 1.78, 32, 'Sí', 'Crossfit', 82.5, 97.0, 39.0, 'Lactosa'),
('303PQR', 'Laura Fernández', 68.7, 1.70, 29, 'Sí', 'Pilates', 78.0, 92.5, 37.5, 'Ninguna'),
('404STU', 'Ricardo Sánchez', 90.2, 1.85, 40, 'Sí', 'Pesas', 88.5, 105.0, 42.0, 'Nueces'),
('505VWX', 'Isabel Jiménez', 62.4, 1.62, 27, 'Sí', 'Running', 73.0, 88.5, 34.5, NULL),
('606YZA', 'Jorge Herrera', 78.1, 1.79, 33, 'No', NULL, 86.0, 101.5, 40.5, 'Polen'),
('707BCD', 'Elena Ramírez', 58.9, 1.65, 26, 'Sí', 'Spinning', 72.5, 87.0, 35.5, 'Gluten');
