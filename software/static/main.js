// Find elements
const root = document.querySelector('div#app-root');
root.innerHTML = bootstrapApp({ title: `It's Lit` });

// boostrap
function bootstrapApp(props) {
  return buildMainTemplate(props);
}

// buidler functions
function buildMainTemplate(props) {
  const { title } = props;

  const header = `<h2>${title}</h2>`;

  return buildBasicGrid(header, '', '');
}

function buildBasicGrid(header, main, footer) {
  return `
    <div class="basic-grid">
      <div class="grid-header">${header}</div>
      <div class="grid-main">${main}</div>
      <div class="grid-footer">${footer}</div>
    </div>
  `;
}
