// App.js
// Week 5 - Frontend Frameworks
// Demonstrates: React Router (SPA navigation), useState, useEffect
//
// To run this project:
//   npx create-react-app my-app
//   cd my-app
//   npm install react-router-dom
//   Replace src/App.js with this file, then `npm start`

import React, { useState, useEffect } from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link,
  NavLink,
} from "react-router-dom";

// ---------------------------------------------------------
// Home Page: demonstrates useState + useEffect
// A counter whose value is reflected in both the UI and the
// browser tab's document title.
// ---------------------------------------------------------
function Home() {
  const [count, setCount] = useState(0);

  // useEffect runs after every render where `count` changes.
  // It syncs the counter value with the document title,
  // similar to a componentDidUpdate lifecycle method.
  useEffect(() => {
    document.title = `Count: ${count}`;

    // Optional cleanup function - runs before the next effect
    // or when the component unmounts.
    return () => {
      document.title = "React App";
    };
  }, [count]); // dependency array -> effect re-runs only when count changes

  return (
    <div className="page">
      <h1>Home</h1>
      <p>This page demonstrates the useState and useEffect hooks.</p>
      <p>
        Current count: <strong>{count}</strong>
      </p>
      <button onClick={() => setCount((c) => c + 1)}>Increment</button>
      <button onClick={() => setCount((c) => c - 1)}>Decrement</button>
      <button onClick={() => setCount(0)}>Reset</button>
      <p className="hint">
        Check your browser tab title — it updates with the count!
      </p>
    </div>
  );
}

// ---------------------------------------------------------
// About Page
// ---------------------------------------------------------
function About() {
  return (
    <div className="page">
      <h1>About</h1>
      <p>
        This is a small single-page application (SPA) built with React and
        React Router to demonstrate client-side routing without full page
        reloads.
      </p>
    </div>
  );
}

// ---------------------------------------------------------
// Contact Page
// ---------------------------------------------------------
function Contact() {
  const [submitted, setSubmitted] = useState(false);
  const [name, setName] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmitted(true);
  };

  return (
    <div className="page">
      <h1>Contact</h1>
      {submitted ? (
        <p>Thanks for reaching out, {name || "friend"}!</p>
      ) : (
        <form onSubmit={handleSubmit}>
          <label>
            Name:{" "}
            <input
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          </label>
          <button type="submit">Send</button>
        </form>
      )}
    </div>
  );
}

// ---------------------------------------------------------
// Navigation bar - uses NavLink so the active route can be
// styled differently.
// ---------------------------------------------------------
function NavBar() {
  return (
    <nav className="navbar">
      <NavLink to="/" end>
        Home
      </NavLink>
      <NavLink to="/about">About</NavLink>
      <NavLink to="/contact">Contact</NavLink>
    </nav>
  );
}

// ---------------------------------------------------------
// Root App component - sets up the Router and Routes
// ---------------------------------------------------------
export default function App() {
  return (
    <Router>
      <div className="app">
        <NavBar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
          <Route
            path="*"
            element={
              <div className="page">
                <h1>404</h1>
                <p>Page not found. <Link to="/">Go home</Link></p>
              </div>
            }
          />
        </Routes>
      </div>
    </Router>
  );
}
