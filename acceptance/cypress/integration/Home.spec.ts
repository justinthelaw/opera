describe('App', () => {
	it('loads correctly', () => {
		cy.visit('/')
		cy.findByText(/smarter bullets/i)
	})
})
