import re

output = """/Global_NOP/IL_Shapers/4mb_ADSL_No_Shaping/DUMMY-PacketShaper-PS01/135-10004197# measure dump class all by var 8h bytes avg-bps
"time:08-Mar-2018 06:54:00"
"class-var","/Inbound/Secondary/Dummy_Testing/HDS_NAS","/Inbound/Primary/Dummy_Testing/UEV","/Inbound/Primary/Dummy_Testing/HDS_NAS","/Outbound/Secondary/RAS/TW3-RAS","/Outbound/Secondary/RAS/RWS2-Watford-XKpool","/Outbound/Secondary/RAS/RWS2-Watford-DHCP","/Outbound/Secondary/RAS/RWS2-DummySite-XKpool","/Outbound/Secondary/RAS/RWS2-DummySite-DHCP","/Outbound/Secondary/RAS/RAS2-BBP","/Outbound/Secondary/RAS/RAS2-ACP","/Outbound/Secondary/RAS","/Outbound/Secondary/Dummy_Testing/ExchangeHybrid","/Outbound/Primary/RAS/TW3-RAS","/Outbound/Primary/RAS/RWS2-Watford-XKpool","/Outbound/Primary/RAS/RWS2-DummySite-DHCP","/Outbound/Primary/RAS/RWS2-DummySite-XKpool","/Outbound/Primary/RAS/RWS2-DummySite-DHCP","/Outbound/Secondary","/Outbound/Primary/RAS/RAS2-BBP","/Outbound/Primary/RAS/RAS2-DummySite","/Outbound/Primary/RAS","/Outbound/Primary/Dummy_Testing/ExchangeHybrid","/Outbound/SyntheticTransactions/DummySite128.8","/Inbound/SyntheticTransactions/X.X.X.X","/Outbound/SyntheticTransactions/X.X.X.X","/Inbound/SyntheticTransactions/X.X.X.X","/Outbound/SyntheticTransactions/X.X.X.X","/Inbound/SyntheticTransactions/X.X.X.X","/Outbound/SyntheticTransactions/X.X.X.X","/Inbound/Secondary/RAS/TW3-RAS","/Inbound/Secondary/RAS/RWS2-DummySite-XKpool","/Inbound/Secondary/RAS/RWS2-DummySite-DHCP","/Outbound/Telnet","/Outbound/SSL","/Outbound/SOAP-HTTP","/Outbound/SMTP","/Outbound/SameSide","/Inbound/Secondary/RAS/RWS2-DummySite-XKpool","/Outbound/Oracle/Oracle-CASM","/Outbound/Oracle/Default","/Outbound/Oracle","/Outbound/MS-Exchange","/Outbound/MS-ActiveDir","/Inbound/Secondary/RAS/RWS2-DummySite-DHCP","/Inbound/Secondary/RAS/RAS2-BBP","/Inbound/Secondary/RAS/RAS2-DummySite","/Inbound/Secondary/RAS","/Inbound/Secondary/Dummy_Testing/ExchangeHybrid","/Inbound/Primary/RAS/TW3-RAS","/Inbound/Primary/RAS/RWS2-DummySite-XKpool","/Inbound/Primary/RAS/RWS2-DummySite-DHCP","/Outbound/VOIP","/Inbound/Primary/RAS/RWS2-DummySite-XKpool","/Inbound/Primary/RAS/RWS2-DummySite-DHCP","/Inbound/Primary/RAS/RAS2-BBP","/Inbound/Primary/RAS/RAS2-DummySite","/Inbound/Primary/RAS","/Inbound/Primary/Dummy_Testing/ExchangeHybrid","/Outbound/Secondary/EUCS/SCCM/SCCM-F","/Outbound/Secondary/EUCS/SCCM/SCCM-C","/Outbound/Secondary/EUCS/SCCM","/Outbound/Secondary/EUCS","/Outbound/Primary/EUCS/SCCM/SCCM-F","/Outbound/Primary/EUCS/SCCM/SCCM-C","/Outbound/Primary/EUCS/SCCM","/Outbound/Primary/EUCS","/Inbound/Secondary/EUCS/SCCM/SCCM-F","/Inbound/Secondary/EUCS/SCCM/SCCM-C","/Inbound/Secondary/EUCS/SCCM","/Inbound/Secondary/EUCS","/Inbound/Primary/EUCS/SCCM/SCCM-F","/Inbound/Primary/EUCS/SCCM/SCCM-C","/Inbound/Primary/EUCS/SCCM","/Inbound/Primary/EUCS","/Outbound/Secondary/O365/O365_F5_VIP_DummySite","/Outbound/Secondary/O365/O365_F5_VIP_DummySite","/Outbound/Secondary/O365","/Outbound/Primary/O365/O365_F5_VIP_DummySite","/Outbound/Primary/O365/O365_F5_VIP_DummySite","/Outbound/Primary/O365","/Inbound/Secondary/O365/O365_F5_VIP_DummySite","/Inbound/Secondary/O365/O365_F5_VIP_DummySite","/Inbound/Secondary/O365","/Inbound/Primary/O365/O365_F5_VIP_DummySite","/Inbound/Primary/O365/O365_F5_VIP_DummySite","/Inbound/Primary/O365","/Outbound/Secondary/Logica_Services/DMU","/Outbound/Primary/Logica_Services/DMU","/Inbound/Secondary/Logica_Services/DMU","/Inbound/Primary/Logica_Services/DMU","/Outbound/Secondary/Logica_Services/App_Reg","/Outbound/Primary/Logica_Services/App_Reg","/Inbound/Secondary/Logica_Services/App_Reg","/Inbound/Primary/Logica_Services/App_Reg","/Outbound/Secondary/Dummy_Testing/ISAProxy/DummyProxy/Websites","/Outbound/Secondary/Dummy_Testing/ISAProxy/DummyProxy/Web_Streaming","/Outbound/Secondary/Dummy_Testing/ISAProxy/DummyProxy/Phoenix","/Outbound/Secondary/Dummy_Testing/ISAProxy/DummyProxy/FTP","/Outbound/Secondary/Dummy_Testing/ISAProxy/DummyProxy/Default","/Outbound/Secondary/Dummy_Testing/ISAProxy/DummyProxy","/Outbound/Secondary/Dummy_Testing/ISAProxy/ProxyDummySite/Websites","/Outbound/Secondary/Dummy_Testing/ISAProxy/ProxyDummySite/Web_Streaming","/Outbound/Secondary/Dummy_Testing/ISAProxy/ProxyDummySite/Phoenix","/Outbound/Secondary/Dummy_Testing/ISAProxy/ProxyDummySite/FTP","/Outbound/Secondary/Dummy_Testing/ISAProxy/ProxyDummySite/Default","/Outbound/Secondary/Dummy_Testing/ISAProxy/ProxyDummySite","/Outbound/Secondary/Dummy_Testing/ISAProxy","/Outbound/Primary/Dummy_Testing/ISAProxy/DummyProxy/Websites","/Outbound/Primary/Dummy_Testing/ISAProxy/DummyProxy/Web_Streaming","/Outbound/Primary/Dummy_Testing/ISAProxy/DummyProxy/Phoenix","/Outbound/Primary/Dummy_Testing/ISAProxy/DummyProxy/FTP","/Outbound/Primary/Dummy_Testing/DummyProxy/DummyProxy/Default","/Outbound/Primary/Dummy_Testing/DummyProxy/DummyProxy","/Outbound/Primary/Dummy_Testing/DummyProxy/ProxyDummySite/Websites","/Outbound/Primary/Dummy_Testing/DummyProxy/ProxyDummySite/Web_Streaming","/Outbound/Primary/Dummy_Testing/DummyProxy/ProxyDummySite/Phoenix","/Outbound/Primary/Dummy_Testing/DummyProxy/ProxyDummySite/FTP","/Outbound/Primary/Dummy_Testing/DummyProxy/ProxyDummySite/Default","/Outbound/Primary/Dummy_Testing/DummyProxy/ProxyDummySite","/Outbound/Primary/Dummy_Testing/DummyProxy","/Inbound/Secondary/Dummy_Testing/DummyProxy/DummyProxy/Websites","/Inbound/Secondary/Dummy_Testing/DummyProxy/DummyProxy/Web_Streaming","/Inbound/Secondary/Dummy_Testing/DummyProxy/DummyProxy/Phoenix","/Inbound/Secondary/Dummy_Testing/DummyProxy/DummyProxy/FTP","/Inbound/Secondary/Dummy_Testing/DummyProxy/DummyProxy/Default","/Inbound/Secondary/Dummy_Testing/DummyProxy/DummyProxy","/Inbound/Secondary/Dummy_Testing/DummyProxy/DummyProxy/Websites","/Inbound/Secondary/Dummy_Testing/DummyProxy/DummyProxy/Web_Streaming","/Inbound/Secondary/Dummy_Testing/DummyProxy/DummyProxy/Phoenix","/Outbound/SyntheticTransactions","/Inbound/Secondary/Dummy_Testing/DummyProxy/DummyProxy/FTP","/Inbound/Secondary/Dummy_Testing/DummyProxy/DummyProxy/Default","/Inbound/Secondary/Dummy_Testing/DummyProxy/DummyProxy","/Inbound/Secondary/Dummy_Testing/DummyProxy","/Inbound/Primary/Dummy_Testing/DummyProxy/DummyProxy/Websites","/Inbound/Primary/Dummy_Testing/DummyProxy/DummyProxy/Web_Streaming","/Inbound/Primary/Dummy_Testing/DummyProxy/DummyProxy/Phoenix","/Inbound/Primary/Dummy_Testing/DummyProxy/DummyProxy/FTP","/Inbound/Primary/Dummy_Testing/DummyProxy/DummyProxy/Default","/Inbound/Primary/Dummy_Testing/DummyProxy/DummyProxy","/Inbound/Primary/Dummy_Testing/DummyProxy/DummyProxy/Websites","/Inbound/Primary/Dummy_Testing/DummyProxy/DummyProxy/Web_Streaming","/Inbound/Primary/Dummy_Testing/DummyProxy/DummyProxy/Phoenix","/Inbound/Primary/Dummy_Testing/DummyProxy/DummyProxy/FTP","/Inbound/Primary/Dummy_Testing/DummyProxy/DummyProxy/Default","/Inbound/Primary/Dummy_Testing/DummyProxy/DummyProxy","/Inbound/Primary/Dummy_Testing/DummyProxy","/Outbound/Secondary/Dummy_Testing/Proxy/Phoenix","/Outbound/Primary/Dummy_Testing/Proxy/Phoenix","/Inbound/Secondary/Dummy_Testing/Proxy/Phoenix","/Inbound/Primary/Dummy_Testing/Proxy/Phoenix","/Outbound/Secondary/Dummy_Testing/Proxy_SSM/Youtube","/Outbound/Secondary/Dummy_Testing/Proxy_SSM/Vimeo","/Outbound/Secondary/Dummy_Testing/Proxy_SSM/Twitter","/Outbound/Secondary/Dummy_Testing/Proxy_SSM/SocialNetwork","/Outbound/Secondary/Dummy_Testing/Proxy_SSM/Pinterest","/Outbound/DummyClient_Applications/eDiary/SSL","/Outbound/DummyClient_Applications/eDiary/HTTP","/Outbound/DummyClient_Applications/eDiary","/Outbound/Secondary/Dummy_Testing/Proxy_SSM/MySpace","/Outbound/Secondary/Dummy_Testing/Proxy_SSM/MetaCafe","/Outbound/Secondary/Dummy_Testing/Proxy_SSM/Linkedin","/Outbound/Secondary/Dummy_Testing/Proxy_SSM/Flickr","/Outbound/Secondary/Dummy_Testing/Proxy_SSM/Facebook","/Outbound/Secondary/Dummy_Testing/Proxy_SSM/BBC_IPlayer","/Outbound/Secondary/Dummy_Testing/Proxy_SSM","/Outbound/Primary/Dummy_Testing/Proxy_SSM/SocialNetwork","/Outbound/Primary/Dummy_Testing/Proxy_SSM/Linkedin","/Inbound/Secondary/Dummy_Testing/Proxy_SSM/Youtube","/Inbound/Secondary/Dummy_Testing/Proxy_SSM/Vimeo","/Inbound/Secondary/Dummy_Testing/Proxy_SSM/Twitter","/Inbound/Secondary/Dummy_Testing/Proxy_SSM/SocialNetwork","/Inbound/Secondary/Dummy_Testing/Proxy_SSM/Pinterest","/Inbound/Secondary/Dummy_Testing/Proxy_SSM/MySpace","/Inbound/Secondary/Dummy_Testing/Proxy_SSM/MetaCafe","/Inbound/Secondary/Dummy_Testing/Proxy_SSM/Linkedin","/Inbound/Secondary/Dummy_Testing/Proxy_SSM/Flickr","/Inbound/Secondary/Dummy_Testing/Proxy_SSM/Facebook","/Inbound/Secondary/Dummy_Testing/Proxy_SSM/BBC_IPlayer","/Inbound/Secondary/Dummy_Testing/Proxy_SSM","/Inbound/Primary/Dummy_Testing/Proxy_SSM/SocialNetwork","/Inbound/Primary/Dummy_Testing/Proxy_SSM/Linkedin","/Outbound/Primary/Dummy_Testing/Proxy_SSM/Youtube","/Outbound/Primary/Dummy_Testing/Proxy_SSM/Vimeo","/Outbound/DummyClient_Applications","/Outbound/Primary/Dummy_Testing/Proxy_SSM/Twitter","/Outbound/Primary/Dummy_Testing/Proxy_SSM/Pinterest","/Outbound/Primary/Dummy_Testing/Proxy_SSM/MySpace","/Outbound/Primary/Dummy_Testing/Proxy_SSM/MetaCafe","/Outbound/LDAP","/Outbound/Primary/Dummy_Testing/Proxy_SSM/Flickr","/Outbound/HTTP-Tunnel","/Outbound/HTTP","/Outbound/Primary/Dummy_Testing/Proxy_SSM/Facebook","/Outbound/DCOM","/Outbound/Primary/Dummy_Testing/Proxy_SSM/BBC_IPlayer","/Outbound/Primary/Dummy_Testing/Proxy_SSM","/Inbound/Primary/Dummy_Testing/Proxy_SSM/Youtube","/Inbound/Primary/Dummy_Testing/Proxy_SSM/Vimeo","/Inbound/Primary/Dummy_Testing/Proxy_SSM/Twitter","/Inbound/Primary/Dummy_Testing/Proxy_SSM/Pinterest","/Inbound/Primary/Dummy_Testing/Proxy_SSM/MySpace","/Inbound/Primary/Dummy_Testing/Proxy_SSM/MetaCafe","/Inbound/Primary/Dummy_Testing/Proxy_SSM/Flickr","/Outbound/Primary","/Inbound/Primary/Dummy_Testing/Proxy_SSM/Facebook","/Inbound/Primary/Dummy_Testing/Proxy_SSM/BBC_IPlayer","/Inbound/Primary/Dummy_Testing/Proxy_SSM","/Outbound/Secondary/Unisys_Services/ERM_Local","/Outbound/Secondary/Unisys_Services/ERM_Central","/Outbound/Secondary/Unisys_Services","/Outbound/Secondary/Remote_Sites/DummyClient_Applications/MERIS/User_Traffic","/Outbound/Secondary/Remote_Sites/DummyClient_Applications/MERIS/Server_Traffic","/Outbound/Secondary/Remote_Sites/DummyClient_Applications/MERIS","/Outbound/Secondary/Remote_Sites/DummyClient_Applications","/Outbound/Secondary/Remote_Sites/DummyClient-to-DummyClient/Default","/Outbound/Secondary/Remote_Sites/DummyClient-to-DummyClient/Caching_Servers","/Outbound/Secondary/Remote_Sites/DummyClient-to-DummyClient","/Outbound/Secondary/Remote_Sites","/Outbound/Secondary/Logica_Services/XHibit/XHibitBroker","/Outbound/Secondary/Logica_Services/XHibit/Xhibit_Thin","/Outbound/Secondary/Logica_Services/XHibit/XHibit_Thick","/Outbound/Secondary/Logica_Services/XHibit/XHibit_Fax","/Outbound/Secondary/Logica_Services/XHibit/XHibit_Display","/Outbound/Secondary/Logica_Services/XHibit/XHibit_CJSE","/Outbound/Secondary/Logica_Services/XHibit","/Outbound/Secondary/Logica_Services/TRS","/Outbound/Secondary/Logica_Services/SUPS_TEC","/Outbound/Secondary/Logica_Services/SUPS_JUROR","/Outbound/Secondary/Logica_Services/SUPS_Familyman","/Outbound/Secondary/Logica_Services/SUPS_Citrix","/Outbound/Secondary/Logica_Services/SUPS_Caseman","/Outbound/Secondary/Logica_Services/SUPS_CAPS","/Outbound/Secondary/Logica_Services/ProbateMan","/Outbound/Secondary/Logica_Services/Polar","/Outbound/Secondary/Logica_Services/Martha","/Outbound/Secondary/Logica_Services/LIBRA_Print","/Outbound/Secondary/Logica_Services/Libra","/Outbound/Secondary/Logica_Services/GRS","/Outbound/Secondary/Logica_Services/GAPSv2","/Outbound/Secondary/Logica_Services/eDiaryTraining","/Outbound/Secondary/Logica_Services/eDiary","/Outbound/Secondary/Logica_Services/DAR-FT","/Outbound/Secondary/Logica_Services/Chase","/Outbound/Secondary/Logica_Services/CCITConnect","/Outbound/Secondary/Logica_Services/Casrec","/Outbound/Secondary/Logica_Services/Casper","/Outbound/Secondary/Logica_Services/BMS","/Outbound/Secondary/Logica_Services/Aria","/Outbound/Secondary/Logica_Services","/Outbound/Secondary/Default","/Outbound/Secondary/Dummy_Testing/VMware","/Outbound/Secondary/Dummy_Testing/Terminal_Servers","/Outbound/Secondary/Dummy_Testing/SQL_Servers","/Outbound/Secondary/Dummy_Testing/SPS","/Outbound/Secondary/Dummy_Testing/SCCM","/Outbound/Secondary/Dummy_Testing/Proxy/Websites","/Outbound/AO_Services","/Outbound/Secondary/Dummy_Testing/Proxy/Web_Streaming","/Outbound/Secondary/Dummy_Testing/Proxy/FTP","/Outbound/Secondary/Dummy_Testing/Proxy","/Outbound/Secondary/Dummy_Testing/OCS","/Outbound/Secondary/Dummy_Testing/Lumension","/Outbound/Secondary/Dummy_Testing/LSC_Uniprint","/Outbound/Secondary/Dummy_Testing/LSC_FTP_DropBox","/Outbound/Secondary/Dummy_Testing/LSC_CitrixGateway","/Outbound/Secondary/Dummy_Testing/Loccs","/Outbound/Secondary/Dummy_Testing/Identity_Manager","/Outbound/Secondary/Dummy_Testing/Exchange","/Outbound/Secondary/Dummy_Testing/EVault_Servers","/Inbound/Telnet","/Inbound/SSL","/Inbound/SOAP-HTTP","/Inbound/SMTP","/Inbound/SameSide","/Outbound/Secondary/Dummy_Testing/Domain_Controllers","/Inbound/Oracle/Oracle-CASM","/Inbound/Oracle/Default","/Inbound/Oracle","/Outbound/Secondary/Dummy_Testing/Backups","/Inbound/MS-Exchange","/Inbound/MS-ActiveDir","/Outbound/Secondary/Dummy_Testing/AntiVirus","/Outbound/Secondary/Dummy_Testing","/Outbound/Primary/Unisys_Services/ERM_Local","/Outbound/Primary/Unisys_Services/ERM_Central","/Outbound/Primary/Unisys_Services","/Outbound/Primary/Remote_Sites/DummyClient_Applications/MERIS/User_Traffic","/Outbound/Primary/Remote_Sites/DummyClient_Applications/MERIS/Server_Traffic","/Outbound/Primary/Remote_Sites/DummyClient_Applications/MERIS","/Outbound/Primary/Remote_Sites/DummyClient_Applications","/Outbound/Primary/Remote_Sites/DummyClient-to-DummyClient/Default","/Outbound/Primary/Remote_Sites/DummyClient-to-DummyClient/Caching_Servers","/Outbound/Primary/Remote_Sites/DummyClient-to-DummyClient","/Outbound/Primary/Remote_Sites","/Outbound/Primary/Logica_Services/XHibit/XHibitBroker","/Inbound/SyntheticTransactions/X.X.X.X","/Outbound/Primary/Logica_Services/XHibit/Xhibit_Thin","/Outbound/Primary/Logica_Services/XHibit/XHibit_Thick","/Outbound/Primary/Logica_Services/XHibit/XHibit_Fax","/Outbound/Primary/Logica_Services/XHibit/XHibit_Display","/Outbound/Primary/Logica_Services/XHibit/XHibit_CJSE","/Outbound/Primary/Logica_Services/XHibit","/Outbound/Primary/Logica_Services/TRS","/Outbound/Primary/Logica_Services/SUPS_TEC","/Outbound/Primary/Logica_Services/SUPS_JUROR","/Outbound/Primary/Logica_Services/SUPS_Familyman","/Outbound/Primary/Logica_Services/SUPS_Citrix","/Outbound/Primary/Logica_Services/SUPS_Caseman","/Outbound/Primary/Logica_Services/SUPS_CAPS","/Outbound/Primary/Logica_Services/ProbateMan","/Outbound/Primary/Logica_Services/Polar","/Outbound/Primary/Logica_Services/Martha","/Outbound/Primary/Logica_Services/LIBRA_Print","/Outbound/Primary/Logica_Services/Libra","/Outbound/Primary/Logica_Services/GRS","/Outbound/Primary/Logica_Services/GAPSv2","/Outbound/Primary/Logica_Services/eDiaryTraining","/Outbound/Primary/Logica_Services/eDiary","/Outbound/Primary/Logica_Services/DAR-FT","/Outbound/Primary/Logica_Services/Chase","/Outbound/Primary/Logica_Services/CCITConnect","/Outbound/Primary/Logica_Services/Casrec","/Outbound/Primary/Logica_Services/Casper","/Outbound/Primary/Logica_Services/BMS","/Outbound/Primary/Logica_Services/Aria","/Outbound/Primary/Logica_Services","/Outbound/Primary/Default","/Outbound/Primary/Dummy_Testing/VMware","/Outbound/Primary/Dummy_Testing/Terminal_Servers","/Outbound/Primary/Dummy_Testing/SQL_Servers","/Outbound/Primary/Dummy_Testing/SPS","/Outbound/Primary/Dummy_Testing/SCCM","/Outbound/Primary/Dummy_Testing/Proxy/Websites","/Outbound/Primary/Dummy_Testing/Proxy/Web_Streaming","/Inbound/DummyClient_Applications/SPC/HTTP","/Inbound/DummyClient_Applications/SPC","/Outbound/Primary/Dummy_Testing/Proxy/FTP","/Outbound/Primary/Dummy_Testing/Proxy","/Outbound/Primary/Dummy_Testing/OCS","/Outbound/Primary/Dummy_Testing/Lumension","/Outbound/Primary/Dummy_Testing/LSC_Uniprint","/Outbound/Primary/Dummy_Testing/LSC_FTP_DropBox","/Outbound/Primary/Dummy_Testing/LSC_CitrixGateway","/Outbound/Primary/Dummy_Testing/Loccs","/Outbound/Primary/Dummy_Testing/Identity_Manager","/Outbound/Primary/Dummy_Testing/Exchange","/Outbound/Primary/Dummy_Testing/EVault_Servers","/Outbound/Primary/Dummy_Testing/Domain_Controllers","/Outbound/Primary/Dummy_Testing/Backups","/Outbound/Primary/Dummy_Testing/AntiVirus","/Outbound/Primary/Dummy_Testing","/Outbound/Link_Local","/Inbound/VOIP","/Inbound/Secondary/Unisys_Services/ERM_Local","/Inbound/Secondary/Unisys_Services/ERM_Central","/Inbound/Secondary/Unisys_Services","/Inbound/Secondary/Remote_Sites/DummyClient_Applications/MERIS/User_Traffic","/Inbound/Secondary/Remote_Sites/DummyClient_Applications/MERIS/Server_Traffic","/Inbound/Secondary/Remote_Sites/DummyClient_Applications/MERIS","/Inbound/Secondary/Remote_Sites/DummyClient_Applications","/Inbound/Secondary/Remote_Sites/DummyClient-to-DummyClient/Default","/Inbound/Secondary/Remote_Sites/DummyClient-to-DummyClient/Caching_Servers","/Inbound/Secondary/Remote_Sites/DummyClient-to-DummyClient","/Inbound/Secondary/Remote_Sites","/Inbound/Secondary/Logica_Services/XHibit/XHibitBroker","/Inbound/Secondary/Logica_Services/XHibit/Xhibit_Thin","/Inbound/Secondary/Logica_Services/XHibit/XHibit_Thick","/Inbound/Secondary/Logica_Services/XHibit/XHibit_Fax","/Inbound/Secondary/Logica_Services/XHibit/XHibit_Display","/Inbound/Secondary/Logica_Services/XHibit/XHibit_CJSE","/Inbound/Secondary/Logica_Services/XHibit","/Inbound/Secondary/Logica_Services/TRS","/Inbound/Secondary/Logica_Services/SUPS_TEC","/Inbound/Secondary/Logica_Services/SUPS_JUROR","/Inbound/Secondary/Logica_Services/SUPS_Familyman","/Inbound/Secondary/Logica_Services/SUPS_Citrix","/Inbound/Secondary/Logica_Services/SUPS_Caseman","/Inbound/Secondary/Logica_Services/SUPS_CAPS","/Inbound/Secondary/Logica_Services/ProbateMan","/Inbound/Secondary/Logica_Services/Polar","/Inbound/Secondary/Logica_Services/Martha","/Inbound/Secondary/Logica_Services/LIBRA_Print","/Inbound/Secondary/Logica_Services/Libra","/Inbound/Secondary/Logica_Services/GRS","/Inbound/Secondary/Logica_Services/GAPSv2","/Inbound/Secondary/Logica_Services/eDiaryTraining","/Inbound/Secondary/Logica_Services/eDiary","/Inbound/Secondary/Logica_Services/DAR-FT","/Inbound/Secondary/Logica_Services/Chase","/Inbound/Secondary/Logica_Services/CCITConnect","/Inbound/Secondary/Logica_Services/Casrec","/Inbound/Secondary/Logica_Services/Casper","/Inbound/Secondary/Logica_Services/BMS","/Inbound/Secondary/Logica_Services/Aria","/Inbound/Secondary/Logica_Services","/Inbound/Secondary/Default","/Inbound/Secondary/Dummy_Testing/VMware","/Inbound/Secondary/Dummy_Testing/Terminal_Servers","/Inbound/Secondary/Dummy_Testing/SQL_Servers","/Inbound/DummyClient_Applications/eDiary/SSL","/Inbound/DummyClient_Applications/eDiary/HTTP","/Inbound/DummyClient_Applications/eDiary","/Inbound/Secondary/Dummy_Testing/SPS","/Inbound/Secondary/Dummy_Testing/SCCM","/Inbound/Secondary/Dummy_Testing/Proxy/Websites","/Inbound/Secondary/Dummy_Testing/Proxy/Web_Streaming","/Inbound/Secondary/Dummy_Testing/Proxy/FTP","/Inbound/Secondary/Dummy_Testing/Proxy","/Inbound/Secondary/Dummy_Testing/OCS","/Inbound/Secondary/Dummy_Testing/Lumension","/Inbound/Secondary/Dummy_Testing/LSC_Uniprint","/Inbound/Secondary/Dummy_Testing/LSC_FTP_DropBox","/Inbound/Secondary/Dummy_Testing/LSC_CitrixGateway","/Inbound/Secondary/Dummy_Testing/Loccs","/Inbound/Secondary/Dummy_Testing/Identity_Manager","/Inbound/Secondary/Dummy_Testing/Exchange","/Inbound/Secondary/Dummy_Testing/EVault_Servers","/Inbound/Secondary/Dummy_Testing/Domain_Controllers","/Inbound/Secondary/Dummy_Testing/Backups","/Inbound/Secondary/Dummy_Testing/AntiVirus","/Inbound/Secondary/Dummy_Testing","/Inbound/Secondary","/Inbound/Primary/Unisys_Services/ERM_Local","/Inbound/Primary/Unisys_Services/ERM_Central","/Inbound/Primary/Unisys_Services","/Inbound/Primary/Remote_Sites/DummyClient_Applications/MERIS/User_Traffic","/Inbound/Primary/Remote_Sites/DummyClient_Applications/MERIS/Server_Traffic","/Inbound/LDAP","/Inbound/Primary/Remote_Sites/DummyClient_Applications/MERIS","/Inbound/HTTP-Tunnel","/Inbound/HTTP","/Inbound/DCOM","/Inbound/Primary/Remote_Sites/DummyClient_Applications","/Inbound/Primary/Remote_Sites/DummyClient-to-DummyClient/Default","/Inbound/Primary/Remote_Sites/DummyClient-to-DummyClient/Caching_Servers","/Inbound/Primary/Remote_Sites/DummyClient-to-DummyClient","/Inbound/Primary/Remote_Sites","/Inbound/Primary/Logica_Services/XHibit/XHibitBroker","/Inbound/Primary/Logica_Services/XHibit/Xhibit_Thin","/Inbound/Primary/Logica_Services/XHibit/XHibit_Thick","/Inbound/Primary/Logica_Services/XHibit/XHibit_Fax","/Inbound/Primary/Logica_Services/XHibit/XHibit_Display","/Inbound/Primary/Logica_Services/XHibit/XHibit_CJSE","/Inbound/Primary/Logica_Services/XHibit","/Inbound/Primary/Logica_Services/TRS","/Inbound/Primary/Logica_Services/SUPS_TEC","/Inbound/Primary/Logica_Services/SUPS_JUROR","/Inbound/Primary/Logica_Services/SUPS_Familyman","/Inbound/CIFS","/Inbound/Primary/Logica_Services/SUPS_Citrix","/Inbound/Primary/Logica_Services/SUPS_Caseman","/Inbound/Primary/Logica_Services/SUPS_CAPS","/Inbound/Primary/Logica_Services/ProbateMan","/Inbound/Primary/Logica_Services/Polar","/Inbound/SyntheticTransactions","/Inbound/Primary/Logica_Services/Martha","/Inbound/Primary/Logica_Services/LIBRA_Print","/Inbound/Primary/Logica_Services/Libra","/Inbound/Primary/Logica_Services/GRS","/Inbound/Primary/Logica_Services/GAPSv2","/Inbound/Primary/Logica_Services/eDiaryTraining","/Inbound/Primary/Logica_Services/eDiary","/Inbound/Primary/Logica_Services/DAR-FT","/Inbound/Primary/Logica_Services/Chase","/Inbound/Primary/Logica_Services/CCITConnect","/Inbound/Primary/Logica_Services/Casrec","/Inbound/Primary/Logica_Services/Casper","/Inbound/Primary/Logica_Services/BMS","/Inbound/Primary/Logica_Services/Aria","/Inbound/Primary/Logica_Services","/Inbound/Primary/Default","/Inbound/Primary/Dummy_Testing/VMware","/Inbound/Primary/Dummy_Testing/Terminal_Servers","/Inbound/Primary/Dummy_Testing/SQL_Servers","/Inbound/Primary/Dummy_Testing/SPS","/Inbound/Primary/Dummy_Testing/SCCM","/Inbound/Primary/Dummy_Testing/Proxy/Websites","/Inbound/Primary/Dummy_Testing/Proxy/Web_Streaming","/Inbound/Primary/Dummy_Testing/Proxy/FTP","/Inbound/Primary/Dummy_Testing/Proxy","/Inbound/Primary/Dummy_Testing/OCS","/Inbound/Primary/Dummy_Testing/Lumension","/Inbound/Primary/Dummy_Testing/LSC_Uniprint","/Inbound/Primary/Dummy_Testing/LSC_FTP_DropBox","/Inbound/Primary/Dummy_Testing/LSC_CitrixGateway","/Inbound/Primary/Dummy_Testing/Loccs","/Inbound/Primary/Dummy_Testing/Identity_Manager","/Inbound/Primary/Dummy_Testing/Exchange","/Inbound/Primary/Dummy_Testing/EVault_Servers","/Outbound/Citrix/Default","/Outbound/Citrix","/Inbound/Primary/Dummy_Testing/Domain_Controllers","/Inbound/Primary/Dummy_Testing/Backups","/Inbound/Primary/Dummy_Testing/AntiVirus","/Inbound/Primary/Dummy_Testing","/Inbound/Primary","/Inbound/Link_Local","/Inbound/DummyClient_Applications","/Inbound/FTP","/Inbound/DiscoveredPorts/TCP_Port_4000","/Inbound/DiscoveredPorts","/Inbound/Citrix/Default","/Inbound/Citrix","/Inbound/CIFS/Default","/Outbound/Localhost","/Inbound/Localhost","/Outbound/Default","/Outbound","/Inbound/Default","/Inbound"
"bytes",0,24141260,1076630179,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6328136,0,65387,65387,157368098,9312,0,9312,0,3104,3296,3104,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,146043310,0,0,0,78840,78840,382228006,0,0,0,0,12237322,2359860,14597182,14597182,0,0,0,0,8877854,3353114,12230968,12230968,0,0,0,336676410,258895955,595572365,0,0,0,509568428,179313155,688881583,0,4236876,0,31067468,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,32818498,0,0,0,0,32818498,75998115,0,0,0,0,75998115,108816613,0,0,0,0,0,0,0,0,0,24832,0,0,0,0,99580338,0,0,0,0,99580338,213081235,0,0,0,0,213081235,312661573,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,53270,53270,0,0,0,0,0,0,0,2132941346,0,379207,379207,0,0,0,0,0,0,0,31763,0,31763,31763,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6296373,0,0,0,0,0,0,19808040,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,243740445,14274296,258014741,258014741,0,3296,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,12512,7276243,0,0,0,0,0,0,0,0,0,0,0,11525631,738442064,4144498,232558,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,242497975,0,1509206,0,101758,514723976,0,143287615,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6752689,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6752689,0,0,0,0,0,0,0,0,0,0,0,103746772,45498368,149245140,149245140,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6592,0,127980,8879260,0,0,0,0,0,0,0,0,0,0,0,40074708,499997542,1843801,185247,0,0,0,0,0,0,0,0,0,0,0,0,0,0,227064446,0,0,0,10321851,0,58377,2035513947,3426022728,0,0,0,0,0,0,0,0,2279450,599594,1941937,2309367051,1386661,3578055879
"avg-bps",0,6718,299617,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1761,0,18,18,43794,3,0,3,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,40643,0,0,0,22,22,106371,0,0,0,0,3406,657,4062,4062,0,0,0,0,2471,933,3404,3404,0,0,0,93694,72049,165743,0,0,0,141809,49901,191710,0,1179,0,8646,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9133,0,0,0,0,9133,21150,0,0,0,0,21150,30283,0,0,0,0,0,0,0,0,0,7,0,0,0,0,27712,0,0,0,0,27712,59299,0,0,0,0,59299,87011,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15,15,0,0,0,0,0,0,0,593580,0,106,106,0,0,0,0,0,0,0,9,0,9,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1752,0,0,0,0,0,0,5512,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,67831,3972,71803,71803,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,2025,0,0,0,0,0,0,0,0,0,0,0,3207,205502,1153,65,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,67485,0,420,0,28,143243,0,39876,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1879,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1879,0,0,0,0,0,0,0,0,0,0,0,28872,12662,41534,41534,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,36,2471,0,0,0,0,0,0,0,0,0,0,0,11152,139145,513,52,0,0,0,0,0,0,0,0,0,0,0,0,0,0,63190,0,0,0,2872,0,16,566467,953434,0,0,0,0,0,0,0,0,634,167,540,642678,386,995744
"""


