postal={'D':'NO VÁLIDO', 'F':'NO VÁLIDO', 'I':'NO VÁLIDO','O':'NO VÁLIDO','Q':'NO VÁLIDO','U':'NO VÁLIDO','W':'NO VÁLIDO','A':'Newfoundland','B':'Nova Scotia','C':'Prince Edward Island','E':'New Brunswick','G':'Quebec','H':'Quebec','J':'Quebec','K':'Ontario','L':'Ontario','M':'Ontario','N':'Ontario','P':'Ontario','R':'Manitoba','S':'Saskatchewan','T':'Alberta','V':'British Columbia','X':'Nunavut','Y':'Northwest Territories','Z':'Yukon'}
for c, v in postal.items(): print(c,':',v)  # recorre diccionario

codigo=input('Ingrese un codigo postal: ')

letra=codigo[0]

if codigo[1]=='0':
    print(f'el código postal es en la zona rural de {postal[letra]}')
else:
    print(f'el código postal es en la zona urbana de {postal[letra]}')