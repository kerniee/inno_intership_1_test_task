# coding: utf-8

"""
    Api Documentation

    Api Documentation  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DiseaseControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_all_using_delete2(self, **kwargs):  # noqa: E501
        """deleteAll  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_all_using_delete2(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_all_using_delete2_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_all_using_delete2_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_all_using_delete2_with_http_info(self, **kwargs):  # noqa: E501
        """deleteAll  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_all_using_delete2_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_all_using_delete2" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/potato-diseases', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_affected_areas_using_get2(self, **kwargs):  # noqa: E501
        """getAffectedAreas  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_affected_areas_using_get2(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_affected_areas_using_get2_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_affected_areas_using_get2_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_affected_areas_using_get2_with_http_info(self, **kwargs):  # noqa: E501
        """getAffectedAreas  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_affected_areas_using_get2_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_affected_areas_using_get2" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/potato-diseases/affected-areas', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_files_using_get2(self, disease_id, **kwargs):  # noqa: E501
        """getAllFiles  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_files_using_get2(disease_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int disease_id: diseaseId (required)
        :return: list[DiseaseFileDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_files_using_get2_with_http_info(disease_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_all_files_using_get2_with_http_info(disease_id, **kwargs)  # noqa: E501
            return data

    def get_all_files_using_get2_with_http_info(self, disease_id, **kwargs):  # noqa: E501
        """getAllFiles  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_files_using_get2_with_http_info(disease_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int disease_id: diseaseId (required)
        :return: list[DiseaseFileDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['disease_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_files_using_get2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'disease_id' is set
        if self.api_client.client_side_validation and ('disease_id' not in params or
                                                       params['disease_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `disease_id` when calling `get_all_files_using_get2`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'disease_id' in params:
            path_params['diseaseId'] = params['disease_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/potato-diseases/disease-files/{diseaseId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DiseaseFileDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_using_get5(self, **kwargs):  # noqa: E501
        """getAll  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_using_get5(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_num: pageNum
        :param int per_page: perPage
        :param str name: name
        :param list[str] types: types
        :param list[str] subtypes: subtypes
        :param list[str] affected_areas: affectedAreas
        :return: PageDisease
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_using_get5_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_using_get5_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_using_get5_with_http_info(self, **kwargs):  # noqa: E501
        """getAll  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_using_get5_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_num: pageNum
        :param int per_page: perPage
        :param str name: name
        :param list[str] types: types
        :param list[str] subtypes: subtypes
        :param list[str] affected_areas: affectedAreas
        :return: PageDisease
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_num', 'per_page', 'name', 'types', 'subtypes', 'affected_areas']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_using_get5" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_num' in params:
            query_params.append(('pageNum', params['page_num']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('perPage', params['per_page']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'types' in params:
            query_params.append(('types', params['types']))  # noqa: E501
            collection_formats['types'] = 'multi'  # noqa: E501
        if 'subtypes' in params:
            query_params.append(('subtypes', params['subtypes']))  # noqa: E501
            collection_formats['subtypes'] = 'multi'  # noqa: E501
        if 'affected_areas' in params:
            query_params.append(('affectedAreas', params['affected_areas']))  # noqa: E501
            collection_formats['affectedAreas'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/potato-diseases/all', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageDisease',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_by_id_using_get2(self, id, **kwargs):  # noqa: E501
        """getById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_id_using_get2(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: id (required)
        :return: Disease
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_by_id_using_get2_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_by_id_using_get2_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_by_id_using_get2_with_http_info(self, id, **kwargs):  # noqa: E501
        """getById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_id_using_get2_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: id (required)
        :return: Disease
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_by_id_using_get2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `get_by_id_using_get2`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/potato-diseases/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Disease',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_by_number_and_culture_id_using_get(self, number, culture_id, **kwargs):  # noqa: E501
        """getByNumberAndCultureId  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_number_and_culture_id_using_get(number, culture_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str number: number (required)
        :param int culture_id: cultureId (required)
        :return: Disease
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_by_number_and_culture_id_using_get_with_http_info(number, culture_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_by_number_and_culture_id_using_get_with_http_info(number, culture_id, **kwargs)  # noqa: E501
            return data

    def get_by_number_and_culture_id_using_get_with_http_info(self, number, culture_id, **kwargs):  # noqa: E501
        """getByNumberAndCultureId  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_number_and_culture_id_using_get_with_http_info(number, culture_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str number: number (required)
        :param int culture_id: cultureId (required)
        :return: Disease
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['number', 'culture_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_by_number_and_culture_id_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'number' is set
        if self.api_client.client_side_validation and ('number' not in params or
                                                       params['number'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `number` when calling `get_by_number_and_culture_id_using_get`")  # noqa: E501
        # verify the required parameter 'culture_id' is set
        if self.api_client.client_side_validation and ('culture_id' not in params or
                                                       params['culture_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `culture_id` when calling `get_by_number_and_culture_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'number' in params:
            query_params.append(('number', params['number']))  # noqa: E501
        if 'culture_id' in params:
            query_params.append(('cultureId', params['culture_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/potato-diseases', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Disease',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sub_types_using_get2(self, **kwargs):  # noqa: E501
        """getSubTypes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sub_types_using_get2(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sub_types_using_get2_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_sub_types_using_get2_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_sub_types_using_get2_with_http_info(self, **kwargs):  # noqa: E501
        """getSubTypes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sub_types_using_get2_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sub_types_using_get2" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/potato-diseases/subtypes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_types_using_get2(self, **kwargs):  # noqa: E501
        """getTypes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_types_using_get2(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_types_using_get2_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_types_using_get2_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_types_using_get2_with_http_info(self, **kwargs):  # noqa: E501
        """getTypes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_types_using_get2_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_types_using_get2" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/potato-diseases/types', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_disease_from_xlsx_using_post2(self, file, from_index, to_index, **kwargs):  # noqa: E501
        """saveDiseaseFromXLSX  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_disease_from_xlsx_using_post2(file, from_index, to_index, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file file: file (required)
        :param int from_index: fromIndex (required)
        :param int to_index: toIndex (required)
        :param int sheet_number: sheetNumber
        :return: DownloadReport
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_disease_from_xlsx_using_post2_with_http_info(file, from_index, to_index, **kwargs)  # noqa: E501
        else:
            (data) = self.save_disease_from_xlsx_using_post2_with_http_info(file, from_index, to_index, **kwargs)  # noqa: E501
            return data

    def save_disease_from_xlsx_using_post2_with_http_info(self, file, from_index, to_index, **kwargs):  # noqa: E501
        """saveDiseaseFromXLSX  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_disease_from_xlsx_using_post2_with_http_info(file, from_index, to_index, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file file: file (required)
        :param int from_index: fromIndex (required)
        :param int to_index: toIndex (required)
        :param int sheet_number: sheetNumber
        :return: DownloadReport
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'from_index', 'to_index', 'sheet_number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_disease_from_xlsx_using_post2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if self.api_client.client_side_validation and ('file' not in params or
                                                       params['file'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `file` when calling `save_disease_from_xlsx_using_post2`")  # noqa: E501
        # verify the required parameter 'from_index' is set
        if self.api_client.client_side_validation and ('from_index' not in params or
                                                       params['from_index'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `from_index` when calling `save_disease_from_xlsx_using_post2`")  # noqa: E501
        # verify the required parameter 'to_index' is set
        if self.api_client.client_side_validation and ('to_index' not in params or
                                                       params['to_index'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `to_index` when calling `save_disease_from_xlsx_using_post2`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'from_index' in params:
            query_params.append(('fromIndex', params['from_index']))  # noqa: E501
        if 'to_index' in params:
            query_params.append(('toIndex', params['to_index']))  # noqa: E501
        if 'sheet_number' in params:
            query_params.append(('sheetNumber', params['sheet_number']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            local_var_files['file'] = params['file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/potato-diseases', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DownloadReport',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_disease_using_put2(self, update_disease_dto, **kwargs):  # noqa: E501
        """updateDisease  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_disease_using_put2(update_disease_dto, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateDiseaseDto update_disease_dto: updateDiseaseDto (required)
        :return: Disease
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_disease_using_put2_with_http_info(update_disease_dto, **kwargs)  # noqa: E501
        else:
            (data) = self.update_disease_using_put2_with_http_info(update_disease_dto, **kwargs)  # noqa: E501
            return data

    def update_disease_using_put2_with_http_info(self, update_disease_dto, **kwargs):  # noqa: E501
        """updateDisease  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_disease_using_put2_with_http_info(update_disease_dto, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateDiseaseDto update_disease_dto: updateDiseaseDto (required)
        :return: Disease
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['update_disease_dto']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_disease_using_put2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'update_disease_dto' is set
        if self.api_client.client_side_validation and ('update_disease_dto' not in params or
                                                       params['update_disease_dto'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `update_disease_dto` when calling `update_disease_using_put2`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update_disease_dto' in params:
            body_params = params['update_disease_dto']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/potato-diseases', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Disease',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
