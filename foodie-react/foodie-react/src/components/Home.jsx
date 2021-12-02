import React from "react";
import Explore from "./ExploreListings";

function Home() {
  return (
    <div className="home">
      <div class="container-fluid">
        <div class="row my-5">
          <div class="col my-3">
            <form>
                <div class="form-group">
                  <input type="text" class="form-control" id="product_name" placeholder="Search product" />
                </div>
                <div class="form-group">
                  <button type="submit" class="btn btn-success">Vegan</button>
                  <button type="submit" class="btn btn-info mx-2">Veggie</button>
                </div>
              </form>
          </div>
          <div class="col w-50">
            <Explore />
          </div>
          <div class="col my-1">
            <form>
              <div class="form-group">
                <label for="exampleInputEmail1">Add product</label>
                <input type="text" class="form-control" id="product_name" placeholder="Product name" />
                <small id="emailHelp" class="form-text text-muted">Try to be as specific as possible</small>
              </div>
              <div class="form-group">
                <label for="exampleFormControlSelect1">Category</label>
                <select class="form-control" id="category">
                  <option>Cereal</option>
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

export default Home;
