<head>
<meta charset="UTF-8">
<title>Genki-Analyser Analyse PDF</title>
<link rel="stylesheet"  href="../Style.css">
</head>
<body>
    <div id=conteneur> 
    <image style="display:inline;" src=../Image/genki.png width='250'/> <h1>GENKI </h1><h2>ANALYSER<h2>
    </div>
    <br>
    <br>
<?php

$nomf=$_GET['action'].'"';

$link='"../PDFR/Rapport-';
$but="<button onclick='window.location.href=";
echo($but.$link.$nomf."'>
  <div class='svg-wrapper-1'>
    <div class='svg-wrapper'>
      <svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' width='24' height='24'>
        <path fill='none' d='M0 0h24v24H0z'></path>
        <path fill='currentColor' d='M1.946 9.315c-.522-.174-.527-.455.01-.634l19.087-6.362c.529-.176.832.12.684.638l-5.454 19.086c-.15.529-.455.547-.679.045L12 14l6-8-8 6-8.054-2.685z'></path>
      </svg>
    </div>
  </div>
  <span>Download</span>
</button>");

 ?>