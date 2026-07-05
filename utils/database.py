import pandas as pd
import os

class Database:

    def __init__(self, path):
        self.path = path
        self.ensure_file()

    def ensure_file(self):
        folder = os.path.dirname(self.path)
        if folder:
            os.makedirs(folder, exist_ok=True)

        if not os.path.exists(self.path):
            pd.DataFrame().to_csv(self.path, index=False)

    def load(self):
    import pandas as pd

    if not os.path.exists(self.path):
        return pd.DataFrame()

    if os.path.getsize(self.path) == 0:
        return pd.DataFrame()

    try:
        return pd.read_csv(self.path)
    except pd.errors.EmptyDataError:
        return pd.DataFrame()

    def save(self, df):
        df.to_csv(self.path, index=False)

    def insert(self, data: dict):
        df = self.load()
        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
        self.save(df)
        return True

    def update(self, condition_col, condition_val, updates: dict):
        df = self.load()

        if df.empty:
            return False

        mask = df[condition_col] == condition_val

        for key, value in updates.items():
            df.loc[mask, key] = value

        self.save(df)
        return True

    def delete(self, condition_col, condition_val):
        df = self.load()

        df = df[df[condition_col] != condition_val]

        self.save(df)
        return True

    def find(self, condition_col, condition_val):
        df = self.load()

        result = df[df[condition_col] == condition_val]

        return result
