/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package relationextractor;

/**
 *
 * @author neelesh
 */
import edu.stanford.nlp.ling.CoreAnnotations;
import edu.stanford.nlp.pipeline.Annotation;
import edu.stanford.nlp.pipeline.StanfordCoreNLP;
import edu.stanford.nlp.util.CoreMap;
import edu.stanford.nlp.ie.util.RelationTriple;
import edu.stanford.nlp.naturalli.NaturalLogicAnnotations;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.Properties;

public class RelationExtractor {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        RelationExtractor re = new RelationExtractor();
        re.buildAllRelations();
    }
    
    public void buildAllRelations() {
        try {
            
            HashMap<String, Integer> relationStringMap = new HashMap<>();
            Properties props = new Properties();
            props.setProperty("annotators", "tokenize,ssplit,pos,lemma,depparse,natlog,openie");
            StanfordCoreNLP core = new StanfordCoreNLP(props);

            System.out.println("Stanford Core NLP Initialized");

            BufferedReader br = null;
            //PrintWriter pw = null;
            PrintWriter pwrel = null;
            String line;
            
	    String ANNOTATED_ARTICLE_PATH = "/media/neelesh/Professional/GitRepository/MTP/EntityRanking/Data/output/StanfordOpenIE/annotated/11/";
	    String RELATION_PATH = "/media/neelesh/Professional/GitRepository/MTP/EntityRanking/Data/output/StanfordOpenIE/relation_extracted/11/";
	    String OPENIE_PATH = "/media/neelesh/Professional/GitRepository/MTP/EntityRanking/Data/output/StanfordOpenIE/";
	    File folder = new File(ANNOTATED_ARTICLE_PATH);
	    File[] listOfFiles = folder.listFiles();
            //System.out.println(listOfFiles.length);
            StringBuffer relationPhraseFilePath = new StringBuffer();
            relationPhraseFilePath.append(OPENIE_PATH).append("relation_phrases_11.csv");
            pwrel = new PrintWriter(new FileWriter(relationPhraseFilePath.toString()));
            System.out.println("Total files: " + listOfFiles.length);
            int filesProcessed = 0;
            for (File file : listOfFiles) {
                try{
                filesProcessed = filesProcessed +1;
                System.out.println("Number of files processed: " + filesProcessed);
                System.out.println("Reading File"+ file.getName());
		if (file.isFile()) {
                //System.out.println(" File"+ file.getName());
                StringBuffer inFilePath = new StringBuffer();
                StringBuffer outFilePath = new StringBuffer();
                
                inFilePath.append(ANNOTATED_ARTICLE_PATH).append(file.getName());
                outFilePath.append(RELATION_PATH).append(file.getName());
                
                File file1 = new File(inFilePath.toString());

                if (file1.exists()) {
                    //System.out.println("File exists: " + file1.getName());

                    // Read file                   
                    br = new BufferedReader(new FileReader(inFilePath.toString()));
                   // pw = new PrintWriter(new FileWriter(outFilePath.toString()));
                    
                    

                    // Read all lines
                    while ((line = br.readLine()) != null) {

                        Annotation doc = new Annotation(line);
                        core.annotate(doc);

                        for (CoreMap sentence : doc.get(CoreAnnotations.SentencesAnnotation.class)) {
                            Collection<RelationTriple> triples = sentence.get(NaturalLogicAnnotations.RelationTriplesAnnotation.class);
                            for (RelationTriple triple : triples) {

                               /** pw.write("("
                                        + triple.subjectLemmaGloss() + "#"
                                        + triple.relationLemmaGloss() + "#"
                                        + triple.objectLemmaGloss() + ")\n");**/
                                 String relation = triple.relationLemmaGloss();
                                 if(relationStringMap.containsKey(relation))
                                 {
                                    int count = relationStringMap.get(relation);
                                    relationStringMap.put(relation, count+1);
                                 }
                                 else
                                     relationStringMap.put(relation, 1);
                            //System.out.println("Relation "+relation+" "+relationStringMap.get(relation));
                            }
                            
                        }
                    }
                    br.close();
                   // pw.close();

                }
                else
                {
                    System.out.println(file.getName() +"File doesn't exist");
                }
            }
            }
            catch(Exception e)
                    {
                    System.out.println(e.getMessage());
                    }
           }
            
        for(Map.Entry entry: relationStringMap.entrySet())
        {
            pwrel.write(entry.getKey()+","+entry.getValue()+"\n");
        }
        pwrel.close();
        } catch (Exception e) {
            
            e.printStackTrace();
        }

    }
    
}
