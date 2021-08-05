from typing import Dict, List, NamedTuple

import db

class Category(NamedTuple):
    name: str
    is_base_expense: bool
    aliases: List[str]

class Categories:
    def __init__(self):
        self.categories = self._load_categories()

    def _load_categories(self) -> List[Category]:
        categories = db.fetchall("category", "name is_base_expense aliases".split())
        print(categories)
        categories = self._fill_aliases(categories)
        print(categories)
        return categories

    def get_all_categories(self) -> List[Category]:
        return self.categories

    def _fill_aliases(self, categories: List[Dict]) -> List[Category]:
        categories_result = []
        for category in categories:
            aliases = category["aliases"].split(",")
            aliases.append(category["name"])
            categories_result.append(Category(
                name=category['name'],
                is_base_expense=category['is_base_expense'],
                aliases=aliases
            ))
        return categories_result

    def get_category(self, category_name: str) -> Category:
        finded = None
        other_category = None
        for category in self.categories:
            if category.name == "other":
                other_category = category
            for alias in category.aliases:
                if category_name in alias:
                    finded = category
        if not finded:
            finded = other_category
        return finded