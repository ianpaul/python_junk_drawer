import pandas as pd
import plotly.express as px

db = sqlite3.connect('vpn.db')

df = pd.read_sql_query('Select * from finalperf;', db)

fig = px.bar(df, x='brand', y='score')

fig.show()

