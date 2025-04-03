document.addEventListener('DOMContentLoaded', function() {
    // Handle reset button
    const resetBtn = document.getElementById('reset-btn');
    if (resetBtn) {
        resetBtn.addEventListener('click', function() {
            document.getElementById('value1').value = '';
            document.getElementById('value2').value = '';
            
            // Remove result box if present
            const resultBox = document.querySelector('.result-box');
            if (resultBox) {
                resultBox.remove();
            }
        });
    }
    
    // Add animation to form submission
    const form = document.getElementById('calculator-form');
    if (form) {
        form.addEventListener('submit', function() {
            const submitBtn = this.querySelector('button[type="submit"]');
            submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>Calculating...';
            submitBtn.disabled = true;
        });
    }
});