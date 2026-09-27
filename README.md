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
│   ├── 04_faltas_g3.png
│   └── 05_regressao_linear_g1_g3.png
├── projeto.py                # Script da Fase 1 (Análise Exploratória e Descritiva)
├── fase2_regressao.py        # Script da Fase 2 (Regressão Linear Simples e Dispersão)
├── requirements.txt          # Dependências do projeto
└── README.md                 # Documentação
```

---

## Análises Realizadas

### Fase 1: Análise Exploratória e Estatística Descritiva Univariada
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

### Fase 2: Análise Bivariada e Regressão Linear Simples ($G_1 \rightarrow G_3$)
Estudo da relação linear entre a **Nota do 1º Período ($G_1$)** (variável independente $X$) e a **Nota Final ($G_3$)** (variável dependente $Y$).

1. **Fórmulas e Métricas Calculadas**:
   - **Covariância Amostral**:
     $$\text{Cov}(X, Y) = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{n - 1}$$
   - **Coeficiente de Correlação de Pearson ($r$)**:
     $$r = \frac{\text{Cov}(X, Y)}{s_x s_y}$$
   - **Reta de Regressão Linear Simples ($y = ax + b$)**:
     $$a = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} = \frac{\text{Cov}(X, Y)}{s_x^2}, \quad b = \bar{y} - a\bar{x}$$
   - **Coeficiente de Determinação ($R^2$)**:
     $$R^2 = r^2 \quad (\text{proporção da variância de } Y \text{ explicada por } X)$$

2. **Resultados Obtidos no Dataset**:
   - $\bar{X} \ (G_1) = 10.91$, $\bar{Y} \ (G_3) = 10.42$
   - $\text{Cov}(X, Y) = 12.1877$
   - $r = 0.8015$ (Correlação **forte** e **positiva**)
   - $R^2 = 0.6424$ ($64.24\%$ da variância da nota final é explicada pela nota do 1º período)
   - Reta de Regressão: $y = 1.1063x - 1.6528$

3. **Visualização Gráfica**:
   - **05_regressao_linear_g1_g3.png**: Diagrama de dispersão com os pontos observados, reta de regressão ajustada, linhas de marcação para as médias $\bar{x}$ e $\bar{y}$, centroide amostral e legendas detalhadas.

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

### 4. Executar os scripts

- **Executar a Fase 1 (Estatística Descritiva e Gráficos Gerais):**
  ```bash
  python projeto.py
  ```

- **Executar a Fase 2 (Regressão Linear e Correlação):**
  ```bash
  python fase2_regressao.py
  ```

---

## Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
