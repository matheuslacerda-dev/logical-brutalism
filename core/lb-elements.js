/**
 * LOGICAL BRUTALISM :: WEB COMPONENTS (LB-ELEMENTS)
 * Author: Matheus Lacerda Ferreira
 * Description: Extended components from the browser's native API (Vanilla JS).
 * Philosophy: Zero abstraction, maximum semantic integrity.
 */

class LBButton extends HTMLElement {
  connectedCallback() {
    // Apply official parametric style
    this.classList.add('btn');

    // Enforce button semantics and keyboard accessibility
    if (!this.hasAttribute('role')) {
      this.setAttribute('role', 'button');
    }
    if (!this.hasAttribute('tabindex')) {
      this.setAttribute('tabindex', '0');
    }

    // Coherent trigger matching native button behavior
    this.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        this.click();
      }
    });
  }
}

// Register in the browser window scope
customElements.define('lb-button', LBButton);
