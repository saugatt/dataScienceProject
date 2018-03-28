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
# saving each numercial column as pandas series 
speal_length =  df_iris['Sepal Length']
speal_width =  df_iris['Sepal Width']
petal_length =  df_iris['Petal Length']
petal_width =  df_iris['Petal Width']


print " *******************************************************************************"
print 'For Sepal Length :- '
print 'Count :', speal_length.count()	
print 'Minimum :'	, speal_length.min()
print 'Maximum : ', speal_length.max()
print 'Mean : ', speal_length.mean()	
print 'Median : ', speal_length.median()
print 'Mode : ', speal_length.mode()
print 'Quartile : ' 
print 'Range : '	
print 'Variance : '	
print 'Standard Deviation : '	
print 'Coefficient of Variation : '	
print 'Skewness : '	
print 'Kurtosis : '
print " *******************************************************************************"


print 'For Sepal Width :- '
print 'Count :'	
print 'Minimum :'	
print 'Maximum : '
print 'Mean : '	
print 'Median : '
print 'Mode : '	
print 'Quartile : ' 
print 'Range : '	
print 'Variance : '	
print 'Standard Deviation : '	
print 'Coefficient of Variation : '	
print 'Skewness : '	
print 'Kurtosis : '
print " *******************************************************************************"


print 'For Petal Length:- '
print 'Count :'	
print 'Minimum :'	
print 'Maximum : '
print 'Mean : '	
print 'Median : '
print 'Mode : '	
print 'Quartile : ' 
print 'Range : '	
print 'Variance : '	
print 'Standard Deviation : '	
print 'Coefficient of Variation : '	
print 'Skewness : '	
print 'Kurtosis : '
print " *******************************************************************************"

print 'For Petal Width :- '
print 'Count :'	
print 'Minimum :'	
print 'Maximum : '
print 'Mean : '	
print 'Median : '
print 'Mode : '	
print 'Quartile : ' 
print 'Range : '	
print 'Variance : '	
print 'Standard Deviation : '	
print 'Coefficient of Variation : '	
print 'Skewness : '	
print 'Kurtosis : '
print " *******************************************************************************"


