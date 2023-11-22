import streamlit as st
import pickle


#to open file in read mode
file1=open("model2.pkl","rb")
file2=open("scale2.pkl","rb")


#to read data from file (file1 and file2)
model=pickle.load(file1)   #load()  inbuilt method of pickle,to read data from file
scale=pickle.load(file2)
#model and scale both are user defined object

st.title("Credit Score Classification")

Annual_Income = st.number_input('Enter Annual Income',format='%2d',value=0)

Monthly_Inhand_Salary = st.number_input('Enter Monthly Inhand Salary',format='%2d',value=0)

Number_of_Bank_Accounts = st.number_input('Enter Number of Bank Accounts',format='%1d',value=0)

Number_of_Credit_cards = st.number_input('Enter Number of Credit cards',format='%1d',value=0)

Interest_rate = st.number_input('Enter Interest rate',format='%1d',value=0)

Number_of_Loans = st.number_input('Enter Number of Loans',format='%1d',value=0)

no_of_day_delayed = st.number_input('Enter Average number of days delayed by the person ',format='%2d',value=0)

no_of_delayed_payment = st.number_input('Enter number of delayed payment',format='%1d',value=0)

Credit_Mix = st.number_input('Enter Credit Mix (Good: 1, Standard: 2, bad: 0) : ',format='%1d',value=0)

Outstanding_Debt = st.number_input('Enter Outstanding Debt : ',format='%2d',value=0)

Credit_History_Age = st.number_input('Enter Credit History Age : ',format='%2d',value=0)

Monthly_Balance = st.number_input('Enter Monthly Balance : ',format='%2d',value=0)

                       
#create a list X and hold all inputs in this list according to sequence of given dataset
X=[Annual_Income,Monthly_Inhand_Salary,Number_of_Bank_Accounts,Number_of_Credit_cards,Interest_rate,Number_of_Loans,
no_of_day_delayed,no_of_delayed_payment,Credit_Mix,Outstanding_Debt,Credit_History_Age,Monthly_Balance]
                       
if st.button('predict'):
         #To change list in numpy array (2D)
         import numpy as np
         X=np.array([X]) #[[]] means 2D
         #Apply StandardScaler n input exp
         X=scale.transform(X)

         #predict whether customer credit score Good ,poor ,stanadard
         Y_pred=model.predict(X)[0]
         
         if Y_pred==1:
            st.image('bad-credit-score.jpg')
            st.error("Predicted Credit Score is poor")
           
         elif Y_pred==2:
            st.image('standard-credit-score.png')
            st.success("Predicted Credit Score is Standard")
            
         else:
            st.image('Good-credit-score.png')
            st.success("Predicted Credit Score is Good")
            
        
