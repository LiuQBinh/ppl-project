# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


    from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2z")
        buf.write("\u0365\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4")
        buf.write("g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\4o\to\4")
        buf.write("p\tp\4q\tq\4r\tr\4s\ts\4t\tt\4u\tu\4v\tv\4w\tw\4x\tx\4")
        buf.write("y\ty\4z\tz\4{\t{\4|\t|\4}\t}\4~\t~\4\177\t\177\4\u0080")
        buf.write("\t\u0080\4\u0081\t\u0081\4\u0082\t\u0082\4\u0083\t\u0083")
        buf.write("\4\u0084\t\u0084\4\u0085\t\u0085\4\u0086\t\u0086\4\u0087")
        buf.write("\t\u0087\4\u0088\t\u0088\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3")
        buf.write("\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3")
        buf.write("\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\7\21\u0134\n\21\f\21\16\21\u0137\13\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\7\22\u013f\n\22\f\22\16\22\u0142")
        buf.write("\13\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\7\23\u014b\n")
        buf.write("\23\f\23\16\23\u014e\13\23\3\23\3\23\3\24\3\24\3\25\3")
        buf.write("\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\5\35\u0166\n\35\3\36\3")
        buf.write("\36\7\36\u016a\n\36\f\36\16\36\u016d\13\36\3\37\3\37\6")
        buf.write("\37\u0171\n\37\r\37\16\37\u0172\3 \3 \3!\3!\3\"\3\"\3")
        buf.write("#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3")
        buf.write("+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\63\3\63\5\63\u019d\n\63\3\64\3\64\3\64\7\64\u01a2\n")
        buf.write("\64\f\64\16\64\u01a5\13\64\3\64\3\64\3\64\3\64\7\64\u01ab")
        buf.write("\n\64\f\64\16\64\u01ae\13\64\3\64\3\64\7\64\u01b2\n\64")
        buf.write("\f\64\16\64\u01b5\13\64\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\66\3\66\5\66\u01c2\n\66\3\67\3\67\3")
        buf.write("\67\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u01cd\n\67\38\3")
        buf.write("8\38\38\38\38\38\39\39\3:\3:\3:\3;\3;\3;\3;\7;\u01df\n")
        buf.write(";\f;\16;\u01e2\13;\3;\3;\3;\3;\3;\3<\3<\3<\3<\5<\u01ed")
        buf.write("\n<\3<\3<\3=\3=\3=\3=\3=\3=\5=\u01f7\n=\3=\3=\3>\3>\3")
        buf.write("?\3?\5?\u01ff\n?\3?\6?\u0202\n?\r?\16?\u0203\3@\3@\7@")
        buf.write("\u0208\n@\f@\16@\u020b\13@\3A\3A\3A\7A\u0210\nA\fA\16")
        buf.write("A\u0213\13A\3A\5A\u0216\nA\3A\6A\u0219\nA\rA\16A\u021a")
        buf.write("\7A\u021d\nA\fA\16A\u0220\13A\5A\u0222\nA\3B\3B\3B\7B")
        buf.write("\u0227\nB\fB\16B\u022a\13B\3C\3C\3C\3C\7C\u0230\nC\fC")
        buf.write("\16C\u0233\13C\3D\3D\3D\3D\7D\u0239\nD\fD\16D\u023c\13")
        buf.write("D\3E\3E\3E\3E\3E\3E\3E\3E\3F\3F\3F\3F\3F\3G\3G\3G\3G\3")
        buf.write("G\3G\3G\3G\3H\3H\3H\3H\3H\3H\3I\3I\3I\3I\3I\3I\3I\3I\3")
        buf.write("I\3J\3J\3J\3K\3K\3K\3K\3K\3K\3K\3L\3L\3L\3L\3L\3M\3M\3")
        buf.write("M\3M\3N\3N\3N\3N\3N\3O\3O\3O\3O\3O\3O\3P\3P\3P\3P\3P\3")
        buf.write("P\3Q\3Q\3Q\3R\3R\3R\3R\3S\3S\3S\3S\3S\3S\3T\3T\3T\3T\3")
        buf.write("T\3T\3T\3T\3U\3U\3U\3U\3U\3U\3U\3V\3V\3V\3V\3V\3V\3W\3")
        buf.write("W\3W\3W\3W\3X\3X\3X\3X\3Y\3Y\3Y\3Y\3Z\3Z\3Z\3Z\3Z\3[\3")
        buf.write("[\3[\3[\3[\3[\3[\3[\3[\3[\3[\3[\3\\\3\\\3\\\3\\\3\\\3")
        buf.write("\\\3\\\3\\\3\\\3\\\3\\\3]\3]\3]\3]\3^\3^\3^\3_\3_\3_\3")
        buf.write("`\3`\3`\3`\3`\3`\3`\3a\3a\3a\3a\3a\3b\3b\3b\3b\3b\3c\3")
        buf.write("c\3c\3c\3d\3d\3d\3d\3d\3e\3e\3e\3e\3e\3e\3f\3f\3f\3f\3")
        buf.write("f\3f\3f\3g\3g\3g\3h\3h\3h\3h\3h\3h\3h\3i\3i\3j\3j\3k\3")
        buf.write("k\3l\3l\3m\3m\3n\3n\3o\3o\3o\3p\3p\3p\3q\3q\3q\3r\3r\3")
        buf.write("r\3s\3s\3t\3t\3u\3u\3v\3v\3v\3w\3w\3w\3x\3x\3x\3x\3y\3")
        buf.write("y\3y\3z\3z\3{\3{\3{\3|\3|\3}\3}\3~\3~\3\177\3\177\3\u0080")
        buf.write("\3\u0080\3\u0081\3\u0081\3\u0082\3\u0082\3\u0083\3\u0083")
        buf.write("\3\u0084\3\u0084\3\u0085\3\u0085\3\u0086\6\u0086\u0351")
        buf.write("\n\u0086\r\u0086\16\u0086\u0352\3\u0086\3\u0086\3\u0087")
        buf.write("\3\u0087\3\u0087\3\u0087\7\u0087\u035b\n\u0087\f\u0087")
        buf.write("\16\u0087\u035e\13\u0087\3\u0087\3\u0087\3\u0087\3\u0088")
        buf.write("\3\u0088\3\u0088\5\u0140\u01e0\u035c\2\u0089\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\2=\2?\37A C!E\"G#I$K%M&O\'Q(S)U*")
        buf.write("W+Y,[-]._/a\60c\61e\62g\63i\2k\2m\2o\2q\2s\2u\64w\65y")
        buf.write("\66{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089")
        buf.write("\67\u008b8\u008d9\u008f:\u0091;\u0093<\u0095=\u0097>\u0099")
        buf.write("?\u009b@\u009dA\u009fB\u00a1C\u00a3D\u00a5E\u00a7F\u00a9")
        buf.write("G\u00abH\u00adI\u00afJ\u00b1K\u00b3L\u00b5M\u00b7N\u00b9")
        buf.write("O\u00bbP\u00bdQ\u00bfR\u00c1S\u00c3T\u00c5U\u00c7V\u00c9")
        buf.write("W\u00cbX\u00cdY\u00cfZ\u00d1[\u00d3\\\u00d5]\u00d7^\u00d9")
        buf.write("_\u00db`\u00dda\u00dfb\u00e1c\u00e3d\u00e5e\u00e7f\u00e9")
        buf.write("g\u00ebh\u00edi\u00efj\u00f1k\u00f3l\u00f5m\u00f7n\u00f9")
        buf.write("o\u00fbp\u00fdq\u00ffr\u0101s\u0103t\u0105u\u0107v\u0109")
        buf.write("w\u010bx\u010dy\u010fz\3\2\25\4\2\f\f\17\17\5\2C\\aac")
        buf.write("|\6\2\62;C\\aac|\3\2$$\t\2))^^ddhhppttvv\5\2\62;CHch\4")
        buf.write("\2GGgg\4\2--//\3\2\62;\3\2\63;\3\2\629\4\2\629aa\4\2Z")
        buf.write("Zzz\4\2\62;CH\5\2\62;CHaa\4\2DDdd\3\2\62\63\4\2\62\63")
        buf.write("aa\5\2\n\f\16\17\"\"\2\u0379\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2?\3\2\2")
        buf.write("\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2")
        buf.write("\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3")
        buf.write("\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]")
        buf.write("\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2")
        buf.write("g\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2\u0089\3\2")
        buf.write("\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2")
        buf.write("\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2")
        buf.write("\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5")
        buf.write("\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2")
        buf.write("\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3")
        buf.write("\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2")
        buf.write("\2\2\u00bb\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2\2\2\u00c1")
        buf.write("\3\2\2\2\2\u00c3\3\2\2\2\2\u00c5\3\2\2\2\2\u00c7\3\2\2")
        buf.write("\2\2\u00c9\3\2\2\2\2\u00cb\3\2\2\2\2\u00cd\3\2\2\2\2\u00cf")
        buf.write("\3\2\2\2\2\u00d1\3\2\2\2\2\u00d3\3\2\2\2\2\u00d5\3\2\2")
        buf.write("\2\2\u00d7\3\2\2\2\2\u00d9\3\2\2\2\2\u00db\3\2\2\2\2\u00dd")
        buf.write("\3\2\2\2\2\u00df\3\2\2\2\2\u00e1\3\2\2\2\2\u00e3\3\2\2")
        buf.write("\2\2\u00e5\3\2\2\2\2\u00e7\3\2\2\2\2\u00e9\3\2\2\2\2\u00eb")
        buf.write("\3\2\2\2\2\u00ed\3\2\2\2\2\u00ef\3\2\2\2\2\u00f1\3\2\2")
        buf.write("\2\2\u00f3\3\2\2\2\2\u00f5\3\2\2\2\2\u00f7\3\2\2\2\2\u00f9")
        buf.write("\3\2\2\2\2\u00fb\3\2\2\2\2\u00fd\3\2\2\2\2\u00ff\3\2\2")
        buf.write("\2\2\u0101\3\2\2\2\2\u0103\3\2\2\2\2\u0105\3\2\2\2\2\u0107")
        buf.write("\3\2\2\2\2\u0109\3\2\2\2\2\u010b\3\2\2\2\2\u010d\3\2\2")
        buf.write("\2\2\u010f\3\2\2\2\3\u0111\3\2\2\2\5\u0113\3\2\2\2\7\u0115")
        buf.write("\3\2\2\2\t\u0117\3\2\2\2\13\u0119\3\2\2\2\r\u011b\3\2")
        buf.write("\2\2\17\u011d\3\2\2\2\21\u011f\3\2\2\2\23\u0121\3\2\2")
        buf.write("\2\25\u0123\3\2\2\2\27\u0125\3\2\2\2\31\u0127\3\2\2\2")
        buf.write("\33\u0129\3\2\2\2\35\u012b\3\2\2\2\37\u012d\3\2\2\2!\u012f")
        buf.write("\3\2\2\2#\u013a\3\2\2\2%\u0148\3\2\2\2\'\u0151\3\2\2\2")
        buf.write(")\u0153\3\2\2\2+\u0155\3\2\2\2-\u0157\3\2\2\2/\u0159\3")
        buf.write("\2\2\2\61\u015b\3\2\2\2\63\u015d\3\2\2\2\65\u015f\3\2")
        buf.write("\2\2\67\u0161\3\2\2\29\u0165\3\2\2\2;\u0167\3\2\2\2=\u016e")
        buf.write("\3\2\2\2?\u0174\3\2\2\2A\u0176\3\2\2\2C\u0178\3\2\2\2")
        buf.write("E\u017a\3\2\2\2G\u017c\3\2\2\2I\u017e\3\2\2\2K\u0180\3")
        buf.write("\2\2\2M\u0182\3\2\2\2O\u0184\3\2\2\2Q\u0186\3\2\2\2S\u0188")
        buf.write("\3\2\2\2U\u018a\3\2\2\2W\u018c\3\2\2\2Y\u018e\3\2\2\2")
        buf.write("[\u0190\3\2\2\2]\u0192\3\2\2\2_\u0194\3\2\2\2a\u0196\3")
        buf.write("\2\2\2c\u0198\3\2\2\2e\u019c\3\2\2\2g\u019e\3\2\2\2i\u01b9")
        buf.write("\3\2\2\2k\u01c1\3\2\2\2m\u01cc\3\2\2\2o\u01ce\3\2\2\2")
        buf.write("q\u01d5\3\2\2\2s\u01d7\3\2\2\2u\u01da\3\2\2\2w\u01ec\3")
        buf.write("\2\2\2y\u01f0\3\2\2\2{\u01fa\3\2\2\2}\u01fc\3\2\2\2\177")
        buf.write("\u0205\3\2\2\2\u0081\u0221\3\2\2\2\u0083\u0223\3\2\2\2")
        buf.write("\u0085\u022b\3\2\2\2\u0087\u0234\3\2\2\2\u0089\u023d\3")
        buf.write("\2\2\2\u008b\u0245\3\2\2\2\u008d\u024a\3\2\2\2\u008f\u0252")
        buf.write("\3\2\2\2\u0091\u0258\3\2\2\2\u0093\u0261\3\2\2\2\u0095")
        buf.write("\u0264\3\2\2\2\u0097\u026b\3\2\2\2\u0099\u0270\3\2\2\2")
        buf.write("\u009b\u0274\3\2\2\2\u009d\u0279\3\2\2\2\u009f\u027f\3")
        buf.write("\2\2\2\u00a1\u0285\3\2\2\2\u00a3\u0288\3\2\2\2\u00a5\u028c")
        buf.write("\3\2\2\2\u00a7\u0292\3\2\2\2\u00a9\u029a\3\2\2\2\u00ab")
        buf.write("\u02a1\3\2\2\2\u00ad\u02a7\3\2\2\2\u00af\u02ac\3\2\2\2")
        buf.write("\u00b1\u02b0\3\2\2\2\u00b3\u02b4\3\2\2\2\u00b5\u02b9\3")
        buf.write("\2\2\2\u00b7\u02c5\3\2\2\2\u00b9\u02d0\3\2\2\2\u00bb\u02d4")
        buf.write("\3\2\2\2\u00bd\u02d7\3\2\2\2\u00bf\u02da\3\2\2\2\u00c1")
        buf.write("\u02e1\3\2\2\2\u00c3\u02e6\3\2\2\2\u00c5\u02eb\3\2\2\2")
        buf.write("\u00c7\u02ef\3\2\2\2\u00c9\u02f4\3\2\2\2\u00cb\u02fa\3")
        buf.write("\2\2\2\u00cd\u0301\3\2\2\2\u00cf\u0304\3\2\2\2\u00d1\u030b")
        buf.write("\3\2\2\2\u00d3\u030d\3\2\2\2\u00d5\u030f\3\2\2\2\u00d7")
        buf.write("\u0311\3\2\2\2\u00d9\u0313\3\2\2\2\u00db\u0315\3\2\2\2")
        buf.write("\u00dd\u0317\3\2\2\2\u00df\u031a\3\2\2\2\u00e1\u031d\3")
        buf.write("\2\2\2\u00e3\u0320\3\2\2\2\u00e5\u0323\3\2\2\2\u00e7\u0325")
        buf.write("\3\2\2\2\u00e9\u0327\3\2\2\2\u00eb\u0329\3\2\2\2\u00ed")
        buf.write("\u032c\3\2\2\2\u00ef\u032f\3\2\2\2\u00f1\u0333\3\2\2\2")
        buf.write("\u00f3\u0336\3\2\2\2\u00f5\u0338\3\2\2\2\u00f7\u033b\3")
        buf.write("\2\2\2\u00f9\u033d\3\2\2\2\u00fb\u033f\3\2\2\2\u00fd\u0341")
        buf.write("\3\2\2\2\u00ff\u0343\3\2\2\2\u0101\u0345\3\2\2\2\u0103")
        buf.write("\u0347\3\2\2\2\u0105\u0349\3\2\2\2\u0107\u034b\3\2\2\2")
        buf.write("\u0109\u034d\3\2\2\2\u010b\u0350\3\2\2\2\u010d\u0356\3")
        buf.write("\2\2\2\u010f\u0362\3\2\2\2\u0111\u0112\5\u00abV\2\u0112")
        buf.write("\4\3\2\2\2\u0113\u0114\5\u0089E\2\u0114\6\3\2\2\2\u0115")
        buf.write("\u0116\5\u008dG\2\u0116\b\3\2\2\2\u0117\u0118\5\u00c3")
        buf.write("b\2\u0118\n\3\2\2\2\u0119\u011a\5\u00b1Y\2\u011a\f\3\2")
        buf.write("\2\2\u011b\u011c\5\u00afX\2\u011c\16\3\2\2\2\u011d\u011e")
        buf.write("\5\u0093J\2\u011e\20\3\2\2\2\u011f\u0120\5\u00c1a\2\u0120")
        buf.write("\22\3\2\2\2\u0121\u0122\5\u0097L\2\u0122\24\3\2\2\2\u0123")
        buf.write("\u0124\5\u0095K\2\u0124\26\3\2\2\2\u0125\u0126\5\u0099")
        buf.write("M\2\u0126\30\3\2\2\2\u0127\u0128\5\u00e5s\2\u0128\32\3")
        buf.write("\2\2\2\u0129\u012a\5\u00cdg\2\u012a\34\3\2\2\2\u012b\u012c")
        buf.write("\5\u00bd_\2\u012c\36\3\2\2\2\u012d\u012e\5\u008fH\2\u012e")
        buf.write(" \3\2\2\2\u012f\u0130\7\61\2\2\u0130\u0131\7\61\2\2\u0131")
        buf.write("\u0135\3\2\2\2\u0132\u0134\n\2\2\2\u0133\u0132\3\2\2\2")
        buf.write("\u0134\u0137\3\2\2\2\u0135\u0133\3\2\2\2\u0135\u0136\3")
        buf.write("\2\2\2\u0136\u0138\3\2\2\2\u0137\u0135\3\2\2\2\u0138\u0139")
        buf.write("\b\21\2\2\u0139\"\3\2\2\2\u013a\u013b\7\61\2\2\u013b\u013c")
        buf.write("\7,\2\2\u013c\u0140\3\2\2\2\u013d\u013f\13\2\2\2\u013e")
        buf.write("\u013d\3\2\2\2\u013f\u0142\3\2\2\2\u0140\u0141\3\2\2\2")
        buf.write("\u0140\u013e\3\2\2\2\u0141\u0143\3\2\2\2\u0142\u0140\3")
        buf.write("\2\2\2\u0143\u0144\7,\2\2\u0144\u0145\7\61\2\2\u0145\u0146")
        buf.write("\3\2\2\2\u0146\u0147\b\22\2\2\u0147$\3\2\2\2\u0148\u014c")
        buf.write("\7%\2\2\u0149\u014b\n\2\2\2\u014a\u0149\3\2\2\2\u014b")
        buf.write("\u014e\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014d\3\2\2\2")
        buf.write("\u014d\u014f\3\2\2\2\u014e\u014c\3\2\2\2\u014f\u0150\b")
        buf.write("\23\2\2\u0150&\3\2\2\2\u0151\u0152\5\u00a7T\2\u0152(\3")
        buf.write("\2\2\2\u0153\u0154\5\u00a3R\2\u0154*\3\2\2\2\u0155\u0156")
        buf.write("\5\u00a5S\2\u0156,\3\2\2\2\u0157\u0158\5\u00bf`\2\u0158")
        buf.write(".\3\2\2\2\u0159\u015a\5\u009fP\2\u015a\60\3\2\2\2\u015b")
        buf.write("\u015c\5\u008bF\2\u015c\62\3\2\2\2\u015d\u015e\5\u00b5")
        buf.write("[\2\u015e\64\3\2\2\2\u015f\u0160\5\u00b7\\\2\u0160\66")
        buf.write("\3\2\2\2\u0161\u0162\5\u00b3Z\2\u01628\3\2\2\2\u0163\u0166")
        buf.write("\5;\36\2\u0164\u0166\5=\37\2\u0165\u0163\3\2\2\2\u0165")
        buf.write("\u0164\3\2\2\2\u0166:\3\2\2\2\u0167\u016b\t\3\2\2\u0168")
        buf.write("\u016a\t\4\2\2\u0169\u0168\3\2\2\2\u016a\u016d\3\2\2\2")
        buf.write("\u016b\u0169\3\2\2\2\u016b\u016c\3\2\2\2\u016c<\3\2\2")
        buf.write("\2\u016d\u016b\3\2\2\2\u016e\u0170\7&\2\2\u016f\u0171")
        buf.write("\t\4\2\2\u0170\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172")
        buf.write("\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173>\3\2\2\2\u0174")
        buf.write("\u0175\5\u00d1i\2\u0175@\3\2\2\2\u0176\u0177\5\u00d3j")
        buf.write("\2\u0177B\3\2\2\2\u0178\u0179\5\u00d5k\2\u0179D\3\2\2")
        buf.write("\2\u017a\u017b\5\u00d7l\2\u017bF\3\2\2\2\u017c\u017d\5")
        buf.write("\u00d9m\2\u017dH\3\2\2\2\u017e\u017f\5\u00dbn\2\u017f")
        buf.write("J\3\2\2\2\u0180\u0181\5\u00ddo\2\u0181L\3\2\2\2\u0182")
        buf.write("\u0183\5\u00dfp\2\u0183N\3\2\2\2\u0184\u0185\5\u00e1q")
        buf.write("\2\u0185P\3\2\2\2\u0186\u0187\5\u00e3r\2\u0187R\3\2\2")
        buf.write("\2\u0188\u0189\5\u00e7t\2\u0189T\3\2\2\2\u018a\u018b\5")
        buf.write("\u00e9u\2\u018bV\3\2\2\2\u018c\u018d\5\u00ebv\2\u018d")
        buf.write("X\3\2\2\2\u018e\u018f\5\u00edw\2\u018fZ\3\2\2\2\u0190")
        buf.write("\u0191\5\u00efx\2\u0191\\\3\2\2\2\u0192\u0193\5\u00f1")
        buf.write("y\2\u0193^\3\2\2\2\u0194\u0195\5\u0105\u0083\2\u0195`")
        buf.write("\3\2\2\2\u0196\u0197\5\u00f5{\2\u0197b\3\2\2\2\u0198\u0199")
        buf.write("\5\u0109\u0085\2\u0199d\3\2\2\2\u019a\u019d\5\u009bN\2")
        buf.write("\u019b\u019d\5\u009dO\2\u019c\u019a\3\2\2\2\u019c\u019b")
        buf.write("\3\2\2\2\u019df\3\2\2\2\u019e\u01a3\7$\2\2\u019f\u01a0")
        buf.write("\7)\2\2\u01a0\u01a2\7$\2\2\u01a1\u019f\3\2\2\2\u01a2\u01a5")
        buf.write("\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4")
        buf.write("\u01ac\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a6\u01ab\5i\65\2")
        buf.write("\u01a7\u01ab\n\5\2\2\u01a8\u01a9\7)\2\2\u01a9\u01ab\7")
        buf.write("$\2\2\u01aa\u01a6\3\2\2\2\u01aa\u01a7\3\2\2\2\u01aa\u01a8")
        buf.write("\3\2\2\2\u01ab\u01ae\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac")
        buf.write("\u01ad\3\2\2\2\u01ad\u01b3\3\2\2\2\u01ae\u01ac\3\2\2\2")
        buf.write("\u01af\u01b0\7)\2\2\u01b0\u01b2\7$\2\2\u01b1\u01af\3\2")
        buf.write("\2\2\u01b2\u01b5\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4")
        buf.write("\3\2\2\2\u01b4\u01b6\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b6")
        buf.write("\u01b7\7$\2\2\u01b7\u01b8\b\64\3\2\u01b8h\3\2\2\2\u01b9")
        buf.write("\u01ba\7^\2\2\u01ba\u01bb\t\6\2\2\u01bbj\3\2\2\2\u01bc")
        buf.write("\u01bd\7^\2\2\u01bd\u01c2\n\6\2\2\u01be\u01c2\5o8\2\u01bf")
        buf.write("\u01c2\5m\67\2\u01c0\u01c2\5s:\2\u01c1\u01bc\3\2\2\2\u01c1")
        buf.write("\u01be\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c1\u01c0\3\2\2\2")
        buf.write("\u01c2l\3\2\2\2\u01c3\u01c4\7^\2\2\u01c4\u01c5\4\62\65")
        buf.write("\2\u01c5\u01c6\4\629\2\u01c6\u01cd\4\629\2\u01c7\u01c8")
        buf.write("\7^\2\2\u01c8\u01c9\4\629\2\u01c9\u01cd\4\629\2\u01ca")
        buf.write("\u01cb\7^\2\2\u01cb\u01cd\4\629\2\u01cc\u01c3\3\2\2\2")
        buf.write("\u01cc\u01c7\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cdn\3\2\2")
        buf.write("\2\u01ce\u01cf\7^\2\2\u01cf\u01d0\7w\2\2\u01d0\u01d1\5")
        buf.write("q9\2\u01d1\u01d2\5q9\2\u01d2\u01d3\5q9\2\u01d3\u01d4\5")
        buf.write("q9\2\u01d4p\3\2\2\2\u01d5\u01d6\t\7\2\2\u01d6r\3\2\2\2")
        buf.write("\u01d7\u01d8\7^\2\2\u01d8\u01d9\7j\2\2\u01d9t\3\2\2\2")
        buf.write("\u01da\u01db\7%\2\2\u01db\u01dc\7%\2\2\u01dc\u01e0\3\2")
        buf.write("\2\2\u01dd\u01df\13\2\2\2\u01de\u01dd\3\2\2\2\u01df\u01e2")
        buf.write("\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e0\u01de\3\2\2\2\u01e1")
        buf.write("\u01e3\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e3\u01e4\7%\2\2")
        buf.write("\u01e4\u01e5\7%\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e7\b")
        buf.write(";\2\2\u01e7v\3\2\2\2\u01e8\u01ed\5\u0081A\2\u01e9\u01ed")
        buf.write("\5\u0083B\2\u01ea\u01ed\5\u0085C\2\u01eb\u01ed\5\u0087")
        buf.write("D\2\u01ec\u01e8\3\2\2\2\u01ec\u01e9\3\2\2\2\u01ec\u01ea")
        buf.write("\3\2\2\2\u01ec\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee")
        buf.write("\u01ef\b<\4\2\u01efx\3\2\2\2\u01f0\u01f6\5{>\2\u01f1\u01f7")
        buf.write("\5\177@\2\u01f2\u01f7\5}?\2\u01f3\u01f4\5\177@\2\u01f4")
        buf.write("\u01f5\5}?\2\u01f5\u01f7\3\2\2\2\u01f6\u01f1\3\2\2\2\u01f6")
        buf.write("\u01f2\3\2\2\2\u01f6\u01f3\3\2\2\2\u01f7\u01f8\3\2\2\2")
        buf.write("\u01f8\u01f9\b=\5\2\u01f9z\3\2\2\2\u01fa\u01fb\5\u0081")
        buf.write("A\2\u01fb|\3\2\2\2\u01fc\u01fe\t\b\2\2\u01fd\u01ff\t\t")
        buf.write("\2\2\u01fe\u01fd\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff\u0201")
        buf.write("\3\2\2\2\u0200\u0202\t\n\2\2\u0201\u0200\3\2\2\2\u0202")
        buf.write("\u0203\3\2\2\2\u0203\u0201\3\2\2\2\u0203\u0204\3\2\2\2")
        buf.write("\u0204~\3\2\2\2\u0205\u0209\5\u0105\u0083\2\u0206\u0208")
        buf.write("\t\n\2\2\u0207\u0206\3\2\2\2\u0208\u020b\3\2\2\2\u0209")
        buf.write("\u0207\3\2\2\2\u0209\u020a\3\2\2\2\u020a\u0080\3\2\2\2")
        buf.write("\u020b\u0209\3\2\2\2\u020c\u0222\7\62\2\2\u020d\u021e")
        buf.write("\t\13\2\2\u020e\u0210\t\n\2\2\u020f\u020e\3\2\2\2\u0210")
        buf.write("\u0213\3\2\2\2\u0211\u020f\3\2\2\2\u0211\u0212\3\2\2\2")
        buf.write("\u0212\u0215\3\2\2\2\u0213\u0211\3\2\2\2\u0214\u0216\7")
        buf.write("a\2\2\u0215\u0214\3\2\2\2\u0215\u0216\3\2\2\2\u0216\u0218")
        buf.write("\3\2\2\2\u0217\u0219\t\n\2\2\u0218\u0217\3\2\2\2\u0219")
        buf.write("\u021a\3\2\2\2\u021a\u0218\3\2\2\2\u021a\u021b\3\2\2\2")
        buf.write("\u021b\u021d\3\2\2\2\u021c\u0211\3\2\2\2\u021d\u0220\3")
        buf.write("\2\2\2\u021e\u021c\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u0222")
        buf.write("\3\2\2\2\u0220\u021e\3\2\2\2\u0221\u020c\3\2\2\2\u0221")
        buf.write("\u020d\3\2\2\2\u0222\u0082\3\2\2\2\u0223\u0224\7\62\2")
        buf.write("\2\u0224\u0228\t\f\2\2\u0225\u0227\t\r\2\2\u0226\u0225")
        buf.write("\3\2\2\2\u0227\u022a\3\2\2\2\u0228\u0226\3\2\2\2\u0228")
        buf.write("\u0229\3\2\2\2\u0229\u0084\3\2\2\2\u022a\u0228\3\2\2\2")
        buf.write("\u022b\u022c\7\62\2\2\u022c\u022d\t\16\2\2\u022d\u0231")
        buf.write("\t\17\2\2\u022e\u0230\t\20\2\2\u022f\u022e\3\2\2\2\u0230")
        buf.write("\u0233\3\2\2\2\u0231\u022f\3\2\2\2\u0231\u0232\3\2\2\2")
        buf.write("\u0232\u0086\3\2\2\2\u0233\u0231\3\2\2\2\u0234\u0235\7")
        buf.write("\62\2\2\u0235\u0236\t\21\2\2\u0236\u023a\t\22\2\2\u0237")
        buf.write("\u0239\t\23\2\2\u0238\u0237\3\2\2\2\u0239\u023c\3\2\2")
        buf.write("\2\u023a\u0238\3\2\2\2\u023a\u023b\3\2\2\2\u023b\u0088")
        buf.write("\3\2\2\2\u023c\u023a\3\2\2\2\u023d\u023e\7R\2\2\u023e")
        buf.write("\u023f\7t\2\2\u023f\u0240\7q\2\2\u0240\u0241\7i\2\2\u0241")
        buf.write("\u0242\7t\2\2\u0242\u0243\7c\2\2\u0243\u0244\7o\2\2\u0244")
        buf.write("\u008a\3\2\2\2\u0245\u0246\7o\2\2\u0246\u0247\7c\2\2\u0247")
        buf.write("\u0248\7k\2\2\u0248\u0249\7p\2\2\u0249\u008c\3\2\2\2\u024a")
        buf.write("\u024b\7g\2\2\u024b\u024c\7z\2\2\u024c\u024d\7v\2\2\u024d")
        buf.write("\u024e\7g\2\2\u024e\u024f\7p\2\2\u024f\u0250\7f\2\2\u0250")
        buf.write("\u0251\7u\2\2\u0251\u008e\3\2\2\2\u0252\u0253\7d\2\2\u0253")
        buf.write("\u0254\7t\2\2\u0254\u0255\7g\2\2\u0255\u0256\7c\2\2\u0256")
        buf.write("\u0257\7m\2\2\u0257\u0090\3\2\2\2\u0258\u0259\7e\2\2\u0259")
        buf.write("\u025a\7q\2\2\u025a\u025b\7p\2\2\u025b\u025c\7v\2\2\u025c")
        buf.write("\u025d\7k\2\2\u025d\u025e\7p\2\2\u025e\u025f\7w\2\2\u025f")
        buf.write("\u0260\7g\2\2\u0260\u0092\3\2\2\2\u0261\u0262\7k\2\2\u0262")
        buf.write("\u0263\7h\2\2\u0263\u0094\3\2\2\2\u0264\u0265\7g\2\2\u0265")
        buf.write("\u0266\7n\2\2\u0266\u0267\7u\2\2\u0267\u0268\7g\2\2\u0268")
        buf.write("\u0269\7k\2\2\u0269\u026a\7h\2\2\u026a\u0096\3\2\2\2\u026b")
        buf.write("\u026c\7g\2\2\u026c\u026d\7n\2\2\u026d\u026e\7u\2\2\u026e")
        buf.write("\u026f\7g\2\2\u026f\u0098\3\2\2\2\u0270\u0271\7h\2\2\u0271")
        buf.write("\u0272\7q\2\2\u0272\u0273\7t\2\2\u0273\u009a\3\2\2\2\u0274")
        buf.write("\u0275\7v\2\2\u0275\u0276\7t\2\2\u0276\u0277\7w\2\2\u0277")
        buf.write("\u0278\7g\2\2\u0278\u009c\3\2\2\2\u0279\u027a\7h\2\2\u027a")
        buf.write("\u027b\7c\2\2\u027b\u027c\7n\2\2\u027c\u027d\7u\2\2\u027d")
        buf.write("\u027e\7g\2\2\u027e\u009e\3\2\2\2\u027f\u0280\7c\2\2\u0280")
        buf.write("\u0281\7t\2\2\u0281\u0282\7t\2\2\u0282\u0283\7c\2\2\u0283")
        buf.write("\u0284\7{\2\2\u0284\u00a0\3\2\2\2\u0285\u0286\7k\2\2\u0286")
        buf.write("\u0287\7p\2\2\u0287\u00a2\3\2\2\2\u0288\u0289\7k\2\2\u0289")
        buf.write("\u028a\7p\2\2\u028a\u028b\7v\2\2\u028b\u00a4\3\2\2\2\u028c")
        buf.write("\u028d\7h\2\2\u028d\u028e\7n\2\2\u028e\u028f\7q\2\2\u028f")
        buf.write("\u0290\7c\2\2\u0290\u0291\7v\2\2\u0291\u00a6\3\2\2\2\u0292")
        buf.write("\u0293\7d\2\2\u0293\u0294\7q\2\2\u0294\u0295\7q\2\2\u0295")
        buf.write("\u0296\7n\2\2\u0296\u0297\7g\2\2\u0297\u0298\7c\2\2\u0298")
        buf.write("\u0299\7p\2\2\u0299\u00a8\3\2\2\2\u029a\u029b\7t\2\2\u029b")
        buf.write("\u029c\7g\2\2\u029c\u029d\7v\2\2\u029d\u029e\7w\2\2\u029e")
        buf.write("\u029f\7t\2\2\u029f\u02a0\7p\2\2\u02a0\u00aa\3\2\2\2\u02a1")
        buf.write("\u02a2\7e\2\2\u02a2\u02a3\7n\2\2\u02a3\u02a4\7c\2\2\u02a4")
        buf.write("\u02a5\7u\2\2\u02a5\u02a6\7u\2\2\u02a6\u00ac\3\2\2\2\u02a7")
        buf.write("\u02a8\7P\2\2\u02a8\u02a9\7w\2\2\u02a9\u02aa\7n\2\2\u02aa")
        buf.write("\u02ab\7n\2\2\u02ab\u00ae\3\2\2\2\u02ac\u02ad\7x\2\2\u02ad")
        buf.write("\u02ae\7c\2\2\u02ae\u02af\7n\2\2\u02af\u00b0\3\2\2\2\u02b0")
        buf.write("\u02b1\7x\2\2\u02b1\u02b2\7c\2\2\u02b2\u02b3\7t\2\2\u02b3")
        buf.write("\u00b2\3\2\2\2\u02b4\u02b5\7u\2\2\u02b5\u02b6\7g\2\2\u02b6")
        buf.write("\u02b7\7n\2\2\u02b7\u02b8\7h\2\2\u02b8\u00b4\3\2\2\2\u02b9")
        buf.write("\u02ba\7e\2\2\u02ba\u02bb\7q\2\2\u02bb\u02bc\7p\2\2\u02bc")
        buf.write("\u02bd\7u\2\2\u02bd\u02be\7v\2\2\u02be\u02bf\7t\2\2\u02bf")
        buf.write("\u02c0\7w\2\2\u02c0\u02c1\7e\2\2\u02c1\u02c2\7v\2\2\u02c2")
        buf.write("\u02c3\7q\2\2\u02c3\u02c4\7t\2\2\u02c4\u00b6\3\2\2\2\u02c5")
        buf.write("\u02c6\7f\2\2\u02c6\u02c7\7g\2\2\u02c7\u02c8\7u\2\2\u02c8")
        buf.write("\u02c9\7v\2\2\u02c9\u02ca\7t\2\2\u02ca\u02cb\7w\2\2\u02cb")
        buf.write("\u02cc\7e\2\2\u02cc\u02cd\7v\2\2\u02cd\u02ce\7q\2\2\u02ce")
        buf.write("\u02cf\7t\2\2\u02cf\u00b8\3\2\2\2\u02d0\u02d1\7p\2\2\u02d1")
        buf.write("\u02d2\7g\2\2\u02d2\u02d3\7y\2\2\u02d3\u00ba\3\2\2\2\u02d4")
        buf.write("\u02d5\7D\2\2\u02d5\u02d6\7{\2\2\u02d6\u00bc\3\2\2\2\u02d7")
        buf.write("\u02d8\7f\2\2\u02d8\u02d9\7q\2\2\u02d9\u00be\3\2\2\2\u02da")
        buf.write("\u02db\7u\2\2\u02db\u02dc\7v\2\2\u02dc\u02dd\7t\2\2\u02dd")
        buf.write("\u02de\7k\2\2\u02de\u02df\7p\2\2\u02df\u02e0\7i\2\2\u02e0")
        buf.write("\u00c0\3\2\2\2\u02e1\u02e2\7v\2\2\u02e2\u02e3\7j\2\2\u02e3")
        buf.write("\u02e4\7g\2\2\u02e4\u02e5\7p\2\2\u02e5\u00c2\3\2\2\2\u02e6")
        buf.write("\u02e7\7x\2\2\u02e7\u02e8\7q\2\2\u02e8\u02e9\7k\2\2\u02e9")
        buf.write("\u02ea\7f\2\2\u02ea\u00c4\3\2\2\2\u02eb\u02ec\7p\2\2\u02ec")
        buf.write("\u02ed\7k\2\2\u02ed\u02ee\7n\2\2\u02ee\u00c6\3\2\2\2\u02ef")
        buf.write("\u02f0\7v\2\2\u02f0\u02f1\7j\2\2\u02f1\u02f2\7k\2\2\u02f2")
        buf.write("\u02f3\7u\2\2\u02f3\u00c8\3\2\2\2\u02f4\u02f5\7h\2\2\u02f5")
        buf.write("\u02f6\7k\2\2\u02f6\u02f7\7p\2\2\u02f7\u02f8\7c\2\2\u02f8")
        buf.write("\u02f9\7n\2\2\u02f9\u00ca\3\2\2\2\u02fa\u02fb\7u\2\2\u02fb")
        buf.write("\u02fc\7v\2\2\u02fc\u02fd\7c\2\2\u02fd\u02fe\7v\2\2\u02fe")
        buf.write("\u02ff\7k\2\2\u02ff\u0300\7e\2\2\u0300\u00cc\3\2\2\2\u0301")
        buf.write("\u0302\7v\2\2\u0302\u0303\7q\2\2\u0303\u00ce\3\2\2\2\u0304")
        buf.write("\u0305\7f\2\2\u0305\u0306\7q\2\2\u0306\u0307\7y\2\2\u0307")
        buf.write("\u0308\7p\2\2\u0308\u0309\7v\2\2\u0309\u030a\7q\2\2\u030a")
        buf.write("\u00d0\3\2\2\2\u030b\u030c\7-\2\2\u030c\u00d2\3\2\2\2")
        buf.write("\u030d\u030e\7/\2\2\u030e\u00d4\3\2\2\2\u030f\u0310\7")
        buf.write(",\2\2\u0310\u00d6\3\2\2\2\u0311\u0312\7\61\2\2\u0312\u00d8")
        buf.write("\3\2\2\2\u0313\u0314\7\'\2\2\u0314\u00da\3\2\2\2\u0315")
        buf.write("\u0316\7#\2\2\u0316\u00dc\3\2\2\2\u0317\u0318\7(\2\2\u0318")
        buf.write("\u0319\7(\2\2\u0319\u00de\3\2\2\2\u031a\u031b\7~\2\2\u031b")
        buf.write("\u031c\7~\2\2\u031c\u00e0\3\2\2\2\u031d\u031e\7?\2\2\u031e")
        buf.write("\u031f\7?\2\2\u031f\u00e2\3\2\2\2\u0320\u0321\7#\2\2\u0321")
        buf.write("\u0322\7?\2\2\u0322\u00e4\3\2\2\2\u0323\u0324\7?\2\2\u0324")
        buf.write("\u00e6\3\2\2\2\u0325\u0326\7@\2\2\u0326\u00e8\3\2\2\2")
        buf.write("\u0327\u0328\7>\2\2\u0328\u00ea\3\2\2\2\u0329\u032a\7")
        buf.write("@\2\2\u032a\u032b\7?\2\2\u032b\u00ec\3\2\2\2\u032c\u032d")
        buf.write("\7>\2\2\u032d\u032e\7?\2\2\u032e\u00ee\3\2\2\2\u032f\u0330")
        buf.write("\7?\2\2\u0330\u0331\7?\2\2\u0331\u0332\7\60\2\2\u0332")
        buf.write("\u00f0\3\2\2\2\u0333\u0334\7-\2\2\u0334\u0335\7\60\2\2")
        buf.write("\u0335\u00f2\3\2\2\2\u0336\u0337\7`\2\2\u0337\u00f4\3")
        buf.write("\2\2\2\u0338\u0339\7<\2\2\u0339\u033a\7<\2\2\u033a\u00f6")
        buf.write("\3\2\2\2\u033b\u033c\7*\2\2\u033c\u00f8\3\2\2\2\u033d")
        buf.write("\u033e\7+\2\2\u033e\u00fa\3\2\2\2\u033f\u0340\7]\2\2\u0340")
        buf.write("\u00fc\3\2\2\2\u0341\u0342\7_\2\2\u0342\u00fe\3\2\2\2")
        buf.write("\u0343\u0344\7}\2\2\u0344\u0100\3\2\2\2\u0345\u0346\7")
        buf.write("\177\2\2\u0346\u0102\3\2\2\2\u0347\u0348\7=\2\2\u0348")
        buf.write("\u0104\3\2\2\2\u0349\u034a\7\60\2\2\u034a\u0106\3\2\2")
        buf.write("\2\u034b\u034c\7.\2\2\u034c\u0108\3\2\2\2\u034d\u034e")
        buf.write("\7<\2\2\u034e\u010a\3\2\2\2\u034f\u0351\t\24\2\2\u0350")
        buf.write("\u034f\3\2\2\2\u0351\u0352\3\2\2\2\u0352\u0350\3\2\2\2")
        buf.write("\u0352\u0353\3\2\2\2\u0353\u0354\3\2\2\2\u0354\u0355\b")
        buf.write("\u0086\2\2\u0355\u010c\3\2\2\2\u0356\u0357\7%\2\2\u0357")
        buf.write("\u0358\7%\2\2\u0358\u035c\3\2\2\2\u0359\u035b\13\2\2\2")
        buf.write("\u035a\u0359\3\2\2\2\u035b\u035e\3\2\2\2\u035c\u035d\3")
        buf.write("\2\2\2\u035c\u035a\3\2\2\2\u035d\u035f\3\2\2\2\u035e\u035c")
        buf.write("\3\2\2\2\u035f\u0360\7\2\2\3\u0360\u0361\b\u0087\6\2\u0361")
        buf.write("\u010e\3\2\2\2\u0362\u0363\13\2\2\2\u0363\u0364\b\u0088")
        buf.write("\7\2\u0364\u0110\3\2\2\2 \2\u0135\u0140\u014c\u0165\u016b")
        buf.write("\u0172\u019c\u01a3\u01aa\u01ac\u01b3\u01c1\u01cc\u01e0")
        buf.write("\u01ec\u01f6\u01fe\u0203\u0209\u0211\u0215\u021a\u021e")
        buf.write("\u0221\u0228\u0231\u023a\u0352\u035c\b\b\2\2\3\64\2\3")
        buf.write("<\3\3=\4\3\u0087\5\3\u0088\6")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Class_word = 1
    Prog_word = 2
    Extends_word = 3
    Void_word = 4
    Var_word = 5
    Val_word = 6
    If_word = 7
    Then_word = 8
    Else_word = 9
    Elseif_word = 10
    For_word = 11
    Assign_op = 12
    To_word = 13
    Do_word = 14
    Break_word = 15
    Comment_normal = 16
    Comment_block = 17
    Comment_sharp = 18
    Bool_word = 19
    Int_word = 20
    Float_word = 21
    Str_word = 22
    Array_word = 23
    Main_word = 24
    Cons_word = 25
    Dest_word = 26
    Self_word = 27
    ID = 28
    Add = 29
    Sub = 30
    Mul = 31
    Div = 32
    Mod = 33
    Not = 34
    And = 35
    Or = 36
    Equal = 37
    Diff = 38
    Greater = 39
    Lesser = 40
    Greater_euqal = 41
    Lesser_equal = 42
    String_comp = 43
    String_concat = 44
    Member_access_in = 45
    Member_access_out = 46
    Colon = 47
    BOOLEANLIT = 48
    STRINGLIT = 49
    BLOCKCOMMENT = 50
    INTLIT = 51
    FLOATLIT = 52
    PROGRAM = 53
    MAIN = 54
    EXTENDS = 55
    BREAK = 56
    CONT = 57
    IF = 58
    ELSEIF = 59
    ELSE = 60
    FOR = 61
    BOOLTRUE = 62
    BOOLFALSE = 63
    ARRAY = 64
    IN = 65
    INT = 66
    FLOAT = 67
    BOOL = 68
    RETURN = 69
    CLASS = 70
    NULL = 71
    VAL = 72
    VAR = 73
    SELF = 74
    CONS = 75
    DEST = 76
    KEYWORD_NEW = 77
    BY = 78
    DO = 79
    STRING = 80
    THEN = 81
    VOID = 82
    NIL = 83
    THIS = 84
    FINAL = 85
    STATIC = 86
    TO = 87
    DOWNTO = 88
    ADD_OP = 89
    SUB_OP = 90
    MUL_OP = 91
    FLOAT_DIVISION_OP = 92
    MOD_OP = 93
    NOT_OP = 94
    AND_OP = 95
    OR_OP = 96
    EQUAL_OP = 97
    NOT_EQUAL_OP = 98
    ASSIGN_OP = 99
    GREATER_OP = 100
    LESS_OP = 101
    GREATER_EQUAL_OP = 102
    LESS_EQUAL_OP = 103
    STRING_COMP_OP = 104
    STRING_CONCAT_OP = 105
    CONCATENATION_OP = 106
    MEMBER_ACCESS_OUT = 107
    LP = 108
    RP = 109
    LSB = 110
    RSB = 111
    LB = 112
    RB = 113
    SEMI = 114
    DOT = 115
    COMA = 116
    COLON = 117
    WS = 118
    UNTERMINATED_COMMENT = 119
    ERROR_CHAR = 120

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Program'", "'main'", "'extends'", "'break'", "'continue'", 
            "'if'", "'elseif'", "'else'", "'for'", "'true'", "'false'", 
            "'array'", "'in'", "'int'", "'float'", "'boolean'", "'return'", 
            "'class'", "'Null'", "'val'", "'var'", "'self'", "'constructor'", 
            "'destructor'", "'new'", "'By'", "'do'", "'string'", "'then'", 
            "'void'", "'nil'", "'this'", "'final'", "'static'", "'to'", 
            "'downto'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'='", "'>'", "'<'", "'>='", "'<='", 
            "'==.'", "'+.'", "'^'", "'::'", "'('", "')'", "'['", "']'", 
            "'{'", "'}'", "';'", "'.'", "','", "':'" ]

    symbolicNames = [ "<INVALID>",
            "Class_word", "Prog_word", "Extends_word", "Void_word", "Var_word", 
            "Val_word", "If_word", "Then_word", "Else_word", "Elseif_word", 
            "For_word", "Assign_op", "To_word", "Do_word", "Break_word", 
            "Comment_normal", "Comment_block", "Comment_sharp", "Bool_word", 
            "Int_word", "Float_word", "Str_word", "Array_word", "Main_word", 
            "Cons_word", "Dest_word", "Self_word", "ID", "Add", "Sub", "Mul", 
            "Div", "Mod", "Not", "And", "Or", "Equal", "Diff", "Greater", 
            "Lesser", "Greater_euqal", "Lesser_equal", "String_comp", "String_concat", 
            "Member_access_in", "Member_access_out", "Colon", "BOOLEANLIT", 
            "STRINGLIT", "BLOCKCOMMENT", "INTLIT", "FLOATLIT", "PROGRAM", 
            "MAIN", "EXTENDS", "BREAK", "CONT", "IF", "ELSEIF", "ELSE", 
            "FOR", "BOOLTRUE", "BOOLFALSE", "ARRAY", "IN", "INT", "FLOAT", 
            "BOOL", "RETURN", "CLASS", "NULL", "VAL", "VAR", "SELF", "CONS", 
            "DEST", "KEYWORD_NEW", "BY", "DO", "STRING", "THEN", "VOID", 
            "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", "ADD_OP", 
            "SUB_OP", "MUL_OP", "FLOAT_DIVISION_OP", "MOD_OP", "NOT_OP", 
            "AND_OP", "OR_OP", "EQUAL_OP", "NOT_EQUAL_OP", "ASSIGN_OP", 
            "GREATER_OP", "LESS_OP", "GREATER_EQUAL_OP", "LESS_EQUAL_OP", 
            "STRING_COMP_OP", "STRING_CONCAT_OP", "CONCATENATION_OP", "MEMBER_ACCESS_OUT", 
            "LP", "RP", "LSB", "RSB", "LB", "RB", "SEMI", "DOT", "COMA", 
            "COLON", "WS", "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    ruleNames = [ "Class_word", "Prog_word", "Extends_word", "Void_word", 
                  "Var_word", "Val_word", "If_word", "Then_word", "Else_word", 
                  "Elseif_word", "For_word", "Assign_op", "To_word", "Do_word", 
                  "Break_word", "Comment_normal", "Comment_block", "Comment_sharp", 
                  "Bool_word", "Int_word", "Float_word", "Str_word", "Array_word", 
                  "Main_word", "Cons_word", "Dest_word", "Self_word", "ID", 
                  "NORM_ID", "SPEC_ID", "Add", "Sub", "Mul", "Div", "Mod", 
                  "Not", "And", "Or", "Equal", "Diff", "Greater", "Lesser", 
                  "Greater_euqal", "Lesser_equal", "String_comp", "String_concat", 
                  "Member_access_in", "Member_access_out", "Colon", "BOOLEANLIT", 
                  "STRINGLIT", "ESC_SEQ", "ILL_ESC_SEQ", "OCTAL_ESC", "UNICODE_ESC", 
                  "HEX_DIGIT", "UNKNOW_ESC", "BLOCKCOMMENT", "INTLIT", "FLOATLIT", 
                  "INTERGER_PART", "EXPONENT", "FRACTION", "DECIMAL", "OCTAL", 
                  "HEX", "BIN", "PROGRAM", "MAIN", "EXTENDS", "BREAK", "CONT", 
                  "IF", "ELSEIF", "ELSE", "FOR", "BOOLTRUE", "BOOLFALSE", 
                  "ARRAY", "IN", "INT", "FLOAT", "BOOL", "RETURN", "CLASS", 
                  "NULL", "VAL", "VAR", "SELF", "CONS", "DEST", "KEYWORD_NEW", 
                  "BY", "DO", "STRING", "THEN", "VOID", "NIL", "THIS", "FINAL", 
                  "STATIC", "TO", "DOWNTO", "ADD_OP", "SUB_OP", "MUL_OP", 
                  "FLOAT_DIVISION_OP", "MOD_OP", "NOT_OP", "AND_OP", "OR_OP", 
                  "EQUAL_OP", "NOT_EQUAL_OP", "ASSIGN_OP", "GREATER_OP", 
                  "LESS_OP", "GREATER_EQUAL_OP", "LESS_EQUAL_OP", "STRING_COMP_OP", 
                  "STRING_CONCAT_OP", "CONCATENATION_OP", "MEMBER_ACCESS_OUT", 
                  "LP", "RP", "LSB", "RSB", "LB", "RB", "SEMI", "DOT", "COMA", 
                  "COLON", "WS", "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[50] = self.STRINGLIT_action 
            actions[58] = self.INTLIT_action 
            actions[59] = self.FLOATLIT_action 
            actions[133] = self.UNTERMINATED_COMMENT_action 
            actions[134] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	s = ""
            	check = False;
            	for i in range(len(self.text)):
            		s += self.text[i]
            		a = ''
            		if(i == len(self.text)-1): a = ''
            		else: a = self.text[i+1]
            		b = ((a != 'b') and  (a != 'f') and  (a != 'r') and  (a != 'n') and  (a != 't') and (a != '\'') and  (a != '"') and (a != '\\'))
            		if(self.text[i] == '\\' and b == True):
            			s += self.text[i+1]
            			check = True
            			break;
            	if(check == True):
            		self.text = s
            		self.text = self.text[1:]
            		raise IllegalEscape(self.text)
            	else:
            		self.text = s
            		self.text = self.text[1:-1]

     

    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	self.text = self.text.replace('_','')

     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	self.text = self.text.replace('_','')
            	##print("Float: ", self.text)

     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             raise UnterminatedComment(self.text) 
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                from lexererr import ErrorToken
                raise ErrorToken(self.text)

     


