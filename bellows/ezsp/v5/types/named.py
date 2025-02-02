"""Protocol version 5 named types."""

import bellows.types.basic as basic
from bellows.types.named import (  # noqa: F401, F403
    EUI64,
    Bool,
    Channels,
    EmberApsOption,
    EmberBindingType,
    EmberCertificate283k1Data,
    EmberCertificateData,
    EmberConcentratorType,
    EmberConfigTxPowerMode,
    EmberCurrentSecurityBitmask,
    EmberEventUnits,
    EmberGpKeyType,
    EmberGpSecurityLevel,
    EmberIncomingMessageType,
    EmberInitialSecurityBitmask,
    EmberJoinDecision,
    EmberJoinMethod,
    EmberKeyStatus,
    EmberKeyStructBitmask,
    EmberLibraryStatus,
    EmberMacPassthroughType,
    EmberMessageDigest,
    EmberMulticastId,
    EmberNetworkStatus,
    EmberNodeId,
    EmberNodeType,
    EmberOutgoingMessageType,
    EmberPanId,
    EmberPrivateKey283k1Data,
    EmberPrivateKeyData,
    EmberPublicKey283k1Data,
    EmberPublicKeyData,
    EmberSignature283k1Data,
    EmberSignatureData,
    EmberSmacData,
    EmberStatus,
    EmberZdoConfigurationFlags,
    EmberZllKeyIndex,
    EmberZllState,
    ExtendedPanId,
    EzspEndpointFlags,
    EzspExtendedValueId,
    EzspMfgTokenId,
    EzspNetworkScanType,
    EzspSourceRouteOverheadInformation,
    EzspStatus,
    EzspZllNetworkOperation,
    KeyData,
)


class EmberRf4ceTxOption(basic.uint8_t):
    # RF4CE transmission options.
    pass


class EmberRf4ceNodeCapabilities(basic.uint8_t):
    # The RF4CE node capabilities.
    pass


class EmberRf4ceApplicationCapabilities(basic.uint8_t):
    # The RF4CE application capabilities.
    pass


