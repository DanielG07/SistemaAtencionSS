import pdfquery
from datetime import datetime
import os

datos_comprobante = {
   "archivo": "", "titulo1": "", "titulo2": "", "titulo3": "", "titulo4": "",
   "plantel": "", "clave_plantel": "", "codigo_barras": "", "boleta": "",
   "paterno": "", "materno": "", "nombre": "", "curp": "",  "sexo": "", "id_sexo":"",
   "codigo_postal": "", "tel_particular": "", "direccion": "", "alcaldia": "",
   "escolaridad": "", "correo": "", "carrera": "","id_carrera":"", "clave_carrera": "", 
   "prestatario": "", "codigo": "", "programa": "", "clave_programa": "", 
   "responsable": "", "cargo": "", "tel_responsable": "", "fecha_elaboracion": "",
   "fecha_inicio": "", "fecha_termino": "", "correo_prestatario": "",
   "ubicacion_calleynum": "", "ubicacion_colonia": "", "ubicacion_alcaldia": "",
   "ubicacion_codpos": "",
}


def conversiondate(fecha):
	date_time_obj = datetime.strptime(fecha, '%d %m %Y')
	s = date_time_obj.strftime('%Y-%m-%d')	
	return s

def putField(pdf, campo, bboxes, notFound='No disponible'):
		flag = False
		for bbox in bboxes:
			if flag == False:
				xx = pdf.pq(bbox).text()
				if len(xx) != 0:
					datos_comprobante[campo]=xx
					flag = True
		if flag == False:
			datos_comprobante[campo]=notFound

