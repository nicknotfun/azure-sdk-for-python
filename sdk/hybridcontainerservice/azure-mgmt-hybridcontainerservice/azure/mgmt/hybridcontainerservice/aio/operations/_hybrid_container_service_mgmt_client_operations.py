# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload

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
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._hybrid_container_service_mgmt_client_operations import (
    build_delete_kubernetes_versions_request,
    build_delete_vm_skus_request,
    build_get_kubernetes_versions_request,
    build_get_vm_skus_request,
    build_put_kubernetes_versions_request,
    build_put_vm_skus_request,
)
from .._vendor import HybridContainerServiceMgmtClientMixinABC

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class HybridContainerServiceMgmtClientOperationsMixin(HybridContainerServiceMgmtClientMixinABC):
    @distributed_trace_async
    async def get_kubernetes_versions(
        self, custom_location_resource_uri: str, **kwargs: Any
    ) -> _models.KubernetesVersionProfile:
        """Gets the supported kubernetes versions.

        Gets the supported kubernetes versions from the underlying custom location.

        :param custom_location_resource_uri: The fully qualified Azure Resource manager identifier of
         the custom location resource. Required.
        :type custom_location_resource_uri: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: KubernetesVersionProfile or the result of cls(response)
        :rtype: ~azure.mgmt.hybridcontainerservice.models.KubernetesVersionProfile
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
        cls: ClsType[_models.KubernetesVersionProfile] = kwargs.pop("cls", None)

        request = build_get_kubernetes_versions_request(
            custom_location_resource_uri=custom_location_resource_uri,
            api_version=api_version,
            template_url=self.get_kubernetes_versions.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("KubernetesVersionProfile", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_kubernetes_versions.metadata = {
        "url": "/{customLocationResourceUri}/providers/Microsoft.HybridContainerService/kubernetesVersions/default"
    }

    async def _put_kubernetes_versions_initial(
        self,
        custom_location_resource_uri: str,
        kubernetes_versions: Union[_models.KubernetesVersionProfile, IO],
        **kwargs: Any
    ) -> _models.KubernetesVersionProfile:
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
        cls: ClsType[_models.KubernetesVersionProfile] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(kubernetes_versions, (IOBase, bytes)):
            _content = kubernetes_versions
        else:
            _json = self._serialize.body(kubernetes_versions, "KubernetesVersionProfile")

        request = build_put_kubernetes_versions_request(
            custom_location_resource_uri=custom_location_resource_uri,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self._put_kubernetes_versions_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("KubernetesVersionProfile", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("KubernetesVersionProfile", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    _put_kubernetes_versions_initial.metadata = {
        "url": "/{customLocationResourceUri}/providers/Microsoft.HybridContainerService/kubernetesVersions/default"
    }

    @overload
    async def begin_put_kubernetes_versions(
        self,
        custom_location_resource_uri: str,
        kubernetes_versions: _models.KubernetesVersionProfile,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.KubernetesVersionProfile]:
        """Puts the kubernetes version.

        Puts the kubernetes version resource type.

        :param custom_location_resource_uri: The fully qualified Azure Resource manager identifier of
         the custom location resource. Required.
        :type custom_location_resource_uri: str
        :param kubernetes_versions: Kubernetes Versions resource definition. Required.
        :type kubernetes_versions: ~azure.mgmt.hybridcontainerservice.models.KubernetesVersionProfile
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either KubernetesVersionProfile or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.hybridcontainerservice.models.KubernetesVersionProfile]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_put_kubernetes_versions(
        self,
        custom_location_resource_uri: str,
        kubernetes_versions: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.KubernetesVersionProfile]:
        """Puts the kubernetes version.

        Puts the kubernetes version resource type.

        :param custom_location_resource_uri: The fully qualified Azure Resource manager identifier of
         the custom location resource. Required.
        :type custom_location_resource_uri: str
        :param kubernetes_versions: Kubernetes Versions resource definition. Required.
        :type kubernetes_versions: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either KubernetesVersionProfile or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.hybridcontainerservice.models.KubernetesVersionProfile]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_put_kubernetes_versions(
        self,
        custom_location_resource_uri: str,
        kubernetes_versions: Union[_models.KubernetesVersionProfile, IO],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.KubernetesVersionProfile]:
        """Puts the kubernetes version.

        Puts the kubernetes version resource type.

        :param custom_location_resource_uri: The fully qualified Azure Resource manager identifier of
         the custom location resource. Required.
        :type custom_location_resource_uri: str
        :param kubernetes_versions: Kubernetes Versions resource definition. Is either a
         KubernetesVersionProfile type or a IO type. Required.
        :type kubernetes_versions: ~azure.mgmt.hybridcontainerservice.models.KubernetesVersionProfile
         or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either KubernetesVersionProfile or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.hybridcontainerservice.models.KubernetesVersionProfile]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.KubernetesVersionProfile] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._put_kubernetes_versions_initial(
                custom_location_resource_uri=custom_location_resource_uri,
                kubernetes_versions=kubernetes_versions,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("KubernetesVersionProfile", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod,
                AsyncARMPolling(lro_delay, lro_options={"final-state-via": "azure-async-operation"}, **kwargs),
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    begin_put_kubernetes_versions.metadata = {
        "url": "/{customLocationResourceUri}/providers/Microsoft.HybridContainerService/kubernetesVersions/default"
    }

    async def _delete_kubernetes_versions_initial(  # pylint: disable=inconsistent-return-statements
        self, custom_location_resource_uri: str, **kwargs: Any
    ) -> None:
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

        request = build_delete_kubernetes_versions_request(
            custom_location_resource_uri=custom_location_resource_uri,
            api_version=api_version,
            template_url=self._delete_kubernetes_versions_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 202:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    _delete_kubernetes_versions_initial.metadata = {
        "url": "/{customLocationResourceUri}/providers/Microsoft.HybridContainerService/kubernetesVersions/default"
    }

    @distributed_trace_async
    async def begin_delete_kubernetes_versions(
        self, custom_location_resource_uri: str, **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Delete the kubernetes versions.

        Delete the kubernetes versions resource type.

        :param custom_location_resource_uri: The fully qualified Azure Resource manager identifier of
         the custom location resource. Required.
        :type custom_location_resource_uri: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._delete_kubernetes_versions_initial(  # type: ignore
                custom_location_resource_uri=custom_location_resource_uri,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod,
                AsyncARMPolling(lro_delay, lro_options={"final-state-via": "azure-async-operation"}, **kwargs),
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    begin_delete_kubernetes_versions.metadata = {
        "url": "/{customLocationResourceUri}/providers/Microsoft.HybridContainerService/kubernetesVersions/default"
    }

    @distributed_trace_async
    async def get_vm_skus(self, custom_location_resource_uri: str, **kwargs: Any) -> _models.VmSkuProfile:
        """Gets the supported VM skus.

        Gets the supported VM skus from the underlying custom location.

        :param custom_location_resource_uri: The fully qualified Azure Resource manager identifier of
         the custom location resource. Required.
        :type custom_location_resource_uri: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: VmSkuProfile or the result of cls(response)
        :rtype: ~azure.mgmt.hybridcontainerservice.models.VmSkuProfile
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
        cls: ClsType[_models.VmSkuProfile] = kwargs.pop("cls", None)

        request = build_get_vm_skus_request(
            custom_location_resource_uri=custom_location_resource_uri,
            api_version=api_version,
            template_url=self.get_vm_skus.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("VmSkuProfile", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_vm_skus.metadata = {
        "url": "/{customLocationResourceUri}/providers/Microsoft.HybridContainerService/skus/default"
    }

    async def _put_vm_skus_initial(
        self, custom_location_resource_uri: str, skus: Union[_models.VmSkuProfile, IO], **kwargs: Any
    ) -> _models.VmSkuProfile:
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
        cls: ClsType[_models.VmSkuProfile] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(skus, (IOBase, bytes)):
            _content = skus
        else:
            _json = self._serialize.body(skus, "VmSkuProfile")

        request = build_put_vm_skus_request(
            custom_location_resource_uri=custom_location_resource_uri,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self._put_vm_skus_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("VmSkuProfile", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("VmSkuProfile", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    _put_vm_skus_initial.metadata = {
        "url": "/{customLocationResourceUri}/providers/Microsoft.HybridContainerService/skus/default"
    }

    @overload
    async def begin_put_vm_skus(
        self,
        custom_location_resource_uri: str,
        skus: _models.VmSkuProfile,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.VmSkuProfile]:
        """Puts the VM SKUs.

        Puts the VM SKUs resource type.

        :param custom_location_resource_uri: The fully qualified Azure Resource manager identifier of
         the custom location resource. Required.
        :type custom_location_resource_uri: str
        :param skus: VM SKUs resource definition. Required.
        :type skus: ~azure.mgmt.hybridcontainerservice.models.VmSkuProfile
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either VmSkuProfile or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.hybridcontainerservice.models.VmSkuProfile]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_put_vm_skus(
        self, custom_location_resource_uri: str, skus: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncLROPoller[_models.VmSkuProfile]:
        """Puts the VM SKUs.

        Puts the VM SKUs resource type.

        :param custom_location_resource_uri: The fully qualified Azure Resource manager identifier of
         the custom location resource. Required.
        :type custom_location_resource_uri: str
        :param skus: VM SKUs resource definition. Required.
        :type skus: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either VmSkuProfile or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.hybridcontainerservice.models.VmSkuProfile]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_put_vm_skus(
        self, custom_location_resource_uri: str, skus: Union[_models.VmSkuProfile, IO], **kwargs: Any
    ) -> AsyncLROPoller[_models.VmSkuProfile]:
        """Puts the VM SKUs.

        Puts the VM SKUs resource type.

        :param custom_location_resource_uri: The fully qualified Azure Resource manager identifier of
         the custom location resource. Required.
        :type custom_location_resource_uri: str
        :param skus: VM SKUs resource definition. Is either a VmSkuProfile type or a IO type. Required.
        :type skus: ~azure.mgmt.hybridcontainerservice.models.VmSkuProfile or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either VmSkuProfile or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.hybridcontainerservice.models.VmSkuProfile]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.VmSkuProfile] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._put_vm_skus_initial(
                custom_location_resource_uri=custom_location_resource_uri,
                skus=skus,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("VmSkuProfile", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod,
                AsyncARMPolling(lro_delay, lro_options={"final-state-via": "azure-async-operation"}, **kwargs),
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    begin_put_vm_skus.metadata = {
        "url": "/{customLocationResourceUri}/providers/Microsoft.HybridContainerService/skus/default"
    }

    async def _delete_vm_skus_initial(  # pylint: disable=inconsistent-return-statements
        self, custom_location_resource_uri: str, **kwargs: Any
    ) -> None:
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

        request = build_delete_vm_skus_request(
            custom_location_resource_uri=custom_location_resource_uri,
            api_version=api_version,
            template_url=self._delete_vm_skus_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 202:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    _delete_vm_skus_initial.metadata = {
        "url": "/{customLocationResourceUri}/providers/Microsoft.HybridContainerService/skus/default"
    }

    @distributed_trace_async
    async def begin_delete_vm_skus(self, custom_location_resource_uri: str, **kwargs: Any) -> AsyncLROPoller[None]:
        """Deletes the Vm Skus.

        Deletes the Vm Sku resource type.

        :param custom_location_resource_uri: The fully qualified Azure Resource manager identifier of
         the custom location resource. Required.
        :type custom_location_resource_uri: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._delete_vm_skus_initial(  # type: ignore
                custom_location_resource_uri=custom_location_resource_uri,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod,
                AsyncARMPolling(lro_delay, lro_options={"final-state-via": "azure-async-operation"}, **kwargs),
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    begin_delete_vm_skus.metadata = {
        "url": "/{customLocationResourceUri}/providers/Microsoft.HybridContainerService/skus/default"
    }
