CREATE TABLE IF NOT EXISTS `tellabs_mwr_radio` (
  `NE_Identifier` varchar(50) DEFAULT NULL,
  `IP_Address` varchar(50) DEFAULT NULL,
  `Date_Time` varchar(50) DEFAULT NULL,
  `NE_Type` varchar(50) DEFAULT NULL,
  `Radio_Branch_Id` varchar(50) DEFAULT NULL,
  `StatusInfo` varchar(50) DEFAULT NULL,
  `UAS` varchar(50) DEFAULT NULL,
  `SES` varchar(50) DEFAULT NULL,
  `ES` varchar(50) DEFAULT NULL,
  `AIS` varchar(50) DEFAULT NULL,
  `RLTS1` varchar(50) DEFAULT NULL,
  `RLTS2` varchar(50) DEFAULT NULL,
  `RLTM_MIN` varchar(50) DEFAULT NULL,
  `RLTM_MAX` varchar(50) DEFAULT NULL,
  `TLTM_MIN` varchar(50) DEFAULT NULL,
  `TLTM_MAX` varchar(50) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

load data local infile '/home/ahmed/test_dir/MWRRadioPerformaceReport10.15.243.10.csv' into table tellabs_mwr_radio fields terminated by ','
enclosed by '"' lines terminated by '\n' ignore 1 lines;

load data local infile '/home/ahmed/test_dir/MWRRadioPerformaceReport10.15.243.12.csv' into table tellabs_mwr_radio fields terminated by ','
enclosed by '"' lines terminated by '\n' ignore 1 lines;

load data local infile '/home/ahmed/test_dir/MWRRadioPerformaceReport10.15.244.10.csv' into table tellabs_mwr_radio fields terminated by ','
enclosed by '"' lines terminated by '\n' ignore 1 lines;

load data local infile '/home/ahmed/test_dir/MWRRadioPerformaceReport10.15.244.12.csv' into table tellabs_mwr_radio fields terminated by ','
enclosed by '"' lines terminated by '\n' ignore 1 lines;


-- Complete Hourly Report

select 
    hourly_data.IP_address,
    substring(hourly_data.datehour,1,9) as hour_to_day,    
    hourly_data.Radio_Branch_Id,
    hourly_data.StatusInfo,
    floor(avg(hourly_data.UAS)) as avg_UAS,
    floor(avg(hourly_data.SES)) as avg_SES,
    floor(avg(hourly_data.ES)) as avg_ES,
    floor(avg(hourly_data.AIS)) as avg_AIS,
    floor(avg(hourly_data.RLTS1)) as avg_RLTS1,
    floor(avg(hourly_data.RLTS2)) as avg_RLTS2,
    floor(avg(hourly_data.RLTM_MIN)) as avg_RLTM_MIN,
    floor(avg(hourly_data.RLTM_MAX)) as avg_RLTM_MAX,
    floor(avg(hourly_data.TLTM_MIN)) as avg_TLTM_MIN,
    floor(avg(hourly_data.TLTM_MAX)) as avg_TLTM_MAX
from 
(
    select 
        IP_Address, 
        Date_Time, 
        Radio_Branch_Id, 
        substring(Date_Time, 1, 9) as datehour, 
        StatusInfo, 
        UAS,
        SES,
        ES,
        AIS,
        RLTS1,
        RLTS2,
        RLTM_MIN,
        RLTM_MAX,
        TLTM_MIN,
        TLTM_MAX
    from tellabs_mwr_radio
) as hourly_data
group by hourly_data.datehour, hourly_data.Radio_Branch_Id, hourly_data.IP_Address

INTO OUTFILE '/tmp/MWRRadioPerformanceHourly.csv' 
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n' ;


-- Complete Daily Report


select 
    daily_data.IP_address,
    substring(daily_data.hour_to_day,1,6) as daily,
    daily_data.Radio_Branch_Id,
    daily_data.StatusInfo,
    floor(avg(daily_data.avg_UAS)) as avg_UAS,
    floor(avg(daily_data.avg_SES)) as avg_SES,
    floor(avg(daily_data.avg_ES)) as avg_ES,
    floor(avg(daily_data.avg_AIS)) as avg_AIS,
    floor(avg(daily_data.avg_RLTS1)) as avg_RLTS1,
    floor(avg(daily_data.avg_RLTS2)) as avg_RLTS2,
    floor(avg(daily_data.avg_RLTM_MIN)) as avg_RLTM_MIN,
    floor(avg(daily_data.avg_RLTM_MAX)) as avg_RLTM_MAX,
    floor(avg(daily_data.avg_TLTM_MIN)) as avg_TLTM_MIN,
    floor(avg(daily_data.avg_TLTM_MAX)) as avg_TLTM_MAX

from
(
    select 
        hourly_data.IP_address,
        hourly_data.Date_Time,
        hourly_data.Radio_Branch_Id,
        substring(hourly_data.datehour,1,6) as hour_to_day,
        hourly_data.StatusInfo,
        floor(avg(hourly_data.UAS)) as avg_UAS,
        floor(avg(hourly_data.SES)) as avg_SES,
        floor(avg(hourly_data.ES)) as avg_ES,
        floor(avg(hourly_data.AIS)) as avg_AIS,
        floor(avg(hourly_data.RLTS1)) as avg_RLTS1,
        floor(avg(hourly_data.RLTS2)) as avg_RLTS2,
        floor(avg(hourly_data.RLTM_MIN)) as avg_RLTM_MIN,
        floor(avg(hourly_data.RLTM_MAX)) as avg_RLTM_MAX,
        floor(avg(hourly_data.TLTM_MIN)) as avg_TLTM_MIN,
        floor(avg(hourly_data.TLTM_MAX)) as avg_TLTM_MAX
    from 
    (
        select 
            IP_Address, 
            Date_Time, 
            Radio_Branch_Id, 
            substring(Date_Time, 1, 9) as datehour, 
            StatusInfo, 
            UAS,
            SES,
            ES,
            AIS,
            RLTS1,
            RLTS2,
            RLTM_MIN,
            RLTM_MAX,
            TLTM_MIN,
            TLTM_MAX
        from tellabs_mwr_radio
    ) as hourly_data
    group by hourly_data.datehour, hourly_data.Radio_Branch_Id, hourly_data.IP_Address

) as daily_data
group by daily_data.hour_to_day, daily_data.Radio_Branch_Id, daily_data.IP_Address


INTO OUTFILE '/tmp/MWRRadioPerformanceDaily.csv' 
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n' ;

