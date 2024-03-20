# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AdministratorName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AdministratorName."""

    ACTIVE_DIRECTORY = "ActiveDirectory"


class AdministratorType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the sever administrator."""

    ACTIVE_DIRECTORY = "ActiveDirectory"


class AdvancedThreatProtectionName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AdvancedThreatProtectionName."""

    DEFAULT = "Default"


class AdvancedThreatProtectionProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current provisioning state."""

    SUCCEEDED = "Succeeded"
    UPDATING = "Updating"
    CANCELED = "Canceled"
    FAILED = "Failed"


class AdvancedThreatProtectionState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the state of the Advanced Threat Protection, whether it is enabled or disabled on the
    server.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class BackupFormat(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Backup Format for the current backup. (CollatedFormat is INTERNAL – DO NOT USE)."""

    COLLATED_FORMAT = "CollatedFormat"
    RAW = "Raw"


class BackupType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """BackupType."""

    FULL = "FULL"


class ConfigurationSource(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Source of the configuration."""

    SYSTEM_DEFAULT = "system-default"
    USER_OVERRIDE = "user-override"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class CreateMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The mode to create a new MySQL server."""

    DEFAULT = "Default"
    POINT_IN_TIME_RESTORE = "PointInTimeRestore"
    REPLICA = "Replica"
    GEO_RESTORE = "GeoRestore"


class DataEncryptionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The key type, AzureKeyVault for enable cmk, SystemManaged for disable cmk."""

    AZURE_KEY_VAULT = "AzureKeyVault"
    SYSTEM_MANAGED = "SystemManaged"


class EnableStatusEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum to indicate whether value is 'Enabled' or 'Disabled'."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class HighAvailabilityMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """High availability mode for a server."""

    DISABLED = "Disabled"
    ZONE_REDUNDANT = "ZoneRedundant"
    SAME_ZONE = "SameZone"


class HighAvailabilityState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The state of server high availability."""

    NOT_ENABLED = "NotEnabled"
    CREATING_STANDBY = "CreatingStandby"
    HEALTHY = "Healthy"
    FAILING_OVER = "FailingOver"
    REMOVING_STANDBY = "RemovingStandby"


class ImportSourceStorageType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Storage type of import source."""

    AZURE_BLOB = "AzureBlob"


class IsConfigPendingRestart(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """If is the configuration pending restart or not."""

    TRUE = "True"
    FALSE = "False"


class IsDynamicConfig(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """If is the configuration dynamic."""

    TRUE = "True"
    FALSE = "False"


class IsReadOnly(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """If is the configuration read only."""

    TRUE = "True"
    FALSE = "False"


class MaintenanceProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current provisioning state."""

    SUCCEEDED = "Succeeded"
    CREATING = "Creating"
    DELETING = "Deleting"
    FAILED = "Failed"


class MaintenanceState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current status of this maintenance."""

    SCHEDULED = "Scheduled"
    RE_SCHEDULED = "ReScheduled"
    IN_PREPARATION = "InPreparation"
    PROCESSING = "Processing"
    COMPLETED = "Completed"
    CANCELED = "Canceled"


class MaintenanceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of this maintenance."""

    ROUTINE_MAINTENANCE = "RoutineMaintenance"
    MINOR_VERSION_UPGRADE = "MinorVersionUpgrade"
    SECURITY_PATCHES = "SecurityPatches"
    HOT_FIXES = "HotFixes"


class ManagedServiceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of managed service identity."""

    USER_ASSIGNED = "UserAssigned"


class ObjectType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Identifies the type of source operation."""

    BACKUP_AND_EXPORT_RESPONSE = "BackupAndExportResponse"
    IMPORT_FROM_STORAGE_RESPONSE = "ImportFromStorageResponse"


class OperationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The operation status."""

    PENDING = "Pending"
    """The operation has been accepted but hasn't started."""
    IN_PROGRESS = "InProgress"
    """The operation is running"""
    SUCCEEDED = "Succeeded"
    """The operation Succeeded"""
    FAILED = "Failed"
    """The operation Failed"""
    CANCEL_IN_PROGRESS = "CancelInProgress"
    """The cancellation in progress"""
    CANCELED = "Canceled"
    """The operation has been Canceled"""


class PrivateEndpointConnectionProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current provisioning state."""

    SUCCEEDED = "Succeeded"
    CREATING = "Creating"
    DELETING = "Deleting"
    FAILED = "Failed"


class PrivateEndpointServiceConnectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The private endpoint connection status."""

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current provisioning state."""

    SUCCEEDED = "Succeeded"
    CREATING = "Creating"
    DELETING = "Deleting"
    FAILED = "Failed"
    CANCELED = "Canceled"


class ReplicationRole(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The replication role."""

    NONE = "None"
    SOURCE = "Source"
    REPLICA = "Replica"


class ResetAllToDefault(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether to reset all server parameters to default."""

    TRUE = "True"
    FALSE = "False"


class ServerSkuTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The tier of the particular SKU, e.g. GeneralPurpose."""

    BURSTABLE = "Burstable"
    GENERAL_PURPOSE = "GeneralPurpose"
    MEMORY_OPTIMIZED = "MemoryOptimized"


class ServerState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The state of a server."""

    READY = "Ready"
    DROPPING = "Dropping"
    DISABLED = "Disabled"
    STARTING = "Starting"
    STOPPING = "Stopping"
    STOPPED = "Stopped"
    UPDATING = "Updating"


class ServerVersion(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The version of a server."""

    FIVE7 = "5.7"
    EIGHT0_21 = "8.0.21"
