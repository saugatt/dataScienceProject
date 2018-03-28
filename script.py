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
mode = str(speal_length.mode()).split()[1]
print 'Mode : ', mode
quat1 = str(speal_length.quantile([0.25])).split()[1]
print 'Quartile 1 :', quat1
print 'Range : ', speal_length.max() - speal_length.min()
print 'Variance : ', speal_length.var()
print 'Standard Deviation : ',  speal_length.std()
print 'Coefficient of Variation : '	, speal_length.std() / speal_length.mean() * 100, '%'
print 'Skewness : ', speal_length.skew()	
print 'Kurtosis : ', speal_length.kurtosis()
print " *******************************************************************************"


print 'For Sepal Width :- '
print 'Count :', speal_width.count()	
print 'Minimum :'	, speal_width.min()
print 'Maximum : ', speal_width.max()
print 'Mean : ', speal_width.mean()	
print 'Median : ', speal_width.median()
mode = str(speal_width.mode()).split()[1]
print 'Mode : ', mode
quat1 = str(speal_width.quantile([0.25])).split()[1]
print 'Quartile 1 :', quat1
print 'Range : ', speal_width.max() - speal_width.min()
print 'Variance : ', speal_width.var()
print 'Standard Deviation : ',  speal_width.std()
print 'Coefficient of Variation : '	, speal_width.std() / speal_width.mean() * 100, '%'
print 'Skewness : ', speal_width.skew()	
print 'Kurtosis : ', speal_width.kurtosis()
print " *******************************************************************************"


print 'For Petal Length:- '
print 'Count :', petal_length.count()	
print 'Minimum :'	, petal_length.min()
print 'Maximum : ', petal_length.max()
print 'Mean : ', petal_length.mean()	
print 'Median : ', petal_length.median()
mode = str(petal_length.mode()).split()[1]
print 'Mode : ', mode
quat1 = str(petal_length.quantile([0.25])).split()[1]
print 'Quartile 1 :', quat1
print 'Range : ', petal_length.max() - petal_length.min()
print 'Variance : ', petal_length.var()
print 'Standard Deviation : ',  petal_length.std()
print 'Coefficient of Variation : '	, petal_length.std() / petal_length.mean() * 100, '%'
print 'Skewness : ', petal_length.skew()	
print 'Kurtosis : ', petal_length.kurtosis()
print " *******************************************************************************"

print 'For Petal Width :- '
print 'Count :', petal_width.count()	
print 'Minimum :'	, petal_width.min()
print 'Maximum : ', petal_width.max()
print 'Mean : ', petal_width.mean()	
print 'Median : ', petal_width.median()
mode = str(petal_width.mode()).split()[1]
print 'Mode : ', mode
quat1 = str(petal_width.quantile([0.25])).split()[1]
print 'Quartile 1 :', quat1
print 'Range : ', petal_width.max() - petal_width.min()
print 'Variance : ', petal_width.var()
print 'Standard Deviation : ',  petal_width.std()
print 'Coefficient of Variation : '	, petal_width.std() / petal_width.mean() * 100, '%'
print 'Skewness : ', petal_width.skew()	
print 'Kurtosis : ', petal_width.kurtosis()
print " *******************************************************************************"


