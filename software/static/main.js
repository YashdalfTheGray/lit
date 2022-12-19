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

  return `
    <h2>${title}</h2>
  `;
}

function bootstrapApp(props) {
  return getMainTemplate(props);
}
