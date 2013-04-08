CREATE TABLE IF NOT EXISTS `tellabs_mwr_lan_performace_report` (
  `IPAddress` varchar(50) DEFAULT NULL,
  `Date_Time` varchar(50) DEFAULT NULL,
  `CustomerId` varchar(50) DEFAULT NULL,
  `EqType` varchar(50) DEFAULT NULL,
  `Interface` varchar(50) DEFAULT NULL,
  `StatusInfo` varchar(50) DEFAULT NULL,
  `DropEvents` varchar(50) DEFAULT NULL,
  `OctetsRX` varchar(50) DEFAULT NULL,
  `PktsRX` varchar(50) DEFAULT NULL,
  `BroadcastPktsRX` varchar(50) DEFAULT NULL,
  `MulticastPktsRX` varchar(50) DEFAULT NULL,
  `CRCAlignError` varchar(50) DEFAULT NULL,
  `UndersizePkts` varchar(50) DEFAULT NULL,
  `OversizePkts` varchar(50) DEFAULT NULL,
  `Fragments` varchar(50) DEFAULT NULL,
  `Jabber` varchar(50) DEFAULT NULL,
  `Collisions` varchar(50) DEFAULT NULL,
  `UtilizationRX` varchar(50) DEFAULT NULL,
  `OctetsTX` varchar(50) DEFAULT NULL,
  `PktsTX` varchar(50) DEFAULT NULL,
  `BroadcastPktsTX` varchar(50) DEFAULT NULL,
  `MulticastPktsTX` varchar(50) DEFAULT NULL,
  `UtilizationTX` varchar(50) DEFAULT NULL,
  `MinBandwidth` varchar(50) DEFAULT NULL,
  `MaxBandwidth` varchar(50) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;


SELECT *, max(OctetsRX), max(OctetsTX) FROM `tellabs_mwr_lan_performace_report` where `Date_Time` like "010113:00%" and Interface like "LAN-1" and IPAddress like "10.15.243.10";



SELECT * from tellabs_mwr_lan_performace_report 
where 
Data_Time like "010113:0000" and 
IPAddress like "10.15.243.10";


SELECT * from tellabs_mwr_lan_performace_report
where 
`Date_Time` like "010113:00%" ;

SELECT * from tellabs_mwr_lan_performace_report
group by (IPAddress, Date_Time, Interface);

SELECT * from tellabs_mwr_lan_performace_report group by DateTime;


select max(OctetsRX), dathour from (
select OctetsRX, Date_Time, substring(Date_Time, 1, 9) as dathour from tellabs_mwr_lan_performace_report) group by dathour;

select * from 
tellabs_mwr_lan_performace_report 
    where 
        substring(Date_Time, 1, 9) 
    like 
        (select substring(Date_Time,1,9) from 
            tellabs_mwr_lan_performace_report) 
group by Date_Time;


    select max(temp.OctetsRX),max(temp.OctetsTX),substring(temp.dathour,1,6) as hour_to_day from 
    (
        select OctetsRX, OctetsTX, Date_Time, substring(Date_Time, 1, 9) as dathour 
            from tellabs_mwr_lan_performace_report
    ) as temp
    group by temp.dathour


select max(hour_table.OctetsRX), max(hour_table.OctetsTX), hour_table.hour_to_day from (

select max(temp.OctetsRX),max(temp.OctetsTX),substring(temp.dathour,1,6) as hour_to_day from 
    (
        select OctetsRX, OctetsTX, Date_Time, substring(Date_Time, 1, 9) as dathour 
            from tellabs_mwr_lan_performace_report
    ) as temp
    group by temp.dathour
)
as hour_table group by hour_table.hour_to_day;





select max(hour_table.ORX), max(hour_table.OTX), hour_table.hour_to_day  from 
(
    select max(temp.OctetsRX) as ORX ,max(temp.OctetsTX) as OTX, substring(temp.dathour,1,6) as hour_to_day from 
    (
        select OctetsRX, OctetsTX, Date_Time, substring(Date_Time, 1, 9) as dathour, Interface, IPAddress
            from tellabs_mwr_lan_performace_report
    ) as temp
    group by temp.dathour, Interface, IPAddress

) as hour_table 
group by hour_table.hour_to_day;


