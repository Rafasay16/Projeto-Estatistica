# ============================================================
# PROJETO I - ANÁLISE ESTATÍSTICA DO DESEMPENHO DOS ALUNOS
# ============================================================


# ============================================================
# 1. IMPORTAÇÃO DAS BIBLIOTECAS
# ============================================================

from pathlib import Path

# O Pandas é utilizado para carregar, organizar e analisar
# os dados do nosso banco de dados.
import pandas as pd

# O Matplotlib é utilizado para criar os gráficos.
import matplotlib.pyplot as plt

# Diretório base do script
BASE_DIR = Path(__file__).resolve().parent
PASTA_GRAFICOS = BASE_DIR / "graficos"
PASTA_GRAFICOS.mkdir(parents=True, exist_ok=True)


# ============================================================
# 2. CARREGAMENTO DO BANCO DE DADOS
# ============================================================

# Aqui estamos lendo o arquivo CSV que está dentro da pasta
# "dados".
#
# "df" significa DataFrame, que é a estrutura usada pelo
# Pandas para armazenar os dados em linhas e colunas.
#
# O parâmetro sep=";" informa que os dados do arquivo CSV
# estão separados por ponto e vírgula.

df = pd.read_csv(
    BASE_DIR / "dados" / "student-mat.csv",
    sep=";"
)


# ============================================================
# 3. CONHECENDO O BANCO DE DADOS
# ============================================================

print("=" * 60)
print("INFORMAÇÕES DO BANCO DE DADOS")
print("=" * 60)

# df.shape[0] mostra a quantidade de linhas/registros.
print(f"Quantidade de registros: {df.shape[0]}")

# df.shape[1] mostra a quantidade de colunas/variáveis.
print(f"Quantidade de variáveis: {df.shape[1]}")

# head() mostra os primeiros 5 registros do banco.
print("\nPrimeiros 5 registros:")
print(df.head())


# ============================================================
# 4. VERIFICAÇÃO DE DADOS AUSENTES
# ============================================================

print("\n" + "=" * 60)
print("VERIFICAÇÃO DE DADOS AUSENTES")
print("=" * 60)

# isnull() identifica os valores vazios.
# sum() conta quantos valores vazios existem em cada coluna.

dados_ausentes = df.isnull().sum()

print(dados_ausentes)

# Aqui verificamos se a soma de todos os valores ausentes
# é igual a zero.
#
# Se for zero, significa que não existem dados ausentes.

if dados_ausentes.sum() == 0:
    print("\nNão existem dados ausentes no banco.")
else:
    print("\nExistem dados ausentes no banco.")


# ============================================================
# 5. SELEÇÃO DA VARIÁVEL PRINCIPAL
# ============================================================

# A variável G3 representa a nota final do estudante
# na disciplina de Matemática.
#
# Vamos armazenar essa coluna na variável "notas_finais"
# para facilitar os cálculos.

notas_finais = df["G3"]


# ============================================================
# 6. MEDIDAS DE POSIÇÃO
# ============================================================

# MÉDIA
#
# mean() calcula a média aritmética de todas as notas.

media = notas_finais.mean()


# MEDIANA
#
# median() encontra o valor central das notas quando elas
# são organizadas em ordem crescente.

mediana = notas_finais.median()


# MODA
#
# mode() identifica a nota que aparece com maior frequência.
#
# O resultado é armazenado em "moda" porque pode existir
# mais de uma moda.

moda = notas_finais.mode()


# Mostramos os resultados no terminal.

print("\n" + "=" * 60)
print("MEDIDAS DE POSIÇÃO - NOTA FINAL (G3)")
print("=" * 60)

print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda: {moda.tolist()}")


# ============================================================
# 7. MEDIDAS DE DISPERSÃO
# ============================================================

# DESVIO PADRÃO
#
# std() calcula o desvio padrão das notas.
#
# Ele mostra o quanto os valores estão dispersos em relação
# à média.

desvio_padrao = notas_finais.std()


# COEFICIENTE DE VARIAÇÃO
#
# O coeficiente de variação relaciona o desvio padrão
# com a média e apresenta o resultado em porcentagem.

coeficiente_variacao = (
    desvio_padrao / media
) * 100


print("\n" + "=" * 60)
print("MEDIDAS DE DISPERSÃO - NOTA FINAL (G3)")
print("=" * 60)

print(f"Desvio padrão: {desvio_padrao:.2f}")
print(f"Coeficiente de variação: {coeficiente_variacao:.2f}%")


# ============================================================
# 8. ESTATÍSTICAS DESCRITIVAS
# ============================================================

# describe() calcula várias estatísticas descritivas
# automaticamente.
#
# Entre elas:
# count = quantidade de valores
# mean  = média
# std   = desvio padrão
# min   = menor valor
# 25%   = primeiro quartil
# 50%   = mediana
# 75%   = terceiro quartil
# max   = maior valor

estatisticas = notas_finais.describe()


print("\n" + "=" * 60)
print("ESTATÍSTICAS DESCRITIVAS - NOTA FINAL (G3)")
print("=" * 60)

print(estatisticas)


