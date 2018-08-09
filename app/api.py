from flask import jsonify, Response
from flask.views import MethodView
from webargs.flaskparser import use_args

from app.client import client, EventClientException
from app.router import route
from app.schema import EventSchema


@route("/events", "events-api")
class EventsAPI(MethodView):

    @use_args(EventSchema)
    def post(self, event: EventSchema) -> Response:
        try:
            client.send_event(event)
            return jsonify({
                "message": "Event queued successfully!"
            }), 201
        except EventClientException as e:
            return jsonify({"message": str(e)}), 500
