# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.streamanalytics import StreamAnalyticsManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-streamanalytics
# USAGE
    python output_create_blob_csv.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = StreamAnalyticsManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="56b5e0a9-b645-407d-99b0-c64f86013e3d",
    )

    response = client.outputs.create_or_replace(
        resource_group_name="sjrg5023",
        job_name="sj900",
        output_name="output1623",
        output={
            "properties": {
                "datasource": {
                    "properties": {
                        "blobPathPrefix": "my/path",
                        "blobWriteMode": "Once",
                        "container": "state",
                        "dateFormat": "yyyy/MM/dd",
                        "pathPattern": "{date}/{time}",
                        "storageAccounts": [{"accountKey": "accountKey==", "accountName": "someAccountName"}],
                        "timeFormat": "HH",
                    },
                    "type": "Microsoft.Storage/Blob",
                },
                "serialization": {"properties": {"encoding": "UTF8", "fieldDelimiter": ","}, "type": "Csv"},
            }
        },
    )
    print(response)


# x-ms-original-file: specification/streamanalytics/resource-manager/Microsoft.StreamAnalytics/preview/2021-10-01-preview/examples/Output_Create_Blob_CSV.json
if __name__ == "__main__":
    main()
