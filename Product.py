class Product:
    def __init__(self, name, article, sections = []):
        self.name = name
        self.article = article
        self.sections = sections if len(sections) else []

    def __str__(self):
        return self.name +"("+ str(len(self.sections)) +"): " + self.article


if __name__ == '__main__':
    product = Product('test','123')
    print(product)