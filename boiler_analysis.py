import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
from sklearn.metrics import r2_score 
import matplotlib.pyplot as plt

 #importing the data from the sheet into a DataFrame object
df = pd.read_excel('D:\PS\SIP PROJECT DATA 2.xlsx')
df.drop([0],axis=0,inplace=True) 

x = df[['Load','Ash(%)','Moisture (%)','Carbon (%)','Hydrogen(%)','Nitrogen(%)','Oxygen(%)','Sulphur(%) ','GCV of Coal (Kcal/Kg)']].tail(5000).values
y = df['Boiler eff'].tail(5000).values.reshape(-1,1)

# Check correlation and r squared value of each input with the output
from scipy.stats import pearsonr
print(f'Correlation between Load and y = {pearsonr(x[:,0],y[:,0])[0]:.2f}')
print(f'Correlation between Ash(%) and y = {pearsonr(x[:,1],y[:,0])[0]:.2f}')
print(f'Correlation between Moisture (%) and y = {pearsonr(x[:,2],y[:,0])[0]:.2f}')
print(f'Correlation between Carbon (%) and y = {pearsonr(x[:,3],y[:,0])[0]:.2f}')
print(f'Correlation between Hydrogen(%) and y = {pearsonr(x[:,4],y[:,0])[0]:.2f}')
print(f'Correlation between Nitrogen(%) and y = {pearsonr(x[:,5],y[:,0])[0]:.2f}')
print(f'Correlation between Oxygen(%) and y = {pearsonr(x[:,6],y[:,0])[0]:.2f}')
print(f'Correlation between Sulphur(%) and y = {pearsonr(x[:,7],y[:,0])[0]:.2f}')
print(f'Correlation between GCV of Coal and y = {pearsonr(x[:,8],y[:,0])[0]:.2f}')


#run the linear regression algorithm and train the algorithm using the dataset
poly_reg = PolynomialFeatures(degree=6)
X_poly = poly_reg.fit_transform(x)

reg = linear_model.LinearRegression(normalize = True)
reg.fit(X_poly,y)

print(reg.coef_)
print('\n',reg.intercept_)
print('\n')

#input the parameters for prediction
df_2 = pd.read_excel('D:\PS\SIP PROJECT DATA 2.xlsx')
predicted_efficiency = reg.predict(poly_reg.fit_transform(df_2[['Load','Ash(%)','Moisture (%)','Carbon (%)','Hydrogen(%)','Nitrogen(%)','Oxygen(%)','Sulphur(%) ','GCV of Coal (Kcal/Kg)']].tail(30).values))
print('The boiler efficiency matrix is-')
print(predicted_efficiency)
print('\n')

#Evaluation of the model using it's R^2 score
r2 = r2_score(df_2['Boiler eff'].tail(30),predicted_efficiency)
print('Coefficient of Determination', r2) 

#plotting Experimental efficiency vs Predicted efficiency
plt.scatter(predicted_efficiency, df_2['Boiler eff'].tail(30))
plt.xlim(60, 100)
plt.ylim(60,100)
plt.xlabel("Prediced_eff")
plt.ylabel("Experimental_eff")
plt.show()