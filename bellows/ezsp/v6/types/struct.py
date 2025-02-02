"""Protocol version 6 specific structs."""

import bellows.types.basic as basic
from bellows.types.struct import (  # noqa: F401
    EmberAesMmoHashContext,
    EmberApsFrame,
    EmberBindingTableEntry,
    EmberCurrentSecurityState,
    EmberGpAddress,
    EmberInitialSecurityState,
    EmberMulticastTableEntry,
    EmberNeighborTableEntry,
    EmberNetworkParameters,
    EmberRouteTableEntry,
    EmberTokTypeStackZllData,
    EmberTokTypeStackZllSecurity,
    EmberTransientKeyData,
    EmberZigbeeNetwork,
    EmberZllAddressAssignment,
    EmberZllDeviceInfoRecord,
    EmberZllInitialSecurityState,
    EmberZllNetwork,
    EmberZllSecurityAlgorithmData,
    EzspStruct,
)

from . import named


class EmberKeyStruct(EzspStruct):
    # A structure containing a key and its associated data.
    # A bitmask indicating the presence of data within the various fields
    # in the structure.
    bitmask: named.EmberKeyStructBitmask
    # The type of the key.
    type: named.EmberKeyType
    # The actual key data.
    key: named.KeyData
    # The outgoing frame counter associated with the key.
    outgoingFrameCounter: basic.uint32_t
    # The frame counter of the partner device associated with the key.
    incomingFrameCounter: basic.uint32_t
    # The sequence number associated with the key.
    sequenceNumber: basic.uint8_t
    # The IEEE address of the partner device also in possession of the key.
    partnerEUI64: named.EUI64


class EmberGpSinkListEntry(EzspStruct):
    # A sink list entry
    # The sink list type.
    type: basic.uint8_t
    # The EUI64 of the target sink.
    sinkEUI: named.EUI64
    # The short address of the target sink.
    sinkNodeId: named.EmberNodeId


class EmberGpProxyTableEntry(EzspStruct):
    """The internal representation of a proxy table entry."""

    # The link key to be used to secure this pairing link.
    securityLinkKey: named.KeyData
    # Internal status of the proxy table entry.
    status: named.EmberGpProxyTableEntryStatus
    # The tunneling options
    # (this contains both options and extendedOptions from the spec).
    options: basic.uint32_t
    # The addressing info of the GPD.
    gpd: EmberGpAddress
    # The assigned alias for the GPD.
    assignedAlias: named.EmberNodeId
    # The security options field.
    securityOptions: basic.uint8_t
    # The security frame counter of the GPD.
    gpdSecurityFrameCounter: named.EmberGpSecurityFrameCounter
    # The key to use for GPD.
    gpdKey: named.KeyData
    # The list of sinks (hardcoded to 2 which is the spec minimum).
    sinkList: basic.FixedList[EmberGpSinkListEntry, 2]
    # The groupcast radius.
    groupcastRadius: basic.uint8_t
    # The search counter
    searchCounter: basic.uint8_t


class EmberGpSinkTableEntry(EzspStruct):
    """The internal representation of a sink table entry."""

    # Internal status of the sink table entry
    status: named.EmberGpSinkTableEntryStatus
    # The tunneling options
    # (this contains both options and extendedOptions from the spec).
    options: basic.uint32_t
    # The addressing info of the GPD.
    gpd: EmberGpAddress
    # The device id for the GPD.
    deviceId: basic.uint8_t
    # The list of sinks (hardcoded to 2 which is the spec minimum).
    sinkList: basic.FixedList[EmberGpSinkListEntry, 2]
    # The assigned alias for the GPD.
    assignedAlias: named.EmberNodeId
    # The groupcast radius.
    groupcastRadius: basic.uint8_t
    # The security options field.
    securityOptions: basic.uint8_t
    # The security frame counter of the GPD.
    gpdSecurityFrameCounter: named.EmberGpSecurityFrameCounter
    # The key to use for GPD.
    gpdKey: named.KeyData


class EmberDutyCycleLimits(EzspStruct):
    """A structure containing duty cycle limit configurations.

    All limits are absolute, and are required to be as follows:
    suspLimit > critThresh > limitThresh
    For example:
    suspLimit = 250 (2.5%), critThresh = 180 (1.8%), limitThresh 100 (1.00%).
    """

    # The vendor identifier field shall contain the vendor identifier of the node.
    vendorId: basic.uint16_t
    # The vendor string field shall contain the vendor string of the node.
    vendorString: basic.FixedList[basic.uint8_t, 7]


class EmberPerDeviceDutyCycle(EzspStruct):
    """A structure containing per device overall duty cycle consumed

    up to the suspend limit).
    """

    # Node Id of device whose duty cycle is reported.
    nodeId: named.EmberNodeId
    # Amount of overall duty cycle consumed (up to suspend limit).
    dutyCycleConsumed: named.EmberDutyCycleHectoPct
