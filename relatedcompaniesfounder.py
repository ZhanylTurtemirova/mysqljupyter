import pandas as pd
class CompaniesSearcher:
    def __init__(self,db_connection):
            self.db_connection = db_connection  
            
    def find_companies_by_name(self,name):
        query="SELECT FullNameRu, Founders FROM Minjust2018 WHERE FullNameRu LIKE '%"+name+"%' LIMIT 0, 20"
        df = pd.read_sql_query(query,self.db_connection)
        return df

    def find_companies_by_founder(self,founder, nosearch):
            df = pd.read_sql_query(
            "SELECT FullNameRu FROM Minjust2018 WHERE Founders LIKE '%"+ founder +"%' AND FullNameRu <> '"+nosearch+"' LIMIT 0, 10",
            self.db_connection)
            return df.values.tolist()
        
    def find_companies_by_founders_string(self,company_with_founders):
            founders_list = company_with_founders[1].split(',')
            data = {}
            for i, founder in enumerate(founders_list):
                   data[founder] = self.find_companies_by_founder(founder, company_with_founders[0])
            return data

    def find_related_companies_by_founders(self,companies_dataframe):
            companies_array = companies_dataframe.values
            companies_list = list(map(self.find_companies_by_founders_string, companies_array))
            data = {}
            for i, company in enumerate(companies_array):
                data[company[0]] = companies_list[i]
            return data
    
    def find_companies_related_to_companies_via_founders(self,companies):
            frames = []
            for company in companies:
                frames.append(self.find_companies_by_name(company))
            df = pd.concat(frames) 
            return self.find_related_companies_by_founders(df)

