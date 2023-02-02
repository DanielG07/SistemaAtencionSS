from io import BytesIO
import xlsxwriter
from flask import send_file

def createApiResponse(data):
    bufferFile = writeBufferExcelFile(data)
    mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    return send_file(bufferFile, mimetype=mimetype)

def writeBufferExcelFile(data):
    buffer = BytesIO()
    workbook = xlsxwriter.Workbook(buffer)
    
    worksheet = workbook.add_worksheet()

    merge_format = workbook.add_format({
    'align':    'center',
    'valign':   'vcenter',
    })

    worksheet.merge_range('A1:A2', 'Merged Cells', merge_format)
    worksheet.merge_range('B1:B2', 'Merged Cells', merge_format)
    worksheet.merge_range('C1:C2', 'Merged Cells', merge_format)
    worksheet.merge_range('D1:D2', 'Merged Cells', merge_format)
    worksheet.merge_range('F1:F2', 'Merged Cells', merge_format)
    worksheet.merge_range('G1:H1', 'Merged Cells', merge_format)
    worksheet.merge_range('I1:I2', 'Merged Cells', merge_format)
    worksheet.merge_range('J1:J2', 'Merged Cells', merge_format)
    worksheet.merge_range('K1:K2', 'Merged Cells', merge_format)
    worksheet.merge_range('L1:L2', 'Merged Cells', merge_format)
    worksheet.merge_range('M1:N1', 'Merged Cells', merge_format)
    worksheet.merge_range('O1:O2', 'Merged Cells', merge_format)
    worksheet.merge_range('P1:P2', 'Merged Cells', merge_format)

    worksheet.set_column_pixels('A:A',16)
    worksheet.set_column_pixels('B:B',64)
    worksheet.set_column_pixels('C:C',27)
    worksheet.set_column_pixels('D:D',43)
    worksheet.set_column_pixels('E:E',45)
    worksheet.set_column_pixels('F:F',57)
    worksheet.set_column_pixels('G:G',51)
    worksheet.set_column_pixels('H:H',51)
    worksheet.set_column_pixels('I:I',57)
    worksheet.set_column_pixels('J:J',164)
    worksheet.set_column_pixels('K:K',52)
    worksheet.set_column_pixels('L:L',46)
    worksheet.set_column_pixels('M:M',33)
    worksheet.set_column_pixels('N:N',33)
    worksheet.set_column_pixels('O:O',64)
    worksheet.set_column_pixels('P:P',159)
    worksheet.set_column_pixels('Q:Q',62)

    worksheet.set_row_pixels(0,36)

    worksheet.write('A1:A2', 'N°')
    worksheet.write('B1:B2', 'MODALIDAD')
    worksheet.write('C1:C2', 'AÑO')
    worksheet.write('D1:D2', 'LISTADO')
    worksheet.write('E2', 'TRABAJÓ')
    worksheet.write('F1:F2', 'NÚMERO DE REGISTRO')
    worksheet.write('G1:H1', 'FECHA')
    worksheet.write('G2', 'INICIO')
    worksheet.write('H2', 'TÉRMINO')
    worksheet.write('I1:I2', 'BOLETA')
    worksheet.write('J1:J2', 'NOMBRE')
    worksheet.write('K1:K2', 'GÉNERO')
    worksheet.write('L1:L2', 'CARRERA')
    worksheet.write('M1:N1', 'LISTADO ENVIADO')
    worksheet.write('M2', 'FECHA')
    worksheet.write('N2', 'FOLIO')
    worksheet.write('O1:O2', 'VISTO BUENO')
    worksheet.write('P1:P2', 'OBSERVACIONES POR DEVOLUCIÓN')
    worksheet.write('Q1', 'CONSTANCIA ENVIADA AL INTERESADO')
    worksheet.write('Q2', 'FECHA')

    index = 3
    for item in data:
        worksheet.write('A' + str(index), str(index - 2))
        worksheet.write('B' + str(index), item['numero'])
        worksheet.write('C' + str(index), item['boleta'])
        worksheet.write('D' + str(index), item['nombre'])
        worksheet.write('E' + str(index), item['nombre'])
        worksheet.write('F' + str(index), item['nombre'])
        worksheet.write('G' + str(index), item['genero'])
        worksheet.write('H' + str(index), item['carrera'])
        worksheet.write('I' + str(index), item['correo_electronico'])
        index = index + 1

    worksheet.autofit()
    workbook.close()
    buffer.seek(0)
    return buffer