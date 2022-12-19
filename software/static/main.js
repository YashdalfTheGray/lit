const root = document.querySelector('div#app-root');

root.innerHTML = bootstrapApp({ title: `It's Lit` });

function getMainTemplate(props) {
  const { title } = props;

  return `
    <h2>${title}</h2>
  `;
}

function bootstrapApp(props) {
  return getMainTemplate(props);
}
