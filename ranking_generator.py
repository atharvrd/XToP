def get_employee_ranking(employees_df):

    ranking = employees_df.sort_values(
        by="Sales",
        ascending=False
    )

    return ranking