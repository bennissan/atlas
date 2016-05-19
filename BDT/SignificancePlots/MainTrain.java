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

public class MainTrain {

    private static String USAGE_MESSAGE = "USAGE: java Main [.arff TRAINING FILE NAME]";
    public static void main(String args[]) {

        //TODO: get this from command line
        String[] options = new String[2];
        options[0] =  "-I";
        options[1] = args[1];
        
        //check for correct number of arguments
        if(args.length < 2) {
            System.out.println(USAGE_MESSAGE);
            System.exit(0);
        } else if (args.length > 2) {
            System.out.println(USAGE_MESSAGE);
            System.exit(0);
        }
        
        try {
            Instances trainingData = importData(args[0]);
            AdaBoostM1 booster = createBoosterModel(trainingData, options);
            writeSourceToFile(booster, "AdaBoostClass");
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

    private static AdaBoostM1 createBoosterModel(Instances data, String[] options) 
    {
        AdaBoostM1 booster = new AdaBoostM1();   // new instance with default stumps
        // setting class attribute
        //The class index indicates the target attribute used for classification.
        //By default, in an ARFF file, it is the last attribute
        data.setClassIndex(data.numAttributes() - 1);
        
        try {
            booster.setOptions(options);     // set the options
            booster.buildClassifier(data);   // build classifier
        } catch(Exception e) {
            e.printStackTrace();
            System.exit(0);
        }

        return booster;
    }
    
    // Takes trained AdaBoost model and name of class to write to
    private static void writeSourceToFile(AdaBoostM1 booster, String className)
    {
        try {
            PrintWriter writer = new PrintWriter(className + ".java", "UTF-8");
            writer.print(booster.toSource(className));
            writer.close();
        } catch(Exception e) {
            e.printStackTrace();
            System.exit(0);   
        }
    }
}
