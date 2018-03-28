import pandas as pd
import numpy as np

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
# since we are keeping the serial number as x in histograms 
df_iris['sn'] = pd.Series(np.arange(1, 151))
# see if the sn has been added
print df_iris.head(10)

#for scatterplot
def scatter(ser, x_label, y_label, color):
    fig, (ax1) = plt.subplots(ncols=1, sharey=True)
    plt.scatter(ser.index, ser, c=color)
    ax1.set_xlabel(x_label)
    ax1.set_ylabel(y_label)
    plt.show()
    

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


# this is the part where we generate histogram, scatter plots, 
# since when we asked in the class we saide that the 
fig, (ax1, ax2) = plt.subplots(ncols=2, sharey=True)
sb.boxplot(x='Sepal Length',y='Species',data=df_iris,linewidth=2, ax=ax1)
sb.boxplot(x='Sepal Width',y='Species',data=df_iris,linewidth=2,  ax=ax2)
fig, (ax1, ax2) = plt.subplots(ncols=2, sharey=True)
sb.boxplot(x='Petal Length',y='Species',data=df_iris,linewidth=2, ax=ax1)
sb.boxplot(x='Petal Width',y='Species',data=df_iris,linewidth=2,  ax=ax2)
scatter(speal_length,'Index of Values', 'Sepal Length in CM', 'red' )
scatter(petal_length,'Index of Values', 'Petal Length in CM', 'green' )
scatter(speal_width,'Index of Values', 'Sepal Width in CM', 'blue' )
scatter(petal_width,'Index of Values', 'Petal Width in CM', 'yellow' )
print 'Histograms for Sepal Length in Red'
pd.plotting.bootstrap_plot(speal_length, color='r')
print 'Histograms for Petal Length in Green'
pd.plotting.bootstrap_plot(petal_length, color='g')
print 'Histograms for Sepal Width in Blue'
pd.plotting.bootstrap_plot(speal_width, color='b')
print 'Histograms for Petal Width in Yellow'
pd.plotting.bootstrap_plot(petal_width, color='y')
