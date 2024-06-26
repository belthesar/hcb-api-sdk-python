# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel

import contextlib
with contextlib.suppress(ImportError):
    from .transaction import Transaction
    from .organization import Organization


class AchTransferStatus(Enum):
    """An enumeration representing different categories.

    :cvar PENDING: "pending"
    :vartype PENDING: str
    :cvar IN_TRANSIT: "in_transit"
    :vartype IN_TRANSIT: str
    :cvar DEPOSITED: "deposited"
    :vartype DEPOSITED: str
    :cvar REJECTED: "rejected"
    :vartype REJECTED: str
    """

    PENDING = "pending"
    IN_TRANSIT = "in_transit"
    DEPOSITED = "deposited"
    REJECTED = "rejected"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, AchTransferStatus._member_map_.values()))


@JsonMap({})
class Beneficiary(BaseModel):
    """Beneficiary

    :param name: name, defaults to None
    :type name: str, optional
    """

    def __init__(self, name: str = None):
        if name is not None:
            self.name = name


@JsonMap({"id_": "id", "date_": "date"})
class AchTransfer(BaseModel):
    """ACH Transfer model

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
    :type status: AchTransferStatus, optional
    :param beneficiary: beneficiary, defaults to None
    :type beneficiary: Beneficiary, optional
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
        status: AchTransferStatus = None,
        beneficiary: Beneficiary = None,
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
            self.status = self._enum_matching(
                status, AchTransferStatus.list(), "status"
            )
        if beneficiary is not None:
            self.beneficiary = self._define_object(beneficiary, Beneficiary)
