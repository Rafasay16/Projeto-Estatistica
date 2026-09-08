from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
PASTA_GRAFICOS = BASE_DIR / "graficos"
PASTA_GRAFICOS.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(
    BASE_DIR / "dados" / "student-mat.csv",
    sep=";"
)

print("=" * 60)
print("INFORMAÇÕES DO BANCO DE DADOS")
print("=" * 60)

print(f"Quantidade de registros: {df.shape[0]}")
print(f"Quantidade de variáveis: {df.shape[1]}")

print("\nPrimeiros 5 registros:")
print(df.head())

print("\n" + "=" * 60)
print("VERIFICAÇÃO DE DADOS AUSENTES")
print("=" * 60)

dados_ausentes = df.isnull().sum()
print(dados_ausentes)

if dados_ausentes.sum() == 0:
    print("\nNão existem dados ausentes no banco.")
else:
    print("\nExistem dados ausentes no banco.")

notas_finais = df["G3"]

media = notas_finais.mean()
mediana = notas_finais.median()
moda = notas_finais.mode()

print("\n" + "=" * 60)
print("MEDIDAS DE POSIÇÃO - NOTA FINAL (G3)")
print("=" * 60)

print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda: {moda.tolist()}")

desvio_padrao = notas_finais.std()
coeficiente_variacao = (desvio_padrao / media) * 100

print("\n" + "=" * 60)
print("MEDIDAS DE DISPERSÃO - NOTA FINAL (G3)")
print("=" * 60)

print(f"Desvio padrão: {desvio_padrao:.2f}")
print(f"Coeficiente de variação: {coeficiente_variacao:.2f}%")

estatisticas = notas_finais.describe()

print("\n" + "=" * 60)
print("ESTATÍSTICAS DESCRITIVAS - NOTA FINAL (G3)")
print("=" * 60)

print(estatisticas)

plt.figure(figsize=(10, 6))
plt.hist(
    notas_finais,
    bins=11,
    color="steelblue",
    edgecolor="black",
    alpha=0.8
)
plt.axvline(
    media,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Média = {media:.2f}"
)
plt.axvline(
    mediana,
    color="green",
    linestyle="--",
    linewidth=2,
    label=f"Mediana = {mediana:.2f}"
)
plt.title("Distribuição das Notas Finais - Matemática")
plt.xlabel("Nota Final (G3)")
plt.ylabel("Quantidade de Alunos")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig(
    PASTA_GRAFICOS / "01_histograma_g3.png",
    dpi=300
)
plt.show()

plt.figure(figsize=(8, 6))
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
plt.savefig(
    PASTA_GRAFICOS / "02_boxplot_g3.png",
    dpi=300
)
plt.show()

medias = df[["G1", "G2", "G3"]].mean()

plt.figure(figsize=(8, 6))
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
plt.ylim(0, 20)

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
plt.savefig(
    PASTA_GRAFICOS / "03_medias_g1_g2_g3.png",
    dpi=300
)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(
    df["absences"],
    notas_finais,
    color="purple",
    alpha=0.6,
    edgecolors="black"
)
plt.title("Relação entre Número de Faltas e Nota Final")
plt.xlabel("Número de Faltas")
plt.ylabel("Nota Final (G3)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(
    PASTA_GRAFICOS / "04_faltas_g3.png",
    dpi=300
)
plt.show()

print("\n" + "=" * 60)
print("ANÁLISE CONCLUÍDA COM SUCESSO!")
print("=" * 60)