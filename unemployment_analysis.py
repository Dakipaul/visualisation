
#Importing python inbuilt libraries
import pandas as pd
import matplotlib.pyplot as plt

#Read the .csv files in dataframe 
unemployed = pd.read_csv('D:/Datasets/unemployment_analysis.csv')

'''Lineplot for Unemployment in three Different Nations from 1990-2020'''
#plotting figure by inserting vales from dataframe labelling the plots and adding legend to the plot
plt.figure()
plt.plot(unemployed['Year'], unemployed['Europe & Central Asia'], color='g', label='Europe & Central Asia')
plt.plot(unemployed['Year'], unemployed['United Kingdom'], color='r', label='United kngdom')
plt.plot(unemployed['Year'], unemployed['United States'], color='b', label='United States')
plt.xlabel("Years")
plt.ylabel("unemployment_rate")
plt.title('unemployment from 1990 to 2020')
plt.legend()
plt.show()
#saving the figure as Lineplot.png file
plt.savefig('Lineplot.png')

'''Barplot for unemployent rate in 4 different Nations from (1990-2020)'''
#subplotting figure by inserting vales from dataframe labelling the plots and adding legend to the plot
plt.subplot(2,2,1)
plt.bar(unemployed['Year'], unemployed['United Arab Emirates'], color='r', label='UAE', alpha=0.8)
plt.legend()
plt.subplot(2,2,2)
plt.bar(unemployed['Year'], unemployed['India'], color='b', label='IND', alpha=0.8)
plt.legend()
plt.subplot(2,2,3)
plt.bar(unemployed['Year'], unemployed['Pakistan'], color='y', label='PAK', alpha=0.8)
plt.legend()
plt.subplot(2,2,4)
plt.bar(unemployed['Year'], unemployed['South Africa'], color='k', label='SA',alpha=0.9)
plt.legend()
plt.show()
#saving the figure as Barplot.png file
plt.savefig('Barplot.png')

'''Scatterplot for unemployent rate in 3 different Nations from (1990-2020)'''
#plotting figure by inserting vales from dataframe labelling the plots and adding legend to the plot
plt.scatter(unemployed['Year'],unemployed['Portugal'],color='y', marker='v',label='Por')
plt.legend()
plt.scatter(unemployed['Year'],unemployed['Netherlands'],color='k', alpha=0.5, marker='o',label='Dutch')
plt.legend()
plt.scatter(unemployed['Year'],unemployed['Germany'],color='m', marker='v',label='Ger')
plt.legend()
plt.xlabel("Years")
plt.ylabel("unemployment_rate")
plt.title('Unemployment Rate from 90-20')
plt.show()
#saving the figure as Scatterplot.png file
plt.savefig('Scatterplot.png')


