/*
 * Sequence File to HDFS Filesystem
 * 
 * We take information from Facebook as Batch
 * and then store them in Sequence file in Hadoop Distributed File System.
 * 
 * */


import java.io.IOException;
import java.net.URI;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.LocalFileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IOUtils;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.SequenceFile;
import org.apache.hadoop.io.Text;

import static java.lang.String.format;
import static java.lang.System.currentTimeMillis;
import static java.lang.System.out;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
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


public class SequenceFileToHDFS {

	private String indexDir;
	private String seqfilesDir;
	private String hadoopDir;
	private int id;
	
	private void setIndexDir(String indexDir) {
		this.indexDir = indexDir;
	}

	private void setSequenceFilesDir(String seqfilesDir) {
		this.seqfilesDir = seqfilesDir;
	}

	private void setIndex(int id) {
		this.id = id;
	}

	private void setHadoopDir(String hadoopDir) {
		this.hadoopDir = hadoopDir;
	}

	@SuppressWarnings("deprecation")
	public static void main(String[] args) throws IOException 
	{
		String accessToken = "<<ACCESS_TOKEN_HERE>>";
		
		//get current date time with Date()
		DateFormat dateFormat = new SimpleDateFormat("yyyy_MM_dd_HH_mm_ss");
		Date date = new Date();
				//System.out.println(dateFormat.format(date));  

		String uri = "sequence_file_"+dateFormat.format(date)+".seq";
		Configuration conf = new Configuration();
        
        /*
         * Uncomment this 2 lines below to get configuratio from the XML
         * Make sure the PATH is set right to get the configuration
         * Which will dump the Sequence file into HADOOP
        */
		//conf.addResource(new Path ("/usr/local/hadoop/conf/core-site.xml"));
		//conf.addResource(new Path ("/usr/local/hadoop/conf/hdfs-site.xml"));
		
        /*Comment these 2 lines below and uncomment above 2 lines to write the data into Hadoop*/
			FileSystem.getLocal(conf); //for local file system
			LocalFileSystem fs = FileSystem.getLocal(conf);
		/*Local Sequence End Here*/
        
        /* Uncomment line below to make it work with Configuration file above <Lines 94/95>*/
		//FileSystem fs = FileSystem.get(URI.create(uri), conf);
		
        Path path = new Path(uri);

		/*
		 * Starting Facebook Retrieval
		 */
		
		DefaultFacebookClient facebookClient = new DefaultFacebookClient(accessToken);
		User user = facebookClient.fetchObject("me", User.class);

		/* 
		 * Building Batch Request to send to Facebook 
		 */
				
		BatchRequest meRequest = new BatchRequestBuilder("me").build();
		BatchRequest meFriendRequest = new BatchRequestBuilder("me/friends").build();
		BatchRequest meLikeRequest = new BatchRequestBuilder("me/likes").parameters(Parameter.with("limit", 5)).build();

		/* Executing BATCH Request */ 
		/* This will be our Sequence Value*/
		List<BatchResponse> batchResponses =
			facebookClient.executeBatch(meRequest, meFriendRequest, meLikeRequest);

		/*
		 * Based on the Response from Facebook 
		 * We create Sequence File.
		 * 
		 */
		
		if(batchResponses.get(0).getCode() == 200)
		{
			/* Creating Sequence Key */
			JsonObject sequencekeyMapUser = new JsonObject();
			sequencekeyMapUser.put("facebookId", user.getId());
			sequencekeyMapUser.put("facebookName",user.getName());
			sequencekeyMapUser.put("timestamp", dateFormat.format(date));

			Text key = new Text();
			Text value = new Text();
			SequenceFile.Writer writer = null;
			try 
			{
				writer = SequenceFile.createWriter(fs, conf, path, key.getClass(), value.getClass());
				key.set(sequencekeyMapUser.toString());
				value.set(batchResponses.toString());
				System.out.printf("[%s]\t%s\t%s\n", writer.getLength(), key, value);
				writer.append(key, value);

			} 
			finally 
			{
				IOUtils.closeStream(writer);
			}
		}
		else if(batchResponses.get(0).getCode() != 200)
		{
			System.out.printf("Access Token Expired\n");
		}
	}
}
