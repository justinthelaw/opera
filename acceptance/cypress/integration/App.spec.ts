describe('App', () => {
	it('loads correctly', () => {
		cy.visit('/')
		cy.get('element').should('exist')
	})
})
