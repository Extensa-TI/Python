"""
Modulo Collections - Counter

Collections -> High-performance Container Datetypes

Counter -> Recebe um iterável como parâmetro
"""
from collections import Counter

lista = [1,1,1,1,2,2,3,3,3,3,1,1,2,2,4,4,4,5,5,5,5,3,45,46,66,66,43,34]
res = Counter(lista)
print(type(res))
print(res)

print(Counter('Geek University'))

texto = """Más Notícias é uma obra de arte feita por Rodolfo Amoedo em 1895. 
Retrata uma mulher sentada em uma poltrona, com o olhar direcionado para a frente, 
encarando quem a observa. O quadro está localizado no Museu Nacional de Belas Artes 
e caracteriza-se por unir traços realistas de pintura e de outros movimentos 
nascentes no Brasil, como o simbolismo e o modernismo. 
A conexão de diversas influências fez com que esse quadro fosse interpretado como 
especialmente relevante para a história da arte brasileira.
Apresentada na Segunda Exposição Geral da Escola Nacional de Belas Artes (ENBA), 
a obra de Amoedo foi considerada fora dos cânones da pintura mais convencional 
e acadêmica. Foi celebrada pela crítica especializada por introduzir correntes 
artísticas novas ao Brasil, já em voga na Europa onde o artista havia estado alguns 
anos antes do lançamento, e realizar na arte uma investigação da psicologia feminina.
A pintura de Amoedo ainda se tornou a expressão de mudanças mais amplas na sociedade. 
Características da obra, como seu tamanho e tema, foram associadas ao fortalecimento 
da burguesia e a mudanças na relação entre arte e vida doméstica. """

palavras = texto.split()
print(palavras)
res = Counter(palavras)
print(res)
# most_common (mais ocorrência)
print(res.most_common(5))
