from excel_reader import read_excel
from ppt_generator import create_ppt

df = read_excel("data/report.xlsx")

print(df.keys())

ppt = create_ppt(df)

ppt.save("output/report.pptx")

print("PPT Saved Successfully")