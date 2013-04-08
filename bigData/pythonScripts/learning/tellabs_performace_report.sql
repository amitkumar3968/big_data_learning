create table tellabs_mwr_lan_performace_report( IPAddress varchar(50),
Date_Time varchar(50),
CustomerId varchar(50),
EqType varchar(50),
Interface varchar(50),
StatusInfo varchar(50),
DropEvents varchar(50),
OctetsRX varchar(50), 
PktsRX varchar(50),
BroadcastPktsRX varchar(50),
MulticastPktsRX varchar(50),
CRCAlignError varchar(50),
UndersizePkts varchar(50),
OversizePkts varchar(50),
Fragments varchar(50),
Jabber varchar(50),
Collisions varchar(50),
UtilizationRX varchar(50),
OctetsTX varchar(50),
PktsTX varchar(50),
BroadcastPktsTX varchar(50),
MulticastPktsTX varchar(50),
UtilizationTX varchar(50),
MinBandwidth varchar(50),
MaxBandwidth varchar(50)
)


-- Daily Data Test
 
select * from
(
select 
    max(hourly_data.OctetsRX) as ORX, 
    max(hourly_data.OctetsTX) as OTX, 
    substring(hourly_data.dathour,1,9) as hour_to_day, 
    hourly_data.Interface, 
    hourly_data.IPAddress, 
    floor(avg(hourly_data.DropEvents)) as avg_drop, 
    floor(avg(hourly_data.CRCAlignError)) as avg_crc_align,
    floor(avg(hourly_data.Jabber)) as avg_jabber, 
    floor(avg(hourly_data.Collisions)) as avg_collisions 
from 
(
    select 
        OctetsRX, 
        OctetsTX, 
        Date_Time, 
        substring(Date_Time, 1, 9) as dathour, 
        Interface, 
        IPAddress, 
        DropEvents, 
        CRCAlignError, 
        Jabber, 
        Collisions
    from tellabs_heavy
) as hourly_data
group by hourly_data.dathour, hourly_data.Interface, hourly_data.IPAddress
) as query_table

where query_table.IPAddress like "10.15.243.10" and query_table.hour_to_day like "010113:23" and query_table.Interface like "Port-A"
