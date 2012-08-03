hadoopscript
============
Please Readme
- hadoop script to setup Single Node Cluster - For Hadoop 1.0.3 Only.
- Tested on Ubuntu 11.10 - Fresh Install.
- Scripts assumes nothing is installed for Hadoop and installs Required Components for Hadoop to run.
- This Script was created using the Installation Guide by Micheal Noll.
http://www.michael-noll.com/tutorials/running-hadoop-on-ubuntu-linux-single-node-cluster/    

HOWTO
-------------------

Steps For Executing Script: Currently script only takes single option at a time :(
-----------------------------------------------------------------------
Execute Help
]$ sudo ./initScriptHadoop.sh --help

usage: ./initScriptHadoop.sh <single-parameter>

  Optional parameters:
     --install-init, -i         Initialization script To Install Hadoop as Single Node Cluster.
     Use the below Options, Once you are logged-in as Hadoop User 'hduser' created in the -i init script above.   
     --install-ssh, -s          Install ssh-keygen -t rsa -P 
     --install-bashrc, -b       Updated '.bashrc' with JAVA_HOME, HADOOP_HOME.
     --ipv6-disable, -v         IPv6 Support Disable.[ Might Not be required. 
                                Updating 'conf/hadoop-env.sh' with 'HADOOP_OPTS=-Djava.net.preferIPv4Stack=true' option in -e]
     --hostname-update, -u      Update Hostname for the system.
     --config-update, -c        Update Configuration with default values (Single Node) in core-site.xml, mapred-site.xml, hdfs-site.xml.
     --update-hadoop-env, -e    Update Hadoop Env Script with JAVA_HOME.
     --help, -h                 Display this Message.

1. First Install prerequisites using -i Option
     ahmed@ahmed-on-Edge:~$ ./initScriptHadoop.sh -i
      Welcome to Precofiguration For Hadoop single node setup wizard 
     
     Would you like install Java 1.6 ? (y/n) y
     Would you like to setup user 'hduser' and 'hadoop Group'? (y/n) y
     Would you like to download Hadoop 1.0.3 and extract to /usr/local? (y/n) y
     Would you like to make 'hduser' owner /usr/local/hadoop/ directory? (y/n) y
     Would you like to login into 'htuser' once done? (y/n) y
     
      Review your choices:
     
      Install Java 1.6             : y
      Setup 'hduser' user          : y
      Download Hadoop 1.0.3        : y
      Setup 'hduser' as Owner      : y
      Login to 'hduser'            : y
     
     Proceed with setup? (y/n)y

2. Login to 'hduser' which will be created in the -i options.
3. Execute options -s, -b, -c, -e 
   /initScriptHadoop.sh -s;
   /initScriptHadoop.sh -b;
   /initScriptHadoop.sh -c;
   /initScriptHadoop.sh -e;
4. Add 'hduser' sudoer list to execute the below commands
5. Execute options -v, -u (OPTIONAL)
   /initScriptHadoop.sh -v;
   /initScriptHadoop.sh -u;