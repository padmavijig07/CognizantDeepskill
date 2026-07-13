import { render, screen } from "@testing-library/react";
import React from "react";

function App() {
  return <h1>Hello Mokitha</h1>;
}

test("React Component Test", () => {
  render(<App />);
  expect(screen.getByText("Hello Mokitha")).toBeInTheDocument();
});

global.fetch = jest.fn(() =>
  Promise.resolve({
    json: () =>
      Promise.resolve({
        name: "Mokitha",
      }),
  })
);

test("Mock API Test", async () => {
  const response = await fetch("/user");
  const data = await response.json();

  expect(data.name).toBe("Mokitha");
});