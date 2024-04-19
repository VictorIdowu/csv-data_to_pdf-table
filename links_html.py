from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.set_font('helvetica', size=20)
pdf.write(5, "To find out what's new in tutorial, Click ")
pdf.set_font(style='U')
link = pdf.add_link(page=2)
pdf.write(5, "here", link)

# second page
pdf.add_page()
pdf.image("logo.png", 10, 10, 50, 0, "", "https://github.com/VictorIdowu")
pdf.set_left_margin(60)
pdf.set_font('helvetica', size=18)
pdf.write_html(""" You can add any html code in here <b>This text is bold</b> <h1>This is a heading</h1> <a href="https://github.com/VictorIdowu">My Github</a> """)

pdf.output('tutorial.pdf')