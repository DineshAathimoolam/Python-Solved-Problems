dict1={'color':'purple','shape':'rectangle','phone':'Iqoo'}
dict2={'color':'violet','edge':'triangle','model':'vivo'}
dict1['Headset']='oneplus'
print(dict1)
#print(dict1['Headset'])
print('POP')
dict2.pop('edge')
print(dict2)
print('update')
dict1.update(dict2)
print(dict1)
print('Keys')
dict1.keys()
print(dict1)
print('-----------------------------------------')
thisDict={
    "Brand": "Honda",
    "Model": "city",
    "year": 2024
    }
thisDict["year"]=2023
print(thisDict["Model"])
thisDict.update({"Owner":"Dinesh"})
print(thisDict)
a=thisDict["Model"]
print(a)
thisDict.keys()
print(thisDict)
print("------------------------------------")


