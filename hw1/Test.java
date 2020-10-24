import java.io.IOException;
import java.util.*;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;

public class Test {

  public static class Map extends Mapper<LongWritable, Text, Text, Text> {
    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String line = value.toString();
        String[] result = line.split(",");
        context.write(new Text("Station"), new Text(result[1]));
        context.write(new Text("Type"), new Text(result[2]));        
        StringTokenizer tokenizer = new StringTokenizer(line);
        while (tokenizer.hasMoreTokens()) {
            String token = tokenizer.nextToken();
            context.write(new Text("What ever you like"), new Text(token));
        }
    }
 }

 public static class Reduce extends Reducer<Text, Text, Text, Text> {

    public void reduce(Text key, Iterable<Text> values, Context context)
      throws IOException, InterruptedException {
        if (key.toString() == "What ever you like") {

          int cnt = 0;
          String temp = "";
          for (Text val : values) {
              // sum += val.get();
              temp = val.toString();
              cnt++;
          }
          Text outputStr = new Text(Integer.toString(cnt) + temp);
          context.write(key, outputStr);
        }else {
          
          for (Text val : values) {
            context.write(key, new Text(val.toString()));
          }

          // HashMap hm = new HashMap();
          // for (Text val : values) {
          //   if (hm.containsKey((val.toString()))) {
          //     int cnt = (int)hm.get(val.toString()) + 1;
          //     hm.put(val.toString(), cnt);
          //   }else {
              
          //     hm.put(val.toString(), 1);
          //   }
          // }
          
          // Iterator iterator  = hm.entrySet().iterator();
          // while(iterator.hasNext()) {
          //   String key1 = (String) iterator.next();
          //   String val1 = (String) hm.get(key1);
          //   context.write(new Text(key1), new Text(val1));
          // }
      }        
    }
 }

 public static void main(String[] args) throws Exception {

    Configuration conf = new Configuration();
    Job job = new Job(conf, "Test");

    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(Text.class);

    job.setMapperClass(Map.class);
    job.setReducerClass(Reduce.class);
    job.setJarByClass(Test.class);

    job.setInputFormatClass(TextInputFormat.class);
    job.setOutputFormatClass(TextOutputFormat.class);

    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));

    job.waitForCompletion(true);
  }

}