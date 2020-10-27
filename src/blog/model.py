from dataclasses import dataclass
from datetime import date


@dataclass
class Post:
    title: str
    body: str
    created_at: date
    updated_at: date


