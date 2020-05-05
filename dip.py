# 依存性逆転の原則（Dependency Inversion Principle）の効能を感じるためのデモ

# 抽象は具象に依存してはならない。具象が抽象に依存しなければならない。
# 例） EBookReader(抽象クラス)は，EBook を介して 具象クラス（PDFBook, HTMLBook） にアクセスする。
# 抽象はインタフェースに依存するが，具象には依存しない。具象の知識を持つ必要がない。
# 具象クラスでの「インタフェースのルールを守る範囲での変更」は抽象クラスへ影響を与えない。

from abc import ABC, abstractmethod

# 具象クラス（PDFBook，HTMLBook） と EBookReader を結ぶインタフェース
class EBook(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def read(self):
        pass


class EBookReader:
    def __init__(self, book: EBook):
        self.book = book
        pass

    def read(self):
        return self.book.read()

class PDFBook(EBook):
    def __init__(self):
        pass

    def read(self):
        return "reading a pdf book"

class HTMLBook(EBook):
    def __init__(self):
        pass

    def read(self):
        return "reading a HTML book"

if __name__ == '__main__':
    # PDF の本を読む
    pdf_book = PDFBook()
    pdf_reader = EBookReader(pdf_book)
    print(pdf_reader.read())

    # HTML の本を読む
    html_book = HTMLBook()
    html_reader = EBookReader(html_book)
    print(html_reader.read())