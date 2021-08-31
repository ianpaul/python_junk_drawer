import pandas as pd
df = pd.read_csv("nfl-2021.csv")
covered_stadiums = ["Allegiant Stadium", "AT&T Stadium", "Caesars Superdome", "Ford Field", "Lucas Oil Stadium", "Mercedes-Benz Stadium", "NRG Stadium", "SoFi Stadium", "State Farm Stadium", "U.S Bank Stadium"]

df["Counts"] = [1 if ele in covered_stadiums else 0 for ele in df["Location"]]

df = df.rename(columns={'Away Team': 'Away', 'Home Team': 'Home'})
out = (df['Counts'].isin([1]).groupby(df['Home']).sum().astype(int).reset_index())
out2 = (df['Counts'].isin([1]).groupby(df['Away']).sum().astype(int).reset_index())

new_df = pd.merge(out, out2, left_on=['Home'], right_on=['Away'], how= 'left')
new_df['Roofs'] = new_df['Counts_x'] + new_df['Counts_y']
result = new_df.drop(['Counts_x', 'Counts_y', 'Away'], axis=1)

final = result.rename(columns={'Home': 'Team'})
print(final.sort_values(['Roofs'], ascending=False))