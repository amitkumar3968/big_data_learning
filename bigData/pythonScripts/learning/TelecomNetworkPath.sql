CREATE TABLE IF NOT EXISTS `IPForwardingTableVRF` (
  `IP_Address` varchar(50) DEFAULT NULL,
  `Cluster_ID` varchar(50) DEFAULT NULL,
  `VLAN_ID` varchar(50) DEFAULT NULL,
  `RBS_Name` varchar(50) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;


CREATE TABLE IF NOT EXISTS `IPForwardingTable` (
  `RBS_KEY` varchar(50) DEFAULT NULL,
  `RBS_NODE_INTERFACE_KEY` varchar(50) DEFAULT NULL,
  `VLAN_ID_KEY` varchar(50) DEFAULT NULL,
  `RBS_MW_CLUSTER_KEY` varchar(50) DEFAULT NULL,
  `RBS_ACCESS_NODE_KEY` varchar(50) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;


CREATE TABLE IF NOT EXISTS `MWRConfig` (
  `NEID` varchar(50) DEFAULT NULL,
  `Station_ID` varchar(50) DEFAULT NULL,
  `Cluster_VLAN_Table` varchar(50) DEFAULT NULL,
  `VLAN_Label` varchar(50) DEFAULT NULL,
  `LAN1` varchar(50) DEFAULT NULL,
  `LAN2` varchar(50) DEFAULT NULL,
  `LAN3` varchar(50) DEFAULT NULL,
  `LAN4` varchar(50) DEFAULT NULL,
  `Radio_1A` varchar(50) DEFAULT NULL,
  `SNMP_Address` varchar(50) DEFAULT NULL,
  `MAC_ETH_IP` varchar(50) DEFAULT NULL,
  `Subnet` varchar(50) DEFAULT NULL,
  `NET_Address` varchar(50) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

load data local infile '/home/ahmed/test_dir/IPForwardingTableVRF.csv' into table IPForwardingTableVRF fields terminated by ','
enclosed by '"' lines terminated by '\n' ignore 1 lines;

load data local infile '/home/ahmed/test_dir/IPForwardingTableKey.csv' into table IPForwardingTable fields terminated by ','
enclosed by '"' lines terminated by '\n' ignore 1 lines;

load data local infile '/home/ahmed/test_dir/MWRConfig.csv' into table MWRConfig fields terminated by ','
enclosed by '"' lines terminated by '\n' ignore 1 lines;



select * from IPForwardingTableVRF;
select * from IPForwardingTable;
select * from MWRConfig;

select * from MWRConfig join MWRConfig.VLAN_Label =  


SELECT * from 
(
SELECT MWRConfig.*, IPForwardingTableVRF.* FROM MWRConfig JOIN IPForwardingTableVRF ON MWRConfig.VLAN_Label = IPForwardingTableVRF.VLAN_ID where IPForwardingTableVRF.VLAN_ID = 70 
and MWRConfig.Cluster = IPForwardingTableVRF.Cluster_ID
)  as interTable
where interTable.IP_Address like "10.157.244.196"
;


select substring(RBS_KEY, 1, 5), IPForwardingTable.* as RBS_Name from IPForwardingTable;

select * from
(
    select * from 
    (
        select MWRConfig.*, IPForwardingTable.* from MWRConfig left JOIN IPForwardingTable on IPForwardingTable.RBS_MW_CLUSTER_KEY = MWRConfig.Cluster  
            and substring(MWRConfig.NEID,1 ,5) as neid = substring(RBS_KEY, 1, 5) as rbskey

    ) as interTable
     JOIN IPForwardingTable on IPForwardingTable.VLAN_ID_KEY = interTable.VLAN_Table group by SNMP_Address

) as interTable2 where interTable2.Radio_1A like "Unchanged"

select substring(IPForwardingTable.RBS_KEY, 1, 5), MWRConfig.*, IPForwardingTable.* from MWRConfig  JOIN 
    IPForwardingTable on substring(MWRConfig.NEID,1,5) = substring(RBS_KEY, 1, 5) group by MWRConfig.NEID, MWRConfig.Cluster, MWRConfig.SNMP_Address ;




select substring(RBS_KEY, 1, 5) as rbskey from IPForwardingTable group by rbskey;



-- -----------------------------------------
-- -----------------------------------------
-- -----------------------------------------





select SecondLevelTransform.* from
(
    select FirstLevelTransform.* from 
    (
        select MWRConfig.*, IPForwardingTable.* from MWRConfig left JOIN IPForwardingTable on IPForwardingTable.RBS_MW_CLUSTER_KEY = MWRConfig.Cluster  
            and substring(MWRConfig.NEID,1 ,5) = substring(IPForwardingTable.RBS_KEY, 1, 5)

    ) as FirstLevelTransform
     JOIN IPForwardingTable on IPForwardingTable.VLAN_ID_KEY = FirstLevelTransform.VLAN_Table group by SNMP_Address order by INET_ATON(SNMP_Address)

) as SecondLevelTransform where SecondLevelTransform.Radio_1A like "Unchanged"



select FirstLevelTransform.* from 
(
    select MWRConfig.*, IPForwardingTable.* from MWRConfig left JOIN IPForwardingTable on IPForwardingTable.RBS_MW_CLUSTER_KEY = MWRConfig.Cluster  
        and substring(MWRConfig.NEID,1 ,5) = substring(IPForwardingTable.RBS_KEY, 1, 5)

) as FirstLevelTransform
 JOIN IPForwardingTable on IPForwardingTable.VLAN_ID_KEY = FirstLevelTransform.VLAN_Table group by SNMP_Address order by INET_ATON(SNMP_Address)









































