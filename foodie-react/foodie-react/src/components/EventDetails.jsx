import React, { useState } from "react";
import axios from 'axios';
import { useParams } from 'react-router-dom'

function DeleteEvent(id) {
    axios.delete('http://127.0.0.1:8000/events/delete/'+id)
    .then((res) => {
        alert('event deleted');
    })
}

function EventDetails() {

    const { id } = useParams();

    const [fetchedData, setFetchedData] = useState(['yo']);
  
    React.useEffect(() => {
        axios.get('http://127.0.0.1:8000/events/'+id)
        .then((res) => {
            setFetchedData(res.data);
        })
    }, []);

    return (
    <div className="chat">
        <div class="container-fluid">
        <div class="row my-5">
            <div class="col">
            </div>
            <div class="col">
            <div class="card">
            <div class="card-body">
                <h5 class="card-title"> {fetchedData.event_name} </h5>
                <h6 class="card-subtitle mb-2 text-muted">{fetchedData.details}</h6>
                <div class="card-text">
                details of event
                </div>
                <br />
                <button onClick = {() => DeleteEvent(id)}>Delete</button>
            </div>
            </div>
            </div>
            <div class="col">
            </div>
        </div>
        </div>
    </div>
    );
}

export default EventDetails;
