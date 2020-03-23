from tabula import read_pdf

df = read_pdf('../Pdfs/Libro1.pdf',
              guess=False,
              pandas_options={'skiprows':[0,1],'header':None} 
             )
df.head()

headers = ['Mes','Dia','Año','PptSalpo','TempMax','TempMin','Ppt','Wind','Hum','Solar']
df.columns = headers

df.head()

df.to_excel('../Xls/Libro1.xlsx')


