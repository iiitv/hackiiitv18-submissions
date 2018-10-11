const ADD_IMAGE = '/ADD_IMAGE';
const DELETE_IAMGE = '/DELETE_IAMGE';
const EDIT_IMAGE = '/EDIT_IMAGE';

export function addImage(photo, image) {
  return {
    type: ADD_IMAGE,
    photo,
    image
  };
}

export function deleteImage(id) {
  return {
    type: DELETE_IAMGE,
    id
  };
}

export function editImage(id, postdata) {
  return {
    type: EDIT_IMAGE,
    id,
    postdata
  };
}

export default function reducer(state = { images: {}, imageIds: [] }, action) {
  switch (action.type) {
    case ADD_IMAGE:
      return {
        ...state,
        images: {
          ...state.images,
          [action.photo.nameup]: {
            name: action.photo.name,
            extension: action.photo.type.split('/')[1],
            src: action.image.src,
            description: '',
            tags: '',
            resolution: `${action.image.width} x ${action.image.height}`
          }
        },
        imageIds: [...state.imageIds, action.photo.nameup]
      };

    case DELETE_IAMGE:
      return {
        ...state,
        images: {
          ...state.images,
          [action.id]: {}
        }
      };

    case EDIT_IMAGE:
      return {
        ...state,
        images: {
          ...state.images,
          [action.id]: {
            ...action.postdata
          }
        }
      };
    default:
      return state;
  }
}
