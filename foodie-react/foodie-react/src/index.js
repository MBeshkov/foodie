import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import {
  Navigation,
  Footer,
  Home,
  Events,
  Chat,
  Profile,
  ListingDetails,
  EventDetails,
} from "./components";

ReactDOM.render(
  <Router>
    <Navigation />
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/events" element={<Events />} />
      <Route path="/chat" element={<Chat />} />
      <Route path="/profile" element={<Profile />} />
      <Route path="/listingdetails/:id" element={<ListingDetails />} />
      <Route path="/eventdetails/:id" element={<EventDetails />} />
    </Routes>
    <Footer />
  </Router>,

  document.getElementById("root")
);

