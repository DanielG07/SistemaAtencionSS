
# SistemaAtencionSS - Desarrollo

Sistema para atención del Servicio Social Esca UST, donde se busca dar seguimiento de los documentos de los alumnos que realicen su servicio social y sean pertenecientes a la Escuela Superior de Contabilidad y Administración Unidad Santo Tomas.

## Requerimientos del sistema

Los siguientes son los valores del sistema donde se ha ejecutado la aplicación principalmente.

- Python 3.11.4
- pip 23.2.1
- MySQL 8.0.34 for Win64

## Configuracion del proyecto
1. Clonar repositorio "git clone https://github.com/DanielG07/SistemaAtencionSS.git"

2. Ejecutar script creación base de datos "CREACIONBDMYSQL.sql" - 
```
mysql -u <username> -p
```
despues
```
source <path\CREACIONBDMYSQL.sql>
```
 o **ejecutar script desde manejador de base de datos.**

3. Modificar los valores de conexión de la base de datos en el archivo app.py. **(Opcional)**

> En caso de querer hacer pruebas de conexión puede ser desde el archivo conexionBd.py

4. Ejecutar script para crear administrador en la base de datos. **(Opcional)**
```
python .\app\registro_admins.py 
```

5. Generar carpeta dentro de carpeta app
- \documentos
    - \CartaCompromiso
	- \Expedientes
	- \Evaluaciones
	- \CartasTermino
	- \CartasTerminoSelladas
	- \ConstanciasLiberacion
	- \ConstanciasLiberacionSelladas

6. Crear archivo .env para declaración de valores de conexión a la base de datos

```Dotenv
SERVER='localhost'
DATABASE='Sistema_Atencion_SS'
USERNAMEBD='root'
PASSWORDBD='root'
```

7. Instalar paquete para manejar ambientes virtuales

```PowerShell
pip install virtualenv == 20.16.5
```

8. Crear ambiente virtual 

```PowerShell
virtualenv -p python3 env
```

9. Activar ambiente virtual

 - Windows

```PowerShell
.\env\Scripts\activate
```
    
 - Linux/MacOS

```PowerShell
source ./venv/bin/activate
```

**Nota:** Revisar que siempre se este trabajando en el entorno *(env)* a partir de este paso.

10. Instalar paquetes de la aplicación

```PowerShell
pip install -r requerimientos.txt
```

11. Ejecutar aplicación

```PowerShell
python .\app\app.py
```