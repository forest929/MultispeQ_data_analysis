# Analysis for photosynQ data using Python

### Libraries 
* Pandas
* Matplotlib
* Pathlib
* Seaborn
  
## FILTER DATA
1. Use your own data or find available data from projects on the PhotosynQ platform
   https://photosynq.org/search?utf8=%E2%9C%93&q=plants&filter=projects
2. Clean up poor data.
   Due to system error or device error, sometimes the data points collected during measurements were invalid, which will be removed before handling the data set.
4. Select parameters of interest.
 ```python
  all_relavant_cols = ['Light Intensity (PAR)', 'LEF', 'Phi2', 'qL', 'PhiNPQ', 'NPQt', 'PhiNO','PS1 Active Centers', 'PS1 Open Centers', 'PS1 Over Reduced Centers', 'SPAD']
  ```
## PLOT DATA
1. Correlation heatmap
2. Pairplot



