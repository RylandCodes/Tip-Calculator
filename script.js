document.getElementById('calculate-button').addEventListener('click', () => {
  const price = parseFloat(document.getElementById('price-input').value);
  const tipPercent = parseFloat(document.getElementById('tax-input').value);

  if (isNaN(price) || isNaN(tipPercent)) {
    document.getElementById('result-text').textContent = 'Please enter valid numbers';
    return;
  }

  const tipAmount = price * (tipPercent / 100);
  const total = price + tipAmount;

  document.getElementById('result-text').textContent = `Tip: $${tipAmount.toFixed(
    2
  )} | Total: $${total.toFixed(2)}`;
});
