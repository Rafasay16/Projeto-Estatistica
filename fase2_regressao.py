"""Projeto de Estatística - Fase 2: Análise Bivariada e Regressão Linear

Base de dados: student-mat.csv (UCI Machine Learning Repository)
Variáveis analisadas:
  - X: G1 (Nota do 1º Período)
  - Y: G3 (Nota Final em Matemática)
"""

import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# -------------------------------------------------------------
# 1. Carregamento dos dados
# -------------------------------------------------------------
caminho_dados = os.path.join("dados", "student-mat.csv")

if not os.path.exists(caminho_dados):
    raise FileNotFoundError(f"Arquivo não encontrado em: {caminho_dados}")

# O arquivo student-mat.csv original utiliza ';' como separador
df = pd.read_csv(caminho_dados, sep=";")

# Seleção das variáveis quantitativas
x = df["G1"].to_numpy(dtype=float)
y = df["G3"].to_numpy(dtype=float)
n = len(x)

# -------------------------------------------------------------
# 2. Cálculos Estatísticos (Fórmulas Manuais / Teóricas)
# -------------------------------------------------------------
# Médias
media_x = np.mean(x)
media_y = np.mean(y)

# Desvios e Variâncias Amostrais (graus de liberdade n - 1)
desvios_x = x - media_x
desvios_y = y - media_y

var_x = np.sum(desvios_x**2) / (n - 1)
var_y = np.sum(desvios_y**2) / (n - 1)

std_x = np.sqrt(var_x)
std_y = np.sqrt(var_y)

# Covariância Amostral Cov(X, Y)
cov_xy = np.sum(desvios_x * desvios_y) / (n - 1)

# Coeficiente de Correlação Linear de Pearson (r)
r = cov_xy / (std_x * std_y)

# Coeficientes da Regressão Linear Simples por Mínimos Quadrados (OLS): y = a*x + b
# a (inclinação / coeficiente angular) = Cov(X, Y) / Var(X)
a = np.sum(desvios_x * desvios_y) / np.sum(desvios_x**2)
# b (intercepto / coeficiente linear) = y_medio - a * x_medio
b = media_y - a * media_x

# Coeficiente de Determinação (R²)
r2 = r**2

# -------------------------------------------------------------
# 3. Exibição dos Resultados no Terminal
# -------------------------------------------------------------
print("=" * 60)
print("     FASE 2 - ANÁLISE BIVARIADA E REGRESSÃO LINEAR")
print("=" * 60)
print(f"Total de registros analisados (N): {n}")
print(f"Média de G1 (X): {media_x:.2f} (DP: {std_x:.2f})")
print(f"Média de G3 (Y): {media_y:.2f} (DP: {std_y:.2f})")
print("-" * 60)
print(f"Covariância Amostral:       {cov_xy:.4f}")
print(f"Correlação de Pearson (r):  {r:.4f} (Forte correlação positiva)")
print(f"Coeficiente R²:             {r2:.4f} ({r2 * 100:.2f}% da variância explicada)")
print("-" * 60)
sinal_b = "+" if b >= 0 else "-"
print(f"Equação da Reta Estimada:  G3 = {a:.2f} * G1 {sinal_b} {abs(b):.2f}")
print("=" * 60)

# -------------------------------------------------------------
# 4. Geração e Salvamento do Gráfico
# -------------------------------------------------------------
os.makedirs("graficos", exist_ok=True)

plt.figure(figsize=(9, 6), dpi=300)

# Scatter plot dos dados reais com leve transparência para visualizar sobreposições
plt.scatter(
    x,
    y,
    color="#2563eb",
    alpha=0.45,
    edgecolors="none",
    s=40,
    label=f"Alunos (N = {n})",
)

# Reta de Regressão Linear
x_linha = np.linspace(x.min(), x.max(), 200)
y_linha = a * x_linha + b
plt.plot(
    x_linha,
    y_linha,
    color="#dc2626",
    linewidth=2.5,
    label=f"Reta: G3 = {a:.2f}·G1 {sinal_b} {abs(b):.2f}",
)

# Linhas pontilhadas do centroide amostral (médias de X e Y)
plt.axvline(
    x=media_x,
    color="#64748b",
    linestyle="--",
    linewidth=1.2,
    alpha=0.7,
    label=f"Média G1 ({media_x:.2f})",
)
plt.axhline(
    y=media_y,
    color="#64748b",
    linestyle="--",
    linewidth=1.2,
    alpha=0.7,
    label=f"Média G3 ({media_y:.2f})",
)

# Ponto de interseção das médias (o centro de gravidade da distribuição)
plt.scatter(
    [media_x],
    [media_y],
    color="#e11d48",
    s=90,
    zorder=5,
    edgecolors="#ffffff",
    linewidth=1.5,
    label=f"Centroide Amostral ({media_x:.1f}, {media_y:.1f})",
)

# Configurações visuais do gráfico
plt.title(
    "Distribuição Conjunta e Regressão Linear Simples: G1 vs G3",
    fontsize=13,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Nota do 1º Período (G1) [Escala 0 a 20]", fontsize=11)
plt.ylabel("Nota Final em Matemática (G3) [Escala 0 a 20]", fontsize=11)
plt.xlim(-0.5, 20.5)
plt.ylim(-0.5, 20.5)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper left", framealpha=0.9)

# Salvar o arquivo na pasta de gráficos
caminho_saida = os.path.join("graficos", "05_regressao_linear_g1_g3.png")
plt.tight_layout()
plt.savefig(caminho_saida, dpi=300)
plt.close()

print(f"\nGráfico gerado com sucesso: {caminho_saida}")
