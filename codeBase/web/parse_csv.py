import pandas as pd
import json


df_symps = pd.read_csv("data/SymptomList.csv", header=None)
symp_id_map = { name: i for i, name in enumerate(df_symps.loc[:, 0]) }
del df_symps


result = {}

symp_class = {
    "upper_symps_list": ["Otolaryngology", "Thoracic"],
    "lower_symps_list": ["Gynaecology", "Urology"],
    "skin_symps_list": ["Dermatology"],
    "general_symps_list": ["Endocrinology"]
}

for cat, file_name_list in symp_class.items():
    cat_symps = set()
    for fname in file_name_list:
        df_disease_symp = pd.read_csv(f"data/{fname}.csv")
        for symp in df_disease_symp.loc[:, 'symptoms']:
            cat_symps.add(symp.lower())
    result[cat] = [{ "name": symp, "code": symp_id_map[symp] } for symp in sorted(cat_symps)]

with open("static/js/symptoms.json", "w") as fout:
    json.dump(result, fout)