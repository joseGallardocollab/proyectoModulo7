const saldos = document.querySelectorAll('.aw-saldo-cliente');

saldos.forEach(element => {
    const saldo = Number(element.dataset.target);

    element.innerText = new Intl.NumberFormat('es-CL', {
        style: 'currency',
        currency: 'CLP',
        minimumFractionDigits: 0
    }).format(saldo);
});