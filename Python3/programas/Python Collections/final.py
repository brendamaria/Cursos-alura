from collections import Counter

def contador(txt):
    frequencia_de_letras = Counter(txt.lower().split(" "))
    letras_contadas = sum(frequencia_de_letras.values())
    print(f"A quantidade de letras é {letras_contadas}")

    proporcao = [(letra, porcentagem / letras_contadas) for letra, porcentagem in frequencia_de_letras.items()]
    proporcao = Counter(dict(proporcao))
    porcentagem = proporcao.most_common(10)

    print("------------------------------- \n")
    print("A frequencia de letras é: ")
    for caractere, porcento in porcentagem:
        print(f"{caractere} --> {porcento * 100:.2f}%")


texto1 = ''' A Segunda Guerra Mundial revelou para o mundo as piores ações realizas em conflitos entre exércitos de países rivais. 
Como dito, anteriormente havia também atitudes exageradas, mas foi tal conflito que reuniu países do mundo inteiro o primeiro a apresentar para o mundo as situações de guerra com maior profundidade. 
O grupo dos países do Eixo, que reunia as ditaduras fascistas como Alemanha, Itália e Japão, foi o grande promotor de violação dos direitos humanos. O líder alemão Adolf Hitler promoveu uma série de ações que desrespeitaram assustadoramente os direitos humanos. 
Ele foi o responsável pelo genocídio de judeus promovido nos campos de concentração, do qual resultaram aproximadamente 6 milhões de mortes. O seu exército nazista se encarregou ainda de matar civis e prisioneiros. Tais condutas chocaram o mundo, após a guerra. 
O conceito de Crimes de Guerra só surgiu mesmo após o conflito mundial e a revelação das ações exageradas. 
A partir de então, surgiram leis internacionais que se destinavam a condenar tais ações. 
Já nos anos de 1945 e 1946, o Tribunal de Nuremberg julgou e condenou os nazistas por seus crimes cometidos na Segunda Guerra Mundial. Na ocasião, foram executados doze líderes nazistas. Da mesma forma, um tribunal julgou e condenou sete comandantes japoneses à morte em Tóquio, em 1948. 
A Convenção de Genebra, que foi criada em 1864, inseriu os Crimes de Guerra nas leis internacionais após a Segunda Guerra Mundial. Sua legislação é quem define Crimes de Guerra como ataques voluntários contra civis, prisioneiros e feridos, em tempos de guerra. 
Mas sua contínua modificação acrescentou genocídios e crimes contra a humanidade na lista dos Crimes de Guerra. De acordo com o grupo de leis, um indivíduo pode ser condenado pelas ações tomadas por um país ou por integrantes de seu exército. 
Os acordos internacionais que inseriram Crimes de Guerra na Convenção de Genebra são geridos pela Corte Penal Internacional, a qual tem competência para julgar os Crimes de Guerra. Recentemente, o Tribunal de Haia passou a julgar os Crimes de Guerra e considerar também estupros em massa e escravização sexual como integrantes dos crimes contra a humanidade. 
Desrespeitar a Convenção de Genebra é também um Crime de Guerra.
'''

texto2 = ''' Segundo a teoria de Einstein, a força da gravidade seria uma manifestação da deformação no espaço-tempo causada pela massa dos corpos celestes, como os planetas ou estrelas. 
Essa deformação seria maior ou menor de acordo com a massa ou a densidade do corpo. Portanto, quanto maior a massa do corpo, maior a deformação e, por sua vez, maior a força de gravidade dele. 
Consequentemente, maior é a velocidade de escape, força mínima que deve ser empregada, para que um objeto possa vencer a gravidade deste corpo. Por exemplo, para que um foguete saia da atmosfera terrestre para o espaço ele precisa de uma força de escape de 40.320 km/h. 
Em Júpiter, essa força teria de ser 214.200 km/h. Essa diferença muito grande, é porque sua massa é muito maior que a da Terra.
É isso que acontece nos buracos negros. Há uma concentração de massa tão grande em um ponto tão infinitamente pequeno que a densidade é suficiente para causar tal deformação no espaço-tempo que a velocidade de escape neste local é maior que a da luz. 
Por isso que nem mesmo a luz consegue escapar de um buraco negro. E, já que nada consegue se mover mais rápido que a velocidade da luz, nada pode escapar de um buraco negro.
'''


contador(texto1)
contador(texto2)
