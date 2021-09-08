# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class AnalyzeParameters(msrest.serialization.Model):
    """This is the parameter set of either the conversation application itself or one of the target services.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: LUISParameters, DeepstackParameters, QuestionAnsweringParameters.

    All required parameters must be populated in order to send to Azure.

    :param target_type: Required. The type of a target service.Constant filled by server.  Possible
     values include: "luis", "luis_deepstack", "question_answering".
    :type target_type: str or ~azure.ai.language.conversations.models.TargetType
    :param api_version: The API version to use when call a specific target service.
    :type api_version: str
    """

    _validation = {
        'target_type': {'required': True},
    }

    _attribute_map = {
        'target_type': {'key': 'targetType', 'type': 'str'},
        'api_version': {'key': 'apiVersion', 'type': 'str'},
    }

    _subtype_map = {
        'target_type': {'luis': 'LUISParameters', 'luis_deepstack': 'DeepstackParameters', 'question_answering': 'QuestionAnsweringParameters'}
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AnalyzeParameters, self).__init__(**kwargs)
        self.target_type = None  # type: Optional[str]
        self.api_version = kwargs.get('api_version', None)


class BasePrediction(msrest.serialization.Model):
    """This is the base class of prediction.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: DeepstackPrediction, WorkflowPrediction.

    All required parameters must be populated in order to send to Azure.

    :param project_type: Required. The type of the project.Constant filled by server.  Possible
     values include: "conversation", "workflow".
    :type project_type: str or ~azure.ai.language.conversations.models.ProjectType
    :param top_intent: The intent with the highest score.
    :type top_intent: str
    """

    _validation = {
        'project_type': {'required': True},
    }

    _attribute_map = {
        'project_type': {'key': 'projectType', 'type': 'str'},
        'top_intent': {'key': 'topIntent', 'type': 'str'},
    }

    _subtype_map = {
        'project_type': {'conversation': 'DeepstackPrediction', 'workflow': 'WorkflowPrediction'}
    }

    def __init__(
        self,
        **kwargs
    ):
        super(BasePrediction, self).__init__(**kwargs)
        self.project_type = None  # type: Optional[str]
        self.top_intent = kwargs.get('top_intent', None)


