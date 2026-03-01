import os
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px


def load_data(file_path: str) -> pd.DataFrame:
    """
    Загружает CSV файл и возвращает DataFrame.
    """
    try:
        data_frame = pd.read_csv(file_path)

        # Очистка названий колонок
        data_frame.columns = (
            data_frame.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        return data_frame

    except Exception as error:
        print(f"Ошибка загрузки данных: {error}")
        raise


# Автоматический путь к файлу
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "StudentsPerformance.csv")

data_frame = load_data(FILE_PATH)

AVAILABLE_COLUMNS = ["math_score", "reading_score", "writing_score"]

app = dash.Dash(__name__)

app.layout = html.Div([

    # Заголовок страницы
    html.H1("Students Performance Interactive Dashboard"),

    html.Hr(),

    # Dropdown
    html.Label("Выберите предмет:"),
    dcc.Dropdown(
        id="score_selector",
        options=[
            {"label": "Math Score", "value": "math_score"},
            {"label": "Reading Score", "value": "reading_score"},
            {"label": "Writing Score", "value": "writing_score"},
        ],
        value="math_score"
    ),

    html.Br(),

    # Radio Buttons
    html.Label("Выберите тип графика:"),
    dcc.RadioItems(
        id="chart_type",
        options=[
            {"label": "Histogram", "value": "histogram"},
            {"label": "Boxplot", "value": "box"},
            {"label": "Bar (Average)", "value": "bar"},
        ],
        value="histogram",
        inline=True
    ),

    html.Br(),

    # Slider
    html.Label("Количество интервалов (bins) для Histogram:"),
    dcc.Slider(
        id="bins_slider",
        min=5,
        max=30,
        step=1,
        value=10,
        marks={i: str(i) for i in range(5, 31, 5)}
    ),

    html.Br(),

    # График
    dcc.Graph(id="score_graph")
])


@app.callback(
    Output("score_graph", "figure"),
    [
        Input("score_selector", "value"),
        Input("chart_type", "value"),
        Input("bins_slider", "value")
    ]
)
def update_graph(selected_score: str, chart_type: str, bins_value: int):
    """
    Обновляет график в зависимости от выбранных параметров.
    """
    try:

        if chart_type == "histogram":
            figure = px.histogram(
                data_frame,
                x=selected_score,
                nbins=bins_value,
                title=f"Histogram of {selected_score}"
            )

        elif chart_type == "box":
            figure = px.box(
                data_frame,
                y=selected_score,
                title=f"Boxplot of {selected_score}"
            )

        elif chart_type == "bar":
            averages = data_frame[AVAILABLE_COLUMNS].mean().reset_index()
            averages.columns = ["subject", "average_score"]

            figure = px.bar(
                averages,
                x="subject",
                y="average_score",
                title="Average Score by Subject"
            )

        else:
            figure = px.histogram(data_frame, x="math_score")

        return figure

    except Exception as error:
        print(f"Ошибка обновления графика: {error}")
        return px.histogram(data_frame, x="math_score")


if __name__ == "__main__":
    app.run(debug=True)
