package com.mycompany.freenewsinterfaz;

import java.io.IOException;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.event.ActionEvent;

public class PrimaryController {

    @FXML
    private void switchToLink()  throws IOException {
        App.setRoot("link");
    }
    
    @FXML
    private void switchToNoticiasGuardadas()  throws IOException {
        App.setRoot("noticiaguardada1");
    }
}
