package com.ftp.server;

/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *  http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

import java.io.File;

import org.apache.ftpserver.FtpServer;
import org.apache.ftpserver.FtpServerFactory;
import org.apache.ftpserver.ftplet.User;
import org.apache.ftpserver.ftplet.UserManager;
import org.apache.ftpserver.listener.ListenerFactory;
//import org.apache.ftpserver.main.AddUser;
import org.apache.ftpserver.ssl.SslConfigurationFactory;
import org.apache.ftpserver.usermanager.ClearTextPasswordEncryptor;
import org.apache.ftpserver.usermanager.PropertiesUserManagerFactory;
import org.apache.ftpserver.usermanager.SaltedPasswordEncryptor;
import org.apache.ftpserver.usermanager.UserFactory;
import org.apache.ftpserver.usermanager.impl.BaseUser;
import org.apache.log4j.PropertyConfigurator;
import org.slf4j.impl.Log4jLoggerFactory;

/*
 * @author <a href="http://mina.apache.org">Apache MINA Project</a>
 */
public class EmbeddingFtpServer {

    public static void main(String[] args) throws Exception {
        
    	PropertyConfigurator.configure("log4j.properties");
    	 
    	FtpServerFactory serverFactory = new FtpServerFactory();
        ListenerFactory factory = new ListenerFactory();
        
        // set the port of the listener
        factory.setPort(8080);
        

        // define SSL configuration
//        System.out.println("Creating SSL");
//        SslConfigurationFactory ssl = new SslConfigurationFactory();
//        ssl.setKeystoreFile(new File("ftpserver.jks"));
//        ssl.setKeystorePassword("password");
//
//        // set the SSL configuration for the listener
//        factory.setSslConfiguration(ssl.createSslConfiguration());
//        factory.setImplicitSsl(true);
//        System.out.println("SSL Complete");
        
        // replace the default listener
        serverFactory.addListener("default", factory.createListener());
        
        System.out.println("Adding Users Now");
        PropertiesUserManagerFactory userManagerFactory = new PropertiesUserManagerFactory();
        userManagerFactory.setFile(new File("users.properties"));
        
        
        userManagerFactory.setPasswordEncryptor(new SaltedPasswordEncryptor());
        UserManager userManagement = userManagerFactory.createUserManager();
        UserFactory userFact = new UserFactory();
        userFact.setName("ahmed");
        userFact.setPassword("ahmed");
        userFact.setHomeDirectory("F:/");
        User user = userFact.createUser();
        userManagement.save(user);
        
        serverFactory.setUserManager(userManagement);
        serverFactory.setUserManager(userManagerFactory.createUserManager());
        
        // start the server
        FtpServer server = serverFactory.createServer(); 
        
        System.out.println("Server Starting" + factory.getPort());
        server.start();
    }
}
