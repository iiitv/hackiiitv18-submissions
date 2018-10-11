const rootUrl = 'http://192.168.137.49:5000';

let token = localStorage.token;
if (!token)
  token = localStorage.token = Math.random()
    .toString(36)
    .substr(-8);

const commonHeaders = {
  // Accept: 'application/json',
  // Authorization: token,
  // 'Content-Type': 'application/json'
  'Access-Control-Allow-Origin': '*'
};
const apiMiddleware = ({ dispatch }) => next => action => {
  const { promise, type, ...rest } = action;
  if (!promise) {
    return next(action);
  }
  next({ type: `${type}_REQUEST`, ...rest });

  const fetchType = {
    headers: new Headers(commonHeaders),
    method: promise.method || 'GET'
  };
  if (promise.postData) {
    const body = JSON.stringify(promise.postData);
    fetchType.body = body;
  }
  return fetch(`${rootUrl}${promise.path}`, fetchType)
    .then(response => {
      // if (response.ok) {
      return response.json().then(data => {
        return { type: `${type}_SUCCESS`, response: data, ...rest };
      });
      // }
      console.log(44, 'fail');
      // return response
      //   .json()
      //   .then(error => ({ type: `${type}_FAILURE`, response: error, ...rest }));
    })
    .then(data => next(data))
    .catch(error => {
      console.error(51, error);
      return next({
        type: `${type}_FAILURE`,
        response: { message: error.message },
        ...rest
      });
    });
};

export default apiMiddleware;
