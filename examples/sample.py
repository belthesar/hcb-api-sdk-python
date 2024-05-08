# This file was generated by liblab | https://liblab.com/

from hcb_api import HcbAPI, Environment

sdk = HcbAPI(access_token="YOUR_ACCESS_TOKEN", base_url=Environment.DEFAULT.value)

result = sdk.organizations.list_transparent_organizations(
    page=1, per_page=50, offset=6, expand="expand"
)

print(result)
