/**
 * LOGICAL BRUTALISM :: WEB COMPONENTS (LB-ELEMENTS)
 * Author: Matheus Lacerda Ferreira
 * Descrição: Componentes estendidos da API nativa do navegador (Vanilla JS).
 * Filosofia: Zero abstração, máxima integridade semântica.
 */

class LBButton extends HTMLElement {
  connectedCallback() {
    // Aplica o estilo paramétrico oficial
    this.classList.add('btn');
    
    // Força semântica de botão e acessibilidade de teclado
    if (!this.hasAttribute('role')) {
      this.setAttribute('role', 'button');
    }
    if (!this.hasAttribute('tabindex')) {
      this.setAttribute('tabindex', '0');
    }
    
    // Disparo coerente com o comportamento nativo de botões 
    this.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        this.click();
      }
    });
  }
}

// Registro no escopo da janela do navegador
customElements.define('lb-button', LBButton);
