function includeHeaderFooter(headerPath, footerPath) {
  // Header
  fetch(headerPath)
    .then(res => res.text())
    .then(data => {
      const headerDiv = document.getElementById('header');
      if (headerDiv) headerDiv.innerHTML = data;
    });
  // Footer
  fetch(footerPath)
    .then(res => res.text())
    .then(data => {
      const footerDiv = document.getElementById('footer');
      if (footerDiv) footerDiv.innerHTML = data;
    });
}