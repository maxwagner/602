# Max Wagner
# Not overly complicated, but I think it does the job just fine for a wikipedia page.
# I played with being more specific when grabbing text from the page, but in this form it should analyze any page.

from tkFileDialog import askopenfilename
import pandas

def getfile():
    Tk().withdraw()
    csvfile = askopenfilename()
    return csvfile


if __name__ == "__main__":