# ============================================================
# 9. GRÁFICO 1 - HISTOGRAMA
# ============================================================

# figure() cria uma área para o gráfico.
# figsize define o tamanho da figura.

plt.figure(figsize=(10, 6))


# hist() cria o histograma.
#
# Estamos utilizando os valores da variável G3.
#
# bins=11 divide os valores em 11 intervalos.
#
# color define a cor das barras.
#
# edgecolor define a cor das bordas.
#
# alpha controla a transparência.

plt.hist(
    notas_finais,
    bins=11,
    color="steelblue",
    edgecolor="black",
    alpha=0.8
)


# Aqui criamos uma linha vertical indicando a média.

plt.axvline(
    media,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Média = {media:.2f}"
)


# Aqui criamos uma linha vertical indicando a mediana.

plt.axvline(
    mediana,
    color="green",
    linestyle="--",
    linewidth=2,
    label=f"Mediana = {mediana:.2f}"
)


# Título do gráfico.

plt.title("Distribuição das Notas Finais - Matemática")


# Nome do eixo horizontal.

plt.xlabel("Nota Final (G3)")


# Nome do eixo vertical.

plt.ylabel("Quantidade de Alunos")


# Mostra a legenda das linhas de média e mediana.

plt.legend()


# Adiciona uma grade horizontal para facilitar a leitura.

plt.grid(axis="y", alpha=0.3)


# Ajusta automaticamente os elementos do gráfico.

plt.tight_layout()


# Salva o gráfico dentro da pasta "graficos".

# dpi=300 aumenta a qualidade da imagem.

plt.savefig(
    PASTA_GRAFICOS / "01_histograma_g3.png",
    dpi=300
)


# Mostra o gráfico na tela.

plt.show()


# ============================================================
# 10. GRÁFICO 2 - BOXPLOT
# ============================================================

plt.figure(figsize=(8, 6))


# boxplot cria o gráfico de caixa.
#
# Ele permite visualizar:
# - mínimo
# - primeiro quartil
# - mediana
# - terceiro quartil
# - máximo
# - possíveis valores discrepantes

plt.boxplot(
    notas_finais,
    patch_artist=True,
    boxprops=dict(
        facecolor="lightblue"
    ),
    medianprops=dict(
        color="red",
        linewidth=2
    )
)


plt.title("Boxplot das Notas Finais - Matemática")

plt.ylabel("Nota Final (G3)")

plt.grid(
    axis="y",
    alpha=0.3
)

plt.tight_layout()


# Salva o boxplot na pasta de gráficos.

plt.savefig(
    PASTA_GRAFICOS / "02_boxplot_g3.png",
    dpi=300
)


plt.show()


# ============================================================
# 11. GRÁFICO 3 - COMPARAÇÃO ENTRE G1, G2 E G3
# ============================================================

# Aqui selecionamos as colunas G1, G2 e G3.
#
# Depois utilizamos mean() para calcular a média de cada
# uma dessas avaliações.

medias = df[["G1", "G2", "G3"]].mean()


plt.figure(figsize=(8, 6))


# bar() cria um gráfico de barras.
#
# As três barras representam as médias de G1, G2 e G3.

plt.bar(
    ["G1", "G2", "G3"],
    medias,
    color=[
        "orange",
        "steelblue",
        "green"
    ],
    edgecolor="black"
)


plt.title("Média das Notas - G1, G2 e G3")

plt.xlabel("Avaliação")

plt.ylabel("Média das Notas")


# Como as notas vão de 0 a 20,
# configuramos o eixo para essa mesma escala.

plt.ylim(0, 20)


# Este for coloca o valor da média acima de cada barra.

for i, valor in enumerate(medias):

    plt.text(
        i,
        valor + 0.3,
        f"{valor:.2f}",
        ha="center"
    )


plt.grid(
    axis="y",
    alpha=0.3
)

plt.tight_layout()


# Salva o gráfico.

plt.savefig(
    PASTA_GRAFICOS / "03_medias_g1_g2_g3.png",
    dpi=300
)


plt.show()


# ============================================================
# 12. GRÁFICO 4 - FALTAS X NOTA FINAL
# ============================================================

plt.figure(figsize=(10, 6))


# scatter() cria um gráfico de dispersão.
#
# Cada ponto representa um estudante.
#
# Eixo X = quantidade de faltas.
#
# Eixo Y = nota final G3.

plt.scatter(
    df["absences"],
    notas_finais,
    color="purple",
    alpha=0.6,
    edgecolors="black"
)


plt.title(
    "Relação entre Número de Faltas e Nota Final"
)

plt.xlabel("Número de Faltas")

plt.ylabel("Nota Final (G3)")


plt.grid(alpha=0.3)

plt.tight_layout()


# Salva o gráfico.

plt.savefig(
    PASTA_GRAFICOS / "04_faltas_g3.png",
    dpi=300
)


plt.show()


# ============================================================
# 13. FINALIZAÇÃO
# ============================================================

print("\n" + "=" * 60)
print("ANÁLISE CONCLUÍDA COM SUCESSO!")
print("=" * 60)