import pandas as pd
import numpy as np

# data = pd.read_csv("venv\data\GeneralTraining.csv")
# diseases = 

class find_diseases():
    def diseases():
        data = pd.read_csv("venv\data\GeneralTraining.csv")
        diseases = data["prognosis"].unique()
        print(diseases)
        return diseases

def main():
    fd = find_diseases()
    return fd.diseases()



if __name__ == "__main__":
    main()