def analyze_performance(employees_df):

    result = employees_df.copy()

    result["Achievement %"] = (
        result["Sales"] / result["Target"]
    ) * 100

    return result