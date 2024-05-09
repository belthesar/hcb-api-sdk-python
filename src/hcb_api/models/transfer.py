# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel

import contextlib
with contextlib.suppress(ImportError):
    from .transaction import Transaction
    from .organization import Organization


class TransferStatus(Enum):
    """An enumeration representing different categories.

    :cvar FULFILLED: "fulfilled"
    :vartype FULFILLED: str
    :cvar PROCESSING: "processing"
    :vartype PROCESSING: str
    :cvar REJECTED: "rejected"
    :vartype REJECTED: str
    :cvar CANCELED: "canceled"
    :vartype CANCELED: str
    :cvar ERRORED: "errored"
    :vartype ERRORED: str
    :cvar UNDER_REVIEW: "under_review"
    :vartype UNDER_REVIEW: str
    :cvar PENDING: "pending"
    :vartype PENDING: str
    """

    FULFILLED = "fulfilled"
    PROCESSING = "processing"
    REJECTED = "rejected"
    CANCELED = "canceled"
    ERRORED = "errored"
    UNDER_REVIEW = "under_review"
    PENDING = "pending"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, TransferStatus._member_map_.values()))


@JsonMap({"id_": "id", "date_": "date"})
class Transfer(BaseModel):
    """Transfer model

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
    :type amount_cents: str, optional
    :param date_: date_, defaults to None
    :type date_: str, optional
    :param status: status, defaults to None
    :type status: TransferStatus, optional
    """

    def __init__(
        self,
        id_: str = None,
        object: str = None,
        href: str = None,
        memo: str = None,
        transaction: Transaction = None,
        organization: Organization = None,
        amount_cents: str = None,
        date_: str = None,
        status: TransferStatus = None,
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
        if status is not None:
            self.status = self._enum_matching(status, TransferStatus.list(), "status")
