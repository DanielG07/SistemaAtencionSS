import pyodbc
server='DESKTOP-A8TJQDL\SQLEXPRESS01'
bd='Sistema_Atencion_SS'
user='SS_SISTEMAATENCION'
password='Irvin19+'
try:
    conexion=pyodbc.connect(
       'DRIVER={SQL Server};SERVER='+server+';DATABASE='+bd+';UID='+user+';PWD='+password
   )
    print('Conexion exitosa')
    
    cursor = conexion.cursor()
except:
    print('Error al intentar conectarse')