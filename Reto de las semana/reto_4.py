def catalogacion_audiovisual(inventario: list) -> tuple:
 #DVD
 filtrar_dvd=[x for x in inventario if x["tipo"] == "DVD" in x["tipo"]]
 dvd=[x for x in filtrar_dvd if x["área"] == "Administración" or x["área"] == "Física" or x["área"] == "Matemáticas" in x["área"]]
 dvd+= list(filter(lambda x: x["área"] == "Tecnología" and 2021 - x["año"]  <= 15  ,filtrar_dvd)) # dvd de tecnologia menor a 15 años
 #DVD eliminados
 dvd_eliminado=list(filter(lambda x: x["área"] == "Tecnología" and not 2021 - x["año"]  <= 15  ,filtrar_dvd))
 dvd_eliminado=list(map(lambda x: x["id"] ,dvd_eliminado))
 #CD
 filtrar_cd = [x for x in inventario if x["tipo"] == "CD" in x["tipo"]]
 dvd+=list(filter(lambda x: x["área"] == "Tecnología" and 2021 - x["año"]  <= 8  ,filtrar_cd))
 dvd+=list(filter(lambda x: x["área"] != "Tecnología" and 2021 - x["año"]  <= 10  ,filtrar_cd))
 dvd.sort(key=lambda item: item.get("id"))
 #CD eliminados
 cd_eliminado=list(filter(lambda x: x["área"] == "Tecnología" and not 2021 - x["año"]  <= 8  ,filtrar_cd))
 cd_eliminado+=list(filter(lambda x: x["área"] == "Administración" or x["área"] == "Física" or x["área"] == "Matemáticas" and not 2021 - x["año"]  <= 10  ,filtrar_cd))
 cd_eliminado= list(sorted(map(lambda x: x["id"] ,cd_eliminado)))
 #CAMBIAR EL ORDEN DEL APELLIDO
 
 return(dvd,dvd_eliminado,cd_eliminado)
 

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
