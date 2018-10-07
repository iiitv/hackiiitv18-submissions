const SELECTED_CATEGORY = '/SELECTED_CATEGORY';

export function selectedCategory(category) {
  return {
    type: SELECTED_CATEGORY,
    category
  };
}

export default function reducer(state = { category: '' }, action) {
  switch (action.type) {
    case SELECTED_CATEGORY:
      return {
        category: action.category
      };

    default:
      return state;
  }
}
