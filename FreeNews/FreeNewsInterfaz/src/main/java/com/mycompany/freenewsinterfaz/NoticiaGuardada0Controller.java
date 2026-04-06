package com.mycompany.freenewsinterfaz;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Label;


public class NoticiaGuardada0Controller {

    @FXML
    private Label titular;
    static String titular_global;
    
    public void cambiarLabel(String titular_string){
        titular.setText(titular_string);
    }
    
    @FXML
    public void switchToNoticia0() throws IOException{
        titular_global = titular.getText();
        App.setRoot("noticia0");
    }
    
    static String getTitularGlobal(){
        return titular_global;
    }
}