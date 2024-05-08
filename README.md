# HCB_API Python SDK 1.0.1

A Python SDK for HCB_API.

- API version: 3.0.0
- SDK version: 1.0.1

This Python SDK maintained by @belthesar. I am in no way affiliated with Hack Club or the HCB API. This SDK is not officially supported by Hack Club. Use at your own risk.

From the [HCB API documentation](https://hcb-api.hackclub.com/docs):

> The HCB API is an unauthenticated REST API that allows you to read public information from organizations with <a href='https://changelog.hcb.hackclub.com/transparent-finances-(optional-feature)-151427'>Transparency Mode</a> enabled. <br><br><strong>Questions or suggestions?</strong> <br>Reach us in the #hcb channel on the <a href='https://hackclub.com/slack'>Hack Club Slack</a> or email <a href='mailto:hcb@hackclub.com'>hcb@hackclub.com</a>. <br><br>Happy hacking! ✨

## Table of Contents

- [Installation](#installation)
- [Authentication](#authentication)
- [Services](#services)

## Installation

```bash
pip install hcb_api
```

## Authentication

The HCB API does not require authentication, and only allows you to read public information from organizations with [Transparency Mode](https://changelog.hcb.hackclub.com/transparent-finances-(optional-feature)-151427) enabled.
While the SDK does have support for an `access_token` parameter, it is not required to make requests to the API. In the event that the API requires authentication in the future, the SDK will be updated to support it.

## Services

A list of all SDK services. Click on the service name to access its corresponding service methods.

| Service                                       |
| :-------------------------------------------- |
| [CardsService](#cardsservice)                 |
| [ChecksService](#checksservice)               |
| [AchTransfersService](#achtransfersservice)   |
| [InvoicesService](#invoicesservice)           |
| [TransfersService](#transfersservice)         |
| [DonationsService](#donationsservice)         |
| [CardChargesService](#cardchargesservice)     |
| [TransactionsService](#transactionsservice)   |
| [OrganizationsService](#organizationsservice) |

### CardsService

A list of all methods in the `CardsService` service. Click on the method name to view detailed information about that method.

| Methods                                                     | Description |
| :---------------------------------------------------------- | :---------- |
| [list_an_organizations_cards](#list_an_organizations_cards) |             |
| [get_a_single_card](#get_a_single_card)                     |             |

#### **list_an_organizations_cards**

- HTTP Method: `GET`
- Endpoint: `/api/v3/organizations/{organization_id}/cards`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| organization_id | str | ✅ | list_an_organizations_cards |
| expand | str | ❌ | list_an_organizations_cards |
| page | int | ❌ | list_an_organizations_cards |
| per_page | int | ❌ | list_an_organizations_cards |
| offset | int | ❌ | list_an_organizations_cards |

**Return Type**

`List[Card]`

**Example Usage Code Snippet**

```py
from hcb_api import HCB_API, Environment

sdk = HCB_API(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.cards.list_an_organizations_cards(
    organization_id="organization_id",
    expand="expand",
    page=1,
    per_page=50,
    offset=8
)

print(result)
```

#### **get_a_single_card**

- HTTP Method: `GET`
- Endpoint: `/api/v3/cards/{card_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| card_id | str | ✅ | get_a_single_card |
| expand | str | ❌ | get_a_single_card |

**Return Type**

`Card`

**Example Usage Code Snippet**

```py
from hcb_api import HCB_API, Environment

sdk = HCB_API(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.cards.get_a_single_card(
    card_id="card_id",
    expand="expand"
)

print(result)
```

### ChecksService

A list of all methods in the `ChecksService` service. Click on the method name to view detailed information about that method.

| Methods                                                       | Description |
| :------------------------------------------------------------ | :---------- |
| [list_an_organizations_checks](#list_an_organizations_checks) |             |
| [get_a_single_check](#get_a_single_check)                     |             |

#### **list_an_organizations_checks**

- HTTP Method: `GET`
- Endpoint: `/api/v3/organizations/{organization_id}/checks`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| organization_id | str | ✅ | list_an_organizations_checks |
| expand | str | ❌ | list_an_organizations_checks |
| page | int | ❌ | list_an_organizations_checks |
| per_page | int | ❌ | list_an_organizations_checks |
| offset | int | ❌ | list_an_organizations_checks |

**Return Type**

`List[Check]`

**Example Usage Code Snippet**

```py
from hcb_api import HCB_API, Environment

sdk = HCB_API(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.checks.list_an_organizations_checks(
    organization_id="organization_id",
    expand="expand",
    page=1,
    per_page=50,
    offset=1
)

print(result)
```

#### **get_a_single_check**

- HTTP Method: `GET`
- Endpoint: `/api/v3/checks/{check_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| check_id | str | ✅ | get_a_single_check |
| expand | str | ❌ | get_a_single_check |

**Return Type**

`Check`

**Example Usage Code Snippet**

```py
from hcb_api import HCB_API, Environment

sdk = HCB_API(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.checks.get_a_single_check(
    check_id="check_id",
    expand="expand"
)

print(result)
```

### AchTransfersService

A list of all methods in the `AchTransfersService` service. Click on the method name to view detailed information about that method.

| Methods                                                                     | Description |
| :-------------------------------------------------------------------------- | :---------- |
| [list_an_organizations_ach_transfers](#list_an_organizations_ach_transfers) |             |
| [get_a_single_ach_transfer](#get_a_single_ach_transfer)                     |             |

#### **list_an_organizations_ach_transfers**

- HTTP Method: `GET`
- Endpoint: `/api/v3/organizations/{organization_id}/ach_transfers`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| organization_id | str | ✅ | list_an_organizations_ach_transfers |
| expand | str | ❌ | list_an_organizations_ach_transfers |
| page | int | ❌ | list_an_organizations_ach_transfers |
| per_page | int | ❌ | list_an_organizations_ach_transfers |
| offset | int | ❌ | list_an_organizations_ach_transfers |

**Return Type**

`List[AchTransfer]`

**Example Usage Code Snippet**

```py
from hcb_api import HCB_API, Environment

sdk = HCB_API(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.ach_transfers.list_an_organizations_ach_transfers(
    organization_id="organization_id",
    expand="expand",
    page=1,
    per_page=50,
    offset=9
)

print(result)
```

#### **get_a_single_ach_transfer**

- HTTP Method: `GET`
- Endpoint: `/api/v3/ach_transfers/{ach_transfer_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| ach_transfer_id | str | ✅ | get_a_single_ach_transfer |
| expand | str | ❌ | get_a_single_ach_transfer |

**Return Type**

`AchTransfer`

**Example Usage Code Snippet**

```py
from hcb_api import HCB_API, Environment

sdk = HCB_API(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.ach_transfers.get_a_single_ach_transfer(
    ach_transfer_id="ach_transfer_id",
    expand="expand"
)

print(result)
```

### InvoicesService

A list of all methods in the `InvoicesService` service. Click on the method name to view detailed information about that method.

| Methods                                                           | Description |
| :---------------------------------------------------------------- | :---------- |
| [list_an_organizations_invoices](#list_an_organizations_invoices) |             |
| [get_a_single_invoice](#get_a_single_invoice)                     |             |

#### **list_an_organizations_invoices**

- HTTP Method: `GET`
- Endpoint: `/api/v3/organizations/{organization_id}/invoices`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| organization_id | str | ✅ | list_an_organizations_invoices |
| expand | str | ❌ | list_an_organizations_invoices |
| page | int | ❌ | list_an_organizations_invoices |
| per_page | int | ❌ | list_an_organizations_invoices |
| offset | int | ❌ | list_an_organizations_invoices |

**Return Type**

`List[Invoice]`

**Example Usage Code Snippet**

```py
from hcb_api import HCB_API, Environment

sdk = HCB_API(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.invoices.list_an_organizations_invoices(
    organization_id="organization_id",
    expand="expand",
    page=1,
    per_page=50,
    offset=9
)

print(result)
```

#### **get_a_single_invoice**

- HTTP Method: `GET`
- Endpoint: `/api/v3/invoices/{invoice_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| invoice_id | str | ✅ | get_a_single_invoice |
| expand | str | ❌ | get_a_single_invoice |

**Return Type**

`Invoice`

**Example Usage Code Snippet**

```py
from hcb_api import HCB_API, Environment

sdk = HCB_API(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.invoices.get_a_single_invoice(
    invoice_id="invoice_id",
    expand="expand"
)

print(result)
```

### TransfersService

A list of all methods in the `TransfersService` service. Click on the method name to view detailed information about that method.

| Methods                                                             | Description |
| :------------------------------------------------------------------ | :---------- |
| [list_an_organizations_transfers](#list_an_organizations_transfers) |             |
| [get_a_single_transfer](#get_a_single_transfer)                     |             |

#### **list_an_organizations_transfers**

- HTTP Method: `GET`
- Endpoint: `/api/v3/organizations/{organization_id}/transfers`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| organization_id | str | ✅ | list_an_organizations_transfers |
| expand | str | ❌ | list_an_organizations_transfers |
| page | int | ❌ | list_an_organizations_transfers |
| per_page | int | ❌ | list_an_organizations_transfers |
| offset | int | ❌ | list_an_organizations_transfers |

**Return Type**

`List[Transfer]`

**Example Usage Code Snippet**

```py
from hcb_api import HCB_API, Environment

sdk = HCB_API(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.transfers.list_an_organizations_transfers(
    organization_id="organization_id",
    expand="expand",
    page=1,
    per_page=50,
    offset=7
)

print(result)
```

#### **get_a_single_transfer**

- HTTP Method: `GET`
- Endpoint: `/api/v3/transfers/{transfer_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| transfer_id | str | ✅ | get_a_single_transfer |
| expand | str | ❌ | get_a_single_transfer |

**Return Type**

`Transfer`

**Example Usage Code Snippet**

```py
from hcb_api import HCB_API, Environment

sdk = HCB_API(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.transfers.get_a_single_transfer(
    transfer_id="transfer_id",
    expand="expand"
)

print(result)
```

### DonationsService

A list of all methods in the `DonationsService` service. Click on the method name to view detailed information about that method.

| Methods                                                             | Description |
| :------------------------------------------------------------------ | :---------- |
| [list_an_organizations_donations](#list_an_organizations_donations) |             |
| [get_a_single_donation](#get_a_single_donation)                     |             |

#### **list_an_organizations_donations**

- HTTP Method: `GET`
- Endpoint: `/api/v3/organizations/{organization_id}/donations`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| organization_id | str | ✅ | list_an_organizations_donations |
| expand | str | ❌ | list_an_organizations_donations |
| page | int | ❌ | list_an_organizations_donations |
| per_page | int | ❌ | list_an_organizations_donations |
| offset | int | ❌ | list_an_organizations_donations |

**Return Type**

`List[Donation]`

**Example Usage Code Snippet**

```py
from hcb_api import HCB_API, Environment

sdk = HCB_API(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.donations.list_an_organizations_donations(
    organization_id="organization_id",
    expand="expand",
    page=1,
    per_page=50,
    offset=6
)

print(result)
```

#### **get_a_single_donation**

- HTTP Method: `GET`
- Endpoint: `/api/v3/donations/{donation_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| donation_id | str | ✅ | get_a_single_donation |
| expand | str | ❌ | get_a_single_donation |

**Return Type**

`Donation`

**Example Usage Code Snippet**

```py
from hcb_api import HCB_API, Environment

sdk = HCB_API(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.donations.get_a_single_donation(
    donation_id="donation_id",
    expand="expand"
)

print(result)
```

### CardChargesService

A list of all methods in the `CardChargesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                   | Description                             |
| :------------------------------------------------------------------------ | :-------------------------------------- |
| [list_an_organizations_card_charges](#list_an_organizations_card_charges) | Transactions created using an HCB card. |
| [get_a_card_charge](#get_a_card_charge)                                   |                                         |

#### **list_an_organizations_card_charges**

Transactions created using an HCB card.

- HTTP Method: `GET`
- Endpoint: `/api/v3/organizations/{organization_id}/card_charges`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| organization_id | str | ✅ | Transactions created using an HCB card. |
| expand | str | ❌ | Transactions created using an HCB card. |
| page | int | ❌ | Transactions created using an HCB card. |
| per_page | int | ❌ | Transactions created using an HCB card. |
| offset | int | ❌ | Transactions created using an HCB card. |

**Return Type**

`List[CardCharge]`

**Example Usage Code Snippet**

```py
from hcb_api import HCB_API, Environment

sdk = HCB_API(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.card_charges.list_an_organizations_card_charges(
    organization_id="organization_id",
    expand="expand",
    page=1,
    per_page=50,
    offset=8
)

print(result)
```

#### **get_a_card_charge**

- HTTP Method: `GET`
- Endpoint: `/api/v3/card_charges/{card_charge_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| card_charge_id | str | ✅ | get_a_card_charge |
| expand | str | ❌ | get_a_card_charge |

**Return Type**

`CardCharge`

**Example Usage Code Snippet**

```py
from hcb_api import HCB_API, Environment

sdk = HCB_API(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.card_charges.get_a_card_charge(
    card_charge_id="card_charge_id",
    expand="expand"
)

print(result)
```

### TransactionsService

A list of all methods in the `TransactionsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                   | Description                                                                                                                                             |
| :------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [list_an_organizations_transactions](#list_an_organizations_transactions) | Transaction represent a line item on an Organization's ledger. There are various <em>types</em> of transaction (see the <em>type</em> below).<br/><br/> |
| [get_a_single_transaction](#get_a_single_transaction)                     |                                                                                                                                                         |

#### **list_an_organizations_transactions**

Transaction represent a line item on an Organization's ledger. There are various <em>types</em> of transaction (see the <em>type</em> below).<br/><br/>

- HTTP Method: `GET`
- Endpoint: `/api/v3/organizations/{organization_id}/transactions`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| organization_id | str | ✅ | Transaction represent a line item on an Organization's ledger. There are various <em>types</em> of transaction (see the <em>type</em> below).<br/><br/> |
| expand | str | ❌ | Transaction represent a line item on an Organization's ledger. There are various <em>types</em> of transaction (see the <em>type</em> below).<br/><br/> |
| page | int | ❌ | Transaction represent a line item on an Organization's ledger. There are various <em>types</em> of transaction (see the <em>type</em> below).<br/><br/> |
| per_page | int | ❌ | Transaction represent a line item on an Organization's ledger. There are various <em>types</em> of transaction (see the <em>type</em> below).<br/><br/> |
| offset | int | ❌ | Transaction represent a line item on an Organization's ledger. There are various <em>types</em> of transaction (see the <em>type</em> below).<br/><br/> |

**Return Type**

`List[Transaction]`

**Example Usage Code Snippet**

```py
from hcb_api import HCB_API, Environment

sdk = HCB_API(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.transactions.list_an_organizations_transactions(
    organization_id="organization_id",
    expand="expand",
    page=1,
    per_page=50,
    offset=10
)

print(result)
```

#### **get_a_single_transaction**

- HTTP Method: `GET`
- Endpoint: `/api/v3/transactions/{transaction_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| transaction_id | str | ✅ | get_a_single_transaction |
| expand | str | ❌ | get_a_single_transaction |

**Return Type**

`Transaction`

**Example Usage Code Snippet**

```py
from hcb_api import HCB_API, Environment

sdk = HCB_API(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.transactions.get_a_single_transaction(
    transaction_id="transaction_id",
    expand="expand"
)

print(result)
```

### OrganizationsService

A list of all methods in the `OrganizationsService` service. Click on the method name to view detailed information about that method.

| Methods                                                           | Description                                                                                                                                                                                                 |
| :---------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_a_single_organization](#get_a_single_organization)           | The organization must be in <a href='https://changelog.hcb.hackclub.com/transparent-finances-(optional-feature)-151427'><strong>Transparency Mode</strong></a>.                                             |
| [list_transparent_organizations](#list_transparent_organizations) | Returns a list of organizations in <a href='https://changelog.hcb.hackclub.com/transparent-finances-(optional-feature)-151427'><strong>Transparency Mode</strong></a> that have opted in to public listing. |

#### **get_a_single_organization**

The organization must be in <a href='https://changelog.hcb.hackclub.com/transparent-finances-(optional-feature)-151427'><strong>Transparency Mode</strong></a>.

- HTTP Method: `GET`
- Endpoint: `/api/v3/organizations/{organization_id}`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| organization_id | str | ✅ | The organization must be in <a href='https://changelog.hcb.hackclub.com/transparent-finances-(optional-feature)-151427'><strong>Transparency Mode</strong></a>. |
| expand | str | ❌ | The organization must be in <a href='https://changelog.hcb.hackclub.com/transparent-finances-(optional-feature)-151427'><strong>Transparency Mode</strong></a>. |

**Return Type**

`Organization`

**Example Usage Code Snippet**

```py
from hcb_api import HCB_API, Environment

sdk = HCB_API(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.organizations.get_a_single_organization(
    organization_id="organization_id",
    expand="expand"
)

print(result)
```

#### **list_transparent_organizations**

Returns a list of organizations in <a href='https://changelog.hcb.hackclub.com/transparent-finances-(optional-feature)-151427'><strong>Transparency Mode</strong></a> that have opted in to public listing.

- HTTP Method: `GET`
- Endpoint: `/api/v3/organizations`

**Parameters**
| Name | Type| Required | Description |
| :-------- | :----------| :----------:| :----------|
| page | int | ❌ | Returns a list of organizations in <a href='https://changelog.hcb.hackclub.com/transparent-finances-(optional-feature)-151427'><strong>Transparency Mode</strong></a> that have opted in to public listing. |
| per_page | int | ❌ | Returns a list of organizations in <a href='https://changelog.hcb.hackclub.com/transparent-finances-(optional-feature)-151427'><strong>Transparency Mode</strong></a> that have opted in to public listing. |
| offset | int | ❌ | Returns a list of organizations in <a href='https://changelog.hcb.hackclub.com/transparent-finances-(optional-feature)-151427'><strong>Transparency Mode</strong></a> that have opted in to public listing. |
| expand | str | ❌ | Returns a list of organizations in <a href='https://changelog.hcb.hackclub.com/transparent-finances-(optional-feature)-151427'><strong>Transparency Mode</strong></a> that have opted in to public listing. |

**Return Type**

`List[Organization]`

**Example Usage Code Snippet**

```py
from hcb_api import HCB_API, Environment

sdk = HCB_API(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.organizations.list_transparent_organizations(
    page=1,
    per_page=50,
    offset=6,
    expand="expand"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
