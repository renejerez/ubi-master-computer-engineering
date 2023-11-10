{
  "title": "step01",
  "steps": [
      {
          "type": "setViewport",
          "width": 906,
          "height": 961,
          "deviceScaleFactor": 1,
          "isMobile": false,
          "hasTouch": false,
          "isLandscape": false
      },
      {
          "type": "navigate",
          "url": "chrome://new-tab-page/",
          "assertedEvents": [
              {
                  "type": "navigation",
                  "url": "chrome://new-tab-page/",
                  "title": "New Tab"
              }
          ]
      },
      {
          "type": "navigate",
          "url": "https://onpoint-hml.azurewebsites.net/login/simula-excelsior",
          "assertedEvents": [
              {
                  "type": "navigation",
                  "url": "https://onpoint-hml.azurewebsites.net/login/simula-excelsior",
                  "title": ""
              }
          ]
      },
      {
          "type": "click",
          "target": "main",
          "selectors": [
              [
                  "form > span:nth-of-type(1) input"
              ],
              [
                  "xpath///*[@id=\"app\"]/div[2]/div[4]/div/div[2]/div/div/div/span/form/span[1]/div/div/input"
              ],
              [
                  "pierce/form > span:nth-of-type(1) input"
              ]
          ],
          "offsetY": 17.4375,
          "offsetX": 175.796875
      },
      {
          "type": "change",
          "value": "opcao@opcao.com.br",
          "selectors": [
              [
                  "form > span:nth-of-type(1) input"
              ],
              [
                  "xpath///*[@id=\"app\"]/div[2]/div[4]/div/div[2]/div/div/div/span/form/span[1]/div/div/input"
              ],
              [
                  "pierce/form > span:nth-of-type(1) input"
              ]
          ],
          "target": "main"
      },
      {
          "type": "keyDown",
          "target": "main",
          "key": "Tab"
      },
      {
          "type": "keyUp",
          "key": "Tab",
          "target": "main"
      },
      {
          "type": "change",
          "value": "Teste123*",
          "selectors": [
              [
                  "span:nth-of-type(2) input"
              ],
              [
                  "xpath///*[@id=\"app\"]/div[2]/div[4]/div/div[2]/div/div/div/span/form/span[2]/div/div/input"
              ],
              [
                  "pierce/span:nth-of-type(2) input"
              ]
          ],
          "target": "main"
      },
      {
          "type": "click",
          "target": "main",
          "selectors": [
              [
                  "#app span.vs-button-text"
              ],
              [
                  "xpath///*[@id=\"app\"]/div[2]/div[4]/div/div[2]/div/div/div/span/form/button/span[2]"
              ],
              [
                  "pierce/#app span.vs-button-text"
              ],
              [
                  "text/Entrar"
              ]
          ],
          "offsetY": 6.78125,
          "offsetX": 21.5
      },
      {
          "type": "waitForElement",
          "selectors": [
              "aria/Nova proposta",
              "div.grid > button",
              "xpath///*[@id=\"content-area\"]/div[3]/div/div/div/section/div[2]/button",
              "pierce/div.grid > button"
          ]
      }
  ]
}
