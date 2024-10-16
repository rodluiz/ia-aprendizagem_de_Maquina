!pip install ucimlrepo # Instalando a biblioteca

import pandas as pd
import numpy as np  
from ucimlrepo import fetch_ucirepo
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Carregar a base de dados WDBC usando ucimlrepo
breast_cancer_wisconsin_diagnostic = fetch_ucirepo(id=17) 
X = breast_cancer_wisconsin_diagnostic.data.features 
y = breast_cancer_wisconsin_diagnostic.data.targets

# 2. Pré-processamento dos dados
y = np.where(y == 'malignant', 1, 0)  # Convertendo a coluna alvo para numérica
print(np.unique(y))  #  <-- Correção: Usando np.unique(y)

scaler = StandardScaler()
X = scaler.fit_transform(X)

# Correção: Usando stratify=y para garantir a estratificação na divisão dos dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# 3. Criação e Treinamento do modelo MLP
mlp = MLPClassifier(hidden_layer_sizes=(100, 50), activation='tanh', max_iter=2000, tol=1e-6, random_state=42)
mlp.fit(X_train, y_train)

# 4. Avaliação do Modelo
y_pred = mlp.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia: {accuracy:.4f}')
cm = confusion_matrix(y_test, y_pred)
print(f'Matriz de Confusão:\n{cm}')
print(f'Relatório de Classificação:\n{classification_report(y_test, y_pred)}')

# 5. Visualização da Matriz de Confusão
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Previsões')
plt.ylabel('Valores Reais')
plt.title('Matriz de Confusão')
plt.show()
