from marshmallow import Schema, fields


class EventSchema(Schema):
    event_type = fields.String()
    data = fields.String()
