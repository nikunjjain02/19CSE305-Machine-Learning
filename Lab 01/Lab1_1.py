import pandas as pd
import numpy as np

#Load the data into csv file if multiple sheets are there on the excel file
df= pd.DataFrame(pd.read_csv(r"C:\Users\nikun\Desktop\ML_Files\lab1.csv"))
print(df)

#Dropping/Deleting various columns which are useless
columns_to_drop = ['Candy','Mango','Milk']
df = df.drop(columns = columns_to_drop)
#print(df.head())

#Making three matrices A , X and C to perform AX=C

#Making Matrix A
item_quantities = df[['Candies (#)' , 'Mangoes (Kg)' , 'Milk Packets (#)']].values
A=item_quantities

#Making matrix X
X=np.zeros((len(df), 3))

#Making matrix C
C=df['Payment (Rs)'].values

rank_A=np.linalg.matrix_rank(A)

#-------Dimensionality--------
print('Dimensionality of the matrix is' , rank_A)

#-------Number of vectors in matrix---------
print('Number of vectors in matrix A:' , A.shape[0])

#-------Rank of Matrix A---------
print("The rank of the matrix A is " , rank_A)

#---------Inverse of the Matrix A-----------
Inve = np.linalg.pinv(A)
print("Inverse of the Matrix A is " , Inve)

#---------Solving For X Matrix to find cost of each product--------
product_costs = np.dot(Inve , C)

print("Product of Costs")
print("Candies Costs:",product_costs[0])
print("Mangoes Costs:",product_costs[1])
print("Milk Packets Costs:",product_costs[2])

#--------Training the model to add the column of Rich/Poor----------
df['Class'] = df['Payment (Rs)'].apply(lambda x: 'RICH' if x > 200 else 'POOR')
print(df)