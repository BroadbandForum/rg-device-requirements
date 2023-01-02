!include cover-page.md

!include wt-notice.md

!include front-matter.md

# Executive Summary {#executive-summary .unnumbered .unlisted .new-page}

%bbfNumber% specifies a superset of requirements for broadband
Residential Gateway (RG) devices that are capable of supporting a full
suite of voice, data, broadcast video, video on demand and two-way video
applications in broadband networks.

The requirements are grouped into modules. This means that an RG can be
specified by listing the modules that the RG is expected to support. No
single device is expected to support all modules.

Requirements are sometimes modified when a new TR-124 revision is
created. It is therefore necessary for any identification of modules
supported (or to be supported) by a RG also note which TR-124 revision
was used to generate the module list.

TR-124 Issue 2 updated TR-124 Issue 1 to include requirements for IPv6.

TR-124 Issue 3 clarifies and corrects TR-124 Issue 2 and defines new
profiles.

TR-124 Issue 4 defines several new profiles.

TR-124 Issue 5:

-   takes into account the deprecation of TR-064 Issue 1 in favor of
    Issue 2 (adding the MGMT.LOCAL.TR-064 profile and fixing text in
    several places),

-   takes into account the deprecation by UPnP Forum of UPnP IGD V1.0 in
    favor of UPnP IGD V2.0,

-   defines the new WAN.TRANS.MAP-E profile for MAP-E support.

TR-124 Issue 6:

-   Adds security requirements for RGs
-   Adds requirements for G.fast enabled RGs
-   Adds requirements for TWAMP performance measurement
-   Adds requirements for 5G-RG in Wireless-Wireline Convergence (WWC)
    architecture

TR-124 Issue 7:

-   Updates the 5G-WWC requirements and adds two new IF requirements for
    fixed RGs with LTE or NR interfaces.
-   Adds SEC.FIRMWARE for firmware authentication and encryption
    requirements.

# Purpose and Scope {#purpose-and-scope .new-page}

## Purpose

%bbfNumber% presents a superset of requirements for broadband
Residential Gateway devices that are capable of supporting a full suite
of voice, data, broadcast video, video on demand and two-way video
applications in broadband networks.

## Scope

A Residential Gateway implementing the general requirements of
%bbfNumber% will incorporate at least one embedded WAN interface,
routing, bridging, a basic or enhanced firewall, one or multiple LAN
interfaces and home networking functionality that can be deployed as a
consumer self-installable device.

%bbfNumber% specifies a baseline of Residential Gateway device and
application functions needed to support service delivery in routed and
bridged broadband network architectures. Devices can be specified that
will operate on any of the different types of Broadband Forum defined
network architectures. This allows service providers to configure a
Residential Gateway supporting specified %bbfNumber% modular
requirements locally via TR-064i2 and Web Graphical User Interface or
remotely via TR-069.

%bbfNumber% provides optional requirements modules for various physical
broadband interfaces (e.g. xDSL, Ethernet, GPON) and home networking
(LAN) interfaces that may be implemented on Residential Gateways to meet
local service provider needs. Furthermore, to accommodate common
region-specific service provider requirements that do not apply
globally, additional regional annexes are included in the %bbfNumber%
requirements that may be included in region-specific product profiles
(e.g. North American Power and Environmental requirements).

