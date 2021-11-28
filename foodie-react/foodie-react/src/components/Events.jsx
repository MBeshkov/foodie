import React, { useState } from "react";
import axios from 'axios';
import Explore from "./ExploreEvents";

function CreateEvent(event_name) {
  axios.post("http://127.0.0.1:8000/events/create/", {
    event_name: "bro",
    category: "cmn",
  })
  .then((res) => {
      alert('event created');
  })
}

function Events() {

  const [newEvent, setNewEvent] = useState(['default']);

  return (
    <div className="events">
      <div class="container-fluid">
        <div class="row my-5">
          <div class="col">
          </div>
          <div class="col">
            <Explore />
          </div>
          <div class="col">
            <form onSubmit={CreateEvent(newEvent)}>
              <div>
                <input
                  type="text"
                  name="event_name"
                  value={newEvent}
                  onChange={(event) => {setNewEvent(event.target.value)}} />
              </div>
              <input type="submit" value="Submit" />
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Events;
