package junit;

import java.io.File;

public class FilesSelect {
    
    public static void main(String[]args)
    {
        File curDir = new File("C:/Dados/UBI/14450-QA");
        getAllFiles(curDir);
    }
    private static void getAllFiles(File curDir) {

        File[] filesList = curDir.listFiles();
        for(File f : filesList){
            if(f.isDirectory())
                getAllFiles(f);
            if(f.isFile()){
                System.out.println(f.getName());
            }
        }

    }


}
