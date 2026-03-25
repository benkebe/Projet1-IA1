import streamlit as st
import datetime as dt
from PIL import Image
import matplotlib.pyplot as plt
from pandas import read_csv
import seaborn as sns
from pandas.plotting import scatter_matrix


st.sidebar.title("Projet 1 - Streamlit")
menu = st.sidebar.selectbox("Menu", ["Accueil", "Analyses de donnees", "Tendances",
                                     "Correlations","Visualisations","Reccomandations"])

try:
    URL='BeansDataSet.csv'
    col=['Channel','Region','Robusta','Arabica','Espresso','Lungo','Latte','Cappuccino']
    data=read_csv(URL)
except:
        st.write('Erreur de chargement du fichier')


if menu == "Accueil":
    st.markdown(
        """
        <div style='text-align: center;'>
        <h1>Analyse des ventes Beans & Pods</h1>
        <p style="color: blue;">Bienvenue sur notre application d'analyse des ventes de café !</p>
        """,
        unsafe_allow_html=True  
        
    ) 
    st.dataframe(data)


elif menu == "Analyses de donnees":
    st.markdown(
        """
        <div style='text-align: center;'>
        <h1>Analyse des ventes Beans & Pods</h1>
        <h2>Analyses des donnees</h2>
        <p style="color: blue;">Voici quelques analyses de données basées sur les ventes de nos produits :</p>
        """,
        unsafe_allow_html=True 

    )
    
    region=st.selectbox("Sélectionnez une région :",['North','South','Central'])
    channel=st.selectbox("Sélectionnez un canal de vente :",['Online','Store'])
    filtre = (data['Region'] == region) & (data['Channel'] == channel)

    st.write("Nombre total de ventes :", data.shape[0])
    
    if region=='North' and channel=='Online':
        st.write("Ventes de café en ligne dans la région Nord :")
        st.dataframe(data[filtre])
    elif region=='North' and channel=='Store':
        st.write("Ventes de café en magasin dans la région Nord :")
        st.dataframe(data[filtre])
    elif region=='South' and channel=='Online':
        st.write("Ventes de café en ligne dans la région Sud :")
        st.dataframe(data[filtre])
    elif region=='South' and channel=='Store':
        st.write("Ventes de café en magasin dans la région Sud :")
        st.dataframe(data[filtre])
    elif region=='Central' and channel=='Online':
        st.write("Ventes de café en ligne dans la région Centrale :")
        st.dataframe(data[filtre])
    elif region=='Central' and channel=='Store':
        st.write("Ventes de café en magasin dans la région Centrale :")
        st.dataframe(data[filtre])

    st.subheader("Distribution des régions :")
    figure, ax = plt.subplots()
    data['Region'].value_counts().plot(kind='bar', ax=ax)
    st.pyplot(figure)

    st.header("Statistiques descriptives")
    st.write(data.describe())
    

    
elif menu == "Tendances":
    st.markdown(
        """
        <div style='text-align: center;'>
        <h1>Analyse des ventes Beans & Pods</h1>
        <h2>Tendances</h2>
        <p style="color: blue;">Voici les tendances de vente de nos produits :</p>
        """,
        unsafe_allow_html=True 

    )
    
    st.header("Tendances de vente par produit :")
    produits = ['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']
    st.write(data.describe())

    num_cols = ['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']

    st.subheader("Histogramme des ventes par produit : ")
    figure, ax = plt.subplots(figsize=(15,10))


    data[num_cols].hist(bins=20,figsize=(15,20),grid=True,layout=(3,3))
    st.pyplot(plt.gcf())

    st.subheader("Graphes de densités : ")
    figure2, ax = plt.subplots(figsize=(15,10))
    data[num_cols].plot(kind='density', layout=(3,3), figsize=(15,10), sharex=False, sharey=False, subplots=True)
    st.pyplot(plt.gcf())

    ventes_totales = data[produits].sum()
    produit_le_mieux_vendu = ventes_totales.idxmax()
    produit_le_moins_vendu = ventes_totales.idxmin()
    st.header(f"Le produit le mieux vendu est : {produit_le_mieux_vendu}")
    st.header(f"Le produit le moins vendu est : {produit_le_moins_vendu}")

elif menu == "Correlations":
     
     st.markdown(
        """
        <div style='text-align: center;'>
        <h1>Analyse des ventes Beans & Pods</h1>
        <h2>Correlations</h2>
        <p style="color: blue;">Voici les tendances de vente de nos produits :</p>
        """,
        unsafe_allow_html=True 

    )
     
     st.write('Etudes de correlations :')
     corr = data.corr(numeric_only=True)
     figure, ax = plt.subplots(figsize=(10,8))
     sns.heatmap(corr, annot=True, cmap='summer', fmt='.3f', ax=ax)
     st.pyplot(figure)


elif menu == "Visualisations":
    st.markdown(
        """
        <div style='text-align: center;'>
        <h1>Analyse des ventes Beans & Pods</h1>
        <h2>Visualisations</h2>
        <p style="color: blue;">Bienvenue sur notre application d'analyse des ventes de café !</p>
        """,
        unsafe_allow_html=True  
        
    )
    st.header("Techniques de visualisation : ")

    num_cols = ['Robusta','Arabica','Espresso','Lungo','Latte','Cappuccino']

    # Histogrammes
    st.subheader("Histogramme des variables : ")
    data[num_cols].hist(bins=20, figsize=(15,20), grid=True, layout=(3,3))
    st.pyplot(plt.gcf())

    # Histogramme spécifique (remplace glucose par Robusta par ex)
    st.subheader("Histogramme de Robusta :")
    figure, ax = plt.subplots(figsize=(10,6))
    ax.hist(data['Robusta'], bins=20)
    ax.set_title("Distribution de Robusta")
    st.pyplot(figure)

    # Densité
    st.subheader("Graphes de densités : ")
    data[num_cols].plot(kind='density', layout=(3,3), figsize=(15,10),
                         sharex=False, sharey=False, subplots=True)
    st.pyplot(plt.gcf())

    # Scatter Matrix
    st.subheader("Scatter Matrix : ")
    scatter_matrix(data[num_cols], figsize=(15,15))
    st.pyplot(plt.gcf())

    # Pairplot
    st.subheader("Les pairplots : ")
    sns.pairplot(data, vars=num_cols, hue='Channel')  # ou Region
    st.pyplot()

    

elif menu == "Reccomandations":
    st.markdown(
        """
        <div style='text-align: center;'>
        <h1>Analyse des ventes Beans & Pods</h1>
        <p style="color: blue;">Bienvenue sur notre application d'analyse des ventes de café !</p>
        """,
        unsafe_allow_html=True  
        
    )
    st.header("Recommandations marketing")

    st.write("""
    - Investir dans le produit le plus vendu
    - Améliorer les produits les moins vendus
    - Cibler les régions les plus performantes
    - Développer les ventes en ligne
    """)

    

    



    






   

        


    

    


    
        
        
       





