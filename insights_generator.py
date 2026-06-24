def generate_insights(
    employees_df,
    revenue_df,
    products_df,
    regional_df
):

    insights = []

    # Revenue Growth

    start_revenue = revenue_df.iloc[0]["Revenue"]
    end_revenue = revenue_df.iloc[-1]["Revenue"]

    growth = (
        (end_revenue - start_revenue)
        / start_revenue
    ) * 100

    insights.append(
        f"Revenue grew by {growth:.1f}% from "
        f"{revenue_df.iloc[0]['Month']} "
        f"to "
        f"{revenue_df.iloc[-1]['Month']}."
    )

    # Top Performer

    top_employee = employees_df.loc[
        employees_df["Sales"].idxmax()
    ]

    insights.append(
        f"{top_employee['Name']} is the top performer "
        f"with sales of {top_employee['Sales']:,}."
    )

    # Best Region

    top_region = regional_df.loc[
        regional_df["Revenue"].idxmax()
    ]

    insights.append(
        f"{top_region['Region']} region generated "
        f"the highest revenue."
    )

    # Best Product

    top_product = products_df.loc[
        products_df["Revenue"].idxmax()
    ]

    insights.append(
        f"{top_product['Product']} contributes "
        f"the highest product revenue."
    )

    return insights