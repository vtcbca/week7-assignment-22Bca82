#create product.csv file which contain product number,name and selling of january to june month.
header=['Prod_No','Prod_Name','Jan','Feb','Mar','Apr','May','Jun']
# 5 product details print in csv file directly
rows=[
    [1,'mobile',9500,8500,9600,10000,11000,10500],
    [2,'Mouse',5600,4500,3000,5800,6000,6500],
    [3,'Monitor',15000,10500,18000,9000,8500,12000],
    [4,'CPU',36000,30000,45000,40000,32000,31000],
    [5,'Scanner',4500,5600,7500,9000,8500,9500]
     ]

# create empty list to store more 7 product details from user input
l=[] 
for i in range(7):
    n=int(input('Enter Product Id:'))
    name=input('Enter Product Name:')
    jan=int(input('Enter Jan Month Selling:'))
    feb=int(input('Enter Feb Month Selling:'))
    march=int(input('Enter March Month Selling:'))
    april=int(input('Enter April Month Selling:'))
    may=int(input('Enter May Month Selling:'))
    jun=int(input('Enter Jun Month Selling:'))
#   create a list 
    data=[n,name,jan,feb,march,april,may,jun]
    l.append(data)


from csv import writer
file="d://22bca82//sqlite3//product.csv"

with open(file,"w",newline="")as write_file:
#     create the writer object
    write=writer(write_file)
#     adding header to the csv file
    write.writerow(header)
#     adding 5 record directly
    write.writerows(rows)
#     adding 7 record from user
    write.writerows(l)
    print('successfully file created and data inserted')
	
	
	#create DataFrame
import pandas as pd
file="d://22bca82//sqlite3//product.csv"
df=pd.read_csv(file)
print(df)

#change column name Product No,Product Name,January,February,March,April,May,June
import pandas as pd
file="d://sqlite3//product.csv"
df=pd.read_csv(file)
df.columns=['Product No','Product Name','January','February','March','April','May','June']
print(df)

#Add column "Total Sell" to count total of all month and "Average Sell"
import pandas as pd
file="d://22bca82//sqlite3//product.csv"
df=pd.read_csv(file)
df['Total Sell']=df['January']+df['February']+df['March']+df['April']+df['May']+df['June']
print(df)

#Add 2 row at the end.
import pandas as pd
file="d://22bca82//sqlite3//product.csv"
df=pd.read_csv(file)

#to know the length of the dataframe
len(df)
df.loc[12]=[13,'Camera',4500,6000,10000,9500,8500,8000]
df.loc[13]=[14,'Head-phone',6500,7200,3600,4500,9000,6000]
print(df)

#Add 2 row after 3rd row.
import pandas as pd
file="d://22bca82//sqlite3//product.csv"
df=pd.read_csv(file)

#to know the length of the dataframe
len(df)
df.loc[2.5]=[3.4,'Moniter',4500,6000,10000,9500,8500,8000]
df.loc[2.6]=[3.5,'Head-phone',6500,7200,3600,4500,9000,6000]
df=df.sort_index(),reset_index()
print(df)


#print last 5 rows
import pandas as pd
file="d://22bca82//sqlite3//product.csv"
df=pd.read_csv(file)
#.tail() method print last 5 rows from the dataframe
df.tail()

#print row 6 to 10
import pandas as pd
file="d://22bca82//sqlite3//product.csv"
df=pd.read_csv(file)
#loc[start:stop:step]
#in this here we start from 6 and end to 10.
df.loc[6:10]

#print only product Name
import pandas as pd
file="d://22bca82//sqlite3//product.csv"
df=pd.read_csv(file)
df['Product Name']

#print sell of january month with product id and product name
import pandas as pd
file="d://22bca82//sqlite3//product.csv"
df=pd.read_csv(file)
print(df[['January','Product No','Product Name']])

#print sell of january month with product id and product name
import pandas as pd
file="d://22bca82//sqlite3//product.csv"
df=pd.read_csv(file)
data=df[(df["January"]>5000) & (df["February"]>8000)][['Product No','Product Name']]
print(data)

#print record in sorting order of product name.
import pandas as pd
file="d://22bca82//sqlite3//product.csv"
df=pd.read_csv(file)
sorted_name=df.sort_values(by='Product Name')
print(sorted_name)

#Display only odd index number column record.
import pandas as pd
file="d://22bca82//sqlite3//product.csv"
df=pd.read_csv(file)
print(df.loc[1::2])

#Display alternate row
import pandas as pd
file="d://22bca82//sqlite3//product.csv"
df=pd.read_csv(file)
print(df.loc[::2])
