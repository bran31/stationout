import React from "react";
import logo from "./logo.svg";
import "./App.css";
import Navbarr from "./components/NavBarr";
import Listing from "./components/Listing";

function App() {
  return (
    <div className="App">
      <Navbarr />
      <br />

      <Listing />
    </div>
  );
}

export default App;
