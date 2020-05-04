from flask import Flask, render_template
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import pandas as pd

def plot_num_test(name: str, measurements: list, dates: list, fp: str): 
    '''
    use this function to plot dynamics 
    of numerical tests 
    e.g.: pain level, time walking etc

    params: 
    name - name of test e.g. "Уровень боли"
    measurements - list of results of a test
    dates - list of dates when results were obtained

    resulted plot is written to file with name fp(filepath)
    '''
    assert len(measurements) == len(dates)
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=pd.Series(dates, name='Дата'), 
            y=pd.Series(measurements, name=name),
            mode='lines+markers',
            name=name,
            text=name,
            line={'color': 'mediumblue'},
            textfont={'family': 'Raleway'}
            )
        )

    fig.write_html(fp)

measurements = [1, 3, 2, 7, 9, 5, 6, 7, 1, 3, 7, 5, 6, 7 ]
dates = [
    '10-03-2003', '11-03-2003', '12-03-2003', '13-03-2003', '14-03-2003', '15-03-2003', '16-03-2003', '17-03-2003', '18-03-2003', '19-03-2003', '20-03-2003', '21-03-2003', '22-03-2003', '23-03-2003',
    ]
dates = [datetime.strptime(d, '%d-%m-%Y') for d in dates]
plot_num_test(
    'Уровень боли', measurements, 
    dates, 'templates/user/pain_level.html'
)

measurements = [30, 15, 17, 26, 38, 32, 20][::-1]
dates = [
    '10-03-2003', '11-03-2003', '12-03-2003', '13-03-2003', '14-03-2003', '15-03-2003', '16-03-2003'
    ]
dates = [datetime.strptime(d, '%d-%m-%Y') for d in dates]
plot_num_test(
    'Не уровень боли', measurements, 
    dates, 'templates/user/not_pain_level.html'
)


app = Flask(__name__)
@app.route('/')
def main():
    return render_template('index.html')

app.run(debug=True)