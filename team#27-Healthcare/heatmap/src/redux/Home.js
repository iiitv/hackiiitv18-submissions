import React, { Component } from 'react';
import Post from '../components/post';
import { Link } from 'react-router-dom';
import { getAllPosts } from '../redux/reducers/post';
import { deletePost } from '../redux/reducers/delete_post';
import { vote } from '../redux/reducers/edit_post';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import compose from 'recompose/compose';
import { selectedCategory } from '../redux/reducers/selected_category';
import { getCategoryPost } from '../redux/reducers/category_post';
import { selectedSort } from '../redux/reducers/selected_sort';
import {
  RadioGroup,
  Paper,
  FormControlLabel,
  Radio,
  withStyles,
  Button,
  MenuItem,
  TextField
} from '@material-ui/core';

const styles = () => ({
  selector: {
    display: 'flex',
    flexDirection: 'row',
    justifyContent: 'space-around'
  }
});
const sorts = [
  {
    value: 'popular',
    label: 'Popular'
  },
  {
    value: 'unpopular',
    label: 'Unpopular'
  },
  {
    value: 'newest',
    label: 'Newest'
  },
  {
    value: 'oldest',
    label: 'Oldest'
  }
];

class Home extends Component {
  componentWillMount() {
    const { category = '' } = this.props.match.params;
    category
      ? this.props.actions.getCategoryPost(category)
      : this.props.actions.getAllPosts();
  }
  deletePost = postId => {
    this.props.actions.deletePost(postId).then(res => {
      if (res.response.deleted) this.props.actions.getAllPosts();
      else alert('some error occured');
    });
  };
  votePost = (toggle, postId) => {
    this.props.actions
      .vote({ option: toggle }, postId)
      .then(({ response }) => this.props.actions.getAllPosts());
  };
  handleChange = event => {
    if (event.target.value) {
      this.props.actions.selectedCategory(event.target.value);
      this.props.actions.getCategoryPost(event.target.value);
    } else {
      this.props.actions.getAllPosts();
    }
    this.props.history.push(`/${event.target.value}`);
  };
  handleChangeSort = name => event => {
    this.props.actions.selectedSort(event.target.value);
  };
  render() {
    const { classes, post = {} } = this.props;
    const { category = '' } = this.props.match.params;
    const { posts = [] } = post;
    const filtered = category ? this.props.categoryPost : posts;
    if (!posts) return <div />;
    return (
      <div>
        <Paper elevation={5}>
          <RadioGroup
            className={classes.selector}
            value={category}
            onChange={this.handleChange}
          >
            <FormControlLabel value="" control={<Radio />} label="All" />
            <FormControlLabel value="react" control={<Radio />} label="React" />
            <FormControlLabel value="redux" control={<Radio />} label="Redux" />
            <FormControlLabel
              value="udacity"
              control={<Radio />}
              label="Udacity"
            />
            <FormControlLabel
              value="javascript"
              control={<Radio />}
              label="JavaScript"
            />
          </RadioGroup>
        </Paper>
        <Paper
          elevation={5}
          style={{ margin: '2%', padding: '0% 2% 0% 2%', textAlign: 'start' }}
        >
          <TextField
            id="select-sort"
            select
            label="Sort By"
            className={classes.textField}
            value={this.props.selectedSort}
            onChange={this.handleChangeSort('sort')}
            margin="normal"
            style={{ width: '100%' }}
          >
            {sorts.map(option => (
              <MenuItem key={option.value} value={option.value}>
                {option.label}
              </MenuItem>
            ))}
          </TextField>
        </Paper>
        {filtered
          .sort((a, b) => {
            switch (this.props.selectedSort) {
              case 'popular':
                return b.voteScore - a.voteScore;
              case 'unpopular':
                return a.voteScore - b.voteScore;
              case 'newest':
                return b.timestamp - a.timestamp;
              case 'oldest':
                return a.timestamp - b.timestamp;
              default:
                return;
            }
          })
          .map(post => (
            <Post
              key={post.id}
              post={post}
              deletePost={this.deletePost}
              vote={this.votePost}
            />
          ))}
        <Button
          variant="contained"
          style={{
            backgroundColor: 'white',
            color: 'deepskyblue'
          }}
        >
          <Link to="/addpost">Add Post</Link>
        </Button>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  post: state.post,
  selectedCategory: state.selectedCategory.category,
  categoryPost: state.categoryPost.posts,
  selectedSort: state.selectedSort.sort
});

const mapDispatchToProps = dispatch => ({
  actions: bindActionCreators(
    {
      getAllPosts,
      deletePost,
      vote,
      selectedCategory,
      getCategoryPost,
      selectedSort
    },
    dispatch
  ),
  dispatch
});

export default compose(
  withStyles(styles, { name: 'Home' }),
  connect(
    mapStateToProps,
    mapDispatchToProps
  )
)(Home);
