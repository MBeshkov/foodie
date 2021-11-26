import React, { useState } from 'react';
import axios from 'axios';

const ListingsList = () => {

  const [fetchedData, setFetchedData] = useState(['yo']);
  
  React.useEffect(() => {
    axios.get('http://127.0.0.1:8000/listings/')
    .then((res) => {
        setFetchedData(res.data);
    })
  }, []);

  return(
      <div>
          { fetchedData.map( listing => 
          <div class="card">
            <div class="card-body">
              <h5 class="card-title"> {listing.id} </h5>
              <h6 class="card-subtitle mb-2 text-muted">{listing.absolute_url} </h6>
              <div class="card-text">
                {listing.category}
              </div>
            </div>
          </div>
          )}
      </div>
  );
};

const Explore = () => {
  return (
    <ListingsList></ListingsList>
  );
};

export default Explore;