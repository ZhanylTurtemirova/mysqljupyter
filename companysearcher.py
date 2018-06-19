import pandas as pd
class Companysearcher:
    def __init__(self,db_connection):
            self.db_connection = db_connection       
            
    def find(self,name):
        query="SELECT FullNameRu, HeadName,Founders FROM Minjust2018 WHERE FullNameRu LIKE '%"+name+"%' LIMIT 0, 20"
        df = pd.read_sql_query(query,self.db_connection)
        return self.df_to_dictionary(df)
    
    def df_to_dictionary(self,df):
            companies={}
            companies_List=df.values.tolist()
            for company in companies_List:
                companies[company[0]]= company[-2:]
            return companies
    
   

