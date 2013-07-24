#  All information about the Table Name, Column Family and Column Qualifiers 
#  will be in CAPs Letters 
# 

# ************************************************** # 
#    Creating Table for Date Based lookup Table      #
# ************************************************** # 

create "DATE_TABLE","DATE_BASED_LOOKUP"

# All Column Qualifier in the above table will be prefixed with "ALL_"
# Any data which needs to be looked-up based on a DATE will go in this table.

# ROW KEY : <DATE>

# Column Qualifier for this table

# ALL_AREAS
# ALL_NODES
# ALL_RBS
# ALL_RNC
# ALL_TRUNKS
# ALL_*


# ************************************************** # 
#    Creating Table for Area Based lookup Table      #
# ************************************************** #  
 

create "AREA_TABLE", "AREA_BASED_LOOKUP"

# All Column Qualifier in the above table will be prefixed with "AREA_"
# Any data which needs to be looked-up based on a AREA will go in this table. 

# ROW KEY : <DATE:AREA>

# Column Qualifier for this table

# AREA_NODES_DETAILS
# AREA_TRUNK_DETAILS
# AREA_RBS_DETAILS
# AREA_RNC_DETAILS
# AREA_LSP_DETAILS
# AREA_*


# ************************************************** # 
#    Creating Table for Node Information             #
# ************************************************** #  


create "NODE_TABLE","NODE_INFORMATION"

# All Data related to node is stored in this table. Prefix with "NODE_"
# Any Data which needs node information should query this table. 

# ROW KEY : <DATE:NODE>

# Column Qualifier for this table

# NODE_HW_INFO
# NODE_SW_INFO
# NODE_INTERFACES
# NODE_TRUNKS_PER_INTERFACE
# NODE_ALL_TRUNKS
# NODE_INGRESS_LSP  
# NODE_EGRESS_LSP
# NODE_TRANSIT_LSP
# NODE_ALL_LSP
# NODE_ALL_PWE
# NODE_VRF_TABLE_INFO
# NODE_CPU_UTILIZATION
# NODE_VLAN_PER_INTERFACE
# NODE_*



# ************************************************** # 
#    Creating Table for RBS RNC Information          #
# ************************************************** #  

create "RBS_RNC_TABLE","RBS_RNC_DETAILS"

# All Data related to RBS RNC path is stored in this table. Prefix with "RBS_RNC_"
# Any Data which needs node information should query this table. 

# ROW KEY : <DATE:RBS_ID:RNC_ID>

# Column Qualifier for this table

# RBS_RNC_LOCATION_DETAILS
# RBS_RNC_ALL_DETAILS
# RBS_RNC_FORWARD_PATH
# RBS_RNC_REVERSE_PATH



# ************************************************** # 
#    Creating Table for Node Information             #
# ************************************************** #  

# All Data related to node is stored in this table. Prefix with "NODE_"
# Any Data which needs node information should query this table. 

# ROW KEY : <DATE:NODE>

# Column Qualifier for this table


# ************************************************** # 
#    Creating Table for Node Information             #
# ************************************************** #  

# All Data related to node is stored in this table. Prefix with "NODE_"
# Any Data which needs node information should query this table. 

# ROW KEY : <DATE:NODE>

# Column Qualifier for this table



# ************************************************** # 
#    Creating Table for Node Information             #
# ************************************************** #  

# All Data related to node is stored in this table. Prefix with "NODE_"
# Any Data which needs node information should query this table. 

# ROW KEY : <DATE:NODE>

# Column Qualifier for this table


# ************************************************** # 
#    Creating Table for Node Information             #
# ************************************************** #  

# All Data related to node is stored in this table. Prefix with "NODE_"
# Any Data which needs node information should query this table. 

# ROW KEY : <DATE:NODE>

# Column Qualifier for this table















