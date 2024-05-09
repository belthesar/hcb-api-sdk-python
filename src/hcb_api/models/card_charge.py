# This file was generated by liblab | https://liblab.com/


from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel

import contextlib
with contextlib.suppress(ImportError):
    from .transaction import Transaction
    from .organization import Organization
    from .card import Card
    from .user import User


@JsonMap({"id_": "id", "date_": "date"})
class CardCharge(BaseModel):
    """Card Charge model

    :param id_: id_, defaults to None
    :type id_: str, optional
    :param object: object, defaults to None
    :type object: str, optional
    :param href: href, defaults to None
    :type href: str, optional
    :param memo: memo, defaults to None
    :type memo: str, optional
    :param transaction: Transaction model, defaults to None
    :type transaction: Transaction, optional
    :param organization: Organization model, defaults to None
    :type organization: Organization, optional
    :param amount_cents: amount_cents, defaults to None
    :type amount_cents: int, optional
    :param date_: date_, defaults to None
    :type date_: str, optional
    :param card: Card model, defaults to None
    :type card: Card, optional
    :param user: user, defaults to None
    :type user: User, optional
    """

    def __init__(
        self,
        id_: str = None,
        object: str = None,
        href: str = None,
        memo: str = None,
        transaction: Transaction = None,
        organization: Organization = None,
        amount_cents: int = None,
        date_: str = None,
        card: Card = None,
        user: User = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if object is not None:
            self.object = object
        if href is not None:
            self.href = href
        if memo is not None:
            self.memo = memo
        if transaction is not None:
            self.transaction = self._define_object(transaction, Transaction)
        if organization is not None:
            self.organization = self._define_object(organization, Organization)
        if amount_cents is not None:
            self.amount_cents = amount_cents
        if date_ is not None:
            self.date_ = date_
        if card is not None:
            self.card = self._define_object(card, Card)
        if user is not None:
            self.user = self._define_object(user, User)
