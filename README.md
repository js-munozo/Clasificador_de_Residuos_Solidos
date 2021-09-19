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

- Esto se logra con un modelo de **red neuronal convolucional** propio, construido y optimizado mediante modificación de hiperparámetros, obteniendo los siguientes resultados en la clasificación:

![alt text](https://raw.githubusercontent.com/js-munozo/Clasificador_de_Residuos_Solidos/main/imagenes/cnn.png)


luego se aplica transfer learning mediante tres modelos ampliamente conocidos y usados en el campo de la visión por computador obteniendo los siguientes resultados:

- **VGG16** 

![alt text](https://raw.githubusercontent.com/js-munozo/Clasificador_de_Residuos_Solidos/main/imagenes/vgg.png)

- **Resnet**

![alt text]()

- **Inception + Resnet**

![alt text]()


Al final, se evalúa el desempeño mediante diferentes métricas como la matriz de confusión, la precisión, el recall y el F1 score.

Se intenta mejorar las predicciones del modelo, haciendo uso de un webscrapper construido en Python y selenium para obtener imágenes directamente desde Google, sin embargo, dado que los datos del dataset son tomados mediante una misma cámara con resolución y dimensiones de imágen específicos, es extremadamente complicado encontrar imagenes similares en google, por esta razón no se agregan imágenes nuevas al dataset ya que puede generar mayor sesgo en el entrenamiento.
