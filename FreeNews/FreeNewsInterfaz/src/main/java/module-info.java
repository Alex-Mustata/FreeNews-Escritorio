module com.mycompany.freenewsinterfaz {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.base;

    opens com.mycompany.freenewsinterfaz to javafx.fxml;
    exports com.mycompany.freenewsinterfaz;
}
