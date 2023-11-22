
## Crea un grafico con subgraficos para cada histograma con el limite de columnas indicado 

import seaborn as sns
import matplotlib.pyplot as plt
import math

def plot_histograms(dataframe, max_columns=3):
    # Obtén la lista de columnas categóricas
    categorical_columns = dataframe.select_dtypes(include=['object']).columns.tolist()

    # Calcula el número total de variables categóricas y el número de filas y columnas deseadas
    num_categorical = len(categorical_columns)
    num_cols = min(num_categorical, max_columns)
    num_rows = math.ceil(num_categorical / num_cols)

    # Configura el tamaño del gráfico
    plt.figure(figsize=(5 * max_columns, 5 * num_rows))

    # Itera sobre las columnas categóricas y crea un histograma para cada una
    for i, column in enumerate(categorical_columns, start=1):
        plt.subplot(num_rows, num_cols, i)
        sns.histplot(data=dataframe, x=column, kde=True)  # Puedes ajustar las opciones según tu preferencia
        plt.title(f'Histograma de {column}')
        plt.xlabel(column)
        plt.ylabel('Frecuencia')

    # Ajusta el espaciado entre subgráficos
    plt.tight_layout()

    # Muestra el gráfico
    plt.show()

# Ejemplo de uso
# Supongamos que tienes un DataFrame llamado 'df' con las variables categóricas
# Puedes llamar a la función de la siguiente manera:
# plot_histograms(df, max_columns=4)
