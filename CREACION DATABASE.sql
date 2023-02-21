USE master
GO

ALTER DATABASE Sistema_Atencion_SS SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
GO

DROP DATABASE Sistema_Atencion_SS;
GO

CREATE DATABASE Sistema_Atencion_SS
GO

USE Sistema_Atencion_SS
GO

CREATE TABLE TIPO_USERS_TABLE
(
Id_Tipo_Users INT PRIMARY KEY NOT NULL,
Descripcion_user VARCHAR(20)
)
GO

CREATE TABLE TABLE_SEXO
(
Id_Sexo INT PRIMARY KEY NOT NULL,
Sexo VARCHAR(15)
);
GO

CREATE TABLE TABLE_CARRERA
(
Id_Carrera INT PRIMARY KEY NOT NULL,
Descripcion_Carrera VARCHAR(15)
);
GO
ALTER TABLE TABLE_CARRERA
ALTER COLUMN Descripcion_Carrera VARCHAR(200)
GO

CREATE TABLE STATUS_USER
(
Id_Estatus_user INT PRIMARY KEY NOT NULL,
Descripcion_Status VARCHAR(10)
);
GO

CREATE TABLE USERS 
(
Id_user INT PRIMARY KEY NOT NULL IDENTITY,
boleta VARCHAR(25) NOT NULL,
passw VARBINARY(max) NOT NULL,
Tipo_user INT, 
Id_Estatus_user INT,
FOREIGN KEY (Id_Estatus_user) REFERENCES STATUS_USER(Id_Estatus_user),
FOREIGN KEY (Tipo_user) REFERENCES TIPO_USERS_TABLE(Id_Tipo_Users) 
);
GO

CREATE TABLE DATA_USERS
(
Id_data_users INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
user_id INT NOT NULL,
Nombre VARCHAR(40),
A_Paterno VARCHAR(40),
A_Materno VARCHAR(40),
CURP VARCHAR(30),
Boleta VARCHAR(25),
Id_Sexo INT,
Id_Plantel int,
Semestre int, 
CP VARCHAR(30),
Tel_particular VARCHAR(30),
Direccion VARCHAR(max),
Alcaldia VARCHAR(75),
Escolaridad VARCHAR(10),
Correo  VARCHAR(50),
Id_carrera INT,
Clave_carrera VARCHAR (10),
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
Token VARCHAR(32),
FOREIGN KEY (Id_carrera) REFERENCES TABLE_CARRERA (Id_Carrera),
FOREIGN KEY (Id_Sexo) REFERENCES TABLE_SEXO (Id_Sexo),
FOREIGN KEY (user_id) REFERENCES USERS (Id_user)
);
GO
CREATE TABLE STATUS_DOCUMENTO(
Id_Status_Documento INT PRIMARY KEY NOT NULL,
Status_Documento VARCHAR(20)
)
GO
CREATE TABLE TIPO_DOCUMENTO(
Id_Tipo_Documento INT PRIMARY KEY NOT NULL,
Tipo_Documento VARCHAR(40)
)
GO

CREATE TABLE DOCUMENTOS(
No_Registro VARCHAR(20) PRIMARY KEY,
Id_Tipo_Documento INT,
Id_Status_Documento INT,
Fecha_Envio DATE,
Fecha_aceptado DATE,
Ubicacion_Archivo VARCHAR(80)
FOREIGN KEY (Id_Tipo_Documento) REFERENCES TIPO_DOCUMENTO(Id_Tipo_Documento),
FOREIGN KEY (Id_Status_Documento) REFERENCES STATUS_DOCUMENTO(Id_Status_Documento)
)
GO
Alter Table DATA_USERS
ADD No_Registro VARCHAR(20)
GO
Alter Table DATA_USERS
ADD FOREIGN KEY (No_Registro) REFERENCES DOCUMENTOS(No_Registro)
GO



