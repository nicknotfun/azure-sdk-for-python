# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AbusePenalty
from ._models_py3 import Account
from ._models_py3 import AccountListResult
from ._models_py3 import AccountModel
from ._models_py3 import AccountModelListResult
from ._models_py3 import AccountProperties
from ._models_py3 import AccountSku
from ._models_py3 import AccountSkuListResult
from ._models_py3 import ApiKeys
from ._models_py3 import ApiProperties
from ._models_py3 import AzureEntityResource
from ._models_py3 import CallRateLimit
from ._models_py3 import CapacityConfig
from ._models_py3 import CheckDomainAvailabilityParameter
from ._models_py3 import CheckSkuAvailabilityParameter
from ._models_py3 import CommitmentCost
from ._models_py3 import CommitmentPeriod
from ._models_py3 import CommitmentPlan
from ._models_py3 import CommitmentPlanAccountAssociation
from ._models_py3 import CommitmentPlanAccountAssociationListResult
from ._models_py3 import CommitmentPlanAssociation
from ._models_py3 import CommitmentPlanListResult
from ._models_py3 import CommitmentPlanProperties
from ._models_py3 import CommitmentQuota
from ._models_py3 import CommitmentTier
from ._models_py3 import CommitmentTierListResult
from ._models_py3 import Deployment
from ._models_py3 import DeploymentListResult
from ._models_py3 import DeploymentModel
from ._models_py3 import DeploymentProperties
from ._models_py3 import DeploymentScaleSettings
from ._models_py3 import DomainAvailability
from ._models_py3 import Encryption
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import Identity
from ._models_py3 import IpRule
from ._models_py3 import KeyVaultProperties
from ._models_py3 import MetricName
from ._models_py3 import Model
from ._models_py3 import ModelDeprecationInfo
from ._models_py3 import ModelListResult
from ._models_py3 import ModelSku
from ._models_py3 import MultiRegionSettings
from ._models_py3 import NetworkRuleSet
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import PatchResourceTags
from ._models_py3 import PatchResourceTagsAndSku
from ._models_py3 import PrivateEndpoint
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateEndpointConnectionListResult
from ._models_py3 import PrivateEndpointConnectionProperties
from ._models_py3 import PrivateLinkResource
from ._models_py3 import PrivateLinkResourceListResult
from ._models_py3 import PrivateLinkResourceProperties
from ._models_py3 import PrivateLinkServiceConnectionState
from ._models_py3 import ProxyResource
from ._models_py3 import QuotaLimit
from ._models_py3 import RegenerateKeyParameters
from ._models_py3 import RegionSetting
from ._models_py3 import RequestMatchPattern
from ._models_py3 import Resource
from ._models_py3 import ResourceSku
from ._models_py3 import ResourceSkuListResult
from ._models_py3 import ResourceSkuRestrictionInfo
from ._models_py3 import ResourceSkuRestrictions
from ._models_py3 import Sku
from ._models_py3 import SkuAvailability
from ._models_py3 import SkuAvailabilityListResult
from ._models_py3 import SkuCapability
from ._models_py3 import SkuChangeInfo
from ._models_py3 import SystemData
from ._models_py3 import ThrottlingRule
from ._models_py3 import Usage
from ._models_py3 import UsageListResult
from ._models_py3 import UserAssignedIdentity
from ._models_py3 import UserOwnedStorage
from ._models_py3 import VirtualNetworkRule

