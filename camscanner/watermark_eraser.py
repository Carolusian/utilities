# -*- coding: utf-8 -*-
import os
import argparse
from PyPDF2 import PdfFileReader, PdfFileWriter

BASE_PATH = os.path.dirname(os.path.realpath(__file__))


def main():
    # get arguments
    parser = argparse.ArgumentParser(
        description='remove watermark from PDFs produced by CamScanner'
    )
    parser.add_argument('input_path', help='input file path.')
    parser.add_argument('output_path', help='output file path.')
    args = parser.parse_args()

     
    in_pdf = PdfFileReader(open(args.input_path, 'rb'))
    out_pdf = PdfFileWriter()

    # merge the cover and the file
    page_count = in_pdf.getNumPages()
    for page_num in range(page_count):
        in_page = in_pdf.getPage(page_num)
        in_page.mediaBox.lowerLeft = (in_page.mediaBox.getLowerLeft_x(), 45)
        out_pdf.addPage(in_page)

    with open(args.output_path, 'wb') as output_stream:
        out_pdf.write(output_stream)


if __name__ == '__main__':
    main()

