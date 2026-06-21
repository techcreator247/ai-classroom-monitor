import pandas as pd
import os

FILE = "attention_report.xlsx"

def save_report(data):

    df = pd.DataFrame(data)

    if os.path.exists(FILE):
        old = pd.read_excel(FILE)
        df = pd.concat([old, df], ignore_index=True)

    df.to_excel(FILE, index=False)