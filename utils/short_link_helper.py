import hashlib

from sqlalchemy.exc import SQLAlchemyError

from db.database import SessionLocal
from db.models import Link

db = SessionLocal()


def generate_hash(original_url: str) -> str:
    hashed = hashlib.sha256(original_url.encode()).hexdigest()
    return hashed[:7]


def generate_short_link(url: str) -> list:
    if "http" not in url or "https" not in url:
        url = "https://" + url
    short_url = generate_hash(url)
    return [short_url, url]


def save_link(url: str, short_url: str) -> None:
    link = Link(url=url, short_url=short_url)
    try:
        db.add(link)
        db.commit()
        db.refresh(link)
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()


def get_link(short_url: str, request) -> str:
    existing_link = db.query(Link).filter_by(short_url=short_url).first()

    if existing_link:
        new_link = request.url[:-19] + short_url
        return new_link
    return "Link not found"
