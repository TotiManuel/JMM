<?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $nombre = $_POST["nombre"];
        $email = $_POST["email"];

        echo "<p>Nombre: $nombre</p>";
        echo "<p>Email: $email</p>";
    } else {
        echo "<p>No se han recibido datos del formulario.</p>";
    }
    ?>