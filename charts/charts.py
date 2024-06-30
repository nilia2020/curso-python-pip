# Traigo la librería matpolib
import matplotlib.pyplot as plt


# Función que genera un gráfico de barras y lo guarda en un archivo png
def generate_bar_chart():
    labels = ["A", "B", "C"]
    values = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.bar(x=labels, height=values)
    plt.savefig("bars.png")
    print("gráficos generados bars.png")
    plt.close()


# Función que genera un gráfico de torta y lo guarda en un archivo png
def generate_pie_chart():
    labels = ["A", "B", "C"]
    values = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig("pie.png")
    print("gráficos generados pie.png")
    plt.close()
