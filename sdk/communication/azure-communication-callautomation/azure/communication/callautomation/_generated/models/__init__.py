# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models import AddParticipantFailed
from ._models import AddParticipantRequest
from ._models import AddParticipantResponse
from ._models import AddParticipantSucceeded
from ._models import AnswerCallRequest
from ._models import CallConnected
from ._models import CallConnectionProperties
from ._models import CallDisconnected
from ._models import CallLocator
from ._models import CallParticipant
from ._models import CallTransferAccepted
from ._models import CallTransferFailed
from ._models import ChannelAffinity
from ._models import Choice
from ._models import ChoiceResult
from ._models import CommunicationError
from ._models import CommunicationErrorResponse
from ._models import CommunicationIdentifierModel
from ._models import CommunicationUserIdentifierModel
from ._models import ContinuousDtmfRecognitionRequest
from ._models import ContinuousDtmfRecognitionStopped
from ._models import ContinuousDtmfRecognitionToneFailed
from ._models import ContinuousDtmfRecognitionToneReceived
from ._models import CreateCallRequest
from ._models import DtmfOptions
from ._models import DtmfResult
from ._models import FileSource
from ._models import MicrosoftTeamsUserIdentifierModel
from ._models import MuteParticipantsRequest
from ._models import MuteParticipantsResponse
from ._models import ParticipantsUpdated
from ._models import PhoneNumberIdentifierModel
from ._models import PlayCanceled
from ._models import PlayCompleted
from ._models import PlayFailed
from ._models import PlayOptions
from ._models import PlayRequest
from ._models import PlaySource
from ._models import RecognizeCanceled
from ._models import RecognizeCompleted
from ._models import RecognizeFailed
from ._models import RecognizeOptions
from ._models import RecognizeRequest
from ._models import RecordingStateChanged
from ._models import RecordingStateResponse
from ._models import RedirectCallRequest
from ._models import RejectCallRequest
from ._models import RemoveParticipantFailed
from ._models import RemoveParticipantRequest
from ._models import RemoveParticipantResponse
from ._models import RemoveParticipantSucceeded
from ._models import ResultInformation
from ._models import SendDtmfCompleted
from ._models import SendDtmfFailed
from ._models import SendDtmfRequest
from ._models import SendDtmfResponse
from ._models import SpeechOptions
from ._models import SpeechResult
from ._models import SsmlSource
from ._models import StartCallRecordingRequest
from ._models import TextSource
from ._models import ToneInfo
from ._models import TransferCallResponse
from ._models import TransferToParticipantRequest

from ._enums import CallConnectionState
from ._enums import CallLocatorKind
from ._enums import CallRejectReason
from ._enums import CommunicationCloudEnvironmentModel
from ._enums import CommunicationIdentifierModelKind
from ._enums import DtmfTone
from ._enums import Gender
from ._enums import PlaySourceType
from ._enums import RecognitionType
from ._enums import RecognizeInputType
from ._enums import RecordingChannel
from ._enums import RecordingContent
from ._enums import RecordingFormat
from ._enums import RecordingState
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AddParticipantFailed",
    "AddParticipantRequest",
    "AddParticipantResponse",
    "AddParticipantSucceeded",
    "AnswerCallRequest",
    "CallConnected",
    "CallConnectionProperties",
    "CallDisconnected",
    "CallLocator",
    "CallParticipant",
    "CallTransferAccepted",
    "CallTransferFailed",
    "ChannelAffinity",
    "Choice",
    "ChoiceResult",
    "CommunicationError",
    "CommunicationErrorResponse",
    "CommunicationIdentifierModel",
    "CommunicationUserIdentifierModel",
    "ContinuousDtmfRecognitionRequest",
    "ContinuousDtmfRecognitionStopped",
    "ContinuousDtmfRecognitionToneFailed",
    "ContinuousDtmfRecognitionToneReceived",
    "CreateCallRequest",
    "DtmfOptions",
    "DtmfResult",
    "FileSource",
    "MicrosoftTeamsUserIdentifierModel",
    "MuteParticipantsRequest",
    "MuteParticipantsResponse",
    "ParticipantsUpdated",
    "PhoneNumberIdentifierModel",
    "PlayCanceled",
    "PlayCompleted",
    "PlayFailed",
    "PlayOptions",
    "PlayRequest",
    "PlaySource",
    "RecognizeCanceled",
    "RecognizeCompleted",
    "RecognizeFailed",
    "RecognizeOptions",
    "RecognizeRequest",
    "RecordingStateChanged",
    "RecordingStateResponse",
    "RedirectCallRequest",
    "RejectCallRequest",
    "RemoveParticipantFailed",
    "RemoveParticipantRequest",
    "RemoveParticipantResponse",
    "RemoveParticipantSucceeded",
    "ResultInformation",
    "SendDtmfCompleted",
    "SendDtmfFailed",
    "SendDtmfRequest",
    "SendDtmfResponse",
    "SpeechOptions",
    "SpeechResult",
    "SsmlSource",
    "StartCallRecordingRequest",
    "TextSource",
    "ToneInfo",
    "TransferCallResponse",
    "TransferToParticipantRequest",
    "CallConnectionState",
    "CallLocatorKind",
    "CallRejectReason",
    "CommunicationCloudEnvironmentModel",
    "CommunicationIdentifierModelKind",
    "DtmfTone",
    "Gender",
    "PlaySourceType",
    "RecognitionType",
    "RecognizeInputType",
    "RecordingChannel",
    "RecordingContent",
    "RecordingFormat",
    "RecordingState",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
