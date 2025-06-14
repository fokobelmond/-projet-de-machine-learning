import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title("Resultat de demande de crédit")

#collecter le profil d'entré

st.sidebar.header("Caracteristiques du client")
def client_caract_entree():
    Gender=st.sidebar.selectbox('Genre',('Male','Female'))
    Married=st.sidebar.selectbox('Marié',('Yes','No'))
    Dependents=st.sidebar.selectbox("nombre d'enfants",('0','1','2','3+'))
    Education=st.sidebar.selectbox(' Education',('Graduate','Not Graduate'))
    Self_Employed=st.sidebar.selectbox('entrepreneur',('Yes','No'))
    ApplicantIncome=st.sidebar.slider('salaire du client',150.0,8100.0,150.0)
    CoapplicantIncome=st.sidebar.slider('salaire du conjoint',0.0,4500.0,0.0)
    LoanAmount=st.sidebar.slider('Montant du credit',9.0,700.0,9.0)
    Loan_Amount_Term=st.sidebar.selectbox("Durée du credit",(360., 120., 240., 180.,  60., 300., 480.,  36.,  84.,  12.))
    Credit_History=st.sidebar.selectbox('histrorique de credit',(1.0,0.0))
    Property_Area=st.sidebar.selectbox("Zone d'habitation",('Urban','Rural','Semiurban'))
    data={
    'Gender' :Gender,
    'Married':Married,
    'Dependents' :Dependents,
    'Education' :Education,
    'Self_Employed':Self_Employed,
    'ApplicantIncome' :ApplicantIncome,
    'CoapplicantIncome' :CoapplicantIncome,
    'LoanAmount' :LoanAmount,
    'Loan_Amount_Term' :Loan_Amount_Term,
    'Credit_History' :Credit_History,
    'Property_Area' :Property_Area
    }

    profil_client=pd.DataFrame(data,index=[0])
    return profil_client
input_df=client_caract_entree()

#transforfer les données

#1) importer les données

df=pd.read_csv('train_home_loan(1).csv')
credit_input=df.drop(columns=['Loan_ID','Loan_Status'])
df['Gender']=df['Gender'].fillna(df['Gender'].mode()[0])
df['Married']=df['Married'].fillna(df['Married'].mode()[0])
df['Dependents']=df['Dependents'].fillna(df['Dependents'].mode()[0])
df['Self_Employed']=df['Self_Employed'].fillna(df['Self_Employed'].mode()[0])
df['LoanAmount']=df['LoanAmount'].fillna(df['LoanAmount'].median())
df['Loan_Amount_Term']=df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].median())
df['Credit_History']=df['Credit_History'].fillna(df['Credit_History'].median())
donnee_entree=pd.concat([input_df,credit_input],axis=0)

#2) encoder les données

var_cat=['Gender', 'Married', 'Dependents', 'Education','Self_Employed','Property_Area']
donnee_entree = pd.get_dummies(donnee_entree, columns=var_cat, drop_first=True)
st.write(donnee_entree[:1])
#importer le modèle
load_model=pickle.load(open('previson_credit.pkl','rb'))

#apliquer le modèle
prevision = load_model.predict(donnee_entree[:1])

st.subheader('Résultat de la prévision')

if prevision == 1:
    st.success("Crédit accordé")
else:
    st.error("Crédit refusé")
