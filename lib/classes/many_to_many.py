class Article:
    article_container = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.article_container.append(self)

    @property
    def title(self):
        return self._title 

    @title.setter
    def title(self, set_title):
        if isinstance(set_title, str) and (5 <= len(set_title) <= 50) and not hasattr(self, "title"):
            self._title = set_title
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception('The name should be of type string')
        if (len(name) <= 0):
            raise Exception('The name cannot be empty')
        self.name = name

    def articles(self):
        return [article for article in Article.article_container if article.author == self]
    def magazines(self):
        return list([article.magazine for article in Article.article_container if article.author == self])

    def add_article(self, magazine, title):
        return Article(self, magazine, title)


    def topic_areas(self):
        return(
            list({magazine.category for magazine in self.magazines()})
            if self.magazines()
            else None
        )

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    
    @property 
    def name(self):
        return self._name
    @name.setter
    def name(self, set_name):
        if isinstance(set_name, str) and 2 <= len(set_name) <= 16:
            self._name = set_name
        else:
            raise ValueError("Magazine name must be of type string and between 2 and 16 characters")
        
    @property
    def category(self):
        return self._category
    @category.setter 
    def category(self, set_category):
        if (len(set_category) == 0):
            raise ValueError("Category cannot be empty")
        if not isinstance(set_category, str):
            raise Exception("Category must be of type string") 
        else:
            self._category = set_category
        
    def articles(self):
        return [article for article in Article.article_container if article.magazine == self ]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        articles = self.articles()
        if (articles):
           return [article.title for article in articles]
        else:
            None


    def contributing_authors(self):
       contributors = [article.author for article in Article.article_container if article.magazine == self]
       for element in contributors:
            if contributors.count(element) >= 2:
                return [element for element in contributors]
            else: 
                return None