## Detecção de Câncer de Mama com Redes Neurais MLP

Este repositório contém a implementação em Python de um modelo de Rede Neural Artificial Multicamadas (MLP) para a detecção de câncer de mama, replicando o estudo apresentado no artigo "[## Detecção de Câncer de Mama com Redes Neurais MLP

Este repositório contém a implementação em Python de um modelo de Rede Neural Artificial Multicamadas (MLP) para a detecção de câncer de mama, replicando o estudo apresentado no artigo "[Título do Artigo]".

**Objetivo:**

O objetivo deste projeto é replicar os resultados do estudo utilizando a base de dados WDBC e avaliar a performance do modelo MLP na classificação de tumores como benignos ou malignos.

**Base de Dados:**

A base de dados utilizada é a *Breast Cancer Wisconsin (Diagnostic)* (WDBC), disponível no repositório de Machine Learning da UCI: [https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)).

A base contém 569 instâncias, cada uma com 32 atributos (features) descrevendo características de núcleos celulares de imagens digitalizadas de biópsias de câncer de mama. A variável alvo (target) é o diagnóstico, classificado como "benigno" ou "maligno".

**Implementação:**

O código Python utiliza as seguintes bibliotecas:

* `pandas`: para manipulação e análise de dados.
* `numpy`: para operações matemáticas e manipulação de arrays.
* `ucimlrepo`: para importar a base de dados WDBC diretamente do repositório da UCI.
* `sklearn`: para pré-processamento dos dados, criação e avaliação do modelo MLP.
* `seaborn` e `matplotlib`: para visualização dos resultados.

**Etapas da Implementação:**

1. **Importação das bibliotecas:** Importa as bibliotecas necessárias para o projeto.
2. **Carregamento dos dados:** Utiliza o `ucimlrepo` para carregar a base de dados WDBC.
3. **Pré-processamento dos dados:**
    * Converte a variável alvo para numérica (0 para benigno e 1 para maligno).
    * Padroniza os dados numéricos utilizando `StandardScaler` para evitar problemas de escala.
    * Divide os dados em conjuntos de treino e teste, utilizando `train_test_split` com estratificação para garantir a proporção das classes em ambos os conjuntos.
4. **Criação e treinamento do modelo MLP:**
    * Cria um modelo `MLPClassifier` com duas camadas ocultas (100 e 50 neurônios), função de ativação `tanh` e outros parâmetros especificados no estudo.
    * Treina o modelo utilizando os dados de treino.
5. **Avaliação do modelo:**
    * Realiza previsões com os dados de teste.
    * Calcula métricas de desempenho: acurácia, matriz de confusão, precisão, recall e F1-score.
    * Imprime os resultados da avaliação.
6. **Visualização da matriz de confusão:** Utiliza `seaborn` para criar um mapa de calor da matriz de confusão.

**Como Executar o Código:**

1. Instale as bibliotecas necessárias: `pip install ucimlrepo pandas numpy scikit-learn seaborn matplotlib`
2. Copie o código Python para um arquivo (ex.: `cancer_detection.py`).
3. Execute o código: `python cancer_detection.py`

**Resultados:**

O código irá imprimir a acurácia do modelo, a matriz de confusão e o relatório de classificação. Além disso, será exibido um gráfico da matriz de confusão.

**Próximos Passos:**

* Experimentar outras configurações da MLP (número de camadas, neurônios, função de ativação, etc.) para tentar melhorar o desempenho do modelo.
* Comparar os resultados com outros modelos de Machine Learning para avaliar a eficácia da MLP para este problema.
* Implementar técnicas de otimização de hiperparâmetros para encontrar a melhor configuração para a MLP.

**Contribuições:**

Contribuições para este projeto são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para sugerir melhorias, correções ou novas funcionalidades. 

Espero que esta documentação seja útil para entender e replicar o projeto! 😄 
]".

**Objetivo:**

O objetivo deste projeto é replicar os resultados do estudo utilizando a base de dados WDBC e avaliar a performance do modelo MLP na classificação de tumores como benignos ou malignos.

**Base de Dados:**

A base de dados utilizada é a *Breast Cancer Wisconsin (Diagnostic)* (WDBC), disponível no repositório de Machine Learning da UCI: [https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)).

A base contém 569 instâncias, cada uma com 32 atributos (features) descrevendo características de núcleos celulares de imagens digitalizadas de biópsias de câncer de mama. A variável alvo (target) é o diagnóstico, classificado como "benigno" ou "maligno".

**Implementação:**

O código Python utiliza as seguintes bibliotecas:

* `pandas`: para manipulação e análise de dados.
* `numpy`: para operações matemáticas e manipulação de arrays.
* `ucimlrepo`: para importar a base de dados WDBC diretamente do repositório da UCI.
* `sklearn`: para pré-processamento dos dados, criação e avaliação do modelo MLP.
* `seaborn` e `matplotlib`: para visualização dos resultados.

**Etapas da Implementação:**

1. **Importação das bibliotecas:** Importa as bibliotecas necessárias para o projeto.
2. **Carregamento dos dados:** Utiliza o `ucimlrepo` para carregar a base de dados WDBC.
3. **Pré-processamento dos dados:**
    * Converte a variável alvo para numérica (0 para benigno e 1 para maligno).
    * Padroniza os dados numéricos utilizando `StandardScaler` para evitar problemas de escala.
    * Divide os dados em conjuntos de treino e teste, utilizando `train_test_split` com estratificação para garantir a proporção das classes em ambos os conjuntos.
4. **Criação e treinamento do modelo MLP:**
    * Cria um modelo `MLPClassifier` com duas camadas ocultas (100 e 50 neurônios), função de ativação `tanh` e outros parâmetros especificados no estudo.
    * Treina o modelo utilizando os dados de treino.
5. **Avaliação do modelo:**
    * Realiza previsões com os dados de teste.
    * Calcula métricas de desempenho: acurácia, matriz de confusão, precisão, recall e F1-score.
    * Imprime os resultados da avaliação.
6. **Visualização da matriz de confusão:** Utiliza `seaborn` para criar um mapa de calor da matriz de confusão.

**Como Executar o Código:**

1. Instale as bibliotecas necessárias: `pip install ucimlrepo pandas numpy scikit-learn seaborn matplotlib`
2. Copie o código Python para um arquivo (ex.: `cancer_detection.py`).
3. Execute o código: `python cancer_detection.py`

**Resultados:**

O código irá imprimir a acurácia do modelo, a matriz de confusão e o relatório de classificação. Além disso, será exibido um gráfico da matriz de confusão.

**Próximos Passos:**

* Experimentar outras configurações da MLP (número de camadas, neurônios, função de ativação, etc.) para tentar melhorar o desempenho do modelo.
* Comparar os resultados com outros modelos de Machine Learning para avaliar a eficácia da MLP para este problema.
* Implementar técnicas de otimização de hiperparâmetros para encontrar a melhor configuração para a MLP.

**Contribuições:**

Contribuições para este projeto são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para sugerir melhorias, correções ou novas funcionalidades. 

Espero que esta documentação seja útil para entender e replicar o projeto! 😄 
