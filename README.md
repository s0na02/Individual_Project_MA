# Individual Project
## Cohort analysis python package


The following python package was created in the scopes of an individual project for **DS223 Maketing Analytics** course. 

The python package focuses on cohort analysis.

Codes for the cohort analysis can be found in Cohort folder.

---

### Installation:

You can install **Cohort** using 

```python
pip install cohort
``` 
---

### Usage:

```python
import pandas as pd
import matplotlib.pyplot as plt
from cohort import cohort_analysis

# Read dataset 

data=pd.read_csv('data.csv',encoding='latin',parse_dates=['OrderDate'])

analysis=cohort_analysis(input_df=data, ActivityDate='OrderDate', CustomerID='UserId')

## Generate retention heatmap

analysis.plot_retention()
```

![](https://imgur.com/XVM3TkC.png)




