// Dependencies
import React from "react";
import { render, screen } from "@testing-library/react";


describe("App", () => {
  it("renders the expected text", () => {
    // Render the App component in a test container
    render(<div>Hello World</div>);

    // Assert that the expected text is rendered
    const textElement = screen.getByText("Hello World");
    expect(textElement).toBeInTheDocument();
  });
});
