# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer
from .._vendor import RecoveryServicesBackupClientMixinABC, _convert_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_provision_request(
    vault_name: str,
    resource_group_name: str,
    fabric_name: str,
    container_name: str,
    protected_item_name: str,
    recovery_point_id: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-04-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints/{recoveryPointId}/provisionInstantItemRecovery",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "vaultName": _SERIALIZER.url("vault_name", vault_name, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "fabricName": _SERIALIZER.url("fabric_name", fabric_name, "str"),
        "containerName": _SERIALIZER.url("container_name", container_name, "str"),
        "protectedItemName": _SERIALIZER.url("protected_item_name", protected_item_name, "str"),
        "recoveryPointId": _SERIALIZER.url("recovery_point_id", recovery_point_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_revoke_request(
    vault_name: str,
    resource_group_name: str,
    fabric_name: str,
    container_name: str,
    protected_item_name: str,
    recovery_point_id: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-04-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints/{recoveryPointId}/revokeInstantItemRecovery",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "vaultName": _SERIALIZER.url("vault_name", vault_name, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "fabricName": _SERIALIZER.url("fabric_name", fabric_name, "str"),
        "containerName": _SERIALIZER.url("container_name", container_name, "str"),
        "protectedItemName": _SERIALIZER.url("protected_item_name", protected_item_name, "str"),
        "recoveryPointId": _SERIALIZER.url("recovery_point_id", recovery_point_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class ItemLevelRecoveryConnectionsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.recoveryservicesbackup.activestamp.RecoveryServicesBackupClient`'s
        :attr:`item_level_recovery_connections` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def provision(  # pylint: disable=inconsistent-return-statements
        self,
        vault_name: str,
        resource_group_name: str,
        fabric_name: str,
        container_name: str,
        protected_item_name: str,
        recovery_point_id: str,
        parameters: _models.ILRRequestResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """Provisions a script which invokes an iSCSI connection to the backup data. Executing this script
        opens a file
        explorer displaying all the recoverable files and folders. This is an asynchronous operation.
        To know the status of
        provisioning, call GetProtectedItemOperationResult API.

        :param vault_name: The name of the recovery services vault. Required.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present. Required.
        :type resource_group_name: str
        :param fabric_name: Fabric name associated with the backed up items. Required.
        :type fabric_name: str
        :param container_name: Container name associated with the backed up items. Required.
        :type container_name: str
        :param protected_item_name: Backed up item name whose files/folders are to be restored.
         Required.
        :type protected_item_name: str
        :param recovery_point_id: Recovery point ID which represents backed up data. iSCSI connection
         will be provisioned
         for this backed up data. Required.
        :type recovery_point_id: str
        :param parameters: resource ILR request. Required.
        :type parameters: ~azure.mgmt.recoveryservicesbackup.activestamp.models.ILRRequestResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def provision(  # pylint: disable=inconsistent-return-statements
        self,
        vault_name: str,
        resource_group_name: str,
        fabric_name: str,
        container_name: str,
        protected_item_name: str,
        recovery_point_id: str,
        parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """Provisions a script which invokes an iSCSI connection to the backup data. Executing this script
        opens a file
        explorer displaying all the recoverable files and folders. This is an asynchronous operation.
        To know the status of
        provisioning, call GetProtectedItemOperationResult API.

        :param vault_name: The name of the recovery services vault. Required.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present. Required.
        :type resource_group_name: str
        :param fabric_name: Fabric name associated with the backed up items. Required.
        :type fabric_name: str
        :param container_name: Container name associated with the backed up items. Required.
        :type container_name: str
        :param protected_item_name: Backed up item name whose files/folders are to be restored.
         Required.
        :type protected_item_name: str
        :param recovery_point_id: Recovery point ID which represents backed up data. iSCSI connection
         will be provisioned
         for this backed up data. Required.
        :type recovery_point_id: str
        :param parameters: resource ILR request. Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def provision(  # pylint: disable=inconsistent-return-statements
        self,
        vault_name: str,
        resource_group_name: str,
        fabric_name: str,
        container_name: str,
        protected_item_name: str,
        recovery_point_id: str,
        parameters: Union[_models.ILRRequestResource, IO],
        **kwargs: Any
    ) -> None:
        """Provisions a script which invokes an iSCSI connection to the backup data. Executing this script
        opens a file
        explorer displaying all the recoverable files and folders. This is an asynchronous operation.
        To know the status of
        provisioning, call GetProtectedItemOperationResult API.

        :param vault_name: The name of the recovery services vault. Required.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present. Required.
        :type resource_group_name: str
        :param fabric_name: Fabric name associated with the backed up items. Required.
        :type fabric_name: str
        :param container_name: Container name associated with the backed up items. Required.
        :type container_name: str
        :param protected_item_name: Backed up item name whose files/folders are to be restored.
         Required.
        :type protected_item_name: str
        :param recovery_point_id: Recovery point ID which represents backed up data. iSCSI connection
         will be provisioned
         for this backed up data. Required.
        :type recovery_point_id: str
        :param parameters: resource ILR request. Is either a ILRRequestResource type or a IO type.
         Required.
        :type parameters: ~azure.mgmt.recoveryservicesbackup.activestamp.models.ILRRequestResource or
         IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IOBase, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "ILRRequestResource")

        request = build_provision_request(
            vault_name=vault_name,
            resource_group_name=resource_group_name,
            fabric_name=fabric_name,
            container_name=container_name,
            protected_item_name=protected_item_name,
            recovery_point_id=recovery_point_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.provision.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    provision.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints/{recoveryPointId}/provisionInstantItemRecovery"
    }

    @distributed_trace
    def revoke(  # pylint: disable=inconsistent-return-statements
        self,
        vault_name: str,
        resource_group_name: str,
        fabric_name: str,
        container_name: str,
        protected_item_name: str,
        recovery_point_id: str,
        **kwargs: Any
    ) -> None:
        """Revokes an iSCSI connection which can be used to download a script. Executing this script opens
        a file explorer
        displaying all recoverable files and folders. This is an asynchronous operation.

        :param vault_name: The name of the recovery services vault. Required.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the recovery services vault is
         present. Required.
        :type resource_group_name: str
        :param fabric_name: Fabric name associated with the backed up items. Required.
        :type fabric_name: str
        :param container_name: Container name associated with the backed up items. Required.
        :type container_name: str
        :param protected_item_name: Backed up item name whose files/folders are to be restored.
         Required.
        :type protected_item_name: str
        :param recovery_point_id: Recovery point ID which represents backed up data. iSCSI connection
         will be revoked for
         this backed up data. Required.
        :type recovery_point_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_revoke_request(
            vault_name=vault_name,
            resource_group_name=resource_group_name,
            fabric_name=fabric_name,
            container_name=container_name,
            protected_item_name=protected_item_name,
            recovery_point_id=recovery_point_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.revoke.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    revoke.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints/{recoveryPointId}/revokeInstantItemRecovery"
    }
