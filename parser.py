"""
====================================================
PARSER
Compiler Bahasa Jawa Tengah
====================================================

Parser bertugas memeriksa apakah susunan token
sesuai dengan grammar, kemudian membentuk AST.
"""

from ast_node import Node


class Parser:

    def __init__(self, tokens):

        self.tokens = tokens
        self.posisi = 0
        self.current = self.tokens[self.posisi]

    # ==========================================
    # Pindah ke token berikutnya
    # ==========================================

    def next(self):

        self.posisi += 1

        if self.posisi < len(self.tokens):
            self.current = self.tokens[self.posisi]
        else:
            self.current = ("EOF", None)

    # ==========================================
    # Memastikan token sesuai
    # ==========================================

    def eat(self, token):

        if self.current[0] == token:
            self.next()

        else:
            raise SyntaxError(

                f"Seharusnya '{token}', tetapi mendapat '{self.current[0]}'"

            )

    # ==========================================
    # Program
    # ==========================================

    def parse(self):

        node = self.statement()

        if self.current[0] != "EOF":

            raise SyntaxError(

                "Masih ada token yang belum diproses."

            )

        return node

    # ==========================================
    # Statement
    # ==========================================

    def statement(self):

        # --------------------------------------
        # cetak(...)
        # --------------------------------------

        if self.current[0] == "CETAK":

            self.eat("CETAK")
            self.eat("LPAREN")

            isi = self.expression()

            self.eat("RPAREN")

            return Node(

                "CETAK",
                "cetak",
                kiri=isi

            )

        # --------------------------------------
        # assignment
        # angka = 10
        # --------------------------------------

        elif (

            self.current[0] == "IDENTIFIER"

            and

            self.tokens[self.posisi + 1][0] == "ASSIGN"

        ):

            nama = self.current[1]

            self.eat("IDENTIFIER")

            self.eat("ASSIGN")

            nilai = self.expression()

            return Node(

                "ASSIGN",

                nama,

                kiri=nilai

            )

        # --------------------------------------
        # ekspresi biasa
        # --------------------------------------

        return self.expression()

    # ==========================================
    # Expression
    # ==========================================

    def expression(self):

        node = self.term()

        while self.current[0] in ("PLUS", "MINUS"):

            if self.current[0] == "PLUS":

                self.eat("PLUS")

                node = Node(

                    "PLUS",

                    "+",

                    kiri=node,

                    kanan=self.term()

                )

            else:

                self.eat("MINUS")

                node = Node(

                    "MINUS",

                    "-",

                    kiri=node,

                    kanan=self.term()

                )

        return node

    # ==========================================
    # Term
    # ==========================================

    def term(self):

        node = self.factor()

        while self.current[0] in (

            "MULTIPLY",

            "DIVIDE"

        ):

            if self.current[0] == "MULTIPLY":

                self.eat("MULTIPLY")

                node = Node(

                    "MULTIPLY",

                    "*",

                    kiri=node,

                    kanan=self.factor()

                )

            else:

                self.eat("DIVIDE")

                node = Node(

                    "DIVIDE",

                    "/",

                    kiri=node,

                    kanan=self.factor()

                )

        return node

    # ==========================================
    # Factor
    # ==========================================

    def factor(self):

        token = self.current

        # ---------------------

        if token[0] == "NUMBER":

            self.eat("NUMBER")

            return Node(

                "NUMBER",

                token[1]

            )

        # ---------------------

        elif token[0] == "IDENTIFIER":

            self.eat("IDENTIFIER")

            return Node(

                "IDENTIFIER",

                token[1]

            )

        # ---------------------

        elif token[0] == "LPAREN":

            self.eat("LPAREN")

            node = self.expression()

            self.eat("RPAREN")

            return node

        raise SyntaxError(

            f"Token '{token[1]}' tidak valid."

        )