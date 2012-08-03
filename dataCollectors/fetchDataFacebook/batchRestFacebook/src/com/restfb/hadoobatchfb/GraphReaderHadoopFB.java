package com.restfb.hadoobatchfb;

import static java.lang.String.format;
import static java.lang.System.currentTimeMillis;
import static java.lang.System.out;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.restfb.Connection;
import com.restfb.DefaultFacebookClient;
import com.restfb.DefaultJsonMapper;
import com.restfb.Facebook;
import com.restfb.FacebookClient;
import com.restfb.JsonMapper;
import com.restfb.Parameter;
import com.restfb.batch.BatchRequest;
import com.restfb.batch.BatchRequest.BatchRequestBuilder;
import com.restfb.batch.BatchResponse;
import com.restfb.json.JsonArray;
import com.restfb.json.JsonObject;
import com.restfb.types.Page;
import com.restfb.types.Post;
import com.restfb.types.Url;
import com.restfb.types.User;


public class GraphReaderHadoopFB {

  public static void main(String[] args) {

      /* 
         Get you access token from Facebook link below
         https://developers.facebook.com/tools/explorer
      */
	  DefaultFacebookClient facebookClient = new DefaultFacebookClient("<<ACCESS_TOKEN_HER>>");
	  
	  	out.println("Starting BATCH \n");
	  
	  	//Building Batch Request to send to Facebook
	  	out.println("Creating BATCH \n");
		BatchRequest meRequest = new BatchRequestBuilder("me").build();
		BatchRequest meFriendRequest = new BatchRequestBuilder("me/friends").build();
		BatchRequest meLikeRequest = new BatchRequestBuilder("me/likes").parameters(Parameter.with("limit", 5)).build();
		
		
		//Creating POST Request - Not working yet - moved to GET
		out.println("Posting Request \n");
		BatchRequest postRequest = new BatchRequestBuilder("me").method("GET")
				.body(Parameter.with("message", "Info!!!")).build();

		//Executing BATCH Request 
		out.println("Complete Batch Response \n");
		List<BatchResponse> batchResponses =
				facebookClient.executeBatch(meRequest, meFriendRequest, meLikeRequest, postRequest);
		
		
		//Got Response we can use this information to process further.
		out.println("\n Response \n");
		BatchResponse meResponse = batchResponses.get(0);
		BatchResponse meFriendResponse = batchResponses.get(1);
		BatchResponse meLikeResponse = batchResponses.get(2);
		BatchResponse postResponse = batchResponses.get(3);
		
		out.println("\n *********** Individual Reponse ************* \n");
		
		out.println("\n meResponse \n");
		out.println(meResponse.getBody());
		
		out.println("\n meFriendResponse \n");
		out.println(meFriendResponse.getBody());
		
		out.println("\n meLikeResponse Getting 5 (LIMITED) \n");
		out.println(meLikeResponse.getBody());
		
		out.println("\n postResponse \n");
		out.println(postResponse.getBody());
		
  }
}