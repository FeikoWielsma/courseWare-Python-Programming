"""Python Character Mapping Codec generated from 'PTCP154.txt' with gencodec.py.

Written by Marc-Andre Lemburg (mal@lemburg.com).

(c) Copyright CNRI, All Rights Reserved. NO WARRANTY.
(c) Copyright 2000 Guido van Rossum.

"""  # "

import codecs

### Codec APIs


class Codec(codecs.Codec):
    def encode(self, input, errors="strict"):
        return codecs.charmap_encode(input, errors, encoding_map)

    def decode(self, input, errors="strict"):
        return codecs.charmap_decode(input, errors, decoding_map)


class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input, self.errors, encoding_map)[0]


class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.charmap_decode(input, self.errors, decoding_map)[0]


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


### encodings module API


def getregentry():
    return codecs.CodecInfo(
        name="ptcp154",
        encode=Codec().encode,
        decode=Codec().decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    )


### Decoding Map

decoding_map = codecs.make_identity_dict(range(256))
decoding_map.update(
    {
        0x0080: 0x0496,  #        CYRILLIC CAPITAL LETTER ZHE WITH DESCENDER
        0x0081: 0x0492,  #        CYRILLIC CAPITAL LETTER GHE WITH STROKE
        0x0082: 0x04EE,  #        CYRILLIC CAPITAL LETTER U WITH MACRON
        0x0083: 0x0493,  #        CYRILLIC SMALL LETTER GHE WITH STROKE
        0x0084: 0x201E,  #        DOUBLE LOW-9 QUOTATION MARK
        0x0085: 0x2026,  #        HORIZONTAL ELLIPSIS
        0x0086: 0x04B6,  #        CYRILLIC CAPITAL LETTER CHE WITH DESCENDER
        0x0087: 0x04AE,  #        CYRILLIC CAPITAL LETTER STRAIGHT U
        0x0088: 0x04B2,  #        CYRILLIC CAPITAL LETTER HA WITH DESCENDER
        0x0089: 0x04AF,  #        CYRILLIC SMALL LETTER STRAIGHT U
        0x008A: 0x04A0,  #        CYRILLIC CAPITAL LETTER BASHKIR KA
        0x008B: 0x04E2,  #        CYRILLIC CAPITAL LETTER I WITH MACRON
        0x008C: 0x04A2,  #        CYRILLIC CAPITAL LETTER EN WITH DESCENDER
        0x008D: 0x049A,  #        CYRILLIC CAPITAL LETTER KA WITH DESCENDER
        0x008E: 0x04BA,  #        CYRILLIC CAPITAL LETTER SHHA
        0x008F: 0x04B8,  #        CYRILLIC CAPITAL LETTER CHE WITH VERTICAL STROKE
        0x0090: 0x0497,  #        CYRILLIC SMALL LETTER ZHE WITH DESCENDER
        0x0091: 0x2018,  #        LEFT SINGLE QUOTATION MARK
        0x0092: 0x2019,  #        RIGHT SINGLE QUOTATION MARK
        0x0093: 0x201C,  #        LEFT DOUBLE QUOTATION MARK
        0x0094: 0x201D,  #        RIGHT DOUBLE QUOTATION MARK
        0x0095: 0x2022,  #        BULLET
        0x0096: 0x2013,  #        EN DASH
        0x0097: 0x2014,  #        EM DASH
        0x0098: 0x04B3,  #        CYRILLIC SMALL LETTER HA WITH DESCENDER
        0x0099: 0x04B7,  #        CYRILLIC SMALL LETTER CHE WITH DESCENDER
        0x009A: 0x04A1,  #        CYRILLIC SMALL LETTER BASHKIR KA
        0x009B: 0x04E3,  #        CYRILLIC SMALL LETTER I WITH MACRON
        0x009C: 0x04A3,  #        CYRILLIC SMALL LETTER EN WITH DESCENDER
        0x009D: 0x049B,  #        CYRILLIC SMALL LETTER KA WITH DESCENDER
        0x009E: 0x04BB,  #        CYRILLIC SMALL LETTER SHHA
        0x009F: 0x04B9,  #        CYRILLIC SMALL LETTER CHE WITH VERTICAL STROKE
        0x00A1: 0x040E,  #        CYRILLIC CAPITAL LETTER SHORT U (Byelorussian)
        0x00A2: 0x045E,  #        CYRILLIC SMALL LETTER SHORT U (Byelorussian)
        0x00A3: 0x0408,  #        CYRILLIC CAPITAL LETTER JE
        0x00A4: 0x04E8,  #        CYRILLIC CAPITAL LETTER BARRED O
        0x00A5: 0x0498,  #        CYRILLIC CAPITAL LETTER ZE WITH DESCENDER
        0x00A6: 0x04B0,  #        CYRILLIC CAPITAL LETTER STRAIGHT U WITH STROKE
        0x00A8: 0x0401,  #        CYRILLIC CAPITAL LETTER IO
        0x00AA: 0x04D8,  #        CYRILLIC CAPITAL LETTER SCHWA
        0x00AD: 0x04EF,  #        CYRILLIC SMALL LETTER U WITH MACRON
        0x00AF: 0x049C,  #        CYRILLIC CAPITAL LETTER KA WITH VERTICAL STROKE
        0x00B1: 0x04B1,  #        CYRILLIC SMALL LETTER STRAIGHT U WITH STROKE
        0x00B2: 0x0406,  #        CYRILLIC CAPITAL LETTER BYELORUSSIAN-UKRAINIAN I
        0x00B3: 0x0456,  #        CYRILLIC SMALL LETTER BYELORUSSIAN-UKRAINIAN I
        0x00B4: 0x0499,  #        CYRILLIC SMALL LETTER ZE WITH DESCENDER
        0x00B5: 0x04E9,  #        CYRILLIC SMALL LETTER BARRED O
        0x00B8: 0x0451,  #        CYRILLIC SMALL LETTER IO
        0x00B9: 0x2116,  #        NUMERO SIGN
        0x00BA: 0x04D9,  #        CYRILLIC SMALL LETTER SCHWA
        0x00BC: 0x0458,  #        CYRILLIC SMALL LETTER JE
        0x00BD: 0x04AA,  #        CYRILLIC CAPITAL LETTER ES WITH DESCENDER
        0x00BE: 0x04AB,  #        CYRILLIC SMALL LETTER ES WITH DESCENDER
        0x00BF: 0x049D,  #        CYRILLIC SMALL LETTER KA WITH VERTICAL STROKE
        0x00C0: 0x0410,  #        CYRILLIC CAPITAL LETTER A
        0x00C1: 0x0411,  #        CYRILLIC CAPITAL LETTER BE
        0x00C2: 0x0412,  #        CYRILLIC CAPITAL LETTER VE
        0x00C3: 0x0413,  #        CYRILLIC CAPITAL LETTER GHE
        0x00C4: 0x0414,  #        CYRILLIC CAPITAL LETTER DE
        0x00C5: 0x0415,  #        CYRILLIC CAPITAL LETTER IE
        0x00C6: 0x0416,  #        CYRILLIC CAPITAL LETTER ZHE
        0x00C7: 0x0417,  #        CYRILLIC CAPITAL LETTER ZE
        0x00C8: 0x0418,  #        CYRILLIC CAPITAL LETTER I
        0x00C9: 0x0419,  #        CYRILLIC CAPITAL LETTER SHORT I
        0x00CA: 0x041A,  #        CYRILLIC CAPITAL LETTER KA
        0x00CB: 0x041B,  #        CYRILLIC CAPITAL LETTER EL
        0x00CC: 0x041C,  #        CYRILLIC CAPITAL LETTER EM
        0x00CD: 0x041D,  #        CYRILLIC CAPITAL LETTER EN
        0x00CE: 0x041E,  #        CYRILLIC CAPITAL LETTER O
        0x00CF: 0x041F,  #        CYRILLIC CAPITAL LETTER PE
        0x00D0: 0x0420,  #        CYRILLIC CAPITAL LETTER ER
        0x00D1: 0x0421,  #        CYRILLIC CAPITAL LETTER ES
        0x00D2: 0x0422,  #        CYRILLIC CAPITAL LETTER TE
        0x00D3: 0x0423,  #        CYRILLIC CAPITAL LETTER U
        0x00D4: 0x0424,  #        CYRILLIC CAPITAL LETTER EF
        0x00D5: 0x0425,  #        CYRILLIC CAPITAL LETTER HA
        0x00D6: 0x0426,  #        CYRILLIC CAPITAL LETTER TSE
        0x00D7: 0x0427,  #        CYRILLIC CAPITAL LETTER CHE
        0x00D8: 0x0428,  #        CYRILLIC CAPITAL LETTER SHA
        0x00D9: 0x0429,  #        CYRILLIC CAPITAL LETTER SHCHA
        0x00DA: 0x042A,  #        CYRILLIC CAPITAL LETTER HARD SIGN
        0x00DB: 0x042B,  #        CYRILLIC CAPITAL LETTER YERU
        0x00DC: 0x042C,  #        CYRILLIC CAPITAL LETTER SOFT SIGN
        0x00DD: 0x042D,  #        CYRILLIC CAPITAL LETTER E
        0x00DE: 0x042E,  #        CYRILLIC CAPITAL LETTER YU
        0x00DF: 0x042F,  #        CYRILLIC CAPITAL LETTER YA
        0x00E0: 0x0430,  #        CYRILLIC SMALL LETTER A
        0x00E1: 0x0431,  #        CYRILLIC SMALL LETTER BE
        0x00E2: 0x0432,  #        CYRILLIC SMALL LETTER VE
        0x00E3: 0x0433,  #        CYRILLIC SMALL LETTER GHE
        0x00E4: 0x0434,  #        CYRILLIC SMALL LETTER DE
        0x00E5: 0x0435,  #        CYRILLIC SMALL LETTER IE
        0x00E6: 0x0436,  #        CYRILLIC SMALL LETTER ZHE
        0x00E7: 0x0437,  #        CYRILLIC SMALL LETTER ZE
        0x00E8: 0x0438,  #        CYRILLIC SMALL LETTER I
        0x00E9: 0x0439,  #        CYRILLIC SMALL LETTER SHORT I
        0x00EA: 0x043A,  #        CYRILLIC SMALL LETTER KA
        0x00EB: 0x043B,  #        CYRILLIC SMALL LETTER EL
        0x00EC: 0x043C,  #        CYRILLIC SMALL LETTER EM
        0x00ED: 0x043D,  #        CYRILLIC SMALL LETTER EN
        0x00EE: 0x043E,  #        CYRILLIC SMALL LETTER O
        0x00EF: 0x043F,  #        CYRILLIC SMALL LETTER PE
        0x00F0: 0x0440,  #        CYRILLIC SMALL LETTER ER
        0x00F1: 0x0441,  #        CYRILLIC SMALL LETTER ES
        0x00F2: 0x0442,  #        CYRILLIC SMALL LETTER TE
        0x00F3: 0x0443,  #        CYRILLIC SMALL LETTER U
        0x00F4: 0x0444,  #        CYRILLIC SMALL LETTER EF
        0x00F5: 0x0445,  #        CYRILLIC SMALL LETTER HA
        0x00F6: 0x0446,  #        CYRILLIC SMALL LETTER TSE
        0x00F7: 0x0447,  #        CYRILLIC SMALL LETTER CHE
        0x00F8: 0x0448,  #        CYRILLIC SMALL LETTER SHA
        0x00F9: 0x0449,  #        CYRILLIC SMALL LETTER SHCHA
        0x00FA: 0x044A,  #        CYRILLIC SMALL LETTER HARD SIGN
        0x00FB: 0x044B,  #        CYRILLIC SMALL LETTER YERU
        0x00FC: 0x044C,  #        CYRILLIC SMALL LETTER SOFT SIGN
        0x00FD: 0x044D,  #        CYRILLIC SMALL LETTER E
        0x00FE: 0x044E,  #        CYRILLIC SMALL LETTER YU
        0x00FF: 0x044F,  #        CYRILLIC SMALL LETTER YA
    }
)

### Encoding Map

encoding_map = codecs.make_encoding_map(decoding_map)
