// Type signatures
/**
 * @typedef MainProps
 * @type {object}
 * @property {string} title - the title of the app
 */

// Find elements
const root = document.querySelector('div#app-root');
root.innerHTML = bootstrapApp({ title: `It's Lit` });

// boostrap
function bootstrapApp(props) {
  return buildMainTemplate(props);
}

// buidler functions
/**
 * Builds the main template
 * @param {MainProps} props the props that drive the app
 * @returns {string} the template
 */
function buildMainTemplate(props) {
  return buildBasicGrid(buildHeader(props), '', '');
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

function buildHeader(props) {
  const { title } = props;

  return `
    <div class="header">
      <h2>${title}</h2>
    </div>
  `;
}
