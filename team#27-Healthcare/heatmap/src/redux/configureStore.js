import { createStore, applyMiddleware } from 'redux';
import logger from 'redux-logger';
import apiMiddleware from './middleware/apiMiddleware';
import reducers from './combinedReducers';

const configureStore = () =>
  createStore(
    reducers,
    applyMiddleware(apiMiddleware, logger)
    //applyMiddleware(apiMiddleware)
  );

export default configureStore;
