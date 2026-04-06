
package com.mycompany.freenewsinterfaz;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;

import java.io.*;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.text.Text;


public class LinkController {
    
    @FXML
    private TextField link;
    
    @FXML
    private Text respuesta;
    
    @FXML
    private Button enviar;
    
    String enlace = "";
    File archivo_enlace =  new File("..\\free_news_escritorio\\java_python.txt");
    long error;
    
    @FXML
    private void switchToPrimary() throws IOException {
        App.setRoot("primary");
    }
    
    public void crearArchivo() throws IOException{
        
        if (!archivo_enlace.exists()) {
            archivo_enlace.createNewFile();
        }
    }
    
    public void ejecutarScriptPython() throws IOException, InterruptedException{
        String ruta = "..\\free_news_escritorio\\FreeNews.py";
        Process p = new ProcessBuilder("python", ruta).redirectErrorStream(true).start();
        
        error = p.getInputStream().transferTo(System.out);
        System.out.println(error);
        
    }
    
    public void enviarEnlace(ActionEvent event) throws IOException {
        enlace = link.getText();
        if (enlace.contains("https://elpais.com")) {
            crearArchivo();
            
            try (FileWriter fw = new FileWriter(archivo_enlace);){
                
                fw.write("elpais");
                fw.append("\n");
                fw.append(enlace);
                
                Thread.sleep(500);
            }
            catch (Exception e){
                e.printStackTrace();
                respuesta.setText("Ocurrio un error");
            }
            
        } else if(enlace.contains("https://www.diariosur.es")){
            crearArchivo();
            
            try (FileWriter fw = new FileWriter(archivo_enlace);){
                
                fw.write("diariosur");
                fw.append("\n");
                fw.append(enlace);
                
                Thread.sleep(500);
            }
            catch (Exception e){
                e.printStackTrace();
                respuesta.setText("Ocurrio un error");
            }
            
        } else if(enlace.contains("https://www.eldiario.es")){
            crearArchivo();
            
            try (FileWriter fw = new FileWriter(archivo_enlace);){
                
                fw.write("eldiario");
                fw.append("\n");
                fw.append(enlace);
                
                Thread.sleep(500);
            }
            catch (Exception e){
                e.printStackTrace();
                respuesta.setText("Ocurrio un error");
            }
            
        } else if(enlace.contains("https://www.abc.es")){
            crearArchivo();
            
            try (FileWriter fw = new FileWriter(archivo_enlace);){
                
                fw.write("abc");
                fw.append("\n");
                fw.append(enlace);
                
                Thread.sleep(500);
            }
            catch (Exception e){
                e.printStackTrace();
                respuesta.setText("Ocurrio un error");
            }
            
        } else if(enlace.contains("https://www.diariovasco.com")){
            crearArchivo();
            
            try (FileWriter fw = new FileWriter(archivo_enlace);){
                
                fw.write("diariovasco");
                fw.append("\n");
                fw.append(enlace);
                
                Thread.sleep(500);
            }
            catch (Exception e){
                e.printStackTrace();
                respuesta.setText("Ocurrio un error");
            }
        }
            
        
        try {
            ejecutarScriptPython();

           if (error == 31 || error == 119) {
                respuesta.setVisible(true);
                respuesta.setText("Operación realizada con exito"); 
           }else{
                respuesta.setVisible(true);
                respuesta.setText("Ocurrio un error");
            }
        }
        catch (Exception e){
            e.printStackTrace();
        }
            
        
    }
    
}
