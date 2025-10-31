document.addEventListener('DOMContentLoaded', () => {
  const input = document.getElementById('demo-input');
  const run = document.getElementById('demo-run');
  const out = document.getElementById('demo-output');

  run.addEventListener('click', () => {
    const v = Number(input.value || 0);
    const step1 = v + 1;
    const step2 = step1 + 1;
    out.textContent = `Result after AddOne → AddOne: ${step2}`;
  });
});
