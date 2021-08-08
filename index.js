function send() {
    var message = document.querySelector("#message").value;
    alert(message);

    // var chat = document.querySelector("#chat");
    chat.innerHTML +=
        `
        <div class="card">
                            <div class="card-body">
                                ${message}
                            </div>
        </div>
        `;
    axios.post(`/message/${message}`)
        .then(response => {
            console.log(response);
        })
        .catch(error => {
            console.log(error);
        });
}