class EzspConfigId(basic.enum8):
    # Identifies a configuration value.

    # The number of packet buffers available to the stack.  When set to the
    # special value 0xFF, the NCP will allocate all remaining configuration RAM
    # towards packet buffers, such that the resulting count will be the largest
    # whole number of packet buffers that can fit into the available memory.
    CONFIG_PACKET_BUFFER_COUNT = 0x01
    # The maximum number of router neighbors the stack can keep track of. A
    # neighbor is a node within radio range.
    CONFIG_NEIGHBOR_TABLE_SIZE = 0x02
    # The maximum number of APS retried messages the stack can be transmitting
    # at any time.
    CONFIG_APS_UNICAST_MESSAGE_COUNT = 0x03
    # The maximum number of non-volatile bindings supported by the stack.
    CONFIG_BINDING_TABLE_SIZE = 0x04
    # The maximum number of EUI64 to network address associations that the
    # stack can maintain for the application. (Note, the total number of such
    # address associations maintained by the NCP is the sum of the value of
    # this setting and the value of ::CONFIG_TRUST_CENTER_ADDRESS_CACHE_SIZE).
    CONFIG_ADDRESS_TABLE_SIZE = 0x05
    # The maximum number of multicast groups that the device may be a member
    # of.
    CONFIG_MULTICAST_TABLE_SIZE = 0x06
    # The maximum number of destinations to which a node can route messages.
    # This includes both messages originating at this node and those relayed
    # for others.
    CONFIG_ROUTE_TABLE_SIZE = 0x07
    # The number of simultaneous route discoveries that a node will support.
    CONFIG_DISCOVERY_TABLE_SIZE = 0x08
    # Specifies the stack profile.
    CONFIG_STACK_PROFILE = 0x0C
    # The security level used for security at the MAC and network layers. The
    # supported values are 0 (no security) and 5 (payload is encrypted and a
    # four-byte MIC is used for authentication).
    CONFIG_SECURITY_LEVEL = 0x0D
    # The maximum number of hops for a message.
    CONFIG_MAX_HOPS = 0x10
    # The maximum number of end device children that a router will support.
    CONFIG_MAX_END_DEVICE_CHILDREN = 0x11
    # The maximum amount of time that the MAC will hold a message for indirect
    # transmission to a child.
    CONFIG_INDIRECT_TRANSMISSION_TIMEOUT = 0x12
    # The maximum amount of time that an end device child can wait between
    # polls. If no poll is heard within this timeout, then the parent removes
    # the end device from its tables.
    CONFIG_END_DEVICE_POLL_TIMEOUT = 0x13
    # The maximum amount of time that a mobile node can wait between polls. If
    # no poll is heard within this timeout, then the parent removes the mobile
    # node from its tables.
    CONFIG_MOBILE_NODE_POLL_TIMEOUT = 0x14
    # The number of child table entries reserved for use only by mobile nodes.
    CONFIG_RESERVED_MOBILE_CHILD_ENTRIES = 0x15
    # Enables boost power mode and/or the alternate transmitter output.
    CONFIG_TX_POWER_MODE = 0x17
    # 0: Allow this node to relay messages. 1: Prevent this node from relaying
    # messages.
    CONFIG_DISABLE_RELAY = 0x18
    # The maximum number of EUI64 to network address associations that the
    # Trust Center can maintain.  These address cache entries are reserved for
    # and reused by the Trust Center when processing device join/rejoin
    # authentications. This cache size limits the number of overlapping joins
    # the Trust Center can process within a narrow time window (e.g. two
    # seconds), and thus should be set to the maximum number of near
    # simultaneous joins the Trust Center is expected to accommodate. (Note,
    # the total number of such address associations maintained by the NCP is
    # the sum of the value of this setting and the value of
    # ::CONFIG_ADDRESS_TABLE_SIZE.)
    CONFIG_TRUST_CENTER_ADDRESS_CACHE_SIZE = 0x19
    # The size of the source route table.
    CONFIG_SOURCE_ROUTE_TABLE_SIZE = 0x1A
    # The units used for timing out end devices on their parents.
    CONFIG_END_DEVICE_POLL_TIMEOUT_SHIFT = 0x1B
    # The number of blocks of a fragmented message that can be sent in a single
    # window.
    CONFIG_FRAGMENT_WINDOW_SIZE = 0x1C
    # The time the stack will wait (in milliseconds) between sending blocks of
    # a fragmented message.
    CONFIG_FRAGMENT_DELAY_MS = 0x1D
    # The size of the Key Table used for storing individual link keys (if the
    # device is a Trust Center) or Application Link Keys (if the device is a
    # normal node).
    CONFIG_KEY_TABLE_SIZE = 0x1E
    # The APS ACK timeout value. The stack waits this amount of time between
    # resends of APS retried messages.
    CONFIG_APS_ACK_TIMEOUT = 0x1F
    # The duration of an active scan, in the units used by the 15.4 scan
    # parameter (((1 << duration) + 1) * 15ms). This also controls the jitter
    # used when responding to a beacon request.
    CONFIG_ACTIVE_SCAN_DURATION = 0x20
    # The time the coordinator will wait (in seconds) for a second end device
    # bind request to arrive.
    CONFIG_END_DEVICE_BIND_TIMEOUT = 0x21
    # The number of PAN id conflict reports that must be received by the
    # network manager within one minute to trigger a PAN id change.
    CONFIG_PAN_ID_CONFLICT_REPORT_THRESHOLD = 0x22
    # The timeout value in minutes for how long the Trust Center or a normal
    # node waits for the ZigBee Request Key to complete. On the Trust Center
    # this controls whether or not the device buffers the request, waiting for
    # a matching pair of ZigBee Request Key. If the value is non-zero, the
    # Trust Center buffers and waits for that amount of time. If the value is
    # zero, the Trust Center does not buffer the request and immediately
    # responds to the request.  Zero is the most compliant behavior.
    CONFIG_REQUEST_KEY_TIMEOUT = 0x24
    # This value indicates the size of the runtime modifiable certificate
    # table. Normally certificates are stored in MFG tokens but this table can
    # be used to field upgrade devices with new Smart Energy certificates.
    # This value cannot be set, it can only be queried.
    CONFIG_CERTIFICATE_TABLE_SIZE = 0x29
    # This is a bitmask that controls which incoming ZDO request messages are
    # passed to the application. The bits are defined in the
    # EmberZdoConfigurationFlags enumeration. To see if the application is
    # required to send a ZDO response in reply to an incoming message, the
    # application must check the APS options bitfield within the
    # incomingMessageHandler callback to see if the
    # APS_OPTION_ZDO_RESPONSE_REQUIRED flag is set.
    CONFIG_APPLICATION_ZDO_FLAGS = 0x2A
    # The maximum number of broadcasts during a single broadcast timeout
    # period.
    CONFIG_BROADCAST_TABLE_SIZE = 0x2B
    # The size of the MAC filter list table.
    CONFIG_MAC_FILTER_TABLE_SIZE = 0x2C
    # The number of supported networks.
    CONFIG_SUPPORTED_NETWORKS = 0x2D
    # Whether multicasts are sent to the RxOnWhenIdle=true address (0xFFFD) or
    # the sleepy broadcast address (0xFFFF). The RxOnWhenIdle=true address is
    # the ZigBee compliant destination for multicasts.
    CONFIG_SEND_MULTICASTS_TO_SLEEPY_ADDRESS = 0x2E
    # ZLL group address initial configuration.
    CONFIG_ZLL_GROUP_ADDRESSES = 0x2F
    # ZLL rssi threshold initial configuration.
    CONFIG_ZLL_RSSI_THRESHOLD = 0x30
    # The maximum number of pairings supported by the stack. Controllers
    # must support at least one pairing table entry while targets must
    # support at least five.
    CONFIG_RF4CE_PAIRING_TABLE_SIZE = 0x31
    # The maximum number of outgoing RF4CE packets supported by the stack.
    CONFIG_RF4CE_PENDING_OUTGOING_PACKET_TABLE_SIZE = 0x32
    # Toggles the mtorr flow control in the stack.
    # The maximum number of pairings supported by the stack. Controllers
    # must support at least one pairing table entry while targets must
    # support at least five.
    CONFIG_MTORR_FLOW_CONTROL = 0x33
    # Setting the retry queue size.
    CONFIG_RETRY_QUEUE_SIZE = 0x34
    # Setting the new broadcast entry threshold.
    CONFIG_NEW_BROADCAST_ENTRY_THRESHOLD = 0x35
    # The length of time, in seconds, that a trust center will store a
    # transient link key that a device can use to join its network. A transient
    # key is added with a call to emberAddTransientLinkKey. After the transient
    # key is added, it will be removed once this amount of time has passed. A
    # joining device will not be able to use that key to join until it is added
    # again on the trust center. The default value is 300 seconds, i.e., 5
    # minutes.
    CONFIG_TRANSIENT_KEY_TIMEOUT_S = 0x36
    # Whether the NCP has updated Green Power support. Both host and NCP software must
    # be updated to fully support Green Power Proxy Basic functionality. The 5.10.1 host
    # software calls new EZSP functions for Green Power.  If this configuration value is
    # not present, the host will not call the new functions.
    CONFIG_GREEN_POWER_ACTIVE = 0x37


