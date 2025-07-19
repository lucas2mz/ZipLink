#!/usr/bin/env python3

from app.backend.models.link import Link
import random
import string
from app.backend.persistance.LinkRepository import LinkRepository

class ZPFacade:

    def __init__(self):
        self.link = LinkRepository()
        
    def create_url(self, data):
        link = Link(**data)
        self.link.add(link)
        return link
    
    def get_by_short_code(self, short_code):
        return self.link.get_by_short_code(short_code=short_code)
    
    def update_url(self, link_id, data):
        return self.link.update(link_id=link_id, data=data)

    def generate_short_code(self, length=6):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choices(characters, k=length))
