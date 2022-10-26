while True: 
    try:
        orientacao=input()
        def orienta(dizer):
            if dizer == 'esquerda':
                print('ingles')
            elif dizer =='direita':
                print('frances')
            elif dizer == 'nenhuma':
                print('portugues')
            elif dizer =='ambas':
                print('caiu')
        orienta(orientacao)
    except EOFError: 
        break