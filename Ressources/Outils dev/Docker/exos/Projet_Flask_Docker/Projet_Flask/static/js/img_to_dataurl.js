function upload_img() {
    var canvas = document.getElementById("canvas"); //récupération du canvas, càd l'image dessinée
    var dataURL = canvas.toDataURL("image/png"); //conversion de l'image en URL data : il s'agit d'une string représentant l'image en base64
    document.getElementById('data').value = dataURL; //on affecte àl'input data du formulaire l'image sous forme de data url
    var fd = new FormData(document.forms["form1"]); //récupération des données du formulaire (donc des données de l'image)

    var xhr = new XMLHttpRequest({mozSystem: true}); //création d'une requête XML pour échanger avec le serveur
    xhr.open('POST', 'http://127.0.0.1:5000/dataurl', true); //ouverture de la page dataurl POSTsur laquelle on envoie l'url de l'image

    xhr.onreadystatechange = function () { //on définit ce qui se passe lors des changements de la requête XML
        if (xhr.readyState == XMLHttpRequest.DONE) { //si requête terminée, càd formulaire envoyé sur /dataurl puis une fois sur la page,
                                                     //predict_from_dataurl est éxecuté et renvoie la valeur de la prédiction, alors :


            var pred = JSON.parse(xhr.responseText);
            document.getElementById('predRF').innerHTML = pred.rf; //on met à jour les éléments du html en indiquant la valeur prédite
            document.getElementById('predCNN').innerHTML = pred.cnn;
        }
    }

    xhr.onload = function() { //ce qu'on fait à la fin de la requête, ici rien

    };
    xhr.send(fd); //on initie la requête XML avec un paramêtre : le formulaire à envoyé
};