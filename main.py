import pandas as pd
import matplotlib.pyplot as plt
import os

# Carrega o dataset
df = pd.read_csv('./data/dataset_ecommerce.csv')

# Contador para nomear os gráficos
contador_grafico = 1

# --------------------------------------------------
# Gráfico 1: Histograma de Preço Unitário
plt.figure(figsize=(10, 6))
plt.hist(df['Preço_Unitário'], bins=30, color='skyblue', edgecolor='black')
plt.title('Distribuição de Preços Unitários', fontsize=14)
plt.xlabel('Preço Unitário (R$)', fontsize=12)
plt.ylabel('Frequência', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig(os.path.join('images', f'grafico{contador_grafico}.png'))  # Salva na pasta
contador_grafico += 1  # Incrementa o contador
plt.show()
plt.close()

# --------------------------------------------------
# Gráfico 2: Contagem por Categoria
plt.figure(figsize=(10, 6))
df['Categoria'].value_counts().plot(kind='bar', color='orange', edgecolor='black')
plt.title('Vendas por Categoria', fontsize=14)
plt.xlabel('Categoria', fontsize=12)
plt.ylabel('Contagem', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig(os.path.join('images', f'grafico{contador_grafico}.png'))
contador_grafico += 1
plt.show()
plt.close()

# --------------------------------------------------
# Gráfico 3: Relação Preço vs Quantidade
plt.figure(figsize=(10, 6))
plt.scatter(df['Preço_Unitário'], df['Quantidade_Vendida'], alpha=0.5, color='purple')
plt.title('Relação: Preço vs Quantidade Vendida', fontsize=14)
plt.xlabel('Preço Unitário (R$)', fontsize=12)
plt.ylabel('Quantidade Vendida', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig(os.path.join('images', f'grafico{contador_grafico}.png'))
contador_grafico += 1
plt.show()
plt.close()

# --------------------------------------------------
# Gráfico 4: Boxplot de Preços por Categoria
plt.figure(figsize=(10, 6))
df.boxplot(column='Preço_Unitário', by='Categoria', patch_artist=True)
plt.title('Variação de Preços por Categoria', fontsize=14)
plt.suptitle('')
plt.xlabel('Categoria', fontsize=12)
plt.ylabel('Preço Unitário (R$)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig(os.path.join('images', f'grafico{contador_grafico}.png'))
contador_grafico += 1
plt.show()
plt.close()

# --------------------------------------------------
# Gráfico 5: Mapa de Correlação
numeric_cols = ['Preço_Unitário', 'Quantidade_Vendida', 'Nota_Avaliação', 'Receita_Total']
corr = df[numeric_cols].corr()

plt.figure(figsize=(10, 6))
plt.imshow(corr, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.title('Correlações entre Variáveis', fontsize=14)
plt.xticks(range(len(corr)), numeric_cols, rotation=45)
plt.yticks(range(len(corr)), numeric_cols)
plt.savefig(os.path.join('images', f'grafico{contador_grafico}.png'))  # Último gráfico
plt.show()
plt.close()