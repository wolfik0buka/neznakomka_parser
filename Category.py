class Category:
    def __init__(self, name, link):
        self.name = name
        self.link = link
        self.children = []

    def __str__(self):
        return self.name + "("+ str(len(self.children)) +"): " + self.link

    def add_child(self, child):
        self.children.append(child)

    def to_dict(self):
        # Преобразуем объект в словарь
        return {
            'name': self.name,
            'link': self.link,
            'children': [child.to_dict() for child in self.children]  # Рекурсивно сериализуем детей
        }

if __name__ == '__main__':
    category = Category('test')
    print(category)