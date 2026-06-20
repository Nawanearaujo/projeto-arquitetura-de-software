import pandas as pd
import os

def ingest_heart_data(raw_file_path: str, processed_path: str) -> pd.DataFrame:

    try:
        df = pd.read_csv(raw_file_path)
        
        os.makedirs(os.path.dirname(processed_path), exist_ok=True)
        df.to_csv(processed_path, index=False)
        
        print(f"Dataset carregado com sucesso. Registros: {len(df)}")
        return df
    except Exception as e:
        print(f"Erro na ingestão: {e}")
        return None

if __name__ == "__main__":
    ingest_heart_data("data/raw/heart.csv", "data/raw/heart_disease_raw.csv")