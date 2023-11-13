beforeEach(() => {
  // URL para todos os casos de teste
  cy.visit('https://onpoint-hml.azurewebsites.net/login/simula-excelsior');
})

it('Criacao da Proposta', () => {
  // Login
  cy.get(':nth-child(1) > .vs-component > .vs-con-input > .vs-inputx').type('opcao@opcao.com.br') // input usuario
    .should('have.value', 'opcao@opcao.com.br'); // validar usuario

  cy.get(':nth-child(2) > .vs-component > .vs-con-input > .vs-inputx').type('Teste123*') // input senha
    .should('have.value', 'Teste123*'); // validar senha

  cy.get('form > .vs-button').click().wait(15000); // entrar


  // Nova Proposta
  cy.get('.nova-proposta-btn').should('be.visible').click();
  cy.wrap('01.265.684/0001-16').as('cnpjTomador'); // input cnpj tomador

  cy.get('@cnpjTomador').then(cnpjTomador => {
    cy.get('.multiselect__placeholder').should('be.visible').type(cnpjTomador);
    cy.get('.option__desc').click().wait(10000);
  });
  cy.get('.wizard-footer-right > .vs-component').click().wait(6000); // confirmar tomador

 /*********************************************/ 
 /*HERE ERROR BETWEEN SERVER AND LOCAL*/
 /*********************************************/ 
 
  /*
    cy.wrap('45.685.872/0001-79').as('cnpjSegurado'); // input cnpj segurado
    cy.get('@cnpjSegurado').then(cnpjSegurado => {
      cy.get('.dados-seguradora > .vx-row > .mt-5 > .multiselect > .multiselect__tags').should('be.visible').type(cnpjSegurado);
      cy.get('.option__desc').click().wait(10000);
    });/*

    /* ==== Generated with Cypress Studio ==== */
    cy.get('#buscar-segurado').clear();
    cy.get('#buscar-segurado').type('45.685.872/0001-79');
    //cy.get('.option__desc > :nth-child(3)').click();
    /* ==== End Cypress Studio ==== */
    cy.get('.dados-seguradora > .vx-row > .mt-5 > .multiselect > .multiselect__tags').should('be.visible');
    cy.get('.option__desc').click().wait(10000);

    cy.get('.wizard-footer-right > .vs-component').click().wait(6000); // confirmar segurado

    cy.get('#vs4__combobox').should('be.visible').click();
    cy.get('#vs4__option-4') // selecionar grupo de modalidades (dropdown)
      .click();
    cy.get('#vs5__combobox').should('be.visible').click();
    cy.get('#vs5__option-5') // selecionar modalidade principal
      .click();
    cy.get('.pl-2 > :nth-child(2) > .w-full').type('1000') // input da importancia segurada
      .should('have.value', '1000'); // validar valor inserido

    cy.get('.pl-3 > :nth-child(2) > .vdp-datepicker > :nth-child(1) > input').click();
    cy.get('[style=""] > div > :nth-child(33)') // inicio da vigencia
      .click(); // data setada para 31/05

    cy.get(':nth-child(3) > :nth-child(2) > .vs-component > .vs-con-input > .vs-inputx').type('120{enter}') // input do prazo em dias
      .should('have.value', 120); // validar o valor inserido

    cy.get(':nth-child(1) > .container-element > :nth-child(2) > .vs-component > .vs-con-input > .vs-inputx').type('123456') // input do numero do edital
      .should('have.value', '123456'); // validar o valor inserido

    cy.get('.px-8 > .flex-row-reverse > .vs-component') // enviar para seguradora
      .click().wait(20000);

    // Emissao
    cy.get('.ml-3').click().wait(4000);
    cy.get('.wizard-footer-right > :nth-child(4)').click();
    cy.get('.vs-checkbox--input:first').click(); // declarar leitura
    cy.get('.termos-aceite-modal > .vs-popup > .vs-popup--content > :nth-child(4) > .vx-col > .button-primary').click(); // emitir*/

})