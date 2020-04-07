"""
    Serialize & Deserialize OY response
    _____________________________________
    serialize all of response to prevent all changes from oy side breaking the
    libs
"""
from marshmallow import Schema, fields


class InquiryAccountSchema(Schema):
    """ used to serialize oy inquiry account response """

    recipient_bank = fields.Str()
    recipient_account = fields.Str()
    recipient_name = fields.Str()
    timestamp = fields.DateTime(format="%d-%m-%Y %H:%M:%S")


class DisburseSchema(Schema):
    """ used to serialize oy disburse response """

    recipient_bank = fields.Str(attribute="recipient_bank")
    recipient_account = fields.Str(attribute="recipient_account")
    amount = fields.Decimal()
    trx_id = fields.Str()  # trx id genertaed from oy
    trx_reference = fields.Str()  # trx id received from oy
    timestamp = fields.DateTime(format="%d-%m-%Y %H:%M:%S")


class DisburseStatusSchema(Schema):
    """ used to serialize oy disburse response """

    name = fields.Str(attribute="recipient_name")
    bank_code = fields.Str(attribute="recipient_bank")
    account_no = fields.Str(attribute="recipient_account")
    trx_id = fields.Str(attribute="partner_trx_id")  # the one we request to oy
    trx_reference = fields.Str(attribute="trx_id")  # the one we recevie from oy
    amount = fields.Decimal()
    timestamp = fields.DateTime(format="%d-%m-%Y %H:%M:%S")
    created_date = fields.DateTime(format="%d-%m-%Y %H:%M:%S")
    last_updated_date = fields.DateTime(format="%d-%m-%Y %H:%M:%S")


class GetBalanceSchema(Schema):
    """ used to serialize oy get balance response """

    balance = fields.Decimal()
    timestamp = fields.DateTime(format="%d-%m-%Y %H:%M:%S")


class GenerateVaSchema(Schema):
    """ used to serialize oy generate va no response """

    va_no = fields.Str(attribute="vaNumber")
    amount = fields.Decimal()
    timestamp = fields.DateTime(format="%d-%m-%Y %H:%M:%S")
