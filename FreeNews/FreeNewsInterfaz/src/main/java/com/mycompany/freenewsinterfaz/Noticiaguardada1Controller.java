package com.mycompany.freenewsinterfaz;

import java.util.*;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.ResourceBundle;
import javafx.application.Platform;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.control.Label;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.Priority;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class Noticiaguardada1Controller implements Initializable { 
    
    private int cantidad_noticias;
    private ArrayList<String> lista_titulares = new ArrayList<>();
    
    @FXML
    private AnchorPane pantalla;
    
    @FXML
    private VBox caja_noticias;
    
    @FXML
    private void switchToLinks()  throws IOException {
        App.setRoot("primary");
    }
    
    private void leerNoticias(){
        String ruta = "..\\free_news_escritorio\\informacion.csv";
        
        //Conseguir la cantidad de noticias que hay contando las lineas del CSV
        try (BufferedReader reader = new BufferedReader(new FileReader(ruta))) {
            while (reader.readLine() != null) {
                cantidad_noticias++;
            }
            System.out.println(cantidad_noticias);
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
    
    private void llenarListaTitulares(){
        String ruta = "..\\free_news_escritorio\\titulares.txt";
        //Conseguir los titulares
        try (BufferedReader reader = new BufferedReader(new FileReader(ruta))) {
            String linea; 
            while ( (linea = reader.readLine()) != null) {
                System.out.println(linea);
                lista_titulares.add(linea);
            }
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
    
    @FXML
    public void crearNoticia() throws IOException{
       
       for (int i = 1; i < cantidad_noticias; i++) {
           
            FXMLLoader loader = new FXMLLoader(getClass().getResource("/com/mycompany/freenewsinterfaz/noticiaguardada0.fxml")); 
            
            //Cargamos el padre (noticia) y el controlador para poder editar el titular
            AnchorPane noticia = loader.load();
            NoticiaGuardada0Controller controller = loader.getController();
            
            caja_noticias.getChildren().add(noticia);
            controller.cambiarLabel(lista_titulares.get(i-1));
            
        }
    }
    
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        
        pantalla.sceneProperty().addListener((obs, oldScene, newScene) -> {
            if (newScene != null) {
                Stage stage = (Stage) newScene.getWindow();
                stage.setWidth(764);
                stage.setHeight(480);
            }
        });
        
        try {
            leerNoticias();
            llenarListaTitulares();
            crearNoticia();
            
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }    
}
