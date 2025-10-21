import pandas as pd

df = pd.read_csv("Book1.csv")

# Melt
df_long = df.melt(
    id_vars=["Category"],
    var_name="Age group",
    value_name="Value"
)

df_long.to_csv("alcohol_clean.csv", index=False)
