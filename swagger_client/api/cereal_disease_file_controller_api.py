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


class CerealDiseaseFileControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_by_id_using_delete1(self, file_id, **kwargs):  # noqa: E501
        """deleteById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_by_id_using_delete1(file_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int file_id: fileId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_by_id_using_delete1_with_http_info(file_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_by_id_using_delete1_with_http_info(file_id, **kwargs)  # noqa: E501
            return data

    def delete_by_id_using_delete1_with_http_info(self, file_id, **kwargs):  # noqa: E501
        """deleteById  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_by_id_using_delete1_with_http_info(file_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int file_id: fileId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_by_id_using_delete1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_id' is set
        if self.api_client.client_side_validation and ('file_id' not in params or
                                                       params['file_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `file_id` when calling `delete_by_id_using_delete1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'file_id' in params:
            path_params['fileId'] = params['file_id']  # noqa: E501

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
            '/api/v1/cereal-disease-file/downloadFile/{fileId}', 'DELETE',
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

    def download_file_using_get1(self, file_id, **kwargs):  # noqa: E501
        """downloadFile  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_file_using_get1(file_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int file_id: fileId (required)
        :return: ByteArrayResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.download_file_using_get1_with_http_info(file_id, **kwargs)  # noqa: E501
        else:
            (data) = self.download_file_using_get1_with_http_info(file_id, **kwargs)  # noqa: E501
            return data

    def download_file_using_get1_with_http_info(self, file_id, **kwargs):  # noqa: E501
        """downloadFile  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_file_using_get1_with_http_info(file_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int file_id: fileId (required)
        :return: ByteArrayResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_file_using_get1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_id' is set
        if self.api_client.client_side_validation and ('file_id' not in params or
                                                       params['file_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `file_id` when calling `download_file_using_get1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'file_id' in params:
            path_params['fileId'] = params['file_id']  # noqa: E501

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
            '/api/v1/cereal-disease-file/downloadFile/{fileId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ByteArrayResource',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upload_file_using_post1(self, file, **kwargs):  # noqa: E501
        """uploadFile  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_file_using_post1(file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file file: file (required)
        :param int disease_id: diseaseId
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.upload_file_using_post1_with_http_info(file, **kwargs)  # noqa: E501
        else:
            (data) = self.upload_file_using_post1_with_http_info(file, **kwargs)  # noqa: E501
            return data

    def upload_file_using_post1_with_http_info(self, file, **kwargs):  # noqa: E501
        """uploadFile  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_file_using_post1_with_http_info(file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file file: file (required)
        :param int disease_id: diseaseId
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'disease_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_file_using_post1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if self.api_client.client_side_validation and ('file' not in params or
                                                       params['file'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `file` when calling `upload_file_using_post1`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'disease_id' in params:
            query_params.append(('diseaseId', params['disease_id']))  # noqa: E501

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
            '/api/v1/cereal-disease-file', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