from ._cognitive_services_management_client_enums import AbusePenaltyAction
from ._cognitive_services_management_client_enums import ActionType
from ._cognitive_services_management_client_enums import CommitmentPlanProvisioningState
from ._cognitive_services_management_client_enums import CreatedByType
from ._cognitive_services_management_client_enums import DeploymentModelVersionUpgradeOption
from ._cognitive_services_management_client_enums import DeploymentProvisioningState
from ._cognitive_services_management_client_enums import DeploymentScaleType
from ._cognitive_services_management_client_enums import HostingModel
from ._cognitive_services_management_client_enums import KeyName
from ._cognitive_services_management_client_enums import KeySource
from ._cognitive_services_management_client_enums import ModelLifecycleStatus
from ._cognitive_services_management_client_enums import NetworkRuleAction
from ._cognitive_services_management_client_enums import Origin
from ._cognitive_services_management_client_enums import PrivateEndpointConnectionProvisioningState
from ._cognitive_services_management_client_enums import PrivateEndpointServiceConnectionStatus
from ._cognitive_services_management_client_enums import ProvisioningState
from ._cognitive_services_management_client_enums import PublicNetworkAccess
from ._cognitive_services_management_client_enums import QuotaUsageStatus
from ._cognitive_services_management_client_enums import ResourceIdentityType
from ._cognitive_services_management_client_enums import ResourceSkuRestrictionsReasonCode
from ._cognitive_services_management_client_enums import ResourceSkuRestrictionsType
from ._cognitive_services_management_client_enums import RoutingMethods
from ._cognitive_services_management_client_enums import SkuTier
from ._cognitive_services_management_client_enums import UnitType
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AbusePenalty",
    "Account",
    "AccountListResult",
    "AccountModel",
    "AccountModelListResult",
    "AccountProperties",
    "AccountSku",
    "AccountSkuListResult",
    "ApiKeys",
    "ApiProperties",
    "AzureEntityResource",
    "CallRateLimit",
    "CapacityConfig",
    "CheckDomainAvailabilityParameter",
    "CheckSkuAvailabilityParameter",
    "CommitmentCost",
    "CommitmentPeriod",
    "CommitmentPlan",
    "CommitmentPlanAccountAssociation",
    "CommitmentPlanAccountAssociationListResult",
    "CommitmentPlanAssociation",
    "CommitmentPlanListResult",
    "CommitmentPlanProperties",
    "CommitmentQuota",
    "CommitmentTier",
    "CommitmentTierListResult",
    "Deployment",
    "DeploymentListResult",
    "DeploymentModel",
    "DeploymentProperties",
    "DeploymentScaleSettings",
    "DomainAvailability",
    "Encryption",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "Identity",
    "IpRule",
    "KeyVaultProperties",
    "MetricName",
    "Model",
    "ModelDeprecationInfo",
    "ModelListResult",
    "ModelSku",
    "MultiRegionSettings",
    "NetworkRuleSet",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "PatchResourceTags",
    "PatchResourceTagsAndSku",
    "PrivateEndpoint",
    "PrivateEndpointConnection",
    "PrivateEndpointConnectionListResult",
    "PrivateEndpointConnectionProperties",
    "PrivateLinkResource",
    "PrivateLinkResourceListResult",
    "PrivateLinkResourceProperties",
    "PrivateLinkServiceConnectionState",
    "ProxyResource",
    "QuotaLimit",
    "RegenerateKeyParameters",
    "RegionSetting",
    "RequestMatchPattern",
    "Resource",
    "ResourceSku",
    "ResourceSkuListResult",
    "ResourceSkuRestrictionInfo",
    "ResourceSkuRestrictions",
    "Sku",
    "SkuAvailability",
    "SkuAvailabilityListResult",
    "SkuCapability",
    "SkuChangeInfo",
    "SystemData",
    "ThrottlingRule",
    "Usage",
    "UsageListResult",
    "UserAssignedIdentity",
    "UserOwnedStorage",
    "VirtualNetworkRule",
    "AbusePenaltyAction",
    "ActionType",
    "CommitmentPlanProvisioningState",
    "CreatedByType",
    "DeploymentModelVersionUpgradeOption",
    "DeploymentProvisioningState",
    "DeploymentScaleType",
    "HostingModel",
    "KeyName",
    "KeySource",
    "ModelLifecycleStatus",
    "NetworkRuleAction",
    "Origin",
    "PrivateEndpointConnectionProvisioningState",
    "PrivateEndpointServiceConnectionStatus",
    "ProvisioningState",
    "PublicNetworkAccess",
    "QuotaUsageStatus",
    "ResourceIdentityType",
    "ResourceSkuRestrictionsReasonCode",
    "ResourceSkuRestrictionsType",
    "RoutingMethods",
    "SkuTier",
    "UnitType",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
