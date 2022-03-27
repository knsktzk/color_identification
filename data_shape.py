import numpy as np
import pandas as pd

color_dic = { "black":0, "red":1, "green":2, "blue":3, "blueen":4, "purple":5,}
color_dic_key = color_dic.keys()

def make_data(color):

    df_405 = pd.read_csv("./test_data/{}_405.csv".format(color))
    df_450 = pd.read_csv("./test_data/{}_450.csv".format(color))
    df_620 = pd.read_csv("./test_data/{}_620.csv".format(color))

    data = [(list(df_405.loc[ i ,:])[1:]) for i in range(8) ]
    list_405 = [a_value for a_list in data for a_value in a_list]


    data = [(list(df_450.loc[ i ,:])[1:]) for i in range(8) ]
    list_450 = [a_value for a_list in data for a_value in a_list]


    data = [(list(df_620.loc[ i ,:])[1:]) for i in range(8) ]
    list_620 = [a_value for a_list in data for a_value in a_list]
        
    a_color_data = [ [list_405[i], list_450[i], list_620[i], color_dic[color]] for i in range( len(list_405) ) ]
    
    return a_color_data

dataset_ls = [a_data for color in color_dic_key for a_data in make_data(color)]
df = pd.DataFrame(dataset_ls, columns=[405, 450, 620, "color_tag"])
df.to_csv("./test_dataset.csv", index=False)