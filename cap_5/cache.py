cache = {}


def pega_dados_do_servidor(url):
    nome = "Lucas"
    return nome


def pega_pagina(url):
    if cache.get(url):
        return cache[url]
    else:
        dados = pega_dados_do_servidor(url)
        cache[url] = dados
        return dados


if __name__ == '__main__':
    print(cache)
    print("não encontrei, vou analisar no servidor........")
    pega_pagina("site/lucas")
    print("encontrei armazenei os dados abaixo:")
    print(cache)
    print("procurando os dados...")
    print("esta aqui seus dados:")
    print(pega_pagina("site/lucas"))
