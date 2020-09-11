class Article:
    '''
    Article class to define Movie Objects
    '''

    def __init__(self,source,author,title,description,url,published_at):
        self.source = source.name
        self.author=author
        self.title = title
        self.description = description
        self.url = url
        self.vote_average = vote_average
        self.published_at =publishedAt