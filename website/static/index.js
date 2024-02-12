function deleteNote(noteID){
    fetch('/delete-note', {
            method: "POST",
            body: JSON.stringify({noteID:noteID})
        })
        .then((_res) => {
            window.location.href = "/";
        })
        .catch((error) => {
            console.error('Błąd fetch:', error);
        });
    }
