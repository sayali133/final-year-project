import React from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import App from "./App.js";
import { AppProvider } from "./context.js";
import "./assests/css/bootstrap.css";
import "./assests/css/style.css";

const root = createRoot(document.getElementById("root"));

root.render(
  <BrowserRouter>
    <AppProvider>
      <App />
    </AppProvider>
  </BrowserRouter>
);
