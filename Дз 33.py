class Word:
    def __init__(self, word, translations=None):
        self.word = word
        self.translations = translations or {}
        self.left = None
        self.right = None

    def add_translation(self, language, translation):
        self.translations[language] = translation

    def remove_translation(self, language):
        if language in self.translations:
            del self.translations[language]

    def update_translation(self, language, new_translation):
        if language in self.translations:
            self.translations[language] = new_translation
        else:
            print("Переклад для вказаної мови не існує.")

    def __str__(self):
        return f"{self.word}: {', '.join([f'{lang}: {trans}' for lang, trans in self.translations.items()])}"


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, word):
        if not self.root:
            self.root = word
        else:
            self._insert_recursive(self.root, word)

    def _insert_recursive(self, node, word):
        if word.word < node.word:
            if node.left is None:
                node.left = word
            else:
                self._insert_recursive(node.left, word)
        elif word.word > node.word:
            if node.right is None:
                node.right = word
            else:
                self._insert_recursive(node.right, word)
        else:
            print("Слово вже існує в словнику.")

    def search(self, word):
        return self._search_recursive(self.root, word)

    def _search_recursive(self, node, word):
        if node is None:
            return None
        elif word == node.word:
            return node
        elif word < node.word:
            return self._search_recursive(node.left, word)
        else:
            return self._search_recursive(node.right, word)


class Dictionary:
    def __init__(self):
        self.tree = Tree()
        self.popularity_counter = {}

    def add_word(self, word, translations=None):
        new_word = Word(word, translations)
        self.tree.insert(new_word)
        self.popularity_counter[word] = 0

    def remove_word(self, word):
        node_to_remove = self.tree.search(word)
        if node_to_remove:
            del self.popularity_counter[word]
        else:
            print("Слово не знайдено в словнику.")

    def add_translation(self, word, language, translation):
        node = self.tree.search(word)
        if node:
            node.add_translation(language, translation)
        else:
            print("Слово не знайдено в словнику.")

    def increment_popularity(self, word):
        if word in self.popularity_counter:
            self.popularity_counter[word] += 1

    def get_top_10_popular_words(self):
        sorted_popularity = sorted(self.popularity_counter.items(), key=lambda x: x[1], reverse=True)
        return [word for word, _ in sorted_popularity[:10]]

    def get_top_10_unpopular_words(self):
        sorted_popularity = sorted(self.popularity_counter.items(), key=lambda x: x[1])
        return [word for word, _ in sorted_popularity[:10]]

    def display_word_translations(self, word):
        node = self.tree.search(word)
        if node:
            print(node)
        else:
            print("Слово не знайдено в словнику.")
dictionary = Dictionary()

dictionary.add_word("яблуко", {"французька": "pomme"})
dictionary.add_word("банан", {"французька": "banane"})
dictionary.add_word("автомобіль", {"французька": "voiture"})
dictionary.add_word("собака", {"французька": "chien"})

dictionary.display_word_translations("яблуко")
dictionary.add_translation("банан", "французька", "banane")

word_banana = dictionary.tree.search("банан")
if word_banana:
    word_banana.update_translation("українська", "бананчик")
else:
    print("Слово не знайдено в словнику.")

word_apple = dictionary.tree.search("яблуко")
if word_apple:
    word_apple.remove_translation("французька")
else:
    print("Слово не знайдено в словнику.")

print("Топ-10 найпопулярніших слів:")
print(dictionary.get_top_10_popular_words())
print("Топ-10 найнепопулярніших слів:")
print(dictionary.get_top_10_unpopular_words())


