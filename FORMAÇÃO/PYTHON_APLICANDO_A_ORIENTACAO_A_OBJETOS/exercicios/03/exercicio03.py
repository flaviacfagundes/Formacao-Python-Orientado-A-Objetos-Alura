
class Musica:
    musicas = []

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)
    
    def __str__(self):
        return f'Música: {self.nome} \nArtista: {self.artista} \nDuração: {self.duracao}'
    
    def listar_musicas():
        for musica in Musica.musicas:
            print('')
            print(f'• Música: {musica.nome} \n• Artista: {musica.artista} \n• Duração: {musica.duracao}')
        print('')

musica1 = Musica('Whole Lotta Love', 'Led Zeppelin', 333)
musica2 = Musica('Holiday', 'Green Day', 232)

Musica.listar_musicas()
