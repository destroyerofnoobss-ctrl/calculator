let display = document.getElementById('display');
let expression = '';

function appendNumber(num) {
    if (num === '.' && expression.includes('.')) {
        return; // Prevent multiple decimal points
    }
    expression += num;
    updateDisplay();
}

function appendOperator(op) {
    if (expression === '') return;
    // Prevent multiple operators in a row
    const lastChar = expression[expression.length - 1];
    if (['+', '-', '*', '/', '%'].includes(lastChar)) {
        expression = expression.slice(0, -1) + op;
    } else {
        expression += op;
    }
    updateDisplay();
}

function clearDisplay() {
    expression = '';
    updateDisplay();
}

function deleteLast() {
    expression = expression.slice(0, -1);
    updateDisplay();
}

function calculate() {
    if (expression === '') return;
    
    try {
        // Use Function constructor instead of eval for better safety
        const result = Function('"use strict"; return (' + expression + ')')();
        expression = result.toString();
        updateDisplay();
    } catch (error) {
        display.value = 'Error';
        expression = '';
    }
}

function updateDisplay() {
    display.value = expression || '0';
}

// Keyboard support
document.addEventListener('keydown', (e) => {
    if (e.key >= '0' && e.key <= '9') appendNumber(e.key);
    if (e.key === '.') appendNumber('.');
    if (e.key === '+' || e.key === '-' || e.key === '*' || e.key === '/') {
        e.preventDefault();
        appendOperator(e.key);
    }
    if (e.key === '%') {
        e.preventDefault();
        appendOperator('%');
    }
    if (e.key === 'Enter') {
        e.preventDefault();
        calculate();
    }
    if (e.key === 'Backspace') {
        e.preventDefault();
        deleteLast();
    }
    if (e.key === 'Escape') {
        e.preventDefault();
        clearDisplay();
    }
});

// Initialize display
updateDisplay();