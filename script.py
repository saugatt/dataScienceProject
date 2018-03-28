import pandas as pd

# we are ingnoring the warnings given by seaborn
import warnings
warnings.filterwarnings("ignore")

#matplot lib and seaborn is used for Stastical data visualization
import matplotlib.pyplot as plt
import seaborn as sb

#importing the dataset which is the same folder
df_iris=pd.read_csv('iris.csv')

# test if the file is imported correctly
print df_iris.head(10)
print 'For Sepal Length'


