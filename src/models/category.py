from pony.orm import PrimaryKey, Set

from src.models import db


class Category(db.Entity):
    name = PrimaryKey(str)
    posts = Set("Post")