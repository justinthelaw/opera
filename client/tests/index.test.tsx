// Dependencies
import React from "react";
import { render, screen } from "@testing-library/react";


describe("React and Jest are functioning", () => {
  it("renders HTML correctly using React", () => {
    // Render the App component in a test container
    render(<div>Hello World</div>);

    // Assert that the expected text is rendered
    const textElement = screen.getByText("Hello World");
    expect(textElement).toBeInTheDocument();
  });
});
