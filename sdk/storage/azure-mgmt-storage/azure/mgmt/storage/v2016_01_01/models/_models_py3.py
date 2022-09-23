# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional, TYPE_CHECKING, Union

import msrest.serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    import __init__ as _models


class CheckNameAvailabilityResult(msrest.serialization.Model):
    """The CheckNameAvailability operation response.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name_available: Gets a boolean value that indicates whether the name is available for you
     to use. If true, the name is available. If false, the name has already been taken or is invalid
     and cannot be used.
    :vartype name_available: bool
    :ivar reason: Gets the reason that a storage account name could not be used. The Reason element
     is only returned if NameAvailable is false. Known values are: "AccountNameInvalid",
     "AlreadyExists".
    :vartype reason: str or ~azure.mgmt.storage.v2016_01_01.models.Reason
    :ivar message: Gets an error message explaining the Reason value in more detail.
    :vartype message: str
    """

    _validation = {
        'name_available': {'readonly': True},
        'reason': {'readonly': True},
        'message': {'readonly': True},
    }

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(CheckNameAvailabilityResult, self).__init__(**kwargs)
        self.name_available = None
        self.reason = None
        self.message = None


class CustomDomain(msrest.serialization.Model):
    """The custom domain assigned to this storage account. This can be set via Update.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required. Gets or sets the custom domain name assigned to the storage account. Name
     is the CNAME source.
    :vartype name: str
    :ivar use_sub_domain_name: Indicates whether indirect CName validation is enabled. Default
     value is false. This should only be set on updates.
    :vartype use_sub_domain_name: bool
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'use_sub_domain_name': {'key': 'useSubDomainName', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        name: str,
        use_sub_domain_name: Optional[bool] = None,
        **kwargs
    ):
        """
        :keyword name: Required. Gets or sets the custom domain name assigned to the storage account.
         Name is the CNAME source.
        :paramtype name: str
        :keyword use_sub_domain_name: Indicates whether indirect CName validation is enabled. Default
         value is false. This should only be set on updates.
        :paramtype use_sub_domain_name: bool
        """
        super(CustomDomain, self).__init__(**kwargs)
        self.name = name
        self.use_sub_domain_name = use_sub_domain_name


class Encryption(msrest.serialization.Model):
    """The encryption settings on the storage account.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar services: List of services which support encryption.
    :vartype services: ~azure.mgmt.storage.v2016_01_01.models.EncryptionServices
    :ivar key_source: The encryption keySource (provider). Possible values (case-insensitive):
     Microsoft.Storage. Has constant value: "Microsoft.Storage".
    :vartype key_source: str
    """

    _validation = {
        'key_source': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'services': {'key': 'services', 'type': 'EncryptionServices'},
        'key_source': {'key': 'keySource', 'type': 'str'},
    }

    key_source = "Microsoft.Storage"

    def __init__(
        self,
        *,
        services: Optional["_models.EncryptionServices"] = None,
        **kwargs
    ):
        """
        :keyword services: List of services which support encryption.
        :paramtype services: ~azure.mgmt.storage.v2016_01_01.models.EncryptionServices
        """
        super(Encryption, self).__init__(**kwargs)
        self.services = services


class EncryptionService(msrest.serialization.Model):
    """A service that allows server-side encryption to be used.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar enabled: A boolean indicating whether or not the service encrypts the data as it is
     stored.
    :vartype enabled: bool
    :ivar last_enabled_time: Gets a rough estimate of the date/time when the encryption was last
     enabled by the user. Only returned when encryption is enabled. There might be some unencrypted
     blobs which were written after this time, as it is just a rough estimate.
    :vartype last_enabled_time: ~datetime.datetime
    """

    _validation = {
        'last_enabled_time': {'readonly': True},
    }

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'last_enabled_time': {'key': 'lastEnabledTime', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        *,
        enabled: Optional[bool] = None,
        **kwargs
    ):
        """
        :keyword enabled: A boolean indicating whether or not the service encrypts the data as it is
         stored.
        :paramtype enabled: bool
        """
        super(EncryptionService, self).__init__(**kwargs)
        self.enabled = enabled
        self.last_enabled_time = None


class EncryptionServices(msrest.serialization.Model):
    """A list of services that support encryption.

    :ivar blob: The encryption function of the blob storage service.
    :vartype blob: ~azure.mgmt.storage.v2016_01_01.models.EncryptionService
    """

    _attribute_map = {
        'blob': {'key': 'blob', 'type': 'EncryptionService'},
    }

    def __init__(
        self,
        *,
        blob: Optional["_models.EncryptionService"] = None,
        **kwargs
    ):
        """
        :keyword blob: The encryption function of the blob storage service.
        :paramtype blob: ~azure.mgmt.storage.v2016_01_01.models.EncryptionService
        """
        super(EncryptionServices, self).__init__(**kwargs)
        self.blob = blob


class Endpoints(msrest.serialization.Model):
    """The URIs that are used to perform a retrieval of a public blob, queue, or table object.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar blob: Gets the blob endpoint.
    :vartype blob: str
    :ivar queue: Gets the queue endpoint.
    :vartype queue: str
    :ivar table: Gets the table endpoint.
    :vartype table: str
    :ivar file: Gets the file endpoint.
    :vartype file: str
    """

    _validation = {
        'blob': {'readonly': True},
        'queue': {'readonly': True},
        'table': {'readonly': True},
        'file': {'readonly': True},
    }

    _attribute_map = {
        'blob': {'key': 'blob', 'type': 'str'},
        'queue': {'key': 'queue', 'type': 'str'},
        'table': {'key': 'table', 'type': 'str'},
        'file': {'key': 'file', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(Endpoints, self).__init__(**kwargs)
        self.blob = None
        self.queue = None
        self.table = None
        self.file = None


class Resource(msrest.serialization.Model):
    """Resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar location: Resource location.
    :vartype location: str
    :ivar tags: A set of tags. Tags assigned to a resource; can be used for viewing and grouping a
     resource (across resource groups).
    :vartype tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        location: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        """
        :keyword location: Resource location.
        :paramtype location: str
        :keyword tags: A set of tags. Tags assigned to a resource; can be used for viewing and grouping
         a resource (across resource groups).
        :paramtype tags: dict[str, str]
        """
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags


class Sku(msrest.serialization.Model):
    """The SKU of the storage account.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required. Gets or sets the sku name. Required for account creation; optional for
     update. Note that in older versions, sku name was called accountType. Known values are:
     "Standard_LRS", "Standard_GRS", "Standard_RAGRS", "Standard_ZRS", "Premium_LRS".
    :vartype name: str or ~azure.mgmt.storage.v2016_01_01.models.SkuName
    :ivar tier: Gets the sku tier. This is based on the SKU name. Known values are: "Standard",
     "Premium".
    :vartype tier: str or ~azure.mgmt.storage.v2016_01_01.models.SkuTier
    """

    _validation = {
        'name': {'required': True},
        'tier': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Union[str, "_models.SkuName"],
        **kwargs
    ):
        """
        :keyword name: Required. Gets or sets the sku name. Required for account creation; optional for
         update. Note that in older versions, sku name was called accountType. Known values are:
         "Standard_LRS", "Standard_GRS", "Standard_RAGRS", "Standard_ZRS", "Premium_LRS".
        :paramtype name: str or ~azure.mgmt.storage.v2016_01_01.models.SkuName
        """
        super(Sku, self).__init__(**kwargs)
        self.name = name
        self.tier = None


class StorageAccount(Resource):
    """The storage account.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar location: Resource location.
    :vartype location: str
    :ivar tags: A set of tags. Tags assigned to a resource; can be used for viewing and grouping a
     resource (across resource groups).
    :vartype tags: dict[str, str]
    :ivar sku: Gets the SKU.
    :vartype sku: ~azure.mgmt.storage.v2016_01_01.models.Sku
    :ivar kind: Gets the Kind. Known values are: "Storage", "BlobStorage".
    :vartype kind: str or ~azure.mgmt.storage.v2016_01_01.models.Kind
    :ivar provisioning_state: Gets the status of the storage account at the time the operation was
     called. Known values are: "Creating", "ResolvingDNS", "Succeeded".
    :vartype provisioning_state: str or ~azure.mgmt.storage.v2016_01_01.models.ProvisioningState
    :ivar primary_endpoints: Gets the URLs that are used to perform a retrieval of a public blob,
     queue, or table object. Note that Standard_ZRS and Premium_LRS accounts only return the blob
     endpoint.
    :vartype primary_endpoints: ~azure.mgmt.storage.v2016_01_01.models.Endpoints
    :ivar primary_location: Gets the location of the primary data center for the storage account.
    :vartype primary_location: str
    :ivar status_of_primary: Gets the status indicating whether the primary location of the storage
     account is available or unavailable. Known values are: "Available", "Unavailable".
    :vartype status_of_primary: str or ~azure.mgmt.storage.v2016_01_01.models.AccountStatus
    :ivar last_geo_failover_time: Gets the timestamp of the most recent instance of a failover to
     the secondary location. Only the most recent timestamp is retained. This element is not
     returned if there has never been a failover instance. Only available if the accountType is
     Standard_GRS or Standard_RAGRS.
    :vartype last_geo_failover_time: ~datetime.datetime
    :ivar secondary_location: Gets the location of the geo-replicated secondary for the storage
     account. Only available if the accountType is Standard_GRS or Standard_RAGRS.
    :vartype secondary_location: str
    :ivar status_of_secondary: Gets the status indicating whether the secondary location of the
     storage account is available or unavailable. Only available if the SKU name is Standard_GRS or
     Standard_RAGRS. Known values are: "Available", "Unavailable".
    :vartype status_of_secondary: str or ~azure.mgmt.storage.v2016_01_01.models.AccountStatus
    :ivar creation_time: Gets the creation date and time of the storage account in UTC.
    :vartype creation_time: ~datetime.datetime
    :ivar custom_domain: Gets the custom domain the user assigned to this storage account.
    :vartype custom_domain: ~azure.mgmt.storage.v2016_01_01.models.CustomDomain
    :ivar secondary_endpoints: Gets the URLs that are used to perform a retrieval of a public blob,
     queue, or table object from the secondary location of the storage account. Only available if
     the SKU name is Standard_RAGRS.
    :vartype secondary_endpoints: ~azure.mgmt.storage.v2016_01_01.models.Endpoints
    :ivar encryption: Gets the encryption settings on the account. If unspecified, the account is
     unencrypted.
    :vartype encryption: ~azure.mgmt.storage.v2016_01_01.models.Encryption
    :ivar access_tier: Required for storage accounts where kind = BlobStorage. The access tier used
     for billing. Known values are: "Hot", "Cool".
    :vartype access_tier: str or ~azure.mgmt.storage.v2016_01_01.models.AccessTier
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'sku': {'readonly': True},
        'kind': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'primary_endpoints': {'readonly': True},
        'primary_location': {'readonly': True},
        'status_of_primary': {'readonly': True},
        'last_geo_failover_time': {'readonly': True},
        'secondary_location': {'readonly': True},
        'status_of_secondary': {'readonly': True},
        'creation_time': {'readonly': True},
        'custom_domain': {'readonly': True},
        'secondary_endpoints': {'readonly': True},
        'encryption': {'readonly': True},
        'access_tier': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'kind': {'key': 'kind', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'primary_endpoints': {'key': 'properties.primaryEndpoints', 'type': 'Endpoints'},
        'primary_location': {'key': 'properties.primaryLocation', 'type': 'str'},
        'status_of_primary': {'key': 'properties.statusOfPrimary', 'type': 'str'},
        'last_geo_failover_time': {'key': 'properties.lastGeoFailoverTime', 'type': 'iso-8601'},
        'secondary_location': {'key': 'properties.secondaryLocation', 'type': 'str'},
        'status_of_secondary': {'key': 'properties.statusOfSecondary', 'type': 'str'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'custom_domain': {'key': 'properties.customDomain', 'type': 'CustomDomain'},
        'secondary_endpoints': {'key': 'properties.secondaryEndpoints', 'type': 'Endpoints'},
        'encryption': {'key': 'properties.encryption', 'type': 'Encryption'},
        'access_tier': {'key': 'properties.accessTier', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        """
        :keyword location: Resource location.
        :paramtype location: str
        :keyword tags: A set of tags. Tags assigned to a resource; can be used for viewing and grouping
         a resource (across resource groups).
        :paramtype tags: dict[str, str]
        """
        super(StorageAccount, self).__init__(location=location, tags=tags, **kwargs)
        self.sku = None
        self.kind = None
        self.provisioning_state = None
        self.primary_endpoints = None
        self.primary_location = None
        self.status_of_primary = None
        self.last_geo_failover_time = None
        self.secondary_location = None
        self.status_of_secondary = None
        self.creation_time = None
        self.custom_domain = None
        self.secondary_endpoints = None
        self.encryption = None
        self.access_tier = None


class StorageAccountCheckNameAvailabilityParameters(msrest.serialization.Model):
    """StorageAccountCheckNameAvailabilityParameters.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required.
    :vartype name: str
    :ivar type:  Has constant value: "Microsoft.Storage/storageAccounts".
    :vartype type: str
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    type = "Microsoft.Storage/storageAccounts"

    def __init__(
        self,
        *,
        name: str,
        **kwargs
    ):
        """
        :keyword name: Required.
        :paramtype name: str
        """
        super(StorageAccountCheckNameAvailabilityParameters, self).__init__(**kwargs)
        self.name = name