def pdf_to_dict(archivoPDF):	
		pdf = pdfquery.PDFQuery(archivoPDF)
		pdf.load(0)
		pdf.tree.write(archivoPDF+'.xml', pretty_print = True, encoding="utf-8")

		datos_comprobante["archivo"]=archivoPDF	

		# Lista de posiciones donde se encuentra el tag Titulo1
		bboxes = [
		'LTTextLineHorizontal:in_bbox("128.0, 967.102, 376.15, 981.102")',	
		
		]

		putField(pdf, "titulo1", bboxes, notFound='No disponible')	

		# Lista de posiciones donde se encuentran los titulo2
		bboxes = [
		'LTTextLineHorizontal:in_bbox("110.0, 954.516, 424.736, 966.516")',			
		]

		putField(pdf, "titulo2", bboxes, notFound='No disponible')			

		# Lista de posiciones donde se encuentra el titulo3
		bboxes = [
		'LTTextLineHorizontal:in_bbox("110.0, 939.516, 396.068, 951.516")',
		]

		putField(pdf, "titulo3", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra la titulo 4
		bboxes = [
		'LTTextLineHorizontal:in_bbox("138.0, 924.723, 366.58, 935.723")',
		]

		putField(pdf, "titulo4", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra el Plantel
		bboxes = [
		'LTTextLineHorizontal:in_bbox("132.0, 901.93, 164.23, 911.93")',
		'LTTextLineHorizontal:in_bbox("132.0, 901.93, 182.01, 911.93")',

		]

		putField(pdf, "plantel", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra la clave de plantel
		bboxes = [
		'LTTextLineHorizontal:in_bbox("385.0, 901.93, 401.68, 911.93")',
		]

		putField(pdf, "clave_plantel", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra la boleta en Código de Barras
		bboxes = [
		'LTTextLineHorizontal:in_bbox("250.136, 874.003, 299.064, 880.803")',
		'LTTextLineHorizontal:in_bbox("264.172, 874.003, 314.077, 880.803")',
		'LTTextLineHorizontal:in_bbox("263.677, 874.003, 314.559, 880.803")',
		'LTTextLineHorizontal:in_bbox("268.77,  874.003, 319.159, 880.803")',
		'LTTextLineHorizontal:in_bbox("249.982, 874.003, 328.267, 880.803")',
		'LTTextLineHorizontal:in_bbox("263.677, 874.003, 874.003, 880.803")',
		]

		putField(pdf, "codigo_barras", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra la boleta
		bboxes = [
		'LTTextLineHorizontal:in_bbox("38.0, 809.93, 93.6, 819.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 809.93, 94.71, 819.93")',
        'LTTextLineHorizontal:in_bbox("38.0, 809.93, 95.82, 819.93")',
        'LTTextLineHorizontal:in_bbox("38.0, 809.93, 126.96, 819.93")',
		]

		putField(pdf, "boleta", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra el Apellido Paterno
		bboxes = [
		'LTTextLineHorizontal:in_bbox("160.0, 809.93, 187.77, 819.93")',
		'LTTextLineHorizontal:in_bbox("160.0, 809.93, 211.11, 819.93")',
		'LTTextLineHorizontal:in_bbox("160.0, 809.93, 213.9, 819.93")',
		'LTTextLineHorizontal:in_bbox("160.0, 809.93, 215.56, 819.93")',
		'LTTextLineHorizontal:in_bbox("160.0, 809.93, 220.57, 819.93")',
		'LTTextLineHorizontal:in_bbox("160.0, 809.93, 220.0, 819.93")',
		'LTTextLineHorizontal:in_bbox("160.0, 809.93, 221.11, 819.93")',
		'LTTextLineHorizontal:in_bbox("160.0, 809.93, 221.13, 819.93")',
		'LTTextLineHorizontal:in_bbox("160.0, 809.93, 222.78, 819.93")',
		'LTTextLineHorizontal:in_bbox("160.0, 809.93, 222.22, 819.93")',
		'LTTextLineHorizontal:in_bbox("160.0, 809.93, 222.8, 819.93")',
		'LTTextLineHorizontal:in_bbox("160.0, 809.93, 227.23, 819.93")',
		'LTTextLineHorizontal:in_bbox("160.0, 809.93, 232.22, 819.93")',
		'LTTextLineHorizontal:in_bbox("160.0, 809.93, 232.8, 819.93")',
		'LTTextLineHorizontal:in_bbox("160.0, 809.93, 242.24, 819.93")',
		'LTTextLineHorizontal:in_bbox("160.0, 809.93, 246.12, 819.93")',
		'LTTextLineHorizontal:in_bbox("160.0, 809.93, 253.35, 819.93")',
		'LTTextLineHorizontal:in_bbox("160.0, 809.93, 262.25, 819.93")',
		'LTTextLineHorizontal:in_bbox("160.0, 809.93, 278.9, 819.93")',
		]

		putField(pdf, "paterno", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra el Apellido Materno
		bboxes = [
		'LTTextLineHorizontal:in_bbox("372.0, 809.93, 420.9, 819.93")',
		'LTTextLineHorizontal:in_bbox("372.0, 809.93, 433.11, 819.93")',
		'LTTextLineHorizontal:in_bbox("372.0, 809.93, 434.22, 819.93")',
		'LTTextLineHorizontal:in_bbox("372.0, 809.93, 447.58, 819.93")',
		'LTTextLineHorizontal:in_bbox("372.0, 809.93, 455.9, 819.93")',
		'LTTextLineHorizontal:in_bbox("372.0, 809.93, 488.14, 819.93")',

		]

		putField(pdf, "materno", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra el Nombre
		bboxes = [
		'LTTextLineHorizontal:in_bbox("38.0, 778.93, 109.13, 788.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 778.93, 109.69, 788.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 778.93, 110.23, 788.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 778.93, 110.8,  788.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 778.93, 111.35, 788.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 778.93, 116.35, 788.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 778.93, 120.79, 788.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 778.93, 128.58, 788.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 778.93, 132.46, 788.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 778.93, 135.24, 788.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 778.93, 146.36, 788.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 778.93, 148.57, 788.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 778.93, 154.69, 788.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 778.93, 186.36, 788.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 778.93, 195.25, 788.93")',
		]

		putField(pdf, "nombre", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra la CURP
		bboxes = [
		'LTTextLineHorizontal:in_bbox("315.0, 778.93, 432.79, 788.93")',	
		'LTTextLineHorizontal:in_bbox("315.0, 778.93, 433.91, 788.93")',
		'LTTextLineHorizontal:in_bbox("315.0, 778.93, 435.58, 788.93")',
		'LTTextLineHorizontal:in_bbox("315.0, 778.93, 436.7, 788.93")',
		'LTTextLineHorizontal:in_bbox("315.0, 778.93, 438.35, 788.93")',
		]

		putField(pdf, "curp", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra el campo Sexo  M
		bboxes = [
		'LTTextLineHorizontal:in_bbox("528.0, 779.93, 541.34, 789.93")',
		]
		flag = False
		for bbox in bboxes:
			if flag == False:
				puente = pdf.pq(bbox).text()
				if len(puente) != 0:
					if puente == 'XX':
						datos_comprobante["Sexo"].append('Masculino')	
					flag = True
		if flag == False:
			# Lista de posiciones donde se encuentra el campo Sexo F
			bboxes = [ 
			'LTTextLineHorizontal:in_bbox("560.0, 779.93, 573.34, 789.93")',
			]
			for bbox in bboxes:
				if flag == False:
					puente = pdf.pq(bbox).text()
					if len(puente) != 0:
						if puente == 'XX':
							datos_comprobante["Sexo"].append('Femenino')
						flag = True
			if flag == False:
				datos_comprobante["Sexo"].append('No disponible')

		# Lista de posiciones donde se encuentra Código Postal
		bboxes = [
		'LTTextLineHorizontal:in_bbox("545.0, 728.93, 572.8, 738.93")',
		'LTTextLineHorizontal:in_bbox("545.0, 728.93, 575.4, 738.93")',	
		'LTTextLineHorizontal:in_bbox("545.0, 728.93, 578.36, 738.93")',
		
		]

		putField(pdf, "codigo_postal", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra el Teléfono particular
		bboxes = [
		'LTTextLineHorizontal:in_bbox("38.0, 691.93, 93.6, 701.93")',	
		'LTTextLineHorizontal:in_bbox("38.0, 691.93, 100.26, 701.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 691.93, 103.04, 701.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 691.93, 103.59, 701.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 691.93, 104.5, 701.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 691.93, 144.18, 701.93")',
		
		]

		putField(pdf, "tel_particular", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra la Dirección del Prestador de SS (Alumno)
		bboxes = [
		'LTTextLineHorizontal:in_bbox("38.0, 748.93, 413.64, 758.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 748.93, 431.43, 758.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 748.93, 455.34, 758.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 748.93, 604.79, 758.93")',	
		'LTTextLineHorizontal:in_bbox("38.0, 748.93, 618.15, 758.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 748.93, 782.08, 758.93")',
		]

		putField(pdf, "direccion", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra la Alcaldía y Estado (Alumno)
		bboxes = [
		'LTTextLineHorizontal:in_bbox("38.0, 733.93, 269.72, 743.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 733.93, 286.93, 743.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 733.93, 291.95, 743.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 733.93, 302.5,  743.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 733.93, 304.17, 743.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 733.93, 309.18, 743.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 733.93, 313.63, 743.93")',
		]

		putField(pdf, "alcaldia", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra Escolaridad (Alumno)
		bboxes = [
		'LTTextLineHorizontal:in_bbox("260.0, 691.93, 282.79, 701.93")',
		'LTTextLineHorizontal:in_bbox("260.0, 691.93, 288.35, 701.93")',
		]

		putField(pdf, "escolaridad", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra el Correo electrónico (Alumno)
		bboxes = [
		'LTTextLineHorizontal:in_bbox("345.0, 691.93, 471.85, 701.93")',
		'LTTextLineHorizontal:in_bbox("345.0, 691.93, 490.76, 701.93")',
		'LTTextLineHorizontal:in_bbox("345.0, 691.93, 492.95, 701.93")',
		'LTTextLineHorizontal:in_bbox("345.0, 691.93, 501.0, 701.93")',
		'LTTextLineHorizontal:in_bbox("345.0, 691.93, 518.56, 701.93")',
		'LTTextLineHorizontal:in_bbox("345.0, 691.93, 519.61, 701.93")',
		'LTTextLineHorizontal:in_bbox("345.0, 691.93, 525.2, 701.93")',
		'LTTextLineHorizontal:in_bbox("345.0, 691.93, 549.62, 701.93")',
		'LTTextLineHorizontal:in_bbox("345.0, 691.93, 571.85, 701.93")',
		]

		putField(pdf, "correo", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra la Carrera
		bboxes = [
		'LTTextLineHorizontal:in_bbox("40.0, 664.93, 213.37, 674.93")',
		'LTTextLineHorizontal:in_bbox("40.0, 664.93, 324.5,  674.93")',
		'LTTextLineHorizontal:in_bbox("40.0, 664.93, 348.93, 674.93")',
		'LTTextLineHorizontal:in_bbox("40.0, 664.93, 414.52, 674.93")',		
		]

		putField(pdf, "carrera", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra la Clave de la Carrera
		bboxes = [
		'LTTextLineHorizontal:in_bbox("492.0, 664.93, 525.36, 674.93")',
		
		]

		putField(pdf, "clave_carrera", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra el Prestatario
		bboxes = [
		'LTTextLineHorizontal:in_bbox("38.0, 600.93,  232.49, 610.93")',
		'LTTextLineHorizontal:in_bbox("30.0, 601.551, 306.15, 608.551")',
		'LTTextLineHorizontal:in_bbox("30.0, 601.551, 310.35, 608.551")',
		'LTTextLineHorizontal:in_bbox("38.0, 600.93,  327.52, 610.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 600.93,  385.2, 610.93")',
		'LTTextLineHorizontal:in_bbox("30.0, 601.551, 406.15, 608.551")',
		'LTTextLineHorizontal:in_bbox("38.0, 600.93,  409.18, 610.93")',
		'LTTextLineHorizontal:in_bbox("30.0, 601.551, 417.016, 608.551")',
		'LTTextLineHorizontal:in_bbox("38.0, 600.93,  432.49, 610.93")',
		'LTTextLineHorizontal:in_bbox("30.0, 601.551, 456.15, 608.551")',
		'LTTextLineHorizontal:in_bbox("30.0, 600.93,  566.56, 610.93")',
		]

		putField(pdf, "prestatario", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra el Código del Prestatario
		bboxes = [
		'LTTextLineHorizontal:in_bbox("457.0, 600.93, 566.56, 610.93")',	
		]

		putField(pdf, "codigo", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra el Programa
		bboxes = [
		'LTTextLineHorizontal:in_bbox("30.0, 570.93, 86.9, 580.93")',
		'LTTextLineHorizontal:in_bbox("30.0, 570.93, 181.38, 580.93")',	
		'LTTextLineHorizontal:in_bbox("30.0, 570.93, 375.75, 580.93")',
		'LTTextLineHorizontal:in_bbox("30.0, 571.551,426.739, 578.551")',
		'LTTextLineHorizontal:in_bbox("30.0, 570.93, 450.2, 580.93")',
		'LTTextLineHorizontal:in_bbox("30.0, 571.551, 681.938, 578.551")',
		'LTTextLineHorizontal:in_bbox("30.0, 570.93, 579.56, 580.93")',
		]

		putField(pdf, "programa", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra la Clave del Programa
		bboxes = [
		'LTTextLineHorizontal:in_bbox("457.0, 570.93, 579.56, 580.93")',	
		
		]

		putField(pdf, "clave_programa", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra el Responsable
		bboxes = [
		'LTTextLineHorizontal:in_bbox("38.0, 541.93, 253.05, 551.93")',	
		'LTTextLineHorizontal:in_bbox("38.0, 541.93, 273.05, 551.93")',	
		
		]

		putField(pdf, "responsable", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra el Cargo del Responsable
		bboxes = [
		'LTTextLineHorizontal:in_bbox("38.0, 514.551, 270.61, 521.551")',	
		'LTTextLineHorizontal:in_bbox("38.0, 513.93, 275.85, 523.93")',
		'LTTextLineHorizontal:in_bbox("38.0, 514.551, 293.164, 521.551")',
		
		]

		putField(pdf, "cargo", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra el Teléfono del Responsable
		bboxes = [
		'LTTextLineHorizontal:in_bbox("322.0, 513.93, 419.29, 523.93")',
		
		]

		putField(pdf, "tel_responsable", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra la fecha de elaboracion
		bboxes = [
		'LTTextLineHorizontal:in_bbox("37.0, 316.93, 99.24, 326.93")',
		
		]

		putField(pdf, "fecha_elaboracion", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra la fecha de inicio
		bboxes = [
		'LTTextLineHorizontal:in_bbox("32.0, 370.93, 92.24, 380.93")',
		
		]

		putField(pdf, "fecha_inicio", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra la fecha de termino
		bboxes = [
		'LTTextLineHorizontal:in_bbox("106.0, 370.93, 168.24, 380.93")',
		
		]

		putField(pdf, "fecha_termino", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra correo prestatario
		bboxes = [
		'LTTextLineHorizontal:in_bbox("246.0, 429.93, 337.29, 439.93")',
		'LTTextLineHorizontal:in_bbox("246.0, 429.93, 375.64, 439.93")',
		
		]

		putField(pdf, "correo_prestatario", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra ubicacion calleynum
		bboxes = [
		'LTTextLineHorizontal:in_bbox("38.0, 482.93, 249.16, 492.93")',
		
		]

		putField(pdf, "ubicacion_calleynum", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra ubicacion calleynum
		bboxes = [
		'LTTextLineHorizontal:in_bbox("38.0, 470.93, 185.27, 480.93")',
		
		]

		putField(pdf, "ubicacion_colonia", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra ubicacion alcaldia
		bboxes = [
		'LTTextLineHorizontal:in_bbox("38.0, 457.93, 229.7, 467.93")',
		
		]

		putField(pdf, "ubicacion_alcaldia", bboxes, notFound='No disponible')

		# Lista de posiciones donde se encuentra ubicacion codpos
		bboxes = [
		'LTTextLineHorizontal:in_bbox("38.0, 442.93, 88.03, 452.93")',
		
		]

		putField(pdf, "ubicacion_codpos", bboxes, notFound='No disponible')

		datos_comprobante['fecha_inicio'] = conversiondate(datos_comprobante['fecha_inicio'])
		datos_comprobante['fecha_termino'] = conversiondate(datos_comprobante['fecha_termino'])


		if(datos_comprobante['carrera']=='UPIITA INGENIERO EN TELEMÁTICA'):
			datos_comprobante['id_carrera']=5

		if(datos_comprobante['sexo']=='Masculino'):
			datos_comprobante['id_sexo']=1	

		return datos_comprobante


def lectura(nombre_archivo):
	print(nombre_archivo)
	registro = pdf_to_dict(nombre_archivo)	
	return registro

def main():
	archivo = "./app/pdfs/Daniel_Gonzalez.pdf"
	print('LLAMO A LA FUNCION LECTURA')
	reg = lectura(archivo)
	print(reg)

if __name__ == '__main__':
	main()
