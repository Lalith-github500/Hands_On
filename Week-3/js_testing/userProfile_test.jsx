import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import UserProfile from "./userProfile";

describe("UserProfile", () => {
  test("renders user name", () => {
    render(
      <UserProfile
        name="Alice Johnson"
        email="alice@example.com"
      />
    );

    expect(
      screen.getByText("Alice Johnson")
    ).toBeInTheDocument();
  });

  test("renders user email", () => {
    render(
      <UserProfile
        name="Alice Johnson"
        email="alice@example.com"
      />
    );

    expect(
      screen.getByText("alice@example.com")
    ).toBeInTheDocument();
  });

  test("renders both name and email", () => {
    render(
      <UserProfile
        name="Bob Smith"
        email="bob@example.com"
      />
    );

    expect(screen.getByText("Bob Smith")).toBeInTheDocument();
    expect(screen.getByText("bob@example.com")).toBeInTheDocument();
  });
});