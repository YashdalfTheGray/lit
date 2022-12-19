const root = document.querySelector('div#app-root');

root.innerHTML = bootstrapApp({ title: `It's Lit` });

function getBasicGrid(header, main, footer) {
  return `
    <div class="basic-grid">
      <div class="grid-header">${header}</div>
      <div class="grid-main">${main}</div>
      <div class="grid-footer">${footer}</div>
    </div>
  `;
}

function getMainTemplate(props) {
  const { title } = props;

  const header = `<h2>${title}</h2>`;

  return getBasicGrid(header, '', '');
}

function bootstrapApp(props) {
  return getMainTemplate(props);
}
