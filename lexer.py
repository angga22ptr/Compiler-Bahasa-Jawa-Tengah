"""
====================================================
LEXER
Compiler Bahasa Jawa Tengah
====================================================

Lexer bertugas mengubah source code
menjadi kumpulan token.
"""

import re


# ==================================================
# Keyword Bahasa Jawa Tengah
# ==================================================

KEYWORDS = {

    "cetak": "CETAK",

    "nek": "NEK",

    "liyane": "LIYANE",

    "nalika": "NALIKA",

    "gawe": "GAWE",

    "balekno": "BALEKNO",

    "bener": "BENER",

    "salah": "SALAH"

}


# ==================================================
# Daftar Token
# ==================================================

TOKEN_SPECIFICATION = [

    ("NUMBER", r"\d+(\.\d+)?"),

    ("STRING", r'"[^"]*"'),

    ("PLUS", r"\+"),

    ("MINUS", r"-"),

    ("MULTIPLY", r"\*"),

    ("DIVIDE", r"/"),

    ("ASSIGN", r"="),

    ("LPAREN", r"\("),

    ("RPAREN", r"\)"),

    ("IDENTIFIER", r"[A-Za-z_][A-Za-z0-9_]*"),

    ("SKIP", r"[ \t\n]+"),

    ("MISMATCH", r".")
]


regex = "|".join(

    f"(?P<{nama}>{pola})"

    for nama, pola in TOKEN_SPECIFICATION

)


class Lexer:

    def __init__(self, kode):

        self.kode = kode

    def tokenize(self):

        tokens = []

        for cocok in re.finditer(regex, self.kode):

            jenis = cocok.lastgroup

            nilai = cocok.group()

            # Lewati spasi
            if jenis == "SKIP":
                continue

            # Cek keyword Jawa Tengah
            if jenis == "IDENTIFIER":

                if nilai in KEYWORDS:

                    jenis = KEYWORDS[nilai]

            # Konversi angka
            elif jenis == "NUMBER":

                if "." in nilai:

                    nilai = float(nilai)

                else:

                    nilai = int(nilai)

            # Token tidak dikenali
            elif jenis == "MISMATCH":

                raise SyntaxError(

                    f"Token '{nilai}' tidak dikenali."

                )

            tokens.append((jenis, nilai))

        tokens.append(("EOF", None))

        return tokens