# coding: utf-8

# flake8: noqa
"""
    Web of Science API Lite

    A responsive API that supports rich searching across the Web of Science Core Collection to retrieve core article metadata.  This service provides a great way to reuse Web of Science data both internally and externally to enhance  institutional repositories and research networking systems with best-in-class data. This API supports searching across the Web of Science to retrieve item-level metadata with limited fields:  - UT (Unique Identifier) - Authors - Author keywords - Document type - Title - Issue - Pages - Publication date - Source title - Volume - DOI - ISBN - ISSN   The API supports JSON and XML responses, and this documentation supports trying both response types.   # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from woslite_client.models.author import Author
from woslite_client.models.doctype import Doctype
from woslite_client.models.error_response import ErrorResponse
from woslite_client.models.keyword import Keyword
from woslite_client.models.other import Other
from woslite_client.models.query_result import QueryResult
from woslite_client.models.source import Source
from woslite_client.models.wos_lite_record import WosLiteRecord
from woslite_client.models.wos_lite_record_title import WosLiteRecordTitle
from woslite_client.models.wos_lite_response import WosLiteResponse
