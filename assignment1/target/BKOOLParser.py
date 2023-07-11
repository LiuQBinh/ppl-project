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
        buf.write("\u0219\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\3\2\6\2j\n\2\r\2\16\2k\3\2\3\2\3\2\5\2q\n\2\3\3\3\3\3")
        buf.write("\3\3\3\5\3w\n\3\3\3\3\3\7\3{\n\3\f\3\16\3~\13\3\3\3\3")
        buf.write("\3\3\4\3\4\3\5\3\5\3\5\5\5\u0087\n\5\3\6\3\6\3\6\5\6\u008c")
        buf.write("\n\6\3\6\3\6\3\6\3\7\5\7\u0092\n\7\3\7\5\7\u0095\n\7\3")
        buf.write("\7\3\7\3\7\3\7\5\7\u009b\n\7\3\7\3\7\3\b\5\b\u00a0\n\b")
        buf.write("\3\b\5\b\u00a3\n\b\3\b\3\b\5\b\u00a7\n\b\3\b\3\b\3\b\5")
        buf.write("\b\u00ac\n\b\3\b\3\b\3\b\3\t\3\t\3\t\7\t\u00b4\n\t\f\t")
        buf.write("\16\t\u00b7\13\t\3\t\5\t\u00ba\n\t\3\n\3\n\3\n\5\n\u00bf")
        buf.write("\n\n\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00c7\n\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00d2\n")
        buf.write("\13\5\13\u00d4\n\13\3\13\3\13\5\13\u00d8\n\13\3\f\3\f")
        buf.write("\3\f\7\f\u00dd\n\f\f\f\16\f\u00e0\13\f\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\5\16\u00ea\n\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\5\17\u00f3\n\17\3\17\3\17\3\20\3")
        buf.write("\20\3\20\3\20\5\20\u00fb\n\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u0108\n\21\f\21\16")
        buf.write("\21\u010b\13\21\3\21\3\21\5\21\u010f\n\21\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\5\23\u0121\n\23\3\23\3\23\5\23\u0125\n")
        buf.write("\23\3\23\5\23\u0128\n\23\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\5\25\u0130\n\25\3\25\3\25\3\26\3\26\3\26\5\26\u0137\n")
        buf.write("\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31\5\31\u0140\n\31")
        buf.write("\3\31\3\31\3\32\3\32\5\32\u0146\n\32\3\33\3\33\3\34\3")
        buf.write("\34\3\34\7\34\u014d\n\34\f\34\16\34\u0150\13\34\3\35\3")
        buf.write("\35\3\36\3\36\3\36\7\36\u0157\n\36\f\36\16\36\u015a\13")
        buf.write("\36\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0162\n\37\3 \3")
        buf.write(" \3 \7 \u0167\n \f \16 \u016a\13 \3!\3!\3\"\3\"\3\"\3")
        buf.write("\"\3\"\5\"\u0173\n\"\3#\3#\3#\3#\3#\5#\u017a\n#\3$\3$")
        buf.write("\3$\3$\3$\5$\u0181\n$\3%\3%\3%\3%\3%\3%\7%\u0189\n%\f")
        buf.write("%\16%\u018c\13%\3&\3&\3&\3&\3&\3&\7&\u0194\n&\f&\16&\u0197")
        buf.write("\13&\3\'\3\'\3\'\5\'\u019c\n\'\3(\3(\3(\5(\u01a1\n(\3")
        buf.write(")\3)\3)\3)\3)\3)\3)\3)\6)\u01ab\n)\r)\16)\u01ac\7)\u01af")
        buf.write("\n)\f)\16)\u01b2\13)\3*\3*\3*\3*\3*\3*\3*\3*\5*\u01bc")
        buf.write("\n*\3*\5*\u01bf\n*\7*\u01c1\n*\f*\16*\u01c4\13*\3+\3+")
        buf.write("\3+\3+\3+\5+\u01cb\n+\3+\5+\u01ce\n+\3+\5+\u01d1\n+\3")
        buf.write(",\3,\3,\3,\5,\u01d7\n,\3,\3,\3,\5,\u01dc\n,\3-\3-\3-\3")
        buf.write("-\3-\5-\u01e3\n-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\5.\u01ef")
        buf.write("\n.\3/\3/\3/\7/\u01f4\n/\f/\16/\u01f7\13/\3\60\3\60\3")
        buf.write("\60\5\60\u01fc\n\60\3\60\3\60\3\61\3\61\3\61\7\61\u0203")
        buf.write("\n\61\f\61\16\61\u0206\13\61\3\62\3\62\3\62\5\62\u020b")
        buf.write("\n\62\3\62\3\62\3\63\3\63\3\63\7\63\u0212\n\63\f\63\16")
        buf.write("\63\u0215\13\63\3\64\3\64\3\64\2\6HJPR\65\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@")
        buf.write("BDFHJLNPRTVXZ\\^`bdf\2\f\6\2\4\4\37\37##MM\4\2\37\37#")
        buf.write("#\3\2\t\n\4\2\22\22\24\24\3\2\32\35\3\2\62\63\3\2,\61")
        buf.write("\3\2*+\3\2$%\3\2&(\2\u0234\2p\3\2\2\2\4r\3\2\2\2\6\u0081")
        buf.write("\3\2\2\2\b\u0086\3\2\2\2\n\u0088\3\2\2\2\f\u0091\3\2\2")
        buf.write("\2\16\u009f\3\2\2\2\20\u00b9\3\2\2\2\22\u00be\3\2\2\2")
        buf.write("\24\u00d7\3\2\2\2\26\u00d9\3\2\2\2\30\u00e1\3\2\2\2\32")
        buf.write("\u00e9\3\2\2\2\34\u00eb\3\2\2\2\36\u00f6\3\2\2\2 \u00fe")
        buf.write("\3\2\2\2\"\u0110\3\2\2\2$\u0124\3\2\2\2&\u0129\3\2\2\2")
        buf.write("(\u012c\3\2\2\2*\u0136\3\2\2\2,\u0138\3\2\2\2.\u013a\3")
        buf.write("\2\2\2\60\u013c\3\2\2\2\62\u0145\3\2\2\2\64\u0147\3\2")
        buf.write("\2\2\66\u0149\3\2\2\28\u0151\3\2\2\2:\u0153\3\2\2\2<\u0161")
        buf.write("\3\2\2\2>\u0163\3\2\2\2@\u016b\3\2\2\2B\u0172\3\2\2\2")
        buf.write("D\u0179\3\2\2\2F\u0180\3\2\2\2H\u0182\3\2\2\2J\u018d\3")
        buf.write("\2\2\2L\u019b\3\2\2\2N\u01a0\3\2\2\2P\u01a2\3\2\2\2R\u01b3")
        buf.write("\3\2\2\2T\u01d0\3\2\2\2V\u01db\3\2\2\2X\u01e2\3\2\2\2")
        buf.write("Z\u01ee\3\2\2\2\\\u01f0\3\2\2\2^\u01f8\3\2\2\2`\u01ff")
        buf.write("\3\2\2\2b\u0207\3\2\2\2d\u020e\3\2\2\2f\u0216\3\2\2\2")
        buf.write("hj\5\4\3\2ih\3\2\2\2jk\3\2\2\2ki\3\2\2\2kl\3\2\2\2lm\3")
        buf.write("\2\2\2mn\7\2\2\3nq\3\2\2\2oq\5\\/\2pi\3\2\2\2po\3\2\2")
        buf.write("\2q\3\3\2\2\2rs\7\3\2\2sv\5\6\4\2tu\7\5\2\2uw\5\6\4\2")
        buf.write("vt\3\2\2\2vw\3\2\2\2wx\3\2\2\2x|\7w\2\2y{\5\b\5\2zy\3")
        buf.write("\2\2\2{~\3\2\2\2|z\3\2\2\2|}\3\2\2\2}\177\3\2\2\2~|\3")
        buf.write("\2\2\2\177\u0080\7x\2\2\u0080\5\3\2\2\2\u0081\u0082\t")
        buf.write("\2\2\2\u0082\7\3\2\2\2\u0083\u0087\5\f\7\2\u0084\u0087")
        buf.write("\5\16\b\2\u0085\u0087\5\n\6\2\u0086\u0083\3\2\2\2\u0086")
        buf.write("\u0084\3\2\2\2\u0086\u0085\3\2\2\2\u0087\t\3\2\2\2\u0088")
        buf.write("\u0089\5\6\4\2\u0089\u008b\7s\2\2\u008a\u008c\5:\36\2")
        buf.write("\u008b\u008a\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008d\3")
        buf.write("\2\2\2\u008d\u008e\7t\2\2\u008e\u008f\5\20\t\2\u008f\13")
        buf.write("\3\2\2\2\u0090\u0092\7\6\2\2\u0091\u0090\3\2\2\2\u0091")
        buf.write("\u0092\3\2\2\2\u0092\u0094\3\2\2\2\u0093\u0095\7\7\2\2")
        buf.write("\u0094\u0093\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0096\3")
        buf.write("\2\2\2\u0096\u0097\5.\30\2\u0097\u009a\5\\/\2\u0098\u0099")
        buf.write("\7\21\2\2\u0099\u009b\5Z.\2\u009a\u0098\3\2\2\2\u009a")
        buf.write("\u009b\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009d\7y\2\2")
        buf.write("\u009d\r\3\2\2\2\u009e\u00a0\7\6\2\2\u009f\u009e\3\2\2")
        buf.write("\2\u009f\u00a0\3\2\2\2\u00a0\u00a2\3\2\2\2\u00a1\u00a3")
        buf.write("\7\7\2\2\u00a2\u00a1\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3")
        buf.write("\u00a6\3\2\2\2\u00a4\u00a7\5.\30\2\u00a5\u00a7\7\b\2\2")
        buf.write("\u00a6\u00a4\3\2\2\2\u00a6\u00a5\3\2\2\2\u00a7\u00a8\3")
        buf.write("\2\2\2\u00a8\u00a9\t\3\2\2\u00a9\u00ab\7s\2\2\u00aa\u00ac")
        buf.write("\5:\36\2\u00ab\u00aa\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac")
        buf.write("\u00ad\3\2\2\2\u00ad\u00ae\7t\2\2\u00ae\u00af\5\20\t\2")
        buf.write("\u00af\17\3\2\2\2\u00b0\u00ba\5\22\n\2\u00b1\u00b5\7w")
        buf.write("\2\2\u00b2\u00b4\5\22\n\2\u00b3\u00b2\3\2\2\2\u00b4\u00b7")
        buf.write("\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6")
        buf.write("\u00b8\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00ba\7x\2\2")
        buf.write("\u00b9\u00b0\3\2\2\2\u00b9\u00b1\3\2\2\2\u00ba\21\3\2")
        buf.write("\2\2\u00bb\u00bf\5\32\16\2\u00bc\u00bf\5\24\13\2\u00bd")
        buf.write("\u00bf\5\26\f\2\u00be\u00bb\3\2\2\2\u00be\u00bc\3\2\2")
        buf.write("\2\u00be\u00bd\3\2\2\2\u00bf\23\3\2\2\2\u00c0\u00c1\t")
        buf.write("\4\2\2\u00c1\u00c2\5\\/\2\u00c2\u00c3\7\66\2\2\u00c3\u00c6")
        buf.write("\5*\26\2\u00c4\u00c5\7\21\2\2\u00c5\u00c7\5> \2\u00c6")
        buf.write("\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8\3\2\2\2")
        buf.write("\u00c8\u00c9\7y\2\2\u00c9\u00d8\3\2\2\2\u00ca\u00d3\5")
        buf.write(":\36\2\u00cb\u00cc\7\66\2\2\u00cc\u00cd\7\21\2\2\u00cd")
        buf.write("\u00d1\3\2\2\2\u00ce\u00d2\5@!\2\u00cf\u00d2\5\36\20\2")
        buf.write("\u00d0\u00d2\5$\23\2\u00d1\u00ce\3\2\2\2\u00d1\u00cf\3")
        buf.write("\2\2\2\u00d1\u00d0\3\2\2\2\u00d2\u00d4\3\2\2\2\u00d3\u00cb")
        buf.write("\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5")
        buf.write("\u00d6\7y\2\2\u00d6\u00d8\3\2\2\2\u00d7\u00c0\3\2\2\2")
        buf.write("\u00d7\u00ca\3\2\2\2\u00d8\25\3\2\2\2\u00d9\u00de\5\30")
        buf.write("\r\2\u00da\u00db\7{\2\2\u00db\u00dd\5\30\r\2\u00dc\u00da")
        buf.write("\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de\u00dc\3\2\2\2\u00de")
        buf.write("\u00df\3\2\2\2\u00df\27\3\2\2\2\u00e0\u00de\3\2\2\2\u00e1")
        buf.write("\u00e2\7#\2\2\u00e2\31\3\2\2\2\u00e3\u00ea\5\34\17\2\u00e4")
        buf.write("\u00ea\5 \21\2\u00e5\u00ea\5\"\22\2\u00e6\u00ea\5&\24")
        buf.write("\2\u00e7\u00ea\5(\25\2\u00e8\u00ea\5$\23\2\u00e9\u00e3")
        buf.write("\3\2\2\2\u00e9\u00e4\3\2\2\2\u00e9\u00e5\3\2\2\2\u00e9")
        buf.write("\u00e6\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9\u00e8\3\2\2\2")
        buf.write("\u00ea\33\3\2\2\2\u00eb\u00ec\5P)\2\u00ec\u00ed\7\66\2")
        buf.write("\2\u00ed\u00ee\7\21\2\2\u00ee\u00f2\3\2\2\2\u00ef\u00f3")
        buf.write("\5@!\2\u00f0\u00f3\5\36\20\2\u00f1\u00f3\5$\23\2\u00f2")
        buf.write("\u00ef\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f1\3\2\2\2")
        buf.write("\u00f3\u00f4\3\2\2\2\u00f4\u00f5\7y\2\2\u00f5\35\3\2\2")
        buf.write("\2\u00f6\u00f7\7\13\2\2\u00f7\u00f8\5\6\4\2\u00f8\u00fa")
        buf.write("\7s\2\2\u00f9\u00fb\5> \2\u00fa\u00f9\3\2\2\2\u00fa\u00fb")
        buf.write("\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fd\7t\2\2\u00fd")
        buf.write("\37\3\2\2\2\u00fe\u00ff\7\f\2\2\u00ff\u0100\5@!\2\u0100")
        buf.write("\u0101\7\r\2\2\u0101\u0102\5\20\t\2\u0102\u0109\3\2\2")
        buf.write("\2\u0103\u0104\7\17\2\2\u0104\u0105\5@!\2\u0105\u0106")
        buf.write("\5\20\t\2\u0106\u0108\3\2\2\2\u0107\u0103\3\2\2\2\u0108")
        buf.write("\u010b\3\2\2\2\u0109\u0107\3\2\2\2\u0109\u010a\3\2\2\2")
        buf.write("\u010a\u010e\3\2\2\2\u010b\u0109\3\2\2\2\u010c\u010d\7")
        buf.write("\16\2\2\u010d\u010f\5\20\t\2\u010e\u010c\3\2\2\2\u010e")
        buf.write("\u010f\3\2\2\2\u010f!\3\2\2\2\u0110\u0111\7\20\2\2\u0111")
        buf.write("\u0112\7#\2\2\u0112\u0113\7\66\2\2\u0113\u0114\7\21\2")
        buf.write("\2\u0114\u0115\7:\2\2\u0115\u0116\3\2\2\2\u0116\u0117")
        buf.write("\t\5\2\2\u0117\u0118\7:\2\2\u0118\u0119\7\23\2\2\u0119")
        buf.write("\u011a\5\20\t\2\u011a#\3\2\2\2\u011b\u0125\5P)\2\u011c")
        buf.write("\u011d\7#\2\2\u011d\u0120\7s\2\2\u011e\u0121\5@!\2\u011f")
        buf.write("\u0121\5$\23\2\u0120\u011e\3\2\2\2\u0120\u011f\3\2\2\2")
        buf.write("\u0121\u0122\3\2\2\2\u0122\u0123\7t\2\2\u0123\u0125\3")
        buf.write("\2\2\2\u0124\u011b\3\2\2\2\u0124\u011c\3\2\2\2\u0125\u0127")
        buf.write("\3\2\2\2\u0126\u0128\7y\2\2\u0127\u0126\3\2\2\2\u0127")
        buf.write("\u0128\3\2\2\2\u0128%\3\2\2\2\u0129\u012a\7\25\2\2\u012a")
        buf.write("\u012b\7y\2\2\u012b\'\3\2\2\2\u012c\u012f\7\26\2\2\u012d")
        buf.write("\u0130\5@!\2\u012e\u0130\5$\23\2\u012f\u012d\3\2\2\2\u012f")
        buf.write("\u012e\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u0131\3\2\2\2")
        buf.write("\u0131\u0132\7y\2\2\u0132)\3\2\2\2\u0133\u0137\5.\30\2")
        buf.write("\u0134\u0137\5\60\31\2\u0135\u0137\5,\27\2\u0136\u0133")
        buf.write("\3\2\2\2\u0136\u0134\3\2\2\2\u0136\u0135\3\2\2\2\u0137")
        buf.write("+\3\2\2\2\u0138\u0139\5\6\4\2\u0139-\3\2\2\2\u013a\u013b")
        buf.write("\t\6\2\2\u013b/\3\2\2\2\u013c\u013d\5.\30\2\u013d\u013f")
        buf.write("\7u\2\2\u013e\u0140\5\64\33\2\u013f\u013e\3\2\2\2\u013f")
        buf.write("\u0140\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0142\7v\2\2")
        buf.write("\u0142\61\3\2\2\2\u0143\u0146\5.\30\2\u0144\u0146\5\60")
        buf.write("\31\2\u0145\u0143\3\2\2\2\u0145\u0144\3\2\2\2\u0146\63")
        buf.write("\3\2\2\2\u0147\u0148\7:\2\2\u0148\65\3\2\2\2\u0149\u014e")
        buf.write("\58\35\2\u014a\u014b\7{\2\2\u014b\u014d\58\35\2\u014c")
        buf.write("\u014a\3\2\2\2\u014d\u0150\3\2\2\2\u014e\u014c\3\2\2\2")
        buf.write("\u014e\u014f\3\2\2\2\u014f\67\3\2\2\2\u0150\u014e\3\2")
        buf.write("\2\2\u0151\u0152\7#\2\2\u01529\3\2\2\2\u0153\u0158\5<")
        buf.write("\37\2\u0154\u0155\7{\2\2\u0155\u0157\5<\37\2\u0156\u0154")
        buf.write("\3\2\2\2\u0157\u015a\3\2\2\2\u0158\u0156\3\2\2\2\u0158")
        buf.write("\u0159\3\2\2\2\u0159;\3\2\2\2\u015a\u0158\3\2\2\2\u015b")
        buf.write("\u015c\5*\26\2\u015c\u015d\5\\/\2\u015d\u0162\3\2\2\2")
        buf.write("\u015e\u015f\7#\2\2\u015f\u0160\7\66\2\2\u0160\u0162\5")
        buf.write("\6\4\2\u0161\u015b\3\2\2\2\u0161\u015e\3\2\2\2\u0162=")
        buf.write("\3\2\2\2\u0163\u0168\5@!\2\u0164\u0165\7{\2\2\u0165\u0167")
        buf.write("\5@!\2\u0166\u0164\3\2\2\2\u0167\u016a\3\2\2\2\u0168\u0166")
        buf.write("\3\2\2\2\u0168\u0169\3\2\2\2\u0169?\3\2\2\2\u016a\u0168")
        buf.write("\3\2\2\2\u016b\u016c\5B\"\2\u016cA\3\2\2\2\u016d\u016e")
        buf.write("\5D#\2\u016e\u016f\t\7\2\2\u016f\u0170\5D#\2\u0170\u0173")
        buf.write("\3\2\2\2\u0171\u0173\5D#\2\u0172\u016d\3\2\2\2\u0172\u0171")
        buf.write("\3\2\2\2\u0173C\3\2\2\2\u0174\u0175\5F$\2\u0175\u0176")
        buf.write("\t\b\2\2\u0176\u0177\5F$\2\u0177\u017a\3\2\2\2\u0178\u017a")
        buf.write("\5F$\2\u0179\u0174\3\2\2\2\u0179\u0178\3\2\2\2\u017aE")
        buf.write("\3\2\2\2\u017b\u017c\5H%\2\u017c\u017d\t\t\2\2\u017d\u017e")
        buf.write("\5H%\2\u017e\u0181\3\2\2\2\u017f\u0181\5H%\2\u0180\u017b")
        buf.write("\3\2\2\2\u0180\u017f\3\2\2\2\u0181G\3\2\2\2\u0182\u0183")
        buf.write("\b%\1\2\u0183\u0184\5J&\2\u0184\u018a\3\2\2\2\u0185\u0186")
        buf.write("\f\4\2\2\u0186\u0187\t\n\2\2\u0187\u0189\5J&\2\u0188\u0185")
        buf.write("\3\2\2\2\u0189\u018c\3\2\2\2\u018a\u0188\3\2\2\2\u018a")
        buf.write("\u018b\3\2\2\2\u018bI\3\2\2\2\u018c\u018a\3\2\2\2\u018d")
        buf.write("\u018e\b&\1\2\u018e\u018f\5L\'\2\u018f\u0195\3\2\2\2\u0190")
        buf.write("\u0191\f\4\2\2\u0191\u0192\t\13\2\2\u0192\u0194\5L\'\2")
        buf.write("\u0193\u0190\3\2\2\2\u0194\u0197\3\2\2\2\u0195\u0193\3")
        buf.write("\2\2\2\u0195\u0196\3\2\2\2\u0196K\3\2\2\2\u0197\u0195")
        buf.write("\3\2\2\2\u0198\u0199\7)\2\2\u0199\u019c\5L\'\2\u019a\u019c")
        buf.write("\5N(\2\u019b\u0198\3\2\2\2\u019b\u019a\3\2\2\2\u019cM")
        buf.write("\3\2\2\2\u019d\u019e\7%\2\2\u019e\u01a1\5N(\2\u019f\u01a1")
        buf.write("\5P)\2\u01a0\u019d\3\2\2\2\u01a0\u019f\3\2\2\2\u01a1O")
        buf.write("\3\2\2\2\u01a2\u01a3\b)\1\2\u01a3\u01a4\5R*\2\u01a4\u01b0")
        buf.write("\3\2\2\2\u01a5\u01aa\f\4\2\2\u01a6\u01a7\7u\2\2\u01a7")
        buf.write("\u01a8\5@!\2\u01a8\u01a9\7v\2\2\u01a9\u01ab\3\2\2\2\u01aa")
        buf.write("\u01a6\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01aa\3\2\2\2")
        buf.write("\u01ac\u01ad\3\2\2\2\u01ad\u01af\3\2\2\2\u01ae\u01a5\3")
        buf.write("\2\2\2\u01af\u01b2\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b0\u01b1")
        buf.write("\3\2\2\2\u01b1Q\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b3\u01b4")
        buf.write("\b*\1\2\u01b4\u01b5\5T+\2\u01b5\u01c2\3\2\2\2\u01b6\u01b7")
        buf.write("\f\4\2\2\u01b7\u01b8\7\64\2\2\u01b8\u01be\5T+\2\u01b9")
        buf.write("\u01bb\7s\2\2\u01ba\u01bc\5> \2\u01bb\u01ba\3\2\2\2\u01bb")
        buf.write("\u01bc\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01bf\7t\2\2")
        buf.write("\u01be\u01b9\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c1\3")
        buf.write("\2\2\2\u01c0\u01b6\3\2\2\2\u01c1\u01c4\3\2\2\2\u01c2\u01c0")
        buf.write("\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3S\3\2\2\2\u01c4\u01c2")
        buf.write("\3\2\2\2\u01c5\u01c6\5V,\2\u01c6\u01c7\7\65\2\2\u01c7")
        buf.write("\u01cd\5V,\2\u01c8\u01ca\7s\2\2\u01c9\u01cb\5> \2\u01ca")
        buf.write("\u01c9\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01cc\3\2\2\2")
        buf.write("\u01cc\u01ce\7t\2\2\u01cd\u01c8\3\2\2\2\u01cd\u01ce\3")
        buf.write("\2\2\2\u01ce\u01d1\3\2\2\2\u01cf\u01d1\5V,\2\u01d0\u01c5")
        buf.write("\3\2\2\2\u01d0\u01cf\3\2\2\2\u01d1U\3\2\2\2\u01d2\u01d3")
        buf.write("\7T\2\2\u01d3\u01d4\5V,\2\u01d4\u01d6\7s\2\2\u01d5\u01d7")
        buf.write("\5> \2\u01d6\u01d5\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01d8")
        buf.write("\3\2\2\2\u01d8\u01d9\7t\2\2\u01d9\u01dc\3\2\2\2\u01da")
        buf.write("\u01dc\5X-\2\u01db\u01d2\3\2\2\2\u01db\u01da\3\2\2\2\u01dc")
        buf.write("W\3\2\2\2\u01dd\u01de\7s\2\2\u01de\u01df\5@!\2\u01df\u01e0")
        buf.write("\7t\2\2\u01e0\u01e3\3\2\2\2\u01e1\u01e3\5Z.\2\u01e2\u01dd")
        buf.write("\3\2\2\2\u01e2\u01e1\3\2\2\2\u01e3Y\3\2\2\2\u01e4\u01ef")
        buf.write("\7:\2\2\u01e5\u01ef\7;\2\2\u01e6\u01ef\7\67\2\2\u01e7")
        buf.write("\u01ef\78\2\2\u01e8\u01ef\5b\62\2\u01e9\u01ef\5^\60\2")
        buf.write("\u01ea\u01ef\7#\2\2\u01eb\u01ef\7\"\2\2\u01ec\u01ef\5")
        buf.write("\6\4\2\u01ed\u01ef\7[\2\2\u01ee\u01e4\3\2\2\2\u01ee\u01e5")
        buf.write("\3\2\2\2\u01ee\u01e6\3\2\2\2\u01ee\u01e7\3\2\2\2\u01ee")
        buf.write("\u01e8\3\2\2\2\u01ee\u01e9\3\2\2\2\u01ee\u01ea\3\2\2\2")
        buf.write("\u01ee\u01eb\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ee\u01ed\3")
        buf.write("\2\2\2\u01ef[\3\2\2\2\u01f0\u01f5\7#\2\2\u01f1\u01f2\7")
        buf.write("{\2\2\u01f2\u01f4\7#\2\2\u01f3\u01f1\3\2\2\2\u01f4\u01f7")
        buf.write("\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6")
        buf.write("]\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f8\u01f9\7\36\2\2\u01f9")
        buf.write("\u01fb\7s\2\2\u01fa\u01fc\5`\61\2\u01fb\u01fa\3\2\2\2")
        buf.write("\u01fb\u01fc\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01fe\7")
        buf.write("t\2\2\u01fe_\3\2\2\2\u01ff\u0204\5b\62\2\u0200\u0201\7")
        buf.write("{\2\2\u0201\u0203\5b\62\2\u0202\u0200\3\2\2\2\u0203\u0206")
        buf.write("\3\2\2\2\u0204\u0202\3\2\2\2\u0204\u0205\3\2\2\2\u0205")
        buf.write("a\3\2\2\2\u0206\u0204\3\2\2\2\u0207\u0208\7\36\2\2\u0208")
        buf.write("\u020a\7s\2\2\u0209\u020b\5d\63\2\u020a\u0209\3\2\2\2")
        buf.write("\u020a\u020b\3\2\2\2\u020b\u020c\3\2\2\2\u020c\u020d\7")
        buf.write("t\2\2\u020dc\3\2\2\2\u020e\u0213\5f\64\2\u020f\u0210\7")
        buf.write("{\2\2\u0210\u0212\5f\64\2\u0211\u020f\3\2\2\2\u0212\u0215")
        buf.write("\3\2\2\2\u0213\u0211\3\2\2\2\u0213\u0214\3\2\2\2\u0214")
        buf.write("e\3\2\2\2\u0215\u0213\3\2\2\2\u0216\u0217\5@!\2\u0217")
        buf.write("g\3\2\2\2?kpv|\u0086\u008b\u0091\u0094\u009a\u009f\u00a2")
        buf.write("\u00a6\u00ab\u00b5\u00b9\u00be\u00c6\u00d1\u00d3\u00d7")
        buf.write("\u00de\u00e9\u00f2\u00fa\u0109\u010e\u0120\u0124\u0127")
        buf.write("\u012f\u0136\u013f\u0145\u014e\u0158\u0161\u0168\u0172")
        buf.write("\u0179\u0180\u018a\u0195\u019b\u01a0\u01ac\u01b0\u01bb")
        buf.write("\u01be\u01c2\u01ca\u01cd\u01d0\u01d6\u01db\u01e2\u01ee")
        buf.write("\u01f5\u01fb\u0204\u020a\u0213")
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


        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


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
            self.state = 110
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.Class_word]:
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
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.idlist()
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
            self.state = 112
            self.match(BKOOLParser.Class_word)
            self.state = 113
            self.class_name()
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.Extends_word:
                self.state = 114
                self.match(BKOOLParser.Extends_word)
                self.state = 115
                self.class_name()


            self.state = 118
            self.match(BKOOLParser.LB)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Static_word) | (1 << BKOOLParser.Final_word) | (1 << BKOOLParser.Void_word) | (1 << BKOOLParser.Bool_word) | (1 << BKOOLParser.Int_word) | (1 << BKOOLParser.Float_word) | (1 << BKOOLParser.Str_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.ID))) != 0) or _la==BKOOLParser.CLASS:
                self.state = 119
                self.member_lists()
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 125
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
            self.state = 127
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
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.attributes()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.methods()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 131
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
            self.state = 134
            self.class_name()
            self.state = 135
            self.match(BKOOLParser.LP)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Bool_word) | (1 << BKOOLParser.Int_word) | (1 << BKOOLParser.Float_word) | (1 << BKOOLParser.Str_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.ID))) != 0) or _la==BKOOLParser.CLASS:
                self.state = 136
                self.paramlist()


            self.state = 139
            self.match(BKOOLParser.RP)
            self.state = 140
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
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.Static_word:
                self.state = 142
                self.match(BKOOLParser.Static_word)


            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.Final_word:
                self.state = 145
                self.match(BKOOLParser.Final_word)


            self.state = 148
            self.primitive_Type()
            self.state = 149
            self.idlist()
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.Assign_op:
                self.state = 150
                self.match(BKOOLParser.Assign_op)
                self.state = 151
                self.operands()


            self.state = 154
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
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.Static_word:
                self.state = 156
                self.match(BKOOLParser.Static_word)


            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.Final_word:
                self.state = 159
                self.match(BKOOLParser.Final_word)


            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.Bool_word, BKOOLParser.Int_word, BKOOLParser.Float_word, BKOOLParser.Str_word]:
                self.state = 162
                self.primitive_Type()
                pass
            elif token in [BKOOLParser.Void_word]:
                self.state = 163
                self.match(BKOOLParser.Void_word)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 166
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.Main_word or _la==BKOOLParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 167
            self.match(BKOOLParser.LP)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Bool_word) | (1 << BKOOLParser.Int_word) | (1 << BKOOLParser.Float_word) | (1 << BKOOLParser.Str_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.ID))) != 0) or _la==BKOOLParser.CLASS:
                self.state = 168
                self.paramlist()


            self.state = 171
            self.match(BKOOLParser.RP)
            self.state = 172
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
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.Prog_word, BKOOLParser.Var_word, BKOOLParser.Val_word, BKOOLParser.If_word, BKOOLParser.For_word, BKOOLParser.Break_word, BKOOLParser.Return_word, BKOOLParser.Bool_word, BKOOLParser.Int_word, BKOOLParser.Float_word, BKOOLParser.Str_word, BKOOLParser.Array_word, BKOOLParser.Main_word, BKOOLParser.Self_word, BKOOLParser.ID, BKOOLParser.BOOLEANLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.CLASS, BKOOLParser.KEYWORD_NEW, BKOOLParser.THIS, BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.block_stmt_list()
                pass
            elif token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.match(BKOOLParser.LB)
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Var_word) | (1 << BKOOLParser.Val_word) | (1 << BKOOLParser.If_word) | (1 << BKOOLParser.For_word) | (1 << BKOOLParser.Break_word) | (1 << BKOOLParser.Return_word) | (1 << BKOOLParser.Bool_word) | (1 << BKOOLParser.Int_word) | (1 << BKOOLParser.Float_word) | (1 << BKOOLParser.Str_word) | (1 << BKOOLParser.Array_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.Self_word) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.BOOLEANLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (BKOOLParser.CLASS - 75)) | (1 << (BKOOLParser.KEYWORD_NEW - 75)) | (1 << (BKOOLParser.THIS - 75)) | (1 << (BKOOLParser.LP - 75)))) != 0):
                    self.state = 176
                    self.block_stmt_list()
                    self.state = 181
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 182
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
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 185
                self.stmt()
                pass

            elif la_ == 2:
                self.state = 186
                self.var_cons_decl()
                pass

            elif la_ == 3:
                self.state = 187
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
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.Var_word, BKOOLParser.Val_word]:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.Var_word or _la==BKOOLParser.Val_word):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 191
                self.idlist()
                self.state = 192
                self.match(BKOOLParser.Colon)
                self.state = 193
                self.types()
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.Assign_op:
                    self.state = 194
                    self.match(BKOOLParser.Assign_op)
                    self.state = 195
                    self.expr_list()


                self.state = 198
                self.match(BKOOLParser.SEMI)
                pass
            elif token in [BKOOLParser.Prog_word, BKOOLParser.Bool_word, BKOOLParser.Int_word, BKOOLParser.Float_word, BKOOLParser.Str_word, BKOOLParser.Main_word, BKOOLParser.ID, BKOOLParser.CLASS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self.paramlist()
                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.Colon:
                    self.state = 201
                    self.match(BKOOLParser.Colon)
                    self.state = 202
                    self.match(BKOOLParser.Assign_op)
                    self.state = 207
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        self.state = 204
                        self.expr()
                        pass

                    elif la_ == 2:
                        self.state = 205
                        self.new_val_from_class_stmt()
                        pass

                    elif la_ == 3:
                        self.state = 206
                        self.invocation_stmt()
                        pass




                self.state = 211
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
            self.state = 215
            self.var_cons_name()
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMA:
                self.state = 216
                self.match(BKOOLParser.COMA)
                self.state = 217
                self.var_cons_name()
                self.state = 222
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
            self.state = 223
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
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.as_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self.loop_for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 228
                self.break_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 229
                self.return_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 230
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
            self.state = 233
            self.index_expr(0)

            self.state = 234
            self.match(BKOOLParser.Colon)
            self.state = 235
            self.match(BKOOLParser.Assign_op)
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 237
                self.expr()
                pass

            elif la_ == 2:
                self.state = 238
                self.new_val_from_class_stmt()
                pass

            elif la_ == 3:
                self.state = 239
                self.invocation_stmt()
                pass


            self.state = 242
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
            self.state = 244
            self.match(BKOOLParser.Keyword_new)
            self.state = 245
            self.class_name()
            self.state = 246
            self.match(BKOOLParser.LP)
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Array_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.Self_word) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.Sub) | (1 << BKOOLParser.Not) | (1 << BKOOLParser.BOOLEANLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (BKOOLParser.CLASS - 75)) | (1 << (BKOOLParser.KEYWORD_NEW - 75)) | (1 << (BKOOLParser.THIS - 75)) | (1 << (BKOOLParser.LP - 75)))) != 0):
                self.state = 247
                self.expr_list()


            self.state = 250
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
            self.state = 252
            self.match(BKOOLParser.If_word)
            self.state = 253
            self.expr()
            self.state = 254
            self.match(BKOOLParser.Then_word)
            self.state = 255
            self.block_stmt()
            self.state = 263
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 257
                    self.match(BKOOLParser.Elseif_word)
                    self.state = 258
                    self.expr()
                    self.state = 259
                    self.block_stmt() 
                self.state = 265
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 266
                self.match(BKOOLParser.Else_word)
                self.state = 267
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
            self.state = 270
            self.match(BKOOLParser.For_word)

            self.state = 271
            self.match(BKOOLParser.ID)
            self.state = 272
            self.match(BKOOLParser.Colon)
            self.state = 273
            self.match(BKOOLParser.Assign_op)
            self.state = 274
            self.match(BKOOLParser.INTLIT)
            self.state = 276
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.To_word or _la==BKOOLParser.Down_to_word):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()

            self.state = 277
            self.match(BKOOLParser.INTLIT)
            self.state = 278
            self.match(BKOOLParser.Do_word)
            self.state = 279
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
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 281
                self.index_expr(0)
                pass

            elif la_ == 2:
                self.state = 282
                self.match(BKOOLParser.ID)
                self.state = 283
                self.match(BKOOLParser.LP)
                self.state = 286
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 284
                    self.expr()
                    pass

                elif la_ == 2:
                    self.state = 285
                    self.invocation_stmt()
                    pass


                self.state = 288
                self.match(BKOOLParser.RP)
                pass


            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 292
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
            self.state = 295
            self.match(BKOOLParser.Break_word)
            self.state = 296
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
            self.state = 298
            self.match(BKOOLParser.Return_word)
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 299
                self.expr()

            elif la_ == 2:
                self.state = 300
                self.invocation_stmt()


            self.state = 303
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
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.primitive_Type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                self.array_Type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 307
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
            self.state = 310
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
            self.state = 312
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
            self.state = 314
            self.primitive_Type()
            self.state = 315
            self.match(BKOOLParser.LSB)
            self.state = 317
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.INTLIT:
                self.state = 316
                self.array_size()


            self.state = 319
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
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.primitive_Type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
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
            self.state = 325
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
            self.state = 327
            self.attribute_name()
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMA:
                self.state = 328
                self.match(BKOOLParser.COMA)
                self.state = 329
                self.attribute_name()
                self.state = 334
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
            self.state = 335
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
            self.state = 337
            self.param_decl()
            self.state = 342
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMA:
                self.state = 338
                self.match(BKOOLParser.COMA)
                self.state = 339
                self.param_decl()
                self.state = 344
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
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.types()
                self.state = 346
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.match(BKOOLParser.ID)
                self.state = 349
                self.match(BKOOLParser.Colon)
                self.state = 350
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
            self.state = 353
            self.expr()
            self.state = 358
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMA:
                self.state = 354
                self.match(BKOOLParser.COMA)
                self.state = 355
                self.expr()
                self.state = 360
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
            self.state = 361
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
            self.state = 368
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 363
                self.relational_expr()
                self.state = 364
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.String_comp or _la==BKOOLParser.String_concat):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 365
                self.relational_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 367
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
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                self.logical_expr()
                self.state = 371
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Equal) | (1 << BKOOLParser.Diff) | (1 << BKOOLParser.Greater) | (1 << BKOOLParser.Lesser) | (1 << BKOOLParser.Greater_euqal) | (1 << BKOOLParser.Lesser_equal))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 372
                self.logical_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 374
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
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                self.adding_expr(0)
                self.state = 378
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.And or _la==BKOOLParser.Or):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 379
                self.adding_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
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
            self.state = 385
            self.multiplying_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 392
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Adding_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_expr)
                    self.state = 387
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 388
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.Add or _la==BKOOLParser.Sub):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 389
                    self.multiplying_expr(0) 
                self.state = 394
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

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
            self.state = 396
            self.logical_not_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 403
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Multiplying_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expr)
                    self.state = 398
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 399
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Mul) | (1 << BKOOLParser.Div) | (1 << BKOOLParser.Mod))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 400
                    self.logical_not_expr() 
                self.state = 405
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

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
            self.state = 409
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.Not]:
                self.enterOuterAlt(localctx, 1)
                self.state = 406
                self.match(BKOOLParser.Not)
                self.state = 407
                self.logical_not_expr()
                pass
            elif token in [BKOOLParser.Prog_word, BKOOLParser.Array_word, BKOOLParser.Main_word, BKOOLParser.Self_word, BKOOLParser.ID, BKOOLParser.Sub, BKOOLParser.BOOLEANLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.CLASS, BKOOLParser.KEYWORD_NEW, BKOOLParser.THIS, BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
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
            self.state = 414
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.Sub]:
                self.enterOuterAlt(localctx, 1)
                self.state = 411
                self.match(BKOOLParser.Sub)
                self.state = 412
                self.sign_expr()
                pass
            elif token in [BKOOLParser.Prog_word, BKOOLParser.Array_word, BKOOLParser.Main_word, BKOOLParser.Self_word, BKOOLParser.ID, BKOOLParser.BOOLEANLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.CLASS, BKOOLParser.KEYWORD_NEW, BKOOLParser.THIS, BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
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
            self.state = 417
            self.member_access_in(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 430
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Index_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_expr)
                    self.state = 419
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 424 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 420
                            self.match(BKOOLParser.LSB)
                            self.state = 421
                            self.expr()
                            self.state = 422
                            self.match(BKOOLParser.RSB)

                        else:
                            raise NoViableAltException(self)
                        self.state = 426 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
             
                self.state = 432
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

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
            self.state = 434
            self.member_access_out()
            self._ctx.stop = self._input.LT(-1)
            self.state = 448
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Member_access_inContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_member_access_in)
                    self.state = 436
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 437
                    self.match(BKOOLParser.Member_access_in)
                    self.state = 438
                    self.member_access_out()
                    self.state = 444
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                    if la_ == 1:
                        self.state = 439
                        self.match(BKOOLParser.LP)
                        self.state = 441
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Array_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.Self_word) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.Sub) | (1 << BKOOLParser.Not) | (1 << BKOOLParser.BOOLEANLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (BKOOLParser.CLASS - 75)) | (1 << (BKOOLParser.KEYWORD_NEW - 75)) | (1 << (BKOOLParser.THIS - 75)) | (1 << (BKOOLParser.LP - 75)))) != 0):
                            self.state = 440
                            self.expr_list()


                        self.state = 443
                        self.match(BKOOLParser.RP)

             
                self.state = 450
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

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
            self.state = 462
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 451
                self.class_expr()
                self.state = 452
                self.match(BKOOLParser.Member_access_out)
                self.state = 453
                self.class_expr()
                self.state = 459
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
                if la_ == 1:
                    self.state = 454
                    self.match(BKOOLParser.LP)
                    self.state = 456
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Array_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.Self_word) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.Sub) | (1 << BKOOLParser.Not) | (1 << BKOOLParser.BOOLEANLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (BKOOLParser.CLASS - 75)) | (1 << (BKOOLParser.KEYWORD_NEW - 75)) | (1 << (BKOOLParser.THIS - 75)) | (1 << (BKOOLParser.LP - 75)))) != 0):
                        self.state = 455
                        self.expr_list()


                    self.state = 458
                    self.match(BKOOLParser.RP)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 461
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
            self.state = 473
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.KEYWORD_NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 464
                self.match(BKOOLParser.KEYWORD_NEW)
                self.state = 465
                self.class_expr()
                self.state = 466
                self.match(BKOOLParser.LP)
                self.state = 468
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Array_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.Self_word) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.Sub) | (1 << BKOOLParser.Not) | (1 << BKOOLParser.BOOLEANLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (BKOOLParser.CLASS - 75)) | (1 << (BKOOLParser.KEYWORD_NEW - 75)) | (1 << (BKOOLParser.THIS - 75)) | (1 << (BKOOLParser.LP - 75)))) != 0):
                    self.state = 467
                    self.expr_list()


                self.state = 470
                self.match(BKOOLParser.RP)
                pass
            elif token in [BKOOLParser.Prog_word, BKOOLParser.Array_word, BKOOLParser.Main_word, BKOOLParser.Self_word, BKOOLParser.ID, BKOOLParser.BOOLEANLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.CLASS, BKOOLParser.THIS, BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 472
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
            self.state = 480
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 475
                self.match(BKOOLParser.LP)
                self.state = 476
                self.expr()
                self.state = 477
                self.match(BKOOLParser.RP)
                pass
            elif token in [BKOOLParser.Prog_word, BKOOLParser.Array_word, BKOOLParser.Main_word, BKOOLParser.Self_word, BKOOLParser.ID, BKOOLParser.BOOLEANLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.CLASS, BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 479
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
            self.state = 492
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 482
                self.match(BKOOLParser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 483
                self.match(BKOOLParser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 484
                self.match(BKOOLParser.BOOLEANLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 485
                self.match(BKOOLParser.STRINGLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 486
                self.arrayLIT()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 487
                self.multi_ArrayLIT()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 488
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 489
                self.match(BKOOLParser.Self_word)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 490
                self.class_name()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 491
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
            self.state = 494
            self.match(BKOOLParser.ID)
            self.state = 499
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 495
                    self.match(BKOOLParser.COMA)
                    self.state = 496
                    self.match(BKOOLParser.ID) 
                self.state = 501
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

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
            self.state = 502
            self.match(BKOOLParser.Array_word)
            self.state = 503
            self.match(BKOOLParser.LP)
            self.state = 505
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.Array_word:
                self.state = 504
                self.array_list()


            self.state = 507
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
            self.state = 509
            self.arrayLIT()
            self.state = 514
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMA:
                self.state = 510
                self.match(BKOOLParser.COMA)
                self.state = 511
                self.arrayLIT()
                self.state = 516
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
            self.state = 517
            self.match(BKOOLParser.Array_word)
            self.state = 518
            self.match(BKOOLParser.LP)
            self.state = 520
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Array_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.Self_word) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.Sub) | (1 << BKOOLParser.Not) | (1 << BKOOLParser.BOOLEANLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (BKOOLParser.CLASS - 75)) | (1 << (BKOOLParser.KEYWORD_NEW - 75)) | (1 << (BKOOLParser.THIS - 75)) | (1 << (BKOOLParser.LP - 75)))) != 0):
                self.state = 519
                self.element_list()


            self.state = 522
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
            self.state = 524
            self.elements()
            self.state = 529
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMA:
                self.state = 525
                self.match(BKOOLParser.COMA)
                self.state = 526
                self.elements()
                self.state = 531
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
            self.state = 532
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
         




