# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel

import contextlib
with contextlib.suppress(ImportError):
    from .user import User


class Category(Enum):
    """An enumeration representing different categories.

    :cvar HACKATHON: "hackathon"
    :vartype HACKATHON: str
    :cvar HACK_CLUB: "hack_club"
    :vartype HACK_CLUB: str
    :cvar NONPROFIT: "nonprofit"
    :vartype NONPROFIT: str
    :cvar EVENT: "event"
    :vartype EVENT: str
    :cvar HIGH_SCHOOL_HACKATHON: "high_school_hackathon"
    :vartype HIGH_SCHOOL_HACKATHON: str
    :cvar ROBOTICS_TEAM: "robotics_team"
    :vartype ROBOTICS_TEAM: str
    :cvar HARDWARE_GRANT: "hardware_grant"
    :vartype HARDWARE_GRANT: str
    :cvar HACK_CLUB_HQ: "hack_club_hq"
    :vartype HACK_CLUB_HQ: str
    :cvar OUTERNET_GUILD: "outernet_guild"
    :vartype OUTERNET_GUILD: str
    :cvar GRANT_RECIPIENT: "grant_recipient"
    :vartype GRANT_RECIPIENT: str
    :cvar SALARY: "salary"
    :vartype SALARY: str
    :cvar AI: "ai"
    :vartype AI: str
    :cvar HCB_INTERNALS: "hcb_internals"
    :vartype HCB_INTERNALS: str
    """

    HACKATHON = "hackathon"
    HACK_CLUB = "hack_club"
    NONPROFIT = "nonprofit"
    EVENT = "event"
    HIGH_SCHOOL_HACKATHON = "high_school_hackathon"
    ROBOTICS_TEAM = "robotics_team"
    HARDWARE_GRANT = "hardware_grant"
    HACK_CLUB_HQ = "hack_club_hq"
    OUTERNET_GUILD = "outernet_guild"
    GRANT_RECIPIENT = "grant_recipient"
    SALARY = "salary"
    AI = "ai"
    HCB_INTERNALS = "hcb_internals"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Category._member_map_.values()))


@JsonMap({})
class Balances(BaseModel):
    """Balances

    :param balance_cents: balance_cents, defaults to None
    :type balance_cents: int, optional
    :param fee_balance_cents: fee_balance_cents, defaults to None
    :type fee_balance_cents: int, optional
    :param incoming_balance_cents: incoming_balance_cents, defaults to None
    :type incoming_balance_cents: int, optional
    :param total_raised: total_raised, defaults to None
    :type total_raised: int, optional
    """

    def __init__(
        self,
        balance_cents: int = None,
        fee_balance_cents: int = None,
        incoming_balance_cents: int = None,
        total_raised: int = None,
    ):
        if balance_cents is not None:
            self.balance_cents = balance_cents
        if fee_balance_cents is not None:
            self.fee_balance_cents = fee_balance_cents
        if incoming_balance_cents is not None:
            self.incoming_balance_cents = incoming_balance_cents
        if total_raised is not None:
            self.total_raised = total_raised


@JsonMap({"id_": "id"})
class Organization(BaseModel):
    """Organization model

    :param id_: id_, defaults to None
    :type id_: str, optional
    :param object: object, defaults to None
    :type object: str, optional
    :param href: href, defaults to None
    :type href: str, optional
    :param name: name, defaults to None
    :type name: str, optional
    :param slug: slug, defaults to None
    :type slug: str, optional
    :param website: website, defaults to None
    :type website: str, optional
    :param category: category, defaults to None
    :type category: Category, optional
    :param transparent: transparent, defaults to None
    :type transparent: bool, optional
    :param demo_mode: demo_mode, defaults to None
    :type demo_mode: bool, optional
    :param logo: logo, defaults to None
    :type logo: str, optional
    :param donation_header: donation_header, defaults to None
    :type donation_header: str, optional
    :param background_image: background_image, defaults to None
    :type background_image: str, optional
    :param public_message: public_message, defaults to None
    :type public_message: str, optional
    :param donation_link: donation_link, defaults to None
    :type donation_link: str, optional
    :param balances: balances, defaults to None
    :type balances: Balances, optional
    :param created_at: created_at, defaults to None
    :type created_at: str, optional
    :param users: users, defaults to None
    :type users: List[User], optional
    """

    def __init__(
        self,
        id_: str = None,
        object: str = None,
        href: str = None,
        name: str = None,
        slug: str = None,
        website: str = None,
        category: Category = None,
        transparent: bool = None,
        demo_mode: bool = None,
        logo: str = None,
        donation_header: str = None,
        background_image: str = None,
        public_message: str = None,
        donation_link: str = None,
        balances: Balances = None,
        created_at: str = None,
        users: List[User] = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if object is not None:
            self.object = object
        if href is not None:
            self.href = href
        if name is not None:
            self.name = name
        if slug is not None:
            self.slug = slug
        if website is not None:
            self.website = website
        if category is not None:
            self.category = self._enum_matching(category, Category.list(), "category")
        if transparent is not None:
            self.transparent = transparent
        if demo_mode is not None:
            self.demo_mode = demo_mode
        if logo is not None:
            self.logo = logo
        if donation_header is not None:
            self.donation_header = donation_header
        if background_image is not None:
            self.background_image = background_image
        if public_message is not None:
            self.public_message = public_message
        if donation_link is not None:
            self.donation_link = donation_link
        if balances is not None:
            self.balances = self._define_object(balances, Balances)
        if created_at is not None:
            self.created_at = created_at
        if users is not None:
            self.users = self._define_list(users, User)
