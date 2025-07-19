import pandas as pd
from logger_setup import setup_logger


def filter_data(df:pd.DataFrame):

    logger = setup_logger()
    # filter data based on threshold
    columns_of_interest = ['Light Intensity (PAR)', 'LEF', 'Phi2', 'qL', 'PhiNPQ', 'NPQt', 'PhiNO', 'Series'] # define columns of interest
    plot_columns = [col for col in columns_of_interest if col != 'Series']
    
    df_filtered = df.loc[df[plot_columns].ge(0.005).all(axis=1), columns_of_interest]
    logger.info(f'The original data is of shape {df.shape} and the filtered data is of shape {df_filtered.shape}')

    # standardize the treatment labels
    df_filtered['Series'] = df_filtered['Series'].replace({
        'control': 'Control', 
        'shade': 'ND',
        'grey': 'ND', 
        'Grey': 'ND',
        'orange': 'Orange', 
        'blue': 'Blue'
    })
    filtered_treatments = list(df_filtered['Series'].unique())
    logger.info(f'The unique treatments are {filtered_treatments}')
    
    return df_filtered, plot_columns
