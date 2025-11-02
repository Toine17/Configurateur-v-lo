import pandas as pd
import streamlit as st

df_Boitier_pedalier = pd.read_csv('Boitier_pédalier.csv')
df_Cadre = pd.read_csv('Cadre.csv')
df_Cassette = pd.read_csv('Cassette.csv')
df_Chaines = pd.read_csv('Chaines.csv')
df_Disques = pd.read_csv('Disques.csv')
df_Jantes = pd.read_csv('Jantes.csv')
df_Mini_groupe = pd.read_csv('Mini_groupe.csv')
df_Moyeu = pd.read_csv('Moyeu.csv')
df_Pedalier = pd.read_csv('Pedalier.csv')
df_Pneus = pd.read_csv('Pneus.csv')
df_Rayons = pd.read_csv('Rayons.csv')
df_Roues_completes = pd.read_csv('Roues_completes.csv')
df_Selle = pd.read_csv('Selle.csv')

def extraction_poids_prix (df,nom):
    poids = df['Poids'].loc[df['Nom']== nom].iloc[0]
    prix = df['Prix'].loc[df['Nom']== nom].iloc[0]
    if isinstance(poids, str):
        poids = poids.replace(',', '.').replace('g', '').strip()
    if isinstance(prix, str):
        prix = prix.replace(',', '.').replace('€', '').replace(' ', '').strip()
        prix = prix.replace('\u202f', '').strip()

    poids = float(poids)
    prix = float(prix)
    return poids, prix

choix_configurateur = st.segmented_control("Que veux tu configurer",["Vélo complet","Roues à la carte"])
if choix_configurateur == "Vélo complet" :
    st.write (df_Cadre[['Nom','Poids','Prix']])
    choix_cadre = st.radio("Choisis ton cadre",df_Cadre['Nom'].tolist())
    poids_cadre, prix_cadre = extraction_poids_prix (df_Cadre,choix_cadre)

    st.write (df_Mini_groupe[['Nom','Poids','Prix']])
    choix_Mini_groupe = st.radio("Choisis ton groupe",df_Mini_groupe['Nom'].tolist())
    poids_Mini_groupe, prix_Mini_groupe = extraction_poids_prix (df_Mini_groupe,choix_Mini_groupe)

    st.write (df_Pedalier[['Nom','Poids','Prix']])
    choix_Pedalier = st.radio("Choisis ton pédalier",df_Pedalier['Nom'].tolist())
    poids_Pedalier, prix_Pedalier = extraction_poids_prix (df_Pedalier,choix_Pedalier)

    st.write (df_Cassette[['Nom','Poids','Prix']])
    choix_Cassette = st.radio("Choisis ta cassette 11-30",df_Cassette['Nom'].tolist())
    poids_Cassette, prix_Cassette = extraction_poids_prix (df_Cassette,choix_Cassette)

    st.write (df_Chaines[['Nom','Poids','Prix']])
    choix_Chaines = st.radio("Choisis ta chaine",df_Chaines['Nom'].tolist())
    poids_Chaines, prix_Chaines = extraction_poids_prix (df_Chaines,choix_Chaines)

    st.write (df_Boitier_pedalier[['Nom','Poids','Prix']])
    choix_Boitier_pedalier = st.radio("Choisis ton boitier de pédalier",df_Boitier_pedalier['Nom'].tolist())
    poids_Boitier_pedalier, prix_Boitier_pedalier = extraction_poids_prix (df_Boitier_pedalier,choix_Boitier_pedalier)

    st.write (df_Disques[['Nom','Poids','Prix']])
    choix_Disques = st.radio("Choisis tes disques",df_Disques['Nom'].tolist())
    poids_Disques, prix_Disques = extraction_poids_prix (df_Disques,choix_Disques)

    st.write (df_Pneus)
    choix_Pneus = st.radio("Choisis tes pneux montés avec des chambre à air TPU",df_Pneus['Nom'].tolist())
    poids_Pneus, prix_Pneus = extraction_poids_prix (df_Pneus,choix_Pneus)

    st.write (df_Roues_completes[['Nom','Poids','Prix']])
    choix_Roues_completes = st.radio("Choisis tes roues",df_Roues_completes['Nom'].tolist())
    poids_Roues_completes, prix_Roues_completes = extraction_poids_prix (df_Roues_completes,choix_Roues_completes)

    st.write (df_Selle[['Nom','Poids','Prix']])
    choix_Selle = st.radio("Choisis ta selle",df_Selle['Nom'].tolist())
    poids_Selle, prix_Selle = extraction_poids_prix (df_Selle,choix_Selle)

    poids_total_velo = poids_cadre + poids_Mini_groupe + poids_Pedalier + poids_Cassette + poids_Boitier_pedalier + poids_Chaines + poids_Disques + poids_Pneus + poids_Roues_completes + poids_Selle + 400
    prix_total_velo = prix_cadre + prix_Mini_groupe + prix_Pedalier + prix_Cassette + prix_Boitier_pedalier + prix_Chaines + prix_Disques + prix_Pneus + prix_Roues_completes + prix_Selle + 100
    st.write(f'Le poids du vélo est {round(poids_total_velo/1000,2)}kg pour un prix de {prix_total_velo}€')

elif choix_configurateur == "Roues à la carte" :
    
    choix_jantes = st.radio("Choisis tes jantes",df_Jantes['Nom'].tolist())
    poids_jantes, prix_jantes = extraction_poids_prix (df_Jantes,choix_jantes)
    st.write (df_Jantes[['Nom','Poids','Prix']])  
    

    choix_rayons = st.radio("Choisis tes rayons",df_Rayons['Nom'].tolist())
    poids_rayons, prix_rayons = extraction_poids_prix (df_Rayons,choix_rayons)
    st.write (df_Rayons[['Nom','Poids','Prix']])
    
    
    choix_moyeux = st.radio("Choisis tes moyeux",df_Moyeu['Nom'].tolist())
    poids_moyeux, prix_moyeux = extraction_poids_prix (df_Moyeu,choix_moyeux)
    st.write (df_Moyeu[['Nom','Poids','Prix']])

    poids_total_roues = poids_moyeux + poids_rayons + poids_jantes
    prix_total_roues = prix_moyeux + prix_rayons + prix_jantes
    st.write(poids_total_roues)
    st.write(f'Le poids des roues est {poids_total_roues}g pour un prix de {prix_total_roues}€')