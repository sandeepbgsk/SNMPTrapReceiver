from pysnmp.hlapi import *
from pysnmp import debug

# debug.setLogger(debug.Debug('msgproc'))

next(sendNotification(SnmpEngine(),
     CommunityData('public'),
     UdpTransportTarget(('127.0.0.1', 163)),
     ContextData(),
     'trap',
     # sequence of custom OID-value pairs
     [ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0'), OctetString('123455')),
      ObjectType(ObjectIdentity('1.3.6.1.2.1.1.3.0'), Integer32(42))]))