class EzspValueId(basic.enum8):
    # Identifies a value.

    # The contents of the node data stack token.
    VALUE_TOKEN_STACK_NODE_DATA = 0x00
    # The types of MAC passthrough messages that the host wishes to receive.
    VALUE_MAC_PASSTHROUGH_FLAGS = 0x01
    # The source address used to filter legacy EmberNet messages when the
    # MAC_PASSTHROUGH_EMBERNET_SOURCE flag is set in VALUE_MAC_PASSTHROUGH_FLAGS.
    VALUE_EMBERNET_PASSTHROUGH_SOURCE_ADDRESS = 0x02
    # The number of available message buffers.
    VALUE_FREE_BUFFERS = 0x03
    # Selects sending synchronous callbacks in ezsp-uart.
    VALUE_UART_SYNCH_CALLBACKS = 0x04
    # The maximum incoming transfer size for the local node.
    VALUE_MAXIMUM_INCOMING_TRANSFER_SIZE = 0x05
    # The maximum outgoing transfer size for the local node.
    VALUE_MAXIMUM_OUTGOING_TRANSFER_SIZE = 0x06
    # A boolean indicating whether stack tokens are written to persistent
    # storage as they change.
    VALUE_STACK_TOKEN_WRITING = 0x07
    # A read-only value indicating whether the stack is currently performing a rejoin.
    VALUE_STACK_IS_PERFORMING_REJOIN = 0x08
    # A list of EmberMacFilterMatchData values.
    VALUE_MAC_FILTER_LIST = 0x09
    # The Ember Extended Security Bitmask.
    VALUE_EXTENDED_SECURITY_BITMASK = 0x0A
    # The node short ID.
    VALUE_NODE_SHORT_ID = 0x0B
    # The descriptor capability of the local node.
    VALUE_DESCRIPTOR_CAPABILITY = 0x0C
    # The stack device request sequence number of the local node.
    VALUE_STACK_DEVICE_REQUEST_SEQUENCE_NUMBER = 0x0D
    # Enable or disable radio hold-off.
    VALUE_RADIO_HOLD_OFF = 0x0E
    # The flags field associated with the endpoint data.
    VALUE_ENDPOINT_FLAGS = 0x0F
    # Enable/disable the Mfg security config key settings.
    VALUE_MFG_SECURITY_CONFIG = 0x10
    # Retrieves the version information from the stack on the NCP.
    VALUE_VERSION_INFO = 0x11
    # This will get/set the rejoin reason noted by the host for a subsequent call to
    # emberFindAndRejoinNetwork(). After a call to emberFindAndRejoinNetwork() the
    # host's rejoin reason will be set to REJOIN_REASON_NONE. The NCP will store the
    # rejoin reason used by the call to emberFindAndRejoinNetwork()
    VALUE_NEXT_HOST_REJOIN_REASON = 0x12
    # This is the reason that the last rejoin took place. This value may only be
    # retrieved, not set. The rejoin may have been initiated by the stack (NCP) or the
    # application (host). If a host initiated a rejoin the reason will be set by default
    # to REJOIN_DUE_TO_APP_EVENT_1. If the application wishes to denote its own rejoin
    # reasons it can do so by calling ezspSetValue(VALUE_HOST_REJOIN_REASON,
    # REJOIN_DUE_TO_APP_EVENT_X). X is a number corresponding to one of the app events
    # defined. If the NCP initiated a rejoin it will record this value internally for
    # retrieval by ezspGetValue(VALUE_REAL_REJOIN_REASON).
    VALUE_LAST_REJOIN_REASON = 0x13
    # The next ZigBee sequence number.
    VALUE_NEXT_ZIGBEE_SEQUENCE_NUMBER = 0x14
    # CCA energy detect threshold for radio.
    VALUE_CCA_THRESHOLD = 0x15
    # The RF4CE discovery LQI threshold parameter.
    VALUE_RF4CE_DISCOVERY_LQI_THRESHOLD = 0x16
    # The threshold value for a counter
    VALUE_SET_COUNTER_THRESHOLD = 0x17
    # Resets all counters thresholds to 0xFF
    VALUE_RESET_COUNTER_THRESHOLDS = 0x18
    # Clears all the counters
    VALUE_CLEAR_COUNTERS = 0x19
    # The node's new certificate signed by the CA.
    VALUE_CERTIFICATE_283K1 = 0x1A
    # The Certificate Authority's public key.
    VALUE_PUBLIC_KEY_283K1 = 0x1B
    # The node's new static private key.
    VALUE_PRIVATE_KEY_283K1 = 0x1C
    # The GDP binding recipient parameters
    VALUE_RF4CE_GDP_BINDING_RECIPIENT_PARAMETERS = 0x1D
    # The GDP binding push button stimulus received pending flag
    VALUE_RF4CE_GDP_PUSH_BUTTON_STIMULUS_RECEIVED_PENDING_FLAG = 0x1E
    # The GDP originator proxy flag in the advanced binding options
    VALUE_RF4CE_GDP_BINDING_PROXY_FLAG = 0x1F
    # 0x21 The MSO user string
    VALUE_RF4CE_GDP_APPLICATION_SPECIFIC_USER_STRING = 0x20
    # The MSO user string
    VALUE_RF4CE_MSO_USER_STRING = 0x21
    # The MSO binding recipient parameters
    VALUE_RF4CE_MSO_BINDING_RECIPIENT_PARAMETERS = 0x22
    # The NWK layer security frame counter value
    VALUE_NWK_FRAME_COUNTER = 0x23
    # The APS layer security frame counter value
    VALUE_APS_FRAME_COUNTER = 0x24
    # Sets the device type to use on the next rejoin using device type
    VALUE_RETRY_DEVICE_TYPE = 0x25
    # The device RF4CE base channel
    VALUE_RF4CE_BASE_CHANNEL = 0x26
    # The RF4CE device types supported by the node
    VALUE_RF4CE_SUPPORTED_DEVICE_TYPES_LIST = 0x27
    # The RF4CE profiles supported by the node
    VALUE_RF4CE_SUPPORTED_PROFILES_LIST = 0x28
    # Setting this byte enables R21 behavior on the NCP.
    VALUE_ENABLE_R21_BEHAVIOR = 0x29
    # Configure the antenna mode(0-primary,1-secondary,2- toggle on tx ack fail).
    VALUE_ANTENNA_MODE = 0x30
    # Enable or disable packet traffic arbitration.
    VALUE_ENABLE_PTA = 0x31
    # Set packet traffic arbitration configuration options.
    VALUE_PTA_OPTIONS = 0x32
    # Configure manufacturing library options(0-non-CSMA transmits,1-CSMA transmits).
    VALUE_MFGLIB_OPTIONS = 0x33


