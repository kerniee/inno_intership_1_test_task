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


class CarrotQuestionControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_by_number_using_get2(self, number, **kwargs):  # noqa: E501
        """getByNumber  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_number_using_get2(number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int number: number (required)
        :return: CarrotQuestionDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_by_number_using_get2_with_http_info(number, **kwargs)  # noqa: E501
        else:
            (data) = self.get_by_number_using_get2_with_http_info(number, **kwargs)  # noqa: E501
            return data

    def get_by_number_using_get2_with_http_info(self, number, **kwargs):  # noqa: E501
        """getByNumber  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_number_using_get2_with_http_info(number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int number: number (required)
        :return: CarrotQuestionDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_by_number_using_get2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'number' is set
        if self.api_client.client_side_validation and ('number' not in params or
                                                       params['number'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `number` when calling `get_by_number_using_get2`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'number' in params:
            path_params['number'] = params['number']  # noqa: E501

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
            '/api/v1/questions-carrot/{number}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CarrotQuestionDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_question_by_log_using_get1(self, log, **kwargs):  # noqa: E501
        """getQuestionByLog  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_question_by_log_using_get1(log, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str log: log (required)
        :return: list[CarrotQuestionDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_question_by_log_using_get1_with_http_info(log, **kwargs)  # noqa: E501
        else:
            (data) = self.get_question_by_log_using_get1_with_http_info(log, **kwargs)  # noqa: E501
            return data

    def get_question_by_log_using_get1_with_http_info(self, log, **kwargs):  # noqa: E501
        """getQuestionByLog  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_question_by_log_using_get1_with_http_info(log, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str log: log (required)
        :return: list[CarrotQuestionDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['log']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_question_by_log_using_get1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'log' is set
        if self.api_client.client_side_validation and ('log' not in params or
                                                       params['log'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `log` when calling `get_question_by_log_using_get1`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'log' in params:
            query_params.append(('log', params['log']))  # noqa: E501

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
            '/api/v1/questions-carrot/log', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CarrotQuestionDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
