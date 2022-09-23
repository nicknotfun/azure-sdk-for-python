# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from msrest import Deserializer, Serializer

from azure.mgmt.core import AsyncARMPipelineClient
from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin

from ._configuration import ApplicationInsightsManagementClientConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential
    from azure.core.credentials_async import AsyncTokenCredential

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class ApplicationInsightsManagementClient(MultiApiClientMixin, _SDKClient):
    """Composite Swagger for Application Insights Management Client.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param api_version: API version to use if no profile is provided, or if missing in profile.
    :type api_version: str
    :param base_url: Service URL
    :type base_url: str
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    """

    DEFAULT_API_VERSION = '2022-04-01'
    _PROFILE_TAG = "azure.mgmt.applicationinsights.ApplicationInsightsManagementClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
            'analytics_items': '2015-05-01',
            'annotations': '2015-05-01',
            'api_keys': '2015-05-01',
            'component_available_features': '2015-05-01',
            'component_current_billing_features': '2015-05-01',
            'component_current_pricing_plan': '2017-10-01',
            'component_feature_capabilities': '2015-05-01',
            'component_linked_storage_accounts': '2020-03-01-preview',
            'component_quota_status': '2015-05-01',
            'components': '2020-02-02',
            'ea_subscription_list_migration_date': '2017-10-01',
            'ea_subscription_migrate_to_new_pricing_model': '2017-10-01',
            'ea_subscription_rollback_to_legacy_pricing_model': '2017-10-01',
            'export_configurations': '2015-05-01',
            'favorites': '2015-05-01',
            'live_token': '2021-10-14',
            'my_workbooks': '2021-03-08',
            'operations': '2015-05-01',
            'proactive_detection_configurations': '2015-05-01',
            'web_test_locations': '2015-05-01',
            'web_tests': '2015-05-01',
            'work_item_configurations': '2015-05-01',
            'workbook_templates': '2020-11-20',
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        api_version: Optional[str] = None,
        base_url: str = "https://management.azure.com",
        profile: KnownProfiles = KnownProfiles.default,
        **kwargs  # type: Any
    ) -> None:
        self._config = ApplicationInsightsManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(ApplicationInsightsManagementClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2015-05-01: :mod:`v2015_05_01.models<azure.mgmt.applicationinsights.v2015_05_01.models>`
           * 2017-10-01: :mod:`v2017_10_01.models<azure.mgmt.applicationinsights.v2017_10_01.models>`
           * 2018-05-01-preview: :mod:`v2018_05_01_preview.models<azure.mgmt.applicationinsights.v2018_05_01_preview.models>`
           * 2018-06-17-preview: :mod:`v2018_06_17_preview.models<azure.mgmt.applicationinsights.v2018_06_17_preview.models>`
           * 2019-10-17-preview: :mod:`v2019_10_17_preview.models<azure.mgmt.applicationinsights.v2019_10_17_preview.models>`
           * 2020-02-02: :mod:`v2020_02_02.models<azure.mgmt.applicationinsights.v2020_02_02.models>`
           * 2020-02-02-preview: :mod:`v2020_02_02_preview.models<azure.mgmt.applicationinsights.v2020_02_02_preview.models>`
           * 2020-03-01-preview: :mod:`v2020_03_01_preview.models<azure.mgmt.applicationinsights.v2020_03_01_preview.models>`
           * 2020-06-02-preview: :mod:`v2020_06_02_preview.models<azure.mgmt.applicationinsights.v2020_06_02_preview.models>`
           * 2020-11-20: :mod:`v2020_11_20.models<azure.mgmt.applicationinsights.v2020_11_20.models>`
           * 2021-03-08: :mod:`v2021_03_08.models<azure.mgmt.applicationinsights.v2021_03_08.models>`
           * 2021-08-01: :mod:`v2021_08_01.models<azure.mgmt.applicationinsights.v2021_08_01.models>`
           * 2021-10-14: :mod:`v2021_10.models<azure.mgmt.applicationinsights.v2021_10.models>`
           * 2022-04-01: :mod:`v2022_04_01.models<azure.mgmt.applicationinsights.v2022_04_01.models>`
        """
        if api_version == '2015-05-01':
            from ..v2015_05_01 import models
            return models
        elif api_version == '2017-10-01':
            from ..v2017_10_01 import models
            return models
        elif api_version == '2018-05-01-preview':
            from ..v2018_05_01_preview import models
            return models
        elif api_version == '2018-06-17-preview':
            from ..v2018_06_17_preview import models
            return models
        elif api_version == '2019-10-17-preview':
            from ..v2019_10_17_preview import models
            return models
        elif api_version == '2020-02-02':
            from ..v2020_02_02 import models
            return models
        elif api_version == '2020-02-02-preview':
            from ..v2020_02_02_preview import models
            return models
        elif api_version == '2020-03-01-preview':
            from ..v2020_03_01_preview import models
            return models
        elif api_version == '2020-06-02-preview':
            from ..v2020_06_02_preview import models
            return models
        elif api_version == '2020-11-20':
            from ..v2020_11_20 import models
            return models
        elif api_version == '2021-03-08':
            from ..v2021_03_08 import models
            return models
        elif api_version == '2021-08-01':
            from ..v2021_08_01 import models
            return models
        elif api_version == '2021-10-14':
            from ..v2021_10 import models
            return models
        elif api_version == '2022-04-01':
            from ..v2022_04_01 import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def analytics_items(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`AnalyticsItemsOperations<azure.mgmt.applicationinsights.v2015_05_01.aio.operations.AnalyticsItemsOperations>`
        """
        api_version = self._get_api_version('analytics_items')
        if api_version == '2015-05-01':
            from ..v2015_05_01.aio.operations import AnalyticsItemsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'analytics_items'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def annotations(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`AnnotationsOperations<azure.mgmt.applicationinsights.v2015_05_01.aio.operations.AnnotationsOperations>`
        """
        api_version = self._get_api_version('annotations')
        if api_version == '2015-05-01':
            from ..v2015_05_01.aio.operations import AnnotationsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'annotations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def api_keys(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`APIKeysOperations<azure.mgmt.applicationinsights.v2015_05_01.aio.operations.APIKeysOperations>`
        """
        api_version = self._get_api_version('api_keys')
        if api_version == '2015-05-01':
            from ..v2015_05_01.aio.operations import APIKeysOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'api_keys'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def component_available_features(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`ComponentAvailableFeaturesOperations<azure.mgmt.applicationinsights.v2015_05_01.aio.operations.ComponentAvailableFeaturesOperations>`
        """
        api_version = self._get_api_version('component_available_features')
        if api_version == '2015-05-01':
            from ..v2015_05_01.aio.operations import ComponentAvailableFeaturesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'component_available_features'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def component_current_billing_features(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`ComponentCurrentBillingFeaturesOperations<azure.mgmt.applicationinsights.v2015_05_01.aio.operations.ComponentCurrentBillingFeaturesOperations>`
        """
        api_version = self._get_api_version('component_current_billing_features')
        if api_version == '2015-05-01':
            from ..v2015_05_01.aio.operations import ComponentCurrentBillingFeaturesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'component_current_billing_features'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def component_current_pricing_plan(self):
        """Instance depends on the API version:

           * 2017-10-01: :class:`ComponentCurrentPricingPlanOperations<azure.mgmt.applicationinsights.v2017_10_01.aio.operations.ComponentCurrentPricingPlanOperations>`
        """
        api_version = self._get_api_version('component_current_pricing_plan')
        if api_version == '2017-10-01':
            from ..v2017_10_01.aio.operations import ComponentCurrentPricingPlanOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'component_current_pricing_plan'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def component_feature_capabilities(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`ComponentFeatureCapabilitiesOperations<azure.mgmt.applicationinsights.v2015_05_01.aio.operations.ComponentFeatureCapabilitiesOperations>`
        """
        api_version = self._get_api_version('component_feature_capabilities')
        if api_version == '2015-05-01':
            from ..v2015_05_01.aio.operations import ComponentFeatureCapabilitiesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'component_feature_capabilities'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def component_linked_storage_accounts(self):
        """Instance depends on the API version:

           * 2020-03-01-preview: :class:`ComponentLinkedStorageAccountsOperations<azure.mgmt.applicationinsights.v2020_03_01_preview.aio.operations.ComponentLinkedStorageAccountsOperations>`
        """
        api_version = self._get_api_version('component_linked_storage_accounts')
        if api_version == '2020-03-01-preview':
            from ..v2020_03_01_preview.aio.operations import ComponentLinkedStorageAccountsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'component_linked_storage_accounts'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def component_quota_status(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`ComponentQuotaStatusOperations<azure.mgmt.applicationinsights.v2015_05_01.aio.operations.ComponentQuotaStatusOperations>`
        """
        api_version = self._get_api_version('component_quota_status')
        if api_version == '2015-05-01':
            from ..v2015_05_01.aio.operations import ComponentQuotaStatusOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'component_quota_status'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def components(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`ComponentsOperations<azure.mgmt.applicationinsights.v2015_05_01.aio.operations.ComponentsOperations>`
           * 2018-05-01-preview: :class:`ComponentsOperations<azure.mgmt.applicationinsights.v2018_05_01_preview.aio.operations.ComponentsOperations>`
           * 2020-02-02: :class:`ComponentsOperations<azure.mgmt.applicationinsights.v2020_02_02.aio.operations.ComponentsOperations>`
           * 2020-02-02-preview: :class:`ComponentsOperations<azure.mgmt.applicationinsights.v2020_02_02_preview.aio.operations.ComponentsOperations>`
        """
        api_version = self._get_api_version('components')
        if api_version == '2015-05-01':
            from ..v2015_05_01.aio.operations import ComponentsOperations as OperationClass
        elif api_version == '2018-05-01-preview':
            from ..v2018_05_01_preview.aio.operations import ComponentsOperations as OperationClass
        elif api_version == '2020-02-02':
            from ..v2020_02_02.aio.operations import ComponentsOperations as OperationClass
        elif api_version == '2020-02-02-preview':
            from ..v2020_02_02_preview.aio.operations import ComponentsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'components'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def ea_subscription_list_migration_date(self):
        """Instance depends on the API version:

           * 2017-10-01: :class:`EASubscriptionListMigrationDateOperations<azure.mgmt.applicationinsights.v2017_10_01.aio.operations.EASubscriptionListMigrationDateOperations>`
        """
        api_version = self._get_api_version('ea_subscription_list_migration_date')
        if api_version == '2017-10-01':
            from ..v2017_10_01.aio.operations import EASubscriptionListMigrationDateOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'ea_subscription_list_migration_date'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def ea_subscription_migrate_to_new_pricing_model(self):
        """Instance depends on the API version:

           * 2017-10-01: :class:`EASubscriptionMigrateToNewPricingModelOperations<azure.mgmt.applicationinsights.v2017_10_01.aio.operations.EASubscriptionMigrateToNewPricingModelOperations>`
        """
        api_version = self._get_api_version('ea_subscription_migrate_to_new_pricing_model')
        if api_version == '2017-10-01':
            from ..v2017_10_01.aio.operations import EASubscriptionMigrateToNewPricingModelOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'ea_subscription_migrate_to_new_pricing_model'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def ea_subscription_rollback_to_legacy_pricing_model(self):
        """Instance depends on the API version:

           * 2017-10-01: :class:`EASubscriptionRollbackToLegacyPricingModelOperations<azure.mgmt.applicationinsights.v2017_10_01.aio.operations.EASubscriptionRollbackToLegacyPricingModelOperations>`
        """
        api_version = self._get_api_version('ea_subscription_rollback_to_legacy_pricing_model')
        if api_version == '2017-10-01':
            from ..v2017_10_01.aio.operations import EASubscriptionRollbackToLegacyPricingModelOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'ea_subscription_rollback_to_legacy_pricing_model'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def export_configurations(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`ExportConfigurationsOperations<azure.mgmt.applicationinsights.v2015_05_01.aio.operations.ExportConfigurationsOperations>`
        """
        api_version = self._get_api_version('export_configurations')
        if api_version == '2015-05-01':
            from ..v2015_05_01.aio.operations import ExportConfigurationsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'export_configurations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def favorites(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`FavoritesOperations<azure.mgmt.applicationinsights.v2015_05_01.aio.operations.FavoritesOperations>`
        """
        api_version = self._get_api_version('favorites')
        if api_version == '2015-05-01':
            from ..v2015_05_01.aio.operations import FavoritesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'favorites'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def live_token(self):
        """Instance depends on the API version:

           * 2020-06-02-preview: :class:`LiveTokenOperations<azure.mgmt.applicationinsights.v2020_06_02_preview.aio.operations.LiveTokenOperations>`
           * 2021-10-14: :class:`LiveTokenOperations<azure.mgmt.applicationinsights.v2021_10.aio.operations.LiveTokenOperations>`
        """
        api_version = self._get_api_version('live_token')
        if api_version == '2020-06-02-preview':
            from ..v2020_06_02_preview.aio.operations import LiveTokenOperations as OperationClass
        elif api_version == '2021-10-14':
            from ..v2021_10.aio.operations import LiveTokenOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'live_token'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def my_workbooks(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`MyWorkbooksOperations<azure.mgmt.applicationinsights.v2015_05_01.aio.operations.MyWorkbooksOperations>`
           * 2021-03-08: :class:`MyWorkbooksOperations<azure.mgmt.applicationinsights.v2021_03_08.aio.operations.MyWorkbooksOperations>`
        """
        api_version = self._get_api_version('my_workbooks')
        if api_version == '2015-05-01':
            from ..v2015_05_01.aio.operations import MyWorkbooksOperations as OperationClass
        elif api_version == '2021-03-08':
            from ..v2021_03_08.aio.operations import MyWorkbooksOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'my_workbooks'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`Operations<azure.mgmt.applicationinsights.v2015_05_01.aio.operations.Operations>`
           * 2018-05-01-preview: :class:`Operations<azure.mgmt.applicationinsights.v2018_05_01_preview.aio.operations.Operations>`
           * 2018-06-17-preview: :class:`Operations<azure.mgmt.applicationinsights.v2018_06_17_preview.aio.operations.Operations>`
           * 2020-06-02-preview: :class:`Operations<azure.mgmt.applicationinsights.v2020_06_02_preview.aio.operations.Operations>`
        """
        api_version = self._get_api_version('operations')
        if api_version == '2015-05-01':
            from ..v2015_05_01.aio.operations import Operations as OperationClass
        elif api_version == '2018-05-01-preview':
            from ..v2018_05_01_preview.aio.operations import Operations as OperationClass
        elif api_version == '2018-06-17-preview':
            from ..v2018_06_17_preview.aio.operations import Operations as OperationClass
        elif api_version == '2020-06-02-preview':
            from ..v2020_06_02_preview.aio.operations import Operations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'operations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def proactive_detection_configurations(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`ProactiveDetectionConfigurationsOperations<azure.mgmt.applicationinsights.v2015_05_01.aio.operations.ProactiveDetectionConfigurationsOperations>`
           * 2018-05-01-preview: :class:`ProactiveDetectionConfigurationsOperations<azure.mgmt.applicationinsights.v2018_05_01_preview.aio.operations.ProactiveDetectionConfigurationsOperations>`
        """
        api_version = self._get_api_version('proactive_detection_configurations')
        if api_version == '2015-05-01':
            from ..v2015_05_01.aio.operations import ProactiveDetectionConfigurationsOperations as OperationClass
        elif api_version == '2018-05-01-preview':
            from ..v2018_05_01_preview.aio.operations import ProactiveDetectionConfigurationsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'proactive_detection_configurations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def web_test_locations(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`WebTestLocationsOperations<azure.mgmt.applicationinsights.v2015_05_01.aio.operations.WebTestLocationsOperations>`
        """
        api_version = self._get_api_version('web_test_locations')
        if api_version == '2015-05-01':
            from ..v2015_05_01.aio.operations import WebTestLocationsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'web_test_locations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def web_tests(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`WebTestsOperations<azure.mgmt.applicationinsights.v2015_05_01.aio.operations.WebTestsOperations>`
           * 2018-05-01-preview: :class:`WebTestsOperations<azure.mgmt.applicationinsights.v2018_05_01_preview.aio.operations.WebTestsOperations>`
        """
        api_version = self._get_api_version('web_tests')
        if api_version == '2015-05-01':
            from ..v2015_05_01.aio.operations import WebTestsOperations as OperationClass
        elif api_version == '2018-05-01-preview':
            from ..v2018_05_01_preview.aio.operations import WebTestsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'web_tests'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def work_item_configurations(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`WorkItemConfigurationsOperations<azure.mgmt.applicationinsights.v2015_05_01.aio.operations.WorkItemConfigurationsOperations>`
        """
        api_version = self._get_api_version('work_item_configurations')
        if api_version == '2015-05-01':
            from ..v2015_05_01.aio.operations import WorkItemConfigurationsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'work_item_configurations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def workbook_templates(self):
        """Instance depends on the API version:

           * 2019-10-17-preview: :class:`WorkbookTemplatesOperations<azure.mgmt.applicationinsights.v2019_10_17_preview.aio.operations.WorkbookTemplatesOperations>`
           * 2020-11-20: :class:`WorkbookTemplatesOperations<azure.mgmt.applicationinsights.v2020_11_20.aio.operations.WorkbookTemplatesOperations>`
        """
        api_version = self._get_api_version('workbook_templates')
        if api_version == '2019-10-17-preview':
            from ..v2019_10_17_preview.aio.operations import WorkbookTemplatesOperations as OperationClass
        elif api_version == '2020-11-20':
            from ..v2020_11_20.aio.operations import WorkbookTemplatesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'workbook_templates'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def workbooks(self):
        """Instance depends on the API version:

           * 2015-05-01: :class:`WorkbooksOperations<azure.mgmt.applicationinsights.v2015_05_01.aio.operations.WorkbooksOperations>`
           * 2018-06-17-preview: :class:`WorkbooksOperations<azure.mgmt.applicationinsights.v2018_06_17_preview.aio.operations.WorkbooksOperations>`
           * 2021-08-01: :class:`WorkbooksOperations<azure.mgmt.applicationinsights.v2021_08_01.aio.operations.WorkbooksOperations>`
           * 2022-04-01: :class:`WorkbooksOperations<azure.mgmt.applicationinsights.v2022_04_01.aio.operations.WorkbooksOperations>`
        """
        api_version = self._get_api_version('workbooks')
        if api_version == '2015-05-01':
            from ..v2015_05_01.aio.operations import WorkbooksOperations as OperationClass
        elif api_version == '2018-06-17-preview':
            from ..v2018_06_17_preview.aio.operations import WorkbooksOperations as OperationClass
        elif api_version == '2021-08-01':
            from ..v2021_08_01.aio.operations import WorkbooksOperations as OperationClass
        elif api_version == '2022-04-01':
            from ..v2022_04_01.aio.operations import WorkbooksOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'workbooks'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    async def close(self):
        await self._client.close()
    async def __aenter__(self):
        await self._client.__aenter__()
        return self
    async def __aexit__(self, *exc_details):
        await self._client.__aexit__(*exc_details)
