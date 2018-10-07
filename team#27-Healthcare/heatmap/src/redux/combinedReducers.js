import { combineReducers } from 'redux';
import selectedCategory from './reducers/selected_category';
import selectedSort from './reducers/selected_sort';
import images from './reducers/add_image';
import data from './reducers/get_data';

const rootReducer = combineReducers({
  data
});

export default rootReducer;
