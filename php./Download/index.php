<head>
<meta charset="UTF-8">
<title>Genki-Analyser Analyse PDF</title>
<link rel="stylesheet"  href="../Style.css">
</head>
<body>
    <div id=conteneur> 
    <image style="display:inline;" src=../Image/genki.png width='500'/> <h1>GENKI </h1><h2>ANALYSER<h2>
    </div>
    <br>
    <br>
<?php

$nomf=$_GET['action'];
echo("<a href='../PDFR/Rapport-".$nomf."' >Download</a>");

 ?>