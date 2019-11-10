import os
import json
import pandas as pd
import numpy as np
from functools import partial
from collections import defaultdict

QUALIFICATION_THRESHOLD = 3

def searchDisease(inquiry):
    onehot_database = np.array(pd.read_csv("./diseaseDataset/oneHotdiseaseArray.csv", header=None))
    disease_list    = np.array(pd.read_csv("./diseaseDataset/DiseaseList.csv", header=None))
    symptom_list    = np.array(pd.read_csv("./diseaseDataset/SymptomList.csv", header=None))

    one_hot = np.zeros(len(symptom_list))
    one_hot[inquiry.get("Symptoms")] = 1

    score_matrix = np.matmul(onehot_database, one_hot)
    max_score_idxs = np.where(score_matrix == max(score_matrix))
    # print(max_score_idxs, score_matrix)
    if (inquiry.get("Self_Diag") in disease_list[max_score_idxs]):
        idx = list(np.where(disease_list == inquiry.get("Self_Diag")))
        diagnosis = disease_list[idx]
    else:
        diagnosis = disease_list[max_score_idxs[0]]
    print(diagnosis, max_score_idxs, score_matrix)

    return searchDoc(inquiry, diagnosis)

def searchDoc(inquiry, diagnosis):
    patient_local = inquiry.get("Location")
    patient_selfDiag = inquiry.get("Self_Diag")
    patient_symptoms = inquiry.get("Symptoms")

    with open("./diseaseDataset/DocDictionary.json") as json_file:
        doctor_dict = json.load(json_file)

    outstate_candidates = []
    instate_candidates  = []

    def helper(doctor_info, disease):
        idx = doctor_info["Symptoms"].index(disease)
        return doctor_info["Rating"][idx]

    for k, v in doctor_dict.items():
        doctor_name = k
        doctor_file = v[0]
        # print(diagnosis, doctor_file["Symptoms"])
        if (diagnosis in doctor_file["Symptoms"]):
            idx = doctor_file["Symptoms"].index(diagnosis)
            rating = doctor_file["Rating"][idx]
            if rating > QUALIFICATION_THRESHOLD:
                if patient_local == doctor_file["Location"]:
                    instate_candidates.append(doctor_file)
                else:
                    outstate_candidates.append(doctor_file)

    if instate_candidates != []:
        instate_candidates = sorted(instate_candidates, key = lambda candidate: candidate["Rating"][candidate["Symptoms"].index(diagnosis)], reverse = True)
    
    if outstate_candidates != []:
        outstate_candidates = sorted(outstate_candidates, key = lambda candidate: candidate["Rating"][candidate["Symptoms"].index(diagnosis)], reverse = True)

    if len(instate_candidates) >= 3:
        instate_candidates = instate_candidates[: 3]
    
    if len(outstate_candidates) >= 3:
        outstate_candidates = outstate_candidates[: 3]

    return [instate_candidates + outstate_candidates, diagnosis]

# if __name__ == "__main__":
#     inquiry = {
#         "Symptoms": [27, 110, 37, 85, 38],
#         "Location": "Texas",
#         "Self_Diag": "Hand eczema"
#     }
#     recommondations = searchDisease(inquiry)
#     print(recommondations)