import java.io.IOException;
import java.util.*;
import org.json.*;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;


public class Test {

  // k = 4
  private static String[] centers = new String[4];
  private static String testStr = "";
  
  public static class PreprocessingMap extends Mapper<LongWritable, Text, Text, Text> {

    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {

        String line = value.toString(); 
        StringTokenizer tokenizer = new StringTokenizer(line);
        while (tokenizer.hasMoreTokens()) {
            String token = tokenizer.nextToken();
            String[] result = token.split(",");
            if (result[2].equals("PM2.5") && result[1].equals("大里")) {
                
                String[] subResult = Arrays.copyOfRange(result, 3, result.length);
                for (int i = 0; i < subResult.length; i++) {
                    
                    if (subResult[i].equals("") || subResult[i].equals("NR")) {
                        subResult[i] = "0";
                    }else {

                        subResult[i] = subResult[i].replace("*","");
                        subResult[i] = subResult[i].replace("#","");
                        subResult[i] = subResult[i].replace("x","");
                        if (subResult[i].contains("-")) {
                            subResult[i] = "0";
                        }
                        // if (Float.parseFloat(subResult[i]) < 0) {
                        //     subResult[i] = "0";
                        // }
                    }
                }
                // context.write(new Text("PM2.5"), new Text(result[1] + "," + Arrays.toString(subResult)));
                String output = Arrays.toString(subResult);
                output = output.replace("[","");
                output = output.replace("]","");
                context.write(new Text("PM2.5"), new Text(output));
                // context.write(new Text("PM2.5"), new Text(token));
            }
        }
    }
 }

 public static class PreprocessingReduce extends Reducer<Text, Text, Text, Text> {

    public void reduce(Text key, Iterable<Text> values, Context context)
      throws IOException, InterruptedException {
        
        int cnt = 0;
        for (Text val : values) {
            if (cnt < 4) {
                centers[cnt] = val.toString();
            }
            cnt++;
            context.write(new Text(""), new Text(val.toString()));            
        }
        // 365
        // context.write(new Text("Cnt"), new Text(Integer.toString(cnt)));
        // context.write(new Text("Center"), new Text(Arrays.toString(centers)));

    }
 }

 public static void main(String[] args) throws Exception {

    // Preprocessing
    Configuration conf = new Configuration();
    Job job = new Job(conf, "Preprocessing");

    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(Text.class);

    job.setMapperClass(PreprocessingMap.class);
    job.setReducerClass(PreprocessingReduce.class);
    job.setJarByClass(Hw1.class);

    job.setInputFormatClass(TextInputFormat.class);
    job.setOutputFormatClass(TextOutputFormat.class);

    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));

    job.waitForCompletion(true);
  }

}