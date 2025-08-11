# PhotosynQ data analysis in Python
This repository provides a Python-based workflow for cleaning and analyzing PhotosynQ project data, with a focus on photosynthesis-related parameters.
## 🔧 Libraries Used
* `pandas` - for data manipulation and cleaning
* `matplotlib` - for basic plotting
* `seaborn` - for advanced visualisation
* `pathlib` - for file path handling
  
## FILTER DATA
1. **Obtain Data**
   
   Use your own dataset or download from existing public projects on the PhotosynQ platform:
   https://photosynq.org/search?utf8=%E2%9C%93&q=plants&filter=projects
2. **Clean Invalid Data**
   
   Remove data points that may be invalid due to system or device errors during measurements.
3. **Select Parameters of Interest.**
   
 ```python
  all_relavant_cols = [
    'Light Intensity (PAR)', 'LEF', 'Phi2', 'qL', 'PhiNPQ', 'NPQt',
    'PhiNO','PS1 Active Centers', 'PS1 Open Centers',
    'PS1 Over Reduced Centers', 'SPAD'
  ]
  ```
## PLOT DATA
1. **Correlation Heatmap**
   
   Explore relationships between variables using a heatmap of correlation coefficients.
2. **Pairplot**

   Visualise pairwise relationships between parameters to detect trends.

## Code Demonstration
* Run `main.py`
* Results for selected photosynthetic parameters


<img width="1046" height="198" alt="image" src="https://github.com/user-attachments/assets/3220c1a0-9cda-445b-8dc5-312a97fa4a0b" />

<img width="826" height="365" alt="image" src="https://github.com/user-attachments/assets/b713fb55-ef56-4192-a11f-b215fb41ccdb" />



