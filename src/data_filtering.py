import pandas as pd
from logger_setup import setup_logger

def filter_data(df:pd.DataFrame):
    """
    Filters and cleans PhotosynQ data for analysis.

    This function:
    1. Filters out rows where any of the measurement columns are below a threshold (0.005).
    2. Keeps only a predefined set of columns relevant to photosynthesis.
    3. Standardises the treatment labels in the 'Series' column (e.g., maps 'shade', 'grey', etc. to 'ND').
    4. Logs the original and filtered data shapes, as well as the unique treatment types.

    Parameters:
    ----------
    df : pd.DataFrame
        The original raw PhotosynQ dataset.

    Returns:
    -------
    df_filtered : pd.DataFrame
        The filtered and cleaned dataset, retaining only valid rows and standardised treatment labels.

    plot_columns : list
        The list of measurement columns (excluding the 'Series' label) used for plotting and filtering.
    """
    logger = setup_logger()
    # Define columns of interest
    columns_of_interest = ['Light Intensity (PAR)', 'LEF', 'Phi2', 'qL', 'PhiNPQ', 'NPQt', 'PhiNO', 'Series'] # define columns of interest
    plot_columns = [col for col in columns_of_interest if col != 'Series']

    # Filter rows where all measurement values are >= 0.005
    df_filtered = df.loc[df[plot_columns].ge(0.005).all(axis=1), columns_of_interest]
    logger.info(f'The original data is of shape {df.shape} and the filtered data is of shape {df_filtered.shape}')

    
    return df_filtered, plot_columns
