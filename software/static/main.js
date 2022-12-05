const root = document.querySelector('div#app-root');

root.innerHTML = bootstrapApp(`It's Lit`);

function bootstrapApp(title) {
  return title;
}
