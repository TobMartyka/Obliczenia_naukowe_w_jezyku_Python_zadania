import pandas as pd

elements_data = {
    'Name': ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron',
             'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon'],
    'Symbol': ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne'],
    'Weight': [1.008, 4.0026, 6.94, 9.0122, 10.81, 12.011, 14.007, 15.999, 18.998, 20.180]
}

periodic_table_df = pd.DataFrame(data=elements_data, index=range(1, 11))

print(periodic_table_df)
