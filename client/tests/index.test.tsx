// Dependencies
import React from "react";
import { render, screen } from "@testing-library/react";


describe("React and Jest Functionality", () => {
  it("Renders JSX HTML and produces the correct text", () => {
    // Render the App component in a test container
    render(<div>Hello World</div>);

    // Assert that the expected text is rendered
    const textElement = screen.getByText("Hello World");
    expect(textElement).toBeInTheDocument();
  });
});
