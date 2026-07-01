import { render, screen, fireEvent } from "@testing-library/react";
import { describe, test, expect } from "vitest";
import App from "../App";

describe("App Component", () => {
  test("renders Vite + React text", () => {
    render(<App />);

    expect(screen.getByText(/Vite \+ React/i)).toBeInTheDocument();
  });

  test("increments count on button click", () => {
    render(<App />);

    const button = screen.getByRole("button");

    expect(button).toHaveTextContent("count is 0");

    fireEvent.click(button);
    expect(button).toHaveTextContent("count is 1");

    fireEvent.click(button);
    expect(button).toHaveTextContent("count is 2");
  });
});