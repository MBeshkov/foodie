import React, { useState } from 'react';
import axios from 'axios';
import { Link } from "react-router-dom";

const Explore = () => {
  const [fetchedData, setFetchedData] = useState(['yo']);
  
  React.useEffect(() => {
    axios.get('http://127.0.0.1:8000/events/')
    .then((res) => {
        res.data.reverse();
        setFetchedData(res.data);
    })
  }, []);

  return(
      <div>
          { fetchedData.map( listing => 
          <Link className="nav-link" to={`/eventdetails/${listing.id}`}>
            <div class="card">
              <div class="card-body">
                <h5 class="card-title"> {listing.event_name} </h5>
                <h6 class="card-subtitle mb-2 text-muted">{listing.category} </h6>
                <div class="card-text">
                  event description
                </div>
              </div>
            </div>
          </Link>
          )}
      </div>
  );
}

export default Explore;