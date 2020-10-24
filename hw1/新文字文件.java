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
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.SequenceFile;
import org.apache.hadoop.io.SequenceFile.Writer;
import org.apache.hadoop.io.SequenceFile.Reader;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.compress.GzipCodec;

public class Hw1 {

  // k = 4
  private static String[] centers = new String[4];

  public static class PreprocessingMap extends Mapper<LongWritable, Text, Text, Text> {


    protected void setup(Context context) throws IOException,InterruptedException {
        // Configuration conf = context.getConfiguration();
        // testStr = conf.get("Name");      
    }

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
                String[] result = val.toString().split(",");
                centers[cnt] = val.toString();
                // centers[cnt] = new Double[24];
                // for (int i = 0; i < result.length; i++) {
                //     centers[cnt][i] = Double.parseDouble(result[i]);
                // }
            }
            cnt++;
            context.write(new Text(""), new Text(val.toString()));            
        } 
        // context.write(new Text(String.valueOf(sum)), new Text(String.valueOf(index)));
        // 365
        // context.write(new Text("Cnt"), new Text(Integer.toString(cnt)));
        // context.write(new Text("Center"), new Text(Arrays.toString(centers)));
    }

    protected void cleanup(Context context) throws IOException, InterruptedException { 
        
        Configuration conf = context.getConfiguration();
        FileSystem fs = FileSystem.getLocal(conf);
        Path seqFilePath = new Path("file.seq");
        SequenceFile.Writer writer = SequenceFile.createWriter(conf,
        Writer.file(seqFilePath), Writer.keyClass(Text.class),
        Writer.valueClass(Text.class));
        writer.append(new Text("key1"), new Text("123"));
        writer.append(new Text("key2"), new Text("456"));
        writer.append(new Text("key3"), new Text("789"));
        writer.append(new Text("key4"), new Text("abc"));
        writer.close();
    }
 }

 public static class KMeanMap extends Mapper<LongWritable, Text, Text, Text> {
    
    protected void setup(Context context) throws IOException,InterruptedException {
        Configuration conf = context.getConfiguration();
        Path seqFilePath = new Path("file.seq");
        SequenceFile.Reader reader = new SequenceFile.Reader(conf,
            Reader.file(seqFilePath));

        Text key = new Text();
        Text val = new Text();
        int cnt = 0;
        while (reader.next(key, val)) {
            System.err.println(key + "\t" + val);
            centers[cnt++] = val.toString();
        }

        reader.close();
    }

    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {

        String line = value.toString();
        String[] result = new String[24];
        result = line.split(",");
        Double smallest = 0.0d;
        int index = 0;
        for (int i = 0; i < 4; i++) {
             context.write(new Text("Cent" + String.valueOf(i)), new Text(centers[i]));
        }
        // for (int i = 0; i < 4; i++) {
        //     for (int j = 0; j < 24; j++) {
        //         Double center = centers[i][j];
        //         Double now = Double.parseDouble(result[j]);
        //         context.write(new Text(String.valueOf(i) + "," + String.valueOf(j)), new Text(String.valueOf(now) + "," +String.valueOf(center)));
        //     }
        // }
        // Double sum = 0.0d;
        // for (int i = 0; i < 24; i++) {
        //     Double now = Double.parseDouble(result[i]);
        //     sum += now;
        // }
        // sum = Math.sqrt(Math.abs(sum));
        // context.write(new Text("123"), new Text(String.valueOf(sum)));

        // for (int i = 0; i < 4; i++) {

        //     Double sum = 0.0d;
        //     for (int j = 0; j < 24; j++) {
        //         Double center = centers[i][j];
        //         Double now = Double.parseDouble(result[j]);
        //         Double v = (center - now) * (center - now);
        //         sum += Math.abs(v);
        //     }
        //     // sum = Math.sqrt(sum);
        //     // if (i == 0) {
        //     //     smallest = sum;
        //     //     index = 0;
        //     // }else if (sum < smallest) {
        //     //     smallest = sum;
        //     //     index = i;
        //     // }
        // }
        // context.write(new Text("123"), new Text("123"));
        // context.write(new Text(String.valueOf(index)), value);

        // String line = value.toString();
        // StringTokenizer tokenizer = new StringTokenizer(line);
        // while (tokenizer.hasMoreTokens()) {
        //     String token = tokenizer.nextToken();
        //     context.write(new Text("KMeanMap"), new Text(token));
        // }
    }
 }

 public static class KMeanReduce extends Reducer<Text, Text, Text, Text> {

    public void reduce(Text key, Iterable<Text> values, Context context)
      throws IOException, InterruptedException {

        int cnt = 0;
        for (Text val : values) {
            cnt++;
            context.write(key, val);
        }
        // 365
        context.write(new Text("Cnt"), new Text(Integer.toString(cnt)));
     
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

    // K-mean
    Configuration conf2 = new Configuration();
    Job jobKMean = new Job(conf2, "KMean");
    jobKMean.setOutputKeyClass(Text.class);
    jobKMean.setOutputValueClass(Text.class);

    jobKMean.setMapperClass(KMeanMap.class);
    jobKMean.setReducerClass(KMeanReduce.class);
    jobKMean.setJarByClass(Hw1.class);

    jobKMean.setInputFormatClass(TextInputFormat.class);
    jobKMean.setOutputFormatClass(TextOutputFormat.class);

    FileInputFormat.addInputPath(jobKMean, new Path(args[1]));
    FileOutputFormat.setOutputPath(jobKMean, new Path(args[2]));

    jobKMean.waitForCompletion(true);
  }

   private static void createCenters (int k) {

   }

}