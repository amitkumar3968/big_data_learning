#  All information about the Table Name, Column Family and Column Qualifiers 
#  will be in CAPs Letters 
# 

# ************************************************** # 
#    Creating Table for Date Based lookup Table      #
# ************************************************** # 

echo "create 'DATE_TABLE','DATE_BASED_LOOKUP'" | hbase shell 

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
 

echo "create 'AREA_TABLE', 'AREA_BASED_LOOKUP'" | hbase shell 

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


echo "create 'NODE_TABLE','NODE_INFORMATION'" | hbase shell 

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
# NODE_PERFORMANCE
# NODE_*



# ************************************************** # 
#    Creating Table for RBS RNC Information          #
# ************************************************** #  

echo "create 'RBS_RNC_TABLE','RBS_RNC_DETAILS'" | hbase shell 

# All Data related to RBS RNC path is stored in this table. Prefix with "RBS_RNC_"
# Any Data which needs node information should query this table. 

# ROW KEY : <DATE:RBS_ID:RNC_ID>

# Column Qualifier for this table

# RBS_RNC_LOCATION_DETAILS
# RBS_RNC_ALL_DETAILS
# RBS_RNC_FORWARD_PATH
# RBS_RNC_REVERSE_PATH
# RBS_RNC_*



# ************************************************** # 
#    Creating Table for PWE Information              #
# ************************************************** #  

echo "create 'PWE_TABLE','PWE_DETAILS'" | hbase shell 

# All Data related to PWE is stored in this table. Prefix with "PWE_"
# Any Data which needs node information should query this table. 

# ROW KEY : <DATE:PWE_ID>

# Column Qualifier for this table

# PWE_LOCATION_DETAILS
# PWE_ALL_DETAILS
# PWE_PATH
# PWE_*


# ************************************************** # 
#    Creating Table for LSP Information              #
# ************************************************** #  

echo "create 'LSP_TABLE','LSP_DETAILS'" | hbase shell 

# All Data related to LSP is stored in this table. Prefix with "LSP_"
# Any Data which needs node information should query this table. 

# ROW KEY : <DATE:LSP_ID>

# Column Qualifier for this table

# LSP_LOCATION_DETAILS
# LSP_ALL_DETAILS
# LSP_PATH
# LSP_PERFORMANCE
# LSP_*


# ************************************************** # 
#    Creating Table for VRF_TABLE Information              #
# ************************************************** #  

echo "create 'VRF_TABLE','VRF_DETAILS'" | hbase shell 

# All Data related to VRF is stored in this table. Prefix with "VRF_"
# Any Data which needs node information should query this table. 

# ROW KEY : <DATE:VRF_ID>

# Column Qualifier for this table

# VRF_LOCATION_DETAILS
# VRF_ALL_DETAILS
# VRF_PERFORMANCE
# VRF_*



# ************************************************** # 
#    Creating Table for RNC_TABLE Information              #
# ************************************************** #  

echo "create 'RNC_TABLE','RNC_DETAILS'" | hbase shell 

# All Data related to RNC is stored in this table. Prefix with "RNC_"
# Any Data which needs node information should query this table. 

# ROW KEY : <DATE:RNC_ID>

# Column Qualifier for this table

# RNC_LOCATION_DETAILS
# RNC_ALL_DETAILS
# RNC_PERFORMANCE
# RNC_*


# ************************************************** # 
#    Creating Table for TUNNEL_TABLE Information              #
# ************************************************** #  

echo "create 'TUNNEL_TABLE','TUNNEL_DETAILS'" | hbase shell 

# All Data related to TUNNEL_ is stored in this table. Prefix with "TUNNEL_"
# Any Data which needs node information should query this table. 

# ROW KEY : <DATE:TUNNEL_ID>

# Column Qualifier for this table

# TUNNEL_PATH
# TUNNEL_ALL_DETAILS
# TUNNEL_PERFORMANCE
# TUNNEL_*


# ************************************************** # 
#    Creating Table for TRUNK_TABLE Information              #
# ************************************************** #  

echo "create 'TRUNK_TABLE','TRUNK_DETAILS'" | hbase shell 

# All Data related to TRUNK_ is stored in this table. Prefix with "TRUNK_"
# Any Data which needs node information should query this table. 

# ROW KEY : <DATE:TRUNK_ID>

# Column Qualifier for this table

# TRUNK_ALL_DETAILS
# TRUNK_PERFORMANCE
# TRUNK_GROUP_PERFORMANCE
# TRUNK_*








