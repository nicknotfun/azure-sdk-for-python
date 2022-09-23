# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._operations import Operations
from ._iot_hub_resource_operations import IotHubResourceOperations
from ._resource_provider_common_operations import ResourceProviderCommonOperations
from ._certificates_operations import CertificatesOperations
from ._iot_hub_operations import IotHubOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "Operations",
    "IotHubResourceOperations",
    "ResourceProviderCommonOperations",
    "CertificatesOperations",
    "IotHubOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
