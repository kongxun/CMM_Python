# -*- coding: utf-8 -*-
__author__ = 'idbord'
from cmm.lexer import Lexer
from cmm.parser import Parser
from cmm.generator import Generator


def generator(path):
    result = []
    try:
        stream = open(path, 'r')
        codes = Generator.generate(Parser.parser_analysis(Lexer.lexer_analysis(stream)))
        stream.close()
        for i in codes:
            result.append(i.to_string())
        return result
    except Exception as e:
        print e

