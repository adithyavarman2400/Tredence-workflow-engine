import pandas as pd


def profile_data(state):
    df = pd.DataFrame(state["data"])
    state["summary"] = df.describe().to_dict()
    state["df"] = df
    return state

def detect_anomalies(state):
    df_raw = state["df"]
    df = pd.DataFrame(df_raw).apply(pd.to_numeric, errors='coerce')

    numeric_cols = df.select_dtypes(include="number")
    anomalies = {}

    for col in numeric_cols.columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        outliers = df[(df[col] < lower) | (df[col] > upper)][col].tolist()
        anomalies[col] = outliers

    if "original_anomalies" not in state:
        state["original_anomalies"] = anomalies.copy()

    return state


def generate_rules(state):
    state["rules"] = {"action": "clip_outliers"}
    return state

def apply_rules(state):
    df_raw = state["df"]
    df = pd.DataFrame(df_raw).apply(pd.to_numeric, errors='coerce')

    for col, vals in state["original_anomalies"].items():
        if len(vals) > 0:
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)
            df[col] = df[col].clip(q1, q3)

    state["df"] = df.to_dict(orient="list")

    return state


NODES = {
    "profile_data": profile_data,
    "detect_anomalies": detect_anomalies,
    "generate_rules": generate_rules,
    "apply_rules": apply_rules
}

