from pipeline import extract_json
from pipeline import concat_json
from pipeline import calculate_total_sales_col
from pipeline import load_df


if __name__ == "__main__":
    path = "C:/Users/JHS/Documents/repos/public_knwoledge_base/python/bootcamp_jornada_dados/aula08/data"
    path_output = "C:/Users/JHS/Documents/repos/public_knwoledge_base/python/bootcamp_jornada_dados/aula08/data/"
    df_list = extract_json(path)
    df = concat_json(df_list)
    df = calculate_total_sales_col(df)
    print(load_df(df, path_output, ["parquet"]))
