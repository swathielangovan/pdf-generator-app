from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P",unit="mm",format="A4")
df = pd.read_csv("topics.csv")
for index,row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times",style="B",size=12)
    pdf.set_text_color(100,100,100)
    pdf.cell(w =10, h=12,txt=row['Topic'],align="L", ln=1,border=0)
    for y in range(20,298,10):
        pdf.line(10,y,200,y)


    # pdf.set_font(family="Times",style="I",size=10)
    # pdf.cell(w=10,h=12,txt="Rough notes",align="L",ln=1,border=1)

    #set the footer
    pdf.ln(265)
    pdf.set_font(family="Times",style="I",size=8)
    pdf.set_text_color(200,200,200)
    pdf.cell(w=0,h=10,txt=row["Topic"],align="R")

    for i in range(row["Pages"]-1):
        pdf.add_page()

        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(200, 200, 200)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output1.pdf")