class ConversationAnalysisInput(msrest.serialization.Model):
    """The request body.

    All required parameters must be populated in order to send to Azure.

    :param query: Required. The conversation utterance to be analyzed.
    :type query: str
    :param direct_target: The name of the target project this request is sending to directly.
    :type direct_target: str
    :param language: The language to use in this request. This will be the language setting when
     communicating with all other target projects.
    :type language: str
    :param verbose: If true, the service will return more detailed information in the response.
    :type verbose: bool
    :param is_logging_enabled: If true, the query will be kept by the service for customers to
     further review, to improve the model quality.
    :type is_logging_enabled: bool
    :param parameters: A dictionary representing the input for each target project.
    :type parameters: dict[str, ~azure.ai.language.conversations.models.AnalyzeParameters]
    """

    _validation = {
        'query': {'required': True},
    }

    _attribute_map = {
        'query': {'key': 'query', 'type': 'str'},
        'direct_target': {'key': 'directTarget', 'type': 'str'},
        'language': {'key': 'language', 'type': 'str'},
        'verbose': {'key': 'verbose', 'type': 'bool'},
        'is_logging_enabled': {'key': 'isLoggingEnabled', 'type': 'bool'},
        'parameters': {'key': 'parameters', 'type': '{AnalyzeParameters}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ConversationAnalysisInput, self).__init__(**kwargs)
        self.query = kwargs['query']
        self.direct_target = kwargs.get('direct_target', None)
        self.language = kwargs.get('language', None)
        self.verbose = kwargs.get('verbose', None)
        self.is_logging_enabled = kwargs.get('is_logging_enabled', None)
        self.parameters = kwargs.get('parameters', None)


class ConversationAnalysisResult(msrest.serialization.Model):
    """Represents a conversation analysis response.

    All required parameters must be populated in order to send to Azure.

    :param query: Required. The conversation utterance given by the caller.
    :type query: str
    :param detected_language: The system detected language for the query.
    :type detected_language: str
    :param prediction: Required. The prediction result of a conversation project.
    :type prediction: ~azure.ai.language.conversations.models.BasePrediction
    """

    _validation = {
        'query': {'required': True},
        'prediction': {'required': True},
    }

    _attribute_map = {
        'query': {'key': 'query', 'type': 'str'},
        'detected_language': {'key': 'detectedLanguage', 'type': 'str'},
        'prediction': {'key': 'prediction', 'type': 'BasePrediction'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ConversationAnalysisResult, self).__init__(**kwargs)
        self.query = kwargs['query']
        self.detected_language = kwargs.get('detected_language', None)
        self.prediction = kwargs['prediction']


class DeepstackCallingOptions(msrest.serialization.Model):
    """The option to set to call a LUIS Deepstack project.

    :param language: The language of the query.
    :type language: str
    :param verbose: If true, the service will return more detailed information.
    :type verbose: bool
    :param is_logging_enabled: If true, the query will be saved for customers to further review in
     authoring, to improve the model quality.
    :type is_logging_enabled: bool
    """

    _attribute_map = {
        'language': {'key': 'language', 'type': 'str'},
        'verbose': {'key': 'verbose', 'type': 'bool'},
        'is_logging_enabled': {'key': 'isLoggingEnabled', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DeepstackCallingOptions, self).__init__(**kwargs)
        self.language = kwargs.get('language', None)
        self.verbose = kwargs.get('verbose', None)
        self.is_logging_enabled = kwargs.get('is_logging_enabled', None)


class DeepstackClassification(msrest.serialization.Model):
    """The classification result of a LUIS Deepstack project.

    All required parameters must be populated in order to send to Azure.

    :param category: Required. A predicted class.
    :type category: str
    :param confidence_score: Required. The confidence score of the class from 0.0 to 1.0.
    :type confidence_score: float
    """

    _validation = {
        'category': {'required': True},
        'confidence_score': {'required': True, 'maximum': 1, 'minimum': 0},
    }

    _attribute_map = {
        'category': {'key': 'category', 'type': 'str'},
        'confidence_score': {'key': 'confidenceScore', 'type': 'float'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DeepstackClassification, self).__init__(**kwargs)
        self.category = kwargs['category']
        self.confidence_score = kwargs['confidence_score']


class DeepstackEntity(msrest.serialization.Model):
    """The entity extraction result of a LUIS Deepstack project.

    All required parameters must be populated in order to send to Azure.

    :param category: Required. The entity category.
    :type category: str
    :param text: Required. The predicted entity text.
    :type text: str
    :param offset: Required. The starting index of this entity in the query.
    :type offset: int
    :param length: Required. The length of the text.
    :type length: int
    :param confidence_score: Required. The entity confidence score.
    :type confidence_score: float
    """

    _validation = {
        'category': {'required': True},
        'text': {'required': True},
        'offset': {'required': True},
        'length': {'required': True},
        'confidence_score': {'required': True},
    }

    _attribute_map = {
        'category': {'key': 'category', 'type': 'str'},
        'text': {'key': 'text', 'type': 'str'},
        'offset': {'key': 'offset', 'type': 'int'},
        'length': {'key': 'length', 'type': 'int'},
        'confidence_score': {'key': 'confidenceScore', 'type': 'float'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DeepstackEntity, self).__init__(**kwargs)
        self.category = kwargs['category']
        self.text = kwargs['text']
        self.offset = kwargs['offset']
        self.length = kwargs['length']
        self.confidence_score = kwargs['confidence_score']


class DeepstackParameters(AnalyzeParameters):
    """This is a set of request parameters for LUIS Deepstack projects.

    All required parameters must be populated in order to send to Azure.

    :param target_type: Required. The type of a target service.Constant filled by server.  Possible
     values include: "luis", "luis_deepstack", "question_answering".
    :type target_type: str or ~azure.ai.language.conversations.models.TargetType
    :param api_version: The API version to use when call a specific target service.
    :type api_version: str
    :param calling_options: The option to set to call a LUIS Deepstack project.
    :type calling_options: ~azure.ai.language.conversations.models.DeepstackCallingOptions
    """

    _validation = {
        'target_type': {'required': True},
    }

    _attribute_map = {
        'target_type': {'key': 'targetType', 'type': 'str'},
        'api_version': {'key': 'apiVersion', 'type': 'str'},
        'calling_options': {'key': 'callingOptions', 'type': 'DeepstackCallingOptions'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DeepstackParameters, self).__init__(**kwargs)
        self.target_type = 'luis_deepstack'  # type: str
        self.calling_options = kwargs.get('calling_options', None)


class DeepstackPrediction(BasePrediction):
    """Represents the prediction section of a LUIS Deepstack project.

    All required parameters must be populated in order to send to Azure.

    :param project_type: Required. The type of the project.Constant filled by server.  Possible
     values include: "conversation", "workflow".
    :type project_type: str or ~azure.ai.language.conversations.models.ProjectType
    :param top_intent: The intent with the highest score.
    :type top_intent: str
    :param classifications: Required. The classification results.
    :type classifications: list[~azure.ai.language.conversations.models.DeepstackClassification]
    :param entities: Required. The entity extraction results.
    :type entities: list[~azure.ai.language.conversations.models.DeepstackEntity]
    """

    _validation = {
        'project_type': {'required': True},
        'classifications': {'required': True},
        'entities': {'required': True},
    }

    _attribute_map = {
        'project_type': {'key': 'projectType', 'type': 'str'},
        'top_intent': {'key': 'topIntent', 'type': 'str'},
        'classifications': {'key': 'intents', 'type': '[DeepstackClassification]'},
        'entities': {'key': 'entities', 'type': '[DeepstackEntity]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DeepstackPrediction, self).__init__(**kwargs)
        self.project_type = 'conversation'  # type: str
        self.classifications = kwargs['classifications']
        self.entities = kwargs['entities']


class DeepstackResult(msrest.serialization.Model):
    """The response returned by a LUIS Deepstack project.

    All required parameters must be populated in order to send to Azure.

    :param query: Required. The same query given in request.
    :type query: str
    :param detected_language: The detected language from the query.
    :type detected_language: str
    :param prediction: Required. The predicted result for the query.
    :type prediction: ~azure.ai.language.conversations.models.DeepstackPrediction
    """

    _validation = {
        'query': {'required': True},
        'prediction': {'required': True},
    }

    _attribute_map = {
        'query': {'key': 'query', 'type': 'str'},
        'detected_language': {'key': 'detectedLanguage', 'type': 'str'},
        'prediction': {'key': 'prediction', 'type': 'DeepstackPrediction'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DeepstackResult, self).__init__(**kwargs)
        self.query = kwargs['query']
        self.detected_language = kwargs.get('detected_language', None)
        self.prediction = kwargs['prediction']


class TargetIntentResult(msrest.serialization.Model):
    """This is the base class of an intent prediction.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: LUISTargetIntentResult, DSTargetIntentResult, QuestionAnsweringTargetIntentResult.

    All required parameters must be populated in order to send to Azure.

    :param target_type: Required. This discriminator property specifies the type of the target
     project that returns the response. 'luis' means the type is LUIS Generally Available.
     'luis_deepstack' means LUIS vNext. 'question_answering' means Question Answering.Constant
     filled by server.  Possible values include: "luis", "luis_deepstack", "question_answering".
    :type target_type: str or ~azure.ai.language.conversations.models.TargetType
    :param api_version: The API version used to call a target service.
    :type api_version: str
    :param confidence_score: Required. The prediction score and it ranges from 0.0 to 1.0.
    :type confidence_score: float
    """

    _validation = {
        'target_type': {'required': True},
        'confidence_score': {'required': True, 'maximum': 1, 'minimum': 0},
    }

    _attribute_map = {
        'target_type': {'key': 'targetType', 'type': 'str'},
        'api_version': {'key': 'apiVersion', 'type': 'str'},
        'confidence_score': {'key': 'confidenceScore', 'type': 'float'},
    }

    _subtype_map = {
        'target_type': {'luis': 'LUISTargetIntentResult', 'luis_deepstack': 'DSTargetIntentResult', 'question_answering': 'QuestionAnsweringTargetIntentResult'}
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TargetIntentResult, self).__init__(**kwargs)
        self.target_type = None  # type: Optional[str]
        self.api_version = kwargs.get('api_version', None)
        self.confidence_score = kwargs['confidence_score']


class DSTargetIntentResult(TargetIntentResult):
    """A wrap up of LUIS Deepstack response.

    All required parameters must be populated in order to send to Azure.

    :param target_type: Required. This discriminator property specifies the type of the target
     project that returns the response. 'luis' means the type is LUIS Generally Available.
     'luis_deepstack' means LUIS vNext. 'question_answering' means Question Answering.Constant
     filled by server.  Possible values include: "luis", "luis_deepstack", "question_answering".
    :type target_type: str or ~azure.ai.language.conversations.models.TargetType
    :param api_version: The API version used to call a target service.
    :type api_version: str
    :param confidence_score: Required. The prediction score and it ranges from 0.0 to 1.0.
    :type confidence_score: float
    :param result: The actual response from a LUIS Deepstack application.
    :type result: ~azure.ai.language.conversations.models.DeepstackResult
    """

    _validation = {
        'target_type': {'required': True},
        'confidence_score': {'required': True, 'maximum': 1, 'minimum': 0},
    }

    _attribute_map = {
        'target_type': {'key': 'targetType', 'type': 'str'},
        'api_version': {'key': 'apiVersion', 'type': 'str'},
        'confidence_score': {'key': 'confidenceScore', 'type': 'float'},
        'result': {'key': 'result', 'type': 'DeepstackResult'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DSTargetIntentResult, self).__init__(**kwargs)
        self.target_type = 'luis_deepstack'  # type: str
        self.result = kwargs.get('result', None)


class Error(msrest.serialization.Model):
    """The error object.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. One of a server-defined set of error codes. Possible values include:
     "InvalidRequest", "InvalidArgument", "Unauthorized", "Forbidden", "NotFound",
     "TooManyRequests", "InternalServerError", "ServiceUnavailable".
    :type code: str or ~azure.ai.language.conversations.models.ErrorCode
    :param message: Required. A human-readable representation of the error.
    :type message: str
    :param target: The target of the error.
    :type target: str
    :param details: An array of details about specific errors that led to this reported error.
    :type details: list[~azure.ai.language.conversations.models.Error]
    :param innererror: An object containing more specific information than the current object about
     the error.
    :type innererror: ~azure.ai.language.conversations.models.InnerErrorModel
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[Error]'},
        'innererror': {'key': 'innererror', 'type': 'InnerErrorModel'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Error, self).__init__(**kwargs)
        self.code = kwargs['code']
        self.message = kwargs['message']
        self.target = kwargs.get('target', None)
        self.details = kwargs.get('details', None)
        self.innererror = kwargs.get('innererror', None)


class ErrorResponse(msrest.serialization.Model):
    """Error response.

    :param error: The error object.
    :type error: ~azure.ai.language.conversations.models.Error
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'Error'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class InnerErrorModel(msrest.serialization.Model):
    """An object containing more specific information about the error. As per Microsoft One API guidelines - https://github.com/Microsoft/api-guidelines/blob/vNext/Guidelines.md#7102-error-condition-responses.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. One of a server-defined set of error codes. Possible values include:
     "InvalidRequest", "InvalidParameterValue", "KnowledgeBaseNotFound",
     "AzureCognitiveSearchNotFound", "AzureCognitiveSearchThrottling", "ExtractionFailure".
    :type code: str or ~azure.ai.language.conversations.models.InnerErrorCode
    :param message: Required. Error message.
    :type message: str
    :param details: Error details.
    :type details: dict[str, str]
    :param target: Error target.
    :type target: str
    :param innererror: An object containing more specific information than the current object about
     the error.
    :type innererror: ~azure.ai.language.conversations.models.InnerErrorModel
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '{str}'},
        'target': {'key': 'target', 'type': 'str'},
        'innererror': {'key': 'innererror', 'type': 'InnerErrorModel'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(InnerErrorModel, self).__init__(**kwargs)
        self.code = kwargs['code']
        self.message = kwargs['message']
        self.details = kwargs.get('details', None)
        self.target = kwargs.get('target', None)
        self.innererror = kwargs.get('innererror', None)


class LUISCallingOptions(msrest.serialization.Model):
    """This customizes how the service calls LUIS Generally Available projects.

    :param verbose: Enable verbose response.
    :type verbose: bool
    :param log: Save log to add in training utterances later.
    :type log: bool
    :param show_all_intents: Set true to show all intents.
    :type show_all_intents: bool
    :param timezone_offset: The timezone offset for the location of the request.
    :type timezone_offset: float
    :param spell_check: Enable spell checking.
    :type spell_check: bool
    :param bing_spell_check_subscription_key: The subscription key to use when enabling Bing spell
     check.
    :type bing_spell_check_subscription_key: str
    """

    _attribute_map = {
        'verbose': {'key': 'verbose', 'type': 'bool'},
        'log': {'key': 'log', 'type': 'bool'},
        'show_all_intents': {'key': 'show-all-intents', 'type': 'bool'},
        'timezone_offset': {'key': 'timezoneOffset', 'type': 'float'},
        'spell_check': {'key': 'spellCheck', 'type': 'bool'},
        'bing_spell_check_subscription_key': {'key': 'bing-spell-check-subscription-key', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(LUISCallingOptions, self).__init__(**kwargs)
        self.verbose = kwargs.get('verbose', None)
        self.log = kwargs.get('log', None)
        self.show_all_intents = kwargs.get('show_all_intents', None)
        self.timezone_offset = kwargs.get('timezone_offset', None)
        self.spell_check = kwargs.get('spell_check', None)
        self.bing_spell_check_subscription_key = kwargs.get('bing_spell_check_subscription_key', None)


class LUISParameters(AnalyzeParameters):
    """This is a set of request parameters for LUIS Generally Available projects.

    All required parameters must be populated in order to send to Azure.

    :param target_type: Required. The type of a target service.Constant filled by server.  Possible
     values include: "luis", "luis_deepstack", "question_answering".
    :type target_type: str or ~azure.ai.language.conversations.models.TargetType
    :param api_version: The API version to use when call a specific target service.
    :type api_version: str
    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, any]
    :param query: The utterance to predict.
    :type query: str
    :param calling_options: This customizes how the service calls LUIS Generally Available
     projects.
    :type calling_options: ~azure.ai.language.conversations.models.LUISCallingOptions
    """

    _validation = {
        'target_type': {'required': True},
        'query': {'max_length': 500, 'min_length': 0},
    }

    _attribute_map = {
        'target_type': {'key': 'targetType', 'type': 'str'},
        'api_version': {'key': 'apiVersion', 'type': 'str'},
        'additional_properties': {'key': '', 'type': '{object}'},
        'query': {'key': 'query', 'type': 'str'},
        'calling_options': {'key': 'callingOptions', 'type': 'LUISCallingOptions'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(LUISParameters, self).__init__(**kwargs)
        self.target_type = 'luis'  # type: str
        self.additional_properties = kwargs.get('additional_properties', None)
        self.query = kwargs.get('query', None)
        self.calling_options = kwargs.get('calling_options', None)


class LUISTargetIntentResult(TargetIntentResult):
    """It is a wrap up of LUIS Generally Available response.

    All required parameters must be populated in order to send to Azure.

    :param target_type: Required. This discriminator property specifies the type of the target
     project that returns the response. 'luis' means the type is LUIS Generally Available.
     'luis_deepstack' means LUIS vNext. 'question_answering' means Question Answering.Constant
     filled by server.  Possible values include: "luis", "luis_deepstack", "question_answering".
    :type target_type: str or ~azure.ai.language.conversations.models.TargetType
    :param api_version: The API version used to call a target service.
    :type api_version: str
    :param confidence_score: Required. The prediction score and it ranges from 0.0 to 1.0.
    :type confidence_score: float
    :param result: The actual response from a LUIS Generally Available application.
    :type result: any
    """

    _validation = {
        'target_type': {'required': True},
        'confidence_score': {'required': True, 'maximum': 1, 'minimum': 0},
    }

    _attribute_map = {
        'target_type': {'key': 'targetType', 'type': 'str'},
        'api_version': {'key': 'apiVersion', 'type': 'str'},
        'confidence_score': {'key': 'confidenceScore', 'type': 'float'},
        'result': {'key': 'result', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(LUISTargetIntentResult, self).__init__(**kwargs)
        self.target_type = 'luis'  # type: str
        self.result = kwargs.get('result', None)


class QuestionAnsweringParameters(AnalyzeParameters):
    """This is a set of request parameters for Question Answering knowledge bases.

    All required parameters must be populated in order to send to Azure.

    :param target_type: Required. The type of a target service.Constant filled by server.  Possible
     values include: "luis", "luis_deepstack", "question_answering".
    :type target_type: str or ~azure.ai.language.conversations.models.TargetType
    :param api_version: The API version to use when call a specific target service.
    :type api_version: str
    :param project_parameters: The parameters send to a Question Answering KB.
    :type project_parameters: any
    """

    _validation = {
        'target_type': {'required': True},
    }

    _attribute_map = {
        'target_type': {'key': 'targetType', 'type': 'str'},
        'api_version': {'key': 'apiVersion', 'type': 'str'},
        'project_parameters': {'key': 'projectParameters', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(QuestionAnsweringParameters, self).__init__(**kwargs)
        self.target_type = 'question_answering'  # type: str
        self.project_parameters = kwargs.get('project_parameters', None)


class QuestionAnsweringTargetIntentResult(TargetIntentResult):
    """It is a wrap up a Question Answering KB response.

    All required parameters must be populated in order to send to Azure.

    :param target_type: Required. This discriminator property specifies the type of the target
     project that returns the response. 'luis' means the type is LUIS Generally Available.
     'luis_deepstack' means LUIS vNext. 'question_answering' means Question Answering.Constant
     filled by server.  Possible values include: "luis", "luis_deepstack", "question_answering".
    :type target_type: str or ~azure.ai.language.conversations.models.TargetType
    :param api_version: The API version used to call a target service.
    :type api_version: str
    :param confidence_score: Required. The prediction score and it ranges from 0.0 to 1.0.
    :type confidence_score: float
    :param result: The generated answer by a Question Answering KB.
    :type result: any
    """

    _validation = {
        'target_type': {'required': True},
        'confidence_score': {'required': True, 'maximum': 1, 'minimum': 0},
    }

    _attribute_map = {
        'target_type': {'key': 'targetType', 'type': 'str'},
        'api_version': {'key': 'apiVersion', 'type': 'str'},
        'confidence_score': {'key': 'confidenceScore', 'type': 'float'},
        'result': {'key': 'result', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(QuestionAnsweringTargetIntentResult, self).__init__(**kwargs)
        self.target_type = 'question_answering'  # type: str
        self.result = kwargs.get('result', None)


class WorkflowPrediction(BasePrediction):
    """This represents the prediction result of an Workflow project.

    All required parameters must be populated in order to send to Azure.

    :param project_type: Required. The type of the project.Constant filled by server.  Possible
     values include: "conversation", "workflow".
    :type project_type: str or ~azure.ai.language.conversations.models.ProjectType
    :param top_intent: The intent with the highest score.
    :type top_intent: str
    :param intents: Required. A dictionary that contains all intents. A key is an intent name and a
     value is its confidence score and target type. The top intent's value also contains the actual
     response from the target project.
    :type intents: dict[str, ~azure.ai.language.conversations.models.TargetIntentResult]
    """

    _validation = {
        'project_type': {'required': True},
        'intents': {'required': True},
    }

    _attribute_map = {
        'project_type': {'key': 'projectType', 'type': 'str'},
        'top_intent': {'key': 'topIntent', 'type': 'str'},
        'intents': {'key': 'intents', 'type': '{TargetIntentResult}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(WorkflowPrediction, self).__init__(**kwargs)
        self.project_type = 'workflow'  # type: str
        self.intents = kwargs['intents']
