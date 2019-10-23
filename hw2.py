import pandas as pd

def read_url_create_dataframe(url): #url is a string
    data = pd.read_csv(url)
    return data

def test_create_dataframe(df, columns):
    df_col = list(df)
    if df_col == columns and df.shape[0] >= 10:
        for col in df_col:
            types = []
            for element in list(df[col]):
                types.append(type(element))
            if len(set(list(types))) == 1:
                countinue
            else:
                return False
        return True
    else:
        return False
