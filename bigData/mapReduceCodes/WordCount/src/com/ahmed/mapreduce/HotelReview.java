/**
 * 
 */
package com.ahmed.mapreduce;

import java.io.IOException;
import java.util.*;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.record.CsvRecordInput;
import org.apache.hadoop.util.*;

/**
 * @author Ahmed
 * 
 * CSV File will have the given information.
 * HotelId,	HotelName,		HotelDescription,	HotelAddress,				HotelCustomerReview,	HotelCustomerId,	HotelCustomerRating
 * 12345,	Hotel Spring,	Bangalore INDIA,	Hotel in Bangalore INDIA,	GOOD Hotel,				1,					5
 * 
 * Code is similar to a wordCount Program.
 * 
 * All we are doing in "Map" is get Hotel Information (Hotel Name) 
 * from every line (Object) And get rating from the Line 
 * and Assign it to the "Collector", 
 * "Reduce" do will do the rest to combine all the data
 * 
 */

public class HotelReview {

	public static class Map extends MapReduceBase implements
			Mapper<LongWritable, Text, Text, IntWritable> {
		private final static IntWritable hotelCustomerRating = new IntWritable(1);
		private Text hotelName = new Text();

		@Override
		public void map(LongWritable key, Text value,
				OutputCollector<Text, IntWritable> output, Reporter reporter)
				throws IOException {
			String line = value.toString();
			String[] lineSplit = line.split(",");
			StringTokenizer tokens = new StringTokenizer(line,",");
			
			hotelName.set(lineSplit[1]);
			hotelCustomerRating.set(Integer.parseInt(lineSplit[6]));
		
			output.collect(hotelName, hotelCustomerRating);

		}

	}

	public static class Reduce extends MapReduceBase implements
			Reducer<Text, IntWritable, Text, IntWritable> {

		@Override
		public void reduce(Text key, Iterator<IntWritable> value,
				OutputCollector<Text, IntWritable> outputCollector,
				Reporter reporter) throws IOException {
			int sum = 0;
			while (value.hasNext()) {
				sum = sum + value.next().get();
			}
			outputCollector.collect(key, new IntWritable(sum));
		}

	}

	public static void main(String[] args) throws Exception {
		JobConf conf = new JobConf(HotelReview.class);
		conf.setJobName("HotelReviewCode");

		conf.setOutputKeyClass(Text.class);
		conf.setOutputValueClass(IntWritable.class);

		conf.setMapperClass(Map.class);
		conf.setCombinerClass(Reduce.class);
		conf.setReducerClass(Reduce.class);

		conf.setInputFormat(TextInputFormat.class);
		conf.setOutputFormat(TextOutputFormat.class);

		FileInputFormat.setInputPaths(conf, new Path(args[0]));
		FileOutputFormat.setOutputPath(conf, new Path(args[1]));

		JobClient.runJob(conf);

	}

}