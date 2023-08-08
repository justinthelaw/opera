describe('App', () => {
    it('loads correctly', () => {
        cy.visit('/')
        cy.contains(/opera/i)
    })
})
