# Machine Learning Competition

Este proyecto se vincula a una competición de Kaggle desarrollada en el entorno educativo de [Ironhack](https://www.ironhack.com/en).


## Objetivo

El objetivo es construir un modelo de machine learning que sea capaz de predecir el precio de alojamientos de Airbnb con la mayor precisión posible.

## Workflow

Se parte de un dataset en el que se recoge una cantidad importante de datos acerca de alojamientos disponibles en Airbnb, concretamente de aquellos ubicados en Ámsterdam. En este dataset está disponible el precio real de los alojamientos (taget a predecir), junto con el resto de datos de cada uno de ellos. Este es el conjunto de datos que se utiliza para el entrenamiento y evaluación del ajuste de los diferentes modelos desarrollados.

Adicionalmente, se dispone de otro dataset en el que se incluyen los datos referentes a otros alojamientos, pero no el precio de cada uno de ellos. El precio de estos alojamientos es lo que deberemos predecir (aunque en realidad estos son solo el 50% de los registros sobre los que se evaluan los modelos en la competición, quedando el otro 50% en privado y reservado a los administradores de la competición hasta el momento en que se descubren los resultados finales, los cuales sí que se calculan sobre el 100% de los precios a predecir).

A partir de ahí, se sigue un proceso cuyas etapas principales son las siguientes:

1. **Análisis exploratorio de los datos (EDA**): en esta etapa se hace una exploración inicial de los datos y se lleva a cabo un análisis que nos permita conocer mejor el problema y la información que estamos manejando. 

2. **Limpieza inicial de los datos**: los datos en bruto requieren de una importante labor de limpieza y esto será algo fundamental para poder alcanzar unos resultados favorables a la hora de llevar a cabo nuestras predicciones.

3. **Transformación de los datos**: en esta etapa se lleva a cabo aquellas transformaciones que van más allá de la limpieza de los datos como tal y también será una etapa muy importante a la hora de mejorar la precisión de los modelos.

4. **Modelos de machine learning**: en esta etapa se construyen diferentes modelos de regresión y se compara su rendimiento para tratar de minimizar el error en las predicciones de los precios.

Debemos tener en cuenta que el proceso de construcción de los modelos debe ser completamente empírico, por lo que se trabaja bajo una metodología de prueba y error. Es cierto que el conocimiento experto del problema puede ayudar en estos casos, pero no debemos dar nada por sentado, sino probar diferentes opciones y ajustes para comprobar qué es lo que nos ofrece un mayor rendimiento. Así, a menudo no seguiremos estrictamente el orden anteriormente descrito y volveremos a etapas anteriores para hacer ajustes que puedan mejorar nuestros resultados.


### Tech Stack

- [Pandas](https://pandas.pydata.org/)

- [NumPy](https://numpy.org/)

- [RegEx](https://docs.python.org/3/library/re.html)

- [Matplotlib](https://matplotlib.org/)

- [Seaborn](https://seaborn.pydata.org/)

- [H2O](https://docs.h2o.ai/h2o/latest-stable/h2o-py/docs/intro.html)

- [XGBoost](https://xgboost.readthedocs.io/en/stable/#)

- [SciPy](https://scipy.org/)

- [Statsmodels](https://www.statsmodels.org/stable/index.html)

- [Scikit-learn](https://scikit-learn.org/stable/)