class StorageAccountCreateParameters(msrest.serialization.Model):
    """The parameters used when creating a storage account.

    All required parameters must be populated in order to send to Azure.

    :ivar sku: Required. Required. Gets or sets the sku name.
    :vartype sku: ~azure.mgmt.storage.v2016_01_01.models.Sku
    :ivar kind: Required. Required. Indicates the type of storage account. Known values are:
     "Storage", "BlobStorage".
    :vartype kind: str or ~azure.mgmt.storage.v2016_01_01.models.Kind
    :ivar location: Required. Required. Gets or sets the location of the resource. This will be one
     of the supported and registered Azure Geo Regions (e.g. West US, East US, Southeast Asia,
     etc.). The geo region of a resource cannot be changed once it is created, but if an identical
     geo region is specified on update, the request will succeed.
    :vartype location: str
    :ivar tags: A set of tags. Gets or sets a list of key value pairs that describe the resource.
     These tags can be used for viewing and grouping this resource (across resource groups). A
     maximum of 15 tags can be provided for a resource. Each tag must have a key with a length no
     greater than 128 characters and a value with a length no greater than 256 characters.
    :vartype tags: dict[str, str]
    :ivar custom_domain: User domain assigned to the storage account. Name is the CNAME source.
     Only one custom domain is supported per storage account at this time. To clear the existing
     custom domain, use an empty string for the custom domain name property.
    :vartype custom_domain: ~azure.mgmt.storage.v2016_01_01.models.CustomDomain
    :ivar encryption: Provides the encryption settings on the account. If left unspecified the
     account encryption settings will remain the same. The default setting is unencrypted.
    :vartype encryption: ~azure.mgmt.storage.v2016_01_01.models.Encryption
    :ivar access_tier: Required for storage accounts where kind = BlobStorage. The access tier used
     for billing. Known values are: "Hot", "Cool".
    :vartype access_tier: str or ~azure.mgmt.storage.v2016_01_01.models.AccessTier
    """

    _validation = {
        'sku': {'required': True},
        'kind': {'required': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'sku': {'key': 'sku', 'type': 'Sku'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'custom_domain': {'key': 'properties.customDomain', 'type': 'CustomDomain'},
        'encryption': {'key': 'properties.encryption', 'type': 'Encryption'},
        'access_tier': {'key': 'properties.accessTier', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        sku: "_models.Sku",
        kind: Union[str, "_models.Kind"],
        location: str,
        tags: Optional[Dict[str, str]] = None,
        custom_domain: Optional["_models.CustomDomain"] = None,
        encryption: Optional["_models.Encryption"] = None,
        access_tier: Optional[Union[str, "_models.AccessTier"]] = None,
        **kwargs
    ):
        """
        :keyword sku: Required. Required. Gets or sets the sku name.
        :paramtype sku: ~azure.mgmt.storage.v2016_01_01.models.Sku
        :keyword kind: Required. Required. Indicates the type of storage account. Known values are:
         "Storage", "BlobStorage".
        :paramtype kind: str or ~azure.mgmt.storage.v2016_01_01.models.Kind
        :keyword location: Required. Required. Gets or sets the location of the resource. This will be
         one of the supported and registered Azure Geo Regions (e.g. West US, East US, Southeast Asia,
         etc.). The geo region of a resource cannot be changed once it is created, but if an identical
         geo region is specified on update, the request will succeed.
        :paramtype location: str
        :keyword tags: A set of tags. Gets or sets a list of key value pairs that describe the
         resource. These tags can be used for viewing and grouping this resource (across resource
         groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key with a
         length no greater than 128 characters and a value with a length no greater than 256 characters.
        :paramtype tags: dict[str, str]
        :keyword custom_domain: User domain assigned to the storage account. Name is the CNAME source.
         Only one custom domain is supported per storage account at this time. To clear the existing
         custom domain, use an empty string for the custom domain name property.
        :paramtype custom_domain: ~azure.mgmt.storage.v2016_01_01.models.CustomDomain
        :keyword encryption: Provides the encryption settings on the account. If left unspecified the
         account encryption settings will remain the same. The default setting is unencrypted.
        :paramtype encryption: ~azure.mgmt.storage.v2016_01_01.models.Encryption
        :keyword access_tier: Required for storage accounts where kind = BlobStorage. The access tier
         used for billing. Known values are: "Hot", "Cool".
        :paramtype access_tier: str or ~azure.mgmt.storage.v2016_01_01.models.AccessTier
        """
        super(StorageAccountCreateParameters, self).__init__(**kwargs)
        self.sku = sku
        self.kind = kind
        self.location = location
        self.tags = tags
        self.custom_domain = custom_domain
        self.encryption = encryption
        self.access_tier = access_tier


class StorageAccountKey(msrest.serialization.Model):
    """An access key for the storage account.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar key_name: Name of the key.
    :vartype key_name: str
    :ivar value: Base 64-encoded value of the key.
    :vartype value: str
    :ivar permissions: Permissions for the key -- read-only or full permissions. Known values are:
     "READ", "FULL".
    :vartype permissions: str or ~azure.mgmt.storage.v2016_01_01.models.KeyPermission
    """

    _validation = {
        'key_name': {'readonly': True},
        'value': {'readonly': True},
        'permissions': {'readonly': True},
    }

    _attribute_map = {
        'key_name': {'key': 'keyName', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'permissions': {'key': 'permissions', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(StorageAccountKey, self).__init__(**kwargs)
        self.key_name = None
        self.value = None
        self.permissions = None


class StorageAccountListKeysResult(msrest.serialization.Model):
    """The response from the ListKeys operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar keys: Gets the list of storage account keys and their properties for the specified
     storage account.
    :vartype keys: list[~azure.mgmt.storage.v2016_01_01.models.StorageAccountKey]
    """

    _validation = {
        'keys': {'readonly': True},
    }

    _attribute_map = {
        'keys': {'key': 'keys', 'type': '[StorageAccountKey]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(StorageAccountListKeysResult, self).__init__(**kwargs)
        self.keys = None


class StorageAccountListResult(msrest.serialization.Model):
    """The response from the List Storage Accounts operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: Gets the list of storage accounts and their properties.
    :vartype value: list[~azure.mgmt.storage.v2016_01_01.models.StorageAccount]
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[StorageAccount]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(StorageAccountListResult, self).__init__(**kwargs)
        self.value = None


class StorageAccountRegenerateKeyParameters(msrest.serialization.Model):
    """StorageAccountRegenerateKeyParameters.

    All required parameters must be populated in order to send to Azure.

    :ivar key_name: Required.
    :vartype key_name: str
    """

    _validation = {
        'key_name': {'required': True},
    }

    _attribute_map = {
        'key_name': {'key': 'keyName', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        key_name: str,
        **kwargs
    ):
        """
        :keyword key_name: Required.
        :paramtype key_name: str
        """
        super(StorageAccountRegenerateKeyParameters, self).__init__(**kwargs)
        self.key_name = key_name


class StorageAccountUpdateParameters(msrest.serialization.Model):
    """The parameters that can be provided when updating the storage account properties.

    :ivar sku: Gets or sets the SKU name. Note that the SKU name cannot be updated to Standard_ZRS
     or Premium_LRS, nor can accounts of those sku names be updated to any other value.
    :vartype sku: ~azure.mgmt.storage.v2016_01_01.models.Sku
    :ivar tags: A set of tags. Gets or sets a list of key value pairs that describe the resource.
     These tags can be used in viewing and grouping this resource (across resource groups). A
     maximum of 15 tags can be provided for a resource. Each tag must have a key no greater in
     length than 128 characters and a value no greater in length than 256 characters.
    :vartype tags: dict[str, str]
    :ivar custom_domain: Custom domain assigned to the storage account by the user. Name is the
     CNAME source. Only one custom domain is supported per storage account at this time. To clear
     the existing custom domain, use an empty string for the custom domain name property.
    :vartype custom_domain: ~azure.mgmt.storage.v2016_01_01.models.CustomDomain
    :ivar encryption: Provides the encryption settings on the account. The default setting is
     unencrypted.
    :vartype encryption: ~azure.mgmt.storage.v2016_01_01.models.Encryption
    :ivar access_tier: Required for storage accounts where kind = BlobStorage. The access tier used
     for billing. Known values are: "Hot", "Cool".
    :vartype access_tier: str or ~azure.mgmt.storage.v2016_01_01.models.AccessTier
    """

    _attribute_map = {
        'sku': {'key': 'sku', 'type': 'Sku'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'custom_domain': {'key': 'properties.customDomain', 'type': 'CustomDomain'},
        'encryption': {'key': 'properties.encryption', 'type': 'Encryption'},
        'access_tier': {'key': 'properties.accessTier', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        sku: Optional["_models.Sku"] = None,
        tags: Optional[Dict[str, str]] = None,
        custom_domain: Optional["_models.CustomDomain"] = None,
        encryption: Optional["_models.Encryption"] = None,
        access_tier: Optional[Union[str, "_models.AccessTier"]] = None,
        **kwargs
    ):
        """
        :keyword sku: Gets or sets the SKU name. Note that the SKU name cannot be updated to
         Standard_ZRS or Premium_LRS, nor can accounts of those sku names be updated to any other value.
        :paramtype sku: ~azure.mgmt.storage.v2016_01_01.models.Sku
        :keyword tags: A set of tags. Gets or sets a list of key value pairs that describe the
         resource. These tags can be used in viewing and grouping this resource (across resource
         groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no
         greater in length than 128 characters and a value no greater in length than 256 characters.
        :paramtype tags: dict[str, str]
        :keyword custom_domain: Custom domain assigned to the storage account by the user. Name is the
         CNAME source. Only one custom domain is supported per storage account at this time. To clear
         the existing custom domain, use an empty string for the custom domain name property.
        :paramtype custom_domain: ~azure.mgmt.storage.v2016_01_01.models.CustomDomain
        :keyword encryption: Provides the encryption settings on the account. The default setting is
         unencrypted.
        :paramtype encryption: ~azure.mgmt.storage.v2016_01_01.models.Encryption
        :keyword access_tier: Required for storage accounts where kind = BlobStorage. The access tier
         used for billing. Known values are: "Hot", "Cool".
        :paramtype access_tier: str or ~azure.mgmt.storage.v2016_01_01.models.AccessTier
        """
        super(StorageAccountUpdateParameters, self).__init__(**kwargs)
        self.sku = sku
        self.tags = tags
        self.custom_domain = custom_domain
        self.encryption = encryption
        self.access_tier = access_tier


class Usage(msrest.serialization.Model):
    """Describes Storage Resource Usage.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar unit: Gets the unit of measurement. Known values are: "Count", "Bytes", "Seconds",
     "Percent", "CountsPerSecond", "BytesPerSecond".
    :vartype unit: str or ~azure.mgmt.storage.v2016_01_01.models.UsageUnit
    :ivar current_value: Gets the current count of the allocated resources in the subscription.
    :vartype current_value: int
    :ivar limit: Gets the maximum count of the resources that can be allocated in the subscription.
    :vartype limit: int
    :ivar name: Gets the name of the type of usage.
    :vartype name: ~azure.mgmt.storage.v2016_01_01.models.UsageName
    """

    _validation = {
        'unit': {'readonly': True},
        'current_value': {'readonly': True},
        'limit': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'unit': {'key': 'unit', 'type': 'str'},
        'current_value': {'key': 'currentValue', 'type': 'int'},
        'limit': {'key': 'limit', 'type': 'int'},
        'name': {'key': 'name', 'type': 'UsageName'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(Usage, self).__init__(**kwargs)
        self.unit = None
        self.current_value = None
        self.limit = None
        self.name = None


class UsageListResult(msrest.serialization.Model):
    """The response from the List Usages operation.

    :ivar value: Gets or sets the list of Storage Resource Usages.
    :vartype value: list[~azure.mgmt.storage.v2016_01_01.models.Usage]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Usage]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["_models.Usage"]] = None,
        **kwargs
    ):
        """
        :keyword value: Gets or sets the list of Storage Resource Usages.
        :paramtype value: list[~azure.mgmt.storage.v2016_01_01.models.Usage]
        """
        super(UsageListResult, self).__init__(**kwargs)
        self.value = value


class UsageName(msrest.serialization.Model):
    """The usage names that can be used; currently limited to StorageAccount.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: Gets a string describing the resource name.
    :vartype value: str
    :ivar localized_value: Gets a localized string describing the resource name.
    :vartype localized_value: str
    """

    _validation = {
        'value': {'readonly': True},
        'localized_value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'localized_value': {'key': 'localizedValue', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(UsageName, self).__init__(**kwargs)
        self.value = None
        self.localized_value = None
