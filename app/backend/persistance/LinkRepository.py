from app import db
from app.backend.models.link import Link

class LinkRepository:
    def __init__(self):
        self.model = Link

    def add(self, link: Link):
        db.session.add(link)
        db.session.commit()
        return link

    def get(self, link_id: str):
        return self.model.query.get(link_id)

    def get_all(self):
        return self.model.query.all()

    def update(self, link_id: str, data: dict):
        link = self.get(link_id)
        if link:
            for key, value in data.items():
                if hasattr(link, key):
                    setattr(link, key, value)
            db.session.commit()
        return link

    def delete(self, link_id: str):
        link = self.get(link_id)
        if link:
            db.session.delete(link)
            db.session.commit()
            return True
        return False

    def get_by_short_code(self, short_code: str):
        return self.model.query.filter_by(short_code=short_code).first()

    def get_by_original_url(self, original_url: str):
        return self.model.query.filter_by(original_url=original_url).first()
