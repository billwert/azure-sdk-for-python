# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.databricks import AzureDatabricksManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-databricks
# USAGE
    python workspace_managed_disk_encryption_create.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = AzureDatabricksManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.workspaces.begin_create_or_update(
        resource_group_name="rg",
        workspace_name="myWorkspace",
        parameters={
            "location": "westus",
            "properties": {
                "encryption": {
                    "entities": {
                        "managedDisk": {
                            "keySource": "Microsoft.Keyvault",
                            "keyVaultProperties": {
                                "keyName": "test-cmk-key",
                                "keyVaultUri": "https://test-vault-name.vault.azure.net/",
                                "keyVersion": "00000000000000000000000000000000",
                            },
                            "rotationToLatestKeyVersionEnabled": True,
                        }
                    }
                },
                "managedResourceGroupId": "/subscriptions/subid/resourceGroups/myManagedRG",
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/databricks/resource-manager/Microsoft.Databricks/stable/2023-02-01/examples/WorkspaceManagedDiskEncryptionCreate.json
if __name__ == "__main__":
    main()
