describe('App', () => {
	it('loads correctly', () => {
		cy.visit('/')
		cy.findByText(/hello world/i)
	})
})
