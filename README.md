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

---

### 📥 4. Inserir Processos

- Após iniciar o programa, você será solicitado a informar o número de processos.
- Para cada processo, insira:
  - Tempo de chegada: Momento em que o processo está disponível.
  - Tempo de execução: Duração necessária para executar o processo.
- Informe o valor do quantum para o algoritmo Round-Robin.

---

### 📊 5. Resultados Gerados

- Round-Robin:
  - Tempos médios:
    - Tempo médio de espera.
    - Tempo médio de turnaround.
  - Diagrama de Gantt com as execuções de cada processo.

- SJF (Shortest Job First):
  - Tempos médios:
    - Tempo médio de espera.
    - Tempo médio de turnaround.
  - Diagrama de Gantt com a sequência otimizada pelo menor tempo de execução.

---

### 🖥️ 6. Guia de Uso

- Exemplo de Uso
  - Entrada
    - Número de processos: 3
    - Processos:
      - Processo 1: Tempo de chegada = 0, Tempo de execução = 5
      - Processo 2: Tempo de chegada = 2, Tempo de execução = 3
      - Processo 3: Tempo de chegada = 4, Tempo de execução = 2
    - Quantum (Round-Robin): 2

- Saída
  
  - Round-Robin:
    - Tempo médio de espera: 4.67
    - Tempo médio de turnaround: 9.33
  - Diagrama de Gantt:
```sh
P1 [0-2] -> P2 [2-4] -> P3 [4-6] -> P1 [6-8] -> P2 [8-9] -> P1 [9-10]
```

  - SJF:
    - Tempo médio de espera: 3.33
    - Tempo médio de turnaround: 7.67
  - Diagrama de Gantt:
```sh
P3 [4-6] -> P2 [6-9] -> P1 [0-5]
```

---

## 🎨 Diagrama de Gantt
Os diagramas de Gantt exibem cada processo como uma barra horizontal no tempo em que foi executado, com cores distintas para cada processo. Os diagramas são exibidos automaticamente após a execução dos algoritmos e incluem:

- Processos: Identificados no eixo Y.
- Intervalos de execução: Representados no eixo X.

---

## 🤝 Contribuindo
Contribuições são bem-vindas!
Se você deseja contribuir:

- Faça um fork do repositório.
- Crie uma nova branch:

```sh
git checkout -b minha-contribuicao
```

- Envie suas alterações por um pull request.

--- 

## 📝 Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais informações.

--- 

## 📧 Contato
**Email:** ian.camargo@fatec.sp.gov.br \
**LinkedIn:** https://www.linkedin.com/in/ian-camargo-aa19a2214/
