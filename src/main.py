
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import logging
from logger_setup import setup_logger
import seaborn as sns



def main():

    # Initialize logger
    logger = setup_logger() # Setup logging

    # load data
    file_path = 'data/photosynQ_MallingAce.csv'
    df = pd.read_csv(file_path) 

    # Filter data
    filter_cols = ['qL', 'Phi2', 'PhiNO', 'PhiNPQ', 'NPQt', 'SPAD', 'Light Intensity (PAR)', 'LEF']

    # Create mask for values >= 0.1 in specified columns
    data_mask = df[filter_cols].ge(0.005).all(axis=1)
    control_mask = df['Series'] == 'Control'
     
    all_relavant_cols = ['Light Intensity (PAR)', 'LEF', 'Phi2', 'qL', 'PhiNPQ', 'NPQt', 'PhiNO','PS1 Active Centers', 'PS1 Open Centers', 'PS1 Over Reduced Centers', 'SPAD']
    df_filtered_all_cols = df.loc[data_mask & control_mask, all_relavant_cols]
    
    selected_cols = ['Light Intensity (PAR)', 'LEF', 'Phi2', 'qL', 'PhiNPQ', 'NPQt', 'PhiNO']
    df_filtered_selected_cols = df.loc[data_mask & control_mask, selected_cols]

    name_map = {
    'Light Intensity (PAR)': 'PAR',
    'PS1 Active Centers': 'PS1-Active',
    'PS1 Open Centers': 'PS1-Open',
    'PS1 Over Reduced Centers': 'PS1-Reduced'
    # Add other mappings as needed
    }   

    df_filtered_all_cols = df_filtered_all_cols[all_relavant_cols].rename(columns=name_map)
    df_filtered_selected_cols = df_filtered_selected_cols[selected_cols].rename(columns=name_map)
   
    corr_matrix_all_cols = df_filtered_all_cols.corr()
    corr_matrix_selected_cols = df_filtered_selected_cols.corr()

    for corr_matrix, matrix_type in [(corr_matrix_all_cols, 'full'), 
                                    (corr_matrix_selected_cols, 'selected')]:
       
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix,
                    annot=True,  # Show correlation values
                    cmap='RdBu_r',  # Red for positive, blue for negative
                    vmin=-1, vmax=1,  # Fix the range from -1 to 1
                    center=0,  # Center the colormap at 0
                    fmt='.2f')  # Round correlation values to 2 decimal places
        # Move x-axis labels to top
        plt.tick_params(top=True, bottom=False,
                        labeltop=True, labelbottom=False)

        # Rotate the top labels
        plt.xticks(rotation=45, ha='left')
        plt.yticks(rotation=0)
        plt.tight_layout()
        save_dir = Path('results/correlation') / Path(file_path).stem 
        save_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f'Saving correlation heatmap to {save_dir}')
    
        plt.savefig(save_dir/f'{matrix_type}_heatmap.png', dpi=300, bbox_inches='tight')
        plt.close()
        logger.info(f'Saved Correlation matrix for all {matrix_type} columns')

    # Create pairplot
    for df, data_type in [(df_filtered_all_cols, 'full'), 
                        (df_filtered_selected_cols, 'selected')]:
        
        plt.figure(figsize=(8, 6))

        g = sns.pairplot(df,
                        plot_kws={'s': 20},
                        diag_kws={'bins': 20},
                        height=2.5,
                        aspect=1)
        
        plt.rc('font', size=14)
        plt.rc('legend', fontsize=12)    # legend fontsize and weight

        save_dir = Path('results/correlation') / Path(file_path).stem 
        save_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f'Saving pairplots to {save_dir}')
    
        g.savefig(save_dir/f'{data_type}pairplot.png', dpi=300, bbox_inches='tight')
        plt.close()
        logger.info(f'Saved pairplots for all {data_type} columns')


if __name__ == "__main__":
    main() 

