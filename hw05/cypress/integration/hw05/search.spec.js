///<reference types='cypress'/>

const locator_searchfield = "[id=idSearchBox]"
const locator_non_existent = '.notfound'

describe('Test search', () => {

    beforeEach(() =>{

        cy.visit('https://list.am/am/');
    })
    it('Item valid 01', () =>  {
        const searchString = "Mercedes"

        cy.get(locator_searchfield).type(searchString+'\n')
        cy.get(locator_non_existent).should('not.exist')
        
    })
    it('Item valid 02', () =>  {
        const searchString = "mercedes գազ"

        cy.get(locator_searchfield).type(searchString+'\n')
        cy.get(locator_non_existent).should('not.exist')
        
    })
    it('Item valid 03', () =>  {
        const searchString = "уроки русского"

        cy.get(locator_searchfield).type(searchString+'\n')
        cy.get(locator_non_existent).should('not.exist')
        
    })
    it('Item valid 04', () => {
        
        const searchString = "mercedes գ"
        cy.get(locator_searchfield).type(searchString+'\n')
        cy.get(locator_non_existent).should('not.exist')
        
    })
    it('Item valid 05', () =>  {
        const searchString = "уроки рус"

        cy.get(locator_searchfield).type(searchString+'\n')
        cy.get(locator_non_existent).should('not.exist')
        
    })
    it('Item valid 06', () =>  {
        const searchString = "IpHoNe"

        cy.get(locator_searchfield).type(searchString+'\n')
        cy.get(locator_non_existent).should('not.exist')
        
    })
    it('Item invalid 01', () =>  {
        const searchString = "անհայտ բաներ"

        cy.get(locator_searchfield).type(searchString+'\n')
        cy.get(locator_non_existent).should('exist')
        
    })
  })
