# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, overload
from urllib.parse import parse_qs, urljoin, urlparse

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._trusted_access_role_bindings_operations import (
    build_create_or_update_request,
    build_delete_request,
    build_get_request,
    build_list_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class TrustedAccessRoleBindingsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.containerservice.v2022_08_02_preview.aio.ContainerServiceClient`'s
        :attr:`trusted_access_role_bindings` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(
        self, resource_group_name: str, resource_name: str, **kwargs: Any
    ) -> AsyncIterable["_models.TrustedAccessRoleBinding"]:
        """List trusted access role bindings.

        List trusted access role bindings.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the managed cluster resource. Required.
        :type resource_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either TrustedAccessRoleBinding or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.containerservice.v2022_08_02_preview.models.TrustedAccessRoleBinding]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-08-02-preview"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.TrustedAccessRoleBindingListResult]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    resource_group_name=resource_group_name,
                    resource_name=resource_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urlparse(next_link)
                _next_request_params = case_insensitive_dict(parse_qs(_parsed_next_link.query))
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest("GET", urljoin(next_link, _parsed_next_link.path), params=_next_request_params)
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("TrustedAccessRoleBindingListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName}/trustedAccessRoleBindings"}  # type: ignore

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, resource_name: str, trusted_access_role_binding_name: str, **kwargs: Any
    ) -> _models.TrustedAccessRoleBinding:
        """Get a trusted access role binding.

        Get a trusted access role binding.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the managed cluster resource. Required.
        :type resource_name: str
        :param trusted_access_role_binding_name: The name of trusted access role binding. Required.
        :type trusted_access_role_binding_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TrustedAccessRoleBinding or the result of cls(response)
        :rtype: ~azure.mgmt.containerservice.v2022_08_02_preview.models.TrustedAccessRoleBinding
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-08-02-preview"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.TrustedAccessRoleBinding]

        request = build_get_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            trusted_access_role_binding_name=trusted_access_role_binding_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("TrustedAccessRoleBinding", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName}/trustedAccessRoleBindings/{trustedAccessRoleBindingName}"}  # type: ignore

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        resource_name: str,
        trusted_access_role_binding_name: str,
        trusted_access_role_binding: _models.TrustedAccessRoleBinding,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.TrustedAccessRoleBinding:
        """Create or update a trusted access role binding.

        Create or update a trusted access role binding.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the managed cluster resource. Required.
        :type resource_name: str
        :param trusted_access_role_binding_name: The name of trusted access role binding. Required.
        :type trusted_access_role_binding_name: str
        :param trusted_access_role_binding: A trusted access role binding. Required.
        :type trusted_access_role_binding:
         ~azure.mgmt.containerservice.v2022_08_02_preview.models.TrustedAccessRoleBinding
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TrustedAccessRoleBinding or the result of cls(response)
        :rtype: ~azure.mgmt.containerservice.v2022_08_02_preview.models.TrustedAccessRoleBinding
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        resource_name: str,
        trusted_access_role_binding_name: str,
        trusted_access_role_binding: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.TrustedAccessRoleBinding:
        """Create or update a trusted access role binding.

        Create or update a trusted access role binding.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the managed cluster resource. Required.
        :type resource_name: str
        :param trusted_access_role_binding_name: The name of trusted access role binding. Required.
        :type trusted_access_role_binding_name: str
        :param trusted_access_role_binding: A trusted access role binding. Required.
        :type trusted_access_role_binding: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TrustedAccessRoleBinding or the result of cls(response)
        :rtype: ~azure.mgmt.containerservice.v2022_08_02_preview.models.TrustedAccessRoleBinding
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        resource_name: str,
        trusted_access_role_binding_name: str,
        trusted_access_role_binding: Union[_models.TrustedAccessRoleBinding, IO],
        **kwargs: Any
    ) -> _models.TrustedAccessRoleBinding:
        """Create or update a trusted access role binding.

        Create or update a trusted access role binding.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the managed cluster resource. Required.
        :type resource_name: str
        :param trusted_access_role_binding_name: The name of trusted access role binding. Required.
        :type trusted_access_role_binding_name: str
        :param trusted_access_role_binding: A trusted access role binding. Is either a model type or a
         IO type. Required.
        :type trusted_access_role_binding:
         ~azure.mgmt.containerservice.v2022_08_02_preview.models.TrustedAccessRoleBinding or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TrustedAccessRoleBinding or the result of cls(response)
        :rtype: ~azure.mgmt.containerservice.v2022_08_02_preview.models.TrustedAccessRoleBinding
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-08-02-preview"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.TrustedAccessRoleBinding]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(trusted_access_role_binding, (IO, bytes)):
            _content = trusted_access_role_binding
        else:
            _json = self._serialize.body(trusted_access_role_binding, "TrustedAccessRoleBinding")

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            trusted_access_role_binding_name=trusted_access_role_binding_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_or_update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("TrustedAccessRoleBinding", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName}/trustedAccessRoleBindings/{trustedAccessRoleBindingName}"}  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, resource_name: str, trusted_access_role_binding_name: str, **kwargs: Any
    ) -> None:
        """Delete a trusted access role binding.

        Delete a trusted access role binding.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the managed cluster resource. Required.
        :type resource_name: str
        :param trusted_access_role_binding_name: The name of trusted access role binding. Required.
        :type trusted_access_role_binding_name: str
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-08-02-preview"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_delete_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            trusted_access_role_binding_name=trusted_access_role_binding_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName}/trustedAccessRoleBindings/{trustedAccessRoleBindingName}"}  # type: ignore
