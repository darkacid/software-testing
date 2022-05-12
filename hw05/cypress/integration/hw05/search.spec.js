///<reference types='cypress'/>

const locator_searchfield = "[id=idSearchBox]"
const searchstring_success = "Mercedes"
const searchstring_failure = "fignya"

describe('Test search', () => {

    beforeEach(() =>{

        cy.visit('https://list.am/am/');
    })
    it('Item found', () => {

        cy.get(locator_searchfield).type(searchstring_success+'\n')
        cy.get("div").contains(searchstring_success).first().should('exist')
        
    })
    it('Item not found', () => {
        
        cy.get(locator_searchfield).type(searchstring_failure+'\n')
        cy.get("div").contains(searchstring_failure).should('not.exist')
        
    })
  })