def get_traffic_classes(output_data):
    traffic_classes = re.search(r'(\"class-var\".+)', output_data, re.MULTILINE | re.IGNORECASE)
    traffic_classes = (traffic_classes.group())
    traffic_classes = traffic_classes.split('","')
    traffic_classes.pop(0)
    return traffic_classes


def get_traffic_volumes(output_data):
    traffic_volumes = re.search(r'(\"bytes\".+)', output_data, re.MULTILINE | re.IGNORECASE)
    traffic_volumes = (traffic_volumes.group())
    traffic_volumes = traffic_volumes.split(',')
    traffic_volumes.pop(0)
    return traffic_volumes


def get_average_utilization(output_data):

    average_utilization = re.search(r'(\"avg-bps\".+)', output_data, re.MULTILINE | re.IGNORECASE)
    average_utilization = (average_utilization.group())
    average_utilization = average_utilization.split(',')
    average_utilization.pop(0)
    return average_utilization


# elastic search :)
# direction => "in" | "out" | all
# order_ by => "name" | "volume" | "utilization"
# order => "asc" | "desc"
# size => number of top entries
def get_traffic_classes_data(a, b, c, direction, order_by, order, size):
    traffic_classes = a
    traffic_volumes = b
    average_utilization = c
    traffic_classes_data = {}
    traffic_classes_data_tmp = {}
    traffic_classes_data_all = []
    traffic_classes_data_inbound = []
    traffic_classes_data_outbound = []

    for index, value in enumerate(traffic_volumes):
        traffic_classes_data_tmp[traffic_classes[index]] = {}
        traffic_classes_data_tmp[traffic_classes[index]] = (traffic_classes[index], int(traffic_volumes[index]),
                                                        int(average_utilization[index]))
    for key, value in traffic_classes_data_tmp.iteritems():
        tmp = value  # or tmp = (key, value)
        traffic_classes_data_all.append(tmp)
        if re.search(r'(/Inbound.*)', str(tmp), re.IGNORECASE) is not None:
            traffic_classes_data_inbound.append(tmp)
        elif re.search(r'(/Outbound.*)', str(tmp), re.IGNORECASE) is not None:
            traffic_classes_data_outbound.append(tmp)

    if direction == "in":
        traffic_classes_data = traffic_classes_data_inbound
    elif direction == "out":
        traffic_classes_data = traffic_classes_data_outbound
    elif direction == "all":
        traffic_classes_data = traffic_classes_data_all

    if order_by == "name":
        order_by_index = int(0)
    elif order_by == "volume":
        order_by_index = int(1)
    elif order_by == "utilization":
        order_by_index = int(2)

    def take_index(elem):
        return elem[order_by_index]

    traffic_classes_data.sort(key=take_index)

    if order == "asc":
        pass
    elif order == "desc":
        traffic_classes_data.reverse()

    # if type(size) = int:
    print (traffic_classes_data[0:size])


def main():
    get_traffic_classes_data(get_traffic_classes(output), get_traffic_volumes(output), get_average_utilization(output),
                             "all", "volume", "desc", 5)


if __name__ == "__main__":
    main()

