import os
import pandas as pd
import re

class FileManager:
    def __init__(self, file_path):
        self.data = None
        self.path = file_path
    def load_data(self):
        """
        Charge les données depuis le fichier CSV ou Excel dans un DataFrame.
        """
        if self.path.endswith('.csv'):
            self.data = pd.read_csv(self.path,sep=';')
        elif self.path.endswith(('.xls', '.xlsx')):
            self.data = pd.read_csv(self.path,sep=';')
    # Fonction permettant de renvoyer toute les donnees dans le fichier
    def Extraction_Tout(self):
        if self.data is not None:
            return self.data
    
    # Extraction de sous données en fonction de bacterie
    def Extraction_data_Bacterie(self,name):
        return self.data[self.data['Souche Name'] == name]
                
    
    # Extraction de sous données en fonction de phylum            
    def Extraction_data_Phylum(self, name):
        if self.data is not None:
            return self.data[self.data['phylum'] == name]
        else:
            raise ValueError("Les données ne sont pas chargées. Appelez d'abord load_data().")
    
    # Extraction de sous données en fonction de nutriment 
    def Extraction_data_Nutriment(self,name):
        return self.data[self.data['ImpExp'].str.contains(re.escape(name))]
    
    # Extraction de sous données en fonction de d'import ou export 
    def Extraction_data_Importe_Exporte(self,terme):
        return self.data[self.data['ImpExp'].str.endswith(terme)]
    
    # Extraction de sous données en fonction de bacterie et phylum
    def Extraction_data_Bacterie_Phylum(self,bacterie,phylum):
        mask = ((self.data['Souche Name'] == bacterie) & (self.data['phylum'] == phylum))
        return self.data[mask]
    
    # Extraction de sous données en fonction de bacterie et nutriment
    def Extraction_data_Bacterie_Nutriment(self,bacterie,nutriment):
        mask = ((self.data['Souche Name'] == bacterie) & (self.data['ImpExp'].str.contains(re.escape(nutriment))))
        return self.data[mask]
    
    # Extraction de sous données en fonction de bacterie et import ou export
    def Extraction_data_Bacterie_Importe_Exporte(self,bacterie,terme):
        mask = ((self.data['Souche Name'] == bacterie) & (self.data['ImpExp'].str.endswith(terme)))
        return self.data[mask]
    
    # Extraction de sous données en fonction de phylum et nutriment
    def Extraction_data_Phylum_Nutriment(self,phylum,nutriment):
        mask = ((self.data['phylum'] == phylum) & (self.data['ImpExp'].str.contains(re.escape(nutriment))))
        return self.data[mask]
            
    # Extraction de sous données en fonction de phylum et import ou export
    def Extraction_data_Phylum_Importe_Exporte(self,phylum,terme):
        mask = ((self.data['phylum'] == phylum) & (self.data['ImpExp'].str.endswith(terme)))
        return self.data[mask]
    
    # Extraction de sous données en fonction de  nutriment et import ou expot
    def Extraction_data_Nutriment_Importe_Exporte(self,nutriment,terme):
        mask = ((self.data['ImpExp'].str.contains(re.escape(nutriment))) & (self.data['ImpExp'].str.endswith(terme)))
        return self.data[mask]
    
    # Extraction de sous données en fonction de bacterie, phylum et nutriment
    def Extraction_data_Bacterie_Phylum_Nutriment(self,bacterie,phylum,nutriment):
        mask = ((self.data['Souche Name'] == bacterie) & (self.data['phylum'] == phylum) & (self.data['ImpExp'].str.contains(re.escape(nutriment))))
        return self.data[mask]
    
    # Extraction de sous données en fonction de bacterie, phylum et import ou export
    def Extraction_data_Bacterie_Phylum_Importe_Exporte(self,bacterie,phylum,terme):
        mask = ((self.data['Souche Name'] == bacterie) & (self.data['phylum'] == phylum) & (self.data['ImpExp'].str.endswith(terme)))
        return self.data[mask]
    
    # Extraction de sous données en fonction de bacterie, nutriment et import ou expot
    def Extraction_data_Bacterie_Nutriment_Importe_Exporte(self,bacterie,nutriment,terme):
        mask = ((self.data['Souche Name'] == bacterie) & (self.data['ImpExp'].str.contains(re.escape(nutriment))) & (self.data['ImpExp'].str.endswith(terme)))
        return self.data[mask]
    
    # Extraction de sous données en fonction de phylum, nutriment et import ou export
    def Extraction_data_Phylum_Nutriment_Importe_Exporte(self,phylum,nutriment,terme):
        mask = ((self.data['phylum'] == phylum) & (self.data['ImpExp'].str.contains(re.escape(nutriment))) & (self.data['ImpExp'].str.endswith(terme)))
        return self.data[mask]
    
    # Extraction de sous données en fonction de bacterie, nutriment et import ou export
    def Extraction_data_Bacterie_Phylum_Nutriment_Importe_Exporte(self,bacterie,phylum,nutriment,terme):
        mask = ((self.data['Souche Name'] == bacterie) & (self.data['phylum'] == phylum) & (self.data['ImpExp'].str.contains(re.escape(nutriment))) & (self.data['ImpExp'].str.endswith(terme)))
        return self.data[mask]
            
    # Extraction de sous données en fonction de bacterie, phylum, nutriment et import ou expot
    def Extraction_data_Bacterie_Phylum_Nutriment_Importe_Exporte(self,bacterie,phylum,nutriment,terme):
        mask = ((self.data['Souche Name'] == bacterie) & (self.data['phylum'] == phylum) & (self.data['ImpExp'].str.contains(re.escape(nutriment))) & (self.data['ImpExp'].str.endswith(terme))) 
        return self.data[mask]

    # Fonction permettant d'obtenir les donnee en fonction de requete de l'utilisateur
    def Get_Data(self,bacterie,phylum,nutriment,type):
        if phylum == 'Tout' and bacterie == 'Tout' and nutriment == 'Tout' and type == 'Tout':
            data = self.Extraction_Tout()
        elif phylum == 'Tout' and bacterie != 'Tout' and nutriment == 'Tout' and type == 'Tout':
            data = self.Extraction_data_Bacterie(bacterie)
        elif phylum != 'Tout' and bacterie == 'Tout' and nutriment == 'Tout' and type == 'Tout':
            data = self.Extraction_data_Phylum(phylum) 
        elif phylum == 'Tout' and bacterie == 'Tout' and nutriment != 'Tout' and type == 'Tout':
            data = self.Extraction_data_Nutriment(nutriment) 
        elif phylum == 'Tout' and bacterie == 'Tout' and nutriment == 'Tout' and type != 'Tout':
            data = self.Extraction_data_Importe_Exporte(type) 
        elif phylum != 'Tout' and bacterie != 'Tout' and nutriment == 'Tout' and type == 'Tout':
            data = self.Extraction_data_Bacterie_Phylum(bacterie,phylum)
        elif phylum != 'Tout' and bacterie == 'Tout' and nutriment != 'Tout' and type == 'Tout':
            data = self.Extraction_data_Bacterie_Nutriment(bacterie,nutriment)
        elif phylum != 'Tout' and bacterie == 'Tout' and nutriment == 'Tout' and type != 'Tout':
            data = self.Extraction_data_Bacterie_Importe_Exporte(bacterie,type)  
        elif phylum != 'Tout' and bacterie == 'Tout' and nutriment != 'Tout' and type == 'Tout':
            data = self.Extraction_data_Phylum_Nutriment(phylum,nutriment) 
        elif phylum != 'Tout' and bacterie == 'Tout' and nutriment == 'Tout' and type != 'Tout':
            data = self.Extraction_data_Phylum_Importe_Exporte(phylum,type) 
        elif phylum == 'Tout' and bacterie == 'Tout' and nutriment != 'Tout' and type != 'Tout':
            data = self.Extraction_data_Nutriment_Importe_Exporte(nutriment,type) 
        elif phylum != 'Tout' and bacterie != 'Tout' and nutriment != 'Tout' and type == 'Tout':
            data = self.Extraction_data_Bacterie_Phylum_Nutriment(bacterie,phylum,nutriment)
        elif phylum == 'Tout' and bacterie != 'Tout' and nutriment != 'Tout' and type != 'Tout':
            data = self.Extraction_data_Bacterie_Nutriment_Importe_Exporte(bacterie,nutriment,type)
        elif phylum != 'Tout' and bacterie == 'Tout' and nutriment != 'Tout' and type != 'Tout':
            data = self.Extraction_data_Phylum_Nutriment_Importe_Exporte(phylum,nutriment,type)
        elif phylum == 'Tout' and bacterie != 'Tout' and nutriment != 'Tout' and type != 'Tout':
            data = self.Extraction_data_Bacterie_Nutriment_Importe_Exporte(bacterie,nutriment,type) 
        elif phylum != 'Tout' and bacterie != 'Tout' and nutriment != 'Tout' and type != 'Tout':
            data = self.Extraction_data_Bacterie_Phylum_Nutriment_Importe_Exporte(bacterie,phylum,nutriment,type) 
        return data 
    
    
    def Get_Select_Name(self):
        bacterie = self.data['Souche Name'].unique()
        phylum = self.data['phylum'].unique()
        nutriment = self.data['ImpExp'].str.extract(r'_(.*?)_')
        return bacterie,phylum,nutriment[0].unique()
                
        
          