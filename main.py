import json
from unicodedata import normalize

#Normalizar a texto 
def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

#Arquivo com o json das perguntas e respostas
with open('store.json') as json_file:
    data = json.load(json_file)

questoes=6 #Define quantas questoes tera
alternativas=4 #Define a quantidade de alternativas
k=0
for i in range(questoes*2):
    if i % 2 == 0:        
        k+=1
        print("\n Questao "+str(k)+": "+remover_acentos(data['questions'][i]['question']))
        for j in range(alternativas):
            print("("+str(j+1) + ") : " + data['questions'][i]['choices'][j]['label'])
    
