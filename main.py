# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
Created on Sep 30, 2016

@author: luan vu
'''
from docx import Document

def main():
    document = Document('E:/Downloads/NGANH LUAT/CONG PHAP QUOC TE - 4TC.docx')
    parse_paragraphs(document)
    parse_tables(document)
def parse_paragraphs(document):
    for paragraph in document.paragraphs:
        if not paragraph.text or not paragraph.text.strip():
            continue
        print paragraph.text.encode('UTF-8')
def parse_tables(document):
    pass
if __name__ == '__main__':
    main()