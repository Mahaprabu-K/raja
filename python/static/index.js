function saveData() {

    let name = document.getElementById("name").value;
    let age = document.getElementById("age").value;

    fetch("/save", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: name,
            age: age
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => {
        console.log(error);
    });

}