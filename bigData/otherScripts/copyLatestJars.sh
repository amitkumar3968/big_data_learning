DIR=11June2013
HOME=/home/ahmed/tellabs
DEV=development_branch
echo $DIR
echo $HOME
echo $DEV


cp $HOME/$DIR/$DEV/core/core-api/target/li-core-api-1.0.jar /var/local/libjars/
cp $HOME/$DIR/$DEV/data-dictionary/api/target/li-data-dictionary-api-1.0.jar /var/local/libjars/
cp $HOME/$DIR/$DEV/data-pipeline/model/target/li-data-pipeline-model-1.0.jar /var/local/libjars/
cp $HOME/$DIR/$DEV/li-extension/li-extension-tellabs/target/li-extension-tellabs-1.0.jar /var/local/libjars/
cp $HOME/$DIR/$DEV/platform/li-platform-common-api/target/li-platform-common-api-1.0.jar /var/local/libjars/
cp $HOME/$DIR/$DEV/platform/li-platform-dynamic-ui/target/li-platform-dynamic-ui-1.0.jar /var/local/libjars/
cp $HOME/$DIR/$DEV/data-pipeline/web/target/li-data-pipeline-web/WEB-INF/lib/li-platform-model-1.0.jar /var/local/libjars/
cp $HOME/$DIR/$DEV/utils/bsf/target/li-utils-bsf-1.0.jar /var/local/libjars/
cp $HOME/$DIR/$DEV/li-extension/web/target/li-extension/WEB-INF/lib/bsf-2.4.0.jar  /var/local/libjars/
cp $HOME/$DIR/$DEV/core/core-web/target/li-core-web-1.0/WEB-INF/lib/commons-lang3-3.1.jar /var/local/libjars/
cp $HOME/$DIR/$DEV/li-extension/web/target/li-extension/WEB-INF/lib/li-extension-tellabs-1.0.jar /var/local/libjars/
cp $HOME/$DIR/$DEV/li-extension/web/target/war/work/com.li/li-integration/WEB-INF/lib/li-platform-runtime-1.0.jar  /var/local/libjars/
cp $HOME/$DIR/$DEV/li-extension/web/target/war/work/com.li/li-integration/WEB-INF/lib/li-data-collector-api-1.0.jar  /var/local/libjars/
cp $HOME/$DIR/$DEV/integration/target/war/work/com.li/li-data-collector-web/WEB-INF/lib/commons-lang3-3.1.jar  /var/local/libjars/
cp $HOME/$DIR/$DEV/li-extension/web/target/war/work/com.li/li-integration/WEB-INF/lib/hbase-0.94.2-cdh4.2.0.jar /var/local/libjars/
cp $HOME/$DIR/$DEV/li-extension/web/target/war/work/com.li/li-integration/WEB-INF/lib/jackson-annotations-2.1.2.jar /var/local/libjars/
cp $HOME/$DIR/$DEV/li-extension/web/target/war/work/com.li/li-integration/WEB-INF/lib/jackson-core-2.1.2.jar /var/local/libjars/
cp $HOME/$DIR/$DEV/li-extension/web/target/war/work/com.li/li-integration/WEB-INF/lib/jackson-databind-2.1.2.jar /var/local/libjars/
cp $HOME/$DIR/$DEV/li-extension/web/target/war/work/com.li/li-integration/WEB-INF/lib/mahout-core-0.7-cdh4.2.0.jar /var/local/libjars/
cp $HOME/$DIR/$DEV/li-extension/web/target/war/work/com.li/li-integration/WEB-INF/lib/mahout-math-0.7-cdh4.2.0.jar /var/local/libjars/
cp $HOME/$DIR/$DEV/li-extension/web/target/war/work/com.li/li-integration/WEB-INF/lib/zookeeper-3.4.3-cdh4.1.2.jar /var/local/libjars/

# Shorter Script for the above - Need to test this.
#---
#cp $HOME/$DIR/$DEV/li-extension/web/target/war/work/com.li/li-integration/WEB-INF/lib/li* /var/local/libjars/
#cp $HOME/$DIR/$DEV/li-extension/web/target/war/work/com.li/li-integration/WEB-INF/lib/mahout* /var/local/libjars/
#cp $HOME/$DIR/$DEV/li-extension/web/target/war/work/com.li/li-integration/WEB-INF/lib/jackson* /var/local/libjars/
#cp $HOME/$DIR/$DEV/li-extension/web/target/war/work/com.li/li-integration/WEB-INF/lib/hbase* /var/local/libjars/
#cp $HOME/$DIR/$DEV/li-extension/web/target/war/work/com.li/li-integration/WEB-INF/lib/bsf* /var/local/libjars/
#cp $HOME/$DIR/$DEV/li-extension/web/target/war/work/com.li/li-integration/WEB-INF/lib/common-lang* /var/local/libjars/
#---
