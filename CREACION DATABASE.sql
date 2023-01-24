Create database Sistema_Atencion_SS
USE Sistema_Atencion_SS
GO
DROP TABLE USERS
GO
CREATE TABLE USERS 
(
Id_user int primary key not null IDENTITY,
boleta varchar not null,
passw varbinary(max) not null,
Tipo_user int, 
Id_Estatus_user int,
foreign key (Id_user) references DATA_USERS(Id_data_users),
foreign key (Id_Estatus_user) references STATUS_USER(Id_Estatus_user),
foreign key (Tipo_user) references TIPO_USERS_TABLE(Id_Tipo_Users) 
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
Id_data_users int primary key not null,
Nombre varchar(20),
A_Materno varchar(20),
A_Paterno varchar(20),
CURP varchar(10),
ID_SEXO int,
ID_PLANTEL int, 
CP int,
tel_particular int,
direccion varchar(max),
alcaldia varchar(20),
escolaridad varchar(20),
correo  varchar(20),
id_carrera INT,
prestatario VARCHAR(20),
codigo_Prestatario varchar(20),
responsable VARCHAR(20),
programa VARCHAR(20),
clave_programa VARCHAR(20),
cargo VARCHAR(20),
tel_responsable VARCHAR(20),
fecha_elaboracion date,
fecha_inicio date,
fecha_termino date,
correo_prestatario varchar(20),
ubicacion_calleynum varchar(20),
ubicacion_colonia varchar(20),
ubicacion_alcaldia varchar(20),
ubicacion_codpos varchar(20),
foreign key (id_carrera) references TABLE_CARRERA (id_carrera),
foreign key (ID_SEXO) references TABLE_SEXO (Id_Sexo)
);
GO
Create table TABLE_CARRERA
(
id_carrera int primary key not null,
DESCPCION_CARRERARA VARCHAR(15)
);
GO
Create table TABLE_SEXO
(
Id_Sexo int primary key not null,
NAME_SEXO VARCHAR(15)
);
GO

Create table TIPO_USERS_TABLE
(
Id_Tipo_Users int primary key not null,
Descripcion_user varchar(20)
)
GO

CONSTRAINT Id_user
FOREIGN KEY Id_data_users
REFERENCES parent_table_name(column1,column2,..)