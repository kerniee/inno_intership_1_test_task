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


class RyeDeterminantControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def change_status_using_put7(self, status, determinant_id, **kwargs):  # noqa: E501
        """changeStatus  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_status_using_put7(status, determinant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str status: status (required)
        :param int determinant_id: determinantId (required)
        :return: RyeDeterminant
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.change_status_using_put7_with_http_info(status, determinant_id, **kwargs)  # noqa: E501
        else:
            (data) = self.change_status_using_put7_with_http_info(status, determinant_id, **kwargs)  # noqa: E501
            return data

    def change_status_using_put7_with_http_info(self, status, determinant_id, **kwargs):  # noqa: E501
        """changeStatus  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_status_using_put7_with_http_info(status, determinant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str status: status (required)
        :param int determinant_id: determinantId (required)
        :return: RyeDeterminant
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['status', 'determinant_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method change_status_using_put7" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'status' is set
        if self.api_client.client_side_validation and ('status' not in params or
                                                       params['status'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `status` when calling `change_status_using_put7`")  # noqa: E501
        # verify the required parameter 'determinant_id' is set
        if self.api_client.client_side_validation and ('determinant_id' not in params or
                                                       params['determinant_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `determinant_id` when calling `change_status_using_put7`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
        if 'determinant_id' in params:
            query_params.append(('determinantId', params['determinant_id']))  # noqa: E501

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
            '/api/v1/determinants-rye/status', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RyeDeterminant',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_using_put3(self, determinant, **kwargs):  # noqa: E501
        """create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_using_put3(determinant, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateDeterminantDto determinant: determinant (required)
        :return: RyeDeterminant
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_using_put3_with_http_info(determinant, **kwargs)  # noqa: E501
        else:
            (data) = self.create_using_put3_with_http_info(determinant, **kwargs)  # noqa: E501
            return data

    def create_using_put3_with_http_info(self, determinant, **kwargs):  # noqa: E501
        """create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_using_put3_with_http_info(determinant, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateDeterminantDto determinant: determinant (required)
        :return: RyeDeterminant
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['determinant']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_using_put3" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'determinant' is set
        if self.api_client.client_side_validation and ('determinant' not in params or
                                                       params['determinant'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `determinant` when calling `create_using_put3`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'determinant' in params:
            body_params = params['determinant']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/determinants-rye', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RyeDeterminant',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_using_delete8(self, id, **kwargs):  # noqa: E501
        """delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_using_delete8(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_using_delete8_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_using_delete8_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_using_delete8_with_http_info(self, id, **kwargs):  # noqa: E501
        """delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_using_delete8_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: id (required)
        :return: None
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
                    " to method delete_using_delete8" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `delete_using_delete8`")  # noqa: E501

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
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/determinants-rye/{id}', 'DELETE',
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

    def get_all_using_get15(self, **kwargs):  # noqa: E501
        """getAll  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_using_get15(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime date_from: dateFrom
        :param datetime date_to: dateTo
        :param int page_num: pageNum
        :param int per_page: perPage
        :param str statuses: statuses
        :param str sort: sort
        :return: PageRyeDeterminant
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_using_get15_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_using_get15_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_using_get15_with_http_info(self, **kwargs):  # noqa: E501
        """getAll  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_using_get15_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime date_from: dateFrom
        :param datetime date_to: dateTo
        :param int page_num: pageNum
        :param int per_page: perPage
        :param str statuses: statuses
        :param str sort: sort
        :return: PageRyeDeterminant
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['date_from', 'date_to', 'page_num', 'per_page', 'statuses', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_using_get15" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'date_from' in params:
            query_params.append(('dateFrom', params['date_from']))  # noqa: E501
        if 'date_to' in params:
            query_params.append(('dateTo', params['date_to']))  # noqa: E501
        if 'page_num' in params:
            query_params.append(('pageNum', params['page_num']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('perPage', params['per_page']))  # noqa: E501
        if 'statuses' in params:
            query_params.append(('statuses', params['statuses']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/determinants-rye', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageRyeDeterminant',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_using_get9(self, id, **kwargs):  # noqa: E501
        """get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_using_get9(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: id (required)
        :return: RyeDeterminant
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_using_get9_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_using_get9_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_using_get9_with_http_info(self, id, **kwargs):  # noqa: E501
        """get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_using_get9_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: id (required)
        :return: RyeDeterminant
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
                    " to method get_using_get9" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `get_using_get9`")  # noqa: E501

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
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/determinants-rye/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RyeDeterminant',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
