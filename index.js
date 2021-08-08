var debug = true;
var PORT = 5000;

async function send() {
    var message = document.querySelector("#message").value;
    if (debug) {
        console.log(message);
    }

    var chat = document.querySelector("#chat");
    chat.innerHTML +=
        `
        <div class="card">
                            <div class="card-body">
                                ${message}
                            </div>
        </div>
        `;
    await axios.post(`/message/${message}`)
        .then(response => {
            console.log(response);
        })
        .catch(error => {
            console.log(error);
        });
}