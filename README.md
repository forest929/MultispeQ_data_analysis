# Correlation analysis for photosynQ data that you collected using handheld-MmultiSpe.

* Data available on PhotosynQ platform: https://photosynq.org/search?utf8=%E2%9C%93&q=plants&filter=projects
* Data filtering include clean up your data and keep the parameters you are interested in.
* Photosynthetic parameters covered:
  ```python
  all_relavant_cols = ['Light Intensity (PAR)', 'LEF', 'Phi2', 'qL', 'PhiNPQ', 'NPQt', 'PhiNO','PS1 Active Centers', 'PS1 Open Centers', 'PS1 Over Reduced Centers', 'SPAD']
  ```
* Correlation heatmap and pairplot ploting.


### Libraries 
* Pandas
* Matplotlib
* Pathlib
* Seaborn
