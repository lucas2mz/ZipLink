from flask_restx import Namespace, Resource, fields
from flask import redirect
from app.backend.services import facade

api = Namespace('zipLink', description='ZipLink operations')

LinkModel = api.model('Link', {
    'Url': fields.String(required=True, description='Url to zip')
})

@api.route('/shorten')
class Link(Resource):
    @api.expect(LinkModel, validate=True)
    def post(self):

        url = api.payload.get('Url')
        if not url:
            return {'error': 'Missing URL'}, 400

        short_code = facade.generate_short_code()
        while facade.get_by_short_code(short_code):
            short_code = facade.generate_short_code()

        data = {
                "original_url": url, 
                "short_url": f"http://localhost:5000/{short_code}", 
                "short_code": short_code, 
                "visits": 0
        }
        
        try:
            link = facade.create_url(data)
        except ValueError:
            return {'error': 'Invalid input data'}, 400
        return {"id": link.id, "original_url": link.original_url, "short_url": link.short_url, "short_code": link.short_code, "visits": link.visits}, 201
        
@api.route('/<short_code>')
class LinkGet(Resource):
    def get(self, short_code):
        url = facade.get_by_short_code(short_code)
        if not url:
            return {'error': "Url not found"}, 404
        url.visits += 1

        facade.update_url(link_id=url.id, data={"visits": url.visits})
        
        return redirect(url.original_url)