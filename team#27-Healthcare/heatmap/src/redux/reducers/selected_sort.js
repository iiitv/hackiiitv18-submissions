const SELECTED_SORT = '/SELECTED_SORT';

export function selectedSort(sort) {
  return {
    type: SELECTED_SORT,
    sort
  };
}

export default function reducer(state = { sort: '' }, action) {
  switch (action.type) {
    case SELECTED_SORT:
      return {
        sort: action.sort
      };

    default:
      return state;
  }
}
