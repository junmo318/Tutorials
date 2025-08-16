let display = document.getElementById('result');
let currentInput = '';
let operator = '';
let previousInput = '';
let shouldResetDisplay = false;

function appendToDisplay(value) {
    if (shouldResetDisplay) {
        clearDisplay();
        shouldResetDisplay = false;
    }
    
    if (display.value === '0' && value !== '.') {
        display.value = value;
    } else {
        display.value += value;
    }
}

function clearDisplay() {
    display.value = '0';
    currentInput = '';
    operator = '';
    previousInput = '';
    shouldResetDisplay = false;
}

function deleteLast() {
    if (display.value.length > 1) {
        display.value = display.value.slice(0, -1);
    } else {
        display.value = '0';
    }
}

function calculate() {
    try {
        let expression = display.value;
        
        // Replace display symbols with actual operators
        expression = expression.replace(/×/g, '*');
        expression = expression.replace(/÷/g, '/');
        expression = expression.replace(/−/g, '-');
        
        // Basic validation to prevent code injection
        if (!/^[0-9+\-*/.() ]+$/.test(expression)) {
            throw new Error('Invalid expression');
        }
        
        let result = eval(expression);
        
        // Handle division by zero and other edge cases
        if (!isFinite(result)) {
            throw new Error('Invalid operation');
        }
        
        // Round to prevent floating point precision issues
        result = Math.round(result * 100000000) / 100000000;
        
        display.value = result.toString();
        shouldResetDisplay = true;
        
    } catch (error) {
        display.value = 'Error';
        shouldResetDisplay = true;
    }
}

// Add keyboard support
document.addEventListener('keydown', function(event) {
    const key = event.key;
    
    // Numbers and decimal point
    if (/[0-9.]/.test(key)) {
        appendToDisplay(key);
    }
    // Operators
    else if (key === '+') {
        appendToDisplay('+');
    }
    else if (key === '-') {
        appendToDisplay('−');
    }
    else if (key === '*') {
        appendToDisplay('×');
    }
    else if (key === '/') {
        event.preventDefault(); // Prevent browser search
        appendToDisplay('÷');
    }
    // Enter or equals
    else if (key === 'Enter' || key === '=') {
        event.preventDefault();
        calculate();
    }
    // Escape or C for clear
    else if (key === 'Escape' || key.toLowerCase() === 'c') {
        clearDisplay();
    }
    // Backspace for delete
    else if (key === 'Backspace') {
        event.preventDefault();
        deleteLast();
    }
});

// Initialize display
clearDisplay();