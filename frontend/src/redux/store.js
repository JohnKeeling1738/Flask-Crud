import {applyMiddleware, legacy_createStore}from "redux";
import logger from "redux-logger";
import thunk from "redux-thunk";
import rootReducer from "./rootReducer";

const middleware = [thunk];
if(process.env.NODE_ENV === "development"){
    middleware.push(logger);
}

const store = legacy_createStore(rootReducer,applyMiddleware(...middleware))

export default store;