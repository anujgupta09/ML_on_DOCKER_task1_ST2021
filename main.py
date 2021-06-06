import numpy
import pandas
import os

os.system("tput setaf 2 && clear")
experience = int(input("\nEnter Years of Experience:\t"))

data = pandas.read_csv("SalaryData.csv")

x=data["YearsExperience"]
y=data["Salary"]

x=x.values.reshape(-1,1)
y=y.values.reshape(-1,1)

####################################################################

from sklearn.linear_model import LinearRegression
mind=LinearRegression()

mind.fit(x,y)

Salary=mind.predict([[experience]])
Salary=Salary.astype(int)

os.system("tput setaf 3")

print("\nYour Salary is : Rupees >", Salary,"\n")

os.system("tput setaf 7")
