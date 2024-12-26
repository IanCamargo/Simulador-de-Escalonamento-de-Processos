import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Função para calcular média
def calcular_media(tempos):
    return sum(tempos) / len(tempos)

# Função para simulação do escalonamento circular (Round-Robin)
def escalonamento_circular(processos, quantum):
    n = len(processos)
    tempo_atual = 0
    tempos_espera = [0] * n
    tempos_retorno = [0] * n
    fila = processos.copy()
    execucoes = []

    while any(p['tempo_restante'] > 0 for p in fila):
        for i in range(n):
            if fila[i]['tempo_restante'] > 0:
                tempo_exec = min(quantum, fila[i]['tempo_restante'])
                fila[i]['tempo_restante'] -= tempo_exec
                execucoes.append((fila[i]['id'], tempo_atual, tempo_atual + tempo_exec))
                tempo_atual += tempo_exec
                if fila[i]['tempo_restante'] == 0:
                    tempos_retorno[i] = tempo_atual

        for i in range(n):
            if fila[i]['tempo_restante'] > 0:
                tempos_espera[i] = tempo_atual - processos[i]['tempo_chegada'] - (processos[i]['tempo_execucao'] - fila[i]['tempo_restante'])

    tempo_turnaround = [tempos_retorno[i] - processos[i]['tempo_chegada'] for i in range(n)]
    tempo_medio_espera = calcular_media(tempos_espera)
    tempo_medio_turnaround = calcular_media(tempo_turnaround)

    return execucoes, tempos_espera, tempo_turnaround, tempo_medio_espera, tempo_medio_turnaround

# Função para simulação do escalonamento SJF (não preemptivo)
def escalonamento_sjf(processos):
    processos.sort(key=lambda p: p['tempo_execucao'])
    n = len(processos)
    tempo_atual = 0
    tempos_espera = [0] * n
    tempos_retorno = [0] * n
    execucoes = []

    for p in processos:
        if tempo_atual < p['tempo_chegada']:
            tempo_atual = p['tempo_chegada']
        tempos_espera[p['id'] - 1] = tempo_atual - p['tempo_chegada']
        execucoes.append((p['id'], tempo_atual, tempo_atual + p['tempo_execucao']))
        tempo_atual += p['tempo_execucao']
        tempos_retorno[p['id'] - 1] = tempo_atual

    tempo_turnaround = [tempos_retorno[i] - processos[i]['tempo_chegada'] for i in range(n)]
    tempo_medio_espera = calcular_media(tempos_espera)
    tempo_medio_turnaround = calcular_media(tempo_turnaround)

    return execucoes, tempos_espera, tempo_turnaround, tempo_medio_espera, tempo_medio_turnaround

# Função para exibir diagrama de Gantt com informações adicionais
def exibir_diagrama_gantt(execucoes, titulo, n_processos, tempo_medio_espera, tempo_medio_turnaround):
    colors = cm.get_cmap('tab10', n_processos)  # Mapa de cores
    plt.figure(figsize=(12, 6))

    # Gráfico de barras para o diagrama de Gantt
    for processo, inicio, fim in execucoes:
        plt.barh(f"P{processo}", fim - inicio, left=inicio, edgecolor='black', alpha=0.8, color=colors(processo - 1))

    # Adicionando texto com os tempos médios ao lado do gráfico
    plt.title(f"{titulo} - Diagrama de Gantt")
    plt.xlabel("Tempo")
    plt.ylabel("Processos")
    plt.tight_layout()

    # Adiciona os valores ao lado do gráfico
    texto = (
        f"Tempo médio de espera: {tempo_medio_espera:.2f}\n"
        f"Tempo médio de turnaround: {tempo_medio_turnaround:.2f}"
    )
    plt.figtext(0.85, 0.5, texto, fontsize=12, ha='center', va='baseline', bbox=dict(facecolor='lightgray', edgecolor='black'))

    plt.show()

# Entrada interativa de processos
def entrada_processos():
    processos = []
    n = int(input("Quantos processos deseja simular? "))
    for i in range(n):
        print(f"\nProcesso {i + 1}:")
        tempo_chegada = int(input("  Tempo de chegada: "))
        tempo_execucao = int(input("  Tempo de execução: "))
        processos.append({
            "id": i + 1,
            "tempo_chegada": tempo_chegada,
            "tempo_execucao": tempo_execucao,
            "tempo_restante": tempo_execucao
        })
    return processos

# Função principal
def main():
    print("\n### Simulador de Escalonamento de Processos ###")
    processos = entrada_processos()
    quantum = int(input("\nInforme o Quantum para o escalonamento Circular: "))

    print("\n### Escalonamento Circular (Round-Robin) ###")
    exec_rr, espera_rr, turnaround_rr, media_espera_rr, media_turnaround_rr = escalonamento_circular(processos, quantum)
    print(f"Tempo médio de espera: {media_espera_rr}")
    print(f"Tempo médio de turnaround: {media_turnaround_rr}")
    exibir_diagrama_gantt(exec_rr, "Escalonamento Circular (Round-Robin)", len(processos), media_espera_rr, media_turnaround_rr)

    # Resetando tempos restantes para o SJF
    for p in processos:
        p['tempo_restante'] = p['tempo_execucao']

    print("\n### Escalonamento SJF (Shortest Job First) ###")
    exec_sjf, espera_sjf, turnaround_sjf, media_espera_sjf, media_turnaround_sjf = escalonamento_sjf(processos)
    print(f"Tempo médio de espera: {media_espera_sjf}")
    print(f"Tempo médio de turnaround: {media_turnaround_sjf}")
    exibir_diagrama_gantt(exec_sjf, "Escalonamento SJF (Shortest Job First)", len(processos), media_espera_sjf, media_turnaround_sjf)

# Executar o programa
if __name__ == "__main__":
    main()