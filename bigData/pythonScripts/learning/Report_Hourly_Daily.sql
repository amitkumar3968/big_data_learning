
-- Complete Hourly Report

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

INTO OUTFILE '/tmp/MWRLanPerformanceHourly.csv' 
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n' ;


-- Complete Daily Report

select 


        daily_data.IPAddress, 
        substring(daily_data.hour_to_day,1,6) as DateTime, 
        daily_data.Interface as InterfaceType, 
        max(daily_data.ORX) as OctetsRx, 
        max(daily_data.OTX) as OctetsTX, 
        avg(daily_data.ORX) as avg_ORX,
        avg(daily_data.OTX) as avg_OTX,
        floor(avg(daily_data.avg_drop)) as avg_drop, 
        floor(avg(daily_data.avg_crc_align)) as avg_crc_align,
        floor(avg(daily_data.avg_jabber)) as avg_jabber, 
        floor(avg(daily_data.avg_collisions)) as avg_collisions
from
(
    select 
        hourly_data.IPAddress, 
        substring(hourly_data.datehour,1,6) as hour_to_day,         
        hourly_data.Interface, 
        max(hourly_data.OctetsRX) as ORX, 
        max(hourly_data.OctetsTX) as OTX, 
        avg(hourly_data.OctetsRX),
        avg(hourly_data.OctetsTX),
        avg(hourly_data.DropEvents) as avg_drop, 
        avg(hourly_data.CRCAlignError) as avg_crc_align,
        avg(hourly_data.Jabber) as avg_jabber, 
        avg(hourly_data.Collisions) as avg_collisions 
    from 
    (
        select 
            IPAddress,            
            Date_Time,
            Interface,
            DropEvents, 
            CRCAlignError, 
            Jabber, 
            Collisions
        from tellabs_heavy
    ) as hourly_data
    group by hourly_data.datehour, hourly_data.Interface, hourly_data.IPAddress

) as daily_data
group by daily_data.hour_to_day, daily_data.Interface, daily_data.IPAddress

INTO OUTFILE '/tmp/MWRLanPerformanceDaily.csv' 
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n' ;

