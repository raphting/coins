# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: work.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='work.proto',
  package='coins',
  serialized_pb=_b('\n\nwork.proto\x12\x05\x63oins\"I\n\x07\x43ompute\x12\x0f\n\x07payload\x18\x01 \x02(\t\x12\x0e\n\x06minnum\x18\x02 \x02(\x04\x12\x0e\n\x06maxnum\x18\x03 \x02(\x04\x12\r\n\x05zeros\x18\x04 \x02(\x04')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_COMPUTE = _descriptor.Descriptor(
  name='Compute',
  full_name='coins.Compute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload', full_name='coins.Compute.payload', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minnum', full_name='coins.Compute.minnum', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='maxnum', full_name='coins.Compute.maxnum', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='zeros', full_name='coins.Compute.zeros', index=3,
      number=4, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=94,
)

DESCRIPTOR.message_types_by_name['Compute'] = _COMPUTE

Compute = _reflection.GeneratedProtocolMessageType('Compute', (_message.Message,), dict(
  DESCRIPTOR = _COMPUTE,
  __module__ = 'work_pb2'
  # @@protoc_insertion_point(class_scope:coins.Compute)
  ))
_sym_db.RegisterMessage(Compute)


# @@protoc_insertion_point(module_scope)
