import xlsxwriter

preregistro_mock = [
    {
        "boleta": "2019640295",
        "nombre": "Daniel González Jiménez",
        "carrera": "I. T.",
        "semestre": "9",
        "genero": "Masculino",
        "prestatario": "ESCA UST",
        "f_inicio": "01/10/2021",
        "f_termino": "01/05/2022",
        "correo_electronico": "dgonzalezj1501@alumno.ipn.mx",
        "estatus": "ESPERA",
        "numero": "21140/002",
        "registro_lista": "15",
        "f_envio": "01/01/2021"
    },
    {
        "boleta": "2019640296",
        "nombre": "Jorge Angel Cruz Meneses",
        "carrera": "I. T.",
        "semestre": "9",
        "genero": "Masculino",
        "prestatario": "UNIDAD PROFESIONAL INTERDISCIPLINARIA DE INGENIERIA Y TECNOLOGIAS AVANZADAS",
        "f_inicio": "01/10/2021",
        "f_termino": "01/05/2022",
        "correo_electronico": "dgonzalezj1501@alumno.ipn.mx",
        "estatus": "ESPERA",
        "numero": "21140/030",
        "registro_lista": "15",
        "f_envio": "01/01/2021"
    },
    {
        "boleta": "2019640297",
        "nombre": "Joshep Irvin Camacho Dominguez",
        "carrera": "I. T.",
        "semestre": "9",
        "genero": "Femenino",
        "prestatario": "ESCUELA SUPERIOR DE COMERCIO Y ADMINISTRACION, UNIDAD SANTO TOMAS",
        "f_inicio": "01/10/2021",
        "f_termino": "01/05/2022",
        "correo_electronico": "dgonzalezj1501@alumno.ipn.mx",
        "estatus": "RECHAZADO",
        "numero": "21140/008",
        "registro_lista": "15",
        "f_envio": "01/01/2021"
    },
    {
        "boleta": "2019640298",
        "nombre": "Guillermo Ian Rodriguez Mancera",
        "carrera": "I. T.",
        "semestre": "9",
        "genero": "Masculino",
        "prestatario": "ESCUELA SUPERIOR DE COMERCIO Y ADMINISTRACION, UNIDAD SANTO TOMAS",
        "f_inicio": "01/10/2021",
        "f_termino": "01/05/2022",
        "correo_electronico": "dgonzalezj1501@alumno.ipn.mx",
        "estatus": "ESPERA",
        "numero": "21140/005",
        "registro_lista": "15",
        "f_envio": "01/01/2021"
    },
]

indices = {
    '1': 'B',
    '2': 'C',
    '3': 'D',
    '4': 'F',
    '5': 'G',
    '6': 'H',
    '7': 'I',
    '8': 'J',
    '9': 'K',
    '10': 'L',
    '11': 'M',
    '12': 'N',
    '13': 'O',
    '14': 'P',
    '15': 'Q',
    '16': 'R',
    '17': 'S',
    '18': 'T',
    '19': 'U',
    '20': 'V',
}

workbook = xlsxwriter.Workbook('registros.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', '#')
worksheet.write('B1', 'REG NÚM')
worksheet.write('C1', 'N DE BOLETA')
worksheet.write('D1', 'APELLIDO PATERNO')
worksheet.write('E1', 'APELLIDO MATERNO')
worksheet.write('F1', 'NOMBRE (S)')
worksheet.write('G1', 'GENERO')
worksheet.write('H1', 'CLAVE CARRERA')
worksheet.write('I1', 'MODALIDAD')

index = 2
for item in preregistro_mock:
    worksheet.write('A' + str(index), str(index - 2))
    worksheet.write('B' + str(index), preregistro_mock[index - 2]['numero'])
    worksheet.write('C' + str(index), preregistro_mock[index - 2]['boleta'])
    worksheet.write('D' + str(index), preregistro_mock[index - 2]['nombre'])
    worksheet.write('E' + str(index), preregistro_mock[index - 2]['nombre'])
    worksheet.write('F' + str(index), preregistro_mock[index - 2]['nombre'])
    worksheet.write('G' + str(index), preregistro_mock[index - 2]['genero'])
    worksheet.write('H' + str(index), preregistro_mock[index - 2]['carrera'])
    worksheet.write('I' + str(index), preregistro_mock[index - 2]['correo_electronico'])
    index = index + 1

workbook.close()