class EzspPolicyId(basic.enum8):
    # Identifies a policy.

    # Controls trust center behavior.
    TRUST_CENTER_POLICY = 0x00
    # Controls how external binding modification requests are handled.
    BINDING_MODIFICATION_POLICY = 0x01
    # Controls whether the Host supplies unicast replies.
    UNICAST_REPLIES_POLICY = 0x02
    # Controls whether pollHandler callbacks are generated.
    POLL_HANDLER_POLICY = 0x03
    # Controls whether the message contents are included in the
    # messageSentHandler callback.
    MESSAGE_CONTENTS_IN_CALLBACK_POLICY = 0x04
    # Controls whether the Trust Center will respond to Trust Center link key
    # requests.
    TC_KEY_REQUEST_POLICY = 0x05
    # Controls whether the Trust Center will respond to application link key
    # requests.
    APP_KEY_REQUEST_POLICY = 0x06
    # Controls whether ZigBee packets that appear invalid are automatically
    # dropped by the stack. A counter will be incremented when this occurs.
    PACKET_VALIDATE_LIBRARY_POLICY = 0x07
    # Controls whether the stack will process ZLL messages.
    ZLL_POLICY = 0x08
    # Controls whether the ZigBee RF4CE stack will use standard profile-dependent
    # behavior during the discovery and pairing process. The profiles supported at the
    # NCP at the moment are ZRC 1.1 and MSO. If this policy is enabled the stack will
    # use standard behavior for the profiles ZRC 1.1 and MSO while it will fall back to
    # the on/off RF4CE policies for other profiles. If this policy is disabled the
    # on/off RF4CE policies are used for all profiles.
    RF4CE_DISCOVERY_AND_PAIRING_PROFILE_BEHAVIOR_POLICY = 0x09
    # Controls whether the ZigBee RF4CE stack will respond to an incoming discovery
    # request or not.
    RF4CE_DISCOVERY_REQUEST_POLICY = 0x0A
    # Controls the behavior of the ZigBee RF4CE stack discovery process.
    RF4CE_DISCOVERY_POLICY = 0x0B
    # Controls whether the ZigBee RF4CE stack will accept or deny a pair request.
    RF4CE_PAIR_REQUEST_POLICY = 0x0C


