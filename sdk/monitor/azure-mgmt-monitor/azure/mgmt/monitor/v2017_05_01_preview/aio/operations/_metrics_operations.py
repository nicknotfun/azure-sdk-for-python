# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, Callable, Dict, Optional, TypeVar, Union

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
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._metrics_operations import build_list_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class MetricsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~$(python-base-namespace).v2017_05_01_preview.aio.MonitorManagementClient`'s
        :attr:`metrics` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def list(
        self,
        resource_uri: str,
        timespan: Optional[str] = None,
        interval: Optional[datetime.timedelta] = None,
        metric: Optional[str] = None,
        aggregation: Optional[str] = None,
        top: Optional[int] = None,
        orderby: Optional[str] = None,
        filter: Optional[str] = None,
        result_type: Optional[Union[str, _models.ResultType]] = None,
        **kwargs: Any
    ) -> _models.Response:
        """**Lists the metric values for a resource**.

        :param resource_uri: The identifier of the resource. Required.
        :type resource_uri: str
        :param timespan: The timespan of the query. It is a string with the following format
         'startDateTime_ISO/endDateTime_ISO'. Default value is None.
        :type timespan: str
        :param interval: The interval (i.e. timegrain) of the query. Default value is None.
        :type interval: ~datetime.timedelta
        :param metric: The name of the metric to retrieve. Default value is None.
        :type metric: str
        :param aggregation: The list of aggregation types (comma separated) to retrieve. Default value
         is None.
        :type aggregation: str
        :param top: The maximum number of records to retrieve.
         Valid only if $filter is specified.
         Defaults to 10. Default value is None.
        :type top: int
        :param orderby: The aggregation to use for sorting results and the direction of the sort.
         Only one order can be specified.
         Examples: sum asc. Default value is None.
        :type orderby: str
        :param filter: The **$filter** is used to reduce the set of metric data
         returned.:code:`<br>`Example::code:`<br>`Metric contains metadata A, B and C.:code:`<br>`-
         Return all time series of C where A = a1 and B = b1 or b2:code:`<br>`\ **$filter=A eq ‘a1’ and
         B eq ‘b1’ or B eq ‘b2’ and C eq ‘*’**\ :code:`<br>`- Invalid variant::code:`<br>`\ **$filter=A
         eq ‘a1’ and B eq ‘b1’ and C eq ‘*’ or B = ‘b2’**\ :code:`<br>`This is invalid because the
         logical or operator cannot separate two different metadata names.:code:`<br>`- Return all time
         series where A = a1, B = b1 and C = c1::code:`<br>`\ **$filter=A eq ‘a1’ and B eq ‘b1’ and C eq
         ‘c1’**\ :code:`<br>`- Return all time series where A = a1:code:`<br>`\ **$filter=A eq ‘a1’ and
         B eq ‘\ *’ and C eq ‘*\ ’**. Default value is None.
        :type filter: str
        :param result_type: Reduces the set of data collected. The syntax allowed depends on the
         operation. See the operation's description for details. Known values are: "Data" and
         "Metadata". Default value is None.
        :type result_type: str or ~$(python-base-namespace).v2017_05_01_preview.models.ResultType
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Response or the result of cls(response)
        :rtype: ~$(python-base-namespace).v2017_05_01_preview.models.Response
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2017-05-01-preview"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.Response]

        request = build_list_request(
            resource_uri=resource_uri,
            timespan=timespan,
            interval=interval,
            metric=metric,
            aggregation=aggregation,
            top=top,
            orderby=orderby,
            filter=filter,
            result_type=result_type,
            api_version=api_version,
            template_url=self.list.metadata["url"],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Response", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {"url": "/{resourceUri}/providers/microsoft.insights/metrics"}  # type: ignore
