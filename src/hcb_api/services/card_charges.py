# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.card_charge import CardCharge


class CardChargesService(BaseService):

    @cast_models
    def list_an_organizations_card_charges(
        self,
        organization_id: str,
        expand: str = None,
        page: int = None,
        per_page: int = None,
        offset: int = None,
    ) -> List[CardCharge]:
        """Transactions created using an HCB card.

        :param organization_id: Organization ID or slug.
        :type organization_id: str
        :param expand: Object types to expand in the API response (separated by commas), defaults to None
        :type expand: str, optional
        :param page: Page offset to fetch., defaults to None
        :type page: int, optional
        :param per_page: Number of results to return per page., defaults to None
        :type per_page: int, optional
        :param offset: Pad a number of results., defaults to None
        :type offset: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Return a list of card charges
        :rtype: List[CardCharge]
        """

        Validator(str).validate(organization_id)
        Validator(str).is_optional().validate(expand)
        Validator(int).is_optional().validate(page)
        Validator(int).is_optional().validate(per_page)
        Validator(int).is_optional().validate(offset)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v3/organizations/{{organization_id}}/card_charges",
                self.get_default_headers(),
            )
            .add_path("organization_id", organization_id)
            .add_query("expand", expand)
            .add_query("page", page)
            .add_query("per_page", per_page)
            .add_query("offset", offset)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return [CardCharge._unmap(item) for item in response]

    @cast_models
    def get_a_card_charge(self, card_charge_id: str, expand: str = None) -> CardCharge:
        """get_a_card_charge

        :param card_charge_id: Card charge ID
        :type card_charge_id: str
        :param expand: Object types to expand in the API response (separated by commas), defaults to None
        :type expand: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Return a card charge
        :rtype: CardCharge
        """

        Validator(str).validate(card_charge_id)
        Validator(str).is_optional().validate(expand)

        serialized_request = (
            Serializer(
                f"{self.base_url}/api/v3/card_charges/{{card_charge_id}}",
                self.get_default_headers(),
            )
            .add_path("card_charge_id", card_charge_id)
            .add_query("expand", expand)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return CardCharge._unmap(response)