const GET_ALL = '/GET_ALL';

export function getAll() {
  return {
    type: GET_ALL,
    promise: {
      method: 'GET',
      path: `/get_all`
    }
  };
}

export default function reducer(state = {}, action) {
  switch (action.type) {
    case `${GET_ALL}_REQUEST`:
      return {
        ...state,
        requesting: true
      };
    case `${GET_ALL}_FAILURE`:
      return {
        ...state,
        requesting: false,
        requested: true
      };
    case `${GET_ALL}_SUCCESS`:
      return {
        ...state,
        requesting: false,
        requested: true,
        comment: { ...action.response }
      };
    default:
      return state;
  }
}
