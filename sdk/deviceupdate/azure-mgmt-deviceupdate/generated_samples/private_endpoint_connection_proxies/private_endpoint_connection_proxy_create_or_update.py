# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.deviceupdate import DeviceUpdateMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-deviceupdate
# USAGE
    python private_endpoint_connection_proxy_create_or_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = DeviceUpdateMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.private_endpoint_connection_proxies.begin_create_or_update(
        resource_group_name="test-rg",
        account_name="contoso",
        private_endpoint_connection_proxy_id="peexample01",
        private_endpoint_connection_proxy={
            "remotePrivateEndpoint": {
                "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/test-rg/providers/Microsoft.Network/privateEndpoints/{peName}",
                "immutableResourceId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/test-rg/providers/Microsoft.Network/privateEndpoints/{peName}",
                "immutableSubscriptionId": "00000000-0000-0000-0000-000000000000",
                "location": "westus2",
                "manualPrivateLinkServiceConnections": [
                    {
                        "groupIds": ["DeviceUpdate"],
                        "name": "{privateEndpointConnectionProxyId}",
                        "requestMessage": "Please approve my connection, thanks.",
                    }
                ],
                "privateLinkServiceProxies": [
                    {
                        "groupConnectivityInformation": [],
                        "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/test-rg/providers/Microsoft.Network/privateEndpoints/{privateEndpointConnectionProxyId}/privateLinkServiceProxies/{privateEndpointConnectionProxyId}",
                    }
                ],
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/deviceupdate/resource-manager/Microsoft.DeviceUpdate/stable/2023-07-01/examples/PrivateEndpointConnectionProxies/PrivateEndpointConnectionProxy_CreateOrUpdate.json
if __name__ == "__main__":
    main()
