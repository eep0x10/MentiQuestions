import json
from unicodedata import normalize

#Funcao para normalizar a texto 
def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

#Lê o arquivo store.json
with open('store.json') as json_file:
    data = json.load(json_file)

questoes=6 #Quantidade de questoes
alternativas=4 #Quantidade de alternativas
k=0
for i in range(questoes*2):
    if i % 2 == 0:        
        k+=1
        print("\n Questao "+str(k)+": "+remover_acentos(data['questions'][i]['question']))
        for j in range(alternativas):
            print("("+str(j+1) + ") : " + data['questions'][i]['choices'][j]['label'])
    
