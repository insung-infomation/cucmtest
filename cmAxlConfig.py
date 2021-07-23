'''
Created on 2018. 06. 07.
@author: Administrator
'''

# -*- coding: utf-8 -*-
#!/usr/bin/env python


CM_IP = ''
CM_ID = ''
CM_PW = ''
VER_LIST = [ '10.5', '11.5', '12.5' ]
MENU_LIST = [ 
    'Unified CM',
    'Unified CM Group',
    'Call Pickup Group',
    'Directory Number',
    'Phone NTP Reference',
    'Date/Time Group',
    'Device',
    'EndUser',
    'Device Pool',
    'PhoneTemplate',
    'SoftkeyTemplate',
    'CallingSearchSpace',
    'RoutePartition',
    'Location',
    'Application Server',
    'Application Dial Rules'
]
QUERY_DIC = {
    'Unified CM' : 'SELECT pkid, name, description FROM callmanager',
    'Unified CM Group' : 'SELECT pkid, name, tftpdefault FROM callmanagergroup',    
    'Call Pickup Group' : '''
                        select pg.pkid, pg.name, nl.dnorpattern, nl.description from pickupgroup pg, numplan nl
                        where pg.fknumplan_pickup=nl.pkid
                        ''',
    'Directory Number' : '''
                        select n.pkid, n.dnorpattern, n.description
                            from numplan n left outer join devicenumplanmap m on m.fkdevice = n.pkid 
                            where m.fkdevice is null 
                            and n.tkpatternusage = 2
                            order by dnorpattern
                        ''' ,          
    'Phone NTP Reference' : 'SELECT pkid, name, description FROM ntpserver',
    'Date/Time Group' : 'SELECT pkid, name, datetemplate, tktimezone, tkreset, resettoggle FROM datetimesetting',
    'Device' : 'SELECT pkid, name, isactive, description FROM device',
    'EndUser' : 'SELECT pkid, userid, lastname, firstname, mobile, status FROM enduser',
    'Device Pool' : '''
                    SELECT T.pkid, T.name, CG.name group_name, RG.name region_name, DT.name dt_group_name  
                    FROM devicepool T, callmanagergroup CG, region RG, datetimesetting DT 
                    WHERE T.fkcallmanagergroup=CG.pkid
                    AND T.fkregion=RG.pkid
                    AND T.fkdatetimesetting=DT.pkid
                    ''',   
    'PhoneTemplate' : 'SELECT pkid, name, tkmodel FROM phonetemplate',
    'SoftkeyTemplate' : 'SELECT pkid, name, description FROM softkeytemplate',
    'CallingSearchSpace' : 'SELECT pkid, name, description FROM callingsearchspace',
    'RoutePartition' : 'SELECT pkid, name, description FROM routepartition',  
    'Location' : 'SELECT pkid, name, id FROM location',
    'Application Server' : 'SELECT pkid, name, ipaddr FROM appserver',
    'Application Dial Rules' : 'SELECT * FROM applicationdialrule'
}
HEADER_DIC = {
    'Unified CM' : ['pkid', 'Name', 'Description'],
    'Unified CM Group' : ['pkid', 'Name', 'Auto-registration'],   
    'Call Pickup Group' : ['pkid', 'Pickup Group Name', 'Pickup Group Number', 'Description'],    
    'Directory Number' : ['pkid', 'Pattern/Directory Number', 'description'],  
    'Phone NTP Reference' : ['pkid', 'name', 'description'],
    'Date/Time Group' : ['pkid', 'Name', 'Datetemplate', 'tktimezone', 'tkreset', 'resettoggle'],
    'Device' : ['pkid', 'Name', 'isactive', 'description'],
    'EndUser' : ['pkid', 'userid', 'lastname', 'firstname', 'hp', 'status'],
    'Device Pool' : ['pkid', 'Name', 'CM Group', 'Region', 'Date/Time Group'],   
    'PhoneTemplate' : ['pkid', 'Name', 'tkmodel'],
    'SoftkeyTemplate' : ['pkid', 'Name', 'Description'],
    'CallingSearchSpace' : ['pkid', 'Name', 'Description'],
    'RoutePartition' : ['pkid', 'Name', 'Description'],  
    'Location' : ['pkid', 'Name', 'id'],
    'Application Server' : ['pkid', 'Name', 'ipaddr'],
    'Application Dial Rules' : ['pkid','Name','Description','Number Begins With','Number of Digits','Total Digits to be Removed','Prefix With Pattern']
}
BODY_DIC = {
    'Unified CM Group' : ['pkid', 'name', 'tftpdefault'],
    'Unified CM' : ['pkid', 'name', 'description'],
    'Call Pickup Group' : ['pkid', 'name', 'dnorpattern', 'description'],    
    'Directory Number' : ['pkid','dnorpattern', 'description'],
    'Phone NTP Reference' : ['pkid', 'name', 'description'],
    'Date/Time Group' : ['pkid', 'name', 'datetemplate', 'tktimezone', 'tkreset', 'resettoggle'],
    'Device' : ['pkid', 'name', 'isactive', 'description'],
    'EndUser' : ['pkid', 'userid', 'lastname', 'firstname', 'mobile', 'status'],
    'Device Pool' : ['pkid', 'name', 'group_name', 'region_name', 'dt_group_name'],   
    'PhoneTemplate' : ['pkid', 'name', 'tkmodel'],
    'SoftkeyTemplate' : ['pkid', 'name', 'description'],
    'CallingSearchSpace' : ['pkid', 'name', 'description'],
    'RoutePartition' : ['pkid', 'name', 'description'],  
    'Location' : ['pkid', 'name', 'id'],
    'Application Server' : ['pkid', 'name', 'ipaddr'],
    'Application Dial Rules' : ['pkid','name','description','numbeginwith','numofdigits','digitsremoved','prefix']
}
     