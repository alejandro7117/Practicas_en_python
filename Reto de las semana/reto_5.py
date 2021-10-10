import pandas as pd

def analisis_covid_ciclo_sexo(ruta_archivo:str)-> dict:
    
    #validar que fromato es csvg
    partes= ruta_archivo.split(".")
    if partes[-1].lower() != "csv":
        return "Formato de archivo no válido"

    #algoritmo
    try:
        df=pd.read_csv(ruta_archivo)
        
        df_analisis=pd.DataFrame()
        df_analisis["Sexo"]= df["Sexo"].apply(str.upper)

        def ciclo_vital(edad):
            if edad <=5:
                return "Primera infancia"
            elif edad <= 11:
                return "Infancia"
            elif edad <= 18:
                return "Adolescencia"
            elif edad <= 26:
                return "Juventud"
            elif edad <= 59:
                return "Adultez"
            else:
                return "Persona Mayor"
        
        df_analisis["Ciclo"] = df["Edad"].apply(ciclo_vital)

    #retornar
        return df_analisis.groupby(["Ciclo","Sexo"]).size().unstack().to_dict()
   
    except :
        return "Error procesando el archivo"


    

    

print(analisis_covid_ciclo_sexo("archivo.txt"))
print(analisis_covid_ciclo_sexo("archivo.csv"))
print(analisis_covid_ciclo_sexo("archivo.xls"))

print(analisis_covid_ciclo_sexo("https://raw.githubusercontent.com/cesardiaz-utp/MisionTIC2022-Ciclo1-FundamentosDeProgramacion/main/clase16/Casos_positivos_de_COVID-19_en_ColombiaDiezMil.csv"))