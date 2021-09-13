# Clasificador_de_Residuos_Solidos

Dataset de kaggle:
https://www.kaggle.com/asdasdasasdas/garbage-classification

Consiste en un problema de clasificación entre 6 tipos de residuos sólidos:

- cartón
- vidrio
- metal
- papel
- plastico
- ordinarios

Para aproximar una solución a este problema, se construye un clasificador de residuos sólidos con Tensorflow y Keras.

Esto se logra mediante un modelo de **red neuronal convolucional** propio construido y optimizado mediante modificación de hiperparámetros, luego se aplica transfer learning mediante dos modelos ampliamente conocidos y usados en el campo de la visión por computador, estos son el **VGG16** y el **inception + Resnet V2**.

Al final, se evalúa el desempeño mediante diferentes métricas como la matriz de confusión, la precisión, el recall y el F1 score.
