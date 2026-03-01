import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_bar_chart(data_frame: pd.DataFrame) -> None:
    """
    Строит столбчатую диаграмму средних баллов.
    """
    try:
        columns = ["math score", "reading score", "writing score"]

        average_scores = data_frame[columns].mean()

        plt.figure()
        plt.bar(average_scores.index, average_scores.values)
        plt.title("Average Scores by Subject")
        plt.xlabel("Subject")
        plt.ylabel("Average Score")
        plt.show()

    except Exception as error:
        print(f"Ошибка построения bar chart: {error}")


def load_data(file_path: str) -> pd.DataFrame:
    """
    Загружает CSV файл и возвращает DataFrame.
    """
    try:
        data_frame = pd.read_csv(file_path)
        return data_frame
    except Exception as error:
        print(f"Ошибка при загрузке файла: {error}")
        raise


def plot_line_chart(data_frame: pd.DataFrame, column_name: str) -> None:
    """
    Строит линейный график по выбранному столбцу.
    """
    try:
        sorted_data = data_frame.sort_values(column_name)

        plt.figure()
        plt.plot(sorted_data[column_name])
        plt.title(f"Line Plot of {column_name}")
        plt.xlabel("Students")
        plt.ylabel(column_name)
        plt.show()

    except Exception as error:
        print(f"Ошибка построения линейного графика: {error}")


def plot_histogram(data_frame: pd.DataFrame, column_name: str) -> None:
    """
    Строит гистограмму распределения.
    """
    try:
        plt.figure()
        plt.hist(data_frame[column_name], bins=10)
        plt.title(f"Histogram of {column_name}")
        plt.xlabel(column_name)
        plt.ylabel("Frequency")
        plt.show()

    except Exception as error:
        print(f"Ошибка построения гистограммы: {error}")


def plot_scatter(data_frame: pd.DataFrame, column_x: str, column_y: str) -> None:
    """
    Строит диаграмму рассеяния.
    """
    try:
        plt.figure()
        plt.scatter(data_frame[column_x], data_frame[column_y])
        plt.title(f"{column_x} vs {column_y}")
        plt.xlabel(column_x)
        plt.ylabel(column_y)
        plt.show()

    except Exception as error:
        print(f"Ошибка построения scatter plot: {error}")


def plot_boxplot(data_frame: pd.DataFrame, columns: list) -> None:
    """
    Строит boxplot для нескольких столбцов.
    """
    try:
        plt.figure()
        sns.boxplot(data=data_frame[columns])
        plt.title("Boxplot of Scores")
        plt.show()
        plot_bar_chart(data)

    except Exception as error:
        print(f"Ошибка построения boxplot: {error}")


if __name__ == "__main__":
    FILE_PATH = "StudentsPerformance.csv"

    data = load_data(FILE_PATH)

    plot_line_chart(data, "math score")
    plot_histogram(data, "math score")
    plot_scatter(data, "math score", "reading score")
    plot_boxplot(data, ["math score", "reading score", "writing score"])