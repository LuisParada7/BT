document.addEventListener('DOMContentLoaded', function () {

    const modal = document.getElementById('options-modal');
    if (!modal) return;
    const closeModalButton = modal.querySelector('.modal-close');
    const optionsButtons = document.querySelectorAll('.custom-btn');

    const editLink = modal.querySelector('#edit-link');
    const deleteForm = modal.querySelector('#delete-form');

    optionsButtons.forEach(button => {
        button.addEventListener('click', function () {
            const reservationId = this.dataset.reservationId;

            editLink.href = `/edit/${reservationId}/`;
            deleteForm.action = `/delete/${reservationId}/`;

            modal.style.display = 'flex';
        });
    });

    if (closeModalButton) {
        closeModalButton.addEventListener('click', function () {
            modal.style.display = 'none';
        });
    }

    window.addEventListener('click', function (event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    });
});