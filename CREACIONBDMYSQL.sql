DROP DATABASE IF EXISTS Sistema_Atencion_SS;
CREATE DATABASE Sistema_Atencion_SS;
USE Sistema_Atencion_SS;

CREATE TABLE TIPO_USERS_TABLE (
    Id_Tipo_Users INT PRIMARY KEY NOT NULL,
    Descripcion_user VARCHAR(32)
);

CREATE TABLE TABLE_SEXO (
    Id_Sexo INT PRIMARY KEY NOT NULL,
    Sexo VARCHAR(16)
);

CREATE TABLE TABLE_CARRERA (
    Id_Carrera INT PRIMARY KEY NOT NULL,
    Descripcion_Carrera VARCHAR(128)
);

CREATE TABLE STATUS_USER (
    Id_Estatus_user INT PRIMARY KEY NOT NULL,
    Descripcion_Status VARCHAR(10)
);

CREATE TABLE STATUS_DOCUMENTO (
    Id_Status_Documento INT PRIMARY KEY NOT NULL,
    Status_Documento VARCHAR(32)
);

CREATE TABLE TIPO_DOCUMENTO (
    Id_Tipo_Documento INT PRIMARY KEY NOT NULL,
    Tipo_Documento VARCHAR(64)
);

CREATE TABLE USERS (
    Id_user INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    boleta VARCHAR(32) NOT NULL,
    passw VARBINARY(1024) NOT NULL,
    Tipo_user INT,
    Id_Estatus_user INT,
    Actualizacion_Estatus DATETIME,
    FOREIGN KEY (Id_Estatus_user) REFERENCES STATUS_USER(Id_Estatus_user),
    FOREIGN KEY (Tipo_user) REFERENCES TIPO_USERS_TABLE(Id_Tipo_Users)
);

CREATE TABLE DATA_USERS (
  Id_data_users INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
  user_id INT NOT NULL,
  Nombre VARCHAR(64),
  A_Paterno VARCHAR(64),
  A_Materno VARCHAR(64),
  CURP VARCHAR(32),
  Boleta VARCHAR(32),
  Id_Sexo INT,
  Id_Plantel INT,
  Semestre INT, 
  CP VARCHAR(32),
  Tel_particular VARCHAR(32),
  Direccion VARCHAR(1024),
  Alcaldia VARCHAR(128),
  Escolaridad VARCHAR(16),
  Correo VARCHAR(64),
  Id_carrera INT,
  Clave_carrera VARCHAR(16),
  Prestatario VARCHAR(1024),
  Codigo_Prestatario VARCHAR(32),
  Responsable VARCHAR(128),
  Programa TEXT,
  Clave_programa VARCHAR(32),
  Cargo VARCHAR(128),
  Tel_responsable VARCHAR(64),
  Fecha_registro DATE,
  Fecha_inicio DATE,
  Fecha_termino DATE,
  Correo_prestatario VARCHAR(64),
  Ubicacion_calleynum VARCHAR(128),
  Ubicacion_colonia VARCHAR(128),
  Ubicacion_alcaldia VARCHAR(128),
  Ubicacion_codpos VARCHAR(128),
  Token VARCHAR(32),
  No_Registro VARCHAR(32),
  Numero_Registro INT,
  FOREIGN KEY (Id_carrera) REFERENCES TABLE_CARRERA (Id_Carrera),
  FOREIGN KEY (Id_Sexo) REFERENCES TABLE_SEXO (Id_Sexo),
  FOREIGN KEY (user_id) REFERENCES USERS (Id_user)
);

CREATE TABLE DOCUMENTOS (
  Id_documento INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
  Id_alumno INT,
  Id_Tipo_Documento INT,
  Id_Status_Documento INT,
  Fecha_Envio DATE,
  Fecha_Aceptado DATE,
  Ubicacion_Archivo VARCHAR(256),
  Nombre_Archivo VARCHAR(256),
  FOREIGN KEY (Id_Tipo_Documento) REFERENCES TIPO_DOCUMENTO(Id_Tipo_Documento),
  FOREIGN KEY (Id_Status_Documento) REFERENCES STATUS_DOCUMENTO(Id_Status_Documento),
  FOREIGN KEY (Id_alumno) REFERENCES DATA_USERS(Id_data_users)
);

CREATE TABLE TOKENS (
  id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
  token INT NOT NULL,
  email VARCHAR(255) NOT NULL,
  expiration_time DATETIME NOT NULL
);

INSERT INTO TIPO_USERS_TABLE (Id_Tipo_Users,Descripcion_user)
VALUES (1,'ADMIN'),(2,'STUDENT');

INSERT INTO TABLE_SEXO (Id_Sexo,Sexo)
VALUES (1,'MASCULINO'),(2,'FEMENINO');

INSERT INTO TABLE_CARRERA (id_carrera,Descripcion_Carrera)
VALUES (1,'ESCA.UST CONTADOR PÚBLICO'),
(2,'ESCA.UST LICENCIADO EN RELACIONES COMERCIALES'),
(3,'ESCA.UST LICENCIADO EN NEGOCIOS INTERNACIONALES'),
(4,'ESCA.UST LICENCIADO EN ADMINISTRACION Y DESARROLLO EMPRESARIAL'),
(5,'ESCA.UST LICENCIADO EN COMERCIO INTERNACIONAL'),
(6,'ESCA.UST LICENCIADO EN COMERCIO INTERNACIONAL (SADE)'),
(7,'ESCA.U.TEP. LICENCIADO EN NEGOCIOS INTERNACIONALES');

INSERT INTO STATUS_USER (Id_Estatus_user,Descripcion_Status)
VALUES (1,'ESPERA'),
(2,'RECHAZADO'),
(3,'ACEPTADO'),
(4,'COMPLETADO'),
(5,'CONCLUIDO'),
(6,'ARCHIVADO');

INSERT INTO STATUS_DOCUMENTO (Id_Status_Documento,Status_Documento)
VALUES (1,'SIN ARCHIVO'),
(2,'ACEPTADO'),
(3,'ESPERA APROBACIÓN'),
(4,'RECHAZADO');

INSERT INTO TIPO_DOCUMENTO (Id_Tipo_Documento,Tipo_Documento)
VALUES (1,'EXPEDIENTE'),
(2,'EVALUACIÓN DE DESEMPEÑO'),
(3,'CARTA TÉRMINO'),
(4,'CARTA TÉRMINO SELLADA'),
(5,'CONSTANCIA DE LIBERACIÓN');