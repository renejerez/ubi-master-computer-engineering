package junit;

import java.io.File;
import java.io.FilenameFilter;

public class FilesShow {
    public static void main(String args[]) {

        // try-catch block to handle exceptions
        try {
            File f = new File("C:/Dados/UBI");

            FilenameFilter filter = new FilenameFilter() {
                @Override
                public boolean accept(File f, String name) {
                    // We want to find only .c files
                    return name.endsWith(".py");
                }
            };

            // Note that this time we are using a File class as an array,
            // instead of String
            File[] files = f.listFiles(filter);

            // Get the names of the files by using the .getName() method
            for (int i = 0; i < files.length; i++) {
                System.out.println(files[i].getName());
            }
        } catch (Exception e) {
            System.err.println(e.getMessage());
        }
    }
}