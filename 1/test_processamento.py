from string.templatelib import convert

from processamento import converter
from Numero import Numero
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))


def test_positive_integer_convertions():
    assert convert(10, "123", 3) == "11120"
    assert convert(16, "ABCDEF", 2) == "101010111100110111101111"
    assert convert(8, "123456", 4) == "22130232"
    assert convert(9, "32145", 10) == "21263"
    assert convert(10, "32145", 10) == "32145"
    assert convert(62, "zedA4", 61) == "14miRW"
    assert convert(62, "zedA4", 62) == "zedA4"

def test_negative_integer_convertions():
    assert convert(10, "-123", 3) == "-11120"
    assert convert(16, "-ABCDEF", 2) == "-101010111100110111101111"
    assert convert(8, "-123456", 4) == "-22130232"
    assert convert(9, "-32145", 10) == "-21263"
    assert convert(10, "-32145", 10) == "-32145"
    assert convert(62, "-zedA4", 61) == "-14miRW"
    assert convert(62, "-zedA4", 62) == "-zedA4"

def test_fractional_part_convertions():
    assert convert(10, "0.33", 3) == "0.02222012"
    assert convert(9, "0.32145", 10) == "0.36009077"
    assert convert(10, "0.32145", 10) == "0.32145"
    assert convert(62, "0.ABCabc", 61) == "0.A10LtBj8"

def test_negative_fractional_part_convertions():
    assert convert(10, "-0.33", 3) == "-0.02222012"
    assert convert(9, "-0.32145", 10) == "-0.36009077"
    assert convert(10, "-0.32145", 10) == "-0.32145"
    assert convert(62, "-0.ABCabc", 61) == "-0.A10LtBj8"

def test_float_convertions():
    assert convert(16, "ABC.325", 3) == "10202210.01202202"
    assert convert(16, "325.325", 3) == "1002211.01202202"
    assert convert(62, "abcedf13.123", 34) == "246EQSLCLB.0J8TV063"
    assert convert(60, "abcde1.ABasdf", 28) == "232P72HL.4L5DMOLO"
    assert convert(2, "111010.10101", 2) == "111010.10101"
    assert convert(2, "111010.10101111111111111111", 2) == "111010.10101111"
    assert convert(10, "3456.7778", 4) == "312000.30130131"

def test_negative_float_convertions():
    assert convert(16, "-ABC.325", 3) == "-10202210.01202202"
    assert convert(16, "-325.325", 3) == "-1002211.01202202"
    assert convert(62, "-abcedf13.123", 34) == "-246EQSLCLB.0J8TV063"
    assert convert(60, "-abcde1.ABasdf", 28) == "-232P72HL.4L5DMOLO"
    assert convert(2, "-111010.10101", 2) == "-111010.10101"
    assert convert(2, "-111010.10101111111111111111", 2) == "-111010.10101111"
    assert convert(10, "-3456.7778", 4) == "-312000.30130131"