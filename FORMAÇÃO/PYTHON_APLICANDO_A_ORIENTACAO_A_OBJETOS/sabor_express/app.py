from modelos.restaurante import Restaurante

restaurante_kfc = Restaurante('KFC0', 'Fast Food')
restaurante_ravello = Restaurante('Ravello', 'Italiano')
restaurante_comodoro = Restaurante('Comodoro', 'Hamburgueria')

restaurante_ravello.alterar_status()
restaurante_kfc.receber_avaliacao('Sergio', 10)
restaurante_kfc.receber_avaliacao('Claudia', 8)
restaurante_kfc.receber_avaliacao('Giovanna', 5)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()