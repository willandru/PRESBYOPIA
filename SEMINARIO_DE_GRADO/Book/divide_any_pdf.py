import PyPDF2

# Abre el archivo PDF que quieres leer
pdf_file = open("Borish's Clinical Refraction.pdf", 'rb')

# Crea un objeto PDFReader
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Obtiene el número de páginas del PDF
num_pages = len(pdf_reader.pages)
print(f'Número de páginas: {num_pages}')

# Define los rangos de páginas que deseas dividir
pagina_inicio = 1  # Cambia este valor al número de página inicial
pagina_fin = 406    # Cambia este valor al número de página final

# Crea un objeto PdfWriter para el nuevo PDF
pdf_writer = PyPDF2.PdfWriter()

# Copia las páginas desde la página de inicio hasta la página final al nuevo PDF
for pagina in range(pagina_inicio - 1, pagina_fin):
    page = pdf_reader.pages[pagina]
    pdf_writer.add_page(page)

# Guarda el nuevo PDF en un archivo
with open('nuevo_pdf.pdf', 'wb') as nuevo_pdf:
    pdf_writer.write(nuevo_pdf)

# Cierra el archivo original y el nuevo PDF
pdf_file.close()

print(f'Nuevo PDF creado con páginas {pagina_inicio} a {pagina_fin}')
