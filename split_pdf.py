#  pip install PyPDF2 (available on windows10)

import os
from PyPDF2 import PdfFileWriter, PdfFileReader

def split(pdf_file, delta, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not os.path.exists(pdf_file):
        return

    print('----------参数信息---------------')
    print('File:' + pdf_file)
    print('PageNums:' + str(delta))
    print('Dest:' + output_dir)
    print('-----------pdf开始切分-----------')
    file_name = pdf_file.split('/')[-1].split('.')[0]
    output_dir = os.path.join(out_dir, file_name)
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    input_stream = open(pdf_file, 'rb')
    pdf_input = PdfFileReader(input_stream)
    page_count = pdf_input.getNumPages()
    sum_page_count = int(page_count / (delta * 1.0))
    remind_page = page_count % delta
    for i in range(0, sum_page_count + 1):
        start = i * delta
        end = (i + 1) * delta
        pdf_out = PdfFileWriter()
        file_path = os.path.join(output_dir, os.path.split(pdf_file)[1]) #
        if i < sum_page_count:
            full_file_name = file_name + str(start + 1) + '-' + str(end) + ".pdf"
            file_path = os.path.join(output_dir, full_file_name)
            print(full_file_name + '切分完成')
            for j in range(start, end):
                page = pdf_input.getPage(j)
                pdf_out.addPage(page)
        else:
            full_file_name = file_name + str(start + 1) + '-' + str(start + remind_page) + ".pdf"
            file_path = os.path.join(output_dir, full_file_name)
            print(full_file_name + '切分完成')
            for j in range(delta * (sum_page_count), page_count):
                page = pdf_input.getPage(j)
                pdf_out.addPage(page)
        out_stream = open(file_path, 'wb')
        pdf_out.write(out_stream)
        out_stream.close()
    input_stream.close()
    print('-----------pdf切分完成-----------')

if __name__ == '__main__':
    pdf_path = 'CSAPP.pdf'
    page_count = 100
    out_dir = "result2"
    split(pdf_path, page_count, out_dir)
'''
    import sys
    
    #python splitPdf.py /Users/xxxxx/Downloads/UNIX网络编程卷1：套接字联网API(第3版).pdf 180 /Users/xxxxx/Documents/output

    try:
        pdf_path = sys.argv[1]
        page_count = int(sys.argv[2])
        out_dir = sys.argv[3]
        split(pdf_path, page_count, out_dir)
    except:
        pass
'''
