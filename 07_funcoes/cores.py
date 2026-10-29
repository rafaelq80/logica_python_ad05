# Cores e estilos para texto no terminal (códigos ANSI)
#
# Como usar em outro arquivo:
#   from cores import FRENTE_VERDE, FUNDO_PRETO, RESET
#   print(FRENTE_VERDE + FUNDO_PRETO + "Texto colorido" + RESET)
#
# Sempre termine com RESET, senão o resto do terminal continua colorido.
# Para ver todas as opções, execute este arquivo: python cores.py

# Volta tudo ao normal (cor, fundo e estilo)
RESET = "\033[0m"

# ---------------------------------------------------------------
# Cor do TEXTO (foreground) - cores normais
# ---------------------------------------------------------------
FRENTE_PRETO = "\033[30m"
FRENTE_VERMELHO = "\033[31m"
FRENTE_VERDE = "\033[32m"
FRENTE_AMARELO = "\033[33m"
FRENTE_AZUL = "\033[34m"
FRENTE_MAGENTA = "\033[35m"
FRENTE_CIANO = "\033[36m"
FRENTE_BRANCO = "\033[37m"

# Cor do TEXTO (foreground) - cores claras (brilhantes)
FRENTE_CINZA = "\033[90m"
FRENTE_VERMELHO_CLARO = "\033[91m"
FRENTE_VERDE_CLARO = "\033[92m"
FRENTE_AMARELO_CLARO = "\033[93m"
FRENTE_AZUL_CLARO = "\033[94m"
FRENTE_MAGENTA_CLARO = "\033[95m"
FRENTE_CIANO_CLARO = "\033[96m"
FRENTE_BRANCO_CLARO = "\033[97m"

# ---------------------------------------------------------------
# Cor do FUNDO (background) - cores normais
# ---------------------------------------------------------------
FUNDO_PRETO = "\033[40m"
FUNDO_VERMELHO = "\033[41m"
FUNDO_VERDE = "\033[42m"
FUNDO_AMARELO = "\033[43m"
FUNDO_AZUL = "\033[44m"
FUNDO_MAGENTA = "\033[45m"
FUNDO_CIANO = "\033[46m"
FUNDO_BRANCO = "\033[47m"

# Cor do FUNDO (background) - cores claras (brilhantes)
FUNDO_CINZA = "\033[100m"
FUNDO_VERMELHO_CLARO = "\033[101m"
FUNDO_VERDE_CLARO = "\033[102m"
FUNDO_AMARELO_CLARO = "\033[103m"
FUNDO_AZUL_CLARO = "\033[104m"
FUNDO_MAGENTA_CLARO = "\033[105m"
FUNDO_CIANO_CLARO = "\033[106m"
FUNDO_BRANCO_CLARO = "\033[107m"

# ---------------------------------------------------------------
# Estilos (podem ser combinados com cores)
# Nem todo terminal suporta todos os estilos
# ---------------------------------------------------------------
ESTILO_NEGRITO = "\033[1m"
ESTILO_FRACO = "\033[2m"
ESTILO_ITALICO = "\033[3m"
ESTILO_SUBLINHADO = "\033[4m"
ESTILO_PISCANTE = "\033[5m"
ESTILO_INVERTIDO = "\033[7m"   # Troca a cor do texto com a do fundo
ESTILO_OCULTO = "\033[8m"
ESTILO_RISCADO = "\033[9m"


# ---------------------------------------------------------------
# Demonstração: mostra todas as opções acima na tela
# ---------------------------------------------------------------
if __name__ == "__main__":
    # globals() contém todas as variáveis do arquivo; filtramos pelas que
    # começam com FRENTE_, FUNDO_ ou ESTILO_
    for nome, codigo in list(globals().items()):
        if nome.startswith(("FRENTE_", "FUNDO_", "ESTILO_")):
            # O espaçamento (:<24) fica dentro da cor para o fundo ficar alinhado
            print(f"{codigo}{nome:<24}{RESET}")