nomes = ["ana", "bruno", "carlos", "daniela", "eduardo", "fernanda",
         "gabriel", "helena", "igor", "juliana", "karla", "lucas", "mariana"]


def remover_vogais(nome):
    return ''.join([letra for letra in nome if letra not in 'aeiouAEIOU'])


primeiros_10_nomes_sem_vogais = [remover_vogais(nome) for nome in nomes[:10]]

print(primeiros_10_nomes_sem_vogais)
