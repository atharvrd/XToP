import matplotlib.pyplot as plt


def create_revenue_chart(revenue_df):

    plt.figure(figsize=(8, 4))

    plt.plot(
        revenue_df["Month"],
        revenue_df["Revenue"],
        marker="o",
        linewidth=3
    )

    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.grid(True)

    chart_path = "output/revenue_chart.png"

    plt.savefig(chart_path, bbox_inches="tight")
    plt.close()

    return chart_path


def create_region_chart(regional_df):

    plt.figure(figsize=(6, 6))

    plt.pie(
        regional_df["Revenue"],
        labels=regional_df["Region"],
        autopct="%1.1f%%"
    )

    plt.title("Regional Revenue Distribution")

    chart_path = "output/region_chart.png"

    plt.savefig(chart_path, bbox_inches="tight")
    plt.close()

    return chart_path


def create_product_chart(products_df):

    plt.figure(figsize=(8, 4))

    plt.bar(
        products_df["Product"],
        products_df["Revenue"]
    )

    plt.title("Product Revenue")

    chart_path = "output/product_chart.png"

    plt.savefig(chart_path, bbox_inches="tight")
    plt.close()

    return chart_path