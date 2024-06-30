import matplotlib.pyplot as plt


def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(x=labels, height=values)
    plt.savefig(f"./img/{name}.png")
    print("gráficos generados bar.png")
    plt.close()


def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis("equal")
    plt.savefig("pie.png")
    print("gráficos generados pie.png")
    plt.close()


if __name__ == "__main__":
    labels = ["a", "b", "c"]
    values = [10, 40, 800]
    # generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)
