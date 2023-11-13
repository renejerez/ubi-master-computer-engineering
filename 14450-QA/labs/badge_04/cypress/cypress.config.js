const { defineConfig } = require("cypress");

module.exports = defineConfig({
  projectId: 'n6t8mi',
  e2e: {
    experimentalStudio: true,
    //testIsolation:false,
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});
