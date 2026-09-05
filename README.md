# Projeto I - Análise Estatística do Desempenho dos Alunos

Este projeto realiza uma análise estatística exploratória e descritiva sobre os dados de desempenho acadêmico de estudantes na disciplina de Matemática, utilizando a linguagem **Python** e as bibliotecas **Pandas** e **Matplotlib**.

---

## Estrutura do Projeto

```text
├── dados/
│   └── student-mat.csv       # Base de dados dos estudantes
├── graficos/                 # Gráficos gerados pela análise
│   ├── 01_histograma_g3.png
│   ├── 02_boxplot_g3.png
│   ├── 03_medias_g1_g2_g3.png
│   └── 04_faltas_g3.png
├── projeto.py                # Script principal de análise estatística
├── requirements.txt          # Dependências do projeto
└── README.md                 # Documentação
```

---

## Análises Realizadas

1. **Conhecendo a Base de Dados**:
   - Total de registros e variáveis.
   - Pré-visualização dos primeiros registros.
   - Verificação e contagem de dados ausentes / nulos.

2. **Medidas Estatísticas**:
   - **Medidas de Posição**: Média, Mediana e Moda da nota final ($G_3$).
   - **Medidas de Dispersão**: Desvio Padrão e Coeficiente de Variação ($CV$).
   - **Estatísticas Descritivas**: Resumo completo com quartis (25%, 50%, 75%), mínimo e máximo.

3. **Visualizações Gráficas**:
   - **Histograma**: Distribuição das notas finais com linhas de referência para a média e mediana.
   - **Boxplot**: Visualização de quartis, mediana e identificação de discrepâncias (outliers).
   - **Gráfico de Barras**: Comparação evolutiva das médias entre as avaliações $G_1$, $G_2$ e $G_3$.
   - **Gráfico de Dispersão**: Relação e impacto do número de faltas na nota final do estudante.

---

## Como Executar

### 1. Clonar o repositório
```bash
git clone https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
cd NOME-DO-REPOSITORIO
```

### 2. Criar e ativar o ambiente virtual (opcional, mas recomendado)
```bash
# Windows
python -m venv .venv
.\.venv\Scripts\activate

# Linux / Mac
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4. Executar o script
```bash
python projeto.py
```

---

## Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
