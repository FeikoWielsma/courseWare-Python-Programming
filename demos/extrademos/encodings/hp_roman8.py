"""Python Character Mapping Codec generated from 'hp_roman8.txt' with gencodec.py.

Based on data from ftp://dkuug.dk/i18n/charmaps/HP-ROMAN8 (Keld Simonsen)

Original source: LaserJet IIP Printer User's Manual HP part no
33471-90901, Hewlet-Packard, June 1989.

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
        name="hp-roman8",
        encode=Codec().encode,
        decode=Codec().decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamwriter=StreamWriter,
        streamreader=StreamReader,
    )


### Decoding Map

decoding_map = codecs.make_identity_dict(range(256))
decoding_map.update(
    {
        0x00A1: 0x00C0,  #       LATIN CAPITAL LETTER A WITH GRAVE
        0x00A2: 0x00C2,  #       LATIN CAPITAL LETTER A WITH CIRCUMFLEX
        0x00A3: 0x00C8,  #       LATIN CAPITAL LETTER E WITH GRAVE
        0x00A4: 0x00CA,  #       LATIN CAPITAL LETTER E WITH CIRCUMFLEX
        0x00A5: 0x00CB,  #       LATIN CAPITAL LETTER E WITH DIAERESIS
        0x00A6: 0x00CE,  #       LATIN CAPITAL LETTER I WITH CIRCUMFLEX
        0x00A7: 0x00CF,  #       LATIN CAPITAL LETTER I WITH DIAERESIS
        0x00A8: 0x00B4,  #       ACUTE ACCENT
        0x00A9: 0x02CB,  #       MODIFIER LETTER GRAVE ACCENT (Mandarin Chinese fourth tone)
        0x00AA: 0x02C6,  #       MODIFIER LETTER CIRCUMFLEX ACCENT
        0x00AB: 0x00A8,  #       DIAERESIS
        0x00AC: 0x02DC,  #       SMALL TILDE
        0x00AD: 0x00D9,  #       LATIN CAPITAL LETTER U WITH GRAVE
        0x00AE: 0x00DB,  #       LATIN CAPITAL LETTER U WITH CIRCUMFLEX
        0x00AF: 0x20A4,  #       LIRA SIGN
        0x00B0: 0x00AF,  #       MACRON
        0x00B1: 0x00DD,  #       LATIN CAPITAL LETTER Y WITH ACUTE
        0x00B2: 0x00FD,  #       LATIN SMALL LETTER Y WITH ACUTE
        0x00B3: 0x00B0,  #       DEGREE SIGN
        0x00B4: 0x00C7,  #       LATIN CAPITAL LETTER C WITH CEDILLA
        0x00B5: 0x00E7,  #       LATIN SMALL LETTER C WITH CEDILLA
        0x00B6: 0x00D1,  #       LATIN CAPITAL LETTER N WITH TILDE
        0x00B7: 0x00F1,  #       LATIN SMALL LETTER N WITH TILDE
        0x00B8: 0x00A1,  #       INVERTED EXCLAMATION MARK
        0x00B9: 0x00BF,  #       INVERTED QUESTION MARK
        0x00BA: 0x00A4,  #       CURRENCY SIGN
        0x00BB: 0x00A3,  #       POUND SIGN
        0x00BC: 0x00A5,  #       YEN SIGN
        0x00BD: 0x00A7,  #       SECTION SIGN
        0x00BE: 0x0192,  #       LATIN SMALL LETTER F WITH HOOK
        0x00BF: 0x00A2,  #       CENT SIGN
        0x00C0: 0x00E2,  #       LATIN SMALL LETTER A WITH CIRCUMFLEX
        0x00C1: 0x00EA,  #       LATIN SMALL LETTER E WITH CIRCUMFLEX
        0x00C2: 0x00F4,  #       LATIN SMALL LETTER O WITH CIRCUMFLEX
        0x00C3: 0x00FB,  #       LATIN SMALL LETTER U WITH CIRCUMFLEX
        0x00C4: 0x00E1,  #       LATIN SMALL LETTER A WITH ACUTE
        0x00C5: 0x00E9,  #       LATIN SMALL LETTER E WITH ACUTE
        0x00C6: 0x00F3,  #       LATIN SMALL LETTER O WITH ACUTE
        0x00C7: 0x00FA,  #       LATIN SMALL LETTER U WITH ACUTE
        0x00C8: 0x00E0,  #       LATIN SMALL LETTER A WITH GRAVE
        0x00C9: 0x00E8,  #       LATIN SMALL LETTER E WITH GRAVE
        0x00CA: 0x00F2,  #       LATIN SMALL LETTER O WITH GRAVE
        0x00CB: 0x00F9,  #       LATIN SMALL LETTER U WITH GRAVE
        0x00CC: 0x00E4,  #       LATIN SMALL LETTER A WITH DIAERESIS
        0x00CD: 0x00EB,  #       LATIN SMALL LETTER E WITH DIAERESIS
        0x00CE: 0x00F6,  #       LATIN SMALL LETTER O WITH DIAERESIS
        0x00CF: 0x00FC,  #       LATIN SMALL LETTER U WITH DIAERESIS
        0x00D0: 0x00C5,  #       LATIN CAPITAL LETTER A WITH RING ABOVE
        0x00D1: 0x00EE,  #       LATIN SMALL LETTER I WITH CIRCUMFLEX
        0x00D2: 0x00D8,  #       LATIN CAPITAL LETTER O WITH STROKE
        0x00D3: 0x00C6,  #       LATIN CAPITAL LETTER AE
        0x00D4: 0x00E5,  #       LATIN SMALL LETTER A WITH RING ABOVE
        0x00D5: 0x00ED,  #       LATIN SMALL LETTER I WITH ACUTE
        0x00D6: 0x00F8,  #       LATIN SMALL LETTER O WITH STROKE
        0x00D7: 0x00E6,  #       LATIN SMALL LETTER AE
        0x00D8: 0x00C4,  #       LATIN CAPITAL LETTER A WITH DIAERESIS
        0x00D9: 0x00EC,  #       LATIN SMALL LETTER I WITH GRAVE
        0x00DA: 0x00D6,  #       LATIN CAPITAL LETTER O WITH DIAERESIS
        0x00DB: 0x00DC,  #       LATIN CAPITAL LETTER U WITH DIAERESIS
        0x00DC: 0x00C9,  #       LATIN CAPITAL LETTER E WITH ACUTE
        0x00DD: 0x00EF,  #       LATIN SMALL LETTER I WITH DIAERESIS
        0x00DE: 0x00DF,  #       LATIN SMALL LETTER SHARP S (German)
        0x00DF: 0x00D4,  #       LATIN CAPITAL LETTER O WITH CIRCUMFLEX
        0x00E0: 0x00C1,  #       LATIN CAPITAL LETTER A WITH ACUTE
        0x00E1: 0x00C3,  #       LATIN CAPITAL LETTER A WITH TILDE
        0x00E2: 0x00E3,  #       LATIN SMALL LETTER A WITH TILDE
        0x00E3: 0x00D0,  #       LATIN CAPITAL LETTER ETH (Icelandic)
        0x00E4: 0x00F0,  #       LATIN SMALL LETTER ETH (Icelandic)
        0x00E5: 0x00CD,  #       LATIN CAPITAL LETTER I WITH ACUTE
        0x00E6: 0x00CC,  #       LATIN CAPITAL LETTER I WITH GRAVE
        0x00E7: 0x00D3,  #       LATIN CAPITAL LETTER O WITH ACUTE
        0x00E8: 0x00D2,  #       LATIN CAPITAL LETTER O WITH GRAVE
        0x00E9: 0x00D5,  #       LATIN CAPITAL LETTER O WITH TILDE
        0x00EA: 0x00F5,  #       LATIN SMALL LETTER O WITH TILDE
        0x00EB: 0x0160,  #       LATIN CAPITAL LETTER S WITH CARON
        0x00EC: 0x0161,  #       LATIN SMALL LETTER S WITH CARON
        0x00ED: 0x00DA,  #       LATIN CAPITAL LETTER U WITH ACUTE
        0x00EE: 0x0178,  #       LATIN CAPITAL LETTER Y WITH DIAERESIS
        0x00EF: 0x00FF,  #       LATIN SMALL LETTER Y WITH DIAERESIS
        0x00F0: 0x00DE,  #       LATIN CAPITAL LETTER THORN (Icelandic)
        0x00F1: 0x00FE,  #       LATIN SMALL LETTER THORN (Icelandic)
        0x00F2: 0x00B7,  #       MIDDLE DOT
        0x00F3: 0x00B5,  #       MICRO SIGN
        0x00F4: 0x00B6,  #       PILCROW SIGN
        0x00F5: 0x00BE,  #       VULGAR FRACTION THREE QUARTERS
        0x00F6: 0x2014,  #       EM DASH
        0x00F7: 0x00BC,  #       VULGAR FRACTION ONE QUARTER
        0x00F8: 0x00BD,  #       VULGAR FRACTION ONE HALF
        0x00F9: 0x00AA,  #       FEMININE ORDINAL INDICATOR
        0x00FA: 0x00BA,  #       MASCULINE ORDINAL INDICATOR
        0x00FB: 0x00AB,  #       LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
        0x00FC: 0x25A0,  #       BLACK SQUARE
        0x00FD: 0x00BB,  #       RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
        0x00FE: 0x00B1,  #       PLUS-MINUS SIGN
        0x00FF: None,
    }
)

### Encoding Map

encoding_map = codecs.make_encoding_map(decoding_map)
