/*

   Main.java
   Jared Moskowitz
   10/07/15

   Fiddling With WEKA Java Programs
  */


import java.util.*;
import java.io.*;
import weka.classifiers.meta.*;
import java.nio.file.*;
import weka.core.Instances;
import weka.core.Instance;

public class MainTest {

    private static String USAGE_MESSAGE = "USAGE: java MainTest [.arff TESTING FILE NAME]";
    public static void main(String args[]) {

        
        //check for correct number of arguments
        if(args.length < 2) {
            System.out.println(USAGE_MESSAGE);
            System.exit(0);
        } else if (args.length > 2) {
            System.out.println(USAGE_MESSAGE);
            System.exit(0);
        }
        
        try {
            Instances testingData = importData(args[0]);
            writeScoresToFile(testingData, args[1]);
        } catch(IOException e) {
                e.printStackTrace();
                System.exit(0);
        }
        



        System.exit(1);
    }


    private static Instances importData(String fileName) throws java.io.IOException 
    {
        FileReader reader = new FileReader(fileName);
        Instances data = new Instances(reader);
        data.setClassIndex(data.numAttributes() - 1);
        reader.close();

        return data;
    }
    
    // Takes trained AdaBoost model and name of class to write to
    private static void writeScoresToFile(Instances data, String fileName)
    {
        int instancesCount = data.numInstances();
        int attributesCount = data.numAttributes();
        Object[] point = new Object[attributesCount];
        try {
            PrintWriter writer = new PrintWriter(fileName, "UTF-8");
            for(int i = 0; i<instancesCount; i++) {
                Instance inst = data.instance(i);
                for(int j = 0; j<attributesCount; j++) {
                    point[j] = inst.value(j);
                }
                double[] score = AdaBoostClass.classify(point);
                String classVal = (inst.classValue() > 0)? "+1" : "-1"; //actual predetermined class
                String classification = "" + (score[1] - score[0]) + " " + classVal;
                writer.print(classification);
                writer.println();
            }
            writer.close();
        } catch(Exception e) {
            e.printStackTrace();
            System.exit(0);   
        }
    }
}
