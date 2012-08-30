#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

Instructions:

Assumptions:
-----------------------------------

    1. Mahout Path in set in env variable : export PATH=$MAHOUT_HOME/bin:$PATH
    2. Hadoop Home is set in env variable : export PATH=$HADOOP_HOME/bin:$PATH
    3. If you like to setup a SingleNodeCluster on Ubuntu user the script in /installScript directory


Steps to Execute Script
-------------------------------------

    1. Download Mahout from : apache.mahout.org
    2. Download Dataset from http://www.grouplens.org/node/73 > $HOME/Downloads

# Set WORK_DIR as per you setup - in the script 
WORK_DIR=hdfs://localhost:54310/tmp/mahout-work-${USER}

    3. execute : ./factorize-movielens-1M.sh $HOME/Downloads/ml-1m/ml-1m/ratings.dat


=======================================
My $HOME/.bashrc file (sample).
=======================================

#<bashrc START HERE>

# Set Hadoop-related environment variables
export HADOOP_HOME=/usr/local/hadoop

# Set JAVA_HOME (we will also configure JAVA_HOME directly for Hadoop later on)
export JAVA_HOME=/usr/lib/jvm/java-6-sun

# Some convenient aliases and functions for running Hadoop-related commands
unalias fs &> /dev/null
alias fs="hadoop fs"
unalias hls &> /dev/null
alias hls="fs -ls"

# If you have LZO compression enabled in your Hadoop cluster and
# compress job outputs with LZOP (not covered in this tutorial):
# Conveniently inspect an LZOP compressed file from the command
# line; run via:
#
# $ lzohead /hdfs/path/to/lzop/compressed/file.lzo
#
# Requires installed 'lzop' command.
#
lzohead () {
        hadoop fs -cat $1 | lzop -dc | head -1000 | less
}

# Add Hadoop bin/ directory to PATH
export PATH=$PATH:$HADOOP_HOME/bin

# Set Mahout Home
export MAHOUT_HOME=/usr/local/mahout

# Set Path
export PATH=$PATH:$MAHOUT_HOME/bin

#<bashrc END_HERE>
