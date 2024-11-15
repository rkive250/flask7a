<?php
$servername = "sql202.infinityfree.com";
$username = "if0_37717099";
$password = "rkive12345";
$dbname = "if0_37717099_XXX";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

$nombre_completo = $_POST['nombre_completo'];
$fecha_nacimiento = $_POST['fecha_nacimiento'];
$telefono = $_POST['telefono'];
$correo = $_POST['correo'];
$nombre_libro = $_POST['nombre_libro'];
$fecha_apartado = $_POST['fecha_apartado'];

$sql = "INSERT INTO reservas (nombre_completo, fecha_nacimiento, telefono, correo, nombre_libro, fecha_apartado)
        VALUES ('$nombre_completo', '$fecha_nacimiento', '$telefono', '$correo', '$nombre_libro', '$fecha_apartado')";

if ($conn->query($sql) === TRUE) {
    echo "Reserva realizada con éxito.";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>

