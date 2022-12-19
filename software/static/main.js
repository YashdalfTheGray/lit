const root = document.querySelector('div#app-root');

root.innerHTML = bootstrapApp({ title: `It's Lit` });

function bootstrapApp(props) {
  const { title } = props;
  return title;
}
