# coding: utf-8

# flake8: noqa

"""
    😸 Cheshire-Cat API

    Customizable AI architecture  # noqa: E501

    The version of the OpenAPI document: 0.0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


__version__ = "0.0.61S"

# import apis into sdk package
from cheshire_cat_api.api.memory_api import MemoryApi
from cheshire_cat_api.api.plugins_api import PluginsApi
from cheshire_cat_api.api.rabbit_hole_api import RabbitHoleApi
from cheshire_cat_api.api.settings_embedder_api import SettingsEmbedderApi
from cheshire_cat_api.api.settings_general_api import SettingsGeneralApi
from cheshire_cat_api.api.settings_large_language_model_api import SettingsLargeLanguageModelApi
from cheshire_cat_api.api.settings_prompt_api import SettingsPromptApi
from cheshire_cat_api.api.status_api import StatusApi

# import ApiClient
from cheshire_cat_api.api_response import ApiResponse
from cheshire_cat_api.api_client import ApiClient
from cheshire_cat_api.configuration import Configuration
from cheshire_cat_api.exceptions import OpenApiException
from cheshire_cat_api.exceptions import ApiTypeError
from cheshire_cat_api.exceptions import ApiValueError
from cheshire_cat_api.exceptions import ApiKeyError
from cheshire_cat_api.exceptions import ApiAttributeError
from cheshire_cat_api.exceptions import ApiException

# import models into sdk package
from cheshire_cat_api.models.body_upload_url import BodyUploadUrl
from cheshire_cat_api.models.http_validation_error import HTTPValidationError
from cheshire_cat_api.models.location_inner import LocationInner
from cheshire_cat_api.models.setting_body import SettingBody
from cheshire_cat_api.models.validation_error import ValidationError
