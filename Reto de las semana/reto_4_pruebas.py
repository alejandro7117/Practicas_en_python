def catalogacion_audiovisual(inventario: list) -> tuple:
 #DVD
 filtro_dvd=lambda x: x["tipo"]=="DVD" and x["área"]=="Tecnología" and 2021 - x["año"] > 15
 dvd_eliminado=[x["id"] for x in list(filter(filtro_dvd,inventario))]
 #CD
 filtro_cd=lambda x: x["tipo"]=="CD" and (2021 - x["año"] > 10 or (x["área"]=="Tecnología" and 2021 - x["año"] > 8))
 cd_eliminado=[x["id"] for x in list(filter(filtro_cd,inventario))]
 #MANTENER EN BIBLIOTECA
 biblioteca=[x for x in inventario if x["id"] not in dvd_eliminado and x["id"] not in cd_eliminado]
 #CAMBIAR EL ORDEN DEL APELLIDO
 def ajustar_nombres(item: dict) -> dict:
     from functools import reduce
     item["autor"] = reduce(lambda x, y: x+";"+y, [x.split()[1]+","+x.split()[0] for x in item["autor"].split(",")])
     return item
 biblioteca= list(map(ajustar_nombres,biblioteca))

 
 return(biblioteca,dvd_eliminado,cd_eliminado)
 

inventario = [{'id': '10', 'titulo': 
'Administración de compras', 'tipo': 
'DVD', 'área': 'Administración', 
'autor': 'César Díaz,Andrés García', 
'año': 2005}, {'id': '20', 'titulo': 
'Fundamentos de programación', 'tipo': 
'DVD', 'área': 'Tecnología', 'autor': 
'César Díaz', 'año': 2003}, {'id': '30',
'titulo': 'Actualidad matemática', 
'tipo': 'CD', 'área': 'Matemáticas', 
'autor': 'Pedro Navaja', 'año': 1987}, 
{'id': '40', 'titulo': 'Actualidad informática', 'tipo': 'CD', 'área': 
'Tecnología', 'autor': 'Bill Gates', 
'año': 2019}, {'id': '50', 'titulo': 
'Atomic Physics for Dummies', 'tipo': 
'DVD', 'área': 'Física', 'autor': 
'Albert Einstein', 'año': 1955}]
print(catalogacion_audiovisual(inventario))

inventario = [{'id': '10', 'titulo': 
'Administración de compras', 'tipo': 
'CD', 'área': 'Administración', 'autor':
'César Díaz,Andrés García', 'año': 
2005}, {'id': '30', 'titulo': 
'Actualidad matemática', 'tipo': 'CD', 
'área': 'Matemáticas', 'autor': 'Pedro Navaja', 'año': 1987}, {'id': '20', 
'titulo': 'Fundamentos de programación',
'tipo': 'DVD', 'área': 'Tecnología', 
'autor': 'César Díaz', 'año': 2001}, 
{'id': '40', 'titulo': 'Actualidad informática', 'tipo': 'CD', 'área': 
'Tecnología', 'autor': 'Bill Gates', 
'año': 2000}, {'id': '50', 'titulo': 
'Atomic Physics for Dummies', 'tipo': 
'CD', 'área': 'Física', 'autor': 'Albert Einstein', 'año': 1955}]
print(catalogacion_audiovisual(inventario))