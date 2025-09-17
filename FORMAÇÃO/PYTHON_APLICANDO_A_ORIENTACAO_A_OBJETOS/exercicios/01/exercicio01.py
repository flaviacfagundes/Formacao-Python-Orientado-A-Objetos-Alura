
class Musica:
    nome = ''
    artista = ''
    duracao = 0

musicas = []

eleanor_rigby = Musica()
eleanor_rigby.nome = 'Eleanor Rigby'
eleanor_rigby.artista = 'The Beatles'
eleanor_rigby.duracao = 126

bad_romance = Musica()
bad_romance.nome = 'Bad Romance'
bad_romance.artista = 'Lady Gaga'
bad_romance.duracao = 294

november_rain = Musica()
november_rain.nome = 'November Rain'
november_rain.artista = 'Guns N Roses'
november_rain.duracao = 536 

musicas.append(eleanor_rigby)
musicas.append(bad_romance)
musicas.append(november_rain)

print('')

for musica in musicas:
    print(vars(musica))

print('')
