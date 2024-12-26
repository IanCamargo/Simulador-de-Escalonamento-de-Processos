# Simulador de Escalonamento de Processos

Este projeto é um simulador de algoritmos de escalonamento de processos que implementa **Circular (Round-Robin)** e **Shortest Job First (SJF)**. Ele permite analisar o desempenho desses algoritmos por meio de cálculos de tempos médios e diagramas de Gantt interativos.

---

## 🚀 Funcionalidades

- Entrada interativa para configurar processos (tempo de chegada e execução).
- Implementação dos algoritmos:
  - **Round-Robin (com Quantum configurável).**
  - **SJF (não preemptivo).**
- Cálculo de tempos médios de espera e turnaround para ambos os algoritmos.
- Geração de diagramas de Gantt para visualização das execuções.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Matplotlib** (para diagramas de Gantt)

---

## 📦 Como Instalar e Usar

### 1. Pré-requisitos

- Certifique-se de ter **Python 3.x** instalado.
- Instale a biblioteca `matplotlib`:
  ```sh
  pip install matplotlib
  ```

---

### 2. Clonar o Repositório
  ```sh
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
  ```
---

### 3. Executar o Simulador
  ```bash
Copiar código
python escalonador_processos.py
  ```

### 4. Inserir Processos

- Após iniciar o programa, você será solicitado a informar o número de processos.
- Para cada processo, insira:
  - Tempo de chegada: Momento em que o processo está disponível.
  - Tempo de execução: Duração necessária para executar o processo.
- Informe o valor do quantum para o algoritmo Round-Robin.

