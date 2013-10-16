#!/usr/bin/env python
#Lista 4 de Exercícios
'''
4.Seja o statement sobre diversidade:
“The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.”
.Gere uma lista de palavras deste texto com split(), a seguir crie uma lista com as palavras que
começam ou terminam com uma das letras “python”.
Imprima a lista resultante.Não  se esqueça de remover antes os caracteres especiais
e cuidado com maiúsculas e minúsculas.
'''
def achePython():
    texto = 'The Python Software Foundation and the global Python\
    community welcome and encourage participation by everyone. Our community is based on\
    mutual respect, tolerance, and encouragement, and we are working to help each other live up\
    to these principles. We want our community to be more diverse: whoever you are, and\
    whatever your background, we welcome YOU.'

    #gera um lista com letras da palavra python
    letrasPy = list('python')

    #transforma var texto em um lista de suas palavras, separando-as por espaços
    texto = texto.split()
    
    #lista para resultado
    contemPy = []
    for word in texto:
        #Quem não sabe usar regex em python, levanta a mão: \o/
        word = ((word.replace(',','')).replace('.','')).replace(':','')

        #case sensitive's free zone \o/ - apenas para validar o if...
        if str(word[0]).lower() in letrasPy or str(word[-1]).lower() in letrasPy:
            contemPy.append(word)

    print("Palavras filtradas: \n %s"%contemPy) 
    '''
    5.Seja o mesmo texto acima “splitado”.Calcule quantas palavras possuem uma das letras
    “python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para
    minúsculas e de remover antes os caracteres especiais.
    '''
    #Guarda o total de palavras que possuem uma das letras "python"
    totalContPy = 0
    for word in contemPy:
        if len(word) > 4:
            totalContPy +=1
    print("Total de palavras com alguma letra 'python' e com +  de 4 caracteres: %d"%totalContPy)
achePython()
