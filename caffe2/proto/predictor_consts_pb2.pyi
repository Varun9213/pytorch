"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class PredictorConsts(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    META_NET_DEF_FIELD_NUMBER: builtins.int
    PREDICTOR_DBREADER_FIELD_NUMBER: builtins.int
    PARAMETERS_BLOB_TYPE_FIELD_NUMBER: builtins.int
    INPUTS_BLOB_TYPE_FIELD_NUMBER: builtins.int
    OUTPUTS_BLOB_TYPE_FIELD_NUMBER: builtins.int
    GLOBAL_INIT_NET_TYPE_FIELD_NUMBER: builtins.int
    PREDICT_INIT_NET_TYPE_FIELD_NUMBER: builtins.int
    PREDICT_NET_TYPE_FIELD_NUMBER: builtins.int
    SINGLE_PREDICTOR_FIELD_NUMBER: builtins.int
    MULTI_PREDICTOR_FIELD_NUMBER: builtins.int
    TRAIN_INIT_PLAN_TYPE_FIELD_NUMBER: builtins.int
    TRAIN_PLAN_TYPE_FIELD_NUMBER: builtins.int
    SHAPE_INFO_BLOB_FIELD_NUMBER: builtins.int
    DEFERRED_BLOB_READER_FIELD_NUMBER: builtins.int
    META_NET_DEF: typing.Text = ...
    PREDICTOR_DBREADER: typing.Text = ...
    PARAMETERS_BLOB_TYPE: typing.Text = ...
    INPUTS_BLOB_TYPE: typing.Text = ...
    OUTPUTS_BLOB_TYPE: typing.Text = ...
    GLOBAL_INIT_NET_TYPE: typing.Text = ...
    PREDICT_INIT_NET_TYPE: typing.Text = ...
    PREDICT_NET_TYPE: typing.Text = ...
    SINGLE_PREDICTOR: typing.Text = ...
    MULTI_PREDICTOR: typing.Text = ...
    TRAIN_INIT_PLAN_TYPE: typing.Text = ...
    TRAIN_PLAN_TYPE: typing.Text = ...
    SHAPE_INFO_BLOB: typing.Text = ...
    DEFERRED_BLOB_READER: typing.Text = ...

    def __init__(self,
        *,
        META_NET_DEF : typing.Optional[typing.Text] = ...,
        PREDICTOR_DBREADER : typing.Optional[typing.Text] = ...,
        PARAMETERS_BLOB_TYPE : typing.Optional[typing.Text] = ...,
        INPUTS_BLOB_TYPE : typing.Optional[typing.Text] = ...,
        OUTPUTS_BLOB_TYPE : typing.Optional[typing.Text] = ...,
        GLOBAL_INIT_NET_TYPE : typing.Optional[typing.Text] = ...,
        PREDICT_INIT_NET_TYPE : typing.Optional[typing.Text] = ...,
        PREDICT_NET_TYPE : typing.Optional[typing.Text] = ...,
        SINGLE_PREDICTOR : typing.Optional[typing.Text] = ...,
        MULTI_PREDICTOR : typing.Optional[typing.Text] = ...,
        TRAIN_INIT_PLAN_TYPE : typing.Optional[typing.Text] = ...,
        TRAIN_PLAN_TYPE : typing.Optional[typing.Text] = ...,
        SHAPE_INFO_BLOB : typing.Optional[typing.Text] = ...,
        DEFERRED_BLOB_READER : typing.Optional[typing.Text] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"DEFERRED_BLOB_READER",b"DEFERRED_BLOB_READER",u"GLOBAL_INIT_NET_TYPE",b"GLOBAL_INIT_NET_TYPE",u"INPUTS_BLOB_TYPE",b"INPUTS_BLOB_TYPE",u"META_NET_DEF",b"META_NET_DEF",u"MULTI_PREDICTOR",b"MULTI_PREDICTOR",u"OUTPUTS_BLOB_TYPE",b"OUTPUTS_BLOB_TYPE",u"PARAMETERS_BLOB_TYPE",b"PARAMETERS_BLOB_TYPE",u"PREDICTOR_DBREADER",b"PREDICTOR_DBREADER",u"PREDICT_INIT_NET_TYPE",b"PREDICT_INIT_NET_TYPE",u"PREDICT_NET_TYPE",b"PREDICT_NET_TYPE",u"SHAPE_INFO_BLOB",b"SHAPE_INFO_BLOB",u"SINGLE_PREDICTOR",b"SINGLE_PREDICTOR",u"TRAIN_INIT_PLAN_TYPE",b"TRAIN_INIT_PLAN_TYPE",u"TRAIN_PLAN_TYPE",b"TRAIN_PLAN_TYPE"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"DEFERRED_BLOB_READER",b"DEFERRED_BLOB_READER",u"GLOBAL_INIT_NET_TYPE",b"GLOBAL_INIT_NET_TYPE",u"INPUTS_BLOB_TYPE",b"INPUTS_BLOB_TYPE",u"META_NET_DEF",b"META_NET_DEF",u"MULTI_PREDICTOR",b"MULTI_PREDICTOR",u"OUTPUTS_BLOB_TYPE",b"OUTPUTS_BLOB_TYPE",u"PARAMETERS_BLOB_TYPE",b"PARAMETERS_BLOB_TYPE",u"PREDICTOR_DBREADER",b"PREDICTOR_DBREADER",u"PREDICT_INIT_NET_TYPE",b"PREDICT_INIT_NET_TYPE",u"PREDICT_NET_TYPE",b"PREDICT_NET_TYPE",u"SHAPE_INFO_BLOB",b"SHAPE_INFO_BLOB",u"SINGLE_PREDICTOR",b"SINGLE_PREDICTOR",u"TRAIN_INIT_PLAN_TYPE",b"TRAIN_INIT_PLAN_TYPE",u"TRAIN_PLAN_TYPE",b"TRAIN_PLAN_TYPE"]) -> None: ...
global___PredictorConsts = PredictorConsts
