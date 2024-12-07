import random


class Component:
    def __init__(self, name, alias=None, content=None, is_abstract=False, tags=None, anti_tags=None):
        self.name = name
        self.alias = alias
        self.tags = set(tags)
        self.anti_tags = set(anti_tags)

        if content is not None and not isinstance(content, list):
            content = [content]

        self.content = content
        self.is_abstract = is_abstract

    def get_random_content(self):
        if self.content and len(self.content) > 0:
            return random.choice(self.content)
        return None

    def __repr__(self):
        return f"Component(name={self.name}, alias={self.alias} abstract={self.is_abstract})"