class EzspDecisionId(basic.enum8):
    # Identifies a policy decision.

    # Send the network key in the clear to all joining and rejoining devices.
    ALLOW_JOINS = 0x00
    # Send the network key in the clear to all joining devices.  Rejoining
    # devices are sent the network key encrypted with their trust center link
    # key. The trust center and any rejoining device are assumed to share a
    # link key, either preconfigured or obtained under a previous policy.
    ALLOW_JOINS_REJOINS_HAVE_LINK_KEY = 0x04
    # Send the network key encrypted with the joining or rejoining device's
    # trust center link key. The trust center and any joining or rejoining
    # device are assumed to share a link key, either preconfigured or obtained
    # under a previous policy. This is the default value for the
    # TRUST_CENTER_POLICY.
    ALLOW_PRECONFIGURED_KEY_JOINS = 0x01
    # Send the network key encrypted with the rejoining device's trust center
    # link key. The trust center and any rejoining device are assumed to share
    # a link key, either preconfigured or obtained under a previous policy. No
    # new devices are allowed to join.
    ALLOW_REJOINS_ONLY = 0x02
    # Reject all unsecured join and rejoin attempts.
    DISALLOW_ALL_JOINS_AND_REJOINS = 0x03
    # Take no action on trust center rejoin attempts.
    IGNORE_TRUST_CENTER_REJOINS = 0x05
    # BINDING_MODIFICATION_POLICY default decision. Do not allow the local
    # binding table to be changed by remote nodes.
    DISALLOW_BINDING_MODIFICATION = 0x10
    # BINDING_MODIFICATION_POLICY decision.  Allow remote nodes to change
    # the local binding table.
    ALLOW_BINDING_MODIFICATION = 0x11
    # BINDING_MODIFICATION_POLICY decision.  Allows remote nodes to set local
    # binding entries only if the entries correspond to endpoints defined on
    # the device, and for output clusters bound to those endpoints.
    CHECK_BINDING_MODIFICATIONS_ARE_VALID_ENDPOINT_CLUSTERS = 0x12
    # UNICAST_REPLIES_POLICY default decision.  The NCP will automatically send
    # an empty reply (containing no payload) for every unicast received.
    HOST_WILL_NOT_SUPPLY_REPLY = 0x20
    # UNICAST_REPLIES_POLICY decision. The NCP will only send a reply if it
    # receives a sendReply command from the Host.
    HOST_WILL_SUPPLY_REPLY = 0x21
    # POLL_HANDLER_POLICY default decision. Do not inform the Host when a child polls.
    POLL_HANDLER_IGNORE = 0x30
    # POLL_HANDLER_POLICY decision. Generate a pollHandler callback when a child polls.
    POLL_HANDLER_CALLBACK = 0x31
    # MESSAGE_CONTENTS_IN_CALLBACK_POLICY default decision. Include only the
    # message tag in the messageSentHandler callback.
    MESSAGE_TAG_ONLY_IN_CALLBACK = 0x40
    # MESSAGE_CONTENTS_IN_CALLBACK_POLICY decision. Include both the message
    # tag and the message contents in the messageSentHandler callback.
    MESSAGE_TAG_AND_CONTENTS_IN_CALLBACK = 0x41
    # TC_KEY_REQUEST_POLICY decision. When the Trust Center receives a request
    # for a Trust Center link key, it will be ignored.
    DENY_TC_KEY_REQUESTS = 0x50
    # TC_KEY_REQUEST_POLICY decision. When the Trust Center receives a request for a
    # Trust Center link key, it will reply to it with the corresponding key.
    ALLOW_TC_KEY_REQUESTS = 0x51
    # TC_KEY_REQUEST_POLICY decision. When the Trust Center receives a request
    # for a Trust Center link key, it will generate a key to send to the joiner.
    GENERATE_NEW_TC_LINK_KEY = 0x52
    # APP_KEY_REQUEST_POLICY decision. When the Trust Center receives a request
    # for an application link key, it will be ignored.
    DENY_APP_KEY_REQUESTS = 0x60
    # APP_KEY_REQUEST_POLICY decision. When the Trust Center receives a request
    # for an application link key, it will randomly generate a key and send it
    # to both partners.
    ALLOW_APP_KEY_REQUESTS = 0x61
    # Indicates that packet validate library checks are enabled on the NCP.
    PACKET_VALIDATE_LIBRARY_CHECKS_ENABLED = 0x62
    # Indicates that packet validate library checks are NOT enabled on the NCP.
    PACKET_VALIDATE_LIBRARY_CHECKS_DISABLED = 0x63
    # Indicates that the RF4CE stack during discovery and pairing will use standard
    # profile-dependent behavior for the profiles ZRC 1.1 and MSO, while it will fall
    # back to the on/off policies for any other profile.
    RF4CE_DISCOVERY_AND_PAIRING_PROFILE_BEHAVIOR_ENABLED = 0x70
    # Indicates that the RF4CE stack during discovery and pairing will always use the
    # on/off policies.
    RF4CE_DISCOVERY_AND_PAIRING_PROFILE_BEHAVIOR_DISABLED = 0x71
    # Indicates that the RF4CE stack will respond to incoming discovery requests.
    RF4CE_DISCOVERY_REQUEST_RESPOND = 0x72
    # Indicates that the RF4CE stack will ignore incoming discovery requests.
    RF4CE_DISCOVERY_REQUEST_IGNORE = 0x73
    # Indicates that the RF4CE stack will perform all the discovery trials the
    # application specified in the ezspRf4ceDiscovery() call.
    RF4CE_DISCOVERY_MAX_DISCOVERY_TRIALS = 0x74
    # Indicates that the RF4CE stack will prematurely stop the discovery process if a
    # matching discovery response is received.
    RF4CE_DISCOVERY_STOP_ON_MATCHING_RESPONSE = 0x75
    # Indicates that the RF4CE stack will accept new pairings.
    RF4CE_PAIR_REQUEST_ACCEPT = 0x76
    # Indicates that the RF4CE stack will NOT accept new pairings.
    RF4CE_PAIR_REQUEST_DENY = 0x77


