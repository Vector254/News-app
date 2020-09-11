class Article:
    '''
    Article class to define Movie Objects
    '''

    def __init__(self,source,author,title,description,url,published_at):
        self.source = source
        self.author=author
        self.title = title
        self.description = description
        self.url = url
        self.published_at =published_at