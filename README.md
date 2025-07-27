# 📊 PhotosynQ data analysis in Python
This repository provides a Python-based workflow for cleaning and analyzing PhotosynQ project data, with a focus on photosynthesis-related parameters.
## 🔧 Libraries Used
* `pandas` - for data manipulation and cleaning
* `matplotlib` - for basic plotting
* `seaborn` - for advanced visualisation
* `pathlib` - for file path handling
  
## 📂 FILTER DATA
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
## 📈 PLOT DATA
1. **Correlation Heatmap**
   
   Explore relationships between variables using a heatmap of correlation coefficients.
2. **Pairplot**

   Visualise pairwise relationships between parameters to detect trends.


