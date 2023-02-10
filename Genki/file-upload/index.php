
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
  

    <form action="file-upload" method="post" class="dropzone" id="my-awesome-dropzone" enctype="multipart/form-data"><input type="submit" name="submit" value="analyser" method="post"/></form>
    <br>
    
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/dropzone/5.9.3/min/dropzone.min.js"></script>

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
    //console.log(file);
    // Faites ce que vous voulez avec le fichier ici
    // ...
    //echo("echo")
  }
</script>
    

</body>
<?php


if ($_GET['action']=='file-upload'){echo("caca");
  // Récupération du fichier PDF envoyé à partir du formulaire
  $file = $_FILES['my-awesome-dropzone'];

  // Vérification de l'erreur de téléchargement
  if ($file['error'] === 0) {
    // Définir le chemin d'enregistrement du fichier
    $path = './PDFA/' . $file['name'];

    // Déplacer le fichier PDF à la destination spécifiée
    if (move_uploaded_file($file['tmp_name'], $path)) {
      echo "Fichier PDF enregistré avec succès.";
    } else {
      echo "Erreur lors de l'enregistrement du fichier PDF.";
    }
  } else {
    echo "Erreur lors du téléchargement du fichier PDF.";
  }
}

/*
if(isset($_POST['submit'])){
  if(!empty($_POST['my-awesome-dropzone'])){
    $image=explode('.',$img);

    $image_ext =end($image);
    if(in_array(strtolower($image_ext),array('pdf'))==false){
        echo 'Rentrez image aux extensions pdf';
    }else{
        $image_size =getimagesize($img_t);
        if($image_size['mime']=='application/pdf'){

            $image_src = imagecreatefrompng($img_t);

        }
      }
}}*/
?>