It is intended that these general requirements modules and WAN/LAN
interface modules can be used as references to define a specific product
implementation that may be needed in future Broadband Forum Technical
Reports. This checklist style product profile approach (shown in the
"[Product Profile Template](#product-profile-template-1)" section in
[APPENDIX VI](#product-profile-template-1) is intended to provide an
easy mechanism to define a specific product that is needed by region or
by service providers. An example of such a product profile is TR-068
*Base Requirements for an ADSL Modem with Routing*, which refers to
TR-124 feature modules and regional annexes.

These requirements are both backward and forward-looking. They attempt
to address the needs of current DSL services and architectures as well
as starting to address future needs. Some requirements have been
included in support of TR-059, TR-064i2, TR-069, TR-101i2 and TR-122.
Any CPE that claims to be compliant with these technical requirements
must meet the requirements that reference those documents. It is
understood that a CPE that does not claim to be compliant with these
referenced requirements may or may not meet any or all of these
requirements. On a periodic basis, new general requirements and physical
interface modules may be added in future revisions of TR-124.

Requirements are sometimes modified when a new TR-124 revision is
created. It is therefore necessary for any identification of modules
supported (or to be supported) by a RG also note which TR-124 revision
was used to generate the module list.

# References and Terminology {#references-and-terminology .new-page}

## Conventions

In this %bbfType%, several words are used to signify the requirements of
the specification. These words are always capitalized.

  -----------------------------------------------------------------------
  **MUST**       This word, or the term "REQUIRED", means that the
                 definition is an absolute requirement of the
                 specification.
  -------------- --------------------------------------------------------
  **MUST NOT**   This phrase means that the definition is an absolute
                 prohibition of the specification.

  **SHOULD**     This word, or the term "RECOMMENDED", means that there
                 could exist valid reasons in particular circumstances to
                 ignore this item, but the full implications need to be
                 understood and carefully weighed before choosing a
                 different course.

  **SHOULD NOT** This phrase, or the phrase "NOT RECOMMENDED" means that
                 there could exist valid reasons in particular
                 circumstances when the particular behavior is acceptable
                 or even useful, but the full implications need to be
                 understood and the case carefully weighed before
                 implementing any behavior described with this label.

  **MAY**        This word, or the term "OPTIONAL", means that this item
                 is one of an allowed set of alternatives. An
                 implementation that does not include this option MUST be
                 prepared to inter-operate with another implementation
                 that does include the option.

  **By Default** These words indicate that this is a default setting or
                 operation of the unit that MUST be configurable if
                 provided. This term is not included in RFC 2119
                 \[\[58\]\]\[{{ref\|\_Ref245276168}}\]**.**
  -----------------------------------------------------------------------

Other residential gateway type features not identified in this document
may also be implemented in the device. An implementation that includes
features not identified in this document must be prepared to
inter-operate with implementations that do not include these features.

References to CPE or LAN devices indicate other equipment such as hosts
including PCs and workstations.

In certain cases, %bbfNumber% generically refers to new LAN or WAN
interface performance monitoring data parameters that have not been
specifically defined in the requirements at the time of the publishing
of this document. As these requirements are not yet defined, it is
expected that vendors may support parameter extensions and basic
interface traffic performance statistics until such a time that the
Broadband Forum defines further Technical Reports to support new
interface parameter data models for possible use with TR-064i2, TR-069
and the Web GUI.

## References {#references .new-page}

The following references constitute provisions of this %bbfType%. At the
time of publication, the editions indicated were valid. All references
are subject to revision; users of this %bbfType% are therefore
encouraged to investigate the possibility of applying the most recent
edition of the references listed below.

A list of currently valid Broadband Forum Technical Reports is published
at [www.broadband-forum.org](http://www.broadband-forum.org).

NOTE -- A number of IETF drafts are cited in this document. Due to the
fact that home networking standards and technology are still being
rapidly developed, this was considered necessary. If subsequent drafts
or RFCs are published, they will obsolete the draft cited in this
document.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Document                                             Title                                                                                          Source     Year
  ---------------------------------------------------- ---------------------------------------------------------------------------------------------- ---------- ------
  #\. ANSI/TIA-968-B                                   *Telecommunications -- Telephone Terminal Equipment -- Technical Requirements for Connection   ANSI/TIA   2012
                                                       of Terminal Equipment to the Telephone Network*                                                           

  #\. TR-059                                           *DSL Evolution -- Architecture Requirements for the Support of QoS-Enabled IP Services*        BBF        2003

  #\. TR-062                                           *Auto-Config for the Connection Between the DSL Broadband Network Termination (B-NT) and the   BBF        2003
                                                       Network using ATM (TR-037 update)*                                                                        

  #\. TR-064 Issue 2                                   *LAN-Side CPE Configuration Specification*                                                     BBF        2015

  #\. TR-067 Issue 2                                   *ADSL Interop Test Plan (formerly TR-048)*                                                     BBF        2006

  #\. TR-068 Issue 3                                   *Base requirement for an ADSL Modem with Routing*                                              BBF        2006

  #\. TR-069 Amendment 5                               *CPE WAN Management Protocol*                                                                  BBF        2013

  #\. TR-101 Issue 2                                   *Migration to Ethernet Based Broadband Aggregation*                                            BBF        2011

  #\. TR-106 Amendment 7                               *Data Model Template for TR-069-Enabled Devices*                                               BBF        2013

  #\. TR-114 Issue 2                                   *VDSL2 Performance Test Plan*                                                                  BBF        2012

  #\. TR-115 Issue 2                                   *VDSL2 Functionality Test Plan*                                                                BBF        2012

  #\. TR-122 Amendment 1                               *Base Requirements for Consumer-Oriented Analog Terminal Adapter Functionality*                BBF        2006

  #\. TR-142 Issue 2                                   *Framework for TR-069 enabled PON Devices*                                                     BBF        2010

  #\. TR-181                                           *Device Data Model*                                                                            BBF        2018

  #\.                                                  *TR-069 Device:2 Root Data Model definition for CWMP*                                          BBF        2017
  \[tr-181-2-xx-cwmp-full.xml\]\[{{ref\|Device:2}}\]                                                                                                             

  #\.                                                  *TR-069 Device:2 Root Data Model definition for USP*                                           BBF        2018
  \[tr-181-2-xx-usp-full.xml\]\[{{ref\|Device:2}}\]                                                                                                              

  #\. TR-328                                           *Virtual Business Gateway*                                                                     BBF        2017

  #\. TR-369                                           *User Services Platform (USP)*                                                                 BBF        2018

  #\. FCC Part 15                                      *FCC Rules and Regulations Part 15 - Radio Frequency Devices*                                  FCC        

  #\. FCC Part 68                                      *FCC Rules and Regulations Part 68 - Connection of Terminal Equipment to the Telephone         FCC        
                                                       Network*                                                                                                  

  #\. EN61000-4-4:2004                                 *Electromagnetic compatibility (EMC). Testing and measurement techniques.*                     IEC        2005

  #\. EN61000-4-5: 1995                                *Electromagnetic compatibility (EMC). Testing and measurement techniques. Surge immunity       IEC        1995
                                                       test.*                                                                                                    

  #\. 802.1D                                           *IEEE standard for local and metropolitan area networks--Media access control (MAC) Bridges*   IEEE       2004

  #\. 802.1Q                                           *IEEE Standards for Local and metropolitan area networks---Virtual Bridged Local Area          IEEE       2011
                                                       Networks*                                                                                                 

  #\. 802.1X                                           *IEEE Standard for Local and metropolitan area networks -- Port-Based Network Access Control*  IEEE       2010

  #\. 802.3                                            *IEEE standard for information technology -- Telecommunications and information exchange       IEEE       2012
                                                       between systems -- Local and metropolitan area networks -- Specific requirements Part 3:                  
                                                       Carrier sense multiple access with collision detection (CSMA/CD) access method and physical               
                                                       layer specifications*                                                                                     

  #\. 802.11                                           *Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications*             IEEE       2012

  #\. RFC 768                                          *User Datagram Protocol*                                                                       IETF       1980

  #\. RFC 791                                          *Internet Protocol*                                                                            IETF       1981

  #\. RFC 792                                          *Internet Control Message Protocol*                                                            IETF       1981

  #\. RFC 793                                          *Transmission Control Protocol*                                                                IETF       1981

  #\. RFC 826                                          *An Ethernet Address Resolution Protocol*                                                      IETF       1982

  #\. RFC 894                                          *A Standard for the Transmission of IP Datagrams over Ethernet Networks*                       IETF       1984

  #\. RFC 922                                          *Broadcasting Internet datagrams in the presence of subnets*                                   IETF       1984

  #\. RFC 950                                          *Internet standard subnetting procedure*                                                       IETF       1985

  #\. RFC 959                                          *File Transfer Protocol* *(FTP)*                                                               IETF       1985

  #\. RFC 1034                                         *Domain Names - Concepts and Facilities*                                                       IETF       1987

  #\. RFC 1035                                         *Domain Names - Implementation and Specification*                                              IETF       1987

  #\. RFC 1042                                         *A Standard for the Transmission of IP Datagrams over IEEE 802 Networks*                       IETF       1988

  #\. RFC 1112                                         *Host Extensions for IP Multicasting*                                                          IETF       1989

  #\. RFC 1122                                         *Requirements for Internet Hosts -- Communication Layers*                                      IETF       1989

  #\. RFC 1123                                         *Requirements for Internet Hosts -- Application and Support*                                   IETF       1989

  #\. RFC 1191                                         *Path MTU Discovery*                                                                           IETF       1990

  #\. RFC 1256                                         *ICMP Router Discovery Messages*                                                               IETF       1991

  #\. RFC 1305                                         *Network Time Protocol (Version 3) Specification, Implementation and Analysis*                 IETF       1992

  #\. RFC 1332                                         *The PPP Internet Protocol Control Protocol (IPCP)*                                            IETF       1992

  #\. RFC 1334                                         *PPP Authentication Protocols (PAP)*                                                           IETF       1992

  #\. RFC 1570                                         *PPP LCP Extensions*                                                                           IETF       1994

  #\. RFC 1661                                         *The Point-to-Point Protocol (PPP)*                                                            IETF       1994

  #\. RFC 1812                                         *Requirements for IP Version 4 Routers*                                                        IETF       1995

  #\. RFC 1867                                         *Form-based File Upload in HTML*                                                               IETF       1995

  #\. RFC 1877                                         *PPP Internet Protocol Control Protocol Extensions for Name Server Addresses*                  IETF       1995

  #\. RFC 1918                                         *Address Allocation for Private Internets*                                                     IETF       1996

  #\. RFC 1928                                         *SOCKS Protocol Version 5*                                                                     IETF       1996

  #\. RFC 1990                                         *The PPP Multilink Protocol (MP)*                                                              IETF       1996

  #\. RFC 1994                                         *PPP Challenge Handshake Authentication Protocol (CHAP)*                                       IETF       1996

  #\. RFC 2091                                         *Triggered Extensions to RIP to Support Demand Circuits*                                       IETF       1997

  #\. RFC 2119                                         *Key words for use in RFCs to Indicate Requirement Levels*                                     IETF       1997

  #\. RFC 2131                                         *Dynamic Host Configuration Protocol*                                                          IETF       1997

  #\. RFC 2132                                         *DHCP Options and BOOTP Vendor Extensions*                                                     IETF       1997

  #\. RFC 2153                                         *PPP Vendor Extensions*                                                                        IETF       1997

  #\. RFC 2181                                         *Clarifications to the DNS Specification*                                                      IETF       1997

  #\. RFC 2225                                         *Classical IP and ARP over ATM*                                                                IETF       1998

  #\. RFC 2326                                         *Real time streaming protocol (RTSP)*                                                          IETF       1998

  #\. RFC 2364                                         *PPP over AAL5*                                                                                IETF       1998

  #\. RFC 2388                                         *Returning Values from Forms: multipart/form-data*                                             IETF       1998

  #\. RFC 2453                                         *RIP Version 2*                                                                                IETF       1998

  #\. RFC 2460                                         *Internet Protocol, Version 6 (IPv6) Specification*                                            IETF       1998

  #\. RFC 2464                                         *Transmission of IPv6 Packets over Ethernet Networks*                                          IETF       1998

  #\. RFC 2473                                         *Generic Packet Tunneling in IPv6 Specification*                                               IETF       1998

  #\. RFC 2474                                         *Definition of the Differentiated Services Field (DS Field) in the IPv4 and IPv6 Headers*      IETF       1998

  #\. RFC 2475                                         *An Architecture for Differentiated Services*                                                  IETF       1998

  #\. RFC 2492                                         *IPv6 over ATM Networks*                                                                       IETF       1999

  #\. RFC 2516                                         *A Method for Transmitting PPP Over Ethernet (PPPoE)*                                          IETF       1999

  #\. RFC 2597                                         *Assured Forwarding PHB Group*                                                                 IETF       1999

  #\. RFC 2616                                         *Hypertext Transfer Protocol -- HTTP/1.1*                                                      IETF       1999

  #\. RFC 2661                                         *Layer Two Tunneling Protocol (L2TP)*                                                          IETF       1999

  #\. RFC 2663                                         *IP Network Address Translator (NAT) Terminology and Considerations*                           IETF       1999

  #\. RFC 2684                                         *Multiprotocol Encapsulation over ATM Adaptation Layer 5*                                      IETF       1999

  #\. RFC 2818                                         *HTTP Over TLS*                                                                                IETF       2000

  #\. RFC 2939                                         *Procedures and IANA Guidelines for Definition of New DHCP Options and Message Types*          IETF       2000

  #\. RFC 3022                                         *Traditional IP Network Address Translator (Traditional NAT)*                                  IETF       2001

  #\. RFC 3027                                         *Protocol Complications with the IP Network Address Translator*                                IETF       2001

  #\. RFC 3046                                         *DHCP Relay Agent Information Option*                                                          IETF       2001

  #\. RFC 3145                                         *L2TP Disconnect Cause Information*                                                            IETF       2001

  #\. RFC 3203                                         *DHCP reconfigure extension*                                                                   IETF       2001

  #\. RFC 3246                                         *An Expedited Forwarding PHB (Per-Hop Behavior)*                                               IETF       2002

  #\. RFC 3260                                         *New Terminology and Clarifications for Diffserv*                                              IETF       2002

  #\. RFC 3261                                         *SIP: Session Initiation Protocol*                                                             IETF       2002

  #\. RFC 3315                                         *Dynamic Host Configuration Protocol for IPv6 (DHCPv6)*                                        IETF       2003

  #\. RFC 3376                                         *Internet Group Management Protocol, Version 3*                                                IETF       2002

  #\. RFC 3544                                         *IP Header Compression over PPP*                                                               IETF       2003

  #\. RFC 3550                                         *RTP: A Transport Protocol for Real-Time Applications*                                         IETF       2003

  #\. RFC 3579                                         *RADIUS (Remote Authentication Dial In User Service) Support For extensible authentication     IETF       2003
                                                       protocol (EAP)*                                                                                           

  #\. RFC 3596                                         *DNS Extensions to Support IP Version 6*                                                       IETF       2003

  #\. RFC 3633                                         *IPv6 Prefix Options for Dynamic Host Configuration Protocol (DHCP) version 6*                 IETF       2003

  #\. RFC 3646                                         *DNS Configuration options for Dynamic Host Configuration Protocol for IPv6 (DHCPv6)*          IETF       2003

  #\. RFC 3810                                         *Multicast Listener Discovery Version 2 (MLDv2) for IPv6*                                      IETF       2004

  #\. RFC 3901                                         *DNS IPv6 Transport Operational Guidelines*                                                    IETF       2004

  #\. RFC 3925                                         *Vendor-Identifying Vendor Options for Dynamic Host Configuration Protocol version 4 (DHCPv4)* IETF       2004

  #\. RFC 3931                                         *Layer Two Tunneling Protocol -- Version 3 (L2TPv3)*                                           IETF       2005

  #\. RFC 3947                                         *Negotiation of NAT Traversal in the IKE*                                                      IETF       2005

  #\. RFC 3948                                         *UDP Encapsulation of IPsec ESP packets*                                                       IETF       2005

  #\. RFC 4072                                         *Diameter extensible authentication protocol (EAP) application*                                IETF       2005

  #\. RFC 4075                                         *Simple Network Time Protocol (SNTP) Configuration Option for DHCPv6*                          IETF       2005

  #\. RFC 4191                                         *Default Router Preferences and More-Specific Routes*                                          IETF       2005

  #\. RFC 4193                                         *Unique Local IPv6 Unicast Addresses*                                                          IETF       2005

  #\. RFC 4213                                         *Basic Transition Mechanisms for IPv6 Hosts and Routers*                                       IETF       2005

  #\. RFC 4241                                         *A Model of IPv6/IPv4 Dual Stack Internet Access Service*                                      IETF       2005

  #\. RFC 4301                                         *Security architecture for the Internet Protocol*                                              IETF       2005

  #\. RFC 4302                                         *IP authentication header*                                                                     IETF       2005

  #\. RFC 4303                                         *IP encapsulating security payload (ESP)*                                                      IETF       2005

  #\. RFC 4306                                         *Internet key Exchange (IKEv2) Protocol*                                                       IETF       2005

  #\. RFC 4330                                         *Simple Network Time Protocol (SNTP) Version 4 for IPv4, IPv6 and OSI*                         IETF       2006

  #\. RFC 4361                                         *Node-specific Client Identifiers for Dynamic Host Configuration Protocol Version Four         IETF       2006
                                                       (DHCPv4)*                                                                                                 

  #\. RFC 4443                                         *Internet Control Message Protocol (ICMPv6) for the Internet Protocol Version 6 (IPv6)         IETF       2006
                                                       Specification*                                                                                            

  #\. RFC 4541                                         *Considerations for Internet Group Management Protocol (IGMP) and Multicast Listener Discovery IETF       2006
                                                       (MLD) Snooping Switches*                                                                                  

  #\. RFC 4605                                         *Internet Group Management Protocol (IGMP) /Multicast Listener Discovery (MLD)-Based Multicast IETF       2006
                                                       Forwarding ("IGMP/MLD Proxying")*                                                                         

  #\. RFC 4632                                         *Classless Inter-domain Routing (CIDR): The Internet Address Assignment and Aggregation Plan*  IETF       2006

  #\. RFC 4638                                         *Accommodating a Maximum Transit Unit/Maximum Receive Unit (MTU/MRU) Greater Than 1492 in the  IETF       2006
                                                       Point-to-Point Protocol over Ethernet (PPPoE)*                                                            

  #\. RFC 4704                                         *The Dynamic Host Configuration Protocol for IPv6 (DHCPv6) Client Fully Qualified Domain Name  IETF       2006
                                                       (FQDN) Option*                                                                                            

  #\. RFC 4861                                         *Neighbor Discovery for IP version 6 (IPv6)*                                                   IETF       2007

  #\. RFC 4862                                         *IPv6 Stateless Address Autoconfiguration*                                                     IETF       2007

  #\. RFC 5072                                         *IP version 6 over PPP*                                                                        IETF       2007

  #\. RFC 5172                                         *Negotiation for IPv6 Datagram Compression Using IPv6 Control Protocol*                        IETF       2008

  #\. RFC 5176                                         *Dynamic Authorization Extensions to Remote Authentication Dial In User Service (RADIUS)*      IETF       2008

  #\. RFC 5246                                         *The Transport Layer Security (TLS) Protocol Version 1.2*                                      IETF       2008

  #\. RFC 5247                                         *Extensible Authentication Protocol (EAP) Key Management Framework*                            IETF       2008

  #\. RFC 5280                                         *Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL)    IETF       2008
                                                       Profile*                                                                                                  

  #\. RFC 5625                                         *DNS Proxy Implementation Guidelines*                                                          IETF       2009

  #\. RFC 5880                                         *Bidirectional Forwarding Detection*                                                           IETF       2010

  #\. RFC 5881                                         *Bidirectional forwarding detection (BFD) for IPv4 and IPv6 (single hop)*                      IETF       2010

  #\. RFC 5969                                         *IPv6 Rapid Deployment on IPv4 Infrastructures (6rd) -- Protocol Specification*                IETF       2010

  #\. RFC 5996                                         *Internet Key Exchange Protocol Version 2 (IKEv2)*                                             IETF       2010

  #\. RFC 6092                                         *Recommended Simple Security Capabilities in Customer Premises Equipment (CPE) for Providing   IETF       2011
                                                       Residential IPv6 Internet Service*                                                                        

  #\. RFC 6106                                         *IPv6 Router Advertisement Options for DNS Configuration*                                      IETF       2010

  #\. RFC 6333                                         *Dual-Stack Lite Broadband Deployments Following IPv4 Exhaustion*                              IETF       2011

  #\. RFC 6334                                         *Dynamic Host Configuration Protocol for IPv6 (DHCPv6) Option for Dual-Stack Lite*             IETF       2011

  #\. RFC 6422                                         *Relay-Supplied DHCP Options*                                                                  IETF       2011

  #\. RFC 6434                                         *IPv6* *Node* *Requirements*                                                                   IETF       2011

  #\. RFC 6440                                         *The EAP Re-authentication Protocol (ERP) Local Domain Name DHCPv6 Option*                     IETF       2011

  #\. RFC 6696                                         *EAP Extensions for the EAP Re-authentication Protocol (ERP)*                                  IETF       2012

  #\. RFC 6704                                         *Forcerenew Nonce Authentication*                                                              IETF       2013

  #\. RFC 6731                                         *Improved Recursive DNS Server Selection for Multi-Interfaced Nodes*                           IETF       2013

  #\. RFC 6887                                         *Port Control Protocol (PCP)*                                                                  IETF       2013

  #\. RFC 6970                                         *Universal Plug and Play (UPnP) Internet Gateway Device-Port Control Protocol Interworking     IETF       2013
                                                       Function(IGD-PCP IWF)*                                                                                    

  #\. RFC 7078                                         *Distributing address selection policy using DHCPv6*                                           IETF       2014

  #\. RFC 7291                                         *DHCP Options for the Port Control Protocol (PCP)*                                             IETF       2014

  #\. RFC 7597                                         *Mapping of Address and Port with Encapsulation (MAP-E)*                                       IETF       2015

  #\. RFC 7598                                         *DHCPv6 Options for Configuration of Softwire Address and Port-Mapped Clients*                 IETF       2015

  #\. RFC 7648                                         *Port Control Protocol (PCP) Proxy Function*                                                   IETF       2015

  #\. RFC 7753                                         *Port Control Protocol (PCP) Extension for Port Set Allocation*                                IETF       2015

  #\. ICES-003                                         *Information Technology Equipment (ITE) --- Limits and methods of measurement*                 Industry   2012
                                                                                                                                                      Canada     

  #\. ISO 8601                                         *Data elements and interchange formats -- Information interchange -- Representation of dates   ISO/IEC    2004
                                                       and times*                                                                                                

  #\. G.984.1                                          *Gigabit-capable Passive Optical Networks (GPON)): General characteristics*                    ITU-T      2003

  #\. G.984.2                                          *Gigabit-capable Passive Optical Networks (GPON): Physical Media Dependent (PMD) layer         ITU-T      2003
                                                       specification*                                                                                            

  #\. G.984.2 Amd1                                     *Gigabit-capable Passive Optical Networks (G-PON): Physical Media Dependent (PMD) layer        ITU-T      2006
                                                       specification Amendment 1: New Appendix III -- Industry best practice for 2.488 Gbit/s                    
                                                       downstream, 1.244 Gbit/s upstream G-PON*                                                                  

  #\. G.984.3                                          *Gigabit-capable Passive Optical Networks (GPON): Transmission convergence layer               ITU-T      2008
                                                       specification*                                                                                            

  #\. G.987.1                                          *10-Gigabit-capable passive optical networks (XG-PON): General requirements*                   ITU-T      2016

  #\. G.987.2                                          *10-Gigabit-capable passive optical networks (XG-PON): Physical media dependent (PMD) layer    ITU-T      2016
                                                       specification*                                                                                            

  #\. G.987.3                                          *10-Gigabit-capable passive optical networks (XG-PON): Transmission convergence (TC) layer     ITU-T      2016
                                                       specification*                                                                                            

  #\. G.988                                            *Optical network unit management and control interface(OMCI) specification*                    ITU-T      2012

  #\. G.992.1                                          *Asymmetric digital subscriber line (ADSL) transceivers*                                       ITU-T      1999

  #\. G.992.3                                          *Asymmetric digital subscriber line transceivers 2 (ADSL2)*                                    ITU-T      2009

  #\. G.992.5                                          *Asymmetric digital subscriber line 2 transceivers (ADSL2) -- Extended bandwidth ADSL2         ITU-T      2009
                                                       (ADSL2plus)*                                                                                              

  #\. G.993.2                                          *Very high speed digital subscriber line transceivers 2 (VDSL2)*                               ITU-T      2011

  #\. G.9954                                           *Home networking transceivers - Enhanced physical, media access, and link layer                ITU-T      2007
                                                       specifications*                                                                                           

  #\. G.997.1                                          *Physical layer management for digital subscriber line (DSL) transceivers*                     ITU-T      2012

  #\. G.998.1                                          *ATM-based multi-pair bonding*                                                                 ITU-T      2005

  #\. G.998.2                                          *Ethernet-based multi-pair bonding*                                                            ITU-T      2005

  #\. G.9807.1                                         *10-Gigabit-capable symmetric passive optical network (XGS-PON)*                               ITU-T      2016

  #\. G.9960                                           *Unified high-speed wireline-based home networking transceivers -- System architecture and     ITU-T      2011
                                                       physical layer specification*                                                                             

  #\. G.9961                                           *Unified high-speed wireline-based home networking transceivers -- Data link layer             ITU-T      2010
                                                       specification*                                                                                            

  #\. G.9964                                           *Unified high-speed wireline-based home networking transceivers -- Specification of spectrum   ITU-T      2011
                                                       related components*                                                                                       

  #\. I.610                                            *B-ISDN operation and maintenance principles and functions*                                    ITU-T      1999

  #\. X.509                                            *Information technology -- Open systems interconnection -- The Directory: Public-key and       ITU-T      2012
                                                       attribute certificate frameworks*                                                                         

  #\. T1-413                                           *Network and Customer Installation Interfaces -- Asymmetric Digital Subscriber Line (ADSL)     ANSI       1998
                                                       Metallic Interface*                                                                                       

  #\. T1-413a                                          *Telecommunications -- Network and customer installation interfaces -- Asymmetric digital      ATIS       2001
                                                       subscriber line (ADSL) metallic interface (supplement to ATIS T1.413:1998).*                              

  #\. ATIS 0600421:2001 (R2011)                        *In-Line Filter for Use with Voiceband Terminal Equipment Operating on the Same Wire Pair with ANSI       2001
                                                       High Frequency (up To 12 MHz) Devices*                                                                    

  #\. ATIS 0600427.01:2004 (R2009)                     *ATM-based Multi-pair Bonding*                                                                 ATIS       2004

  #\. ATIS 0600427.02.2005(R21010)                     *Ethernet-based Multi-Pair Bonding*                                                            ATIS       2005

  #\. UL 1310                                          *Standard for Class 2 Power Units*                                                             UL         2011

  #\. UL 60950-1                                       *Safety of Information Technology Equipment*                                                   UL         2003

  #\. AF-TM-0121.000                                   *Traffic management specification, version 4.1*                                                ATM Forum  1999

  #\. UPnP InternetGatewayDevice:2                     *InternetGatewayDevice:2 Device Template Version 1.01*                                         UPnP Forum 2010

  #\. UPnP WANIPConnection:2                           *WANIPConnection:2 Service*                                                                    UPnP Forum 2010

  #\. UPnP WANPPPConnection:1                          *WANPPPConnection:1 Service Template Version 1.01*                                             UPnP Forum 2001

  #\. UPnP WANIPv6FirewallControl:1                    *WANIPv6FirewallControl:1 Service*                                                             UPnP Forum 2010

  #\. HomePlugAV2                                      *HomePlug™ AV2 Technology*                                                                     HomePlug   2012
                                                                                                                                                      Alliance   

  #\. OSGI-CORE-6                                      *The OSGi Alliance, OSGi Core, Release 6*                                                      OSGI       2014
                                                                                                                                                      Alliance   

  #\. OSGI CMPN-6                                      *The OSGi Alliance, OSGi Compendium, Release 6*                                                OSGI       2014
                                                                                                                                                      Alliance   

  #\. JDK Compact                                      *Compact Profiles,                                                                             Oracle     
                                                       https://docs.oracle.com/javase/8/docs/technotes/guides/compactprofiles/compactprofiles.html*              

  #\. draft-ietf-mif-dhcpv6-route-option               *DHCPv6 Route Options*\                                                                        IETF       
                                                       *NOTE: THIS DRAFT IS EXPIRED!!!*                                                                          

  #\. RFC 5357                                         *A Two-Way Active Measurement Protocol (TWAMP)*                                                IETF       2008

  #\. RFC 3772                                         *Point-to-Point (PPP) Vendor Protocol*                                                         IETF       2004

  #\. TS 22.011                                        *Technical Specification Group Services and*\                                                  3GPP       
                                                       *System Aspects; Service accessibility (Release 16)*                                                      

  #\. TS 23.003                                        *Technical Specification Group Core Network and Terminals; Numbering, addressing and           3GPP       
                                                       identification (Release 16)*                                                                              

  #\. TS 23.122                                        *Technical Specification Group Core Network and Terminals; Non-Access-Stratum (NAS) functions  3GPP       
                                                       related to Mobile Station (MS) in idle mode (Release 16)*                                                 

  #\. TS 23.316                                        *Technical Specification Group Services and System Aspects; Wireless and wireline convergence  3GPP       
                                                       access support for the 5G System (5GS) (Release 16)*                                                      

  #\. TS 23.502                                        *Technical Specification Group Services and System Aspects; Procedures for the 5G System;      3GPP       
                                                       Stage 2 (Release 16)*                                                                                     

  #\. TS 23.503                                        *Technical Specification Group Services and System Aspects; Policy and Charging Control        3GPP       
                                                       Framework for the 5G System; Stage 2 (Release 15)*                                                        

  #\. TS 24.501                                        *Technical Specification Group Core Network and Terminals; Non-Access-Stratum (NAS) protocol   3GPP       
                                                       for 5G System (5GS); Stage 3 (Release 16)*                                                                

  #\. TS 24.502                                        *Technical Specification Group Core Network and Terminals; Access to the 3GPP 5G Core Network  3GPP       
                                                       (5GCN) via Non-3GPP Access Networks (N3AN); Stage 3 (Release 16)*                                         

  #\. TS 33.501                                        *Technical Specification Group Services and System Aspects; Security architecture and          3GPP       
                                                       procedures for 5G system (Release 16)*                                                                    

  #\. TS 36.300                                        *Technical Specification Group Radio Access Network; Evolved Universal Terrestrial Radio       3GPP       
                                                       Access (E-UTRA) and Evolved Universal Terrestrial Radio Access Network (E-UTRAN); Overall                 
                                                       description; Stage 2 (Release 16)*                                                                        

  #\. TS 36.800                                        *Technical Specification Group Radio Access Networks; Universal Terrestrial Radio Access       3GPP       
                                                       (UTRA) and Evolved Universal Terrestrial Radio Access (E-UTRA); Extended UMTS / LTE 800 Work              
                                                       Item Technical Report (Release 9)*                                                                        

  #\. TR-456                                           *Access Gateway Function (AGF) Functional Requirements*                                        BBF        2020

  #\. TR-470                                           *5G Fixed Mobile Convergence (FMC) Architecture*                                               BBF        2020

  #\. TS 24.193                                        3rd Generation Partnership Project; Technical Specification Group Core Network and Terminals;  3GPP       
                                                       5G System; Access Traffic Steering, Switching and Splitting ATSSS); Stage 3 (Release 16)                  

  #\. TS 24.301                                        3rd Generation Partnership Project; Technical Specification Group Core Network and Terminals;  3GPP       
                                                       Non-Access-Stratum (NAS) protocol for Evolved Packet System (EPS); Stage 3 (Release 16)                   

  #\. IETF RFC 8822                                    5G Wireless Wireline Convergence User Plane Encapsulation (5WE)                                IETF       2021

  #\. TR-104 Issue 1                                   Provisioning Parameters for VoIP CPE                                                           BBF        2011
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following information is given for the convenience of users of this
%bbfType% and does not constitute an endorsement by the Broadband Forum
of these products:

-   Safari® is a registered trademark of Apple Computer, Inc.

-   HomePlug® is a registered trademark of HomePlug Powerline Alliance,
    Inc.

-   HomePNA® is a registered trademark of HomePNA, Inc.

-   IEEE® is a registered trademark of the Institute of Electrical and
    Electronics Engineers, Inc. (IEEE). This publication is not endorsed
    by the IEEE.

-   Internet Explorer® and Microsoft® are registered trademarks of
    Microsoft Corporation.

-   Java® and JavaScript® are registered trademarks of Oracle, Inc.

-   Mozilla® is a registered trademark of the Mozilla Foundation.

-   Wi-Fi® is a registered trademark of the Wi-Fi Alliance

-   WPA, WPA2,WPA3, Protected Setup, WMM and WMM-SA are trademarks of
    the Wi-Fi Alliance

## Definitions

The following terminology is used throughout this %bbfType%.

  --------------------- -------------------------------------- -----------------------------------------------------
  **5G-RG**             **5G-RG**                              An RG acting as UE with regard to the 5G core. It
                                                               holds a secure element and exchanges NAS signaling
                                                               with the 5G core.

  **5G Access Network   **5G Access Network (5GAN)**           This comprises 5G radio ANs (RANs) and 5G wireline
  (5GAN)**                                                     ANs connecting to a 5G core.

  **5G System (5GS)**   **5G System (5GS)**                    A system consisting of 5G Access Network (AN), 5G
                                                               Core Network and end-device.

  **Access & Mobility   **Access & Mobility Function (AMF)**   The AMF is a 5GC-CP function that terminates N1, the
  Function (AMF)**                                             control interface with UEs, and N2, the control
                                                               interface with access networks. It is responsible for
                                                               mobility & access related functions. It acts as the
                                                               security anchor point for a given UE. At PDU session
                                                               establishment, it selects the SMF corresponding to
                                                               the requested slice and targeted DN, and relays
                                                               session related messages to this SMF.

  **ACS**               **ACS**                                Auto-Configuration Server. This is a component in the
                                                               broadband network responsible for CWMP
                                                               auto-configuration of the CPE for advanced services.

  **Agent**             **Agent**                              A generic term that refers (as appropriate) to either
                                                               a CWMP Endpoint or to a USP Agent.

  **Allowed NSSAI**     **Allowed NSSAI**                      NSSAI provided by the serving PLMN network during
                                                               e.g. a registration procedure, indicating the
                                                               S-NSSAIs value that the UE could use in the serving
                                                               PLMN of the current registration area. (definition
                                                               from TS 23.501 \[x\])

  **Backup**            **Backup**                             The ability to take over a task when a source becomes
                                                               unavailable. Examples:\
                                                               A web server becomes unavailable. For incoming
                                                               traffic, backup provides another web server to take
                                                               over the operation.\
                                                               A communication link becomes unavailable. Via backup,
                                                               another link takes over the communication task.

  **Configurable**      **Configurable**                       A requirement for configurability does not imply any
                                                               particular configuration interface. When specific
                                                               user or TR-069 or other configurability is required,
                                                               the requirement is stated explicitly.

  **Configured NSSAI**  **Configured NSSAI**                   An NSSAI that has been provisioned in the 5G-RG
                                                               applicable to one or more PLMN (definition from TS
                                                               23.501 \[x\]).

  **Connection**        **Connection**                         As used in this document, a connection is the
                                                               continuing ability to communicate over a pair of IP
                                                               addresses.

  **Controller**        **Controller**                         A generic term that refers (as appropriate) to either
                                                               a CWMP ACS or a USP Controller.

  **CPE**               **CPE**                                Customer Premises Equipment; refers (as appropriate)
                                                               to any CWMP-enabled or USP-enabled device and
                                                               therefore covers both Internet Gateway devices and
                                                               LAN-side end devices.

  **CWMP**              **CWMP**                               CPE WAN Management Protocol. Defined in TR-069 \[2\],
                                                               CWMP is a communication protocol between an ACS and
                                                               CWMP-enabled CPE that defines a mechanism for secure
                                                               auto-configuration of a CPE and other CPE management
                                                               functions in a common framework.

  **CWMP Endpoint**     **CWMP Endpoint**                      A CWMP termination point used by a CWMP-enabled CPE
                                                               for communication with the ACS.

  **Device**            **Device**                             Unless otherwise qualified, the term *device* refers
                                                               to an RG.

  **Enabling**          **Enabling**                           Likewise, controllability requirements, for example
                                                               to enable or disable a feature, do not imply a
                                                               control interface.

  **Failover**          **Failover**                           The ability to automatically switch to another source
                                                               when a source becomes unavailable. Examples:\
                                                               \* A web server becomes unavailable. For incoming
                                                               traffic, failover automatically provides another web
                                                               server to take over the operation.\
                                                               \* A communication link becomes unavailable. Via
                                                               failover, another link automatically takes over the
                                                               communication task.

  **GUI**               **GUI**                                The term GUI or web GUI implies access to the RG that
                                                               is visible to the end user. The use of this term in a
                                                               requirement is an assertion that control or
                                                               information display is available to the end user.

  **Load balancing**    **Load balancing**                     The ability to divide the working load of a task over
                                                               multiple sources in an equal way. Examples:\
                                                               A web service that is run by a web server. For
                                                               incoming traffic this can be equally divided over
                                                               multiple servers by a load balancer.\
                                                               A communication link that is supporting a
                                                               communication task. Various links can be used to
                                                               equally divide the communication load by a load
                                                               balancer. This can be for incoming and outgoing
                                                               traffic.\
                                                               Thus, load balancing is only one form of load
                                                               sharing: load balancing is load sharing where the
                                                               load is equally divided over the sources. What
                                                               defines "equal" depends on the use case and metrics
                                                               used.

  **Load sharing**      **Load sharing**                       The ability to divide the working load of a task over
                                                               multiple sources. Examples:\
                                                               A web service that is run by a web server. For
                                                               incoming traffic this can be divided over multiple
                                                               servers by load sharing.\
                                                               A communication link that is supporting a
                                                               communication task. Various links can be used to
                                                               divide the communication load by load sharing. This
                                                               can be for incoming and outgoing traffic.

  **Logs**              **Logs**                               Likewise, requirements for logging do not imply log
                                                               configurability and retrieval on any particular
                                                               interface unless stated explicitly.

  **Network Instance**  **Network Instance**                   Information identifying a domain. Used by the UPF for
                                                               traffic detection and routing (definition from TS
                                                               23.501 \[x\]).

  **Network Slice**     **Network Slice**                      A logical network that provides specific network
                                                               capabilities and network characteristics (definition
                                                               from TS 23.501 \[x\]).

  **Network Slice       **Network Slice Instance**             A set of Network Function instances and the required
  Instance**                                                   resources (e.g. compute, storage and networking
                                                               resources) which form a deployed Network Slice
                                                               (definition from TS 23.501 \[x\]).

  **NSI ID**            **NSI ID**                             an identifier for a Network Slice instance
                                                               (definition from TS 23.501 \[x\]).

  **Network Slice       **Network Slice Selection Assistance   The NSSAI is a collection of S-NSSAIs. An NSSAI may
  Selection Assistance  Information (NSSAI)**                  be a Configured NSSAI, a Requested NSSAI or an
  Information (NSSAI)**                                        Allowed NSSAI. There can be at most eight S-NSSAIs in
                                                               Allowed and Requested NSSAIs sent in signalling
                                                               messages between the UE and the Network.

  **NSSP (Network Slice **NSSP (Network Slice Selection        It is the set of SM-NSSAI that a UE is authorized to
  Selection Policy)**   Policy)**                              access. It is stored in the UE and corresponds to the
                                                               NSSAI in the subscriber information in the network
                                                               database.

                                                               

  **Operator-specific   **Operator-specific configuration**    Many requirements specify defaults, but then add the
  configuration**                                              phrase, "or use an operator-specific configuration."
                                                               This phrase recognizes that operators may override
                                                               TR-124 requirements when necessary to satisfy their
                                                               specific needs.

  **PDU session**       **PDU session**                        Temporal association between the UE and a Data
                                                               Network that provides a PDU connectivity service. A
                                                               session can be IP, Eth or unstructured.

  **Requested NSSAI**   **Requested NSSAI**                    NSSAI provided by the UE to the Serving PLMN during
                                                               registration (definition from TS 23.501 \[x\]).

  **RG**                **RG**                                 A residential gateway (RG) is a device that
                                                               interfaces between the WAN and LAN IP environment for
                                                               a consumer broadband customer. It may route or bridge
                                                               traffic, depending on its configuration and
                                                               specifications.\
                                                               The term RG is retained for historical continuity,
                                                               even though some features may be directed at business
                                                               applications.

  **Smart RG**          A smart residential gateway is a       A smart residential gateway is a residential gateway
                        residential gateway with additional    with additional smart home services.
                        smart home services.                   

  **Software            A Software application consists of one A Software application consists of one or more
  application**         or more software modules and           software modules and configuration data, and provides
                        configuration data, and provides       specific function(s) using the open platform API of a
                        specific function(s) using the open    Smart RG.
                        platform API of a Smart RG.            

  **Software module**   An installable software entity which   An installable software entity which includes
                        includes executables, libraries,       executables, libraries, configuration and other data.
                        configuration and other data.          

  **Subscribed          S-NSSAI based on subscriber            S-NSSAI based on subscriber information, which a UE
  S-NSSAI**             information, which a UE is subscribed  is subscribed to use in a PLMN (definition from TS
                        to use in a PLMN (definition from TS   23.501 \[x\]).
                        23.501 \[x\]).                         

  **USP**               Universal Service Platform. Defined in Universal Service Platform. Defined in TR-369
                        TR-369                                 \[\[18\]\]\[{{ref\|\_Ref2867477}}\], USP is an
                        \[\[18\]\]\[{{ref\|\_Ref2867477}}\],   evolution of CWMP that allows applications to
                        USP is an evolution of CWMP that       manipulate Service Elements in a network of
                        allows applications to manipulate      Controllers and Agents.
                        Service Elements in a network of       
                        Controllers and Agents.                

  **USP Agent**         A USP Agent is a USP Endpoint that     A USP Agent is a USP Endpoint that exposes Service
                        exposes Service Elements to one or     Elements to one or more USP Controllers
                        more USP Controllers                   

  **USP Controller**    A USP Controller is a USP Endpoint     A USP Controller is a USP Endpoint that manipulates
                        that manipulates Service Elements      Service Elements through one or more USP Agents.
                        through one or more USP Agents.        

  **Wireline 5G Access  This is a wireline AN that can connect This is a wireline AN that can connect to a 5G core
  Network (W-5GAN)**    to a 5G core via the AGF. The egress   via the AGF. The egress interfaces of a W-5GAN form
                        interfaces of a W-5GAN form the border the border between access and core. They are N2 for
                        between access and core. They are N2   the control plane and N3 for the user plane.
                        for the control plane and N3 for the   
                        user plane.                            
  --------------------- -------------------------------------- -----------------------------------------------------

## Abbreviations

This %bbfType% defines the following abbreviations:

  -----------------------------------------------------------------------
  5WE          5G WWC Encapsulation
  ------------ ----------------------------------------------------------
  AAA          Authentication, Authorization and Accounting

  AAL          ATM Adaptation Layer

  ac           alternating current

  ADSL         Asynchronous Digital Subscriber Line

  AFTR         Address family transition router

  AGF          Access Gateway Function

  ALG          Application Layer Gateway

  AMF          Access Management Function

  AN           Access Network

  ANSI         American National Standards Institute

  AS           Access Stratum

  ASCII        American Standard Code for Information Interchange

  ATA          Analog Terminal Adapter

  ATM          Asynchronous Transfer Mode

  BFD          Bidirectional forwarding detection

  CP           Control Plane

  CPE          Customer Premises Equipment

  CRC          Cyclic Redundancy Check

  CSA          Canadian Standards Association

  DAD          Duplicate address detection

  DHCP         Dynamic Host Configuration Protocol

  DLNA         Digital living network alliance (www.dlna.org)

  DNS          Domain Name Server

  DoS          Denial of Service

  DSCP         Differentiated Services Code Point

  DSL          Digital Subscriber Line

  DUID         DHCP Unique Identifier

  DUID-EN      DUID based Enterprise Number

  FCC          Federal Communications Commission

  FQDN         Fully Qualified Domain Name

  GMT          Greenwich Mean Time

  GUI          Graphical User Interface

  HTML         Hypertext Markup Language

  HTTP         Hypertext Transfer Protocol

  HTTPS        Secure Hypertext Transfer Protocol

  Hz           Hertz

  IAID         Identification Association Identifier

  IEEE®        The Institute of Electrical and Electronics Engineers

  IETF         The Internet Engineering Task Force

  IMEI         International Mobile Equipment Identity

  IMSI         International Mobile Subscriber Identity

  INP          Impulse noise protection

  IP           Internet Protocol

  IPCP         Internet Protocol Control Protocol

  ISO          International Organization for Standardization

  ITU          International Telecommunication Union

  Kbps         kilobits per second

  LAN          Local Area Network

  LCP          Link Control Protocol

  LPF          Low-pass filter

  MAC          Medium Access Control

  MRU          Maximum Receive Unit

  ms           millisecond

  MTBF         Mean Time Between Failure

  MTU          Maximum Transit Unit

  NAS          Non-Access Stratum

  NAT          Network Address Translation

  NTP          Network Time Protocol

  ONU          Optical Network Unit

  PADI         PPPoE Active Discovery Initiation

  PADO         PPPoE Active Discovery Offer

  PC           Personal Computer

  PCP          Priority Code Point

  PD           Prefix Delegation

  PDU          Protocol Data Unit

  POTS         Plain Old Telephone Service

  PPP          Point to Point Protocol

  PVC          Permanent Virtual Circuit

  QFI          QoS Flow Identifier

  RA           Router Advertisement

  RG           Residential Gateway

  RQI          Reflective QoS Indication

  RTSP         Real time streaming protocol

  SIP          Session Initiation Protocol

  SN           Serial Number

  SNTP         Simple Network Time Protocol

  SSL          Secure Sockets Layer

  SUCI         Subscriber Concealed Identifier

  SUPI         Subscriber Permanent Identifier

  TCP          Transmission Control Protocol

  TLS          Transport Layer Security

  TR           Technical Report

  UDP          User Datagram Protocol

  UE           User Equipment

  UL           Underwriters Laboratories

  ULA          User licensing agreement

  ULC          Underwriters Laboratories Canada

  UP           User Plane

  URSP         UE Route Selection Policy

  USB          Universal Serial Bus

  Vac          Volts ac

  VCI          Virtual Circuit Identifier

  Vdc          Volts dc

  VDSL         Very high-speed Digital Subscriber Line

  VID          VLAN Identifier

  VLAN         Virtual LAN

  VoIP         Voice over IP

  VPI          Virtual Path Identifier

  VSO          Vendor Specific Option

  WAN          Wide Area Network

  WEP          Wireless Encryption Protocol

  Wi-Fi®       Wi-Fi Alliance wireless standards organization

  WPA          Wi-Fi Protected Access

  WWC          Wireline Wireless Convergence
  -----------------------------------------------------------------------

# %bbfType% Impact {#bbftype-impact .new-page}

## Energy Efficiency

%bbfNumber% contains regional power requirements for Residential Gateway
(RG) devices. In general, there is an expectation that these devices
will meet all local regulatory requirements for powering and energy
consumption.

## IPv6

Issue 2 of this %bbfType% was published specifically to provide
requirements needed for deployment of IPv6 capable RGs. Issue 3 includes
a number of minor extensions, corrections and clarifications.

## Security

The requirements in %bbfNumber% are intended to provide a reasonably
secure environment for general consumers, while ensuring that the
functionality is usable by consumers, such that they do not feel that
the degree of security is preventing them from accomplishing what they
want to do.

The requirements are also intended to ensure that the RG does not have a
negative impact on the security of the access network and other users of
the access network.

## Privacy

%bbfNumber% does not explicitly address privacy requirements.

# Residential Gateway Requirements {#residential-gateway-requirements .new-page}

## GEN - General Device Requirements

### GEN.Design - Design

!include temp/001-GEN.DESIGN.yaml

### GEN.OPS - Device Operation

!include temp/002-GEN.OPS.yaml

### GEN.NET - Networking Protocols

!include temp/003-GEN.NET.yaml

### GEN.NETv6 - IPv6 Networking Protocols

!include temp/004-GEN.NETv6.yaml

## WAN - Wide Area Networking {#wan---wide-area-networking .new-page}

### WAN.ATM

!include temp/005-WAN.ATM.yaml

#### WAN. ATM.MULTI - ATM Multi-PVC

!include temp/006-WAN.ATM.MULTI.yaml

### WAN.CONNECT - Connection Establishment

*Note that this module applies to IPv6 connections as well as IPv4, but
only if the RG has an IPv6 stack.*

!include temp/007-WAN.CONNECT.yaml

#### WAN.CONNECT.OnDemand - On-Demand Connection Establishment

The On-demand Connection function applies only to IPv4 connections.
However, when IPv6 is present, its behavior must take the presence of
IPv6 into consideration as described in this module

!include temp/008-WAN.CONNECT.ON-DEMAND.yaml

### WAN.ETHOAM - Ethernet OAM

!include temp/009-WAN.ETHOAM.yaml

### WAN.BRIDGE - Bridging

*Note that the IPv6 parts of this module apply only if the RG supports
IPv6.*

!include temp/010-WAN.BRIDGE.yaml

### WAN.DHCPC - DHCP Client (DHCPv4)

!include temp/011-WAN.DHCPC.yaml

#### WAN.DHCPC.Force - Force renew

!include temp/012-WAN.DHCPC.Force.yaml

#### WAN.DHCPC.BFDecho - BFD echo

!include temp/013-WAN.DHCPC.BFDecho.yaml

#### WAN.DHCPC.BFDKA - BFD Keep-alive

!include temp/014-WAN.DHCPC.BFDKA.yaml

### WAN.DHCPv4 - DHCP Client (DHCPv4)

#### WAN.DHCPv4.ERP - EAP Re-authentication (ERP) for DHCPv4

!include temp/015-WAN.DHCPv4.ERP.yaml

### WAN.DHCPv6 - DHCP Client (DHCPv6)

#### WAN.DHCPv6.ERP - EAP Re-authentication (ERP) for DHCPv6

!include temp/016-WAN.DHCPv6.ERP.yaml

### WAN.IPv6 - IPv6 WAN Connection

!include temp/017-WAN.IPv6.yaml

### WAN.TRANS - Transitional IPv6 WAN Connection

#### WAN.TRANS.6rd - 6rd Transition Mechanism

!include temp/018-WAN.TRANS.6rd.yaml

#### WAN.TRANS.DS-Lite - Dual Stack Lite Transition Mechanism

!include temp/019-WAN.TRANS.DS-Lite.yaml

#### WAN.TRANS.v4-release-control - IPv6 connectivity with content-based IPv4 release control transition mechanism

!include temp/020-WAN.TRANS.v4-release-control.yaml

#### WAN.TRANS.MAP-E - IPv6 connectivity with content-based IPv4 release control transition mechanism

!include temp/021-WAN.TRANS.MAP-E.yaml

### WAN.PPP - PPP Client

!include temp/022-WAN.PPP.yaml

#### WAN.PPP.IPv6 - PPP Client for establishment of IPv6 connection

!include temp/023-WAN.PPP.IPv6.yaml

### WAN.dot1x - 802.1X Client

!include temp/024-WAN.dot1x.yaml

### WAN.DoS - Denial of Service Prevention

*Note: The IPv6 parts of this module apply only if the RG has an IPv6
stack.*

!include temp/025-WAN.DoS.yaml

### WAN.QoS - Quality of Service

*Note: The IPv6 parts of this module apply only if the RG has an IPv6
stack.*

!include temp/026-WAN.QoS.yaml

#### WAN.QoS.VLAN - VLAN based QoS

!include temp/027-WAN.QoS.VLAN.yaml

#### WAN.QoS.TUNNEL - Quality of Service for Tunneled Traffic

This module only applies when the RG is an endpoint for a tunnel to the
WAN. This module applies to IPv6 if it is used as either the tunneled or
the tunneling protocol.

!include temp/028-WAN.QoS.TUNNEL.yaml

### WAN.IPsecClient - IPsec VPN peer to peer

!include temp/029-WAN.IPsecClient.yaml

### WAN.L2tpClient - L2tp VPN Remote Access

!include temp/030-WAN.L2tpClient.yaml

### WAN.PCP - Port Control Protocol

!include temp/031-WAN.PCP.yaml

### WAN.TUN -- WAN Tunnel

!include temp/032-WAN.TUN.yaml

#### WAN.TUN.VXLAN -- VxLAN Tunnel

!include temp/033-WAN.TUN.VXLAN.yaml

#### WAN.TUN.L2 -- L2Tunnel

!include temp/034-WAN.TUN.L2.yaml

## LAN - Local Area Networking {#lan---local-area-networking .new-page}

### LAN.GEN - General LAN Protocols

!include temp/035-LAN.GEN.yaml

### LAN.ADDRESS - Private IPv4 Addressing

!include temp/036-LAN.ADDRESS.yaml

### LAN.ADDRESSv6- LAN IPv6 Addressing

!include temp/037-LAN.ADDRESSv6.yaml

### LAN.DHCPS - DHCPv4 Server

!include temp/038-LAN.DHCPS.yaml

### LAN.DHCPv6S - DHCPv6 Server

!include temp/039-LAN.DHCPv6S.yaml

### LAN.DNS - Naming Services (IPv4 and general requirements)

!include temp/040-LAN.DNS.yaml

### LAN.DNSv6- Naming Services (IPv6)

!include temp/041-LAN.DNSv6.yaml

### LAN.NAT- NAT/NAPT

!include temp/042-LAN.NAT.yaml

### LAN.PFWD - Port Forwarding (IPv4)

!include temp/043-LAN.PFWD.yaml

### LAN.PFWDv6- Port Forwarding (IPv6)

!include temp/044-LAN.PFWDv6.yaml

### LAN.ALG - ALG Functions (IPv4)

!include temp/045-LAN.ALG.yaml

### LAN.FWD - Connection Forwarding

The IPv6 parts of this module apply only if the RG has an IPv6 stack.

!include temp/046-LAN.FWD.yaml

### LAN.IGMP - IGMP

#### LAN.IGMP.BRIDGED - IGMP and Multicast in Bridged Configurations (IPv4)

!include temp/047-LAN.IGMP.BRIDGED.yaml

#### LAN.IGMP.ROUTED - IGMP and Multicast in Routed Configurations (IPv4)

!include temp/048-LAN.IGMP.ROUTED.yaml

### LAN.MLD.ROUTED - MLD and Multicast in Routed Configurations (IPv6)

!include temp/049-LAN.MLD.ROUTED.yaml

### LAN.FW - Firewall (Basic)

This module applies to IPv6 as well as IPv4, but only if the RG has an
IPv6 stack

!include temp/050-LAN.FW.yaml

### LAN.FW.SPI - Firewall (Advanced)

This module applies to IPv6 as well as IPv4, but only if the RG has an
IPv6 stack.

!include temp/051-LAN.FW.SPI.yaml

### LAN.FILTER - Filtering

#### LAN.FILTER.TIME - Time of Day Filtering

!include temp/052-LAN.FILTER.TIME.yaml

#### LAN.FILTER.CONTENT - Content Filtering

!include temp/053-LAN.FILTER.CONTENT.yaml

### LAN.DIAGNOSTICS - Automated User Diagnostics

!include temp/054-LAN.DIAGNOSTICS.yaml

### LAN.CAPTIVE - Captive Portal with Web Redirection

This module applies to IPv6 as well as IPv4, but only if the RG has an
IPv6 stack.

!include temp/055-LAN.CAPTIVE.yaml

### LAN.QoS - LAN quality of service requirements

!include temp/056-LAN.QoS.yaml

### LAN.SIPserver - SIP Server

!include temp/057-LAN.SIPserver.yaml

### LAN.SIPmixer - SIP Mixer

!include temp/058-LAN.SIPmixer.yaml

### LAN.Interworking.UE-Authentication - 3GPP User Equipment Authentication Support

!include temp/059-LAN.Interworking.UE-Authentication.yaml

## MGMT - Management & Diagnostics {#mgmt---management-diagnostics .new-page}

### MGMT.GEN - General

!include temp/060-MGMT.GEN.yaml

### MGMT.UPnP - UPnP

!include temp/061-MGMT.UPnP.yaml

#### MGMT.UPnP.IGD - UPnP IGD

!include temp/062-MGMT.UPnP.IGD.yaml

#### MGMT.UPnP.IGD.ACRF - UPnP IGD to allow Connection Request Forwarding

!include temp/063-MGMT.UPnP.IGD.ACRF.yaml

##### MGMT.UPnP.IGD.ACRF.IPv4 - UPnP IGD to allow Connection Request Forwarding through the NAT of the device

!include temp/064-MGMT.UPnP.IGD.ACRF.IPv4.yaml

##### MGMT.UPnP.IGD.ACRF.IPv6 - UPnP IGD to allow Connection Request Forwarding through the Firewall of the device

!include temp/065-MGMT.UPnP.IGD.ACRF.IPv6.yaml

### MGMT.LOCAL - Local Management

!include temp/066-MGMT.LOCAL.yaml

#### MGMT.LOCAL.TR-064 - TR-064 Issue 2

!include temp/067-MGMT.LOCAL.TR-064.yaml

### MGMT.REMOTE - Remote Management

#### MGMT.REMOTE.TR-069 - Remote Management (TR-069)

!include temp/068-MGMT.REMOTE.TR-069.yaml

#### MGMT.REMOTE.USP - Remote Management (USP)

!include temp/069-MGMT.REMOTE.USP.yaml

#### MGMT.REMOTE.WEB - Remote Management (Web Browser)

This module applies to IPv6 as well as IPv4, but only if the RG has an
IPv6 stack.

!include temp/070-MGMT.REMOTE.WEB.yaml

### MGMT.NTP - Network Time Client

This module applies to IPv6 as well as IPv4, but only if the RG has an
IPv6 stack.

!include temp/071-MGMT.NTP.yaml

### MGMT.TWAMP -- Two Way Active Measurement Protocol

This module applies to IPv6 as well as IPv4, but only if the RG has an
IPv6 stack.

!include temp/072-MGMT.TWAMP.yaml

### MGMT.DATCOL -- Data collection Requirements

#### MGMT.DATCOL.WIFIDIAG -- Wi-Fi Diagnostics Data Collection

For measuring the WiFi experience in the home, these requirements
specify which data is continuously collected about the state and
performance of the home Wi-Fi network(s).

!include temp/073-MGMT.DATCOL.WIFIDIAG.yaml

## IF - Interface Modules {#if---interface-modules .new-page}

### IF.WAN - WAN Interface Modules

#### IF.WAN.ADSL - ADSL and ADSL2+

!include temp/074-IF.WAN.ADSL.yaml

#### IF.WAN.VDSL2 - VDSL2

!include temp/075-IF.WAN.VDSL2.yaml

#### IF.WAN.xDSL - xDSL General Requirements

!include temp/076-IF.WAN.xDSL.yaml

##### IF.WAN.xDSL.INP - xDSL INP Values

!include temp/077-IF.WAN.xDSL.INP.yaml

##### IF.WAN.xDSL.BOND - xDSL Bonding

!include temp/078-IF.WAN.xDSL.BOND.yaml

##### IF.WAN.xDSL.REPORT - xDSL Reporting of Physical Layer Issues

!include temp/079-IF.WAN.xDSL.REPORT.yaml

##### IF.WAN.xDSL.SEALING - DC Sealing Current

!include temp/080-IF.WAN.xDSL.SEALING.yaml

##### IF.WAN.xDSL.SURGE - AC Power Surge Protection

!include temp/081-IF.WAN.xDSL.SURGE.yaml

#### IF.WAN.ETH - Ethernet (WAN)

!include temp/082-IF.WAN.ETH.yaml

#### IF.WAN.GPON - GPON

!include temp/083-IF.WAN.GPON.yaml

#### IF.WAN.XG-PON -- 10G PON

!include temp/084-IF.WAN.XG-PON.yaml

#### IF.WAN.XGS-PON -- XGS PON

!include temp/085-IF.WAN.XGS-PON.yaml

#### IF.WAN.MoCA - MoCA

!include temp/086-IF.WAN.MoCA.yaml

#### IF.WAN.FAST -- G.fast

!include temp/087-IF.WAN.FAST.yaml

##### IF.WAN.FAST.BOND -- G.fast Bonding

!include temp/088-IF.WAN.FAST.BOND.yaml

#### IF.WAN.LTE E-UTRA

!include temp/089-IF.WAN.LTE.yaml

#### IF.WAN.NR New Radio

!include temp/090-IF.WAN.NR.yaml

### IF.LAN - LAN Interface Modules

#### IF.LAN.ETH - Ethernet (LAN)

!include temp/091-IF.LAN.ETH.yaml

##### IF.LAN.ETH.SWITCH - Ethernet Switch

!include temp/092-IF.LAN.ETH.SWITCH.yaml

#### IF.LAN.USB - USB

##### IF.LAN.USB.PC - USB (PC)

!include temp/093-IF.LAN.USB.PC.yaml

#### IF.LAN.VOICE - Voice

##### IF.LAN.VOICE.ATA - Voice ATA Ports

!include temp/094-IF.LAN.VOICE.ATA.yaml

#### IF.LAN.WIRELESS -- Wireless

##### IF.LAN.WIRELESS.AP - Wireless: General Access Point Functions

!include temp/095-IF.LAN.WIRELESS.AP.yaml

###### IF.LAN.WIRELESS.AP.WEP - Wireless: Wired Equivalent Privacy

Note: WEP encryption is no longer secure and SHOULD not be used anymore

!include temp/096-IF.LAN.WIRELESS.AP.WEP.yaml

###### IF.LAN.WIRELESS.AP.WPA2 - Wireless: WPA2 Personal

!include temp/097-IF.LAN.WIRELESS.AP.WPA2.yaml

###### IF.LAN.WIRELESS.AP.WPA3 - Wireless: WPA3 Personal

!include temp/098-IF.LAN.WIRELESS.AP.WPA3.yaml

###### IF.LAN.WIRELESS.AP.WPA2-Enterprise - Wireless: Enterprise WPA2

!include temp/099-IF.LAN.WIRELESS.AP.WPA2-Enterprise.yaml

###### IF.LAN.WIRELESS.AP.WPA3-Enterprise - Wireless: Enterprise WPA3

!include temp/100-IF.LAN.WIRELESS.AP.WPA3-Enterprise.yaml

###### IF.LAN.WIRELESS.AP.ERP-Authenticator - Wireless: ERP Authenticator

!include temp/101-IF.LAN.WIRELESS.AP.ERP-Authenticator.yaml

##### IF.LAN.WIRELESS.11g - Wireless: 802.11g Access Point

!include temp/102-IF.LAN.WIRELESS.11g.yaml

##### IF.LAN.WIRELESS.11a - Wireless: 802.11a Access Point

!include temp/103-IF.LAN.WIRELESS.11a.yaml

##### IF.LAN.WIRELESS.11h - Wireless: 802.11h Access Point

!include temp/104-IF.LAN.WIRELESS.11h.yaml

##### IF.LAN.WIRELESS.11n - Wireless: 802.11n Access Point

!include temp/105-IF.LAN.WIRELESS.11n.yaml

##### IF.LAN.WIRELESS.11ac - Wireless: 802.11ac Access Point

!include temp/106-IF.LAN.WIRELESS.11ac.yaml

##### IF.LAN.WIRELESS.11ax - Wireless: 802.11ax Access Point

!include temp/107-IF.LAN.WIRELESS.11ax.yaml

#### IF.LAN.HomePNA - HomePNA (Phoneline/Coax

!include temp/108-IF.LAN.HomePNA.yaml

#### IF.LAN.MoCA - MoCA (LAN)

!include temp/109-IF.LAN.MoCA.yaml

#### IF.LAN.HomePlugAV - HomePlug AV (LAN)

!include temp/110-IF.LAN.HomePlugAV.yaml

#### IF.LAN.HomePlugAV2- HomePlug AV2 (LAN)

!include temp/111-IF.LAN.HomePlugAV2.yaml

#### IF.LAN.Ghn - G.hn (LAN)

!include temp/112-IF.LAN.Ghn.yaml

## SEC -- Security

### SEC.GEN -- General security

!include temp/113-SEC.GEN.yaml

### SEC.USERINTERFACE -- User Interface security

!include temp/114-SEC.USERINTERFACE.yaml

### SEC.FIRMWARE -- Firmware integrity and security

!include temp/115-SEC.FIRMWARE.yaml

## RGSMART -- Smart Residential Gateway

### RGSMART.OPLAT -- Open platform Support

*Note*: *With the evolution of home networks, The Smart RG needs to
support more and more third-party applications. Each Smart RG vendor has
different hardware and software operating environments. An open platform
allows to update the Smart RG with standardized additional software
applications, without the need to maintain different versions.*

!include temp/116-RGSMART.OPLAT.yaml

#### RGSMART.OPLAT.OSGI -- OSGI Open platform

!include temp/117-RGSMART.OPLAT.OSGI.yaml

#### RGSMART.OPLAT.EE -- Execution Environment

!include temp/118-RGSMART.OPLAT.EE.yaml

## REGIONAL - Regional Annexes

### REGIONAL.NA - North American

#### REGIONAL.NA.POWER - North American Power and Environmental

!include temp/119-REGIONAL.NA.POWER.yaml

#### REGIONAL.NA.LED - North American LED Indicators

!include temp/120-REGIONAL.NA.LED.yaml

#### WPS LED operation

  ---------- ------- ---------- ------------------------------------------
  WLAN WPS   Green   On for     The Wi-Fi protected setup (WPS, previously
  PBC                5min or    called "simple config") has been completed
  Security           until      successfully.
                     pressed    
                     again      

  WLAN WPS   Green   Slow       The Wi-Fi protected setup PBC procedure is
  PBC                flash:\    in progress.
  Security           2 Hz 50%   
                     duty cycle 

  WLAN WPS   Red     Solid      Error unrelated to security, such as
  PBC                           failed to find any partner, or protocol
  Security                      prematurely aborted.\
                                Recommended user action: press WPS button
                                to start protocol again.

  WLAN WPS   Red     Fast       Session overlap detected (possible
  PBC                flash:\    security risk)\
  Security           4 Hz 50%   Recommended user action: Wait for 2
                     duty cycle minutes, then press WPS button again to
                                reattempt. If the condition recurs, refer
                                the user to PIN-based configuration
                                method.

  WLAN WPS   Off                The device is ready for another
  PBC                           authentication.
  Security                      
  ---------- ------- ---------- ------------------------------------------

Note: This is a deviation from the three color indicator option and
behaviors described by the Wi-Fi Alliance, which however, will not
enforce any LED behavior as part of its WPS certification process.

{{drawing\|name=Bild 1\|descr=None}}

Figure %docxSeqFigure% -- WPS pushbutton method state machine

Timeout values are listed below:

-   Reset timeout -- 300 seconds
-   Restart timeout -- 120 seconds
-   Walk timeout -- 120 seconds
-   Monitor timeout -- 120 seconds

## 5G-WWC - 5G Wireless-Wireline Convergence

The 5G-WWC set of requirements define a WAN behavior that is exclusive
of the other behaviors defined in TR-124. For WWC this is referred to as
5G-RG mode of operation, and the non 5G behaviors are referred to as the
FN-RG mode of operation. A device may be configured to exclusively use
one mode of operation or the other, or may be a hybrid of the two via
either VLAN or Ethertype separation of WAN traffic into distinct
interfaces presenting a mix of 5G and non 5G interfaces to the device.

The following table illustrates the set of common and mode specific
functionalities between the two modes of operation.

  ----------------------------------------------------------------------------------------------------------
  **Mutually exclusive **Mutually exclusive **Mutually exclusive              
  requirements**       requirements**       requirements**                    
  -------------------- -------------------- --------------------------------- ------------------------------
  **5G-RG mode of      **5G-RG mode of      **FN-RG mode of operation**       **FN-RG mode of operation**
  operation**          operation**                                            

  5G-WWC               5G-WWC               WAN.CONNECT                       WAN.CONNECT

  5G-WWC.FWA           5G-WWC.FWA           WAN.CONNECT.ON-DEMAND             WAN.CONNECT.ON-DEMAND

  5G-WWC.WAN           5G-WWC.WAN           WAN.ETHOAM                        WAN.ETHOAM

  5G-WWC.Identifiers   5G-WWC.Identifiers   WAN.DHCPC.force                   WAN.DHCPC.force

  5G-WWC.WAN.CP        5G-WWC.WAN.CP        WAN.DHCPC.BFDecho                 WAN.DHCPC.BFDecho

  5G-WWC.WAN.UP        5G-WWC.WAN.UP        WAN.IPv6                          WAN.IPv6

  5G-WWC.WAN.UP.QOS    5G-WWC.WAN.UP.QOS    WAN.TRANS.6rd                     WAN.TRANS.6rd

                                            WAN.TRANS.DSLite                  WAN.TRANS.DSLite

                                            WAN.TRANS.v4-release-control      WAN.TRANS.v4-release-control

                                            WAN.TRANS.MAP-E                   WAN.TRANS.MAP-E

                                            WAN.PPP                           WAN.PPP

                                            WAN.PPP.IPv6                      WAN.PPP.IPv6

                                            WAN.dot1x                         WAN.dot1x

  **Common             **Common             **Common Requirements**           
  Requirements**       Requirements**                                         

                       WAN.DHCPC            WAN.DHCPC requirements            WAN.DHCPC requirements
                       requirements                                           

                       WAN.IPv6             WAN.IPv6 requirements 4, 5, 6, 7, WAN.IPv6 requirements 4, 5, 6,
                       requirements 4, 5,   8, 9, 14, & 19                    7, 8, 9, 14, & 19
                       6, 7, 8, 9, 14, & 19                                   

                       WAN.QOS requirements WAN.QOS requirements 3, 4, 9, 10, WAN.QOS requirements 3, 4, 9,
                       3, 4, 9, 10, 11, &   11, & 12                          10, 11, & 12
                       12                                                     

                       WAN.QOS.VLAN         WAN.QOS.VLAN                      WAN.QOS.VLAN

                       MGMT.REMOTE.TR-069   MGMT.REMOTE.TR-069                MGMT.REMOTE.TR-069
  ----------------------------------------------------------------------------------------------------------

Note: WAN.ATM & WAN.ATM.MULTI are out of scope.

It is recommended that implementers read TR-470 \[209\] 5G FMC
Architecture Overview in conjunction with interpreting these
requirements; in particular, the section 5G-RG Overview of Operation.

### 5G-WWC -- General 5G WWC

!include temp/121-5G-WWC.yaml

#### 5G-WWC.Identifiers -- 5G WWC Identifiers

!include temp/122-5G-WWC.Identifiers.yaml

#### 5G-WWC.FWA -- 5G WWC Fixed Wireless Access

##### 5G-WWC.FWA.IPTV -- 5G WWC Fixed Wireless Access IPTV

!include temp/123-5G-WWC.FWA.IPTV.yaml

#### 5G-WWC.WAN -- 5G WWC Wide Area Network

POST: *Note: A number of NAS procedures have error conditions that
mandate the 5G-RG NAS implementation 'back off' for a period of time
prior to re-attempting the operation. The set of procedures that result
in these conditions is documented in 3GPP TS24.501. The relevance of
these various error, resource or subscription issue conditions to a
5G-RG in relation to the set of timers associated with NAS operations is
discussed in Appendix 9.1 of TR-456i2 \[207\].*

!include temp/124-5G-WWC.WAN.yaml

##### 5G-WWC.WAN.RADIO -- 5G WWC Fixed Wireless Access Radio

!include temp/125-5G-WWC.WAN.RADIO.yaml

##### 5G-WWC.WAN.CP -- 5G WWC WAN Control Plane

POST: Note: PLMN selection defined in 3GPP TS 22.011 and in TS 23.122
are not applicable as described in clause 4.2.1 TS 23.316.

!include temp/126-5G-WWC.WAN.CP.yaml

##### 5G-WWC.WAN.UP -- 5G WWC WAN User Plane

!include temp/127-5G-WWC.WAN.UP.yaml

###### 5G-WWC.WAN.UP.QOS -- 5G WWC WAN User Plane QoS

!include temp/128-5G-WWC.WAN.UP.QOS.yaml

##### 5G-WWC.WAN.HO -- 5G WWC Multi-access handover support

A device that is equipped with both a wireline and a radio interface
(E-UTRA or NR) may implement resiliency on the basis of mobility
hand-off. This can be in the wireline to wireless direction or vice
versa.

!include temp/129-5G-WWC.WAN.HO.yaml

##### 5G-WWC.WAN.ATSSS -- 5G WWC ATSSS

Access traffic steering switching and splitting (ATSSS) is used to
permit a 5G-RG to simultaneously utilize both a 3GPP radio interface and
non-3GPP wireline interface. The 3GPP radio interface may be with either
a E-UTRAN (4G) or NG-RAN (5G). Requirements are specified for 5G
operation, and 4G operation via EPC interworking.

Note that for the BBF WWC work, roaming on either interface is
considered to be out of scope. What is in scope is referred to as
Non-roaming and Roaming with Local Breakout architecture for ATSSS
support in TS 23.501.

TS 23.502 defines the procedures and TS 24.193 provides the stage 3
definition. Impacts to the NAS protocol for ATSSS is described in TS
24.501.

A rough narrative of operation is that:

1.  5G-RG registers with a common PLMN on both the 3GPP and non-3GPP
    interfaces. A security context is established with the first
    registration that is simply referenced by the second association via
    the 5G-GUTI.

2.  The 5G-RG establishes a multi-access (MA) PDU session. Note that
    both the 3GPP radio and wireline interfaces may be 5G, or the 3GPP
    radio interface may be via LTE and employing EPS interworking. When
    both interfaces are 5G, this can be done with a single MA-PDU
    session establish request, assuming that the 5G-RG is already
    registered in both accesses before initiating the PDU Session
    Establishment procedure. When the radio interface is a E-UTRA
    interface, the 'legs' of the MA-PDU session must be separately
    established. During session establishment the 5G-RG is provided with
    ATSSS Rules that contain traffic distribution policies.

3.  The 5G RG distributes traffic across the set of upstream interfaces
    according to ATSSS Rules received from the 5G System.

!include temp/130-5G-WWC.WAN.ATSSS.yaml

#### 5G-WWC.LAN -- 5G WWC LAN

##### 5G-WWC.LAN.DHCPS -- 5G WWC LAN DHCPv4

!include temp/131-5G-WWC.LAN.DHCPS.yaml

##### 5G-WWC.LAN.ADDRESSv6 -- 5G WWC LAN SLAAC

!include temp/132-5G-WWC.LAN.ADDRESSv6.yaml

# IPv6 Flow Diagrams {#ipv6-flow-diagrams .annex .new-page}

The flows in this annex are referenced by requirements in the body, and
are therefore normative.

WAN PPPoE Automated Connection Flow

{{embeddedObject\|progId=PowerPoint.Slide.8}}

Figure %docxSeqFigure% -- WAN PPPoE automated connection flow

## WAN IPv6 Automated Connection Flow {#wan-ipv6-automated-connection-flow .new-page}

This flow assumes no manually configured prefix or address.

{{embeddedObject\|progId=PowerPoint.Slide.8}}

Figure %docxSeqFigure% -- WAN IPv6 automated connection flow

## Receive Router Advertisement Subroutine Flow {#receive-router-advertisement-subroutine-flow .new-page}

{{embeddedObject\|progId=PowerPoint.Slide.8}}

Figure %docxSeqFigure% -- Receive router advertisement subroutine flow

# Application Level Gateway (ALG) and Port Forwarding List {#application-level-gateway-alg-and-port-forwarding-list .appendix .new-page}

This appendix is a partial list of applications and protocols that
should work through the usage of predefined port forwarding
configurations and ALGs. It is not a comprehensive list of all
applications. It is expected that support for more applications will be
needed with time.

**D**

DNS Server

**F**

FTP Client, FTP Server, FW1VPN

**H**

H.323, HTTP Server, HTTPS Server

**I**

ICMP Echo, IIMAP Client, IMAP Client v.3, IMAP server, Internet Phone,
Internet Phone Addressing Server, IPsec Encryption, IPsec ESP, IPsec
IKE, IRC

**L**

L2TP

**M**

mIRC DCC, IRC DCC, mIRC Chat, mIRC IDENT

**N**

NNTP Server, NTP

**P**

POP Client, POP3 Server, PPTP

**R**

RDP, Remote Desktop 32Rlogin/Rcp, RTSP

**S**

SDP, SIP, SMTP Server, SQL\*NET Tools, SSH Secure Shell, SSH Server

**T**

Telnet Server

**U**

USENET News Service

**W**

Web Server, Windows 2000 Terminal Server

**X**

X Windows, XP Remote Desktop

# Example Queuing for an RG {#example-queuing-for-an-rg .appendix .new-page}

This section presents the queuing and scheduling discipline envisioned
for upstream traffic through the RG in support of future service
offerings delivered over the architecture described in TR-059.

{{drawing\|name=Bild 5\|descr=None}}

Figure %docxSeqFigure% -- Upstream Queuing and Scheduling Example for RG

In Figure 5, the following abbreviations apply:

ASP -- Application service provider

PTA -- PPP terminated aggregation

PPP -- Point-to-point protocol

EF -- Expedited forwarding -- as defined in IETF RFC 3246

AF -- Assured forwarding -- as defined in IETF RFC 2597

BE -- Best effort forwarding

RL -- Rate limiter

∑RL -- Summing rate limiter (limits multiple flows)

S -- Scheduler

Multiple access sessions are supported in this model. However, all
traffic is classified and scheduled in a monolithic system. So, while it
might appear at first that the Diffserv queuing and scheduling might
apply only to IP-aware access, in fact all access, IP, Ethernet, or PPP
is managed by the same system that adheres to the Diffserv model.

For example, at the bottom of Figure 5, BE (best effort) treatment is
given to the non-IP-aware access sessions (PPPoE started behind the RG
or delivered to an L2TP tunnel delivery model). This queue might be
repeated several times in order to support fairness among multiple PPPoE
accesses, or it might be a monolithic queue with separate rate limiters
applied to the various access sessions.

The PTA access is a single block of queues. This is done because NSP
access typically works with a single default route to the NSP, and
managing more than one simultaneously at the RG would be perilous. The ∑
rate limiter would limit the overall access traffic for a service
provider.

Rate limiters are also shown within the EF and AF service classes
because the definition of those diffserv types is based on treating the
traffic differently when it falls into various rates.

Finally, at the top of the diagram is the ASP access block of queues. In
phase 1A of the TR-059 architecture, these queues are provisioned and
provide aggregate treatment of traffic mapped to them. In phase 1B, it
will become possible to assign AF queues to applications to give them
specific treatment instead of aggregate treatment. The EF service class
may also require a high degree of coordination among the applications
that make use of it so that its maximum value is not exceeded.

Notable in this architecture is that all the outputs of the EF, AF, and
BE queues are sent to a scheduler (S) that pulls traffic from them in a
strict priority fashion. In this configuration EF traffic is, obviously,
given highest precedence and BE is given the lowest. The AF service
classes fall in between.

Note that there is significant interest in being able to provide a
service arrangement that would allow general Internet access to have
priority over other (bulk rate) services.[^1] Such an arrangement would
be accomplished by assigning the bulk rate service class to BE and by
assigning the default service class (Internet access) as AF with little
or no committed information rate.

Given this arrangement, the precedence of traffic shown in the figure is
arranged as:

EF -- red dotted line

AF -- blue dashed line (with various precedence among AF classes as
described in IETF RFC 2597)

BE -- black solid line

# Routed Architecture -- Examples of Potential Configurations {#routed-architecture-examples-of-potential-configurations .appendix .new-page}

## Introduction

The pictures and descriptions in the following scenarios are intended to
provide examples of the interworking of many of the requirements in this
document.

Since the single PC case is a simple subset of the multi-PC case (except
when explicitly using the single PC mode of operation (LAN.DHCPS.19)),
it will not be directly addressed. The network used in this sequence of
examples has 5 PCs, which are described as being connected over
Ethernet. For purposes of these scenarios, neither the physical network
nor the nature of the attached devices is significant.

## Basic RG as Router Initiating One or More PPPoE Sessions

The four scenarios that follow build on one another to describe a number
of the capabilities required in this document. They show PPPoE being
used in all cases for WAN connectivity, with the embedded DHCP server in
the RG enabled.

### No WAN Connection

-   The router has no WAN connection up.

-   The router has been configured to give PC2 its WAN address via its
    embedded DHCP server. Since the router has no WAN connection, it
    will give PC2 a private address with a 10 minute lease time (as
    defined in LAN.DHCPS.12).

-   PC5 has been configured with a static IP address.

-   PCs 1-4 are configured to make DHCP requests. The router responds to
    all DHCP requests with IP addresses in the range of 192.168.1.64 to
    192.168.1.253 (LAN.DHCPS.8), an IP gateway address (and LAN-side
    address of the device) of 192.168.1.254 (LAN.DHCPS.14), a DNS server
    address of 192.168.1.254 (LAN.DNS.1) and an IP address lease time
    for all PCs but PC2 of 24 hours (LAN.DHCPS.11).

{{drawing\|name=Bild 6\|descr=None}}

Figure %docxSeqFigure% -- Example: No WAN Connection Configuration

### Router Sets Up PPPoE to an ISP

This scenario is the same as presented in the "No WAN Connection"
example above with the following exceptions:

-   The router sets up a PPPoE session to ISP -- it obtains an IP
    address and DNS server addresses via IPCP (WAN.PPP.1)

-   The router gives its public IP address to PC2 (LAN.DHCPS.18) when
    PC2's lease expires.

-   The router is configured to allow PC2 to communicate with other
    devices on the LAN (LAN.ADDRESS.8).

{{drawing\|name=Bild 7\|descr=None}}

Figure %docxSeqFigure% -- Example: Router Sets Up PPPoE to an ISP

### PC3 Sets Up Its Own PPPoE Session

This scenario is the same as presented in [III.2.1](#no-wan-connection)
with the following exceptions:

-   PC3 uses a PPPoE client to establish its own PPPoE session. While
    the private IP address from the router is still associated with
    PC3's Ethernet interface, PC3 also has a public IP address
    associated with its own PPPoE interface. Common behavior is for all
    IP traffic of PC3 to now use this PPPoE interface (WAN.PPP.10,
    LAN.FWD.5).

{{drawing\|name=Bild 8\|descr=None}}

Figure %docxSeqFigure% -- Example: PC3 sets up its own PPPoE Session

### Router Sets Up a Second PPPoE Session

This scenario is the same as presented in [III.2.1](#no-wan-connection)
with the following exceptions:

-   The router sets up second PPPoE session (PPPoEC). It gets an IP
    address and DNS addresses through IPCP. It gets routing information
    from RIP-2 (LAN.FWD.15), manual entry, or other mechanisms
    (LAN.FWD.8). PPPoEA remains the default route (LAN.FWD.20).

-   PC5 requests a DNS lookup for a URL. The router sends simultaneous
    URL lookup requests to DNS servers on both PPPoE connections. The
    DNS server on the PPPoEA connection fails to resolve the URL and the
    PPPoEC connection returns an IP address. The router returns the IP
    address to PC5 (LAN.DNS.3).

-   PC5 sends IP packets to the returned IP address. The router
    determines from its routing table that this goes to the PPPoEC
    connection.

{{drawing\|name=Bild 9\|descr=None}}

Figure %docxSeqFigure% -- Example: Router sets up a Second PPPoE Session

## "RFC 2684 Bridged" Mode

The next three scenarios deal IETF RFC 2684 bridged mode configuration
cases where the network is not expecting a PPP login or the router is
not doing PPP. The first case has the router using its DHCP client to
the WAN, acting as a DHCP server to the LAN, and doing routing and NAPT
to PCs on the LAN. The second case has the router not establishing a WAN
connection, and individual PCs setting up their own PPPoE sessions. In
the third case, the router's embedded DHCP server is also disabled, and
the PCs are getting IP addresses from the WAN.

### Router in IP-routed "RFC 2684 Bridged" Mode, Embedded DHCP Server On

-   The router provides an IP address to each device that it receives a
    DHCP request from.

-   PC5 uses a static IP address and does not send a DHCP request to the
    router.

-   The router has been configured to give PC2 its WAN address. When the
    router has no WAN connection, it gives PC2 a private address with a
    short lease time.

-   The router issues a DHCP request and establishes an IP session to
    the WAN (WAN.ATM.3, WAN.ATM.4, LAN.FWD.1).

-   The router gives its public IP address to PC2.

{{drawing\|name=Bild 10\|descr=None}}

Figure %docxSeqFigure% -- Example: Router in 2684 Bridged Mode with DHCP
Server On

### Router in Bridged Mode, Embedded DHCP Server On

-   The router provides a private IP address to each device that it
    receives a DHCP request from (LAN.DHCPS.3).

-   The router does not establish any IP or PPP sessions to the WAN.

-   No device can get a DHCP response from the WAN, since the router
    will intercept all DHCP requests that come to it.

-   PC1 and PC3 each use a PPPoE client to establish their own PPPoE
    sessions (WAN.PPP.10, LAN.FWD.5). While the private IP address from
    the router is still associated with their PC Ethernet interfaces,
    PC1 and PC3 also have a public IP address associated with their
    respective PPPoE interfaces. Common behavior is for all IP traffic
    of PC1 and PC3 to now use their own PPPoE interfaces.

-   PCs that do not establish their own PPPoE connection cannot connect
    to the WAN, but they can communicate with other PCs on the LAN.

{{drawing\|name=Bild 11\|descr=None}}

Figure %docxSeqFigure% -- Example: Router in Bridged Mode with DHCP
Server On

### Router in Bridged Mode, Embedded DHCP Server Off

-   The router does not establish any IP or PPP sessions to the WAN.

-   All DHCP requests are bridged onto the WAN (WAN.BRIDGE.1).

-   In this example, PC5 does not have a static IP address.

{{drawing\|name=Bild 12\|descr=None}}

Figure %docxSeqFigure% -- Example: Router in Bridged Mode with DHCP
Server off

## Single PC Mode of Operation

-   The router is configured to use the single PC mode of operation
    (LAN.DHCPS.19).

-   The router's embedded DHCP server is on. The embedded DHCP server
    has only one address lease available in this case.

-   PC1 is the first device seen, so it is identified as the "single
    PC".

-   PC1 is provided with a private IP address and 1:1 NAT is performed
    between the WAN and PC1 by the router. The subnet mask sent to PC1
    is 255.255.255.0.

-   Alternately PC1 could be given the router's public address instead,
    as with PC2 in the scenarios in section
    [III.2](#basic-rg-as-router-initiating-one-or-more-pppoe-sessions).

{{drawing\|name=Bild 15\|descr=None}}

Figure %docxSeqFigure% -- Example: Single PC Mode of Operation

## Simultaneous IP and PPPoE WAN Sessions

TR-059 requirements have PPPoE and IP sessions running simultaneously
over the same PVC. Here are some examples of how this might look,
assuming the network is capable of terminating PPPoE and IP at the same
time on the same PVC.

Note: Simultaneous IP and PPPoE is not well supported in the network
today. Most equipment terminating the ATM PVC does not support both IP
and PPPoE connections at the same time.

### Router in IP-routed "2684 Bridged" Mode, Embedded DHCP Server On

-   The router provides an IP address to each device that it receives a
    DHCP request from.

-   PC5 uses a static IP address and does not send a DHCP request to the
    router.

-   The router has been configured to give PC2 its WAN address. When the
    router has no WAN connection, it gives PC2 a private address with a
    10 minute lease time.

-   The router issues a DHCP request and establishes an IP session to
    the WAN.

-   The router gives its public IP address to PC2.

-   PC3 uses a PPPoE client to establish its own PPPoE session
    (WAN.PPP.10, LAN.FWD.5). While the private IP address from the
    router is still associated with PC3's Ethernet interface, PC3 also
    has a public IP address associated with its own PPPoE interface.
    Common behavior is for all IP traffic of PC3 to now use this PPPoE
    interface.

{{drawing\|name=Bild 13\|descr=None}}

Figure %docxSeqFigure% -- Example: Router in Routed 2684 Mode

### Router Sets Up IP as a Second Session

Assuming the scenario in section
[III.2.3](#pc3-sets-up-its-own-pppoe-session) as a base, add:

-   The router sets up connection IPC (LAN.FWD.19). It gets an IP
    address and DNS addresses through a DHCP client request. It gets
    routing information from RIP-2 (LAN.FWD.15). PPPoEA remains the
    default route.

-   PC5 requests a DNS lookup for a URL. The router sends simultaneous
    URL lookup requests to DNS servers on both connections. The DNS
    server on the PPPoEA connection fails to resolve the URL and the IPC
    connection returns an IP address. The router returns the IP address
    to PC5 (LAN.DNS.3).

-   PC5 sends IP packets to the returned IP address. The router
    determines from its routing table that this goes to connection IPC.

{{drawing\|name=Bild 14\|descr=None}}

Figure %docxSeqFigure% -- Example: Router sets up Second IP Connection

## Router Embedded DHCP Server Gives Out Public IP Addresses (from use of IPCP extension)

-   The router initially gives private IP addresses to PCs, before
    setting up its PPPoE session.

-   The router sets up PPPoE to ISP and gets IP address and DNS server
    addresses via IPCP. It also gets a subnet mask via an IPCP extension
    (WAN.DHCPC.1, WAN.PPP.12).

-   The router gives public IP addresses to certain PCs when they issue
    DHCP requests again (LAN.DHCPS.18).

-   PC5 is set for static IP and does not issue a DHCP request.

# Bridged Architecture -- Examples of Potential Configurations {#bridged-architecture-examples-of-potential-configurations .appendix .new-page}

## Introduction

The pictures and descriptions in the following scenarios are intended to
provide examples of the bridge interworking of many of the requirements
in this document.

The network used in this sequence of examples has 5 PCs, which are
described as being connected over Ethernet. For purposes of these
scenarios, the physical network and the exact nature of the connected
devices are not relevant.

## Managed Bridge

-   The RG will have an IP address for management as (described in
    section WAN.BRIDGE), which is obtained using a DHCP client on the
    WAN interface. This address can also be used for other gateway
    originated services such as an attached telephony device.

-   The DHCP server of the RG is configured with the appropriate IP
    address range and subnet mask by the Controller.

-   The PCs are configured to use DHCP for assignment of an IP address.
    All DHCP requests from the PCs are processed by the DHCP server
    (described in section LAN.DHCPS\] on the RG. Note that the scope of
    these addresses is specific to the service provider network
    (i.e. they may be public or private depending on the access network
    design). If private, it is assumed that the service provider has the
    NAT functionality in its network.

-   All subsequent data exchanges between the PCs and the RG are
    performed using 802.1D bridging techniques (described in section
    WAN.BRIDGE).

-   The RG filters specific message types (e.g. UPnP or DHCP) from being
    sent to the WAN (described in section LAN.FW).

{{drawing\|name=Bild 16\|descr=None}}

Figure %docxSeqFigure% -- Example: Managed Bridge Configuration

### Local Management

-   The RG may allow access to a local management interface via a
    default address (described in section LAN.ADDRESS).

## Unmanaged Bridge

-   The RG does not establish any layer 3 connectivity to the WAN.

-   All DHCP requests from the PCs are bridged to the WAN (described in
    section WAN.BRIDGE).

{{drawing\|name=Bild 17\|descr=None}}

Figure %docxSeqFigure% -- Example: Unmanaged Bridge Configuration

### Local Management

-   The RG may allow access to a local management interface via a
    default address (described in section LAN.ADDRESS).

# Sealing Current References {#sealing-current-references .appendix .new-page}

Sealing current is also known in the telecommunications industry as
wetting current. Sealing current may be sourced by the ATU-C in certain
service providers that deploy "dry loop" DSL circuits, meaning that DSL
is delivered in the absence of typical central office or remote terminal
fed analog POTS service on the copper pair.

The following functional diagram depicts a sealing current circuit
design specified in the IF.WAN.SEALING optional module that can be
implemented on an xDSL residential gateway.

{{drawing\|name=Bild 18\|descr=None}}

Figure %docxSeqFigure% -- Sealing current reference design

# Product Profile Template {#product-profile-template .appendix .new-page}

## Introduction

To accommodate the many different residential gateway implementations
that will be needed due to various localized market needs, LAN/WAN
interfaces, and different services that will be delivered in operators'
networks, %bbfNumber% endeavors to define a superset of general
requirements and optional modules that can be implemented on a
residential gateway.

In order to create a specific product based on the %bbfNumber%
modularized requirements, it is necessary for either the Broadband Forum
(in the form of new TR documents) or for individual network operators to
specify the following details to define a specific desired product
implementation:

1.  A filled out product profile matrix template as shown in the example
    below to indicate required modules

2.  Any line item edits to requirements (changes to current %bbfNumber%
    requirements).

3.  Any additional new requirements that are needed in the product.

4.  Any configuration defaults needed. These should refer to %bbfNumber%
    requirements that establish a different or new default value
    required in the implementation.

5.  Localized regulatory, certifications, powering and product labeling
    requirements as necessary.

## Instructions for Completing a Product Profile Template

The following instructions apply to filling out the product profile
template below:

-   Any modules marked with a check mark
    ({{symbolChar\|font=Wingdings\|char=F0FC}}) will be considered
    required, meaning that all MUST requirements in that section are to
    be satisfied (with the exception of any specific line item edits
    that have been made as discussed in section
    [VI.1](#introduction-2)).

-   Any modules that are *not* marked with a check MAY be implemented on
    the product, but are not considered required. Any vendor
    implementing any module, regardless of being considered required or
    not, MUST comply with all MUST requirements in the module
    (i.e. partial implementations of a module MUST NOT be provided).

-   If a module is explicitly not to be included in the product, it must
    be marked with an x mark ({{symbolChar\|font=Wingdings\|char=F0FB}})
    to indicate that it MUST NOT be included.

-   For the optional LAN/WAN modules, where appropriate it may be
    necessary to specify the number or ports/lines to be implemented
    (e.g. "Qty. 4" under the IF.LAN.ETH.SWITCH to indicate 4 ports).

## Product Profile Template

  -------------------------------------------------------------------------------------
  Section                          Title                                  Required?\
                                                                          (,, or
                                                                          blank)
  -------------------------------- -------------------------------------- -------------
  **GEN**                          **General Device Requirements**        

  DESIGN                           Design                                 

  OPS                              Device Operation                       

  NET                              Networking Protocols                   

  NETv6                            IPv6 Networking Protocols              

  **WAN**                          **Wide Area Networking (WAN)**         

  ATM                              ATM                                    

  ATM.MULTI                        ATM Multi-PVC                          

  CONNECT                          Connection Establishment               

  CONNECT.ON-DEMAND                On-Demand Connection Establishment     

  ETHOAM                           Ethernet OAM                           

  BRIDGE                           Bridging                               

  DHCPC                            DHCP Client (DHCPv4)                   

  DHCPC.FORCE                      Force renew                            

  DHCPC.BFDecho                    BFD echo                               

  DHCPC.BFDKA                      BFD Keep-alive                         

  DHCPv4                           DHCP Client (DHCPv4)                   

  DHCPv4.ERP                       EAP Reauthentication (ERP) for DHCPv4  

  DHCPv6                           DHCP Client (DHCPv6)                   

  DHCPv6.ERP                       EAP Reauthentication (ERP) for DHCPv6  

  IPv6                             IPv6 WAN Connection                    

  TRANS.6rd                        6rd Transition Mechanism               

  TRANS.DS-LITE                    Dual Stack Lite Transition Mechanism   

  TRANS.V4-release-control         IPv6 connectivity with content-based   
                                   IPv4 release control transition        
                                   mechanism                              

  TRANS.MAP-E                      IPv6 connectivity with content-based   
                                   IPv4 release control transition        
                                   mechanism                              

  PPP                              PPP Client                             

  PPP.IPv6                         PPP Client for establishment of IPv6   
                                   connection                             

  dot1x                            802.1x Client                          

  DoS                              Denial of Service Prevention           

  QoS                              Quality of Service                     

  QoS.VLAN                         VLAN based QoS                         

  QoS.TUNNEL                       Quality of Service for Tunneled        
                                   Traffic                                

  IPsecClient                      IPsec VPN peer to peer                 

  L2tpClient                       L2tp VPN Remote Access                 

  PCP                              Port Control Protocol                  

  WAN.TUN                          WAN Tunnel                             

  **LAN**                          **Local Area Networking (LAN)**        

  GEN                              General LAN Protocols                  

  ADDRESS                          Private IPv4 Addressing                

  ADDRESSv6                        LAN IPv6 Addressing                    

  DHCPS                            DHCPv4 Server                          

  DHCPv6S                          DHCPv6 Server                          

  DNS                              Naming Services (IPv4 and general      
                                   requirements)                          

  DNSv6                            Naming Services (IPv6)                 

  NAT                              NAT/NAPT                               

  PFWD                             Port Forwarding (IPv4)                 

  PFWDv6                           Port Forwarding (IPv6)                 

  ALG                              ALG Functions (IPv4)                   

  FWD                              Connection Forwarding                  

  IGMP.BRIDGED                     IGMP and Multicast in Bridged          
                                   Configurations (IPv4)                  

  IGMP.ROUTED                      IGMP and Multicast in Routed           
                                   Configurations (IPv4)                  

  MLD.ROUTED                       MLD and Multicast in Routed            
                                   Configurations (IPv6)                  

  FW                               Firewall (Basic)                       

  FW.SPI                           Firewall (Advanced)                    

  FILTER.TIME                      Time of Day Filtering                  

  FILTER.CONTENT                   Content Filtering                      

  DIAGNOSTICS                      Automated User Diagnostics             

  CAPTIVE                          Captive Portal with Web Redirection    

  QOS                              LAN quality of service requirements    

  SIPserver                        SIP Server                             

  SIPmixer                         SIP Mixer                              

  Interworking.UE-Authentication   3GPP User Equipment Authentication     
                                   Support                                

  **MGMT**                         **Management & Diagnostics**           

  GEN                              General                                

  UPnP                             UPnP                                   

  UPnP.IGD                         UPnP IGD                               

  UPnP.IGD.ACRF                    UPnP IGD to allow Connection Request   
                                   Forwarding                             

  LOCAL                            Local Management                       

  LOCAL.TR-064                     TR-064 Issue 2                         

  REMOTE.TR-069                    Remote Management (TR-069)             

  REMOTE.USP                       Remote Management (USP)                

  REMOTE.WEB                       Remote Management (Web Browser)        

  NTP                              Network Time Client                    

  MGMT.DATCOL                      Data collection Requirements           

  MGMT.DATCOL.WIFIDIAG             Wi-Fi Diagnostics Data Collection      

  **IF.WAN**                       **WAN Interface Modules**              **Enter
                                                                          Quantity**

  ADSL                             ADSL and ADSL2+                        

  VDSL2                            VDSL2                                  

  xDSL                             xDSL General Requirements              

  xDSL.INP                         xDSL INP Values                        

  xDSL.BOND                        xDSL Bonding                           

  xDSL.REPORT                      xDSL Reporting of Physical Layer       
                                   Issues                                 

  xDSL.SEALING                     DC Sealing Current                     

  xDSL.SURGE                       AC Power Surge Protection              

  ETH                              Ethernet (WAN)                         

  GPON                             GPON                                   

  XG-PON                           10G PON                                

  XGS-PON                          XGS PON                                

  MoCA                             MoCA (WAN)                             

  **IF.LAN**                       **LAN Interface Modules**              **Enter
                                                                          Quantity**

  ETH                              Ethernet (LAN)                         

  ETH.SWITCH                       Ethernet Switch                        

  USB.PC                           USB (PC)                               

  VOICE.ATA                        Voice ATA Ports                        

  WIRELESS.AP                      Wireless: General Access Point         
                                   Functions                              

  WIRELESS.AP.WEP                  Wireless: Wired Equivalent Privacy     

  WIRELESS.AP.WPA2                 Wireless: WPA2-Personal                

  WIRELESS.AP.WPA3                 Wireless: WPA3-Personal                

  WIRELESS.AP.WPA2-Enterprise      Wireless: WPA2-Enterprise              

  WIRELESS.AP.WPA3-Enterprise      Wireless: WPA3-Enterprise              

  WIRELESS.AP.ERP-Authenticator    Wireless: ERP Authenticator            

  WIRELESS.11g                     Wireless: 802.11g Access Point         

  WIRELESS.11a                     Wireless: 802.11a Access Point         

  WIRELESS.11h                     Wireless: 802.11h Access Point         

  WIRELESS.11n                     Wireless: 802.11n Access Point         

  WIRELESS.11ac                    Wireless: 802.11ac Access Point        

  WIRELESS.11ax                    Wireless: 802.11ax Access Point        

  HomePNA                          HomePNA (Phoneline/Coax)               

  MoCA                             MoCA (LAN)                             

  HomePlugAV                       HomePlug AV (LAN)                      

  HomePlugAV2                      HomePlug AV2 (LAN)                     

  Ghn                              G.hn                                   

  **SEC**                          **Security**                           

  GEN                              General security                       

  USERINTERFACE                    User Interface security                

  **RGSMART**                      **Smart Residential Gateway**          

  OPLAT                            Open platform Support                  

  OPLAT.OSGI                       Open platform Support : OSGI Open      
                                   platform                               

  OPLAT.EE                         Open platform Support : Execution      
                                   Environment                            

  **REGIONAL**                     **Regional Annexes**                   

  NA.Power                         North American Power and Environmental 

  NA.LED                           North American LED Indicators          
  -------------------------------------------------------------------------------------

!include back-matter.md

[^1]: This "bulk rate" service class would typically be used for
    background downloads and potentially for peer-to-peer applications
    as an alternative to blocking them entirely.
