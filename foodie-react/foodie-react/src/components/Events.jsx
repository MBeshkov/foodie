import React, { useState } from "react";
import axios from 'axios';
import Explore from "./ExploreEvents";

function CreateEvent(event_name) {
  axios
  .post("http://127.0.0.1:8000/events/create/", {
    event_name: "bro"
  })
  .then((res) => {
      alert('event created');
  });
}

function Events() {

  const [newEvent, setNewEvent] = useState(['default']);

  return (
    <div className="events">
      <div class="container-fluid">
        <div class="row my-5">
          <div class="col my-3">
              <form>
                <div class="form-group">
                  <input type="text" class="form-control" id="product_name" placeholder="Search event" />
                </div>
                <div class="form-group">
                  <button type="submit" class="btn btn-success">Vegan</button>
                  <button type="submit" class="btn btn-info mx-2">Veggie</button>
                </div>
              </form>
          </div>
          <div class="col">
            <Explore />
          </div>
          <div class="col my-1">
            <form onSubmit={CreateEvent(newEvent)}>
              <div class="form-group">
                <label for="exampleInputEmail1">Add event</label>
                <input type="text" class="form-control" name="event_name" id="event_name" placeholder="Product name" value={newEvent}
                  onChange={(event) => {setNewEvent(event.target.value)}} />
                <small id="emailHelp" class="form-text text-muted">Try to be as specific as possible</small>
              </div>
              <div class="form-group">
                <label for="exampleFormControlSelect1">Category</label>
                <select class="form-control" id="category">
                  <option>Communal</option>
                  <option>Dairy products</option>
                  <option>Egg products</option>
                  <option>Fruits</option>
                  <option>Vegetables</option>
                </select>
              </div>
              <button type="submit" class="btn btn-warning">Submit</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Events;
