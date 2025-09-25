# Dados das culturas
culturas_data = []

# Dados técnicos das culturas
CAFE_INSUMOS = {
    'fungicida': 1.5,    # L/hectare
    'fertilizante': 400, # kg/hectare
    'herbicida': 2.0     # L/hectare
}

CANA_INSUMOS = {
    'herbicida': 3.0,    # L/hectare
    'fertilizante': 500, # kg/hectare
    'inseticida': 0.5    # L/hectare
}

def calcular_area_retangulo(comprimento, largura):
    """Calcula área do retângulo em hectares"""
    area_m2 = comprimento * largura
    return area_m2 / 10000  # Converte para hectares

def calcular_insumos(cultura, area_hectares, insumo):
    """Calcula quantidade de insumo necessária"""
    if cultura.lower() == 'cafe':
        return area_hectares * CAFE_INSUMOS.get(insumo, 0)
    elif cultura.lower() == 'cana':
        return area_hectares * CANA_INSUMOS.get(insumo, 0)
    return 0

def entrada_dados():
    """Entrada de novos dados de cultura"""
    print("\nENTRADA DE DADOS:")
    
    print("Culturas disponíveis:")
    print("1 - Café")
    print("2 - Cana-de-açúcar")
    
    opcao = input("Escolha a cultura (1 ou 2): ")
    
    if opcao == '1':
        cultura = 'cafe'
        nome_cultura = 'Café'
    elif opcao == '2':
        cultura = 'cana'
        nome_cultura = 'Cana-de-açúcar'
    else:
        print("Opção inválida!")
        return
    
    try:
        comprimento = float(input("Comprimento do terreno (metros): "))
        largura = float(input("Largura do terreno (metros): "))
        
        area = calcular_area_retangulo(comprimento, largura)
        
        dados = {
            'cultura': cultura,
            'nome_cultura': nome_cultura,
            'comprimento': comprimento,
            'largura': largura,
            'area_hectares': area
        }
        
        culturas_data.append(dados)
        print(f"\nDados adicionados com sucesso!")
        print(f"Área calculada: {area:.2f} hectares")
        
    except ValueError:
        print("Erro: Digite apenas números válidos!")

def saida_dados():
    """Exibe todos os dados cadastrados"""
    print("\nDADOS CADASTRADOS:")
    
    if not culturas_data:
        print("Nenhum dado cadastrado.")
        return
    
    for i, dados in enumerate(culturas_data):
        print(f"\n--- Registro {i+1} ---")
        print(f"Cultura: {dados['nome_cultura']}")
        print(f"Dimensões: {dados['comprimento']}m x {dados['largura']}m")
        print(f"Área: {dados['area_hectares']:.2f} hectares")
        
        # Mostrar cálculo de insumos
        print("Insumos necessários:")
        if dados['cultura'] == 'cafe':
            for insumo, taxa in CAFE_INSUMOS.items():
                quantidade = calcular_insumos(dados['cultura'], dados['area_hectares'], insumo)
                unidade = 'L' if insumo != 'fertilizante' else 'kg'
                print(f"  {insumo.capitalize()}: {quantidade:.2f} {unidade}")
        else:
            for insumo, taxa in CANA_INSUMOS.items():
                quantidade = calcular_insumos(dados['cultura'], dados['area_hectares'], insumo)
                unidade = 'L' if insumo != 'fertilizante' else 'kg'
                print(f"  {insumo.capitalize()}: {quantidade:.2f} {unidade}")

def atualizar_dados():
    """Atualiza dados em uma posição específica"""
    print("\nATUALIZAR DADOS:")
    
    if not culturas_data:
        print("Nenhum dado cadastrado para atualizar.")
        return
    
    print("Registros disponíveis:")
    for i, dados in enumerate(culturas_data):
        print(f"{i+1} - {dados['nome_cultura']} ({dados['area_hectares']:.2f} ha)")
    
    try:
        posicao = int(input("Digite o número do registro para atualizar: ")) - 1
        
        if 0 <= posicao < len(culturas_data):
            print(f"\nAtualizando: {culturas_data[posicao]['nome_cultura']}")
            
            comprimento = float(input("Novo comprimento (metros): "))
            largura = float(input("Nova largura (metros): "))
            
            area = calcular_area_retangulo(comprimento, largura)
            
            culturas_data[posicao]['comprimento'] = comprimento
            culturas_data[posicao]['largura'] = largura
            culturas_data[posicao]['area_hectares'] = area
            
            print("Dados atualizados com sucesso!")
            print(f"Nova área: {area:.2f} hectares")
        else:
            print("Posição inválida!")
            
    except (ValueError, IndexError):
        print("Erro: Digite um número válido!")

def deletar_dados():
    """Remove dados de uma posição específica"""
    print("\nDELETAR DADOS:")
    
    if not culturas_data:
        print("Nenhum dado cadastrado para deletar.")
        return
    
    print("Registros disponíveis:")
    for i, dados in enumerate(culturas_data):
        print(f"{i+1} - {dados['nome_cultura']} ({dados['area_hectares']:.2f} ha)")
    
    try:
        posicao = int(input("Digite o número do registro para deletar: ")) - 1
        
        if 0 <= posicao < len(culturas_data):
            dados_removidos = culturas_data.pop(posicao)
            print(f"Registro '{dados_removidos['nome_cultura']}' removido com sucesso!")
        else:
            print("Posição inválida!")
            
    except (ValueError, IndexError):
        print("Erro: Digite um número válido!")

def menu_principal():
    """Menu principal da aplicação"""
    while True:
        print("\n" + "="*50)
        print("    FARMTECH SOLUTIONS")
        print("="*50)
        print("1 - Entrada de dados")
        print("2 - Visualizar dados")
        print("3 - Atualizar dados")
        print("4 - Deletar dados")
        print("5 - Sair do programa")
        print("="*50)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            entrada_dados()
        elif opcao == '2':
            saida_dados()
        elif opcao == '3':
            atualizar_dados()
        elif opcao == '4':
            deletar_dados()
        elif opcao == '5':
            print("\nObrigado por usar o FarmTech Solutions!")
            print("Até logo! 🌱")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu_principal()
