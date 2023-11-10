const { defineConfig } = require("cypress");

module.exports = defineConfig({
  projectId: 'n6t8mi',
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});
