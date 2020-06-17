from datetime import datetime

from pony.orm import PrimaryKey, Required, Optional, Set, LongStr

from src.models import db


class Post(db.Entity):
    post_pk = PrimaryKey(int, auto=True)
    title = Required(str)
    content = Optional(LongStr)
    published_at = Required(datetime, default=datetime.now)
    categories = Set("Category")
    comments = Set("Comment")


