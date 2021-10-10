def calculo_recargos(cliente:dict):
    agujas=cliente["agujas"]
    escolares=cliente["escolares"]
    hogar=cliente["hogar"]
    total= agujas + escolares + hogar
    if  cliente["nacional"] == True:
        if total >= 200_000_000: 
            cliente_1 = {   
                "nombre":cliente["nombre"],
                "agujas":10.0,
                "escolares":10.0,
                "hogar":10.0,}
            return cliente_1
        elif total < 200_000_000:
            if agujas > 70_000_000 and hogar > 40_000_000 and escolares > 30_000_000:
                cliente_2 ={
                    "nombre":cliente["nombre"],
                    "agujas":7.0,
                    "escolares":7.0,
                    "hogar":7.0}
                return cliente_2
            else:
                if agujas > 70_000_000 and hogar < 40_000_000  and  escolares < 30_000_000:
                    cliente_2 ={
                        "nombre":cliente["nombre"],
                        "agujas":5.0,
                        "escolares":0.0,
                        "hogar":0.0}
                    return cliente_2
                elif agujas > 70_000_000 and  hogar > 40_000_000  and  escolares < 30_000_000:
                    cliente_2 ={
                        "nombre":cliente["nombre"],
                        "agujas":5.0,
                        "escolares":0.0,
                        "hogar":5.0}
                    return cliente_2
                elif agujas > 70_000_000 and  hogar < 40_000_000  and  escolares > 30_000_000:
                    cliente_2 ={
                        "nombre":cliente["nombre"],
                        "agujas":5.0,
                        "escolares":5.0,
                        "hogar":0.0}
                    return cliente_2
                elif agujas < 70_000_000 and  hogar < 40_000_000  and  escolares > 30_000_000:
                    cliente_2 ={
                        "nombre":cliente["nombre"],
                        "agujas":0.0,
                        "escolares":5.0,
                        "hogar":0.0}
                    return cliente_2
                elif agujas < 70_000_000 and  hogar > 40_000_000  and  escolares > 30_000_000:
                    cliente_2 ={
                        "nombre":cliente["nombre"],
                        "agujas":0.0,
                        "escolares":5.0,
                        "hogar":5.0}
                    return cliente_2
                elif agujas < 70_000_000 and  hogar > 40_000_000  and  escolares < 30_000_000:
                    cliente_2 ={
                        "nombre":cliente["nombre"],
                        "agujas":0.0,
                        "escolares":0.0,
                        "hogar":5.0}
                    return cliente_2
                elif agujas <= 70_000_000 and  hogar <= 40_000_000  and  escolares <= 30_000_000:
                    cliente_2 ={
                        "nombre":cliente["nombre"],
                        "agujas":0.0,
                        "escolares":0.0,
                        "hogar":0.0}
                    return cliente_2
        

    elif cliente["nacional"] == False:
        if total >= 100_000: 
            cliente_1 = {   
                "nombre":cliente["nombre"],
                "agujas":8.0,
                "escolares":8.0,
                "hogar":8.0,}
            return cliente_1
        elif total < 100_000:
            if agujas > 25_000 and hogar > 15_000 and escolares > 10_000:
                cliente_2 ={
                    "nombre":cliente["nombre"],
                    "agujas":5.0,
                    "escolares":5.0,
                    "hogar":5.0}
                return cliente_2
            else:
                if agujas > 25_000 and hogar < 15_000  and  escolares < 10_000:
                    cliente_2 ={
                        "nombre":cliente["nombre"],
                        "agujas":3.0,
                        "escolares":0.0,
                        "hogar":0.0}
                    return cliente_2
                elif agujas > 25_000 and  hogar > 15_000  and  escolares < 10_000:
                    cliente_2 ={
                        "nombre":cliente["nombre"],
                        "agujas":3.0,
                        "escolares":0.0,
                        "hogar":3.0}
                    return cliente_2
                elif agujas > 25_000 and  hogar < 15_000  and  escolares > 10_000:
                    cliente_2 ={
                        "nombre":cliente["nombre"],
                        "agujas":3.0,
                        "escolares":3.0,
                        "hogar":0.0}
                    return cliente_2
                elif agujas < 25_000 and  hogar < 15_000  and  escolares > 10_000:
                    cliente_2 ={
                        "nombre":cliente["nombre"],
                        "agujas":0.0,
                        "escolares":3.0,
                        "hogar":0.0}
                    return cliente_2
                elif agujas < 25_000 and  hogar > 15_000  and  escolares > 10_000:
                    cliente_2 ={
                        "nombre":cliente["nombre"],
                        "agujas":0.0,
                        "escolares":3.0,
                        "hogar":3.0}
                    return cliente_2
                elif agujas < 25_000 and  hogar > 15_000  and  escolares < 10_000:
                    cliente_2 ={
                        "nombre":cliente["nombre"],
                        "agujas":0.0,
                        "escolares":0.0,
                        "hogar":3.0}
                    return cliente_2
                elif agujas <= 25_000 and  hogar <= 15_000  and  escolares <= 10_000:
                    cliente_2 ={
                        "nombre":cliente["nombre"],
                        "agujas":0.0,
                        "escolares":0.0,
                        "hogar":0.0}
                    return cliente_2
        


print(calculo_recargos({"nombre": "César Díaz","nacional": True,"agujas": 0.0,"escolares": 0.0,"hogar": 0.0}))
print(calculo_recargos({"nombre": "César Díaz","nacional": True,"agujas": 150000000.0,"escolares": 30000000.0,"hogar": 20000000.0}))
print(calculo_recargos({"nombre": "César Díaz","nacional": True,"agujas": 100000001.0,"escolares": 32000000.0,"hogar": 41325120.0}))
print(calculo_recargos({"nombre": "César Díaz","nacional": True,"agujas": 70000100.0,"escolares": 20000000.0,"hogar": 40000001.0}))
print(calculo_recargos({"nombre": "César Díaz","nacional": True,"agujas": 70000000.0,"escolares": 30000000.0,"hogar": 40000000.0}))

print(calculo_recargos({"nombre": "César Díaz","nacional": False,"agujas": 0.0,"escolares": 0.0,"hogar": 0.0}))
print(calculo_recargos({"nombre": "César Díaz","nacional": False,"agujas": 25000.0,"escolares": 10000.0,"hogar": 15000.0}))
print(calculo_recargos({"nombre": "César Díaz","nacional": False,"agujas": 30000.0,"escolares": 20000.0,"hogar": 20000.0}))
print(calculo_recargos({"nombre": "César Díaz","nacional": False,"agujas": 80000.0,"escolares": 1500.0,"hogar": 5000.0}))
print(calculo_recargos({"nombre": "César Díaz","nacional": False,"agujas": 70000000.0,"escolares": 30000000.0,"hogar": 40000000.0}))
