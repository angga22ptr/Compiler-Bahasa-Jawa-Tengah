"""
====================================================
VISUAL AST
Compiler Bahasa Jawa Tengah
====================================================
"""


class VisualAST:


    def tampilkan(self, node, prefix="", terakhir=True):

        if node is None:
            return


        bahasa_jawa = {

            "PLUS": "TAMBAH",
            "MINUS": "KURANG",
            "MULTIPLY": "KALI",
            "DIVIDE": "BAGI",

            "NUMBER": "ANGKA",

            "IDENTIFIER": "JENENG",

            "CETAK": "CETAK",

            "ASSIGN": "NEMPEL"

        }


        nama = bahasa_jawa.get(node.tipe, node.tipe)


        print(
            prefix +
            ("└── " if terakhir else "├── ") +
            f"{nama} : {node.nilai}"
        )


        anak = []


        if node.kiri:
            anak.append(node.kiri)

        if node.kanan:
            anak.append(node.kanan)


        for i, child in enumerate(anak):

            self.tampilkan(
                child,
                prefix + ("    " if terakhir else "│   "),
                i == len(anak)-1
            )