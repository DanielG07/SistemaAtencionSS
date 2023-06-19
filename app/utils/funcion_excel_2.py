from io import BytesIO
import xlsxwriter
import math
import datetime
from flask import send_file

def createApiResponse2(data):
    print(data)
    bufferFile = writeBufferExcelFile(data)
    mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    return send_file(bufferFile, mimetype=mimetype)

def writeBufferExcelFile(data):
    buffer = BytesIO()
    workbook = xlsxwriter.Workbook(buffer)

    carreras = {
        "ESCA.UST CONTADOR PÚBLICO": "C.P.",
        "ESCA.UST LICENCIADO EN RELACIONES COMERCIALES": "L.R.C.",
        "ESCA.UST LICENCIADO EN NEGOCIOS INTERNACIONALES": "L.N.I.",
        "ESCA.UST LICENCIADO EN ADMINISTRACION Y DESARROLLO EMPRESARIAL": "L.A.D.E.",
        "ESCA.UST LICENCIADO EN COMERCIO INTERNACIONAL": "L.C.I",
        "ESCA.UST LICENCIADO EN COMERCIO INTERNACIONAL (SADE)": "L.C.I",
        "ESCA.U.TEP. LICENCIADO EN NEGOCIOS INTERNACIONALES": "L.N.I",
    }

    claves = {
        "ESCA.UST CONTADOR PÚBLICO": "140040",
        "ESCA.UST LICENCIADO EN RELACIONES COMERCIALES": "140041",
        "ESCA.UST LICENCIADO EN NEGOCIOS INTERNACIONALES": "140044",
        "ESCA.UST LICENCIADO EN ADMINISTRACION Y DESARROLLO EMPRESARIAL": "140406",
        "ESCA.UST LICENCIADO EN COMERCIO INTERNACIONAL": "140047",
        "ESCA.UST LICENCIADO EN COMERCIO INTERNACIONAL (SADE)": "140042",
        "ESCA.U.TEP. LICENCIADO EN NEGOCIOS INTERNACIONALES": "140044",
    }

    año_actual = datetime.datetime.now().year

    pages = math.ceil(len(data)/20)

    pageIndex = 0

    #for pageIndex in range(pages):

        
    #registros = 20 if pageIndex < pages-1 else (20 if len(data)%20 == 0 else len(data)%20)

    worksheet = workbook.add_worksheet()

    align_center = workbook.add_format({
        'align': 'center',
        'valign': 'vcenter',
        'bg_color': '#E2D1EB',
        'font_size': 8,
        'text_wrap': True,
        'font_name': 'Corbel',
        'border': 1
    })

    worksheet.merge_range('A1:A2', 'Merged Cells', align_center)
    worksheet.merge_range('B1:B2', 'Merged Cells', align_center)
    worksheet.merge_range('C1:C2', 'Merged Cells', align_center)
    worksheet.merge_range('D1:D2', 'Merged Cells', align_center)
    worksheet.merge_range('E1:E2', 'Merged Cells', align_center)
    worksheet.merge_range('F1:F2', 'Merged Cells', align_center)
    worksheet.merge_range('G1:H1', 'Merged Cells', align_center)
    worksheet.merge_range('I1:I2', 'Merged Cells', align_center)
    worksheet.merge_range('J1:J2', 'Merged Cells', align_center)
    worksheet.merge_range('K1:K2', 'Merged Cells', align_center)
    worksheet.merge_range('L1:L2', 'Merged Cells', align_center)
    worksheet.merge_range('M1:M2', 'Merged Cells', align_center)
    worksheet.merge_range('N1:O1', 'Merged Cells', align_center)
    worksheet.merge_range('P1:P2', 'Merged Cells', align_center)
    worksheet.merge_range('Q1:Q2', 'Merged Cells', align_center)

    worksheet.set_column_pixels('A:A',20)
    worksheet.set_column_pixels('B:B',75)
    worksheet.set_column_pixels('C:C',31)
    worksheet.set_column_pixels('D:D',50)
    worksheet.set_column_pixels('E:E',53)
    worksheet.set_column_pixels('F:F',67)
    worksheet.set_column_pixels('G:G',60)
    worksheet.set_column_pixels('H:H',60)
    worksheet.set_column_pixels('I:I',67)
    worksheet.set_column_pixels('J:J',190)
    worksheet.set_column_pixels('K:K',65)
    worksheet.set_column_pixels('L:L',54)
    worksheet.set_column_pixels('M:M',54)
    worksheet.set_column_pixels('N:N',39)
    worksheet.set_column_pixels('O:O',39)
    worksheet.set_column_pixels('P:P',75)
    worksheet.set_column_pixels('Q:Q',186)
    worksheet.set_column_pixels('R:R',72)

    worksheet.set_row_pixels(0,46)
    worksheet.set_row_pixels(1,20)
    worksheet.set_row_pixels(2,20)
    worksheet.set_row_pixels(3,20)
    worksheet.set_row_pixels(4,20)
    worksheet.set_row_pixels(5,20)
    worksheet.set_row_pixels(6,20)
    worksheet.set_row_pixels(7,20)
    worksheet.set_row_pixels(8,20)
    worksheet.set_row_pixels(9,20)
    worksheet.set_row_pixels(10,20)
    worksheet.set_row_pixels(11,20)
    worksheet.set_row_pixels(12,20)
    worksheet.set_row_pixels(13,20)
    worksheet.set_row_pixels(14,20)
    worksheet.set_row_pixels(15,20)
    worksheet.set_row_pixels(16,20)
    worksheet.set_row_pixels(17,20)
    worksheet.set_row_pixels(18,20)
    worksheet.set_row_pixels(19,20)
    worksheet.set_row_pixels(20,20)
    worksheet.set_row_pixels(21,20)

    worksheet.write('A1:A2', 'N°', align_center)
    worksheet.write('B1:B2', 'MODALIDAD', align_center)
    worksheet.write('C1:C2', 'AÑO', align_center)
    worksheet.write('D1:D2', 'LISTADO', align_center)
    worksheet.write('E1:E2', 'TRABAJÓ', align_center)
    worksheet.write('F1:F2', 'NÚMERO DE REGISTRO', align_center)
    worksheet.write('G1:H1', 'FECHA', align_center)
    worksheet.write('G2', 'INICIO', align_center)
    worksheet.write('H2', 'TÉRMINO', align_center)
    worksheet.write('I1:I2', 'BOLETA', align_center)
    worksheet.write('J1:J2', 'NOMBRE', align_center)
    worksheet.write('K1:K2', 'GÉNERO', align_center)
    worksheet.write('L1:L2', 'CARRERA', align_center)
    worksheet.write('M1:M2', 'CLAVE', align_center)
    worksheet.write('N1:O1', 'LISTADO ENVIADO', align_center)
    worksheet.write('N2', 'FECHA', align_center)
    worksheet.write('O2', 'FOLIO', align_center)
    worksheet.write('P1:P2', 'VISTO BUENO', align_center)
    worksheet.write('Q1:Q2', 'OBSERVACIONES POR DEVOLUCIÓN', align_center)
    worksheet.write('R1', 'CONSTANCIA ENVIADA AL INTERESADO', align_center)
    worksheet.write('R2', 'FECHA', align_center)

    date_format = workbook.add_format({
        'num_format': 'dd/mm/yyyy',
        'font_size': 8,
        'text_wrap': True,
        'font_name': 'Corbel',
        'border': 1,
        'valign': 'vcenter',
        })

    text_format = workbook.add_format({
        'font_size': 8,
        'text_wrap': True,
        'font_name': 'Corbel',
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        })

    name_format = workbook.add_format({
        'font_size': 8,
        'text_wrap': True,
        'font_name': 'Corbel',
        'border': 1,
        'valign': 'vcenter',
        })

    index = 3
    for i in range(len(data)):
        item = data.pop(0)
        registro = item['numero'].replace("-", "/")
        worksheet.write('A' + str(index), str(index - 2), text_format)
        worksheet.write('B' + str(index), "TRADICIONAL", text_format)
        worksheet.write('C' + str(index), año_actual, text_format)
        worksheet.write('D' + str(index), pageIndex + 1, text_format)
        worksheet.write('E' + str(index), "", text_format)
        worksheet.write('F' + str(index), registro, text_format)
        worksheet.write('G' + str(index), item['f_inicio'], date_format)
        worksheet.write('H' + str(index), item['f_termino'], date_format)
        worksheet.write('I' + str(index), item['boleta'], text_format)
        worksheet.write('J' + str(index), item['nombre'], name_format)
        worksheet.write('K' + str(index), item['genero'], text_format)
        worksheet.write('L' + str(index), carreras[item['carrera']], text_format)
        worksheet.write('M' + str(index), claves[item['carrera']], text_format)
        worksheet.write('N' + str(index), "", text_format)
        worksheet.write('O' + str(index), "", text_format)
        worksheet.write('P' + str(index), "", text_format)
        worksheet.write('Q' + str(index), "", text_format)
        worksheet.write('R' + str(index), "", text_format)
        index = index + 1
        if pageIndex%20 == 3:
            pageIndex = pageIndex + 1

    
    workbook.close()
    buffer.seek(0)
    return buffer