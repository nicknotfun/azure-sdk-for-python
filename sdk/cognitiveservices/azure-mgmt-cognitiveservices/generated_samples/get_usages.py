# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.cognitiveservices import CognitiveServicesManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-cognitiveservices
# USAGE
    python get_usages.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = CognitiveServicesManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="5a4f5c2e-6983-4ccb-bd34-2196d5b5bbd3",
    )

    response = client.accounts.list_usages(
        resource_group_name="myResourceGroup",
        account_name="TestUsage02",
    )
    print(response)


# x-ms-original-file: specification/cognitiveservices/resource-manager/Microsoft.CognitiveServices/stable/2023-05-01/examples/GetUsages.json
if __name__ == "__main__":
    main()
