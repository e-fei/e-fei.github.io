document.addEventListener('DOMContentLoaded', function () {
  const buttons = document.querySelectorAll('[data-filter]');
  const cards = document.querySelectorAll('.publication-card[data-selected]');
  const empty = document.getElementById('no-selected-publications');
  function filter(value) {
    let visible = 0;
    cards.forEach(function (card) {
      card.hidden = value === 'selected' && card.dataset.selected !== 'true';
      if (!card.hidden) visible++;
    });
    buttons.forEach(function (button) {
      const active = button.dataset.filter === value;
      button.classList.toggle('active', active);
      button.setAttribute('aria-pressed', String(active));
    });
    if (empty) empty.hidden = visible > 0;
  }
  buttons.forEach(function (button) {
    button.addEventListener('click', function () { filter(button.dataset.filter); });
  });
  if (buttons.length) filter('selected');
});
