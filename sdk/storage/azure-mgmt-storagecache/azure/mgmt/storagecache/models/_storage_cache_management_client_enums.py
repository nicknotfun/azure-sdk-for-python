# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AmlFilesystemHealthStateType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """List of AML file system health states."""

    UNAVAILABLE = "Unavailable"
    AVAILABLE = "Available"
    DEGRADED = "Degraded"
    TRANSITIONING = "Transitioning"
    MAINTENANCE = "Maintenance"


class AmlFilesystemIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity used for the resource."""

    USER_ASSIGNED = "UserAssigned"
    NONE = "None"


class AmlFilesystemProvisioningStateType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ARM provisioning state."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CREATING = "Creating"
    DELETING = "Deleting"
    UPDATING = "Updating"
    CANCELED = "Canceled"


class AmlFilesystemSquashMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Squash mode of the AML file system. 'All': User and Group IDs on files will be squashed to the
    provided values for all users on non-trusted systems. 'RootOnly': User and Group IDs on files
    will be squashed to provided values for solely the root user on non-trusted systems. 'None': No
    squashing of User and Group IDs is performed for any users on any systems.
    """

    NONE = "None"
    ROOT_ONLY = "RootOnly"
    ALL = "All"


class ArchiveStatusType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The state of the archive operation."""

    NOT_CONFIGURED = "NotConfigured"
    IDLE = "Idle"
    IN_PROGRESS = "InProgress"
    CANCELED = "Canceled"
    COMPLETED = "Completed"
    FAILED = "Failed"
    CANCELLING = "Cancelling"
    FS_SCAN_IN_PROGRESS = "FSScanInProgress"


class CacheIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity used for the cache."""

    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    NONE = "None"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class DomainJoinedType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """True if the HPC Cache is joined to the Active Directory domain."""

    YES = "Yes"
    NO = "No"
    ERROR = "Error"


class FilesystemSubnetStatusType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of the AML file system subnet check."""

    OK = "Ok"
    INVALID = "Invalid"


class FirmwareStatusType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """True if there is a firmware update ready to install on this cache. The firmware will
    automatically be installed after firmwareUpdateDeadline if not triggered earlier via the
    upgrade operation.
    """

    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"


class HealthStateType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """List of cache health states. Down is when the cluster is not responding.  Degraded is when its
    functioning but has some alerts. Transitioning when it is creating or deleting. Unknown will be
    returned in old api versions when a new value is added in future versions. WaitingForKey is
    when the create is waiting for the system assigned identity to be given access to the
    encryption key in the encryption settings.
    """

    UNKNOWN = "Unknown"
    HEALTHY = "Healthy"
    DEGRADED = "Degraded"
    DOWN = "Down"
    TRANSITIONING = "Transitioning"
    STOPPING = "Stopping"
    STOPPED = "Stopped"
    UPGRADING = "Upgrading"
    FLUSHING = "Flushing"
    WAITING_FOR_KEY = "WaitingForKey"
    START_FAILED = "StartFailed"
    UPGRADE_FAILED = "UpgradeFailed"


class MaintenanceDayOfWeekType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Day of the week on which the maintenance window will occur."""

    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


class MetricAggregationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """MetricAggregationType."""

    NOT_SPECIFIED = "NotSpecified"
    NONE = "None"
    AVERAGE = "Average"
    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"
    TOTAL = "Total"
    COUNT = "Count"


class NfsAccessRuleAccess(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Access allowed by this rule."""

    NO = "no"
    RO = "ro"
    RW = "rw"


class NfsAccessRuleScope(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Scope for this rule. The scope and filter determine which clients match the rule."""

    DEFAULT = "default"
    NETWORK = "network"
    HOST = "host"


class OperationalStateType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Storage target operational state."""

    READY = "Ready"
    BUSY = "Busy"
    SUSPENDED = "Suspended"
    FLUSHING = "Flushing"


class PrimingJobState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The state of the priming operation."""

    QUEUED = "Queued"
    RUNNING = "Running"
    PAUSED = "Paused"
    COMPLETE = "Complete"


class ProvisioningStateType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ARM provisioning state, see
    https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property.
    """

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    CREATING = "Creating"
    DELETING = "Deleting"
    UPDATING = "Updating"


class ReasonCode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The reason for the restriction. As of now this can be "QuotaId" or
    "NotAvailableForSubscription". "QuotaId" is set when the SKU has requiredQuotas parameter as
    the subscription does not belong to that quota. "NotAvailableForSubscription" is related to
    capacity at the datacenter.
    """

    QUOTA_ID = "QuotaId"
    NOT_AVAILABLE_FOR_SUBSCRIPTION = "NotAvailableForSubscription"


class StorageTargetType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the Storage Target."""

    NFS3 = "nfs3"
    CLFS = "clfs"
    UNKNOWN = "unknown"
    BLOB_NFS = "blobNfs"


class UsernameDownloadedType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates whether or not the HPC Cache has performed the username download successfully."""

    YES = "Yes"
    NO = "No"
    ERROR = "Error"


class UsernameSource(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This setting determines how the cache gets username and group names for clients."""

    AD = "AD"
    LDAP = "LDAP"
    FILE = "File"
    NONE = "None"
