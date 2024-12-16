import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Simulation des données COVID-19
# Remarque : Données simulées uniquement à des fins de démonstration
np.random.seed(42)

class Virus:
    def __init__(self):
        """Initialise les données simulées et les régions"""
        self.regions = ['Amérique du Nord', 'Amérique du Sud', 'Europe', 'Asie', 'Afrique']
        self.mois = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin', 'Juil', 'Août', 'Sep', 'Oct', 'Nov', 'Déc']
        self.cas_quotidiens = self.generer_cas_quotidiens()
        self.taux_vaccination = self.generer_taux_vaccination()
        self.taux_mortalite = self.generer_taux_mortalite()
    
    def generer_cas_quotidiens(self):
        """Génère des cas quotidiens simulés pour chaque région"""
        cas = {}
        for region in self.regions:
            base = np.random.randint(1000, 5000)
            vague = base * (1 + 0.5 * np.sin(np.linspace(0, 4*np.pi, 12)))
            cas[region] = vague
        return pd.DataFrame(cas, index=self.mois)
    
    def generer_taux_vaccination(self):
        """Génère des taux de vaccination simulés"""
        taux = {}
        for region in self.regions:
            progression = np.cumsum(np.random.uniform(5, 15, 12))
            progression = np.minimum(progression, 100)  # Limité à 100%
            taux[region] = progression
        return pd.DataFrame(taux, index=self.mois)
    
    def generer_taux_mortalite(self):
        """Génère des taux de mortalité simulés"""
        mortalite = {}
        for region in self.regions:
            taux = np.random.uniform(0.5, 3, 12)
            mortalite[region] = taux
        return pd.DataFrame(mortalite, index=self.mois)
    
    def creer_visualisation(self):
        """Crée une visualisation globale des données"""
        plt.figure(figsize=(20, 15))
        plt.suptitle('Visualisation Globale des Données', fontsize=20, fontweight='bold')
        
        # 1. Graphique en ligne des cas quotidiens
        plt.subplot(2, 2, 1)
        self.cas_quotidiens.plot(kind='line', ax=plt.gca())
        plt.title('Cas quotidiens par région', fontsize=12)
        plt.xlabel('Mois')
        plt.ylabel('Nombre de cas')
        plt.legend(title='Régions', bbox_to_anchor=(1.05, 1), loc='upper left')
        
        # 2. Graphique empilé des taux de vaccination
        plt.subplot(2, 2, 2)
        self.taux_vaccination.plot(kind='bar', stacked=True, ax=plt.gca())
        plt.title('Taux de vaccination cumulés', fontsize=12)
        plt.xlabel('Mois')
        plt.ylabel('Pourcentage de vaccination')
        plt.legend(title='Régions', bbox_to_anchor=(1.05, 1), loc='upper left')
        
        # 3. Carte thermique des taux de mortalité
        plt.subplot(2, 2, 3)
        im = plt.imshow(self.taux_mortalite, cmap='YlOrRd')
        plt.colorbar(im)
        plt.title('Taux de mortalité par région', fontsize=12)
        plt.xlabel('Régions')
        plt.ylabel('Mois')
        plt.xticks(range(len(self.regions)), self.regions, rotation=45)
        plt.yticks(range(len(self.mois)), self.mois)

        # Annotations des cellules
        for i in range(len(self.mois)):
            for j in range(len(self.regions)):
                plt.text(j, i, f'{self.taux_mortalite.iloc[i, j]:.2f}', 
                         ha='center', va='center', 
                         color='black' if self.taux_mortalite.iloc[i, j] < 1.5 else 'white')
        
        # 4. Diagramme circulaire de la répartition totale des cas
        plt.subplot(2, 2, 4)
        total = self.cas_quotidiens.sum()
        plt.pie(total, labels=total.index, autopct='%1.1f%%')
        plt.title('Répartition totale des cas', fontsize=12)
        
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()
    
    def generer_resume_statistique(self):
        """Génère un résumé statistique des données"""
        print("Résumé des cas quotidiens :")
        print(self.cas_quotidiens.describe())
        print("\nRésumé des taux de vaccinb  on :")
        print(self.taux_vaccination.describe())
        print("\nRésumé des taux de mortalité :")
        print(self.taux_mortalite.describe())

# Exécution
visualisateur = Virus()
visualisateur.creer_visualisation()
visualisateur.generer_resume_statistique()

