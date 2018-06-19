import pandas as pd
class FoundersSearcher:
    def __init__(self,db_connection):
        self.db_connection = db_connection
    
    def findCompaniesByFounder(self,name):
        query="SELECT  FullNameRu FROM Minjust2018 WHERE Founders LIKE '%"+name+"%' LIMIT 0, 10"
        df=pd.read_sql_query(query,self.db_connection)
        return df
    def find_foundersList_by_company(self,name):
        query="SELECT Founders FROM Minjust2018 WHERE FullNameRu LIKE '%"+name+"%' LIMIT 0, 10"
        df=pd.read_sql_query(query,self.db_connection)
        return df
    def find_related_founders_by_companies(self, companies):
        companies_arrayList=[]
        g= (list(companies.values))
        for t in g:
            companies_arrayList.append(t[0])
        companyList=[]
        for c in companies_arrayList:
            companyList.append(c[0])

        founders_arrayList=[]
        foundersList=[]
        founders_separatedList=[]
        for c in companyList:
            founders_arrayList.append((self.find_foundersList_by_company(c)).values[0])
        for f in founders_arrayList:
             foundersList.append(f[0].split(','))
        for f in foundersList:
            for x in f:
                founders_separatedList.append(x[0])
        return founders_separatedList
    
    def find_related_founders(self,name):
        companies=self.findCompaniesByFounder(name)
        founders_list=[]
        founders_list =self.find_related_founders_by_companies(companies)
        data={}
        data[name] = founders_list
        return data
    
    
    def find_founders(self,name):
        companies=self.findCompaniesByFounder(name)
        d=[]
        p=[]
        f1=[]
        f2=[]
        g= (list(companies.values))
        for t in g:
            d.append(t[0])
        for c in d:
            p.append((self.find_foundersList_by_company(c)).values[0])
        for x in p:
            f1.append(x[0].split(','))

        for f in f1:
            for q in f:
                f2.append(q)
        data={}
        data[name]=f2
        return data

        
    
    
 