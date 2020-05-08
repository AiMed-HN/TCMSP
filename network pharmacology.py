#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import os


# In[ ]:


druglibrary = r"F:\myresearch\TCM\druglibrary"       ##药库目录
workpath = r"F:\myresearch\TCM\金花清感颗粒"       ##工作目录


# In[ ]:


os.chdir(workpath)


# In[ ]:


prescription = pd.read_table("prescription.txt",header=0)                ##药方文件，放在工作目录下，是一个一数列列的文本文件，表头为drug


# In[ ]:


prescription


# In[ ]:


ingredients = pd.DataFrame()
targets = pd.DataFrame()


# In[ ]:


for drug in prescription["drug"]:
    drugpath = os.path.join(druglibrary,drug)
    ingredient = drugpath+"\\ingredients.txt"
    ingredient = pd.read_table(ingredient,header=None,names=["Mol ID","Molecule Name","MW","AlogP","Hdon","Hacc","OB (%)","Caco-2","BBB","DL","FASA-","HL","Save"])
    target = drugpath+"\\targets.txt"
    target = pd.read_table(target,header=None,names=["Mol ID","Molecule name","Target name","Source","status"])
    ingredients = ingredients.append(ingredient)
    targets = targets.append(target)
    print(drug+"  添加完毕！")


# #### 生成的文件有表头，如果用perl脚本处理，需要去掉表头

# In[ ]:


ingredients.to_csv("ingredients.txt",sep="\t",index=0)
targets.to_csv("targets.txt",sep = "\t",index = 0)


# In[ ]:


targets.shape


# In[ ]:


ingredients.shape


# In[ ]:


targetName = targets[targets["Mol ID"].apply(lambda x:x in list(ingredients["Mol ID"]))].iloc[:,0:3]


# In[ ]:


targetName.shape


# In[ ]:


targetName.to_csv("targetName.txt",sep = "\t",index = 0)


# #### 以下为调试代码

# In[ ]:


uniprot = pd.read_table("uniprot.tsv",header=0)


# In[ ]:


uniprot


# In[ ]:


targetName.head()


# In[ ]:


"NF-kappa-B inhibitor alpha" in list(uniprot["Protein names"])


# In[ ]:


uniprot[uniprot["Protein names"] == "NF-kappa-B inhibitor alpha"]


# #### 以下为执行完addSymbol后执行

# In[ ]:


targetSymbol = pd.read_table("TargetSymbol.txt",header=0)


# In[ ]:


targetSymbol


# In[ ]:


targetSymbol["Symbol"].to_csv("Drug.txt",header = None,index = 0)


# In[ ]:


targetSymbol["Symbol"].shape


# In[ ]:


targetSymbol["MolName"].to_csv("mol.txt",header = None,index = 0)


# In[ ]:





# In[ ]:


disease = pd.read_csv("GeneCards-SearchResults(SarsCov2).csv")


# In[ ]:


disease["Gene Symbol"].to_csv("Disease.txt",header = None,index = 0)


# In[ ]:


disease.shape


# In[ ]:


targetSymbol["Symbol"]


# In[ ]:


disease["Gene Symbol"]


# In[ ]:


drug_disease_1 = pd.DataFrame(set(targetSymbol["Symbol"]).intersection(set(disease["Gene Symbol"])))


# In[ ]:


drug_disease_1.to_csv("drug_disease_1.txt",header = None,index = 0)


# In[ ]:


DD = pd.read_table("Drug_Disease.txt",header = None)


# In[ ]:


DD


# In[ ]:


targetSymbol["Symbol"].drop_duplicates().shape


# In[ ]:


len(set(targetSymbol["Symbol"]))


# In[ ]:


go_bp = pd.read_table("enrichment.Process_BP.tsv",header=0)


# In[ ]:


go_mf = pd.read_table("enrichment.Function_MF.tsv",header=0)


# In[ ]:


go_cc = pd.read_table("enrichment.Component_CC.tsv",header=0)


# In[ ]:


go_bp


# In[ ]:




