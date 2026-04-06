package com.mycompany.freenewsinterfaz;

import static com.mycompany.freenewsinterfaz.NoticiaGuardada0Controller.getTitularGlobal;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.net.URL;
import java.util.ArrayList;
import java.util.ResourceBundle;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;


public class Noticia0Controller implements Initializable {
    
    @FXML
    private VBox pantalla;
    
    @FXML
    private Label titular_noticia;
    @FXML
    private Label texto;
    @FXML
    private void switchToNoticiasGuardadas1() throws IOException {
        App.setRoot("noticiaguardada1");
    }
        
    private void cambiarTitular(){
        this.titular_noticia.setText( getTitularGlobal() );
    }
    private void addTexto(){
        
        String texto = "";
        String ruta = "..\\free_news_escritorio\\news\\"+getTitularGlobal();
        //Conseguir los titulares
        try (BufferedReader reader = new BufferedReader(new FileReader(ruta))) {
            String linea; 
            while ( (linea = reader.readLine()) != null) {
                
                texto += linea;
            }
            this.texto.setText(texto);
            System.out.println(texto);
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        
    }
    
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        pantalla.sceneProperty().addListener((obs, oldScene, newScene) -> {
            if (newScene != null) {
                Stage stage = (Stage) newScene.getWindow();
                stage.setWidth(1000);
                stage.setHeight(1000);
            }
        });
    
        cambiarTitular();
        addTexto();
    }    
}
