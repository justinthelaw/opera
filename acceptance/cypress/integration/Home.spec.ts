describe('App', () => {
	it('loads correctly', () => {
		cy.visit('/')
		cy.findByText(/opera/i)
	})
})