class EmberKeyType(basic.enum8):
    # Describes the type of ZigBee security key.

    # A shared key between the Trust Center and a device.
    TRUST_CENTER_LINK_KEY = 0x01
    # A shared secret used for deriving keys between the Trust Center and a
    # device
    TRUST_CENTER_MASTER_KEY = 0x02
    # The current active Network Key used by all devices in the network.
    CURRENT_NETWORK_KEY = 0x03
    # The alternate Network Key that was previously in use, or the newer key
    # that will be switched to.
    NEXT_NETWORK_KEY = 0x04
    # An Application Link Key shared with another (non-Trust Center) device.
    APPLICATION_LINK_KEY = 0x05
    # An Application Master Key shared secret used to derive an Application
    # Link Key.
    APPLICATION_MASTER_KEY = 0x06


class EmberDeviceUpdate(basic.enum8):
    # The status of the device update.

    STANDARD_SECURITY_SECURED_REJOIN = 0x0
    STANDARD_SECURITY_UNSECURED_JOIN = 0x1
    DEVICE_LEFT = 0x2
    STANDARD_SECURITY_UNSECURED_REJOIN = 0x3


class EmberCounterType(basic.enum8):
    # Defines the events reported to the application by the
    # readAndClearCounters command.

    # The MAC received a broadcast.
    COUNTER_MAC_RX_BROADCAST = 0
    # The MAC transmitted a broadcast.
    COUNTER_MAC_TX_BROADCAST = 1
    # The MAC received a unicast.
    COUNTER_MAC_RX_UNICAST = 2
    # The MAC successfully transmitted a unicast.
    COUNTER_MAC_TX_UNICAST_SUCCESS = 3
    # The MAC retried a unicast.
    COUNTER_MAC_TX_UNICAST_RETRY = 4
    # The MAC unsuccessfully transmitted a unicast.
    COUNTER_MAC_TX_UNICAST_FAILED = 5
    # The APS layer received a data broadcast.
    COUNTER_APS_DATA_RX_BROADCAST = 6
    # The APS layer transmitted a data broadcast.
    COUNTER_APS_DATA_TX_BROADCAST = 7
    # The APS layer received a data unicast.
    COUNTER_APS_DATA_RX_UNICAST = 8
    # The APS layer successfully transmitted a data unicast.
    COUNTER_APS_DATA_TX_UNICAST_SUCCESS = 9
    # The APS layer retried a data unicast.
    COUNTER_APS_DATA_TX_UNICAST_RETRY = 10
    # The APS layer unsuccessfully transmitted a data unicast.
    COUNTER_APS_DATA_TX_UNICAST_FAILED = 11
    # The network layer successfully submitted a new route discovery to the MAC.
    COUNTER_ROUTE_DISCOVERY_INITIATED = 12
    # An entry was added to the neighbor table.
    COUNTER_NEIGHBOR_ADDED = 13
    # An entry was removed from the neighbor table.
    COUNTER_NEIGHBOR_REMOVED = 14
    # A neighbor table entry became stale because it had not been heard from.
    COUNTER_NEIGHBOR_STALE = 15
    # A node joined or rejoined to the network via this node.
    COUNTER_JOIN_INDICATION = 16
    # An entry was removed from the child table.
    COUNTER_CHILD_REMOVED = 17
    # EZSP-UART only. An overflow error occurred in the UART.
    COUNTER_ASH_OVERFLOW_ERROR = 18
    # EZSP-UART only. A framing error occurred in the UART.
    COUNTER_ASH_FRAMING_ERROR = 19
    # EZSP-UART only. An overrun error occurred in the UART.
    COUNTER_ASH_OVERRUN_ERROR = 20
    # A message was dropped at the network layer because the NWK frame counter
    # was not higher than the last message seen from that source.
    COUNTER_NWK_FRAME_COUNTER_FAILURE = 21
    # A message was dropped at the APS layer because the APS frame counter was
    # not higher than the last message seen from that source.
    COUNTER_APS_FRAME_COUNTER_FAILURE = 22
    # Utility counter for general debugging use.
    COUNTER_UTILITY = 23
    # A message was dropped at the APS layer because it had APS encryption but
    # the key associated with the sender has not been authenticated, and thus
    # the key is not authorized for use in APS data messages.
    COUNTER_APS_LINK_KEY_NOT_AUTHORIZED = 24
    # A NWK encrypted message was received but dropped because decryption
    # failed.
    COUNTER_NWK_DECRYPTION_FAILURE = 25
    # An APS encrypted message was received but dropped because decryption
    # failed.
    COUNTER_APS_DECRYPTION_FAILURE = 26
    # The number of times we failed to allocate a set of linked packet buffers.
    # This doesn't necessarily mean that the packet buffer count was 0 at the
    # time, but that the number requested was greater than the number free.
    COUNTER_ALLOCATE_PACKET_BUFFER_FAILURE = 27
    # The number of relayed unicast packets.
    COUNTER_RELAYED_UNICAST = 28
    # The number of times we dropped a packet due to reaching
    # the preset PHY to MAC queue limit (emMaxPhyToMacQueueLength).
    COUNTER_PHY_TO_MAC_QUEUE_LIMIT_REACHED = 29
    # The number of times we dropped a packet due to the
    # packet-validate library checking a packet and rejecting it
    # due to length or other formatting problems.
    COUNTER_PACKET_VALIDATE_LIBRARY_DROPPED_COUNT = 30
    # The number of times the NWK retry queue is full and a
    # new message failed to be added.
    COUNTER_TYPE_NWK_RETRY_OVERFLOW = 31
    # The number of times the PHY layer was unable to transmit
    # due to a failed CCA.
    COUNTER_PHY_CCA_FAIL_COUNT = 32
    # The number of times a NWK broadcast was dropped because
    # the broadcast table was full.
    COUNTER_BROADCAST_TABLE_FULL = 33
    # The number of low priority packet traffic arbitration requests.
    COUNTER_PTA_LO_PRI_REQUESTED = 34
    # The number of high priority packet traffic arbitration requests.
    COUNTER_PTA_HI_PRI_REQUESTED = 35
    # The number of low priority packet traffic arbitration requests denied.
    COUNTER_PTA_LO_PRI_DENIED = 36
    # The number of high priority packet traffic arbitration requests denied.
    COUNTER_PTA_HI_PRI_DENIED = 37
    # The number of aborted low priority packet traffic arbitration transmissions.
    COUNTER_PTA_LO_PRI_TX_ABORTED = 38
    # The number of aborted high priority packet traffic arbitration transmissions.
    COUNTER_PTA_HI_PRI_TX_ABORTED = 39


class EmberNetworkInitBitmask(basic.bitmap16):
    # Bitmask options for emberNetworkInit().

    # No options for Network Init
    NETWORK_INIT_NO_OPTIONS = 0x0000
    # Save parent info (node ID and EUI64) in a token during joining/rejoin,
    # and restore on reboot.
    NETWORK_INIT_PARENT_INFO_IN_TOKEN = 0x0001


EmberNetworkInitStruct = EmberNetworkInitBitmask


class SecureEzspSecurityType(basic.uint32_t):
    """Security type of the Secure EZSP Protocol."""


class SecureEzspSecurityLevel(basic.uint8_t):
    """Security level of the Secure EZSP Protocol."""


class SecureEzspRandomNumber(basic.FixedList[basic.uint8_t, 16]):
    """Randomly generated 64-bit number.

    Both NCP and Host contribute this number to create the Session ID,
    which is used in the nonce.
    """


class SecureEzspSessionId(basic.FixedList[basic.uint8_t, 8]):
    """Generated 64-bit Session ID, using random numbers from Host and NCP.

    It is generated at each reboot (during negotiation phase). Having both sides
    contribute to the value prevents one side from choosing a number that might have
    been previously used (either because of a bug or by malicious intent).
    """
