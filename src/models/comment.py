from datetime import datetime

from pony.orm import Optional, Required

from src.models import db
from src.models.post import Post


class Comment(db.Entity):
    post = Optional(Post)
    content = Required(str)
    published_at = Required(datetime, default=datetime.now)