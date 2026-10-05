from processamento import converter
from Numero import Numero
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))


def _convert(base_atual, valor_atual, base_nova):
    numero = Numero(base_atual, valor_atual, base_nova, "")
    converter(numero)
    return numero.valor_novo


def test_positive_integer_convertions():
    assert _convert(10, "456", 3) == "121220"
    assert _convert(8, "765432", 4) == "332230122"
    assert _convert(9, "45678", 10) == "30446"
    assert _convert(10, "45678", 10) == "45678"
    assert _convert(36, "fedCBA9", 24) == "K00A4199"
    assert _convert(62, "Ab3xY", 61) == "BItZL"
    assert _convert(62, "Ab3xY", 62) == "Ab3xY"


def test_negative_integer_convertions():
    assert _convert(10, "-456", 3) == "-121220"
    assert _convert(16, "-1234AB", 2) == "-100100011010010101011"
    assert _convert(8, "-765432", 4) == "-332230122"
    assert _convert(9, "-45678", 10) == "-30446"
    assert _convert(10, "-45678", 10) == "-45678"
    assert _convert(36, "-fedCBA9", 24) == "-K00A4199"
    assert _convert(62, "-Ab3xY", 61) == "-BItZL"
    assert _convert(62, "-Ab3xY", 62) == "-Ab3xY"


def test_fractional_part_convertions():
    assert _convert(10, "0.47", 3) == "0.11020012"
    assert _convert(9, "0.45678", 10) == "0.51560568"
    assert _convert(10, "0.45678", 10) == "0.45678"
    assert _convert(62, "0.XYZxyz", 61) == "0.X10LtBOG"


def test_negative_fractional_part_convertions():
    assert _convert(10, "-0.47", 3) == "-0.11020012"
    assert _convert(9, "-0.45678", 10) == "-0.51560568"
    assert _convert(10, "-0.45678", 10) == "-0.45678"
    assert _convert(62, "-0.XYZxyz", 61) == "-0.X10LtBOG"


def test_float_convertions():
    assert _convert(16, "DEF.214", 3) == "11220010.01011120"
    assert _convert(16, "214.214", 3) == "201201.01011120"
    assert _convert(62, "xyzAB12.456", 34) == "1UTHEKEUO.283T2N2F"
    assert _convert(60, "fedcb2.CDqwer", 28) == "2B729GNA.5JN1F8ME"
    assert _convert(2, "101101.11001", 2) == "101101.11001"
    assert _convert(2, "101101.1100111111111111111", 2) == "101101.11001111"
    assert _convert(10, "6789.4321", 4) == "1222011.12322132"


def test_negative_float_convertions():
    assert _convert(16, "-DEF.214", 3) == "-11220010.01011120"
    assert _convert(16, "-214.214", 3) == "-201201.01011120"
    assert _convert(62, "-xyzAB12.456", 34) == "-1UTHEKEUO.283T2N2F"
    assert _convert(60, "-fedcb2.CDqwer", 28) == "-2B729GNA.5JN1F8ME"
    assert _convert(2, "-101101.11001", 2) == "-101101.11001"
    assert _convert(2, "-101101.11001111111111111111", 2) == "-101101.11001111"
    assert _convert(10, "-6789.4321", 4) == "-1222011.12322132"
