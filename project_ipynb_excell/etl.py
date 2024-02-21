import pandas as pd
import glob
# read .xlsx file in the current directory

path = 'project_ipynb_excell\\manual\\base_tratada_excel.xlsx'
#pandas read excel
df = pd.read_excel(path)
#print(df)
mapa = {
    "1":"1º Ano",
    "2":"2º Ano",
    "3":"3º Ano",
    "4":"4º Ano",    
    "5":"5º ano",
    "6":"6º Ano",
    "7":"7º Ano",
    "8":"8º Ano",
    "9":"9º Ano"
}
#
df = (
    df
    .assign(SERIE = df['TURMA'].str[0])
)
#
df = (
    df
    .assign(SERIE = df['SERIE'].map(mapa))
    .assign(NOME = df['NOME'].str.upper())
    .assign(ESCOLA = df['ESCOLA'].str.upper())
)
print(df)
#df.to_csv("anapolis_t1.csv", sep=",", encoding="utf-8", index=False, header=True)
df.to_csv("anapolis.csv", sep=";", encoding="ISO-8859-1", index=False, header=True)
 



