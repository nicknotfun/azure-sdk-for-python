# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, Iterator, Optional, TypeVar, cast

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.utils import case_insensitive_dict

from .._serialization import Serializer

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_schema_get_by_id_request(id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-07-01"))
    accept = _headers.pop(
        "Accept",
        "application/json; serialization=Avro, application/json; serialization=json, text/plain; charset=utf-8, text/vnd.ms.protobuf",
    )

    # Construct URL
    _url = "/$schemaGroups/$schemas/{id}"
    path_format_arguments = {
        "id": _SERIALIZER.url("id", id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_schema_get_schema_version_request(
    group_name: str, schema_name: str, schema_version: int, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-07-01"))
    accept = _headers.pop(
        "Accept",
        "application/json; serialization=Avro, application/json; serialization=json, text/plain; charset=utf-8, text/vnd.ms.protobuf",
    )

    # Construct URL
    _url = "/$schemaGroups/{groupName}/schemas/{schemaName}/versions/{schemaVersion}"
    path_format_arguments = {
        "groupName": _SERIALIZER.url("group_name", group_name, "str"),
        "schemaName": _SERIALIZER.url(
            "schema_name", schema_name, "str", max_length=50, pattern=r"^[A-Za-z0-9][^\\/$:]*$"
        ),
        "schemaVersion": _SERIALIZER.url("schema_version", schema_version, "int"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_schema_query_id_by_content_request(
    group_name: str, schema_name: str, *, content: IO, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-07-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/$schemaGroups/{groupName}/schemas/{schemaName}:get-id"
    path_format_arguments = {
        "groupName": _SERIALIZER.url("group_name", group_name, "str"),
        "schemaName": _SERIALIZER.url(
            "schema_name", schema_name, "str", max_length=50, pattern=r"^[A-Za-z0-9][^\\/$:]*$"
        ),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, content=content, **kwargs)


def build_schema_register_request(group_name: str, schema_name: str, *, content: IO, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-07-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/$schemaGroups/{groupName}/schemas/{schemaName}"
    path_format_arguments = {
        "groupName": _SERIALIZER.url("group_name", group_name, "str"),
        "schemaName": _SERIALIZER.url(
            "schema_name", schema_name, "str", max_length=50, pattern=r"^[A-Za-z0-9][^\\/$:]*$"
        ),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, content=content, **kwargs)


class SchemaOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.schemaregistry._generated.AzureSchemaRegistry`'s
        :attr:`schema` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    def get_by_id(self, id: str, **kwargs: Any) -> Iterator[bytes]:
        """Get a registered schema by its unique ID reference.

        Gets a registered schema by its unique ID.  Azure Schema Registry guarantees that ID is unique
        within a namespace. Operation response type is based on serialization of schema requested.

        :param id: References specific schema in registry namespace. Required.
        :type id: str
        :return: Iterator of the response bytes
        :rtype: Iterator[bytes]
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
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[Iterator[bytes]] = kwargs.pop("cls", None)

        request = build_schema_get_by_id_request(
            id=id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = True
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 200]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        if response.status_code == 200:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
            response_headers["Content-Type"] = self._deserialize("str", response.headers.get("Content-Type"))
            response_headers["Schema-Id"] = self._deserialize("str", response.headers.get("Schema-Id"))
            response_headers["Schema-Id-Location"] = self._deserialize(
                "str", response.headers.get("Schema-Id-Location")
            )
            response_headers["Schema-Group-Name"] = self._deserialize("str", response.headers.get("Schema-Group-Name"))
            response_headers["Schema-Name"] = self._deserialize("str", response.headers.get("Schema-Name"))
            response_headers["Schema-Version"] = self._deserialize("int", response.headers.get("Schema-Version"))

            deserialized = response.iter_bytes()

        if response.status_code == 200:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
            response_headers["Content-Type"] = self._deserialize("str", response.headers.get("Content-Type"))
            response_headers["Schema-Id"] = self._deserialize("str", response.headers.get("Schema-Id"))
            response_headers["Schema-Id-Location"] = self._deserialize(
                "str", response.headers.get("Schema-Id-Location")
            )
            response_headers["Schema-Group-Name"] = self._deserialize("str", response.headers.get("Schema-Group-Name"))
            response_headers["Schema-Name"] = self._deserialize("str", response.headers.get("Schema-Name"))
            response_headers["Schema-Version"] = self._deserialize("int", response.headers.get("Schema-Version"))

            deserialized = response.iter_bytes()

        if cls:
            return cls(pipeline_response, cast(Iterator[bytes], deserialized), response_headers)  # type: ignore

        return cast(Iterator[bytes], deserialized)  # type: ignore

    def get_schema_version(
        self, group_name: str, schema_name: str, schema_version: int, **kwargs: Any
    ) -> Iterator[bytes]:
        """Get specific schema versions.

        Gets one specific version of one schema.

        :param group_name: Schema group under which schema is registered.  Group's serialization type
         should match the serialization type specified in the request. Required.
        :type group_name: str
        :param schema_name: Name of schema. Required.
        :type schema_name: str
        :param schema_version: Version number of specific schema. Required.
        :type schema_version: int
        :return: Iterator of the response bytes
        :rtype: Iterator[bytes]
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
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[Iterator[bytes]] = kwargs.pop("cls", None)

        request = build_schema_get_schema_version_request(
            group_name=group_name,
            schema_name=schema_name,
            schema_version=schema_version,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = True
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 200]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        if response.status_code == 200:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
            response_headers["Content-Type"] = self._deserialize("str", response.headers.get("Content-Type"))
            response_headers["Schema-Id"] = self._deserialize("str", response.headers.get("Schema-Id"))
            response_headers["Schema-Id-Location"] = self._deserialize(
                "str", response.headers.get("Schema-Id-Location")
            )
            response_headers["Schema-Group-Name"] = self._deserialize("str", response.headers.get("Schema-Group-Name"))
            response_headers["Schema-Name"] = self._deserialize("str", response.headers.get("Schema-Name"))
            response_headers["Schema-Version"] = self._deserialize("int", response.headers.get("Schema-Version"))

            deserialized = response.iter_bytes()

        if response.status_code == 200:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
            response_headers["Content-Type"] = self._deserialize("str", response.headers.get("Content-Type"))
            response_headers["Schema-Id"] = self._deserialize("str", response.headers.get("Schema-Id"))
            response_headers["Schema-Id-Location"] = self._deserialize(
                "str", response.headers.get("Schema-Id-Location")
            )
            response_headers["Schema-Group-Name"] = self._deserialize("str", response.headers.get("Schema-Group-Name"))
            response_headers["Schema-Name"] = self._deserialize("str", response.headers.get("Schema-Name"))
            response_headers["Schema-Version"] = self._deserialize("int", response.headers.get("Schema-Version"))

            deserialized = response.iter_bytes()

        if cls:
            return cls(pipeline_response, cast(Iterator[bytes], deserialized), response_headers)  # type: ignore

        return cast(Iterator[bytes], deserialized)  # type: ignore

    def query_id_by_content(  # pylint: disable=inconsistent-return-statements
        self, group_name: str, schema_name: str, schema_content: IO, **kwargs: Any
    ) -> None:
        """Get ID for existing schema.

        Gets the ID referencing an existing schema within the specified schema group, as matched by
        schema content comparison.

        :param group_name: Schema group under which schema is registered.  Group's serialization type
         should match the serialization type specified in the request. Required.
        :type group_name: str
        :param schema_name: Name of schema. Required.
        :type schema_name: str
        :param schema_content: String representation (UTF-8) of the registered schema. Required.
        :type schema_content: IO
        :return: None
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
        _params = kwargs.pop("params", {}) or {}

        content_type: str = kwargs.pop(
            "content_type", _headers.pop("Content-Type", "application/json; serialization=Avro")
        )
        cls: ClsType[None] = kwargs.pop("cls", None)

        _content = schema_content

        request = build_schema_query_id_by_content_request(
            group_name=group_name,
            schema_name=schema_name,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
        response_headers["Schema-Id"] = self._deserialize("str", response.headers.get("Schema-Id"))
        response_headers["Schema-Id-Location"] = self._deserialize("str", response.headers.get("Schema-Id-Location"))
        response_headers["Schema-Group-Name"] = self._deserialize("str", response.headers.get("Schema-Group-Name"))
        response_headers["Schema-Name"] = self._deserialize("str", response.headers.get("Schema-Name"))
        response_headers["Schema-Version"] = self._deserialize("int", response.headers.get("Schema-Version"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    def register(  # pylint: disable=inconsistent-return-statements
        self, group_name: str, schema_name: str, schema_content: IO, **kwargs: Any
    ) -> None:
        """Register new schema.

        Register new schema. If schema of specified name does not exist in specified group, schema is
        created at version 1. If schema of specified name exists already in specified group, schema is
        created at latest version + 1.

        :param group_name: Schema group under which schema should be registered.  Group's serialization
         type should match the serialization type specified in the request. Required.
        :type group_name: str
        :param schema_name: Name of schema. Required.
        :type schema_name: str
        :param schema_content: String representation (UTF-8) of the schema being registered. Required.
        :type schema_content: IO
        :return: None
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
        _params = kwargs.pop("params", {}) or {}

        content_type: str = kwargs.pop(
            "content_type", _headers.pop("Content-Type", "application/json; serialization=Avro")
        )
        cls: ClsType[None] = kwargs.pop("cls", None)

        _content = schema_content

        request = build_schema_register_request(
            group_name=group_name,
            schema_name=schema_name,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
        response_headers["Schema-Id"] = self._deserialize("str", response.headers.get("Schema-Id"))
        response_headers["Schema-Id-Location"] = self._deserialize("str", response.headers.get("Schema-Id-Location"))
        response_headers["Schema-Group-Name"] = self._deserialize("str", response.headers.get("Schema-Group-Name"))
        response_headers["Schema-Name"] = self._deserialize("str", response.headers.get("Schema-Name"))
        response_headers["Schema-Version"] = self._deserialize("int", response.headers.get("Schema-Version"))

        if cls:
            return cls(pipeline_response, None, response_headers)
