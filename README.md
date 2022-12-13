# Individual Project
## Cohort analysis python package


The following python package was created in the scopes of an individual project for DS223 Maketing Analytics course. 

The python package focuses on cohort analysis.


### Installation:
---
You can install **Cohort** using 

### Usage:
```python
pip install cohort
``` 

```python
import pandas as pd
import matplotlib.pyplot as plt
from cohort import cohort_analysis

# Read dataset 
data=pd.read_csv()

analysis=cohort_analysis(input_df=data, ActivityDate='', CustomerID='')

## Generate retention heatmap

analysis.plot_retention()



```


