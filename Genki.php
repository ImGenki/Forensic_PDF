
<head>
<meta charset="UTF-8">
<title>Genki-Analyser Analyse PDF</title>
<link rel="stylesheet"  href="Style.css">
</head>
<body>
    <div id=conteneur> 
    <image style="display:inline;" src=./Image/genki.png width='500'/> <h1>GENKI </h1><h2>ANALYSER<h2>
    </div>
    <br>
    <br>
    <div id="drop-area">
     <form action="upload.php" method="post" enctype="multipart/form-data">
     <input type="file" name="file" id="file" class="inputfile" />
     <label for="file">Glissez un fichier ici ou cliquez pour sélectionner un fichier</label>
     <input type="submit">
     </form>
    </div>

<script>
  var dropArea = document.getElementById("drop-area");

  // Ajoutez les événements de gestion des fichiers glissés sur la zone de dépôt
  dropArea.addEventListener("dragenter", handleDragEnter, false);
  dropArea.addEventListener("dragover", handleDragOver, false);
  dropArea.addEventListener("dragleave", handleDragLeave, false);
  dropArea.addEventListener("drop", handleFileDrop, false);

  // Changez la classe de la zone de dépôt lorsque les fichiers sont glissés sur la zone
  function handleDragEnter(e) {
    this.classList.add("drag-over");
  }

  function handleDragOver(e) {
    e.preventDefault();
    e.stopPropagation();
  }

  function handleDragLeave(e) {
    this.classList.remove("drag-over");
  }

  function handleFileDrop(e) {
    e.preventDefault();
    e.stopPropagation();

    this.classList.remove("drag-over");

    var files = e.dataTransfer.files;
    var file = files[0];
    console.log(file);
    // Faites ce que vous voulez avec le fichier ici
    // ...
    echo("echo")
  }
</script>
    

</body>
<?php


?>