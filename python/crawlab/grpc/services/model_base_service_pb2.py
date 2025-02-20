# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services/model_base_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..entity import request_pb2 as entity_dot_request__pb2
from ..entity import response_pb2 as entity_dot_response__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='services/model_base_service.proto',
  package='grpc',
  syntax='proto3',
  serialized_options=b'Z\006.;grpc',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!services/model_base_service.proto\x12\x04grpc\x1a\x14\x65ntity/request.proto\x1a\x15\x65ntity/response.proto2\xac\x04\n\x10ModelBaseService\x12*\n\x07GetById\x12\r.grpc.Request\x1a\x0e.grpc.Response\"\x00\x12&\n\x03Get\x12\r.grpc.Request\x1a\x0e.grpc.Response\"\x00\x12*\n\x07GetList\x12\r.grpc.Request\x1a\x0e.grpc.Response\"\x00\x12-\n\nDeleteById\x12\r.grpc.Request\x1a\x0e.grpc.Response\"\x00\x12)\n\x06\x44\x65lete\x12\r.grpc.Request\x1a\x0e.grpc.Response\"\x00\x12-\n\nDeleteList\x12\r.grpc.Request\x1a\x0e.grpc.Response\"\x00\x12\x32\n\x0f\x46orceDeleteList\x12\r.grpc.Request\x1a\x0e.grpc.Response\"\x00\x12-\n\nUpdateById\x12\r.grpc.Request\x1a\x0e.grpc.Response\"\x00\x12)\n\x06Update\x12\r.grpc.Request\x1a\x0e.grpc.Response\"\x00\x12,\n\tUpdateDoc\x12\r.grpc.Request\x1a\x0e.grpc.Response\"\x00\x12)\n\x06Insert\x12\r.grpc.Request\x1a\x0e.grpc.Response\"\x00\x12(\n\x05\x43ount\x12\r.grpc.Request\x1a\x0e.grpc.Response\"\x00\x42\x08Z\x06.;grpcb\x06proto3'
  ,
  dependencies=[entity_dot_request__pb2.DESCRIPTOR,entity_dot_response__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_MODELBASESERVICE = _descriptor.ServiceDescriptor(
  name='ModelBaseService',
  full_name='grpc.ModelBaseService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=89,
  serialized_end=645,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetById',
    full_name='grpc.ModelBaseService.GetById',
    index=0,
    containing_service=None,
    input_type=entity_dot_request__pb2._REQUEST,
    output_type=entity_dot_response__pb2._RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='grpc.ModelBaseService.Get',
    index=1,
    containing_service=None,
    input_type=entity_dot_request__pb2._REQUEST,
    output_type=entity_dot_response__pb2._RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetList',
    full_name='grpc.ModelBaseService.GetList',
    index=2,
    containing_service=None,
    input_type=entity_dot_request__pb2._REQUEST,
    output_type=entity_dot_response__pb2._RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteById',
    full_name='grpc.ModelBaseService.DeleteById',
    index=3,
    containing_service=None,
    input_type=entity_dot_request__pb2._REQUEST,
    output_type=entity_dot_response__pb2._RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='grpc.ModelBaseService.Delete',
    index=4,
    containing_service=None,
    input_type=entity_dot_request__pb2._REQUEST,
    output_type=entity_dot_response__pb2._RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteList',
    full_name='grpc.ModelBaseService.DeleteList',
    index=5,
    containing_service=None,
    input_type=entity_dot_request__pb2._REQUEST,
    output_type=entity_dot_response__pb2._RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ForceDeleteList',
    full_name='grpc.ModelBaseService.ForceDeleteList',
    index=6,
    containing_service=None,
    input_type=entity_dot_request__pb2._REQUEST,
    output_type=entity_dot_response__pb2._RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateById',
    full_name='grpc.ModelBaseService.UpdateById',
    index=7,
    containing_service=None,
    input_type=entity_dot_request__pb2._REQUEST,
    output_type=entity_dot_response__pb2._RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='grpc.ModelBaseService.Update',
    index=8,
    containing_service=None,
    input_type=entity_dot_request__pb2._REQUEST,
    output_type=entity_dot_response__pb2._RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateDoc',
    full_name='grpc.ModelBaseService.UpdateDoc',
    index=9,
    containing_service=None,
    input_type=entity_dot_request__pb2._REQUEST,
    output_type=entity_dot_response__pb2._RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Insert',
    full_name='grpc.ModelBaseService.Insert',
    index=10,
    containing_service=None,
    input_type=entity_dot_request__pb2._REQUEST,
    output_type=entity_dot_response__pb2._RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Count',
    full_name='grpc.ModelBaseService.Count',
    index=11,
    containing_service=None,
    input_type=entity_dot_request__pb2._REQUEST,
    output_type=entity_dot_response__pb2._RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MODELBASESERVICE)

DESCRIPTOR.services_by_name['ModelBaseService'] = _MODELBASESERVICE

# @@protoc_insertion_point(module_scope)
