create table client (client_id integer not null primary key auto_increment,
                     name varchar(64));
create table portfolio (portfolio_id integer not null primary key auto_increment,
                        client_id integer references client.id,
                        cash decimal(10,2),
                        stocks decimal(10,2));
insert into client (name) values ('John Doe'), ('Jane Doe');
insert into portfolio (client_id, cash, stocks) values (1, 11.11, 22.22),
                                                       (1, 10.11, 23.22),
                                                       (2, 30.30, 40.40),
                                                       (2, 40.40, 50.50);



select * from client;
select * from portfolio;

select name, max(cash + stocks) from client join portfolio using (client_id) group by client_id;


SELECT IPAddress, Date_Time, Interface, OctetsRX, OctetsTX from tellabs_mwr;




SELECT IPAddress, substring(Date_Time,1,9) as date_hour, Interface, OctetsRX, OctetsTX from tellabs_mwr;


select max(hour_table.ORX), max(hour_table.OTX), hour_table.hour_to_day, Interface, IPAddress   from 
(

select max(temp.OctetsRX) as ORX ,max(temp.OctetsTX) as OTX, substring(temp.dathour,1,9) as hour_to_day, temp.Interface, temp.IPAddress from 
(
    select OctetsRX, OctetsTX, Date_Time, substring(Date_Time, 1, 9) as dathour, Interface, IPAddress
        from tellabs_mwr
) as temp
group by temp.dathour, Interface, IPAddress


) as hour_table 
group by hour_table.hour_to_day, Interface, IPAddress;




-- Hourly Report Query 

select max(temp.OctetsRX) as ORX ,max(temp.OctetsTX) as OTX, substring(temp.dathour,1,9) as hour_to_day, temp.Interface, temp.IPAddress from 
(
    select OctetsRX, OctetsTX, Date_Time, substring(Date_Time, 1, 9) as dathour, Interface, IPAddress
        from tellabs_mwr_lan_performace_report
) as temp
group by temp.dathour, Interface, IPAddress;


-- Temp 

select max(temp.OctetsRX) as ORX ,max(temp.OctetsTX) as OTX, substring(temp.dathour,1,9) as hour_to_day, temp.Interface, temp.IPAddress from 
(
    select OctetsRX, OctetsTX, Date_Time, substring(Date_Time, 1, 9) as dathour, Interface, IPAddress
        from tellabs_mwr
) as temp
group by temp.dathour, Interface, IPAddress;



-- Daily Report Query
select max(ORX), max(OTX), daily_data.hour_to_day, daily_data.Interface, daily_data.IPAddress from
(
    select max(hourly_data.OctetsRX) as ORX ,max(hourly_data.OctetsTX) as OTX, substring(hourly_data.dathour,1,6) as hour_to_day, hourly_data.Interface, hourly_data.IPAddress from 
    (
        select OctetsRX, OctetsTX, Date_Time, substring(Date_Time, 1, 9) as dathour, Interface, IPAddress
            from tellabs_mwr_lan_performace_report
    ) as hourly_data
    group by hourly_data.dathour, hourly_data.Interface, hourly_data.IPAddress

) as daily_data
group by daily_data.hour_to_day, daily_data.Interface, daily_data.IPAddress






select max(ORX), max(OTX), daily_data.hour_to_day, daily_data.Interface, daily_data.IPAddress from
(
    select 
        max(hourly_data.OctetsRX) as ORX, 
        max(hourly_data.OctetsTX) as OTX, 
        substring(hourly_data.dathour,1,6) as hour_to_day, 
        hourly_data.Interface, 
        hourly_data.IPAddress, 
        avg(hourly_data.DropEvents) as avg_drop, 
        avg(hourly_data.CRCAlignError) as avg_crc_align,
        avg(hourly_data.Jabber) as avg_jabber, 
        avg(hourly_data.Collisions) as avg_collisions 
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
        from tellabs_mwr_lan_performace_report
    ) as hourly_data
    group by hourly_data.dathour, hourly_data.Interface, hourly_data.IPAddress

) as daily_data
group by daily_data.hour_to_day, daily_data.Interface, daily_data.IPAddress




select 
    max(daily_data.ORX) as ORX, 
    max(daily_data.OTX) as OTX, 
    substring(daily_data.hour_to_day,1,6) as daily, 
    daily_data.Interface, 
    daily_data.IPAddress, 
    avg(daily_data.avg_drop) as avg_drop, 
    avg(daily_data.avg_crc_align) as avg_crc_align,
    avg(daily_data.avg_jabber) as avg_jabber, 
    avg(daily_data.avg_collisions) as avg_collisions
from
(
    select 
        max(hourly_data.OctetsRX) as ORX, 
        max(hourly_data.OctetsTX) as OTX, 
        substring(hourly_data.dathour,1,6) as hour_to_day, 
        hourly_data.Interface, 
        hourly_data.IPAddress, 
        avg(hourly_data.DropEvents) as avg_drop, 
        avg(hourly_data.CRCAlignError) as avg_crc_align,
        avg(hourly_data.Jabber) as avg_jabber, 
        avg(hourly_data.Collisions) as avg_collisions 
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
        from tellabs_mwr_lan_performace_report
    ) as hourly_data
    group by hourly_data.dathour, hourly_data.Interface, hourly_data.IPAddress

) as daily_data
group by daily_data.hour_to_day, daily_data.Interface, daily_data.IPAddress





-- Complete Hourly Report

select 
    max(hourly_data.OctetsRX) as ORX, 
    max(hourly_data.OctetsTX) as OTX, 
    substring(hourly_data.dathour,1,9) as hour_to_day, 
    hourly_data.Interface, 
    hourly_data.IPAddress, 
    avg(hourly_data.DropEvents) as avg_drop, 
    avg(hourly_data.CRCAlignError) as avg_crc_align,
    avg(hourly_data.Jabber) as avg_jabber, 
    avg(hourly_data.Collisions) as avg_collisions 
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


-- Complete Daily Report

select * from 
(
select 
max(daily_data.ORX) as ORX, 
        max(daily_data.OTX) as OTX, 
        substring(daily_data.hour_to_day,1,6) as daily, 
        daily_data.Interface, 
        daily_data.IPAddress, 
        floor(avg(daily_data.avg_drop)) as avg_drop, 
        floor(avg(daily_data.avg_crc_align)) as avg_crc_align,
        floor(avg(daily_data.avg_jabber)) as avg_jabber, 
        floor(avg(daily_data.avg_collisions)) as avg_collisions
from
(
    select 
        max(hourly_data.OctetsRX) as ORX, 
        max(hourly_data.OctetsTX) as OTX, 
        substring(hourly_data.dathour,1,6) as hour_to_day, 
        hourly_data.Interface, 
        hourly_data.IPAddress, 
        avg(hourly_data.DropEvents) as avg_drop, 
        avg(hourly_data.CRCAlignError) as avg_crc_align,
        avg(hourly_data.Jabber) as avg_jabber, 
        avg(hourly_data.Collisions) as avg_collisions 
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

) as daily_data
group by daily_data.hour_to_day, daily_data.Interface, daily_data.IPAddress
) as query 











