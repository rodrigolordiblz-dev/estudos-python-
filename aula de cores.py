'''print('\033[30;43;  molá mundo!\033[0m')

nome = 'rodrigo'
print('ola, muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

#outra forma pode ser utilizando dicionarios

nome = 'rodrigo'
cores = {
    'limpa': '\033[m',
    'preto': '\033[30m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'magenta': '\033[35m',
    'ciano': '\033[36m',
    'branco': '\033[37m',

    'preto_claro': '\033[90m',
    'vermelho_claro': '\033[91m',
    'verde_claro': '\033[92m',
    'amarelo_claro': '\033[93m',
    'azul_claro': '\033[94m',
    'magenta_claro': '\033[95m',
    'ciano_claro': '\033[96m',
    'branco_claro': '\033[97m',

    'fundo_preto': '\033[40m',
    'fundo_vermelho': '\033[41m',
    'fundo_verde': '\033[42m',
    'fundo_amarelo': '\033[43m',
    'fundo_azul': '\033[44m',
    'fundo_magenta': '\033[45m',
    'fundo_ciano': '\033[46m',
    'fundo_branco': '\033[47m',

    'negrito': '\033[1m',
    'sublinhado': '\033[4m',
    'inverso': '\033[7m',

    'pretoebranco': '\033[7;30m'  # fundo branco, texto preto
}

print('ola! muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))'''


nome = 'rodrigo'
cores = {
    'limpa': '\033[m',
    'preto': '\033[30m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'magenta': '\033[35m',
    'ciano': '\033[36m',
    'branco': '\033[37m',

    'preto_claro': '\033[90m',
    'vermelho_claro': '\033[91m',
    'verde_claro': '\033[92m',
    'amarelo_claro': '\033[93m',
    'azul_claro': '\033[94m',
    'magenta_claro': '\033[95m',
    'ciano_claro': '\033[96m',
    'branco_claro': '\033[97m',

    'fundo_preto': '\033[40m',
    'fundo_vermelho': '\033[41m',
    'fundo_verde': '\033[42m',
    'fundo_amarelo': '\033[43m',
    'fundo_azul': '\033[44m',
    'fundo_magenta': '\033[45m',
    'fundo_ciano': '\033[46m',
    'fundo_branco': '\033[47m',

    'negrito': '\033[1m',
    'sublinhado': '\033[4m',
    'inverso': '\033[7m',

    'pretoebranco': '\033[7;30m'
}

for cor, codigo in cores.items():
    if cor != 'limpa':
        print(f"{codigo}{cor}: {nome}{cores['limpa']}")
