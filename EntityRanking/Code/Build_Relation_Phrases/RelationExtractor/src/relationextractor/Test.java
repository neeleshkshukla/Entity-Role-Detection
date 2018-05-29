/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package relationextractor;

import java.io.File;

/**
 *
 * @author neelesh
 */
public class Test {
    
    public static void main(String...args)
    {
         String ANNOTATED_ARTICLE_PATH = "/media/neelesh/Professional/GitRepository/MTP/EntityRanking/Data/output/StanfordOpenIE/annotated";
	 String RELATION_PATH = "../../Data/output/StanfordOpenIE/relation_extracted";
	    
	    File folder = new File(ANNOTATED_ARTICLE_PATH);
            File[] listOfFiles = folder.listFiles();
            System.out.println(listOfFiles.length);
    }
    
}
