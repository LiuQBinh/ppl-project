# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\177")
        buf.write("\u0216\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\3\2\6\2j\n\2\r\2\16\2k\3\2\3\2\3\3\3\3\3\3\3\3\5\3t\n")
        buf.write("\3\3\3\3\3\7\3x\n\3\f\3\16\3{\13\3\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\5\5\5\u0084\n\5\3\6\3\6\3\6\5\6\u0089\n\6\3\6\3")
        buf.write("\6\3\6\3\7\5\7\u008f\n\7\3\7\5\7\u0092\n\7\3\7\3\7\3\7")
        buf.write("\3\7\5\7\u0098\n\7\3\7\3\7\3\b\5\b\u009d\n\b\3\b\5\b\u00a0")
        buf.write("\n\b\3\b\3\b\5\b\u00a4\n\b\3\b\3\b\3\b\5\b\u00a9\n\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\7\t\u00b1\n\t\f\t\16\t\u00b4\13")
        buf.write("\t\3\t\5\t\u00b7\n\t\3\n\3\n\3\n\5\n\u00bc\n\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\5\13\u00c4\n\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00cf\n\13\5\13\u00d1")
        buf.write("\n\13\3\13\3\13\5\13\u00d5\n\13\3\f\3\f\3\f\7\f\u00da")
        buf.write("\n\f\f\f\16\f\u00dd\13\f\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\5\16\u00e7\n\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\5\17\u00f0\n\17\3\17\3\17\3\20\3\20\3\20\3\20\5")
        buf.write("\20\u00f8\n\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\7\21\u0105\n\21\f\21\16\21\u0108\13\21")
        buf.write("\3\21\3\21\5\21\u010c\n\21\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\5\23\u011e\n\23\3\23\3\23\5\23\u0122\n\23\3\23\5\23\u0125")
        buf.write("\n\23\3\24\3\24\3\24\3\25\3\25\3\25\5\25\u012d\n\25\3")
        buf.write("\25\3\25\3\26\3\26\3\26\5\26\u0134\n\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\31\5\31\u013d\n\31\3\31\3\31\3\32\3")
        buf.write("\32\5\32\u0143\n\32\3\33\3\33\3\34\3\34\3\34\7\34\u014a")
        buf.write("\n\34\f\34\16\34\u014d\13\34\3\35\3\35\3\36\3\36\3\36")
        buf.write("\7\36\u0154\n\36\f\36\16\36\u0157\13\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\5\37\u015f\n\37\3 \3 \3 \7 \u0164\n \f")
        buf.write(" \16 \u0167\13 \3!\3!\3\"\3\"\3\"\3\"\3\"\5\"\u0170\n")
        buf.write("\"\3#\3#\3#\3#\3#\5#\u0177\n#\3$\3$\3$\3$\3$\5$\u017e")
        buf.write("\n$\3%\3%\3%\3%\3%\3%\7%\u0186\n%\f%\16%\u0189\13%\3&")
        buf.write("\3&\3&\3&\3&\3&\7&\u0191\n&\f&\16&\u0194\13&\3\'\3\'\3")
        buf.write("\'\5\'\u0199\n\'\3(\3(\3(\5(\u019e\n(\3)\3)\3)\3)\3)\3")
        buf.write(")\3)\3)\6)\u01a8\n)\r)\16)\u01a9\7)\u01ac\n)\f)\16)\u01af")
        buf.write("\13)\3*\3*\3*\3*\3*\3*\3*\3*\5*\u01b9\n*\3*\5*\u01bc\n")
        buf.write("*\7*\u01be\n*\f*\16*\u01c1\13*\3+\3+\3+\3+\3+\5+\u01c8")
        buf.write("\n+\3+\5+\u01cb\n+\3+\5+\u01ce\n+\3,\3,\3,\3,\5,\u01d4")
        buf.write("\n,\3,\3,\3,\5,\u01d9\n,\3-\3-\3-\3-\3-\5-\u01e0\n-\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3.\3.\5.\u01ec\n.\3/\3/\3/\7/\u01f1")
        buf.write("\n/\f/\16/\u01f4\13/\3\60\3\60\3\60\5\60\u01f9\n\60\3")
        buf.write("\60\3\60\3\61\3\61\3\61\7\61\u0200\n\61\f\61\16\61\u0203")
        buf.write("\13\61\3\62\3\62\3\62\5\62\u0208\n\62\3\62\3\62\3\63\3")
        buf.write("\63\3\63\7\63\u020f\n\63\f\63\16\63\u0212\13\63\3\64\3")
        buf.write("\64\3\64\2\6HJPR\65\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdf\2\f")
        buf.write("\6\2\4\4\37\37##MM\4\2\37\37##\3\2\t\n\4\2\22\22\24\24")
        buf.write("\3\2\32\35\3\2\62\63\3\2,\61\3\2*+\3\2$%\3\2&(\2\u0230")
        buf.write("\2i\3\2\2\2\4o\3\2\2\2\6~\3\2\2\2\b\u0083\3\2\2\2\n\u0085")
        buf.write("\3\2\2\2\f\u008e\3\2\2\2\16\u009c\3\2\2\2\20\u00b6\3\2")
        buf.write("\2\2\22\u00bb\3\2\2\2\24\u00d4\3\2\2\2\26\u00d6\3\2\2")
        buf.write("\2\30\u00de\3\2\2\2\32\u00e6\3\2\2\2\34\u00e8\3\2\2\2")
        buf.write("\36\u00f3\3\2\2\2 \u00fb\3\2\2\2\"\u010d\3\2\2\2$\u0121")
        buf.write("\3\2\2\2&\u0126\3\2\2\2(\u0129\3\2\2\2*\u0133\3\2\2\2")
        buf.write(",\u0135\3\2\2\2.\u0137\3\2\2\2\60\u0139\3\2\2\2\62\u0142")
        buf.write("\3\2\2\2\64\u0144\3\2\2\2\66\u0146\3\2\2\28\u014e\3\2")
        buf.write("\2\2:\u0150\3\2\2\2<\u015e\3\2\2\2>\u0160\3\2\2\2@\u0168")
        buf.write("\3\2\2\2B\u016f\3\2\2\2D\u0176\3\2\2\2F\u017d\3\2\2\2")
        buf.write("H\u017f\3\2\2\2J\u018a\3\2\2\2L\u0198\3\2\2\2N\u019d\3")
        buf.write("\2\2\2P\u019f\3\2\2\2R\u01b0\3\2\2\2T\u01cd\3\2\2\2V\u01d8")
        buf.write("\3\2\2\2X\u01df\3\2\2\2Z\u01eb\3\2\2\2\\\u01ed\3\2\2\2")
        buf.write("^\u01f5\3\2\2\2`\u01fc\3\2\2\2b\u0204\3\2\2\2d\u020b\3")
        buf.write("\2\2\2f\u0213\3\2\2\2hj\5\4\3\2ih\3\2\2\2jk\3\2\2\2ki")
        buf.write("\3\2\2\2kl\3\2\2\2lm\3\2\2\2mn\7\2\2\3n\3\3\2\2\2op\7")
        buf.write("\3\2\2ps\5\6\4\2qr\7\5\2\2rt\5\6\4\2sq\3\2\2\2st\3\2\2")
        buf.write("\2tu\3\2\2\2uy\7w\2\2vx\5\b\5\2wv\3\2\2\2x{\3\2\2\2yw")
        buf.write("\3\2\2\2yz\3\2\2\2z|\3\2\2\2{y\3\2\2\2|}\7x\2\2}\5\3\2")
        buf.write("\2\2~\177\t\2\2\2\177\7\3\2\2\2\u0080\u0084\5\f\7\2\u0081")
        buf.write("\u0084\5\16\b\2\u0082\u0084\5\n\6\2\u0083\u0080\3\2\2")
        buf.write("\2\u0083\u0081\3\2\2\2\u0083\u0082\3\2\2\2\u0084\t\3\2")
        buf.write("\2\2\u0085\u0086\5\6\4\2\u0086\u0088\7s\2\2\u0087\u0089")
        buf.write("\5:\36\2\u0088\u0087\3\2\2\2\u0088\u0089\3\2\2\2\u0089")
        buf.write("\u008a\3\2\2\2\u008a\u008b\7t\2\2\u008b\u008c\5\20\t\2")
        buf.write("\u008c\13\3\2\2\2\u008d\u008f\7\6\2\2\u008e\u008d\3\2")
        buf.write("\2\2\u008e\u008f\3\2\2\2\u008f\u0091\3\2\2\2\u0090\u0092")
        buf.write("\7\7\2\2\u0091\u0090\3\2\2\2\u0091\u0092\3\2\2\2\u0092")
        buf.write("\u0093\3\2\2\2\u0093\u0094\5.\30\2\u0094\u0097\5\\/\2")
        buf.write("\u0095\u0096\7\21\2\2\u0096\u0098\5Z.\2\u0097\u0095\3")
        buf.write("\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a")
        buf.write("\7y\2\2\u009a\r\3\2\2\2\u009b\u009d\7\6\2\2\u009c\u009b")
        buf.write("\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009f\3\2\2\2\u009e")
        buf.write("\u00a0\7\7\2\2\u009f\u009e\3\2\2\2\u009f\u00a0\3\2\2\2")
        buf.write("\u00a0\u00a3\3\2\2\2\u00a1\u00a4\5.\30\2\u00a2\u00a4\7")
        buf.write("\b\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a2\3\2\2\2\u00a4\u00a5")
        buf.write("\3\2\2\2\u00a5\u00a6\t\3\2\2\u00a6\u00a8\7s\2\2\u00a7")
        buf.write("\u00a9\5:\36\2\u00a8\u00a7\3\2\2\2\u00a8\u00a9\3\2\2\2")
        buf.write("\u00a9\u00aa\3\2\2\2\u00aa\u00ab\7t\2\2\u00ab\u00ac\5")
        buf.write("\20\t\2\u00ac\17\3\2\2\2\u00ad\u00b7\5\22\n\2\u00ae\u00b2")
        buf.write("\7w\2\2\u00af\u00b1\5\22\n\2\u00b0\u00af\3\2\2\2\u00b1")
        buf.write("\u00b4\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2")
        buf.write("\u00b3\u00b5\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b5\u00b7\7")
        buf.write("x\2\2\u00b6\u00ad\3\2\2\2\u00b6\u00ae\3\2\2\2\u00b7\21")
        buf.write("\3\2\2\2\u00b8\u00bc\5\32\16\2\u00b9\u00bc\5\24\13\2\u00ba")
        buf.write("\u00bc\5\26\f\2\u00bb\u00b8\3\2\2\2\u00bb\u00b9\3\2\2")
        buf.write("\2\u00bb\u00ba\3\2\2\2\u00bc\23\3\2\2\2\u00bd\u00be\t")
        buf.write("\4\2\2\u00be\u00bf\5\\/\2\u00bf\u00c0\7\66\2\2\u00c0\u00c3")
        buf.write("\5*\26\2\u00c1\u00c2\7\21\2\2\u00c2\u00c4\5> \2\u00c3")
        buf.write("\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c5\3\2\2\2")
        buf.write("\u00c5\u00c6\7y\2\2\u00c6\u00d5\3\2\2\2\u00c7\u00d0\5")
        buf.write(":\36\2\u00c8\u00c9\7\66\2\2\u00c9\u00ca\7\21\2\2\u00ca")
        buf.write("\u00ce\3\2\2\2\u00cb\u00cf\5@!\2\u00cc\u00cf\5\36\20\2")
        buf.write("\u00cd\u00cf\5$\23\2\u00ce\u00cb\3\2\2\2\u00ce\u00cc\3")
        buf.write("\2\2\2\u00ce\u00cd\3\2\2\2\u00cf\u00d1\3\2\2\2\u00d0\u00c8")
        buf.write("\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2")
        buf.write("\u00d3\7y\2\2\u00d3\u00d5\3\2\2\2\u00d4\u00bd\3\2\2\2")
        buf.write("\u00d4\u00c7\3\2\2\2\u00d5\25\3\2\2\2\u00d6\u00db\5\30")
        buf.write("\r\2\u00d7\u00d8\7{\2\2\u00d8\u00da\5\30\r\2\u00d9\u00d7")
        buf.write("\3\2\2\2\u00da\u00dd\3\2\2\2\u00db\u00d9\3\2\2\2\u00db")
        buf.write("\u00dc\3\2\2\2\u00dc\27\3\2\2\2\u00dd\u00db\3\2\2\2\u00de")
        buf.write("\u00df\7#\2\2\u00df\31\3\2\2\2\u00e0\u00e7\5\34\17\2\u00e1")
        buf.write("\u00e7\5 \21\2\u00e2\u00e7\5\"\22\2\u00e3\u00e7\5&\24")
        buf.write("\2\u00e4\u00e7\5(\25\2\u00e5\u00e7\5$\23\2\u00e6\u00e0")
        buf.write("\3\2\2\2\u00e6\u00e1\3\2\2\2\u00e6\u00e2\3\2\2\2\u00e6")
        buf.write("\u00e3\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e5\3\2\2\2")
        buf.write("\u00e7\33\3\2\2\2\u00e8\u00e9\5P)\2\u00e9\u00ea\7\66\2")
        buf.write("\2\u00ea\u00eb\7\21\2\2\u00eb\u00ef\3\2\2\2\u00ec\u00f0")
        buf.write("\5@!\2\u00ed\u00f0\5\36\20\2\u00ee\u00f0\5$\23\2\u00ef")
        buf.write("\u00ec\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00ee\3\2\2\2")
        buf.write("\u00f0\u00f1\3\2\2\2\u00f1\u00f2\7y\2\2\u00f2\35\3\2\2")
        buf.write("\2\u00f3\u00f4\7\13\2\2\u00f4\u00f5\5\6\4\2\u00f5\u00f7")
        buf.write("\7s\2\2\u00f6\u00f8\5> \2\u00f7\u00f6\3\2\2\2\u00f7\u00f8")
        buf.write("\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u00fa\7t\2\2\u00fa")
        buf.write("\37\3\2\2\2\u00fb\u00fc\7\f\2\2\u00fc\u00fd\5@!\2\u00fd")
        buf.write("\u00fe\7\r\2\2\u00fe\u00ff\5\20\t\2\u00ff\u0106\3\2\2")
        buf.write("\2\u0100\u0101\7\17\2\2\u0101\u0102\5@!\2\u0102\u0103")
        buf.write("\5\20\t\2\u0103\u0105\3\2\2\2\u0104\u0100\3\2\2\2\u0105")
        buf.write("\u0108\3\2\2\2\u0106\u0104\3\2\2\2\u0106\u0107\3\2\2\2")
        buf.write("\u0107\u010b\3\2\2\2\u0108\u0106\3\2\2\2\u0109\u010a\7")
        buf.write("\16\2\2\u010a\u010c\5\20\t\2\u010b\u0109\3\2\2\2\u010b")
        buf.write("\u010c\3\2\2\2\u010c!\3\2\2\2\u010d\u010e\7\20\2\2\u010e")
        buf.write("\u010f\7#\2\2\u010f\u0110\7\66\2\2\u0110\u0111\7\21\2")
        buf.write("\2\u0111\u0112\7:\2\2\u0112\u0113\3\2\2\2\u0113\u0114")
        buf.write("\t\5\2\2\u0114\u0115\7:\2\2\u0115\u0116\7\23\2\2\u0116")
        buf.write("\u0117\5\20\t\2\u0117#\3\2\2\2\u0118\u0122\5P)\2\u0119")
        buf.write("\u011a\7#\2\2\u011a\u011d\7s\2\2\u011b\u011e\5@!\2\u011c")
        buf.write("\u011e\5$\23\2\u011d\u011b\3\2\2\2\u011d\u011c\3\2\2\2")
        buf.write("\u011e\u011f\3\2\2\2\u011f\u0120\7t\2\2\u0120\u0122\3")
        buf.write("\2\2\2\u0121\u0118\3\2\2\2\u0121\u0119\3\2\2\2\u0122\u0124")
        buf.write("\3\2\2\2\u0123\u0125\7y\2\2\u0124\u0123\3\2\2\2\u0124")
        buf.write("\u0125\3\2\2\2\u0125%\3\2\2\2\u0126\u0127\7\25\2\2\u0127")
        buf.write("\u0128\7y\2\2\u0128\'\3\2\2\2\u0129\u012c\7\26\2\2\u012a")
        buf.write("\u012d\5@!\2\u012b\u012d\5$\23\2\u012c\u012a\3\2\2\2\u012c")
        buf.write("\u012b\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u012e\3\2\2\2")
        buf.write("\u012e\u012f\7y\2\2\u012f)\3\2\2\2\u0130\u0134\5.\30\2")
        buf.write("\u0131\u0134\5\60\31\2\u0132\u0134\5,\27\2\u0133\u0130")
        buf.write("\3\2\2\2\u0133\u0131\3\2\2\2\u0133\u0132\3\2\2\2\u0134")
        buf.write("+\3\2\2\2\u0135\u0136\5\6\4\2\u0136-\3\2\2\2\u0137\u0138")
        buf.write("\t\6\2\2\u0138/\3\2\2\2\u0139\u013a\5.\30\2\u013a\u013c")
        buf.write("\7u\2\2\u013b\u013d\5\64\33\2\u013c\u013b\3\2\2\2\u013c")
        buf.write("\u013d\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u013f\7v\2\2")
        buf.write("\u013f\61\3\2\2\2\u0140\u0143\5.\30\2\u0141\u0143\5\60")
        buf.write("\31\2\u0142\u0140\3\2\2\2\u0142\u0141\3\2\2\2\u0143\63")
        buf.write("\3\2\2\2\u0144\u0145\7:\2\2\u0145\65\3\2\2\2\u0146\u014b")
        buf.write("\58\35\2\u0147\u0148\7{\2\2\u0148\u014a\58\35\2\u0149")
        buf.write("\u0147\3\2\2\2\u014a\u014d\3\2\2\2\u014b\u0149\3\2\2\2")
        buf.write("\u014b\u014c\3\2\2\2\u014c\67\3\2\2\2\u014d\u014b\3\2")
        buf.write("\2\2\u014e\u014f\7#\2\2\u014f9\3\2\2\2\u0150\u0155\5<")
        buf.write("\37\2\u0151\u0152\7{\2\2\u0152\u0154\5<\37\2\u0153\u0151")
        buf.write("\3\2\2\2\u0154\u0157\3\2\2\2\u0155\u0153\3\2\2\2\u0155")
        buf.write("\u0156\3\2\2\2\u0156;\3\2\2\2\u0157\u0155\3\2\2\2\u0158")
        buf.write("\u0159\5*\26\2\u0159\u015a\5\\/\2\u015a\u015f\3\2\2\2")
        buf.write("\u015b\u015c\7#\2\2\u015c\u015d\7\66\2\2\u015d\u015f\5")
        buf.write("\6\4\2\u015e\u0158\3\2\2\2\u015e\u015b\3\2\2\2\u015f=")
        buf.write("\3\2\2\2\u0160\u0165\5@!\2\u0161\u0162\7{\2\2\u0162\u0164")
        buf.write("\5@!\2\u0163\u0161\3\2\2\2\u0164\u0167\3\2\2\2\u0165\u0163")
        buf.write("\3\2\2\2\u0165\u0166\3\2\2\2\u0166?\3\2\2\2\u0167\u0165")
        buf.write("\3\2\2\2\u0168\u0169\5B\"\2\u0169A\3\2\2\2\u016a\u016b")
        buf.write("\5D#\2\u016b\u016c\t\7\2\2\u016c\u016d\5D#\2\u016d\u0170")
        buf.write("\3\2\2\2\u016e\u0170\5D#\2\u016f\u016a\3\2\2\2\u016f\u016e")
        buf.write("\3\2\2\2\u0170C\3\2\2\2\u0171\u0172\5F$\2\u0172\u0173")
        buf.write("\t\b\2\2\u0173\u0174\5F$\2\u0174\u0177\3\2\2\2\u0175\u0177")
        buf.write("\5F$\2\u0176\u0171\3\2\2\2\u0176\u0175\3\2\2\2\u0177E")
        buf.write("\3\2\2\2\u0178\u0179\5H%\2\u0179\u017a\t\t\2\2\u017a\u017b")
        buf.write("\5H%\2\u017b\u017e\3\2\2\2\u017c\u017e\5H%\2\u017d\u0178")
        buf.write("\3\2\2\2\u017d\u017c\3\2\2\2\u017eG\3\2\2\2\u017f\u0180")
        buf.write("\b%\1\2\u0180\u0181\5J&\2\u0181\u0187\3\2\2\2\u0182\u0183")
        buf.write("\f\4\2\2\u0183\u0184\t\n\2\2\u0184\u0186\5J&\2\u0185\u0182")
        buf.write("\3\2\2\2\u0186\u0189\3\2\2\2\u0187\u0185\3\2\2\2\u0187")
        buf.write("\u0188\3\2\2\2\u0188I\3\2\2\2\u0189\u0187\3\2\2\2\u018a")
        buf.write("\u018b\b&\1\2\u018b\u018c\5L\'\2\u018c\u0192\3\2\2\2\u018d")
        buf.write("\u018e\f\4\2\2\u018e\u018f\t\13\2\2\u018f\u0191\5L\'\2")
        buf.write("\u0190\u018d\3\2\2\2\u0191\u0194\3\2\2\2\u0192\u0190\3")
        buf.write("\2\2\2\u0192\u0193\3\2\2\2\u0193K\3\2\2\2\u0194\u0192")
        buf.write("\3\2\2\2\u0195\u0196\7)\2\2\u0196\u0199\5L\'\2\u0197\u0199")
        buf.write("\5N(\2\u0198\u0195\3\2\2\2\u0198\u0197\3\2\2\2\u0199M")
        buf.write("\3\2\2\2\u019a\u019b\7%\2\2\u019b\u019e\5N(\2\u019c\u019e")
        buf.write("\5P)\2\u019d\u019a\3\2\2\2\u019d\u019c\3\2\2\2\u019eO")
        buf.write("\3\2\2\2\u019f\u01a0\b)\1\2\u01a0\u01a1\5R*\2\u01a1\u01ad")
        buf.write("\3\2\2\2\u01a2\u01a7\f\4\2\2\u01a3\u01a4\7u\2\2\u01a4")
        buf.write("\u01a5\5@!\2\u01a5\u01a6\7v\2\2\u01a6\u01a8\3\2\2\2\u01a7")
        buf.write("\u01a3\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01a7\3\2\2\2")
        buf.write("\u01a9\u01aa\3\2\2\2\u01aa\u01ac\3\2\2\2\u01ab\u01a2\3")
        buf.write("\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae")
        buf.write("\3\2\2\2\u01aeQ\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b1")
        buf.write("\b*\1\2\u01b1\u01b2\5T+\2\u01b2\u01bf\3\2\2\2\u01b3\u01b4")
        buf.write("\f\4\2\2\u01b4\u01b5\7\64\2\2\u01b5\u01bb\5T+\2\u01b6")
        buf.write("\u01b8\7s\2\2\u01b7\u01b9\5> \2\u01b8\u01b7\3\2\2\2\u01b8")
        buf.write("\u01b9\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01bc\7t\2\2")
        buf.write("\u01bb\u01b6\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01be\3")
        buf.write("\2\2\2\u01bd\u01b3\3\2\2\2\u01be\u01c1\3\2\2\2\u01bf\u01bd")
        buf.write("\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0S\3\2\2\2\u01c1\u01bf")
        buf.write("\3\2\2\2\u01c2\u01c3\5V,\2\u01c3\u01c4\7\65\2\2\u01c4")
        buf.write("\u01ca\5V,\2\u01c5\u01c7\7s\2\2\u01c6\u01c8\5> \2\u01c7")
        buf.write("\u01c6\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01c9\3\2\2\2")
        buf.write("\u01c9\u01cb\7t\2\2\u01ca\u01c5\3\2\2\2\u01ca\u01cb\3")
        buf.write("\2\2\2\u01cb\u01ce\3\2\2\2\u01cc\u01ce\5V,\2\u01cd\u01c2")
        buf.write("\3\2\2\2\u01cd\u01cc\3\2\2\2\u01ceU\3\2\2\2\u01cf\u01d0")
        buf.write("\7T\2\2\u01d0\u01d1\5V,\2\u01d1\u01d3\7s\2\2\u01d2\u01d4")
        buf.write("\5> \2\u01d3\u01d2\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d5")
        buf.write("\3\2\2\2\u01d5\u01d6\7t\2\2\u01d6\u01d9\3\2\2\2\u01d7")
        buf.write("\u01d9\5X-\2\u01d8\u01cf\3\2\2\2\u01d8\u01d7\3\2\2\2\u01d9")
        buf.write("W\3\2\2\2\u01da\u01db\7s\2\2\u01db\u01dc\5@!\2\u01dc\u01dd")
        buf.write("\7t\2\2\u01dd\u01e0\3\2\2\2\u01de\u01e0\5Z.\2\u01df\u01da")
        buf.write("\3\2\2\2\u01df\u01de\3\2\2\2\u01e0Y\3\2\2\2\u01e1\u01ec")
        buf.write("\7:\2\2\u01e2\u01ec\7;\2\2\u01e3\u01ec\7\67\2\2\u01e4")
        buf.write("\u01ec\78\2\2\u01e5\u01ec\5b\62\2\u01e6\u01ec\5^\60\2")
        buf.write("\u01e7\u01ec\7#\2\2\u01e8\u01ec\7\"\2\2\u01e9\u01ec\5")
        buf.write("\6\4\2\u01ea\u01ec\7[\2\2\u01eb\u01e1\3\2\2\2\u01eb\u01e2")
        buf.write("\3\2\2\2\u01eb\u01e3\3\2\2\2\u01eb\u01e4\3\2\2\2\u01eb")
        buf.write("\u01e5\3\2\2\2\u01eb\u01e6\3\2\2\2\u01eb\u01e7\3\2\2\2")
        buf.write("\u01eb\u01e8\3\2\2\2\u01eb\u01e9\3\2\2\2\u01eb\u01ea\3")
        buf.write("\2\2\2\u01ec[\3\2\2\2\u01ed\u01f2\7#\2\2\u01ee\u01ef\7")
        buf.write("{\2\2\u01ef\u01f1\7#\2\2\u01f0\u01ee\3\2\2\2\u01f1\u01f4")
        buf.write("\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3")
        buf.write("]\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f5\u01f6\7\36\2\2\u01f6")
        buf.write("\u01f8\7s\2\2\u01f7\u01f9\5`\61\2\u01f8\u01f7\3\2\2\2")
        buf.write("\u01f8\u01f9\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u01fb\7")
        buf.write("t\2\2\u01fb_\3\2\2\2\u01fc\u0201\5b\62\2\u01fd\u01fe\7")
        buf.write("{\2\2\u01fe\u0200\5b\62\2\u01ff\u01fd\3\2\2\2\u0200\u0203")
        buf.write("\3\2\2\2\u0201\u01ff\3\2\2\2\u0201\u0202\3\2\2\2\u0202")
        buf.write("a\3\2\2\2\u0203\u0201\3\2\2\2\u0204\u0205\7\36\2\2\u0205")
        buf.write("\u0207\7s\2\2\u0206\u0208\5d\63\2\u0207\u0206\3\2\2\2")
        buf.write("\u0207\u0208\3\2\2\2\u0208\u0209\3\2\2\2\u0209\u020a\7")
        buf.write("t\2\2\u020ac\3\2\2\2\u020b\u0210\5f\64\2\u020c\u020d\7")
        buf.write("{\2\2\u020d\u020f\5f\64\2\u020e\u020c\3\2\2\2\u020f\u0212")
        buf.write("\3\2\2\2\u0210\u020e\3\2\2\2\u0210\u0211\3\2\2\2\u0211")
        buf.write("e\3\2\2\2\u0212\u0210\3\2\2\2\u0213\u0214\5@!\2\u0214")
        buf.write("g\3\2\2\2>ksy\u0083\u0088\u008e\u0091\u0097\u009c\u009f")
        buf.write("\u00a3\u00a8\u00b2\u00b6\u00bb\u00c3\u00ce\u00d0\u00d4")
        buf.write("\u00db\u00e6\u00ef\u00f7\u0106\u010b\u011d\u0121\u0124")
        buf.write("\u012c\u0133\u013c\u0142\u014b\u0155\u015e\u0165\u016f")
        buf.write("\u0176\u017d\u0187\u0192\u0198\u019d\u01a9\u01ad\u01b8")
        buf.write("\u01bb\u01bf\u01c7\u01ca\u01cd\u01d3\u01d8\u01df\u01eb")
        buf.write("\u01f2\u01f8\u0201\u0207\u0210")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'Program'", "'main'", "'extends'", 
                     "'break'", "'continue'", "'if'", "'elseif'", "'else'", 
                     "'for'", "'true'", "'false'", "'array'", "'in'", "'int'", 
                     "'float'", "'boolean'", "'return'", "'class'", "'Null'", 
                     "'val'", "'var'", "'self'", "'constructor'", "'destructor'", 
                     "'new'", "'By'", "'do'", "'string'", "'then'", "'void'", 
                     "'nil'", "'this'", "'final'", "'static'", "'to'", "'downto'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'!='", "'='", "'>'", "'<'", "'>='", "'<='", 
                     "'==.'", "'+.'", "'^'", "'::'", "'('", "')'", "'['", 
                     "']'", "'{'", "'}'", "';'", "'.'", "','", "':'" ]

    symbolicNames = [ "<INVALID>", "Class_word", "Prog_word", "Extends_word", 
                      "Static_word", "Final_word", "Void_word", "Var_word", 
                      "Val_word", "Keyword_new", "If_word", "Then_word", 
                      "Else_word", "Elseif_word", "For_word", "Assign_op", 
                      "To_word", "Do_word", "Down_to_word", "Break_word", 
                      "Return_word", "Comment_normal", "Comment_block", 
                      "Comment_sharp", "Bool_word", "Int_word", "Float_word", 
                      "Str_word", "Array_word", "Main_word", "Cons_word", 
                      "Dest_word", "Self_word", "ID", "Add", "Sub", "Mul", 
                      "Div", "Mod", "Not", "And", "Or", "Equal", "Diff", 
                      "Greater", "Lesser", "Greater_euqal", "Lesser_equal", 
                      "String_comp", "String_concat", "Member_access_in", 
                      "Member_access_out", "Colon", "BOOLEANLIT", "STRINGLIT", 
                      "BLOCKCOMMENT", "INTLIT", "FLOATLIT", "PROGRAM", "MAIN", 
                      "EXTENDS", "BREAK", "CONT", "IF", "ELSEIF", "ELSE", 
                      "FOR", "BOOLTRUE", "BOOLFALSE", "ARRAY", "IN", "INT", 
                      "FLOAT", "BOOL", "RETURN", "CLASS", "NULL", "VAL", 
                      "VAR", "SELF", "CONS", "DEST", "KEYWORD_NEW", "BY", 
                      "DO", "STRING", "THEN", "VOID", "NIL", "THIS", "FINAL", 
                      "STATIC", "TO", "DOWNTO", "ADD_OP", "SUB_OP", "MUL_OP", 
                      "FLOAT_DIVISION_OP", "MOD_OP", "NOT_OP", "AND_OP", 
                      "OR_OP", "EQUAL_OP", "NOT_EQUAL_OP", "ASSIGN_OP", 
                      "GREATER_OP", "LESS_OP", "GREATER_EQUAL_OP", "LESS_EQUAL_OP", 
                      "STRING_COMP_OP", "STRING_CONCAT_OP", "CONCATENATION_OP", 
                      "MEMBER_ACCESS_OUT", "LP", "RP", "LSB", "RSB", "LB", 
                      "RB", "SEMI", "DOT", "COMA", "COLON", "WS", "UNTERMINATED_COMMENT", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_decl = 1
    RULE_class_name = 2
    RULE_member_lists = 3
    RULE_instructor = 4
    RULE_attributes = 5
    RULE_methods = 6
    RULE_block_stmt = 7
    RULE_block_stmt_list = 8
    RULE_var_cons_decl = 9
    RULE_var_cons_list = 10
    RULE_var_cons_name = 11
    RULE_stmt = 12
    RULE_as_stmt = 13
    RULE_new_val_from_class_stmt = 14
    RULE_if_stmt = 15
    RULE_loop_for_stmt = 16
    RULE_invocation_stmt = 17
    RULE_break_stmt = 18
    RULE_return_stmt = 19
    RULE_types = 20
    RULE_class_type = 21
    RULE_primitive_Type = 22
    RULE_array_Type = 23
    RULE_element_type = 24
    RULE_array_size = 25
    RULE_attribute_list = 26
    RULE_attribute_name = 27
    RULE_paramlist = 28
    RULE_param_decl = 29
    RULE_expr_list = 30
    RULE_expr = 31
    RULE_string_expr = 32
    RULE_relational_expr = 33
    RULE_logical_expr = 34
    RULE_adding_expr = 35
    RULE_multiplying_expr = 36
    RULE_logical_not_expr = 37
    RULE_sign_expr = 38
    RULE_index_expr = 39
    RULE_member_access_in = 40
    RULE_member_access_out = 41
    RULE_class_expr = 42
    RULE_piority_exp = 43
    RULE_operands = 44
    RULE_idlist = 45
    RULE_multi_ArrayLIT = 46
    RULE_array_list = 47
    RULE_arrayLIT = 48
    RULE_element_list = 49
    RULE_elements = 50

    ruleNames =  [ "program", "class_decl", "class_name", "member_lists", 
                   "instructor", "attributes", "methods", "block_stmt", 
                   "block_stmt_list", "var_cons_decl", "var_cons_list", 
                   "var_cons_name", "stmt", "as_stmt", "new_val_from_class_stmt", 
                   "if_stmt", "loop_for_stmt", "invocation_stmt", "break_stmt", 
                   "return_stmt", "types", "class_type", "primitive_Type", 
                   "array_Type", "element_type", "array_size", "attribute_list", 
                   "attribute_name", "paramlist", "param_decl", "expr_list", 
                   "expr", "string_expr", "relational_expr", "logical_expr", 
                   "adding_expr", "multiplying_expr", "logical_not_expr", 
                   "sign_expr", "index_expr", "member_access_in", "member_access_out", 
                   "class_expr", "piority_exp", "operands", "idlist", "multi_ArrayLIT", 
                   "array_list", "arrayLIT", "element_list", "elements" ]

    EOF = Token.EOF
    Class_word=1
    Prog_word=2
    Extends_word=3
    Static_word=4
    Final_word=5
    Void_word=6
    Var_word=7
    Val_word=8
    Keyword_new=9
    If_word=10
    Then_word=11
    Else_word=12
    Elseif_word=13
    For_word=14
    Assign_op=15
    To_word=16
    Do_word=17
    Down_to_word=18
    Break_word=19
    Return_word=20
    Comment_normal=21
    Comment_block=22
    Comment_sharp=23
    Bool_word=24
    Int_word=25
    Float_word=26
    Str_word=27
    Array_word=28
    Main_word=29
    Cons_word=30
    Dest_word=31
    Self_word=32
    ID=33
    Add=34
    Sub=35
    Mul=36
    Div=37
    Mod=38
    Not=39
    And=40
    Or=41
    Equal=42
    Diff=43
    Greater=44
    Lesser=45
    Greater_euqal=46
    Lesser_equal=47
    String_comp=48
    String_concat=49
    Member_access_in=50
    Member_access_out=51
    Colon=52
    BOOLEANLIT=53
    STRINGLIT=54
    BLOCKCOMMENT=55
    INTLIT=56
    FLOATLIT=57
    PROGRAM=58
    MAIN=59
    EXTENDS=60
    BREAK=61
    CONT=62
    IF=63
    ELSEIF=64
    ELSE=65
    FOR=66
    BOOLTRUE=67
    BOOLFALSE=68
    ARRAY=69
    IN=70
    INT=71
    FLOAT=72
    BOOL=73
    RETURN=74
    CLASS=75
    NULL=76
    VAL=77
    VAR=78
    SELF=79
    CONS=80
    DEST=81
    KEYWORD_NEW=82
    BY=83
    DO=84
    STRING=85
    THEN=86
    VOID=87
    NIL=88
    THIS=89
    FINAL=90
    STATIC=91
    TO=92
    DOWNTO=93
    ADD_OP=94
    SUB_OP=95
    MUL_OP=96
    FLOAT_DIVISION_OP=97
    MOD_OP=98
    NOT_OP=99
    AND_OP=100
    OR_OP=101
    EQUAL_OP=102
    NOT_EQUAL_OP=103
    ASSIGN_OP=104
    GREATER_OP=105
    LESS_OP=106
    GREATER_EQUAL_OP=107
    LESS_EQUAL_OP=108
    STRING_COMP_OP=109
    STRING_CONCAT_OP=110
    CONCATENATION_OP=111
    MEMBER_ACCESS_OUT=112
    LP=113
    RP=114
    LSB=115
    RSB=116
    LB=117
    RB=118
    SEMI=119
    DOT=120
    COMA=121
    COLON=122
    WS=123
    UNTERMINATED_COMMENT=124
    ERROR_CHAR=125

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def class_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Class_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Class_declContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 102
                self.class_decl()
                self.state = 105 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.Class_word):
                    break

            self.state = 107
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Class_word(self):
            return self.getToken(BKOOLParser.Class_word, 0)

        def class_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Class_nameContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Class_nameContext,i)


        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def Extends_word(self):
            return self.getToken(BKOOLParser.Extends_word, 0)

        def member_lists(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Member_listsContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Member_listsContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_class_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decl" ):
                return visitor.visitClass_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_decl(self):

        localctx = BKOOLParser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(BKOOLParser.Class_word)
            self.state = 110
            self.class_name()
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.Extends_word:
                self.state = 111
                self.match(BKOOLParser.Extends_word)
                self.state = 112
                self.class_name()


            self.state = 115
            self.match(BKOOLParser.LB)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Static_word) | (1 << BKOOLParser.Final_word) | (1 << BKOOLParser.Void_word) | (1 << BKOOLParser.Bool_word) | (1 << BKOOLParser.Int_word) | (1 << BKOOLParser.Float_word) | (1 << BKOOLParser.Str_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.ID))) != 0) or _la==BKOOLParser.CLASS:
                self.state = 116
                self.member_lists()
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 122
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def Prog_word(self):
            return self.getToken(BKOOLParser.Prog_word, 0)

        def CLASS(self):
            return self.getToken(BKOOLParser.CLASS, 0)

        def Main_word(self):
            return self.getToken(BKOOLParser.Main_word, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_class_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_name" ):
                return visitor.visitClass_name(self)
            else:
                return visitor.visitChildren(self)




    def class_name(self):

        localctx = BKOOLParser.Class_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.ID))) != 0) or _la==BKOOLParser.CLASS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_listsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributes(self):
            return self.getTypedRuleContext(BKOOLParser.AttributesContext,0)


        def methods(self):
            return self.getTypedRuleContext(BKOOLParser.MethodsContext,0)


        def instructor(self):
            return self.getTypedRuleContext(BKOOLParser.InstructorContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_member_lists

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_lists" ):
                return visitor.visitMember_lists(self)
            else:
                return visitor.visitChildren(self)




    def member_lists(self):

        localctx = BKOOLParser.Member_listsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_member_lists)
        try:
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.attributes()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.methods()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 128
                self.instructor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_name(self):
            return self.getTypedRuleContext(BKOOLParser.Class_nameContext,0)


        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def paramlist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_instructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstructor" ):
                return visitor.visitInstructor(self)
            else:
                return visitor.visitChildren(self)




    def instructor(self):

        localctx = BKOOLParser.InstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_instructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.class_name()
            self.state = 132
            self.match(BKOOLParser.LP)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Bool_word) | (1 << BKOOLParser.Int_word) | (1 << BKOOLParser.Float_word) | (1 << BKOOLParser.Str_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.ID))) != 0) or _la==BKOOLParser.CLASS:
                self.state = 133
                self.paramlist()


            self.state = 136
            self.match(BKOOLParser.RP)
            self.state = 137
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_Type(self):
            return self.getTypedRuleContext(BKOOLParser.Primitive_TypeContext,0)


        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def Static_word(self):
            return self.getToken(BKOOLParser.Static_word, 0)

        def Final_word(self):
            return self.getToken(BKOOLParser.Final_word, 0)

        def Assign_op(self):
            return self.getToken(BKOOLParser.Assign_op, 0)

        def operands(self):
            return self.getTypedRuleContext(BKOOLParser.OperandsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attributes

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributes" ):
                return visitor.visitAttributes(self)
            else:
                return visitor.visitChildren(self)




    def attributes(self):

        localctx = BKOOLParser.AttributesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attributes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.Static_word:
                self.state = 139
                self.match(BKOOLParser.Static_word)


            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.Final_word:
                self.state = 142
                self.match(BKOOLParser.Final_word)


            self.state = 145
            self.primitive_Type()
            self.state = 146
            self.idlist()
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.Assign_op:
                self.state = 147
                self.match(BKOOLParser.Assign_op)
                self.state = 148
                self.operands()


            self.state = 151
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def Main_word(self):
            return self.getToken(BKOOLParser.Main_word, 0)

        def primitive_Type(self):
            return self.getTypedRuleContext(BKOOLParser.Primitive_TypeContext,0)


        def Void_word(self):
            return self.getToken(BKOOLParser.Void_word, 0)

        def Static_word(self):
            return self.getToken(BKOOLParser.Static_word, 0)

        def Final_word(self):
            return self.getToken(BKOOLParser.Final_word, 0)

        def paramlist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_methods

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethods" ):
                return visitor.visitMethods(self)
            else:
                return visitor.visitChildren(self)




    def methods(self):

        localctx = BKOOLParser.MethodsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_methods)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.Static_word:
                self.state = 153
                self.match(BKOOLParser.Static_word)


            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.Final_word:
                self.state = 156
                self.match(BKOOLParser.Final_word)


            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.Bool_word, BKOOLParser.Int_word, BKOOLParser.Float_word, BKOOLParser.Str_word]:
                self.state = 159
                self.primitive_Type()
                pass
            elif token in [BKOOLParser.Void_word]:
                self.state = 160
                self.match(BKOOLParser.Void_word)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 163
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.Main_word or _la==BKOOLParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 164
            self.match(BKOOLParser.LP)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Bool_word) | (1 << BKOOLParser.Int_word) | (1 << BKOOLParser.Float_word) | (1 << BKOOLParser.Str_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.ID))) != 0) or _la==BKOOLParser.CLASS:
                self.state = 165
                self.paramlist()


            self.state = 168
            self.match(BKOOLParser.RP)
            self.state = 169
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_stmt_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Block_stmt_listContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Block_stmt_listContext,i)


        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = BKOOLParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.Prog_word, BKOOLParser.Var_word, BKOOLParser.Val_word, BKOOLParser.If_word, BKOOLParser.For_word, BKOOLParser.Break_word, BKOOLParser.Return_word, BKOOLParser.Bool_word, BKOOLParser.Int_word, BKOOLParser.Float_word, BKOOLParser.Str_word, BKOOLParser.Array_word, BKOOLParser.Main_word, BKOOLParser.Self_word, BKOOLParser.ID, BKOOLParser.BOOLEANLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.CLASS, BKOOLParser.KEYWORD_NEW, BKOOLParser.THIS, BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.block_stmt_list()
                pass
            elif token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.match(BKOOLParser.LB)
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Var_word) | (1 << BKOOLParser.Val_word) | (1 << BKOOLParser.If_word) | (1 << BKOOLParser.For_word) | (1 << BKOOLParser.Break_word) | (1 << BKOOLParser.Return_word) | (1 << BKOOLParser.Bool_word) | (1 << BKOOLParser.Int_word) | (1 << BKOOLParser.Float_word) | (1 << BKOOLParser.Str_word) | (1 << BKOOLParser.Array_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.Self_word) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.BOOLEANLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (BKOOLParser.CLASS - 75)) | (1 << (BKOOLParser.KEYWORD_NEW - 75)) | (1 << (BKOOLParser.THIS - 75)) | (1 << (BKOOLParser.LP - 75)))) != 0):
                    self.state = 173
                    self.block_stmt_list()
                    self.state = 178
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 179
                self.match(BKOOLParser.RB)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def var_cons_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Var_cons_declContext,0)


        def var_cons_list(self):
            return self.getTypedRuleContext(BKOOLParser.Var_cons_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_block_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt_list" ):
                return visitor.visitBlock_stmt_list(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt_list(self):

        localctx = BKOOLParser.Block_stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_block_stmt_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 182
                self.stmt()
                pass

            elif la_ == 2:
                self.state = 183
                self.var_cons_decl()
                pass

            elif la_ == 3:
                self.state = 184
                self.var_cons_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_cons_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def Colon(self):
            return self.getToken(BKOOLParser.Colon, 0)

        def types(self):
            return self.getTypedRuleContext(BKOOLParser.TypesContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def Var_word(self):
            return self.getToken(BKOOLParser.Var_word, 0)

        def Val_word(self):
            return self.getToken(BKOOLParser.Val_word, 0)

        def Assign_op(self):
            return self.getToken(BKOOLParser.Assign_op, 0)

        def expr_list(self):
            return self.getTypedRuleContext(BKOOLParser.Expr_listContext,0)


        def paramlist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamlistContext,0)


        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def new_val_from_class_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.New_val_from_class_stmtContext,0)


        def invocation_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Invocation_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_var_cons_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_cons_decl" ):
                return visitor.visitVar_cons_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_cons_decl(self):

        localctx = BKOOLParser.Var_cons_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_var_cons_decl)
        self._la = 0 # Token type
        try:
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.Var_word, BKOOLParser.Val_word]:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.Var_word or _la==BKOOLParser.Val_word):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 188
                self.idlist()
                self.state = 189
                self.match(BKOOLParser.Colon)
                self.state = 190
                self.types()
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.Assign_op:
                    self.state = 191
                    self.match(BKOOLParser.Assign_op)
                    self.state = 192
                    self.expr_list()


                self.state = 195
                self.match(BKOOLParser.SEMI)
                pass
            elif token in [BKOOLParser.Prog_word, BKOOLParser.Bool_word, BKOOLParser.Int_word, BKOOLParser.Float_word, BKOOLParser.Str_word, BKOOLParser.Main_word, BKOOLParser.ID, BKOOLParser.CLASS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.paramlist()
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.Colon:
                    self.state = 198
                    self.match(BKOOLParser.Colon)
                    self.state = 199
                    self.match(BKOOLParser.Assign_op)
                    self.state = 204
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        self.state = 201
                        self.expr()
                        pass

                    elif la_ == 2:
                        self.state = 202
                        self.new_val_from_class_stmt()
                        pass

                    elif la_ == 3:
                        self.state = 203
                        self.invocation_stmt()
                        pass




                self.state = 208
                self.match(BKOOLParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_cons_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_cons_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Var_cons_nameContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Var_cons_nameContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMA)
            else:
                return self.getToken(BKOOLParser.COMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_var_cons_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_cons_list" ):
                return visitor.visitVar_cons_list(self)
            else:
                return visitor.visitChildren(self)




    def var_cons_list(self):

        localctx = BKOOLParser.Var_cons_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_var_cons_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.var_cons_name()
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMA:
                self.state = 213
                self.match(BKOOLParser.COMA)
                self.state = 214
                self.var_cons_name()
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_cons_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_var_cons_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_cons_name" ):
                return visitor.visitVar_cons_name(self)
            else:
                return visitor.visitChildren(self)




    def var_cons_name(self):

        localctx = BKOOLParser.Var_cons_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_var_cons_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def as_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.As_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.If_stmtContext,0)


        def loop_for_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Loop_for_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Break_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Return_stmtContext,0)


        def invocation_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Invocation_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_stmt)
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.as_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 224
                self.loop_for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 225
                self.break_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 226
                self.return_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 227
                self.invocation_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class As_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Index_exprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def Colon(self):
            return self.getToken(BKOOLParser.Colon, 0)

        def Assign_op(self):
            return self.getToken(BKOOLParser.Assign_op, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def new_val_from_class_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.New_val_from_class_stmtContext,0)


        def invocation_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Invocation_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_as_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAs_stmt" ):
                return visitor.visitAs_stmt(self)
            else:
                return visitor.visitChildren(self)




    def as_stmt(self):

        localctx = BKOOLParser.As_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_as_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.index_expr(0)

            self.state = 231
            self.match(BKOOLParser.Colon)
            self.state = 232
            self.match(BKOOLParser.Assign_op)
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 234
                self.expr()
                pass

            elif la_ == 2:
                self.state = 235
                self.new_val_from_class_stmt()
                pass

            elif la_ == 3:
                self.state = 236
                self.invocation_stmt()
                pass


            self.state = 239
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class New_val_from_class_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Keyword_new(self):
            return self.getToken(BKOOLParser.Keyword_new, 0)

        def class_name(self):
            return self.getTypedRuleContext(BKOOLParser.Class_nameContext,0)


        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(BKOOLParser.Expr_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_new_val_from_class_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNew_val_from_class_stmt" ):
                return visitor.visitNew_val_from_class_stmt(self)
            else:
                return visitor.visitChildren(self)




    def new_val_from_class_stmt(self):

        localctx = BKOOLParser.New_val_from_class_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_new_val_from_class_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(BKOOLParser.Keyword_new)
            self.state = 242
            self.class_name()
            self.state = 243
            self.match(BKOOLParser.LP)
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Array_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.Self_word) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.Sub) | (1 << BKOOLParser.Not) | (1 << BKOOLParser.BOOLEANLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (BKOOLParser.CLASS - 75)) | (1 << (BKOOLParser.KEYWORD_NEW - 75)) | (1 << (BKOOLParser.THIS - 75)) | (1 << (BKOOLParser.LP - 75)))) != 0):
                self.state = 244
                self.expr_list()


            self.state = 247
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def If_word(self):
            return self.getToken(BKOOLParser.If_word, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def Then_word(self):
            return self.getToken(BKOOLParser.Then_word, 0)

        def block_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Block_stmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,i)


        def Elseif_word(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.Elseif_word)
            else:
                return self.getToken(BKOOLParser.Elseif_word, i)

        def Else_word(self):
            return self.getToken(BKOOLParser.Else_word, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = BKOOLParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(BKOOLParser.If_word)
            self.state = 250
            self.expr()
            self.state = 251
            self.match(BKOOLParser.Then_word)
            self.state = 252
            self.block_stmt()
            self.state = 260
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 254
                    self.match(BKOOLParser.Elseif_word)
                    self.state = 255
                    self.expr()
                    self.state = 256
                    self.block_stmt() 
                self.state = 262
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 263
                self.match(BKOOLParser.Else_word)
                self.state = 264
                self.block_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_for_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def For_word(self):
            return self.getToken(BKOOLParser.For_word, 0)

        def Do_word(self):
            return self.getToken(BKOOLParser.Do_word, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def To_word(self):
            return self.getToken(BKOOLParser.To_word, 0)

        def Down_to_word(self):
            return self.getToken(BKOOLParser.Down_to_word, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def Colon(self):
            return self.getToken(BKOOLParser.Colon, 0)

        def Assign_op(self):
            return self.getToken(BKOOLParser.Assign_op, 0)

        def INTLIT(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.INTLIT)
            else:
                return self.getToken(BKOOLParser.INTLIT, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_loop_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_for_stmt" ):
                return visitor.visitLoop_for_stmt(self)
            else:
                return visitor.visitChildren(self)




    def loop_for_stmt(self):

        localctx = BKOOLParser.Loop_for_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_loop_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(BKOOLParser.For_word)

            self.state = 268
            self.match(BKOOLParser.ID)
            self.state = 269
            self.match(BKOOLParser.Colon)
            self.state = 270
            self.match(BKOOLParser.Assign_op)
            self.state = 271
            self.match(BKOOLParser.INTLIT)
            self.state = 273
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.To_word or _la==BKOOLParser.Down_to_word):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()

            self.state = 274
            self.match(BKOOLParser.INTLIT)
            self.state = 275
            self.match(BKOOLParser.Do_word)
            self.state = 276
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Invocation_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Index_exprContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def invocation_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Invocation_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_invocation_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInvocation_stmt" ):
                return visitor.visitInvocation_stmt(self)
            else:
                return visitor.visitChildren(self)




    def invocation_stmt(self):

        localctx = BKOOLParser.Invocation_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_invocation_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 278
                self.index_expr(0)
                pass

            elif la_ == 2:
                self.state = 279
                self.match(BKOOLParser.ID)
                self.state = 280
                self.match(BKOOLParser.LP)
                self.state = 283
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 281
                    self.expr()
                    pass

                elif la_ == 2:
                    self.state = 282
                    self.invocation_stmt()
                    pass


                self.state = 285
                self.match(BKOOLParser.RP)
                pass


            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 289
                self.match(BKOOLParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Break_word(self):
            return self.getToken(BKOOLParser.Break_word, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = BKOOLParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(BKOOLParser.Break_word)
            self.state = 293
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Return_word(self):
            return self.getToken(BKOOLParser.Return_word, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def invocation_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Invocation_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = BKOOLParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(BKOOLParser.Return_word)
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 296
                self.expr()

            elif la_ == 2:
                self.state = 297
                self.invocation_stmt()


            self.state = 300
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_Type(self):
            return self.getTypedRuleContext(BKOOLParser.Primitive_TypeContext,0)


        def array_Type(self):
            return self.getTypedRuleContext(BKOOLParser.Array_TypeContext,0)


        def class_type(self):
            return self.getTypedRuleContext(BKOOLParser.Class_typeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypes" ):
                return visitor.visitTypes(self)
            else:
                return visitor.visitChildren(self)




    def types(self):

        localctx = BKOOLParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_types)
        try:
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.primitive_Type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.array_Type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 304
                self.class_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_name(self):
            return self.getTypedRuleContext(BKOOLParser.Class_nameContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_class_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_type" ):
                return visitor.visitClass_type(self)
            else:
                return visitor.visitChildren(self)




    def class_type(self):

        localctx = BKOOLParser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.class_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Bool_word(self):
            return self.getToken(BKOOLParser.Bool_word, 0)

        def Int_word(self):
            return self.getToken(BKOOLParser.Int_word, 0)

        def Float_word(self):
            return self.getToken(BKOOLParser.Float_word, 0)

        def Str_word(self):
            return self.getToken(BKOOLParser.Str_word, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_primitive_Type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_Type" ):
                return visitor.visitPrimitive_Type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_Type(self):

        localctx = BKOOLParser.Primitive_TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_primitive_Type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Bool_word) | (1 << BKOOLParser.Int_word) | (1 << BKOOLParser.Float_word) | (1 << BKOOLParser.Str_word))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_Type(self):
            return self.getTypedRuleContext(BKOOLParser.Primitive_TypeContext,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def array_size(self):
            return self.getTypedRuleContext(BKOOLParser.Array_sizeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_array_Type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_Type" ):
                return visitor.visitArray_Type(self)
            else:
                return visitor.visitChildren(self)




    def array_Type(self):

        localctx = BKOOLParser.Array_TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_array_Type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.primitive_Type()
            self.state = 312
            self.match(BKOOLParser.LSB)
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.INTLIT:
                self.state = 313
                self.array_size()


            self.state = 316
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_Type(self):
            return self.getTypedRuleContext(BKOOLParser.Primitive_TypeContext,0)


        def array_Type(self):
            return self.getTypedRuleContext(BKOOLParser.Array_TypeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_element_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_type" ):
                return visitor.visitElement_type(self)
            else:
                return visitor.visitChildren(self)




    def element_type(self):

        localctx = BKOOLParser.Element_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_element_type)
        try:
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.primitive_Type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                self.array_Type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_sizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_size

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_size" ):
                return visitor.visitArray_size(self)
            else:
                return visitor.visitChildren(self)




    def array_size(self):

        localctx = BKOOLParser.Array_sizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_array_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(BKOOLParser.INTLIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Attribute_nameContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Attribute_nameContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMA)
            else:
                return self.getToken(BKOOLParser.COMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_attribute_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_list" ):
                return visitor.visitAttribute_list(self)
            else:
                return visitor.visitChildren(self)




    def attribute_list(self):

        localctx = BKOOLParser.Attribute_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_attribute_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.attribute_name()
            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMA:
                self.state = 325
                self.match(BKOOLParser.COMA)
                self.state = 326
                self.attribute_name()
                self.state = 331
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_attribute_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_name" ):
                return visitor.visitAttribute_name(self)
            else:
                return visitor.visitChildren(self)




    def attribute_name(self):

        localctx = BKOOLParser.Attribute_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_attribute_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Param_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Param_declContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMA)
            else:
                return self.getToken(BKOOLParser.COMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = BKOOLParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_paramlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.param_decl()
            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMA:
                self.state = 335
                self.match(BKOOLParser.COMA)
                self.state = 336
                self.param_decl()
                self.state = 341
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def types(self):
            return self.getTypedRuleContext(BKOOLParser.TypesContext,0)


        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def Colon(self):
            return self.getToken(BKOOLParser.Colon, 0)

        def class_name(self):
            return self.getTypedRuleContext(BKOOLParser.Class_nameContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_decl" ):
                return visitor.visitParam_decl(self)
            else:
                return visitor.visitChildren(self)




    def param_decl(self):

        localctx = BKOOLParser.Param_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_param_decl)
        try:
            self.state = 348
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.types()
                self.state = 343
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self.match(BKOOLParser.ID)
                self.state = 346
                self.match(BKOOLParser.Colon)
                self.state = 347
                self.class_name()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMA)
            else:
                return self.getToken(BKOOLParser.COMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = BKOOLParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.expr()
            self.state = 355
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMA:
                self.state = 351
                self.match(BKOOLParser.COMA)
                self.state = 352
                self.expr()
                self.state = 357
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string_expr(self):
            return self.getTypedRuleContext(BKOOLParser.String_exprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.string_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Relational_exprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Relational_exprContext,i)


        def String_comp(self):
            return self.getToken(BKOOLParser.String_comp, 0)

        def String_concat(self):
            return self.getToken(BKOOLParser.String_concat, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_string_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_expr" ):
                return visitor.visitString_expr(self)
            else:
                return visitor.visitChildren(self)




    def string_expr(self):

        localctx = BKOOLParser.String_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_string_expr)
        self._la = 0 # Token type
        try:
            self.state = 365
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.relational_expr()
                self.state = 361
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.String_comp or _la==BKOOLParser.String_concat):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 362
                self.relational_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                self.relational_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Logical_exprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Logical_exprContext,i)


        def Equal(self):
            return self.getToken(BKOOLParser.Equal, 0)

        def Diff(self):
            return self.getToken(BKOOLParser.Diff, 0)

        def Greater(self):
            return self.getToken(BKOOLParser.Greater, 0)

        def Lesser(self):
            return self.getToken(BKOOLParser.Lesser, 0)

        def Greater_euqal(self):
            return self.getToken(BKOOLParser.Greater_euqal, 0)

        def Lesser_equal(self):
            return self.getToken(BKOOLParser.Lesser_equal, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_relational_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_expr" ):
                return visitor.visitRelational_expr(self)
            else:
                return visitor.visitChildren(self)




    def relational_expr(self):

        localctx = BKOOLParser.Relational_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_relational_expr)
        self._la = 0 # Token type
        try:
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.logical_expr()
                self.state = 368
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Equal) | (1 << BKOOLParser.Diff) | (1 << BKOOLParser.Greater) | (1 << BKOOLParser.Lesser) | (1 << BKOOLParser.Greater_euqal) | (1 << BKOOLParser.Lesser_equal))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 369
                self.logical_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 371
                self.logical_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def adding_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Adding_exprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Adding_exprContext,i)


        def And(self):
            return self.getToken(BKOOLParser.And, 0)

        def Or(self):
            return self.getToken(BKOOLParser.Or, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_logical_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_expr" ):
                return visitor.visitLogical_expr(self)
            else:
                return visitor.visitChildren(self)




    def logical_expr(self):

        localctx = BKOOLParser.Logical_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_logical_expr)
        self._la = 0 # Token type
        try:
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.adding_expr(0)
                self.state = 375
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.And or _la==BKOOLParser.Or):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 376
                self.adding_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
                self.adding_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Adding_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplying_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Multiplying_exprContext,0)


        def adding_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Adding_exprContext,0)


        def Add(self):
            return self.getToken(BKOOLParser.Add, 0)

        def Sub(self):
            return self.getToken(BKOOLParser.Sub, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_adding_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding_expr" ):
                return visitor.visitAdding_expr(self)
            else:
                return visitor.visitChildren(self)



    def adding_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Adding_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_adding_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.multiplying_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 389
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Adding_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_expr)
                    self.state = 384
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 385
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.Add or _la==BKOOLParser.Sub):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 386
                    self.multiplying_expr(0) 
                self.state = 391
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multiplying_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_not_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Logical_not_exprContext,0)


        def multiplying_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Multiplying_exprContext,0)


        def Mul(self):
            return self.getToken(BKOOLParser.Mul, 0)

        def Div(self):
            return self.getToken(BKOOLParser.Div, 0)

        def Mod(self):
            return self.getToken(BKOOLParser.Mod, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_multiplying_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying_expr" ):
                return visitor.visitMultiplying_expr(self)
            else:
                return visitor.visitChildren(self)



    def multiplying_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Multiplying_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_multiplying_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.logical_not_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 400
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Multiplying_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expr)
                    self.state = 395
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 396
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Mul) | (1 << BKOOLParser.Div) | (1 << BKOOLParser.Mod))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 397
                    self.logical_not_expr() 
                self.state = 402
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Logical_not_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Not(self):
            return self.getToken(BKOOLParser.Not, 0)

        def logical_not_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Logical_not_exprContext,0)


        def sign_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Sign_exprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_logical_not_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_not_expr" ):
                return visitor.visitLogical_not_expr(self)
            else:
                return visitor.visitChildren(self)




    def logical_not_expr(self):

        localctx = BKOOLParser.Logical_not_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_logical_not_expr)
        try:
            self.state = 406
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.Not]:
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                self.match(BKOOLParser.Not)
                self.state = 404
                self.logical_not_expr()
                pass
            elif token in [BKOOLParser.Prog_word, BKOOLParser.Array_word, BKOOLParser.Main_word, BKOOLParser.Self_word, BKOOLParser.ID, BKOOLParser.Sub, BKOOLParser.BOOLEANLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.CLASS, BKOOLParser.KEYWORD_NEW, BKOOLParser.THIS, BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
                self.sign_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sign_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Sub(self):
            return self.getToken(BKOOLParser.Sub, 0)

        def sign_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Sign_exprContext,0)


        def index_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Index_exprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_sign_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_expr" ):
                return visitor.visitSign_expr(self)
            else:
                return visitor.visitChildren(self)




    def sign_expr(self):

        localctx = BKOOLParser.Sign_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_sign_expr)
        try:
            self.state = 411
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.Sub]:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                self.match(BKOOLParser.Sub)
                self.state = 409
                self.sign_expr()
                pass
            elif token in [BKOOLParser.Prog_word, BKOOLParser.Array_word, BKOOLParser.Main_word, BKOOLParser.Self_word, BKOOLParser.ID, BKOOLParser.BOOLEANLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.CLASS, BKOOLParser.KEYWORD_NEW, BKOOLParser.THIS, BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                self.index_expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_access_in(self):
            return self.getTypedRuleContext(BKOOLParser.Member_access_inContext,0)


        def index_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Index_exprContext,0)


        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.LSB)
            else:
                return self.getToken(BKOOLParser.LSB, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.RSB)
            else:
                return self.getToken(BKOOLParser.RSB, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expr" ):
                return visitor.visitIndex_expr(self)
            else:
                return visitor.visitChildren(self)



    def index_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Index_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_index_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.member_access_in(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 427
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Index_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_expr)
                    self.state = 416
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 421 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 417
                            self.match(BKOOLParser.LSB)
                            self.state = 418
                            self.expr()
                            self.state = 419
                            self.match(BKOOLParser.RSB)

                        else:
                            raise NoViableAltException(self)
                        self.state = 423 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
             
                self.state = 429
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Member_access_inContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_access_out(self):
            return self.getTypedRuleContext(BKOOLParser.Member_access_outContext,0)


        def member_access_in(self):
            return self.getTypedRuleContext(BKOOLParser.Member_access_inContext,0)


        def Member_access_in(self):
            return self.getToken(BKOOLParser.Member_access_in, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(BKOOLParser.Expr_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_member_access_in

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_access_in" ):
                return visitor.visitMember_access_in(self)
            else:
                return visitor.visitChildren(self)



    def member_access_in(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Member_access_inContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_member_access_in, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.member_access_out()
            self._ctx.stop = self._input.LT(-1)
            self.state = 445
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Member_access_inContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_member_access_in)
                    self.state = 433
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 434
                    self.match(BKOOLParser.Member_access_in)
                    self.state = 435
                    self.member_access_out()
                    self.state = 441
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                    if la_ == 1:
                        self.state = 436
                        self.match(BKOOLParser.LP)
                        self.state = 438
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Array_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.Self_word) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.Sub) | (1 << BKOOLParser.Not) | (1 << BKOOLParser.BOOLEANLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (BKOOLParser.CLASS - 75)) | (1 << (BKOOLParser.KEYWORD_NEW - 75)) | (1 << (BKOOLParser.THIS - 75)) | (1 << (BKOOLParser.LP - 75)))) != 0):
                            self.state = 437
                            self.expr_list()


                        self.state = 440
                        self.match(BKOOLParser.RP)

             
                self.state = 447
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Member_access_outContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Class_exprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Class_exprContext,i)


        def Member_access_out(self):
            return self.getToken(BKOOLParser.Member_access_out, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(BKOOLParser.Expr_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_member_access_out

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_access_out" ):
                return visitor.visitMember_access_out(self)
            else:
                return visitor.visitChildren(self)




    def member_access_out(self):

        localctx = BKOOLParser.Member_access_outContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_member_access_out)
        self._la = 0 # Token type
        try:
            self.state = 459
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 448
                self.class_expr()
                self.state = 449
                self.match(BKOOLParser.Member_access_out)
                self.state = 450
                self.class_expr()
                self.state = 456
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                if la_ == 1:
                    self.state = 451
                    self.match(BKOOLParser.LP)
                    self.state = 453
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Array_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.Self_word) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.Sub) | (1 << BKOOLParser.Not) | (1 << BKOOLParser.BOOLEANLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (BKOOLParser.CLASS - 75)) | (1 << (BKOOLParser.KEYWORD_NEW - 75)) | (1 << (BKOOLParser.THIS - 75)) | (1 << (BKOOLParser.LP - 75)))) != 0):
                        self.state = 452
                        self.expr_list()


                    self.state = 455
                    self.match(BKOOLParser.RP)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 458
                self.class_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD_NEW(self):
            return self.getToken(BKOOLParser.KEYWORD_NEW, 0)

        def class_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Class_exprContext,0)


        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(BKOOLParser.Expr_listContext,0)


        def piority_exp(self):
            return self.getTypedRuleContext(BKOOLParser.Piority_expContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_class_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_expr" ):
                return visitor.visitClass_expr(self)
            else:
                return visitor.visitChildren(self)




    def class_expr(self):

        localctx = BKOOLParser.Class_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_class_expr)
        self._la = 0 # Token type
        try:
            self.state = 470
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.KEYWORD_NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 461
                self.match(BKOOLParser.KEYWORD_NEW)
                self.state = 462
                self.class_expr()
                self.state = 463
                self.match(BKOOLParser.LP)
                self.state = 465
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Array_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.Self_word) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.Sub) | (1 << BKOOLParser.Not) | (1 << BKOOLParser.BOOLEANLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (BKOOLParser.CLASS - 75)) | (1 << (BKOOLParser.KEYWORD_NEW - 75)) | (1 << (BKOOLParser.THIS - 75)) | (1 << (BKOOLParser.LP - 75)))) != 0):
                    self.state = 464
                    self.expr_list()


                self.state = 467
                self.match(BKOOLParser.RP)
                pass
            elif token in [BKOOLParser.Prog_word, BKOOLParser.Array_word, BKOOLParser.Main_word, BKOOLParser.Self_word, BKOOLParser.ID, BKOOLParser.BOOLEANLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.CLASS, BKOOLParser.THIS, BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 469
                self.piority_exp()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Piority_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def operands(self):
            return self.getTypedRuleContext(BKOOLParser.OperandsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_piority_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPiority_exp" ):
                return visitor.visitPiority_exp(self)
            else:
                return visitor.visitChildren(self)




    def piority_exp(self):

        localctx = BKOOLParser.Piority_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_piority_exp)
        try:
            self.state = 477
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 472
                self.match(BKOOLParser.LP)
                self.state = 473
                self.expr()
                self.state = 474
                self.match(BKOOLParser.RP)
                pass
            elif token in [BKOOLParser.Prog_word, BKOOLParser.Array_word, BKOOLParser.Main_word, BKOOLParser.Self_word, BKOOLParser.ID, BKOOLParser.BOOLEANLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.CLASS, BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 476
                self.operands()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def BOOLEANLIT(self):
            return self.getToken(BKOOLParser.BOOLEANLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKOOLParser.STRINGLIT, 0)

        def arrayLIT(self):
            return self.getTypedRuleContext(BKOOLParser.ArrayLITContext,0)


        def multi_ArrayLIT(self):
            return self.getTypedRuleContext(BKOOLParser.Multi_ArrayLITContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def Self_word(self):
            return self.getToken(BKOOLParser.Self_word, 0)

        def class_name(self):
            return self.getTypedRuleContext(BKOOLParser.Class_nameContext,0)


        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = BKOOLParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_operands)
        try:
            self.state = 489
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 479
                self.match(BKOOLParser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 480
                self.match(BKOOLParser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 481
                self.match(BKOOLParser.BOOLEANLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 482
                self.match(BKOOLParser.STRINGLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 483
                self.arrayLIT()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 484
                self.multi_ArrayLIT()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 485
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 486
                self.match(BKOOLParser.Self_word)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 487
                self.class_name()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 488
                self.match(BKOOLParser.THIS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMA)
            else:
                return self.getToken(BKOOLParser.COMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = BKOOLParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_idlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.match(BKOOLParser.ID)
            self.state = 496
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,55,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 492
                    self.match(BKOOLParser.COMA)
                    self.state = 493
                    self.match(BKOOLParser.ID) 
                self.state = 498
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,55,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multi_ArrayLITContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Array_word(self):
            return self.getToken(BKOOLParser.Array_word, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def array_list(self):
            return self.getTypedRuleContext(BKOOLParser.Array_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_multi_ArrayLIT

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulti_ArrayLIT" ):
                return visitor.visitMulti_ArrayLIT(self)
            else:
                return visitor.visitChildren(self)




    def multi_ArrayLIT(self):

        localctx = BKOOLParser.Multi_ArrayLITContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_multi_ArrayLIT)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self.match(BKOOLParser.Array_word)
            self.state = 500
            self.match(BKOOLParser.LP)
            self.state = 502
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.Array_word:
                self.state = 501
                self.array_list()


            self.state = 504
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayLIT(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ArrayLITContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ArrayLITContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMA)
            else:
                return self.getToken(BKOOLParser.COMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list" ):
                return visitor.visitArray_list(self)
            else:
                return visitor.visitChildren(self)




    def array_list(self):

        localctx = BKOOLParser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_array_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self.arrayLIT()
            self.state = 511
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMA:
                self.state = 507
                self.match(BKOOLParser.COMA)
                self.state = 508
                self.arrayLIT()
                self.state = 513
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLITContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Array_word(self):
            return self.getToken(BKOOLParser.Array_word, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def element_list(self):
            return self.getTypedRuleContext(BKOOLParser.Element_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_arrayLIT

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLIT" ):
                return visitor.visitArrayLIT(self)
            else:
                return visitor.visitChildren(self)




    def arrayLIT(self):

        localctx = BKOOLParser.ArrayLITContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_arrayLIT)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.match(BKOOLParser.Array_word)
            self.state = 515
            self.match(BKOOLParser.LP)
            self.state = 517
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Array_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.Self_word) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.Sub) | (1 << BKOOLParser.Not) | (1 << BKOOLParser.BOOLEANLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (BKOOLParser.CLASS - 75)) | (1 << (BKOOLParser.KEYWORD_NEW - 75)) | (1 << (BKOOLParser.THIS - 75)) | (1 << (BKOOLParser.LP - 75)))) != 0):
                self.state = 516
                self.element_list()


            self.state = 519
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ElementsContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ElementsContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMA)
            else:
                return self.getToken(BKOOLParser.COMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_element_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_list" ):
                return visitor.visitElement_list(self)
            else:
                return visitor.visitChildren(self)




    def element_list(self):

        localctx = BKOOLParser.Element_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_element_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self.elements()
            self.state = 526
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMA:
                self.state = 522
                self.match(BKOOLParser.COMA)
                self.state = 523
                self.elements()
                self.state = 528
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElements" ):
                return visitor.visitElements(self)
            else:
                return visitor.visitChildren(self)




    def elements(self):

        localctx = BKOOLParser.ElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_elements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[35] = self.adding_expr_sempred
        self._predicates[36] = self.multiplying_expr_sempred
        self._predicates[39] = self.index_expr_sempred
        self._predicates[40] = self.member_access_in_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def adding_expr_sempred(self, localctx:Adding_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def multiplying_expr_sempred(self, localctx:Multiplying_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def index_expr_sempred(self, localctx:Index_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def member_access_in_sempred(self, localctx:Member_access_inContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




