CREATE DATABASE Sistema_Atencion_SS
GO
USE Sistema_Atencion_SS
GO
DROP TABLE USERS
GO
CREATE TABLE USERS 
(
Id_user INT PRIMARY KEY NOT NULL IDENTITY,
boleta VARCHAR NOT NULL,
passw VARBINARY(max) NOT NULL,
Tipo_user INT, 
Id_Estatus_user INT,
FOREIGN KEY (Id_user) REFERENCES DATA_USERS(Id_data_users),
FOREIGN KEY (Id_Estatus_user) REFERENCES STATUS_USER(Id_Estatus_user),
FOREIGN KEY (Tipo_user) REFERENCES TIPO_USERS_TABLE(Id_Tipo_Users) 
);
GO
CREATE TABLE STATUS_USER
(
Id_Estatus_user INT PRIMARY KEY NOT NULL,
DESCRIPICION_STATUS VARCHAR(10)
);
GO
CREATE TABLE DATA_USERS
(
Id_data_users INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
Nombre VARCHAR(40),
A_Paterno VARCHAR(40),
A_Materno VARCHAR(40),
CURP VARCHAR(30),
Boleta VARCHAR(25),
Id_Sexo INT,
Id_Plantel int, 
CP VARCHAR(30),
Tel_particular VARCHAR(30),
Direccion VARCHAR(max),
Alcaldia VARCHAR(75),
Escolaridad VARCHAR(10),
Correo  VARCHAR(50),
Id_carrera INT,
Prestatario VARCHAR(max),
Codigo_Prestatario VARCHAR(30),
Responsable VARCHAR(75),
Programa VARCHAR(max),
Clave_programa VARCHAR(30),
Cargo VARCHAR(75),
Tel_responsable VARCHAR(40),
Fecha_registro date,
Fecha_inicio date,
Fecha_termino date,
Correo_prestatario VARCHAR(50),
Ubicacion_calleynum VARCHAR(75),
Ubicacion_colonia VARCHAR(75),
Ubicacion_alcaldia VARCHAR(75),
Ubicacion_codpos VARCHAR(30),
FOREIGN KEY (Id_carrera) REFERENCES TABLE_CARRERA (id_carrera),
FOREIGN KEY (Id_Sexo) REFERENCES TABLE_SEXO (Id_Sexo)
);
GO
CREATE TABLE TABLE_CARRERA
(
id_carrera INT PRIMARY KEY NOT NULL,
DESCRIPCION_CARRERA VARCHAR(15)
);
GO
ALTER TABLE TABLE_CARRERA
ALTER COLUMN DESCRIPCION_CARRERA VARCHAR(200)

GO

CREATE TABLE TABLE_SEXO
(
Id_Sexo INT PRIMARY KEY NOT NULL,
NAME_SEXO VARCHAR(15)
);
GO

CREATE TABLE TIPO_USERS_TABLE
(
Id_Tipo_Users INT PRIMARY KEY NOT NULL,
Descripcion_user VARCHAR(20)
)
GO
