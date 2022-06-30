document.querySelectorAll(".drop-zone__input").forEach((inputElement) => {
  const dropZoneElement = inputElement.closest(".drop-zone");

  dropZoneElement.addEventListener("click", (e) => {
    inputElement.click();
  });

  inputElement.addEventListener("change", (e) => {
    if (inputElement.files.length) {
      updateThumbnail(dropZoneElement, inputElement.files[0]);
    }
  });

// cada que le arrastres algo (dragover) le va a agregar a la lista de clases del elemento el drop-zone--over
  dropZoneElement.addEventListener("dragover", (e) => {
    //default cuando arrastras un archivo a un browser es abrir el archivo o descargarlo
    //we dont want that
    e.preventDefault();
    dropZoneElement.classList.add("drop-zone--over");
  });
//cuando quito lo que estoy arrastrando quitale la clase
  ["dragleave", "dragend"].forEach((type) => {
    dropZoneElement.addEventListener(type, (e) => {
      dropZoneElement.classList.remove("drop-zone--over");
    });
  });

  dropZoneElement.addEventListener("drop", (e) => {
    //default cuando arrastras un archivo a un browser es abrir el archivo o descargarlo
    //we dont want that
    e.preventDefault();
    if (e.dataTransfer.files.length) {
      //e es el evento de hacerle drop a un archivo
      //ese evento viene con una propiedad llamada dataTransfer que trae los archivos que se dropearon
      //aqui estoy tomando esos archivos y se los estoy metiendo al elemento input
      inputElement.files = e.dataTransfer.files;
      //solo me importa el primer archivo asi que llamo la funcion que hace la thumbnail y le paso el primer archivo
      //tambin le paso el elemento completo dropzone
      updateThumbnail(dropZoneElement, e.dataTransfer.files[0]);
    }

    dropZoneElement.classList.remove("drop-zone--over");
  });
});

/**
 * Updates the thumbnail on a drop zone element.
 *
 * @param {HTMLElement} dropZoneElement
 * @param {File} file
 */
function updateThumbnail(dropZoneElement, file) {
  //regresa None la primera vez porque pues no hay thumnail
  let thumbnailElement = dropZoneElement.querySelector(".drop-zone__thumb");

  // First time - remove the text
  if (dropZoneElement.querySelector(".drop-zone__prompt")) {
    dropZoneElement.querySelector(".drop-zone__prompt").remove();
  }

  // First time - there is no thumbnail element, so lets create it
  if (!thumbnailElement) {
    thumbnailElement = document.createElement("div");
    thumbnailElement.classList.add("drop-zone__thumb");
    dropZoneElement.appendChild(thumbnailElement);
  }

  thumbnailElement.dataset.label = file.name;

// si el archivo es un zip carga imagen exito, si no carga imagen error
  if (file.type.startsWith("application/x-zip") || file.type.startsWith("application/zip") ) {
    thumbnailElement.style.backgroundImage = "url(/static/LogoLowRes.png)";
    document.getElementById("SendButton").classList.remove("disabled");
    document.getElementById("SendButton").disabled = false;
  } else {
    thumbnailElement.style.backgroundImage = "url(/static/error-web.png)";
    thumbnailElement.dataset.label = "incorrect Format (Zip required)";
    document.getElementById("SendButton").classList.add("disabled");
    document.getElementById("SendButton").disabled = true;
  }
}
